"""Arma video/diapositivas-video-editable.pptx: las 18 diapositivas del video con texto, tablas
y tarjetas editables (para subir a Google Slides). Los gráficos y las fórmulas van como imagen.
El texto de cada diapositiva del guion va en las notas del orador.

Coordenadas en px sobre un lienzo de 1920x1080 (1 px = 6350 EMU = 0,5 pt).
Uso: venv/bin/python materias/analisis-numerico/tp-minimos-cuadrados/caso-silksong/video/armar_pptx_editable.py
"""
import re
from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Emu, Pt

AQUI = Path(__file__).resolve().parent
PX = 6350
INK, SOFT, PAPER, WHITE, LINE, TINT, RED = "262624", "5E5C55", "FAF8F4", "FFFFFF", "E4DFD5", "EFEAE1", "A8243A"
DARK, LIGHT = "1F1B24", "FFF6F2"
SG, IN = "Space Grotesk", "Inter"
# estilo: (fuente, pt, negrita, color)
ST = {
    "eyebrow": (IN, 12, True, RED), "title": (SG, 29, True, INK),
    "lab": (IN, 12, True, SOFT), "k": (SG, 17, True, INK), "t": (IN, 14, False, SOFT),
    "t2": (IN, 16, False, INK), "eq": (IN, 15, False, INK), "num": (SG, 20, True, INK),
    "big": (SG, 56, True, RED), "big3": (SG, 42, True, INK), "huge": (SG, 100, True, RED),
    "cell": (IN, 14, False, INK), "cellh": (IN, 14, True, INK), "pill": (IN, 12, True, RED),
}
L, T, W, H = 96, 336, 1728, 680

guion = (AQUI.parent / "guion-video.md").read_text(encoding="utf-8")
NOTAS = {int(m.group(1)): re.sub(r"\s+", " ", m.group(2).replace("**", "")).strip()
         for m in re.finditer(r"\*\*\[D(\d+) · [^\]]*\]\*\*(.*?)(?=\n\*\*\[D\d+ ·|\n## |\n---)", guion, re.S)}

prs = Presentation()
prs.slide_width, prs.slide_height = Emu(1920 * PX), Emu(1080 * PX)


def rgb(h):
    return RGBColor.from_string(h)


def fmt_run(r, style, color=None):
    f, pt, b, c = ST[style]
    r.font.name, r.font.size, r.font.bold = f, Pt(pt), b
    r.font.color.rgb = rgb(color or c)


def fill_tf(tf, paras, color=None, align=None, anchor=MSO_ANCHOR.TOP, inset=(0, 0)):
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Emu(inset[0] * PX)
    tf.margin_top = tf.margin_bottom = Emu(inset[1] * PX)
    for i, para in enumerate(paras):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        runs = [(para[1], para[0])] if isinstance(para, tuple) else para
        for text, style in runs:
            fmt_run(p.add_run(), style, color)
            p.runs[-1].text = text
        p.space_after = Pt(5)
        if align:
            p.alignment = align


def text(s, x, y, w, h, paras, **kw):
    tb = s.shapes.add_textbox(Emu(x * PX), Emu(y * PX), Emu(w * PX), Emu(h * PX))
    fill_tf(tb.text_frame, paras, **kw)
    return tb


def card(s, x, y, w, h, paras=(), fill=WHITE, line=LINE, color=None, anchor=MSO_ANCHOR.TOP, align=None, radius=20):
    sh = s.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Emu(x * PX), Emu(y * PX), Emu(w * PX), Emu(h * PX))
    sh.adjustments[0] = radius / min(w, h)
    sh.fill.solid()
    sh.fill.fore_color.rgb = rgb(fill)
    if line:
        sh.line.color.rgb = rgb(line)
        sh.line.width = Pt(1)
    else:
        sh.line.fill.background()
    sh.shadow.inherit = False
    if paras:
        fill_tf(sh.text_frame, list(paras), color=color, anchor=anchor, align=align or PP_ALIGN.LEFT, inset=(34, 26))
    return sh


