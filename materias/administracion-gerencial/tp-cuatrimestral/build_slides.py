#!/usr/bin/env python3
"""Genera el deck del TP cuatrimestral de AG (JPMorgan Chase) con python-pptx.

Cada slide calca una sección de la PLANTILLA OFICIAL del enunciado (mismos títulos, mismas
tablas y los mismos rótulos de campo), porque la consigna exige respetar esa estructura.
Salida: exports/00_TP Cuatrimestral_Gx.pptx  (después se sube a Drive y se convierte a Slides).
Contenido canónico en borrador.md: si se cambia uno, cambiar el otro.
Uso: python3 build_slides.py [--grupo B]
"""
import argparse
import os
from lxml import etree
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.oxml.ns import qn

NAVY = RGBColor(0x14, 0x21, 0x3D)
GOLD = RGBColor(0xC9, 0xA2, 0x27)
GOLD_LIGHT = RGBColor(0xF6, 0xEC, 0xCB)
TINT = RGBColor(0xEE, 0xF1, 0xF7)
TINT2 = RGBColor(0xDD, 0xE3, 0xEE)
RED_LIGHT = RGBColor(0xF8, 0xD7, 0xD3)
RED = RGBColor(0xA4, 0x3A, 0x2E)
WHITE = RGBColor(0xFF, 0xFF, 0xFF)
GRAY = RGBColor(0x5F, 0x6B, 0x7A)
BLACK = RGBColor(0x1A, 0x1A, 0x1A)
LINE = "B8C0CC"          # borde de celda (gris, como la planilla)
HEAD = "Cambria"
BODY = "Calibri"

W, H = 13.333, 7.5


def rgb(shape, color):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color


def no_line(shape):
    shape.line.fill.background()


def text(slide, x, y, w, h, s, size=14, bold=False, color=BLACK, font=BODY,
         align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP, italic=False, margin=0.05):
    tb = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    for m in ("margin_left", "margin_right", "margin_top", "margin_bottom"):
        setattr(tf, m, Inches(margin))
    lines = s if isinstance(s, list) else [s]
    for i, line in enumerate(lines):
        p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        p.alignment = align
        runs = line if isinstance(line, list) else [(line, bold)]
        for t, b in runs:
            r = p.add_run()
            r.text = t
            r.font.size = Pt(size)
            r.font.bold = b
            r.font.italic = italic
            r.font.color.rgb = color
            r.font.name = font
    return tb


def box(slide, x, y, w, h, fill, s=None, size=12, bold=False, color=BLACK,
        shape=MSO_SHAPE.RECTANGLE, align=PP_ALIGN.CENTER, line=None, font=BODY):
    sh = slide.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
    rgb(sh, fill)
    if line is None:
        no_line(sh)
    else:
        sh.line.color.rgb = line
        sh.line.width = Pt(1.5)
    sh.shadow.inherit = False
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        sh.adjustments[0] = 0.06
    if s is not None:
        tf = sh.text_frame
        tf.word_wrap = True
        tf.vertical_anchor = MSO_ANCHOR.MIDDLE
        for m in ("margin_left", "margin_right"):
            setattr(tf, m, Inches(0.08))
        tf.margin_top = tf.margin_bottom = Inches(0.03)
        lines = s if isinstance(s, list) else [s]
        for i, line_ in enumerate(lines):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = align
            runs = line_ if isinstance(line_, list) else [(line_, bold)]
            for t, b in runs:
                r = p.add_run()
                r.text = t
                r.font.size = Pt(size)
                r.font.bold = b
                r.font.color.rgb = color
                r.font.name = font
    return sh


