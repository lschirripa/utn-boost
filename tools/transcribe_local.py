"""Transcribe un video/audio LOCAL con Whisper (MLX, Apple Silicon) y emite el
mismo JSON que ``dump_transcript.py``, para que ``/apunte`` funcione igual que
con YouTube.

Pensado para clases que no están en YouTube (SharePoint/Stream, Zoom, mp4
descargados): el audio se extrae con ffmpeg y se transcribe en la Mac, sin
subir nada a ningún servicio.

Uso:
    venv/bin/python tools/transcribe_local.py "ruta/clase.mp4"
    venv/bin/python tools/transcribe_local.py "ruta/clase.mp4" --title "Sistemas estables (teórica)" \
        --out materias/x/eval/apuntes/transcripts/05-sistemas-estables.json \
        --prompt "Fourier, Laplace, transformada Z, polos, ceros"

Salida (stdout o --out): {video_id, title, url, suggested_path, contents}, con
``contents`` en el formato de siempre: marcadores ``[mm:ss|Ns]`` cada 30 s.
Como no hay URL pública, la "plantilla de enlace" apunta al archivo local y los
timestamps se citan como texto (mm:ss), sin link.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
import time
from pathlib import Path

DEFAULT_MODEL = "mlx-community/whisper-large-v3-turbo"
TIMESTAMP_INTERVAL_SECONDS = 30.0


def slugify(value: str, *, max_length: int = 80) -> str:
    value = value.strip()
    value = re.sub(r"[^\w\s-]", "", value, flags=re.UNICODE)
    value = re.sub(r"[\s_-]+", "-", value).strip("-")
    return (value[:max_length].rstrip("-") or "apunte").lower()


def format_hms(seconds: float) -> str:
    total = int(seconds)
    hours, remainder = divmod(total, 3600)
    minutes, secs = divmod(remainder, 60)
    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"
    return f"{minutes:02d}:{secs:02d}"


def render_transcript(segments: list[dict], interval: float = TIMESTAMP_INTERVAL_SECONDS) -> str:
    """Igual que extract_notes.render_transcript: marcador cada ``interval`` s."""
    parts: list[str] = []
    next_marker = 0.0
    for seg in segments:
        text = (seg.get("text") or "").strip()
        if not text:
            continue
        start = float(seg["start"])
        if start >= next_marker:
            parts.append(f"[{format_hms(start)}|{int(start)}s]")
            next_marker = start + interval
        parts.append(text)
    return re.sub(r"[ \t]+", " ", " ".join(parts)).strip()


def drop_hallucinated_repeats(segments: list[dict], max_repeats: int = 3) -> list[dict]:
    """Whisper a veces repite la misma frase en silencios largos: se cortan las
    repeticiones consecutivas por encima de ``max_repeats``."""
    out: list[dict] = []
    run_text, run_len = None, 0
    for seg in segments:
        text = (seg.get("text") or "").strip().lower()
        if text == run_text:
            run_len += 1
            if run_len > max_repeats:
                continue
        else:
            run_text, run_len = text, 1
        out.append(seg)
    return out


def extract_audio(media: Path, wav: Path) -> None:
    subprocess.run(
        ["ffmpeg", "-nostdin", "-loglevel", "error", "-y", "-i", str(media),
         "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", str(wav)],
        check=True,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("media", type=Path, help="Archivo de video/audio local.")
    parser.add_argument("--title", help="Título de la clase (default: nombre del archivo).")
    parser.add_argument("--out", type=Path, help="Escribir el JSON acá en vez de stdout.")
    parser.add_argument("--lang", default="es", help="Idioma del audio (default: es).")
    parser.add_argument("--model", default=DEFAULT_MODEL, help=f"Modelo MLX (default: {DEFAULT_MODEL}).")
    parser.add_argument(
        "--prompt",
        default="",
        help="Vocabulario de la materia para orientar a Whisper (términos técnicos, nombres).",
    )
    parser.add_argument(
        "--out-dir", type=Path, default=Path("apuntes"),
        help="Directorio sugerido para el .md (solo informativo).",
    )
    args = parser.parse_args(argv)

    media: Path = args.media
    if not media.exists():
        print(f"Error: no existe {media}", file=sys.stderr)
        return 1

    import mlx_whisper  # import diferido: tarda en cargar

    title = args.title or media.stem
    t0 = time.time()
    with tempfile.TemporaryDirectory() as tmp:
        wav = Path(tmp) / "audio.wav"
        extract_audio(media, wav)
        result = mlx_whisper.transcribe(
            str(wav),
            path_or_hf_repo=args.model,
            language=args.lang,
            initial_prompt=args.prompt or None,
            condition_on_previous_text=False,  # evita bucles de repetición en clases largas
            verbose=None,
        )

    segments = drop_hallucinated_repeats(result.get("segments", []))
    if not segments:
        print("Error: la transcripción quedó vacía.", file=sys.stderr)
        return 1

    transcript = render_transcript(segments)
    contents = (
        f"Archivo local (sin enlace público; citar timestamps como texto mm:ss): {media}\n\n"
        f"Transcripción:\n{transcript}"
    )
    slug = slugify(title)
    out = {
        "video_id": slugify(media.stem),
        "title": title,
        "url": str(media),
        "suggested_path": str(args.out_dir / f"{slug}.md"),
        "contents": contents,
        "source": "local-whisper",
        "model": args.model,
        "duration_s": round(float(segments[-1]["end"]), 1),
        "elapsed_s": round(time.time() - t0, 1),
    }
    payload = json.dumps(out, ensure_ascii=False, indent=2) + "\n"
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(payload, encoding="utf-8")
        print(f"✓ {args.out} ({out['duration_s']/60:.0f} min de audio en {out['elapsed_s']/60:.1f} min)",
              file=sys.stderr)
    else:
        sys.stdout.write(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