def img(s, nombre, x, y, w, h):
    """Imagen centrada y ajustada dentro de la caja (x, y, w, h)."""
    p = AQUI / nombre
    iw, ih = Image.open(p).size
    k = min(w / iw, h / ih)
    pw, ph = iw * k, ih * k
    s.shapes.add_picture(str(p), Emu(int((x + (w - pw) / 2) * PX)), Emu(int((y + (h - ph) / 2) * PX)),
                         Emu(int(pw * PX)), Emu(int(ph * PX)))


def fig(s, nombre, x, y, w, h):
    card(s, x, y, w, h)
    img(s, nombre, x + 16, y + 16, w - 32, h - 32)


def table(s, x, y, w, rows, widths, row_h=56, sum_row=False):
    gf = s.shapes.add_table(len(rows), len(rows[0]), Emu(x * PX), Emu(y * PX), Emu(w * PX), Emu(row_h * len(rows) * PX))
    t = gf.table
    gf._element.graphic.graphicData.tbl.tblPr.find(
        "{http://schemas.openxmlformats.org/drawingml/2006/main}tableStyleId").text = "{5940675A-B579-460E-94D1-54222C63F5DA}"
    t.first_row = t.horz_banding = False
    for j, fr in enumerate(widths):
        t.columns[j].width = Emu(int(w * fr * PX))
    for i, row in enumerate(rows):
        t.rows[i].height = Emu(row_h * PX)
        for j, val in enumerate(row):
            c = t.cell(i, j)
            c.vertical_anchor = MSO_ANCHOR.MIDDLE
            c.margin_left = c.margin_right = Emu(14 * PX)
            c.margin_top = c.margin_bottom = Emu(4 * PX)
            c.fill.solid()
            c.fill.fore_color.rgb = rgb(TINT if (i == 0 or (sum_row and i == len(rows) - 1)) else WHITE)
            p = c.text_frame.paragraphs[0]
            r = p.add_run()
            r.text = str(val)
            fmt_run(r, "cellh" if i == 0 else "cell")


def nueva(n, eyebrow, titulo=None, bg=PAPER, cam=TINT, eyec=RED, titc=INK):
    s = prs.slides.add_slide(prs.slide_layouts[6])
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = rgb(bg)
    # Recuadro donde el que edita el video pone la cámara del que habla (se puede borrar).
    c = card(s, 1408, 56, 448, 252, [("lab", "CÁMARA DEL QUE HABLA")], fill=cam, line=None,
             color=eyec if bg != PAPER else SOFT, anchor=MSO_ANCHOR.MIDDLE, align=PP_ALIGN.CENTER)
    c.name = "Recuadro cámara"
    text(s, L, 72, 1220, 34, [("eyebrow", eyebrow)], color=eyec)
    if titulo:
        text(s, L, 112, 1240, 150, [("title", titulo)], color=titc)
    s.notes_slide.notes_text_frame.text = f"[D{n}] {NOTAS.get(n, '')}"
    return s


E1, E2, E3 = "1 · EL CASO Y LOS DATOS", "2 · EL MÉTODO", "3 · LOS OTROS DOS MODELOS"
E4, E5 = "4 · COMPARACIÓN Y ELECCIÓN", "5 · CONFIABILIDAD Y CONCLUSIÓN"
MID = MSO_ANCHOR.MIDDLE

# 1 portada
s = nueva(1, "ANÁLISIS NUMÉRICO · K3572 · 2C 2026 · UTN FRBA", bg=DARK, cam="322C39", eyec="F0A9B5")
text(s, L, 500, 1700, 120, [[("Predicción de jugadores en Steam", "title")]], color="F6F1EA")
s.shapes[-1].text_frame.paragraphs[0].runs[0].font.size = Pt(48)
text(s, L, 640, 1700, 60, [("t2", "El caso Hollow Knight: Silksong · Aproximación discreta por mínimos cuadrados")], color="D9D0DC")
s.shapes[-1].text_frame.paragraphs[0].runs[0].font.size = Pt(18)
text(s, L, 960, 1700, 50, [("t", "Marotti · Iglesias Basso · Juliano · Gallegos · Schirripa")], color="D9D0DC")