def title(slide, num, s):
    """Motivo del deck: número de sección en un círculo dorado + título textual de la plantilla."""
    c = slide.shapes.add_shape(MSO_SHAPE.OVAL, Inches(0.6), Inches(0.5), Inches(0.62), Inches(0.62))
    rgb(c, GOLD)
    no_line(c)
    c.shadow.inherit = False
    tf = c.text_frame
    tf.margin_left = tf.margin_right = tf.margin_top = tf.margin_bottom = 0
    tf.vertical_anchor = MSO_ANCHOR.MIDDLE
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.CENTER
    r = p.add_run()
    r.text = str(num)
    r.font.size = Pt(22)
    r.font.bold = True
    r.font.color.rgb = NAVY
    r.font.name = HEAD
    text(slide, 1.4, 0.38, 11.3, 0.85, s, size=30, bold=True, color=NAVY, font=HEAD,
         anchor=MSO_ANCHOR.MIDDLE, margin=0)


def kicker(slide, s):
    """Instrucción textual de la plantilla, debajo del título (p. ej. 'Insertar a continuación…')."""
    text(slide, 0.6, 1.17, 12.1, 0.3, s, size=11, color=GRAY, italic=True, margin=0)


def footer(slide, grupo):
    text(slide, 0.6, 7.02, 12.1, 0.3,
         f"AG · TP Cuatrimestral 2C26 · Grupo {grupo} · JPMorgan Chase & Co. · plantilla oficial de la cátedra",
         size=10, color=GRAY)


def cell_borders(cell, color=LINE, width=0.75):
    """Bordes finos en las cuatro caras (la planilla es una grilla). Van ANTES del relleno en tcPr."""
    tcPr = cell._tc.get_or_add_tcPr()
    tags = ("a:lnL", "a:lnR", "a:lnT", "a:lnB")
    for tag in tags:
        old = tcPr.find(qn(tag))
        if old is not None:
            tcPr.remove(old)
    for i, tag in enumerate(tags):
        ln = etree.Element(qn(tag), w=str(int(Pt(width))), cap="flat", cmpd="sng", algn="ctr")
        sf = etree.SubElement(ln, qn("a:solidFill"))
        etree.SubElement(sf, qn("a:srgbClr"), val=color)
        etree.SubElement(ln, qn("a:prstDash"), val="solid")
        tcPr.insert(i, ln)


def _paragraphs(val):
    """str | [(t,b[,color])…] (un párrafo) | [[(t,b)…], …] (varios párrafos) → lista de párrafos."""
    if isinstance(val, str):
        return [[(val, False)]]
    if val and isinstance(val[0], list):
        return val
    return [val]


def table(slide, x, y, w, rows, col_w, size=12, header=True, row_h=0.5, label_col=False,
          fills=None, header_fill=TINT2, header_color=NAVY):
    """Tabla con la estética de la planilla: encabezado sombreado, columna de rótulos sombreada,
    bordes grises. rows: lista de filas; cada celda str o runs (ver _paragraphs).
    row_h: número o lista por fila. col_w: anchos en pulgadas (suma ≈ w)."""
    nrows, ncols = len(rows), len(rows[0])
    rh = row_h if isinstance(row_h, list) else [row_h] * nrows
    gt = slide.shapes.add_table(nrows, ncols, Inches(x), Inches(y), Inches(w), Inches(sum(rh)))
    tbl = gt.table
    tblPr = gt._element.graphic.graphicData.tbl.tblPr
    tblPr.set("bandRow", "0")
    tblPr.set("firstRow", "0")
    for j, cw in enumerate(col_w):
        tbl.columns[j].width = Inches(cw)
    for i in range(nrows):
        tbl.rows[i].height = Inches(rh[i])
        for j in range(ncols):
            cell = tbl.cell(i, j)
            cell_borders(cell)
            cell.margin_left = cell.margin_right = Inches(0.08)
            cell.margin_top = cell.margin_bottom = Inches(0.05)
            cell.vertical_anchor = MSO_ANCHOR.MIDDLE
            is_head = header and i == 0
            is_label = label_col and j == 0 and not is_head
            custom = fills[i][j] if fills and fills[i] and fills[i][j] else None
            fill = header_fill if is_head else (custom or (TINT if is_label else WHITE))
            cell.fill.solid()
            cell.fill.fore_color.rgb = fill
            tf = cell.text_frame
            tf.word_wrap = True
            for k, runs in enumerate(_paragraphs(rows[i][j])):
                p = tf.paragraphs[0] if k == 0 else tf.add_paragraph()
                if k:
                    p.space_before = Pt(4)
                for part in runs:
                    t, b = part[0], part[1]
                    col = part[2] if len(part) > 2 else (header_color if is_head else BLACK)
                    r = p.add_run()
                    r.text = t
                    r.font.size = Pt(size)
                    r.font.name = BODY
                    r.font.bold = is_head or b or is_label
                    r.font.color.rgb = col
    return gt


