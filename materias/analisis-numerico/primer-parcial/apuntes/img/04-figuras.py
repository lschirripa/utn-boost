"""Figuras de la guía 04-transformada-z-desde-cero.md.

Uso (desde la raíz del repo):
    venv/bin/python materias/analisis-numerico/primer-parcial/apuntes/img/04-figuras.py
Genera 04-fig1 … 04-fig5 (PNG) en esta misma carpeta.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
AZUL, ROJO, VERDE, GRIS, NARANJA = "#1f77b4", "#d62728", "#2ca02c", "#555555", "#ff7f0e"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
T = np.linspace(0, 2 * np.pi, 400)


def guardar(fig, nombre):
    fig.tight_layout()
    fig.savefig(OUT / nombre, dpi=140)
    plt.close(fig)


def plano(ax, lim):
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.set_xlabel("Re(z)")
    ax.set_ylabel("Im(z)")
    ax.grid(alpha=0.25)


def exterior(ax, radio, lim, color, alpha=0.18, hatch=None, etiqueta=None):
    """Sombrea |z| > radio (hasta el borde del dibujo) y dibuja el borde punteado."""
    big = lim * 1.5
    ax.fill(
        np.concatenate([big * np.cos(T), radio * np.cos(T[::-1])]),
        np.concatenate([big * np.sin(T), radio * np.sin(T[::-1])]),
        facecolor=color if hatch is None else "none",
        edgecolor=color if hatch else "none",
        alpha=alpha if hatch is None else 0.55,
        hatch=hatch,
        lw=0,
        label=etiqueta,
    )
    ax.plot(radio * np.cos(T), radio * np.sin(T), "--", color=color, lw=1.8)


def bastones(ax, n, x, color=AZUL, **kw):
    ax.vlines(n, 0, x, color=color, lw=1.6)
    ax.plot(n, x, "o", color=color, ms=6, **kw)
    ax.axhline(0, color="black", lw=0.8)


# ---------- fig1: región de convergencia de u(n) y de a^n ----------
def fig1():
    fig, ax = plt.subplots(1, 2, figsize=(9.6, 4.6))
    plano(ax[0], 2.6)
    exterior(ax[0], 1, 2.6, AZUL)
    ax[0].set_title("Escalón $u(n)$: razón $1/z$\nconverge si $|z|>1$")
    ax[0].annotate("borde punteado:\n$|z|=1$ no entra", (0.707, 0.707), (1.05, 1.75), arrowprops={"arrowstyle": "->"})
    ax[0].text(0, 0, "no\nconverge", ha="center", va="center", color=GRIS)
    plano(ax[1], 5.2)
    exterior(ax[1], 3, 5.2, ROJO)
    ax[1].plot([0, 3 * np.cos(0.8)], [0, 3 * np.sin(0.8)], color=GRIS, lw=1.2)
    ax[1].text(0.55, 1.5, "$R=|a|$", color=GRIS)
    ax[1].set_title("$x(n)=a^n$ (dibujado con $a=3$): razón $a/z$\nconverge si $|z|>|a|$")
    ax[1].text(0, -1.2, "no\nconverge", ha="center", va="center", color=GRIS)
    guardar(fig, "04-fig1-region-convergencia.png")


# ---------- fig2: una sucesión con una regla para pares y otra para impares ----------
def fig2():
    n = np.arange(0, 9)
    x = np.where(n % 2 == 0, 2 * 3.0 ** (-n), 0.5**n)
    fig, ax = plt.subplots(figsize=(8.6, 3.6))
    par = n % 2 == 0
    bastones(ax, n[par], x[par], AZUL, label=r"$n$ par: $2\cdot3^{-n}$  →  $n=2k$")
    bastones(ax, n[~par], x[~par], ROJO, label=r"$n$ impar: $(1/2)^{n}$  →  $n=2k+1$")
    for ni, xi in zip(n[:5], x[:5]):
        ax.annotate(f"{xi:.3g}".replace(".", ","), (ni, xi), (ni + 0.12, xi + 0.07), fontsize=9)
    ax.set_xticks(n)
    ax.set_xlabel("$n$")
    ax.set_ylabel("$x(n)$")
    ax.set_ylim(-0.1, 2.35)
    ax.set_title("Dos sucesiones intercaladas: se transforman por separado (dos series geométricas)")
    ax.legend(loc="upper right")
    ax.grid(alpha=0.25)
    guardar(fig, "04-fig2-pares-impares.png")


# ---------- fig3: la ROC total es la intersección (parcial 2025, Tema 1) ----------
def fig3():
    fig, ax = plt.subplots(1, 2, figsize=(9.6, 4.6))
    lim = 3.2
    plano(ax[0], lim)
    exterior(ax[0], 0.25, lim, ROJO, hatch="\\\\", etiqueta=r"impares: $|z|>\frac{1}{4}$")
    exterior(ax[0], 2, lim, AZUL, hatch="//", etiqueta="pares: $|z|>2$")
    ax[0].set_title("Cada serie geométrica pide lo suyo")
    ax[0].legend(loc="lower left", framealpha=0.95)
    plano(ax[1], lim)
    exterior(ax[1], 2, lim, VERDE, alpha=0.25)
    ax[1].plot(0.25 * np.cos(T), 0.25 * np.sin(T), ":", color=GRIS, lw=1)
    ax[1].set_title("Las dos a la vez (intersección):\nel exterior de la circunferencia más grande, $|z|>2$")
    ax[1].text(0, 1.0, "acá la serie de los\npares no converge", ha="center", va="center", color=GRIS, fontsize=9)
    guardar(fig, "04-fig3-interseccion-roc.png")


# ---------- fig4: la secuencia finita del gráfico (guía ej. 2 y recuperatorio 2025) ----------
def fig4():
    n = np.arange(-1, 7)
    x = np.array([0, 0, 1, 3, 2, 1, 0, 0])
    fig, ax = plt.subplots(figsize=(7.2, 3.4))
    bastones(ax, n, x)
    for ni, xi in zip(n, x):
        if xi:
            ax.annotate(f"$x({ni})={xi}$", (ni, xi), (ni + 0.1, xi + 0.15), fontsize=9)
    ax.axvline(0, color="black", lw=0.8)
    ax.set_xticks(n)
    ax.set_yticks([0, 1, 2, 3])
    ax.set_ylim(-0.3, 3.8)
    ax.set_xlabel("$n$")
    ax.set_ylabel("$x(n)$")
    ax.set_title("Secuencia finita: cada bastón de altura $x(n)$ aporta $x(n)\\,z^{-n}$")
    ax.grid(alpha=0.25)
    guardar(fig, "04-fig4-secuencia-finita.png")


# ---------- fig5: desplazar a derecha y a izquierda ----------
def fig5():
    n0 = np.arange(0, 6)
    x0 = np.array([3, 1, 1.5, 2.5, 1, 1])
    fig, ax = plt.subplots(1, 3, figsize=(11.4, 3.5), sharey=True)
    for a in ax:
        a.set_xlim(-3.5, 8.5)
        a.set_xticks(np.arange(-3, 9))
        a.axvline(0, color="black", lw=0.8)
        a.set_ylim(-0.4, 3.8)
        a.set_xlabel("$n$")
        a.grid(alpha=0.25)
    bastones(ax[0], n0, x0)
    ax[0].set_title("$x(n)$  →  $X(z)$")
    ax[0].annotate("$x(0)$", (0, 3), (-2.6, 3.3), arrowprops={"arrowstyle": "->"}, fontsize=9)
    ax[0].annotate("$x(1)$", (1, 1), (1.4, 2.6), arrowprops={"arrowstyle": "->"}, fontsize=9)
    bastones(ax[1], n0 + 2, x0, VERDE)
    ax[1].set_title("a derecha: $x(n-2)$  →  $z^{-2}X(z)$")
    ax[1].text(-3.2, 3.3, "no se pierde nada", color=GRIS, fontsize=9)
    vivos = n0 - 2 >= 0
    bastones(ax[2], (n0 - 2)[vivos], x0[vivos], NARANJA)
    ax[2].vlines((n0 - 2)[~vivos], 0, x0[~vivos], color=ROJO, lw=1.4, linestyles="dashed")
    ax[2].plot((n0 - 2)[~vivos], x0[~vivos], "x", color=ROJO, ms=9, mew=2)
    ax[2].set_title("a izquierda: $x(n+2)$  →  $z^{2}X(z)-z^{2}x(0)-z\\,x(1)$")
    ax[2].text(1.2, 3.25, "✗ = bastones que caen en\n$n<0$: se restan", color=ROJO, fontsize=9)
    guardar(fig, "04-fig5-desplazamientos.png")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    fig4()
    fig5()
    print("OK: 5 figuras en", OUT)