# 2 idea
s = nueva(2, E1, "La idea original era GTA VI")
card(s, L, 336, 600, 196, [("k", "GTA VI sale solo en consolas"), ("t", "No va a tener datos en Steam para comparar.")])
card(s, L, 556, 600, 218, [("k", "La curva de GTA V no es una caída"), ("t", "Cada actualización del modo online la vuelve a subir.")])
card(s, L, 798, 600, 218, [("k", "Por eso: Hollow Knight: Silksong"), ("t", "Lanzamiento grande (sept. 2025) y sin modo online.")], fill=RED, line=None, color=LIGHT)
fig(s, "graficos/silksong-vs-gta-v.png", 732, T, 1092, H)

# 3 datos
s = nueva(3, E1, "Los datos: SteamCharts, 14 meses")
card(s, L, 336, 760, 250, [("lab", "QUÉ ES y"), ("k", "Promedio de jugadores simultáneos por mes"), ("t", "No cuántos lo jugaron: cuántos estaban jugando al mismo tiempo.")])
card(s, L, 610, 760, 190, [("lab", "QUÉ ES x"), ("t2", "Mes desde el lanzamiento: 1 = sept. 2025 … 14 = oct. 2026")])
card(s, L, 824, 760, 192, [("k", "Queremos estimar x = 15: noviembre de 2026")], fill=RED, line=None, color=LIGHT, anchor=MID)
card(s, 892, T, 932, H)
meses = ["sept. 2025", "oct. 2025", "nov. 2025", "dic. 2025", "ene. 2026", "feb. 2026", "mar. 2026", "abr. 2026",
         "may. 2026", "jun. 2026", "jul. 2026", "ago. 2026", "sept. 2026", "oct. 2026"]
ys = ["191.124", "58.328", "23.721", "17.001", "16.126", "10.613", "8.269", "7.515", "6.967", "7.111", "8.619", "7.972", "7.116", "6.108"]
for k, x0 in ((0, 932), (7, 1378)):
    table(s, x0, 452, 406, [["Mes", "x", "y"]] + [[meses[i], i + 1, ys[i]] for i in range(k, k + 7)], [0.46, 0.16, 0.38])

# 4 nube
s = nueva(4, E1, "La nube de puntos: cae fuerte y después se frena")
fig(s, "graficos/nube.png", L, T, 940, H)
card(s, 1072, 336, 752, 240, [("big", "−69 %"), ("t", "de jugadores del mes 1 al mes 2")])
card(s, 1072, 600, 752, 216, [("k", "Después, una cola que baja muy despacio"), ("t", "Desde el mes 7: entre 6.000 y 9.000 jugadores")])
card(s, 1072, 840, 752, 176, [("k", "Probamos modelos que caen y se van frenando")], fill=TINT, line=None, anchor=MID)

# 5 tres modelos
s = nueva(5, E2, "Tres modelos, un mismo truco")
for i, (nom, col, f, d) in enumerate((("Exponencial", "1BAF7A", "f-exp", "Cada mes se va el mismo porcentaje"),
                                      ("Potencial", "EDA100", "f-pot", "Cada mes se va un porcentaje menor"),
                                      ("Recíproco", "E87BA4", "f-rec", "Baja como 1/x hacia un piso"))):
    x = L + i * 588
    card(s, x, 336, 552, 520)
    card(s, x + 34, 366, 484, 10, fill=col, line=None, radius=5)
    text(s, x + 34, 396, 484, 50, [("k", nom)])
    img(s, f"formulas/{f}.png", x + 34, 500, 484, 150)
    text(s, x + 34, 770, 484, 60, [("t", d)])
card(s, L, 880, W, 136, [("k", "Ninguno es una recta: con un cambio de variables los disfrazamos de recta")], fill=RED, line=None, color=LIGHT, anchor=MID)

