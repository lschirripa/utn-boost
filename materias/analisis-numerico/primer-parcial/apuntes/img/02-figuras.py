"""Figuras de la guía 02-laplace-desde-cero.md.

Uso (desde la raíz del repo):
    venv/bin/python materias/analisis-numerico/primer-parcial/apuntes/img/02-figuras.py
Genera 02-fig1 y 02-fig2 (PNG) en esta misma carpeta.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
AZUL, ROJO, VERDE, GRIS = "#1f77b4", "#d62728", "#2ca02c", "#555555"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})


def ejes(ax):
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.grid(alpha=0.25)


def guardar(fig, nombre):
    fig.tight_layout()
    fig.savefig(OUT / nombre, dpi=140)
    plt.close(fig)


# ---------- fig1: una integral impropia es una transformada evaluada ----------
def fig1():
    t = np.linspace(0, 6, 500)
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.6))
    ax[0].plot(t, t**2, color=AZUL, label="$f(t)=t^2$")
    ax[0].plot(t, 30 * np.exp(-2 * t), color=ROJO, label="$e^{-2t}$ (ampliada ×30)")
    ax[0].set_ylim(0, 36)
    ax[0].set_title("Por separado: $f(t)$ crece, la exponencial la aplasta")
    ax[0].set_xlabel("$t$")
    ax[0].legend(loc="upper center")
    ejes(ax[0])

    y = t**2 * np.exp(-2 * t)
    ax[1].plot(t, y, color=VERDE)
    ax[1].fill_between(t, 0, y, color=VERDE, alpha=0.25)
    ax[1].set_title("El producto $t^2e^{-2t}$: el área es $F(2)$")
    ax[1].set_xlabel("$t$")
    ax[1].text(2.3, 0.085, r"área $=\int_0^\infty t^2e^{-2t}\,dt$" + "\n" + r"$=F(2)=\dfrac{2}{2^3}=\dfrac{1}{4}$", fontsize=11)
    ejes(ax[1])
    guardar(fig, "02-fig1-integral-impropia-es-F-evaluada.png")


# ---------- fig2: función partida con escalones (t entre 1 y 2) ----------
def fig2():
    fig, ax = plt.subplots(1, 3, figsize=(11, 3.2), sharey=True)
    t = np.linspace(0, 3.5, 400)

    ax[0].plot([1, 3.5], [1, 3.5], color=AZUL)
    ax[0].plot([0, 1], [0, 0], color=AZUL)
    ax[0].plot([1, 1], [0, 1], ":", color=GRIS)
    ax[0].set_title("$t\\cdot E(t-1)$: prendo la recta en 1")

    ax[1].plot([2, 3.5], [2, 3.5], color=ROJO)
    ax[1].plot([0, 2], [0, 0], color=ROJO)
    ax[1].plot([2, 2], [0, 2], ":", color=GRIS)
    ax[1].set_title("$t\\cdot E(t-2)$: lo que hay que restar")

    ax[2].plot([0, 1], [0, 0], color=VERDE, lw=2)
    ax[2].plot([1, 2], [1, 2], color=VERDE, lw=2)
    ax[2].plot([2, 3.5], [0, 0], color=VERDE, lw=2)
    ax[2].plot([1, 1], [0, 1], ":", color=GRIS)
    ax[2].plot([2, 2], [0, 2], ":", color=GRIS)
    ax[2].plot(t, t, "--", color=GRIS, lw=0.8)
    ax[2].set_title("$f(t)=t\\,E(t-1)-t\\,E(t-2)$")

    for a in ax:
        a.set_xlabel("$t$")
        a.set_xticks([0, 1, 2, 3])
        a.set_ylim(-0.3, 3.6)
        ejes(a)
    guardar(fig, "02-fig2-funcion-partida-con-escalones.png")


if __name__ == "__main__":
    fig1()
    fig2()
    print("ok")
