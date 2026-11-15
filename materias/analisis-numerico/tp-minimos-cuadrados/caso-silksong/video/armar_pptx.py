"""Arma video/diapositivas-video.pptx con las 18 imágenes de video/diapositivas/ (una por
diapositiva, a pantalla completa) y una segunda versión con el texto del guion de cada una
en las notas del orador.

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



def armar(nombre: str, con_notas: bool) -> None:
    prs = Presentation()
    prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)  # 16:9
    for png in sorted((AQUI / "diapositivas").glob("*.png")):
        n = int(png.name[:2])
        s = prs.slides.add_slide(prs.slide_layouts[6])
        s.shapes.add_picture(str(png), 0, 0, prs.slide_width, prs.slide_height)
        if con_notas:
            bloque = png.name.split("-")[1].replace("bloque", "Bloque ")
            s.notes_slide.notes_text_frame.text = f"[D{n} · {bloque}] {notas.get(n, '')}"
    prs.save(AQUI / nombre)
    print("✓", nombre, len(prs.slides), "diapositivas")


# Keynote rechaza las notas que escribe python-pptx ("the file format is invalid"), así que
# el archivo principal va sin notas y el que las tiene queda aparte.
armar("diapositivas-video.pptx", con_notas=False)
armar("diapositivas-video-con-notas.pptx", con_notas=True)
