"""Gráficos del caso Silksong que no da tools/ajuste_mc.py.

Lee ajuste/resultados.json (salida de ajuste_mc.py) y genera:

- ajuste/modelo-<nombre>-doble.png: cada modelo con la nube, en dos paneles (rango completo y
  zoom en la cola, con la estimación en x = 15).
- ajuste/comparacion-cola.png: todos los modelos con zoom en los meses 3–15, donde está la
  predicción (en el gráfico completo el mes 1 aplasta todo).
- ajuste/silksong-vs-gta-v.png: Silksong y GTA V (Steam, desde abril 2015) en % del primer
  mes, para el gancho de GTA VI (datos/steamcharts-gta-v.csv).

Uso: venv/bin/python materias/analisis-numerico/tp-minimos-cuadrados/caso-silksong/graficos.py
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
from matplotlib.ticker import FuncFormatter  # noqa: E402

AQUI = Path(__file__).resolve().parent
RES = json.loads((AQUI / "ajuste" / "resultados.json").read_text(encoding="utf-8"))

# Paleta categórica en orden fijo (slots 1–6 de la paleta validada del skill dataviz).
MODELOS = [
    ("recta", "Recta", "#2a78d6", lambda p, x: p["a_0"] + p["a_1"] * x),
    ("parabola", "Parábola", "#eb6834", lambda p, x: p["a_0"] + p["a_1"] * x + p["a_2"] * x**2),
    ("exponencial", "Exponencial", "#1baf7a", lambda p, x: p["a_0"] * np.exp(p["a_1"] * x)),
    ("potencial", "Potencial", "#eda100", lambda p, x: p["a_0"] * x ** p["a_1"]),
    ("reciproco", "Recíproco", "#e87ba4", lambda p, x: p["a_0"] + p["a_1"] / x),
    ("hiperbolico", "Hiperbólico", "#008300", lambda p, x: p["a_1"] / (p["a_0"] + x)),
]
# Solo los modelos que se ajustaron (los colores siguen al modelo, no a su posición).
MODELOS = [m for m in MODELOS if m[0] in {r["modelo"] for r in RES["modelos"]}]
TINTA = "#262624"
TINTA_2 = "#6b6a63"
GRILLA = "#e6e5df"

SUP = str.maketrans("0123456789-", "⁰¹²³⁴⁵⁶⁷⁸⁹⁻")


def cientifica(v: float) -> str:
    e = int(np.floor(np.log10(abs(v))))
    return f"{v / 10**e:.2f}".replace(".", ",") + "×10" + str(e).translate(SUP)


miles = FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", "."))


def comparacion_cola() -> None:
    x = np.array(RES["x"])
    y = np.array(RES["y"])
    x0 = RES["x0"]
    params = {m["modelo"]: m for m in RES["modelos"]}

    fig, ax = plt.subplots(figsize=(9, 5.6), dpi=150)
    xs = np.linspace(2.6, 15.4, 400)
    etiquetas = []
    for clave, nombre, color, f in MODELOS:
        m = params[clave]
        ax.plot(xs, f(m["parametros"], xs), color=color, lw=2, label=f"{nombre} (E = {cientifica(m['sse'])})", zorder=2)
        y0 = f(m["parametros"], x0)
        ax.plot([x0], [y0], "o", ms=8, color=color, mec="white", mew=2, zorder=4)
        etiquetas.append((y0, f"{nombre}: {y0:,.0f}".replace(",", "."), color))

    ax.scatter(x[x >= 3], y[x >= 3], s=40, color=TINTA, zorder=5, label="Datos reales (SteamCharts)")
    ax.axvline(x0, color=TINTA_2, lw=1, ls="--", zorder=1)
    ax.axhline(0, color=TINTA_2, lw=1, zorder=1)

    # Etiquetas directas a la derecha, separadas para que no se pisen.
    etiquetas.sort()
    ymin, ymax = -10000, 50000
    pos = []
    for y0, *_ in etiquetas:
        yy = min(max(y0, ymin + 2500), ymax - 2500)
        if pos and yy - pos[-1] < 3000:
            yy = pos[-1] + 3000
        pos.append(yy)
    for (y0, texto, color), yy in zip(etiquetas, pos):
        ax.annotate(texto, xy=(x0, min(max(y0, ymin), ymax)), xytext=(x0 + 0.55, yy),
                    va="center", fontsize=9, color=TINTA,
                    arrowprops=dict(arrowstyle="-", color=color, lw=1))

    ax.set_xlim(2.5, 18.2)
    ax.set_ylim(ymin, ymax)
    ax.set_xticks(range(3, 16))
    ax.yaxis.set_major_formatter(miles)
    ax.set_xlabel("Mes desde el lanzamiento (15 = noviembre 2026)", color=TINTA)
    ax.set_ylabel("Jugadores simultáneos promedio", color=TINTA)
    ax.set_title(f"Hollow Knight: Silksong — los {len(MODELOS)} modelos en la zona de la predicción (meses 3 a 15)",
                 fontsize=11, color=TINTA, loc="left")
    ax.grid(color=GRILLA, lw=0.8)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(TINTA_2)
    ax.tick_params(colors=TINTA_2)
    ax.legend(loc="upper center", fontsize=8.5, frameon=False, ncol=2)
    fig.text(0.01, 0.01, "Zoom: los meses 1 (191.124) y 2 (58.328) quedan fuera de la ventana; "
             "los modelos se ajustaron con los 14 meses.", fontsize=7.5, color=TINTA_2)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(AQUI / "ajuste" / "comparacion-cola.png")
    plt.close(fig)


def _estilo(ax) -> None:
    ax.grid(color=GRILLA, lw=0.8)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(TINTA_2)
    ax.tick_params(colors=TINTA_2, labelsize=8)
    ax.yaxis.set_major_formatter(miles)


def modelos_dobles() -> None:
    x = np.array(RES["x"])
    y = np.array(RES["y"])
    x0 = RES["x0"]
    params = {m["modelo"]: m for m in RES["modelos"]}
    for clave, nombre, color, f in MODELOS:
        p = params[clave]["parametros"]
        y0 = f(p, x0)
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(10, 4), dpi=150)
        for ax, (xa, xb), titulo in ((a1, (0.85, 15.4), "Rango completo"),
                                     (a2, (2.6, 15.4), "Zoom: meses 3 a 15 (zona de la predicción)")):
            xs = np.linspace(xa, xb, 400)
            ys = f(p, xs)
            ax.plot(xs, ys, color=color, lw=2, zorder=2)
            mask = x >= xa
            ax.scatter(x[mask], y[mask], s=28, color=TINTA, zorder=4)
            ax.plot([x0], [y0], "*", ms=13, color=color, mec=TINTA, mew=0.6, zorder=5)
            ax.axhline(0, color=TINTA_2, lw=0.8, zorder=1)
            if ax is a2:
                vals = np.concatenate([y[mask], [y0, 0]])
                lo, hi = vals.min(), vals.max()
                ax.set_ylim(lo - 0.15 * (hi - lo), hi + 0.6 * (hi - lo))
                ax.set_xticks(range(3, 16))
            else:
                ax.set_xticks(range(1, 16, 2))
            ax.set_xlim(xa - 0.2, xb)
            ax.set_title(titulo, fontsize=9.5, color=TINTA, loc="left")
            ax.set_xlabel("Mes desde el lanzamiento", fontsize=8.5, color=TINTA)
            _estilo(ax)
        a1.set_ylabel("Jugadores simultáneos promedio", fontsize=8.5, color=TINTA)
        fig.suptitle(f"Modelo {nombre.lower()} — estimación para noviembre 2026 (★): "
                     f"ŷ(15) = {y0:,.0f}".replace(",", "."), fontsize=11, color=TINTA, x=0.01, ha="left")
        fig.tight_layout()
        fig.savefig(AQUI / "ajuste" / f"modelo-{clave}-doble.png")
        plt.close(fig)


def silksong_vs_gta_v(meses: int = 15) -> None:
    with open(AQUI / "datos" / "steamcharts-gta-v.csv", encoding="utf-8") as f:
        gta = [float(r["jugadores_promedio"]) for r in csv.DictReader(f)][:meses]
    silk = RES["y"]
    fig, ax = plt.subplots(figsize=(9, 4.8), dpi=150)
    for nombre, ys, color in (("Hollow Knight: Silksong (sep 2025 – oct 2026)", silk, "#2a78d6"),
                              ("GTA V en Steam (abr 2015 – jun 2016)", gta, "#eb6834")):
        xs = np.arange(1, len(ys) + 1)
        pct = 100 * np.array(ys) / ys[0]
        ax.plot(xs, pct, color=color, lw=2, marker="o", ms=6, mec="white", mew=1.5, label=nombre)
    ax.annotate("GTA V vuelve a subir\n(oct 2015 – ene 2016)", xy=(10, 100 * gta[9] / gta[0]),
                xytext=(10.6, 48), fontsize=9, color=TINTA,
                arrowprops=dict(arrowstyle="-", color="#eb6834", lw=1))
    ax.set_xticks(range(1, meses + 1))
    ax.set_ylim(0, 105)
    ax.set_xlabel("Mes desde el lanzamiento en Steam", color=TINTA)
    ax.set_ylabel("Jugadores promedio (% del primer mes)", color=TINTA)
    ax.set_title("Los dos caen fuerte al principio; después GTA V se reactiva y Silksong no",
                 fontsize=11, color=TINTA, loc="left")
    ax.grid(color=GRILLA, lw=0.8)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(TINTA_2)
    ax.tick_params(colors=TINTA_2)
    ax.legend(loc="upper right", fontsize=9, frameon=False)
    fig.text(0.01, 0.01, "Fuente: SteamCharts (apps 1030300 y 271590). Primer mes = 100 %: "
             "Silksong 191.124 y GTA V 192.714 jugadores simultáneos promedio.",
             fontsize=7.5, color=TINTA_2)
    fig.tight_layout(rect=(0, 0.03, 1, 1))
    fig.savefig(AQUI / "ajuste" / "silksong-vs-gta-v.png")
    plt.close(fig)


if __name__ == "__main__":
    modelos_dobles()
    print("✓ ajuste/modelo-*-doble.png")
    comparacion_cola()
    print("✓ ajuste/comparacion-cola.png")
    silksong_vs_gta_v()
    print("✓ ajuste/silksong-vs-gta-v.png")
