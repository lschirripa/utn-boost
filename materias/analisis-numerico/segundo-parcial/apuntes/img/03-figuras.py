"""Figuras de la guía 03-raices-desde-cero.md.

Uso (desde la raíz del repo):
    venv/bin/python materias/analisis-numerico/segundo-parcial/apuntes/img/03-figuras.py
Genera 03-fig1 … 03-fig6 (PNG) en esta misma carpeta.
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


# ---------- fig1: separar raíces graficando dos funciones ----------
def fig1():
    x = np.linspace(-1, 2.5, 400)
    fig, ax = plt.subplots(1, 2, figsize=(10, 3.8))
    r = 0.5671433
    ax[0].plot(x, x, color=AZUL, label="$y=x$")
    ax[0].plot(x, np.exp(-x), color=ROJO, label="$y=e^{-x}$")
    ax[0].plot([r], [r], "o", color="black")
    ax[0].axvspan(0, 1, color=VERDE, alpha=0.12)
    ax[0].set_ylim(-1, 2.5)
    ax[0].set_title("Lo que dibujás a mano: dos curvas conocidas")
    ax[0].legend(loc="upper center")
    ejes(ax[0])
    ax[1].plot(x, x - np.exp(-x), color=VERDE, label="$f(x)=x-e^{-x}$")
    ax[1].plot([r], [0], "o", color="black")
    ax[1].axvspan(0, 1, color=VERDE, alpha=0.12)
    ax[1].annotate("$f(0)=-1<0$", (0, -1), (-0.95, -1.6), arrowprops={"arrowstyle": "->"})
    ax[1].annotate("$f(1)=0{,}63>0$", (1, 0.632), (1.2, -0.6), arrowprops={"arrowstyle": "->"})
    ax[1].set_ylim(-2.5, 2.5)
    ax[1].set_title("Lo que no sabés dibujar: el cruce es la raíz de $f$")
    ax[1].legend(loc="upper left")
    ejes(ax[1])
    guardar(fig, "03-fig1-separar-raices.png")


# ---------- fig2: bisección ----------
def fig2():
    f = lambda t: t - np.exp(-t)
    x = np.linspace(-0.05, 1.05, 300)
    fig, ax = plt.subplots(figsize=(8.5, 4.2))
    ax.plot(x, f(x), color=VERDE, lw=2, label="$f(x)=x-e^{-x}$")
    ejes(ax)
    a, b = 0.0, 1.0
    niveles = [-0.55, -0.68, -0.81, -0.94]
    for i, y in enumerate(niveles):
        p = (a + b) / 2
        ax.plot([a, b], [y, y], color=AZUL, lw=3, solid_capstyle="butt")
        ax.plot([p], [y], "o", color=ROJO)
        ax.text(b + 0.015, y, f"paso {i}: $[{a:g};\\ {b:g}]$,  $p={p:g}$,  $f(p)={f(p):+.3f}$", va="center", fontsize=9)
        if f(p) * f(a) > 0:
            a = p
        else:
            b = p
    ax.plot([0.5671433], [0], "o", color="black")
    ax.annotate("raíz $\\alpha\\approx0{,}567$", (0.5671, 0), (0.15, 0.35), arrowprops={"arrowstyle": "->"})
    ax.set_xlim(-0.05, 1.75)
    ax.set_ylim(-1.1, 0.75)
    ax.set_title("Bisección: cada paso se queda con la mitad donde $f$ cambia de signo")
    ax.legend(loc="upper left")
    guardar(fig, "03-fig2-biseccion.png")


# ---------- fig3: regula falsi ----------
def fig3():
    f = lambda t: t**3 - np.exp(t)
    x = np.linspace(0.95, 2.05, 300)
    fig, ax = plt.subplots(figsize=(8, 4.4))
    ax.plot(x, f(x), color=VERDE, lw=2, label="$f(x)=x^3-e^{x}$")
    ax.axhline(0, color="black", lw=0.8)
    ax.grid(alpha=0.25)
    b, xi = 2.0, 1.0
    colores = [AZUL, NARANJA, ROJO]
    for i in range(3):
        xn = b - f(b) * (b - xi) / (f(b) - f(xi))
        ax.plot([xi, b], [f(xi), f(b)], color=colores[i], lw=1.3, label=f"cuerda {i + 1}: $x_{i + 1}={xn:.4f}$")
        ax.plot([xn], [0], "o", color=colores[i], ms=5)
        ax.plot([xn, xn], [0, f(xn)], ":", color=colores[i])
        xi = xn
    ax.plot([2], [f(2)], "s", color="black")
    ax.annotate("extremo fijo $b=2$", (2, f(2)), (1.55, 0.45), arrowprops={"arrowstyle": "->"})
    ax.annotate("$x_0=a=1$", (1, f(1)), (1.05, -1.2), arrowprops={"arrowstyle": "->"})
    ax.set_title("Regula Falsi: cuerdas que pivotean en el extremo fijo ($f'>0$, $f''>0$ ⇒ se fija $b$)")
    ax.legend(loc="upper left", fontsize=9)
    guardar(fig, "03-fig3-regula-falsi.png")


# ---------- fig4: punto fijo (telaraña) ----------
def telarana(ax, g, x0, n, lo, hi, titulo, etiqueta):
    x = np.linspace(lo, hi, 300)
    ax.plot(x, x, color=GRIS, lw=1, label="$y=x$")
    ax.plot(x, g(x), color=AZUL, lw=2, label=etiqueta)
    xi = x0
    ax.plot([xi, xi], [lo, g(xi)], color=ROJO, lw=1)
    for _ in range(n):
        y = g(xi)
        if not (lo - 5 < y < hi + 5):
            break
        ax.plot([xi, y], [y, y], color=ROJO, lw=1)
        ax.plot([y, y], [y, g(y)], color=ROJO, lw=1)
        xi = y
    ax.plot([x0], [lo], "o", color=ROJO, clip_on=False)
    ax.set_xlim(lo, hi)
    ax.set_ylim(lo, hi)
    ax.set_title(titulo, fontsize=10)
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(alpha=0.25)


def fig4():
    fig, ax = plt.subplots(1, 3, figsize=(13, 4.3))
    telarana(ax[0], lambda t: np.exp(-t), 0.1, 8, 0, 1, "$-1<g'<0$: converge en espiral", "$g(x)=e^{-x}$")
    telarana(ax[1], lambda t: 0.5 * np.log(t**2 + 3 * t + 2), 0.05, 8, 0, 1, "$0<g'<1$: converge en escalera", "$g(x)=\\frac{1}{2}\\ln(x^2+3x+2)$")
    telarana(ax[2], lambda t: (t - 1) * np.exp(t), 1.38, 4, 1, 2, "$g'>1$: se escapa de la raíz", "$g_1(x)=(x-1)e^{x}$")
    guardar(fig, "03-fig4-punto-fijo.png")


# ---------- fig5: Newton-Raphson ----------
def fig5():
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.2))
    f = lambda t: t**2 - 3
    df = lambda t: 2 * t
    x = np.linspace(1.2, 3.2, 200)
    ax[0].plot(x, f(x), color=VERDE, lw=2, label="$f(x)=x^2-3$")
    ax[0].axhline(0, color="black", lw=0.8)
    ax[0].grid(alpha=0.25)
    xi = 3.0
    for i, c in enumerate([AZUL, NARANJA, ROJO]):
        xn = xi - f(xi) / df(xi)
        ax[0].plot([xi, xn], [f(xi), 0], color=c, lw=1.3, label=f"tangente en $x_{i}={xi:.4g}$ → $x_{i + 1}={xn:.4f}$")
        ax[0].plot([xi, xi], [0, f(xi)], ":", color=c)
        ax[0].plot([xn], [0], "o", color=c, ms=5)
        xi = xn
    ax[0].set_title("Newton-Raphson: bajar por la tangente hasta el eje $x$")
    ax[0].legend(loc="upper left", fontsize=8)

    f2 = lambda t: t**3 - 2 * t**2 - 3 * t + 10
    df2 = lambda t: 3 * t**2 - 4 * t - 3
    x = np.linspace(-16, 3.5, 400)
    ax[1].plot(x, f2(x), color=VERDE, lw=2, label="$f(x)=x^3-2x^2-3x+10$")
    ax[1].axhline(0, color="black", lw=0.8)
    ax[1].grid(alpha=0.25)
    x0 = 1.9
    x1 = x0 - f2(x0) / df2(x0)
    ax[1].plot([x0, x1], [f2(x0), 0], color=ROJO, lw=1.3, label=f"tangente en $x_0=1{{,}}9$ ($f'=0{{,}}23$) → $x_1={x1:.1f}$")
    ax[1].plot([x0], [f2(x0)], "o", color=ROJO)
    ax[1].plot([x1], [0], "o", color=ROJO)
    ax[1].plot([-2], [0], "o", color="black")
    ax[1].annotate("única raíz: $-2$", (-2, 0), (-9, 25), arrowprops={"arrowstyle": "->"})
    ax[1].set_ylim(-40, 45)
    ax[1].set_title("Mal $x_0$: cerca de un mínimo la tangente es casi horizontal")
    ax[1].legend(loc="lower right", fontsize=8)
    guardar(fig, "03-fig5-newton-raphson.png")


# ---------- fig6: los cuatro ítems a) de parcial ----------
def fig6():
    fig, ax = plt.subplots(2, 2, figsize=(12, 8))
    a = ax[0, 0]
    x = np.linspace(0.3, 7, 500)
    a.plot(x, np.log(0.5 * x), color=ROJO, label="$\\ln(0{,}5x)$")
    a.plot(x, np.sin(2 * x), color=AZUL, label="$\\mathrm{sen}(2x)$")
    for lo in (1, 3, 4):
        a.axvspan(lo, lo + 1, color=VERDE, alpha=0.12)
    a.set_ylim(-1.6, 1.6)
    a.set_title("Tema 1: $\\ln(0{,}5x)=\\mathrm{sen}(2x)$ → $[1;2]$, $[3;4]$, $[4;5]$")
    a.legend(loc="lower right", fontsize=8)
    ejes(a)

    a = ax[0, 1]
    x = np.linspace(-3.6, 1.3, 500)
    a.plot(x, np.exp(2 * x), color=ROJO, label="$e^{2x}$")
    a.plot(x, x**2 + 3 * x + 2, color=AZUL, label="$x^2+3x+2$")
    for lo in (-3, -1, 0):
        a.axvspan(lo, lo + 1, color=VERDE, alpha=0.12)
    a.set_ylim(-1, 7)
    a.set_title("Tema 2: $e^{2x}=x^2+3x+2$ → $[-3;-2]$, $[-1;0]$, $[0;1]$")
    a.legend(loc="upper center", fontsize=8)
    ejes(a)

    a = ax[1, 0]
    x = np.linspace(-3, 3, 600)
    a.plot(x, np.exp(x), color=ROJO, label="$e^{x}$")
    y = x / (x - 1)
    y[np.abs(x - 1) < 0.03] = np.nan
    a.plot(x, y, color=AZUL, label="$x/(x-1)$")
    a.axvline(1, color=GRIS, ls="--", lw=0.8)
    for lo in (-1, 1):
        a.axvspan(lo, lo + 1, color=VERDE, alpha=0.12)
    a.set_ylim(-4, 9)
    a.set_title("1er recuperatorio: $e^{x}=x/(x-1)$ → $[-1;0]$, $[1;2]$")
    a.legend(loc="upper left", fontsize=8)
    ejes(a)

    a = ax[1, 1]
    x = np.linspace(-0.3, 10, 500)
    a.plot(x, np.exp(-2 * x), color=ROJO, label="$e^{-2x}$")
    a.plot(x, np.sin(x), color=AZUL, label="$\\mathrm{sen}(x)$")
    for lo in (0, 3):
        a.axvspan(lo, lo + 1, color=VERDE, alpha=0.12)
    a.set_ylim(-1.3, 1.6)
    a.set_title("2do recuperatorio: $e^{-2x}=\\mathrm{sen}(x)$ → infinitas; $[0;1]$, $[3;4]$, …")
    a.legend(loc="upper right", fontsize=8)
    ejes(a)
    guardar(fig, "03-fig6-parciales-item-a.png")


if __name__ == "__main__":
    fig1(); fig2(); fig3(); fig4(); fig5(); fig6()
    print("ok")
