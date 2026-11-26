"""Figuras de la práctica 05-practica-repaso-primer-parcial.md.

Uso (desde la raíz del repo):
    venv/bin/python materias/analisis-numerico/primer-parcial/apuntes/img/05-figuras.py
Genera 05-fig1 … 05-fig6 (PNG) en esta misma carpeta.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
AZUL, ROJO, VERDE, GRIS = "#1f77b4", "#d62728", "#2ca02c", "#777777"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})


def ejes(ax):
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.grid(alpha=0.25)


def guardar(fig, nombre):
    fig.tight_layout()
    fig.savefig(OUT / nombre, dpi=140)
    plt.close(fig)


def tramo(ax, a, b, f, color, lw=2.2, ls="-", label=None):
    x = np.linspace(a, b, 50)
    ax.plot(x, f(x), color=color, lw=lw, ls=ls, label=label)


# ---------- fig1: ejercicios 1.1 (par) y 1.2 (impar desplazada) ----------
def fig1():
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.4))
    # 1.1: 2t en (0,2), completada par, T = 4
    for k in (-1, 1):
        tramo(ax[0], 4 * k, 4 * k + 2, lambda x, k=k: 2 * (x - 4 * k), GRIS, 1.4, "--")
        tramo(ax[0], 4 * k - 2, 4 * k, lambda x, k=k: -2 * (x - 4 * k), GRIS, 1.4, "--")
    tramo(ax[0], 0, 2, lambda x: 2 * x, ROJO, label="dato: $2t$")
    tramo(ax[0], -2, 0, lambda x: -2 * x, VERDE, label="completado: $k(t)=-2t$")
    ax[0].axhline(2, color=AZUL, lw=1, ls=":", label="valor medio $=2$")
    ax[0].set_xlim(-6.3, 6.3)
    ax[0].set_ylim(-0.3, 5.9)
    ax[0].set_xticks(range(-6, 7, 2))
    ax[0].set_title("Ejercicio 1.1: par (solo cosenos), $T=4$")
    ax[0].legend(fontsize=8, loc="upper right")
    ejes(ax[0])
    # 1.2: t en (1,2), completada con t en (0,1), T = 2
    for k in (-2, -1, 1):
        tramo(ax[1], 2 * k, 2 * k + 2, lambda x, k=k: x - 2 * k, GRIS, 1.4, "--")
    tramo(ax[1], 1, 2, lambda x: x, ROJO, label="dato: $t$ en $(1,2)$")
    tramo(ax[1], 0, 1, lambda x: x, VERDE, label="completado: $t$ en $(0,1)$")
    ax[1].axhline(1, color=AZUL, lw=1, ls=":", label="valor medio $=1$")
    ax[1].set_xlim(-4.3, 4.3)
    ax[1].set_ylim(-0.3, 2.9)
    ax[1].set_title("Ejercicio 1.2: impar desplazada, $T=2$")
    ax[1].legend(fontsize=8, loc="upper right")
    ejes(ax[1])
    guardar(fig, "05-fig1-completar-par-e-impar-desplazada.png")


# ---------- fig2: ejercicio 1.3, pi - t completada par e impar ----------
def fig2():
    pi = np.pi
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.4))
    marcas = [-3 * pi, -2 * pi, -pi, 0, pi, 2 * pi, 3 * pi]
    nombres = ["$-3\\pi$", "$-2\\pi$", "$-\\pi$", "0", "$\\pi$", "$2\\pi$", "$3\\pi$"]
    for k in (-1, 1):
        c = 2 * pi * k
        tramo(ax[0], c, c + pi, lambda x, c=c: pi - (x - c), GRIS, 1.4, "--")
        tramo(ax[0], c - pi, c, lambda x, c=c: pi + (x - c), GRIS, 1.4, "--")
        tramo(ax[1], c, c + pi, lambda x, c=c: pi - (x - c), GRIS, 1.4, "--")
        tramo(ax[1], c - pi, c, lambda x, c=c: -pi - (x - c), GRIS, 1.4, "--")
    tramo(ax[0], 0, pi, lambda x: pi - x, ROJO, label="dato: $\\pi-t$")
    tramo(ax[0], -pi, 0, lambda x: pi + x, VERDE, label="completado: $\\pi+t$")
    ax[0].set_title("Ejercicio 1.3 a): par (solo cosenos)")
    tramo(ax[1], 0, pi, lambda x: pi - x, ROJO, label="dato: $\\pi-t$")
    tramo(ax[1], -pi, 0, lambda x: -pi - x, VERDE, label="completado: $-\\pi-t$")
    ax[1].set_title("Ejercicio 1.3 b): impar (solo senos)")
    for a in ax:
        a.set_xticks(marcas)
        a.set_xticklabels(nombres)
        a.set_yticks([-pi, 0, pi])
        a.set_yticklabels(["$-\\pi$", "0", "$\\pi$"])
        a.set_xlim(-3.2 * pi, 3.2 * pi)
        a.legend(fontsize=8, loc="lower right")
        ejes(a)
    guardar(fig, "05-fig2-pi-menos-t-par-e-impar.png")


# ---------- fig3: ejercicio 1.4, |t| - 3 con T = 12 ----------
def fig3():
    fig, ax = plt.subplots(figsize=(8, 3.2))
    for k in (-1, 0, 1):
        c = 12 * k
        col, lw, ls = (ROJO, 2.2, "-") if k == 0 else (GRIS, 1.4, "--")
        tramo(ax, c - 6, c, lambda x, c=c: -(x - c) - 3, col, lw, ls)
        tramo(ax, c, c + 6, lambda x, c=c: (x - c) - 3, col, lw, ls)
    ax.annotate("", xy=(8, -1), xytext=(2, -1), arrowprops=dict(arrowstyle="<->", color=AZUL))
    ax.text(5, -0.75, "$T/2=6$", color=AZUL, ha="center")
    ax.plot([2, 8], [-1, 1], "o", color=AZUL)
    ax.text(2, -1.6, "$f(2)=-1$", color=AZUL, ha="center", fontsize=9)
    ax.text(8, 1.3, "$f(8)=+1$", color=AZUL, ha="center", fontsize=9)
    ax.set_xticks(range(-18, 19, 6))
    ax.set_xlim(-18.5, 18.5)
    ax.set_ylim(-3.6, 3.6)
    ax.set_title("Ejercicio 1.4: $f(t)=|t|-3$ en $(-6,6)$, $T=12$: par y con simetría de media onda")
    ejes(ax)
    guardar(fig, "05-fig3-modulo-t-menos-3.png")


# ---------- fig4: ejercicio 3.1, corte por el eje real ----------
def fig4():
    fig, ax = plt.subplots(figsize=(8, 3.6))
    for a, b in ((-8, -0.02), (0.02, 8)):
        x = np.linspace(a, b, 3000)
        ax.plot(x, 25 * np.abs(x - 4) / (np.abs(x) * (x**2 + 4 * x + 5)), color=ROJO, lw=2)
    ax.axvline(-2, color=GRIS, lw=1, ls=":")
    ax.plot([4], [0], "o", color=AZUL)
    ax.text(4, 12, "cero en $\\sigma=4$\n(toca el eje)", color=AZUL, ha="center", fontsize=9)
    ax.text(-2, 92, "lomo en $\\sigma=-2$\n(polos $-2\\pm j$)", ha="center", fontsize=9)
    ax.text(0.35, 150, "polo en $\\sigma=0$\n(asíntota vertical)", fontsize=9)
    ax.text(-7.8, 12, "$\\to 0$ (cero en $\\infty$)", fontsize=9)
    ax.set_ylim(-5, 180)
    ax.set_xlim(-8, 8)
    ax.set_xlabel("$\\sigma=\\mathrm{Re}(s)$")
    ax.set_ylabel("$|G(\\sigma)|$")
    ax.set_title("Ejercicio 3.1: corte de $|G(s)|$ por el eje real, $G(s)=\\dfrac{25(s-4)}{s\\,(s^2+4s+5)}$", fontsize=10)
    ejes(ax)
    guardar(fig, "05-fig4-corte-eje-real-k7.png")


# ---------- fig5: ejercicio 3.2, gráfico del enunciado ----------
def fig5():
    fig, ax = plt.subplots(figsize=(8, 3.4))
    K = 3 * np.sqrt(26)
    for a, b in ((-9, 0.985), (1.015, 6)):
        x = np.linspace(a, b, 3000)
        ax.plot(x, K * np.abs(x) / (np.abs(x - 1) * (x**2 + 4 * x + 5)), color="black", lw=1.8)
    ax.axvline(1, color=GRIS, lw=1, ls="--")
    ax.set_ylim(-1, 30)
    ax.set_xlim(-9, 6)
    ax.set_xticks([-2, 1])
    ax.set_yticks([])
    ax.set_xlabel("$\\sigma=\\mathrm{Re}(s)$")
    ax.set_ylabel("$|G(s)|$")
    ax.set_title("Ejercicio 3.2 (enunciado): corte de $|G(s)|$ por el eje real", fontsize=10)
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    guardar(fig, "05-fig5-enunciado-corte-g-desde-grafico.png")


# ---------- fig6: ejercicio 3.2, constelación y vectores hasta 1 + j ----------
def fig6():
    fig, ax = plt.subplots(figsize=(6.4, 4.2))
    polos = [(1, 0), (-2, 1), (-2, -1)]
    largos = ["$1$", "$3$", "$\\sqrt{13}$"]
    for (px, py), l in zip(polos, largos):
        ax.plot([px], [py], "x", color=ROJO, ms=11, mew=2.5)
        ax.annotate("", xy=(1, 1), xytext=(px, py), arrowprops=dict(arrowstyle="->", color=ROJO, lw=1.4))
        ax.text((px + 1) / 2 + 0.12, (py + 1) / 2 + 0.1, l, color=ROJO)
    ax.plot([0], [0], "o", mfc="none", color=AZUL, ms=11, mew=2)
    ax.annotate("", xy=(1, 1), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=AZUL, lw=1.4))
    ax.text(0.2, 0.62, "$\\sqrt{2}$", color=AZUL)
    ax.plot([1], [1], "o", color=VERDE)
    ax.text(1.1, 1.08, "$1+j$", color=VERDE)
    ax.set_xlim(-3, 2.2)
    ax.set_ylim(-1.7, 1.8)
    ax.set_aspect("equal")
    ax.set_xlabel("Re")
    ax.set_ylabel("Im")
    ax.set_title("Ejercicio 3.2: constelación (× polos, ○ cero) y vectores hasta $1+j$", fontsize=10)
    ejes(ax)
    guardar(fig, "05-fig6-constelacion-modulo-grafico.png")


if __name__ == "__main__":
    for f in (fig1, fig2, fig3, fig4, fig5, fig6):
        f()
    print("ok")