def build(grupo):
    prs = Presentation()
    prs.slide_width = Inches(W)
    prs.slide_height = Inches(H)
    blank = prs.slide_layouts[6]

    # ---------- Portada (calca la carátula del enunciado) ----------
    s = prs.slides.add_slide(blank)
    box(s, 0, 0, W, H, NAVY)
    box(s, 0.9, 1.0, 0.16, 0.16, GOLD, shape=MSO_SHAPE.OVAL)
    text(s, 1.2, 0.88, 11, 0.4,
         "Universidad Tecnológica Nacional · Facultad Regional Buenos Aires · Ingeniería en Sistemas de Información",
         size=14, color=WHITE)
    text(s, 0.9, 1.75, 11.5, 0.9, "Administración Gerencial", size=40, bold=True, color=WHITE, font=HEAD)
    text(s, 0.9, 2.65, 11.5, 0.8, "Trabajo Práctico Cuatrimestral (2C26)", size=28, color=GOLD, font=HEAD)
    text(s, 0.9, 3.75, 11.5, 0.5, [[("Empresa analizada: ", False), ("JPMorgan Chase & Co.", True)]],
         size=20, color=WHITE)
    text(s, 0.9, 4.3, 11.5, 0.5, f"Grupo {grupo} · Bergera Vila · Busca · Cobas · Piccininno · Rossi · Schirripa",
         size=16, color=WHITE)
    text(s, 0.9, 5.35, 11.5, 1.2, [
        [("Profesor: ", True), ("Mg. Ing. Daniel Texido", False)],
        [("Ayudantes: ", True), ("Ing. Daniel Ordoñez · Ing. Pablo Brancone", False)],
        [("Curso: ", True), ("K.5571", False)],
    ], size=13, color=TINT2)
    text(s, 0.9, 6.6, 11.5, 0.4, "Entrega: 8 de noviembre de 2026 · 00_TP Cuatrimestral_G" + grupo,
         size=12, color=TINT2)

    # ---------- 1. Datos del Grupo ----------
    s = prs.slides.add_slide(blank)
    title(s, 1, "Datos del Grupo")
    rows = [
        ["Integrante", "Rol Gerencial", "Responsabilidad Principal"],
        ["Germán Martín Bergera Vila", "Gerente General",
         "Estrategia, coordinación del equipo directivo y decisión final (estratega, planeador-organizador y "
         "líder-comunicador, según Sallenave)"],
        ["Juan Ignacio Cobas", "Operaciones",
         "Procesamiento de pagos, mercados y servicios; continuidad operativa (árbitro de perturbaciones, según Mintzberg)"],
        ["Matías Tadeo Rossi", "Comercial / Marketing",
         "Marca Chase, adquisición y retención de clientes, venta cruzada (enlace y portavoz)"],
        ["Clara Belén Busca", "RRHH",
         "Talento, cultura, desarrollo de líderes y plan de sucesión (líder)"],
        ["Franco Ezequiel Piccininno", "Finanzas",
         "Presupuesto (incluido el tecnológico), eficiencia y control de KPI (administrador de recursos)"],
        ["Luciano Schirripa", "Sistemas / Innovación",
         "Plataformas tecnológicas, modernización (cloud), IA y ciberseguridad (monitor, difusor y emprendedor)"],
    ]
    table(s, 0.6, 1.45, 12.1, rows, [3.3, 2.4, 6.4], size=13, row_h=[0.5] + [0.75] * 6, label_col=True)
    text(s, 0.6, 6.5, 12.1, 0.4,
         "Seis roles gerenciales distintos, en el orden de la plantilla. Entre paréntesis, los papeles de Sallenave "
         "(cap. IV) y de Mintzberg (cap. V) que predominan en cada uno.",
         size=11, color=GRAY, italic=True)
    footer(s, grupo)

    # ---------- 2. Empresa Analizada ----------
    s = prs.slides.add_slide(blank)
    title(s, 2, "Empresa Analizada")
    rows = [
        ["Tipo (Real / Ficticia)", [("Real", True), (" · JPMorgan Chase & Co. (Nueva York; NYSE: JPM)", False)]],
        ["Rubro", "Servicios financieros globales (banca minorista, banca de inversión, pagos y gestión de patrimonios) "
                  "con desarrollo tecnológico propio a escala de empresa tech."],
        ["Tamaño", "Más de 300.000 empleados en más de 100 países · activos por ≈ US$4 billones · presupuesto tecnológico "
                   "2026 ≈ US$19.800 millones (≈ US$1.200 millones en IA) y más de 50.000 tecnólogos · centro tecnológico "
                   "en Buenos Aires desde 2014 (≈ 3.800 personas, nueva torre en Núñez)."],
        ["Mercado objetivo", "Personas y pymes (Chase, en EE.UU. y ahora Reino Unido y Alemania) · empresas, gobiernos e "
                             "inversores institucionales (CIB) · grandes patrimonios (AWM)."],
        ["Descripción breve (1 párrafo)",
         "JPMorgan Chase & Co. es el banco más grande de Estados Unidos y uno de los mayores del mundo. Opera en tres "
         "segmentos: banca de consumo (Chase), banca comercial y de inversión (CIB) y gestión de activos y patrimonios "
         "(AWM). Se diferencia por construir su propia tecnología: plataformas de pagos que mueven del orden de "
         "US$10 billones por día, Kinexys (blockchain), LLM Suite (IA generativa interna) y una red global de centros "
         "tecnológicos, entre ellos el Buenos Aires Corporate Center. Por eso lo analizamos como empresa tecnológica: "
         "su producto corre sobre software propio y su mayor inversión es en tecnología."],
    ]
    table(s, 0.6, 1.45, 12.1, rows, [3.0, 9.1], size=12, header=False,
          row_h=[0.5, 0.8, 1.1, 0.8, 1.9], label_col=True)
    footer(s, grupo)

    # ---------- 3. Liderazgo ----------
    s = prs.slides.add_slide(blank)
    title(s, 3, "Liderazgo")
    rows = [
        ["Estilo de liderazgo", [
            [("Liderazgo situacional", True), (" (Hersey y Blanchard) con base demócrata en los niveles gerenciales.", False)],
            [("En la cúpula, ", False), ("liderazgo transformacional", True),
             (" con rasgos carismáticos (Jamie Dimon, CEO desde 2005): metas desafiantes y una visión que trasciende lo "
              "transaccional.", False)]]],
        ["Justificación (máx. 5 líneas)", [
            [("Con más de 300.000 personas no sirve un único estilo: el líder adapta su comportamiento al ", False),
             ("grado de desarrollo de cada colaborador", True), (" (competencia y disposición). A un ingeniero senior del "
              "hub de Buenos Aires se le ", False), ("delega", True), ("; a un recién ingresado se lo ", False),
             ("dirige", True), (" o ", False), ("instruye", True),
             (". Dimon fija metas exigentes y una cultura de “negocios de primera clase, de una manera de primera clase”, "
              "e inspira a trascender el interés individual: el rasgo del líder transformacional.", False)]]],
        ["Problema potencial de liderazgo", [
            [("Dependencia del líder carismático: ", True),
             ("cuando la confianza extrema del líder le impide escuchar y tolerar que lo desafíen, pasa a ser una carga "
              "para la organización (House). Con Dimon de 70 años, el riesgo concreto es una ", False),
             ("sucesión mal preparada", True), (".", False)],
            [("Desajuste situacional: ", True),
             ("dirigir y controlar a equipos competentes y dispuestos (cuando corresponde delegar) es redundante con la "
              "estructura de la tarea (ruta-meta) y actúa como factor higiénico que desmotiva (Herzberg).", False)]]],
    ]
    table(s, 0.6, 1.45, 12.1, rows, [3.0, 9.1], size=12.5, header=False, row_h=[1.2, 1.5, 1.8], label_col=True)
    footer(s, grupo)

    # ---------- 4. Cadena de Valor de Porter: esquema ----------
    s = prs.slides.add_slide(blank)
    title(s, 4, "Cadena de Valor de Porter")
    kicker(s, "Esquema simple de la Cadena de Valor de Porter, adaptado a JPMorgan Chase (un banco que construye su propia tecnología)")
    x0, lab_w, cw = 0.6, 2.6, 9.1
    y = 1.5
    sup = [
        ("Infraestructura gerencial", "Gestión general, planificación y finanzas; riesgo, compliance y legales; capital y licencias bancarias", "prob"),
        ("Gestión de recursos humanos", "Más de 300.000 personas; reclutamiento tecnológico en hubs (Buenos Aires, India, Reino Unido); desarrollo de líderes", None),
        ("Desarrollo de la tecnología", "US$19.800 millones por año; plataformas propias (Payments, Kinexys, LLM Suite); cloud y ciberseguridad", "v1"),
        ("Adquisiciones", "Proveedores de nube, datos de mercado, hardware y servicios; alianzas con fintechs y redes de tarjetas", None),
    ]
    rh = 0.62
    text(s, x0, y - 0.02, 4, 0.3, "ACTIVIDADES DE APOYO", size=10, bold=True, color=GRAY)
    y += 0.3
    for name, desc, tag in sup:
        fill, line = TINT2, None
        if tag == "v1":
            fill = GOLD_LIGHT
        if tag == "prob":
            fill, line = RED_LIGHT, RED
        box(s, x0, y, lab_w, rh - 0.08, NAVY, name, size=12, bold=True, color=WHITE, align=PP_ALIGN.LEFT)
        box(s, x0 + lab_w + 0.05, y, cw - 0.05, rh - 0.08, fill, desc, size=11, align=PP_ALIGN.LEFT, line=line)
        y += rh
    y += 0.12
    text(s, x0, y - 0.02, 4, 0.3, "ACTIVIDADES PRIMARIAS", size=10, bold=True, color=GRAY)
    y += 0.3
    prim = [
        ("Logística de entrada", "Captación de depósitos y fondos; datos de clientes y de mercado", None),
        ("Operaciones", "Pagos (≈ US$10 billones/día), crédito, trading y custodia", "v2"),
        ("Logística de salida", "Canales: app y web Chase, sucursales, cajeros, APIs para empresas", None),
        ("Comercialización y ventas", "Marca Chase, tarjetas Sapphire, banca privada, recompensas", None),
        ("Servicio post-venta", "Atención 24/7, asesoramiento financiero, prevención de fraude", None),
    ]
    pw = (lab_w + cw) / 5
    ph = 1.55          # alto total del bloque (flecha + descripción)
    ah = 0.62          # alto de la flecha
    for i, (name, desc, tag) in enumerate(prim):
        fill = GOLD_LIGHT if tag == "v2" else TINT2
        # la flecha lleva solo el nombre, y en una caja de texto aparte: Google Slides
        # calcula mal el área de texto de los chevrons y el texto largo se desborda por las puntas
        box(s, x0 + i * pw, y, pw - 0.06, ah, fill, shape=MSO_SHAPE.CHEVRON if i else MSO_SHAPE.PENTAGON)
        notch = 0.3 if i else 0.1
        text(s, x0 + i * pw + notch, y, pw - 0.06 - notch - 0.3, ah, name, size=11, bold=True, color=NAVY,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE, margin=0.02)
        text(s, x0 + i * pw, y + ah + 0.05, pw - 0.06, ph - ah - 0.05, desc, size=10.5, color=BLACK,
             align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.TOP, margin=0.04)
    box(s, x0 + lab_w + cw + 0.1, 1.8, 0.9, y + ph - 1.8, NAVY, "MARGEN", size=11, bold=True, color=WHITE)
    ly = y + ph + 0.12
    box(s, x0, ly + 0.05, 0.25, 0.2, GOLD_LIGHT)
    text(s, x0 + 0.3, ly, 3.5, 0.3, "Actividades donde se genera mayor valor", size=11, color=GRAY)
    box(s, x0 + 3.9, ly + 0.05, 0.25, 0.2, RED_LIGHT, line=RED)
    text(s, x0 + 4.2, ly, 3.5, 0.3, "Actividad problemática", size=11, color=GRAY)
    footer(s, grupo)

    # ---------- 4. Cadena de Valor de Porter: campos de la plantilla ----------
    s = prs.slides.add_slide(blank)
    title(s, 4, "Cadena de Valor de Porter (continuación)")
    rows = [
        ["Actividad donde se genera mayor valor (1)",
         [("Desarrollo de la tecnología. ", True), ("Es lo que diferencia a JPM de un banco tradicional: las plataformas propias "
          "bajan el costo por transacción y permiten lanzar productos (Chase UK/Alemania, Kinexys) sin depender de terceros. "
          "Es el “know-how” que atraviesa toda la cadena.", False)]],
        ["Actividad donde se genera mayor valor (2)",
         [("Operaciones. ", True), ("La escala del procesamiento (pagos, mercados, custodia) genera ingresos por comisiones "
          "y datos que ningún competidor nuevo puede replicar rápido. Porter: se puede ser el mejor en marketing, pero no es "
          "ventaja si no se equipara con las operaciones.", False)]],
        ["Actividad problemática",
         [("Infraestructura gerencial (riesgo y compliance) sobre sistemas heredados. ", True), ("Cada cambio pasa por controles "
          "regulatorios y por sistemas legacy: la modernización compite con “mantener las luces prendidas” y "
          "frena el tiempo de salida al mercado.", False)]],
        ["Rol de los Sistemas de Información",
         [("No son soporte: son el núcleo. ", True), ("Todas las actividades primarias corren sobre software propio: los SI "
          "integran datos (entrada), automatizan operaciones (STP), son el canal (app, APIs) y el control (fraude, "
          "compliance). El hub de Buenos Aires es parte de esa cadena.", False)]],
    ]
    table(s, 0.6, 1.45, 12.1, rows, [3.4, 8.7], size=13, header=False, row_h=1.2, label_col=True,
          fills=[[None, None], [None, None], [RED_LIGHT, None], [GOLD_LIGHT, None]])
    footer(s, grupo)

    # ---------- 5. Matriz BCG: gráfico ----------
    s = prs.slides.add_slide(blank)
    title(s, 5, "Matriz BCG")
    kicker(s, "Gráfico simple de la Matriz BCG: cartera de negocios de JPMorgan Chase")
    gx, gy, gw, gh = 1.6, 1.6, 7.6, 4.9
    quads = [
        (gx, gy, "ESTRELLA", TINT2),
        (gx + gw / 2, gy, "DILEMA", TINT),
        (gx, gy + gh / 2, "VACA LECHERA", TINT),
        (gx + gw / 2, gy + gh / 2, "PESO MUERTO (PERRO)", TINT2),
    ]
    for qx, qy, name, fill in quads:
        box(s, qx, qy, gw / 2 - 0.04, gh / 2 - 0.04, fill)
        text(s, qx + 0.12, qy + 0.06, 3, 0.3, name, size=11, bold=True, color=GRAY)
    text(s, 0.5, gy, 1.0, gh, "CRECIMIENTO DE LA DEMANDA", size=10, bold=True, color=GRAY, align=PP_ALIGN.CENTER,
         anchor=MSO_ANCHOR.MIDDLE).rotation = 270
    text(s, 1.15, gy + 0.05, 0.45, 0.3, "Alto", size=10, color=GRAY, align=PP_ALIGN.RIGHT)
    text(s, 1.15, gy + gh - 0.35, 0.45, 0.3, "Bajo", size=10, color=GRAY, align=PP_ALIGN.RIGHT)
    text(s, gx, gy + gh + 0.05, gw, 0.3, "PARTICIPACIÓN RELATIVA EN EL MERCADO", size=10, bold=True, color=GRAY,
         align=PP_ALIGN.CENTER)
    text(s, gx, gy + gh + 0.05, 1, 0.3, "Alta", size=10, color=GRAY)
    text(s, gx + gw - 1, gy + gh + 0.05, 1, 0.3, "Baja", size=10, color=GRAY, align=PP_ALIGN.RIGHT)
    bubbles = [
        (gx + 0.45, gy + 0.55, 1.55, "CIB: banca de inversión y mercados", NAVY, WHITE),
        (gx + 2.15, gy + 0.9, 1.45, "JPMorgan Payments", NAVY, WHITE),
        (gx + 4.15, gy + 0.5, 1.35, "Chase Reino Unido y Alemania", GOLD, NAVY),
        (gx + 5.75, gy + 1.0, 1.3, "Kinexys e IA generativa (LLM Suite)", GOLD, NAVY),
        (gx + 0.55, gy + 2.7, 1.9, "Chase: banca minorista EE.UU.", NAVY, WHITE),
        (gx + 5.4, gy + 3.25, 1.1, "Chase Pay (2019)", GRAY, WHITE),
    ]
    for bx, by, d, lab, fill, fc in bubbles:
        box(s, bx, by, d, d, fill, lab, size=10, bold=True, color=fc, shape=MSO_SHAPE.OVAL)
    box(s, 9.6, 1.6, 3.15, 4.9, TINT, shape=MSO_SHAPE.ROUNDED_RECTANGLE)
    text(s, 9.8, 1.72, 2.8, 0.4, "Cómo leerla", size=14, bold=True, color=NAVY, font=HEAD)
    text(s, 9.8, 2.15, 2.8, 4.3, [
        [("Vaca lechera: ", True), ("Chase minorista genera el efectivo que financia a estrellas y dilemas.", False)],
        [("Estrellas: ", True), ("CIB y Payments: alta participación en demanda que sigue creciendo; necesitan inversión impulsora.", False)],
        [("Dilemas: ", True), ("banca digital en Europa, blockchain e IA: demanda en crecimiento, participación todavía baja; decisión incierta.", False)],
        [("Peso muerto: ", True), ("Chase Pay, billetera propia discontinuada en 2019; sin nuevas inversiones.", False)],
        [("El tamaño de cada burbuja sugiere el peso relativo en ingresos (cualitativo).", False)],
    ], size=12)
    footer(s, grupo)

    # ---------- 5. Matriz BCG: tabla de la plantilla ----------
    s = prs.slides.add_slide(blank)
    title(s, 5, "Matriz BCG (continuación)")
    rows = [
        ["Producto / Servicio", "Cuadrante BCG", "Decisión Estratégica"],
        ["Chase: banca minorista en EE.UU. (cuentas, tarjetas, hipotecas)", "Vaca lechera",
         "Seguir explotando sin grandes inversiones nuevas: financia la inversión tecnológica y la expansión"],
        ["Banca de inversión y mercados (CIB)", "Estrella",
         "Inversión impulsora para sostener la participación: trading electrónico y datos"],
        ["JPMorgan Payments", "Estrella",
         "Invertir: pagos en tiempo real, expansión global, integración con Kinexys"],
        ["Chase Reino Unido y Alemania (banca digital internacional)", "Dilema",
         "Invertir con hitos: crecer hasta el punto de equilibrio (y volverse estrella) o frenar"],
        ["Kinexys (blockchain) e IA generativa (LLM Suite)", "Dilema",
         "Invertir selectivamente: pilotos con casos de uso medibles"],
        ["Chase Pay (billetera digital propia, discontinuada en 2019)", "Peso muerto (perro)",
         "No invertir para mantenerlo vivo (ya ejecutado): apoyarse en Apple Pay, Google Pay y Zelle"],
    ]
    qfill = {"Vaca lechera": TINT, "Estrella": GOLD_LIGHT, "Dilema": TINT2, "Peso muerto (perro)": RED_LIGHT}
    fills = [None] + [[None, qfill[r[1]], None] for r in rows[1:]]
    table(s, 0.6, 1.45, 12.1, rows, [4.6, 1.9, 5.6], size=13, row_h=[0.5] + [0.75] * 6, fills=fills)
    footer(s, grupo)

    # ---------- 6. Decisiones Estratégicas Finales ----------
    s = prs.slides.add_slide(blank)
    title(s, 6, "Decisiones Estratégicas Finales")
    dec = [
        ("Gerente General", "Expansión europea de Chase (Reino Unido → Alemania) con hitos go/no-go",
         "Clientes activos; fecha de punto de equilibrio del negocio", "cliente / económico-financiera"),
        ("Operaciones", "Escalar Payments: liquidación en tiempo real y automatización (STP)",
         "Volumen diario procesado; % de operaciones sin intervención manual", "procesos internos"),
        ("Comercial / Marketing", "Profundizar la relación con clientes Chase (venta cruzada: inversión, tarjetas)",
         "Productos por cliente; NPS", "cliente"),
        ("RRHH", "Plan de sucesión y desarrollo de líderes situacionales",
         "% de puestos críticos con sucesor identificado; rotación voluntaria de talento clave", "innovación y aprendizaje"),
        ("Finanzas", "Disciplina del presupuesto tecnológico: más “cambio”, menos “mantenimiento”",
         "Ratio de eficiencia (gastos / ingresos); % del gasto tech en nuevas capacidades", "económico-financiera"),
        ("Sistemas / Innovación", "Modernización: migración a cloud, baja de legacy y despliegue de IA generativa",
         "% de aplicaciones modernizadas; incidentes críticos por trimestre; % de empleados activos en LLM Suite",
         "procesos internos / innovación y aprendizaje"),
    ]
    rows = [["Decisión Estratégica", "KPI de Control"]]
    for owner, d, kpi, persp in dec:
        rows.append([[(owner + " · ", True), (d, False)],
                     [(kpi, False), ("  (perspectiva: " + persp + ")", False, GRAY)]])
    table(s, 0.6, 1.45, 12.1, rows, [6.0, 6.1], size=12, row_h=[0.45] + [0.78] * 6)
    text(s, 0.6, 6.62, 12.1, 0.35,
         "Cada decisión tiene un gerente dueño. Los KPI son indicadores de un tablero de control estratégico (cap. XV), "
         "clasificados por sus cuatro perspectivas: cliente, económico-financiera, procesos internos, innovación y aprendizaje.",
         size=10.5, color=GRAY, italic=True)
    footer(s, grupo)

    # ---------- Fuentes ----------
    s = prs.slides.add_slide(blank)
    title(s, "i", "Fuentes")
    text(s, 0.6, 1.5, 12, 4.5, [
        "Texido, D. (2026). Administración Gerencial, libro de cátedra: caps. IV y V (el gerente: Sallenave y Mintzberg), VII (liderazgo), VIII (motivación: Herzberg), XIV (estrategia y planeamiento: cadena de valor y BCG) y XV (tablero de control).",
        "JPMorgan Chase & Co. (2026). Annual Report 2025 y resultados del cuarto trimestre de 2025 (SEC EDGAR).",
        "Reuters (septiembre de 2025). JPMorgan lanzará su banco digital minorista en Alemania en 2026.",
        "Bloomberg Línea (diciembre de 2024) y El Economista (2025). Buenos Aires Corporate Center y nueva sede en Núñez.",
        "Cobertura de prensa sobre el presupuesto tecnológico 2026 de JPMorgan Chase (≈ US$19.800 millones, ≈ US$1.200 millones en IA).",
    ], size=13, color=BLACK)
    footer(s, grupo)

    return prs


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--grupo", default="x")
    ap.add_argument("--out", default=None)
    a = ap.parse_args()
    here = os.path.dirname(os.path.abspath(__file__))
    out = a.out or os.path.join(here, "exports", f"00_TP Cuatrimestral_G{a.grupo}.pptx")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    build(a.grupo).save(out)
    print(out)
