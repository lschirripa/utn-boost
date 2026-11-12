"""Arma el TP completo del caso Silksong y lo exporta a HTML y PDF.

Combina:
- tp-fuente.md        (carátula, a, b, aplicaciones, conclusiones, fuentes; con marcadores)
- ajuste/reporte.md   (punto c: desarrollo paso a paso de cada modelo, de tools/ajuste_mc.py)
- borrador-d.md       (punto d)

Salida (regenerable, no editar a mano): exports/tp-silksong.md, .html y .pdf.

Orden para regenerar todo desde los datos:
    venv/bin/python tools/ajuste_mc.py <caso>/datos/datos.csv \
        --modelos exponencial,potencial,reciproco --x0 15 \
        --out-dir <caso>/ajuste
    venv/bin/python <caso>/graficos.py
    venv/bin/python <caso>/armar_tp.py
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
sys.path.insert(0, str(REPO / "tools"))
OUT = AQUI / "exports"

# Por qué probamos cada modelo (va debajo del título de cada uno en el punto c).
POR_QUE = {
    "recta": "Es la referencia más simple. Cuando no se conoce el comportamiento del "
             "fenómeno, la recta muchas veces es una primera aproximación razonable.",
    "parabola": "Agrega curvatura sin dejar de ser un polinomio: puede bajar rápido al "
                "principio y frenarse después, como la nube.",
    "exponencial": "Es el modelo típico de las caídas en las que **cada mes se pierde el "
                   "mismo porcentaje** de jugadores.",
    "potencial": "Modela caídas en las que el porcentaje que se pierde **es cada vez "
                 "menor**: muy fuerte al principio y con una cola que baja despacio.",
    "reciproco": "Baja como $1/x$ y se acerca a un piso $a_0$: podría representar a los "
                 "jugadores \"fieles\" que siguen jugando.",
    "hiperbolico": "También baja como $1/x$, pero corrido en $a_0$ y acercándose a cero; "
                   "es el modelo hiperbólico visto en la teórica.",
}


def _num(v: float, d: int = 4, paren: bool = False) -> str:
    from ajuste_mc import _fmt  # mismo formato que el reporte (coma decimal)
    t = _fmt(v, d)
    return f"({t})" if paren and v < 0 else t


def cramer(m: dict) -> str:
    """Paso 5 con la regla de Cramer (sistema 2×2), a partir de resultados.json.

    Los factores van con 8 decimales y los determinantes con 4, para que las cuentas
    cierren a mano con lo que se ve; las incógnitas, con 4 (como el resto del reporte).
    """
    (a, b), (c, d) = m["matriz_normal"]
    e, f = m["termino_independiente"]
    n0, n1 = list(m["solucion_sistema"])
    v0, v1 = m["solucion_sistema"].values()
    det = a * d - b * c
    d0 = e * d - b * f
    d1 = a * f - e * c
    F = lambda v: _num(v, 8, paren=True)
    D = lambda v: _num(v, 6 if abs(v) < 1000 else 4)
    N = _num
    mat = lambda p, q, r, s_: rf"\begin{{vmatrix}} {F(p)} & {F(q)} \\ {F(r)} & {F(s_)} \end{{vmatrix}}"
    return "\n".join([
        "**Paso 5 — resolución del sistema** (regla de Cramer):",
        "",
        "$$",
        rf"\Delta = {mat(a, b, c, d)} = {F(a)} \cdot {F(d)} - {F(b)} \cdot {F(c)} = {D(det)}",
        "$$",
        "",
        "$$",
        rf"\Delta_{{{n0}}} = {mat(e, b, f, d)} = {F(e)} \cdot {F(d)} - {F(b)} \cdot {F(f)} = {D(d0)}",
        "$$",
        "",
        "$$",
        rf"\Delta_{{{n1}}} = {mat(a, e, c, f)} = {F(a)} \cdot {F(f)} - {F(e)} \cdot {F(c)} = {D(d1)}",
        "$$",
        "",
        "$$",
        rf"{n0} = \frac{{\Delta_{{{n0}}}}}{{\Delta}} = {N(v0)},\qquad "
        rf"{n1} = \frac{{\Delta_{{{n1}}}}}{{\Delta}} = {N(v1)}",
        "$$",
    ])


CLAVES = {"recta": "recta", "parábola": "parabola", "exponencial": "exponencial",
          "potencial": "potencial", "recíproco": "reciproco", "hiperbólico": "hiperbolico"}


def punto_c() -> str:
    rep = (AQUI / "ajuste" / "reporte.md").read_text(encoding="utf-8")
    ini = rep.index("## 1. Modelo")
    fin = rep.index("## Comparación")
    txt = rep[ini:fin].rstrip()
    # R² no se vio en clase: lo sacamos para no usar un concepto sin definir.
    txt = re.sub(r" · coeficiente de determinación \$R\^2 = [^$]*\$\.", ".", txt)

    def titulo(m: re.Match) -> str:
        n, nombre, resto = m.group(1), m.group(2), m.group(3)
        clave = CLAVES[nombre.lower()]
        return f"### c.{n} Modelo {nombre}{resto}\n\n**¿Por qué lo probamos?** {POR_QUE[clave]}"

    txt = re.sub(r"^## (\d+)\. Modelo (\S+)(:.*)$", titulo, txt, flags=re.M)
    # Gráfico de cada modelo: la versión de dos paneles de graficos.py (completo + zoom).
    txt = re.sub(r"\]\(modelo-(\w+)\.png\)", r"](ajuste/modelo-\1-doble.png)", txt)
    txt = re.sub(r"\]\(((?:nube|comparacion)[^)]*\.png)\)", r"](ajuste/\1)", txt)
    # Paso 5 con Cramer (nombrado en la teórica; la consigna pide "resolverlo").
    res = {m["modelo"]: m for m in json.loads(
        (AQUI / "ajuste" / "resultados.json").read_text(encoding="utf-8"))["modelos"]}
    partes = re.split(r"(?=^### c\.\d+ Modelo )", txt, flags=re.M)
    for i, parte in enumerate(partes):
        mt = re.match(r"### c\.\d+ Modelo (\S+):", parte)
        if not mt:
            continue
        clave = CLAVES[mt.group(1).lower()]
        parte, n = re.subn(r"\*\*Paso 5 — solución del sistema:\*\*\n\n\$\$\n.*?\n\$\$",
                           lambda _m: cramer(res[clave]), parte, count=1, flags=re.S)
        assert n == 1, f"no encontré el Paso 5 de {clave}"
        partes[i] = parte
    txt = "".join(partes)
    return txt


def punto_d() -> str:
    d = (AQUI / "borrador-d.md").read_text(encoding="utf-8")
    ini = d.index("## d.1")
    fin = d.rindex("\n---\n")  # pie de "Generado el …"
    txt = d[ini:fin].rstrip()
    return re.sub(r"^## d\.", "### d.", txt, flags=re.M)


def main() -> None:
    fuente = (AQUI / "tp-fuente.md").read_text(encoding="utf-8")
    fuente = re.sub(r"\A<!--.*?-->\s*", "", fuente, flags=re.S)
    tp = fuente.replace("{{MODELOS}}", punto_c()).replace("{{PUNTO_D}}", punto_d())
    assert "{{" not in tp, "quedó un marcador sin reemplazar"
    # El md queda en exports/: las imágenes se referencian desde ahí.
    tp = tp.replace("](ajuste/", "](../ajuste/")
    cabecera = (f"<!-- GENERADO por armar_tp.py el {date.today().isoformat()} — no editar a mano. "
                "Fuentes: tp-fuente.md, ajuste/reporte.md, borrador-d.md. -->\n\n"
                # Que las tablas (≤ 16 filas) no se partan entre páginas del PDF.
                "<style>@media print { table { break-inside: avoid; } }</style>\n\n")
    OUT.mkdir(exist_ok=True)
    md = OUT / "tp-silksong.md"
    md.write_text(cabecera + tp + "\n", encoding="utf-8")
    print(f"✓ {md.relative_to(REPO)}")
    subprocess.run([sys.executable, str(REPO / "tools" / "md_to_html.py"), str(md), "--pdf",
                    "--out-dir", str(OUT)], check=True)


if __name__ == "__main__":
    main()