# 6 cambio de variables
s = nueva(6, E2, "El potencial, disfrazado de recta")
pasos = (("PASO 1", "El modelo", None, "f-pot", 297), ("PASO 2", "Logaritmo natural a los dos lados", None, "pot-2", 581),
         ("PASO 3", "Renombramos y queda una recta", "Y = ln y · X = ln x · A₀ = ln a₀", "pot-3", 414))
for i, (lab, k, t, f, fw) in enumerate(pasos):
    y = 336 + i * 235
    card(s, L, y, W, 210)
    text(s, L + 40, y + (40 if t else 58), 740, 150, [("lab", lab), ("k", k)] + ([("t", t)] if t else []))
    img(s, f"formulas/{f}.png", L + 840, y + 60, fw, 90)

# 7 sistema
s = nueva(7, E2, "Desde ahí, mínimos cuadrados de una recta común")
card(s, L, T, 960, H, [("lab", "TABLA DE SUMATORIAS (14 MESES)")])
table(s, L + 34, 410, 892, [["x", "y", "X = ln x", "Y = ln y", "X²", "X·Y"],
                            [1, "191.124", "0", "12,1607", "0", "0"], [2, "58.328", "0,6931", "10,9738", "0,4805", "7,6065"],
                            [3, "23.721", "1,0986", "10,0741", "1,2069", "11,0675"], ["…"] * 6,
                            [14, "6.108", "2,6391", "8,7174", "6,9646", "23,0056"],
                            ["Σ", "376.590", "25,1912", "133,2038", "53,1185", "230,1661"]],
      [0.1, 0.18, 0.18, 0.18, 0.18, 0.18], sum_row=True)
card(s, 1092, 336, 732, 250, [("lab", "SISTEMA DE ECUACIONES NORMALES"), ("eq", "14·A₀ + 25,1912·a₁ = 133,2038"), ("eq", "25,1912·A₀ + 53,1185·a₁ = 230,1661")])
card(s, 1092, 610, 732, 406, [("lab", "LO RESOLVEMOS (REGLA DE CRAMER)"), ("k", "A₀ = 11,7129"), ("k", "a₁ = −1,2217")], fill=TINT, line=None, anchor=MID)

# 8, 9, 10: un modelo por diapositiva
def modelo(n, eyebrow, titulo, lab1, f1, lab2, f2, graf):
    s = nueva(n, eyebrow, titulo)
    for x, lab, f in ((L, lab1, f1), (978, lab2, f2)):
        card(s, x, 336, 846, 170, [("lab", lab)])
        img(s, f"formulas/{f}.png", x + 34, 396, 660, 76)
        # alinear la fórmula a la izquierda de la tarjeta
        pic = s.shapes[-1]
        pic.left = Emu((x + 34) * PX)
    fig(s, f"graficos/{graf}.png", L, 530, W, 486)


modelo(8, E2, "Ojo: A₀ no es a₀, hay que volver", "VOLVEMOS AL PARÁMETRO ORIGINAL", "pot-a0", "FUNCIÓN APROXIMANTE", "pot-fn", "modelo-potencial-doble")
modelo(9, E3, "Exponencial: logaritmo solo de y", "CAMBIO DE VARIABLES: Y = ln y, LA x QUEDA IGUAL", "exp-cambio", "FUNCIÓN APROXIMANTE", "exp-fn", "modelo-exponencial-doble")
modelo(10, E3, "Recíproco: sin logaritmos ni vuelta", "CAMBIO DE VARIABLES: SOLO CAMBIA LA x", "rec-cambio", "FUNCIÓN APROXIMANTE", "rec-fn", "modelo-reciproco-doble")

# 11 comparación
s = nueva(11, E4, "¿Cuál es el mejor? Miramos el error cuadrático")
cols = (L + 34, L + 350, L + 1010, L + 1400)
for x, t in zip(cols, ("MODELO", "FUNCIÓN APROXIMANTE", "ERROR CUADRÁTICO E", "ESTIMACIÓN ŷ(15)")):
    text(s, x, 340, 420, 34, [("lab", t)])
