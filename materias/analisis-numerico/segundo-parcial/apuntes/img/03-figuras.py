"""Figuras de la guía 03-interpolacion-desde-cero.md.

Uso (desde la raíz del repo):
    venv/bin/python materias/analisis-numerico/segundo-parcial/apuntes/img/03-figuras.py
Genera 03-fig1 … 03-fig5 (PNG) en esta misma carpeta.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
AZUL, ROJO, VERDE, GRIS, NARANJA = "#1f77b4", "#d62728", "#2ca02c", "#555555", "#ff7f0e"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})


def ejes(ax):
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.grid(alpha=0.25)


def guardar(fig, nombre):
    fig.tight_layout()
    fig.savefig(OUT / nombre, dpi=140)
    plt.close(fig)


def interpolante(xs, ys):
    """Coeficientes (potencias decrecientes) del polinomio que pasa por todos los puntos."""
    return np.polyfit(xs, ys, len(xs) - 1)


# ---------- fig1: infinitas funciones interpoladoras (ejemplo del PDF de clase) ----------
def fig1():
    x = np.linspace(-0.25, 3.25, 600)
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.plot(x, x, color=AZUL, lw=2, label="$p_1(x)=x$  (grado 1: el de menor grado)")
    ax.plot(x, x + np.sin(2 * np.pi * x), color=NARANJA, label=r"$p_2(x)=x+\mathrm{sen}(2\pi x)$")
    ax.plot(x, x - x**2 * (1 - np.cos(2 * np.pi * x)), color=VERDE, label=r"$p_3(x)=x-x^2[1-\cos(2\pi x)]$")
    ax.plot(x, x**4 - 6 * x**3 + 11 * x**2 - 5 * x, color=ROJO, label="$p_4(x)=x^4-6x^3+11x^2-5x$")
    ax.plot([0, 1, 2, 3], [0, 1, 2, 3], "o", color="black", zorder=5, label="datos")
    ax.set_ylim(-4, 6)
    ax.set_title("Cuatro funciones distintas que pasan por los mismos 4 puntos")
    ax.legend(fontsize=8, loc="upper left")
    ejes(ax)
    guardar(fig, "03-fig1-infinitas-interpolantes.png")


# ---------- fig2: el teorema con 1 y 2 puntos / infinitos de grado mayor ----------
def fig2():
    x = np.linspace(-0.5, 4.5, 300)
    fig, ax = plt.subplots(1, 3, figsize=(12, 3.6))
    # un punto: una sola constante, infinitas rectas
    ax[0].axhline(2, color=ROJO, lw=2, label="grado 0: una sola")
    for m in (-1.2, -0.5, 0.6, 1.4):
        ax[0].plot(x, 2 + m * (x - 2), color=GRIS, lw=0.9, alpha=0.7)
    ax[0].plot([], [], color=GRIS, lw=0.9, label="grado 1: infinitas")
    ax[0].plot([2], [2], "o", color="black", zorder=5)
    ax[0].set_title("1 punto")
    # dos puntos: una recta, infinitas parábolas
    ax[1].plot(x, 1 + 0.75 * (x - 1), color=ROJO, lw=2, label="grado $\\leq 1$: una sola")
    for c in (-1.0, -0.4, 0.5, 1.1):
        ax[1].plot(x, 1 + 0.75 * (x - 1) + c * (x - 1) * (x - 3), color=GRIS, lw=0.9, alpha=0.7)
    ax[1].plot([], [], color=GRIS, lw=0.9, label="grado 2: infinitas")
    ax[1].plot([1, 3], [1, 2.5], "o", color="black", zorder=5)
    ax[1].set_title("2 puntos")
    # tres puntos: una parábola, infinitas cúbicas
    c2 = interpolante([0.5, 2, 3.5], [1, 3, 1.5])
    ax[2].plot(x, np.polyval(c2, x), color=ROJO, lw=2, label="grado $\\leq 2$: una sola")
    for c in (-0.5, -0.2, 0.25, 0.55):
        ax[2].plot(x, np.polyval(c2, x) + c * (x - 0.5) * (x - 2) * (x - 3.5), color=GRIS, lw=0.9, alpha=0.7)
    ax[2].plot([], [], color=GRIS, lw=0.9, label="grado 3: infinitas")
    ax[2].plot([0.5, 2, 3.5], [1, 3, 1.5], "o", color="black", zorder=5)
    ax[2].set_title("3 puntos")
    for a in ax:
        a.set_ylim(-1, 5)
        a.legend(fontsize=8, loc="upper left")
        ejes(a)
    guardar(fig, "03-fig2-teorema-unicidad.png")


# ---------- fig3: agregar un punto: se mantiene el grado o salta al máximo ----------
def fig3():
    x = np.linspace(0, 5, 300)
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.8))
    for a in ax:
        a.plot([1, 2.5], [2, 2], "o", color="black", zorder=5)
        a.annotate("$P_1$", (1, 2), (0.85, 2.25))
        a.annotate("$P_2$", (2.5, 2), (2.35, 2.25))
        a.set_ylim(0, 5)
        ejes(a)
    ax[0].axhline(2, color=ROJO, lw=2)
    ax[0].plot([4], [2], "o", color=AZUL, zorder=5)
    ax[0].annotate("$P_3$ alineado", (4, 2), (3.45, 2.3), color=AZUL)
    ax[0].set_title("$P_3$ sigue el patrón: el grado no cambia (0)")
    c = interpolante([1, 2.5, 4], [2, 2, 3.8])
    ax[1].axhline(2, color=ROJO, lw=1, ls="--", alpha=0.6)
    ax[1].plot(x, np.polyval(c, x), color=AZUL, lw=2)
    ax[1].plot([4], [3.8], "o", color=AZUL, zorder=5)
    ax[1].annotate("$P_3$ fuera del patrón", (4, 3.8), (2.6, 4.3), color=AZUL)
    ax[1].set_title("$P_3$ no lo sigue: salta de grado 0 a grado 2")
    guardar(fig, "03-fig3-agregar-punto.png")


# ---------- fig4: ejercicio 11 de la guía: (6;81) mantiene la cúbica, (6;80) salta a grado 5 ----------
def fig4():
    xs, ys = [1, 3, 4, 5, 7], [1, 3, 13, 37, 151]
    x = np.linspace(0.6, 7.3, 500)
    p3 = lambda t: t**3 - 5 * t**2 + 8 * t - 3
    c5 = interpolante(xs + [6], ys + [80])
    fig, ax = plt.subplots(1, 2, figsize=(11, 4))
    ax[0].plot(x, p3(x), color=ROJO, lw=2, label="$P(x)=x^3-5x^2+8x-3$ (grado 3)")
    ax[0].plot(x, np.polyval(c5, x), color=AZUL, lw=1.6, ls="--", label="interpolante con $(6;80)$ (grado 5)")
    ax[0].plot(xs, ys, "o", color="black", zorder=5, label="los 5 datos")
    ax[0].plot([6], [81], "s", color=ROJO, zorder=6)
    ax[0].plot([6], [80], "s", color=AZUL, zorder=6)
    ax[0].set_title("A escala completa casi no se distinguen")
    ax[0].legend(fontsize=8, loc="upper left")
    ejes(ax[0])
    ax[1].plot(x, np.polyval(c5, x) - p3(x), color=AZUL, lw=2)
    ax[1].plot(xs, [0] * 5, "o", color="black", zorder=5)
    ax[1].plot([6], [-1], "s", color=AZUL, zorder=6)
    ax[1].annotate("en $x=6$ baja 1:\n$80$ en vez de $81$", (6, -1), (3.6, -1.1), arrowprops={"arrowstyle": "->"})
    ax[1].set_title("Diferencia (grado 5) − (grado 3): cero en los 5 datos")
    ejes(ax[1])
    guardar(fig, "03-fig4-salto-de-grado.png")


# ---------- fig5: parcial 2025 Tema 1: la cúbica por los puntos conocidos fija a y b ----------
def fig5():
    p = lambda t: 0.5 * t**3 + 3 * t - 3
    x = np.linspace(0.5, 8.4, 400)
    fig, ax = plt.subplots(figsize=(7.5, 4.3))
    ax.plot(x, p(x), color=ROJO, lw=2, label=r"$P(x)=\frac{1}{2}x^3+3x-3$ (por los 4 datos conocidos)")
    ax.plot([1, 4, 5, 6], [0.5, 41, 74.5, 123], "o", color="black", zorder=5, label="datos conocidos")
    ax.plot([2], [7], "s", color=VERDE, zorder=6, label="$a=P(2)=7$: sigue en la cúbica")
    ax.plot([8], [277], "s", color=VERDE, zorder=6)
    ax.annotate("$b=P(8)=277$:\ntodo queda en grado 3", (8, 277), (5.3, 265), arrowprops={"arrowstyle": "->"})
    ax.plot([8, 8], [150, 220], "x", color=AZUL, ms=9, zorder=6, label=r"$b\neq 277$: salta a grado 5")
    ax.set_title("Parcial 2025, Tema 1: dónde tienen que caer $a$ y $b$")
    ax.legend(fontsize=8, loc="upper left")
    ejes(ax)
    guardar(fig, "03-fig5-parcial-tema1.png")


# ---------- fig6: interpolar vs aproximar (ejemplo "a tener en cuenta" del teórico) ----------
def fig6():
    X = [0.1, 2.5, 4.3, 4.5, 5.3, 7.8]
    p5 = lambda t: t**5 / 5 - 4 * t**4 + 86 / 3 * t**3 - 88 * t**2 + 105 * t + 10
    Y = [p5(v) for v in X]
    x = np.linspace(0, 8, 500)
    fig, ax = plt.subplots(figsize=(7.5, 4.2))
    ax.plot(x, p5(x), color=ROJO, lw=1.8, label="interpolante (grado 5): pasa por todos, pero oscila")
    ax.plot(x, -0.3889 * x**2 + 6.6082 * x + 19.164, color=AZUL, lw=1.8, label="parábola de ajuste: no pasa por ninguno, sigue la tendencia")
    ax.plot(X, Y, "o", color="black", zorder=5, label="datos")
    ax.set_ylim(0, 72)
    ax.set_title("¿Interpolar o aproximar? (ejemplo del teórico de cátedra)")
    ax.legend(fontsize=8, loc="lower right")
    ejes(ax)
    guardar(fig, "03-fig6-interpolar-vs-aproximar.png")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    fig4()
    fig5()
    fig6()
    print("Figuras generadas en", OUT)
