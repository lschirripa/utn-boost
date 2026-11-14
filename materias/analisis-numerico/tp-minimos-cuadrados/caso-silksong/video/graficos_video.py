"""Gráficos para las diapositivas del video (letra grande, sin título: el título va en la diapositiva).

Mismos datos y colores que graficos.py, pero dibujados al tamaño en que se ven en una
diapositiva de 1920x1080 (1 pulgada = 100 px), para que los ejes se lean en el video.

Uso: venv/bin/python materias/analisis-numerico/tp-minimos-cuadrados/caso-silksong/video/graficos_video.py
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

CASO = Path(__file__).resolve().parent.parent
OUT = Path(__file__).resolve().parent / "graficos"
RES = json.loads((CASO / "ajuste" / "resultados.json").read_text(encoding="utf-8"))
X, Y, X0 = np.array(RES["x"]), np.array(RES["y"]), RES["x0"]
PAR = {m["modelo"]: m for m in RES["modelos"]}

MODELOS = [
    ("exponencial", "Exponencial", "#1baf7a", lambda p, x: p["a_0"] * np.exp(p["a_1"] * x)),
    ("potencial", "Potencial", "#eda100", lambda p, x: p["a_0"] * x ** p["a_1"]),
    ("reciproco", "Recíproco", "#e87ba4", lambda p, x: p["a_0"] + p["a_1"] / x),
]
TINTA, TINTA_2, GRILLA = "#262624", "#6b6a63", "#e6e5df"
plt.rcParams.update({"font.size": 17, "axes.labelsize": 17, "xtick.labelsize": 16,
                     "ytick.labelsize": 16, "axes.titlesize": 18, "legend.fontsize": 16})
miles = FuncFormatter(lambda v, _: f"{v:,.0f}".replace(",", "."))


def fmt(v: float) -> str:
    return f"{v:,.0f}".replace(",", ".").replace("-", "−")


def estilo(ax) -> None:
    ax.grid(color=GRILLA, lw=1)
    for sp in ("top", "right"):
        ax.spines[sp].set_visible(False)
    for sp in ("left", "bottom"):
        ax.spines[sp].set_color(TINTA_2)
    ax.tick_params(colors=TINTA_2)


def guardar(fig, nombre: str) -> None:
    OUT.mkdir(exist_ok=True)
    fig.savefig(OUT / nombre, dpi=200)
    plt.close(fig)
    print("✓", nombre)


def nube() -> None:
    fig, ax = plt.subplots(figsize=(9, 5.9))
    ax.scatter(X, Y, s=110, color=TINTA, zorder=3)
    ax.annotate("mes 1: 191.124", xy=(1, Y[0]), xytext=(1.6, Y[0]), va="center", color=TINTA)
    ax.annotate("mes 2: 58.328", xy=(2, Y[1]), xytext=(2.6, Y[1]), va="center", color=TINTA)
    ax.annotate("mes 14: 6.108", xy=(14, Y[13]), xytext=(11.3, 30000), color=TINTA,
                arrowprops=dict(arrowstyle="-", color=TINTA_2, lw=1.2))
    ax.set_xticks(range(1, 15))
    ax.set_ylim(0, 205000)
    ax.yaxis.set_major_formatter(miles)
    ax.set_xlabel("Mes desde el lanzamiento", color=TINTA)
    ax.set_ylabel("Jugadores simultáneos promedio", color=TINTA)
    estilo(ax)
    fig.tight_layout()
    guardar(fig, "nube.png")


def gta() -> None:
    with open(CASO / "datos" / "steamcharts-gta-v.csv", encoding="utf-8") as f:
        g = [float(r["jugadores_promedio"]) for r in csv.DictReader(f)][:15]
    fig, ax = plt.subplots(figsize=(10, 5.33))
    for nombre, ys, color in (("Silksong (sept. 2025 – oct. 2026)", list(Y), "#2a78d6"),
                              ("GTA V en Steam (abr. 2015 – jun. 2016)", g, "#eb6834")):
        xs = np.arange(1, len(ys) + 1)
        ax.plot(xs, 100 * np.array(ys) / ys[0], color=color, lw=3.5, marker="o", ms=9,
                mec="white", mew=2, label=nombre)
    ax.annotate("GTA V vuelve a subir", xy=(10, 100 * g[9] / g[0]), xytext=(8.2, 46), color=TINTA,
                arrowprops=dict(arrowstyle="-", color="#eb6834", lw=1.5))
    ax.set_xticks(range(1, 16))
    ax.set_ylim(0, 105)
    ax.set_xlabel("Mes desde el lanzamiento en Steam", color=TINTA)
    ax.set_ylabel("Jugadores (% del primer mes)", color=TINTA)
    estilo(ax)
    ax.legend(loc="upper right", frameon=False)
    fig.tight_layout()
    guardar(fig, "silksong-vs-gta-v.png")


def dobles() -> None:
    for clave, nombre, color, f in MODELOS:
        p = PAR[clave]["parametros"]
        y0 = f(p, X0)
        fig, (a1, a2) = plt.subplots(1, 2, figsize=(11.5, 4.6))
        for ax, (xa, xb), titulo in ((a1, (0.85, 15.5), "Los 14 meses"),
                                     (a2, (2.6, 15.5), "Zoom: meses 3 a 15")):
            xs = np.linspace(xa, xb, 400)
            ax.plot(xs, f(p, xs), color=color, lw=3.5, zorder=2)
            m = X >= xa
            ax.scatter(X[m], Y[m], s=60, color=TINTA, zorder=4)
            ax.plot([X0], [y0], "*", ms=24, color=color, mec=TINTA, mew=1, zorder=5)
            ax.axhline(0, color=TINTA_2, lw=1, zorder=1)
            if ax is a2:
                vals = np.concatenate([Y[m], [y0, 0]])
                lo, hi = vals.min(), vals.max()
                ax.set_ylim(lo - 0.2 * (hi - lo), hi + 0.6 * (hi - lo))
                ax.set_xticks(range(3, 16, 2))
                ax.annotate(f"mes 15: {fmt(y0)}", xy=(X0, y0), xytext=(9.6, hi + 0.25 * (hi - lo)),
                            color=TINTA, arrowprops=dict(arrowstyle="-", color=TINTA_2, lw=1.2))
            else:
                ax.set_xticks(range(1, 16, 2))
            ax.set_xlim(xa - 0.2, xb)
            ax.set_title(titulo, color=TINTA, loc="left")
            ax.set_xlabel("Mes desde el lanzamiento", color=TINTA)
            ax.yaxis.set_major_formatter(miles)
            estilo(ax)
        fig.tight_layout()
        guardar(fig, f"modelo-{clave}-doble.png")


def cola() -> None:
    fig, ax = plt.subplots(figsize=(9.6, 5.97))
    xs = np.linspace(2.6, 15.4, 400)
    for clave, nombre, color, f in MODELOS:
        p = PAR[clave]["parametros"]
        y0 = f(p, X0)
        ax.plot(xs, f(p, xs), color=color, lw=3.5, label=nombre, zorder=2)
        ax.plot([X0], [y0], "o", ms=13, color=color, mec="white", mew=2.5, zorder=4)
        dy = {"potencial": 4500, "exponencial": -700, "reciproco": 0}[clave]
        ax.annotate(f"{nombre}: {fmt(y0)}", xy=(X0, y0), xytext=(15.5, y0 + dy), va="center", color=TINTA)
    ax.scatter(X[X >= 3], Y[X >= 3], s=80, color=TINTA, zorder=5, label="Datos reales")
    ax.axvline(X0, color=TINTA_2, lw=1.2, ls="--", zorder=1)
    ax.axhline(0, color=TINTA, lw=1.5, zorder=1)
    ax.set_xlim(2.5, 20.3)
    ax.set_ylim(-10000, 50000)
    ax.set_xticks(range(3, 16, 2))
    ax.yaxis.set_major_formatter(miles)
    ax.set_xlabel("Mes desde el lanzamiento (15 = noviembre 2026)", color=TINTA)
    ax.set_ylabel("Jugadores simultáneos promedio", color=TINTA)
    estilo(ax)
    ax.legend(loc="upper right", frameon=False)
    fig.tight_layout()
    guardar(fig, "comparacion-cola.png")


if __name__ == "__main__":
    nube()
    gta()
    dobles()
    cola()