for i, (nom, f, e, y15, hl) in enumerate((("Recíproco", "rec-fn", "1,82 × 10⁹", "−4.574", True),
                                          ("Potencial", "pot-fn", "4,93 × 10⁹", "4.467", False),
                                          ("Exponencial", "exp-fn", "2,13 × 10¹⁰", "3.182", False))):
    y = 386 + i * 140
    c = card(s, L, y, W, 116, line=RED if hl else LINE)
    if hl:
        c.line.width = Pt(2.5)
    text(s, cols[0], y + 34, 300, 50, [("k", nom)])
    img(s, f"formulas/{f}.png", cols[1], y + 26, 520, 64)
    s.shapes[-1].left = Emu(cols[1] * PX)
    text(s, cols[2], y + 30, 240, 56, [("num", e)])
    if hl:
        card(s, cols[2] + 215, y + 36, 140, 44, [("lab", "el menor")], fill=RED, line=None, color=LIGHT, anchor=MID, align=PP_ALIGN.CENTER, radius=22)
        s.shapes[-1].text_frame.margin_left = s.shapes[-1].text_frame.margin_right = 0
        s.shapes[-1].text_frame.margin_top = s.shapes[-1].text_frame.margin_bottom = 0
    text(s, cols[3], y + 30, 280, 56, [("num", y15)])
text(s, L, 820, W, 50, [("t", "E = suma de (dato real − modelo)², medido en jugadores, con los 14 meses")])

# 12 recíproco negativo
s = nueva(12, E4, "El de menor error predice jugadores negativos")
fig(s, "graficos/comparacion-cola.png", L, T, 1000, H)
card(s, 1132, 336, 692, 236, [("lab", "RECÍPROCO: JUGADORES EN NOVIEMBRE"), ("big", "−4.574")])
card(s, 1132, 596, 692, 186, [("k", "Negativo desde el mes 12"), ("t", "Ese mes hubo 7.972 jugadores reales")])
card(s, 1132, 806, 692, 210, [("k", "¿Por qué tiene poco error?"), ("t", "Copia muy bien el mes 1 (191.124), que pesa más que todo el resto")], fill=TINT, line=None)

# 13 elección
s = nueva(13, E4, "Elegimos en dos pasos")
card(s, L, 336, 846, 460, [("pill", "PASO 1"), ("k", "Descartar lo que no tiene sentido con el fenómeno"), ("t", "Los jugadores no pueden ser negativos"), ("t2", "Recíproco: descartado")])
card(s, 978, 336, 846, 460, [("pill", "PASO 2"), ("k", "Entre los que quedan, el de menor error"), ("t", "Potencial: 4,93 × 10⁹ · Exponencial: 2,13 × 10¹⁰"), ("t2", "Potencial: 4 veces menos error")])
card(s, L, 820, W, 196, [("lab", "JUGADORES QUE SE VAN DE UN MES AL OTRO: CADA VEZ MENOS, COMO SUPONE EL POTENCIAL"),
                         [("69 % ", "num"), ("del mes 1 al 2      ", "t"), ("28 % ", "num"), ("del 3 al 4      ", "t"), ("7 % ", "num"), ("del 8 al 9", "t")]],
     fill=TINT, line=None, anchor=MID)

# 14 estimación
s = nueva(14, E4, "La estimación para noviembre de 2026")
card(s, L, T, W, H)
text(s, L, 450, W, 40, [("lab", "REEMPLAZAMOS x = 15 EN EL MODELO POTENCIAL")], align=PP_ALIGN.CENTER)
img(s, "formulas/est.png", L, 510, W, 92)
text(s, 400, 640, 700, 230, [("huge", "4.467")], align=PP_ALIGN.RIGHT)
text(s, 1130, 705, 520, 140, [("t2", "jugadores simultáneos promedio en noviembre de 2026")])

