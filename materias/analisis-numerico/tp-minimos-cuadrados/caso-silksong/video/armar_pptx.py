"""Arma video/diapositivas-video.pptx con las 18 imágenes de video/diapositivas/ (una por
diapositiva, a pantalla completa) y el texto del guion de cada una en las notas del orador.

Uso: venv/bin/python materias/analisis-numerico/tp-minimos-cuadrados/caso-silksong/video/armar_pptx.py
"""
import re
from pathlib import Path

from pptx import Presentation
from pptx.util import Emu

AQUI = Path(__file__).resolve().parent
guion = (AQUI.parent / "guion-video.md").read_text(encoding="utf-8")
notas = {}
for m in re.finditer(r"\*\*\[D(\d+) · [^\]]*\]\*\*(.*?)(?=\n\*\*\[D\d+ ·|\n## |\n---)", guion, re.S):
    t = re.sub(r"\s+", " ", m.group(2).replace("**", "")).strip()
    notas[int(m.group(1))] = t

prs = Presentation()
prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)  # 16:9
for png in sorted((AQUI / "diapositivas").glob("*.png")):
    n = int(png.name[:2])
    s = prs.slides.add_slide(prs.slide_layouts[6])
    s.shapes.add_picture(str(png), 0, 0, prs.slide_width, prs.slide_height)
    bloque = png.name.split("-")[1].replace("bloque", "Bloque ")
    s.notes_slide.notes_text_frame.text = f"[D{n} · {bloque}] {notas.get(n, '')}"
out = AQUI / "diapositivas-video.pptx"
prs.save(out)
print("✓", out.name, len(prs.slides), "diapositivas;", len(notas), "con notas")
