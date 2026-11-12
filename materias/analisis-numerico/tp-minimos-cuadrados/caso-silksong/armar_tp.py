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

import re
import subprocess
import sys
from datetime import date
from pathlib import Path

AQUI = Path(__file__).resolve().parent
REPO = AQUI.parents[3]
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
    # La cátedra no pide el desarrollo de la resolución del sistema: alcanza con el resultado.
    txt = txt.replace("**Paso 5 — solución del sistema:**",
                      "**Paso 5 — solución del sistema** (resuelto con calculadora):")
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