# 15 confiabilidad
s = nueva(15, E5, "¿Es confiable? El modelo se queda corto")
card(s, L, T, 400, H, [("lab", "A FAVOR"), ("k", "Predecimos un solo mes hacia adelante"), ("t", "Exponencial y potencial coinciden en el orden: 3.182 y 4.467")])
card(s, 532, T, 628, H, [("lab", "EN CONTRA: ÚLTIMOS 4 MESES")])
table(s, 566, 410, 560, [["Mes", "Real", "Modelo", "Dif."], [11, "8.619", "6.525", "−24 %"], [12, "7.972", "5.867", "−26 %"],
                         [13, "7.116", "5.320", "−25 %"], [14, "6.108", "4.860", "−20 %"]], [0.19, 0.27, 0.28, 0.26], row_h=60)
text(s, 566, 730, 560, 90, [("t", "El modelo queda 20 a 26 % por debajo")])
card(s, 1196, T, 628, H, [("lab", "PRUEBA: AJUSTAR CON 11 MESES")])
table(s, 1230, 410, 560, [["Mes", "Real", "Predijo", "Error"], [12, "7.972", "4.787", "−40 %"], [13, "7.116", "4.291", "−40 %"],
                          [14, "6.108", "3.878", "−37 %"]], [0.19, 0.27, 0.28, 0.26], row_h=60)
text(s, 1230, 670, 560, 90, [("t", "También se quedó corto")])

# 16 rango
s = nueva(16, E5, "Entonces, ¿cuánto esperamos para noviembre?")
card(s, L, 336, 500, 540, [("lab", "LO QUE DA EL MODELO"), ("big3", "4.467"), ("t", "Lo tomamos como un piso")], anchor=MID)
card(s, 632, 336, 656, 540, [("lab", "SI SE VUELVE A QUEDAR 20 A 26 % CORTO"), ("big3", "5.600–6.000"), ("t", "El rango que esperamos")], fill=RED, line=None, color=LIGHT, anchor=MID)
card(s, 1324, 336, 500, 540, [("lab", "STEAMCHARTS, ÚLTIMOS 30 DÍAS"), ("big3", "5.702"), ("t", "Al 11 de noviembre: dentro del rango")], anchor=MID)
card(s, L, 900, W, 116, [("t2", "El dato completo de noviembre sale el 1 de diciembre de 2026.")], fill=TINT, line=None, anchor=MID)

# 17 GTA
s = nueva(17, E5, "El modelo supone que no pasa nada nuevo")
fig(s, "graficos/silksong-vs-gta-v.png", L, T, 1100, H)
card(s, 1232, 336, 592, 328, [("k", "GTA V cayó igual que Silksong…"), ("t", "…y volvió a subir con las actualizaciones de su modo online")], anchor=MID)
card(s, 1232, 688, 592, 328, [("lab", "PARA QUÉ LE SIRVE A UN ESTUDIO"), ("k", "Muestra qué pasa si no hace nada"), ("t", "Así decide cuándo sacar una oferta o una expansión")], fill=RED, line=None, color=LIGHT, anchor=MID)

# 18 conclusión
s = nueva(18, E5, bg=RED, cam="8C1C30", eyec="FFD9DE")
text(s, L, 440, 1700, 240, [("title", "El menor error no alcanza: el modelo tiene que tener sentido.")], color=LIGHT)
s.shapes[-1].text_frame.paragraphs[0].runs[0].font.size = Pt(46)
text(s, L, 720, 1700, 60, [("t2", "Estimamos 4.467 jugadores para noviembre de 2026 y esperamos entre 5.600 y 6.000.")], color="FFE4E7")
s.shapes[-1].text_frame.paragraphs[0].runs[0].font.size = Pt(17)
text(s, L, 960, 1700, 50, [("t", "Gracias · Marotti · Iglesias Basso · Juliano · Gallegos · Schirripa")], color="FFE4E7")

out = AQUI / "diapositivas-video-editable.pptx"
prs.save(out)
print("✓", out.name, len(prs.slides), "diapositivas")
