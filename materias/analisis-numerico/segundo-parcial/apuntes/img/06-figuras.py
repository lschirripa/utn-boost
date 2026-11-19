"""Figuras de la guía 06-integracion-desde-cero.md.

Uso (desde la raíz del repo):
    venv/bin/python materias/analisis-numerico/segundo-parcial/apuntes/img/06-figuras.py
Genera 06-fig1 … 06-fig5 (PNG) en esta misma carpeta.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
AZUL, ROJO, VERDE, GRIS, NARANJA = "#1f77b4", "#d62728", "#2ca02c", "#555555", "#ff7f0e"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})


def guardar(fig, nombre):
    fig.tight_layout()
    fig.savefig(OUT / nombre, dpi=140)
    plt.close(fig)


def parabola(xs, ys, t):
    """Parábola interpolante por 3 puntos (Lagrange)."""
    (x0, x1, x2), (y0, y1, y2) = xs, ys
    return (
        y0 * (t - x1) * (t - x2) / ((x0 - x1) * (x0 - x2))
        + y1 * (t - x0) * (t - x2) / ((x1 - x0) * (x1 - x2))
        + y2 * (t - x0) * (t - x1) / ((x2 - x0) * (x2 - x1))
    )


# ---------------------------------------------------------------- fig 1
def fig1():
    f = lambda t: np.exp(-0.9 * t) * 6 + 0.6 * np.sin(1.6 * t) + 1.2
    a, b, N = 0.0, 4.0, 4
    xs = np.linspace(a, b, N + 1)
    t = np.linspace(a, b, 400)
    fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.9), sharey=True)

    ax = axs[0]
    ax.plot(t, f(t), color="black", lw=2, label="f(x)")
    for i in range(N):
        ax.fill([xs[i], xs[i], xs[i + 1], xs[i + 1]], [0, f(xs[i]), f(xs[i + 1]), 0],
                color=AZUL, alpha=0.25, edgecolor=AZUL, lw=1.2)
    ax.plot(xs, f(xs), "o-", color=AZUL, lw=1.5, label="rectas (grado 1)")
    ax.set_title("Trapecios: une de a 2 puntos con rectas\n(N = 4 subintervalos, cualquier N entero)")
    ax.set_xticks(xs)
    ax.set_xticklabels([f"$x_{i}$" for i in range(N + 1)])
    ax.annotate("", xy=(xs[1], 0.35), xytext=(xs[0], 0.35), arrowprops=dict(arrowstyle="<->", color=GRIS))
    ax.text((xs[0] + xs[1]) / 2, 0.5, "h", ha="center", color=GRIS)
    ax.legend(frameon=False)

    ax = axs[1]
    ax.plot(t, f(t), color="black", lw=2, label="f(x)")
    for k, col in zip(range(0, N, 2), (VERDE, NARANJA)):
        tt = np.linspace(xs[k], xs[k + 2], 120)
        pp = parabola(xs[k:k + 3], f(xs[k:k + 3]), tt)
        ax.fill_between(tt, 0, pp, color=col, alpha=0.25)
        ax.plot(tt, pp, color=col, lw=1.6, label=f"parábola {k // 2 + 1} (3 puntos)")
    ax.plot(xs, f(xs), "o", color=GRIS)
    ax.set_title("Simpson: une de a 3 puntos con parábolas\n(cada parábola gasta 2 subintervalos ⇒ N par)")
    ax.set_xticks(xs)
    ax.set_xticklabels([f"$x_{i}$" for i in range(N + 1)])
    ax.legend(frameon=False)
    for ax in axs:
        ax.set_ylim(0, 7.6)
        ax.axhline(0, color="black", lw=0.8)
    guardar(fig, "06-fig1-trapecios-vs-simpson.png")


# ---------------------------------------------------------------- fig 2
def fig2():
    fig, axs = plt.subplots(1, 2, figsize=(10, 3.6))
    a, b = 0.5, 3.0
    t = np.linspace(a, b, 300)
    casos = [
        (lambda u: 0.45 * (u - 0.6) ** 2 + 0.7, "Cóncava hacia ARRIBA (f'' > 0)\nla recta queda por encima ⇒ $A_T$ > área exacta",
         "exceso"),
        (lambda u: -0.45 * (u - 2.6) ** 2 + 3.2, "Cóncava hacia ABAJO (f'' < 0)\nla recta queda por debajo ⇒ $A_T$ < área exacta",
         "defecto"),
    ]
    for ax, (f, titulo, tipo) in zip(axs, casos):
        ax.plot(t, f(t), color="black", lw=2)
        recta = f(a) + (f(b) - f(a)) / (b - a) * (t - a)
        ax.plot([a, b], [f(a), f(b)], "o-", color=AZUL, lw=1.6)
        ax.fill_between(t, 0, np.minimum(recta, f(t)), color=AZUL, alpha=0.18)
        ax.fill_between(t, f(t), recta, color=ROJO, alpha=0.45, hatch="///", edgecolor=ROJO)
        ax.text(1.75, (f(1.75) + (f(a) + (f(b) - f(a)) / (b - a) * (1.75 - a))) / 2, "$e_T$", color=ROJO,
                ha="center", va="center", fontsize=13, fontweight="bold")
        ax.set_title(titulo)
        ax.set_xticks([a, b])
        ax.set_xticklabels(["a", "b"])
        ax.set_yticks([])
        ax.set_ylim(0, 3.6)
        ax.axhline(0, color="black", lw=0.8)
        ax.text(1.75, 0.25, f"trapecio (error por {tipo})", ha="center", color=AZUL)
    guardar(fig, "06-fig2-concavidad-defecto-exceso.png")


# ---------------------------------------------------------------- fig 3
def fig3():
    casos = [
        ("Tema 1: $f''=e^{x}(x^3+6x^2+6x-6)$ en [−7; −5]",
         lambda u: np.exp(u) * (u ** 3 + 6 * u ** 2 + 6 * u - 6), -7, -5, [-6]),
        ("Tema 2: $f''=e^{x}(x^2-5x+7)$ en [0; 2]",
         lambda u: np.exp(u) * (u ** 2 - 5 * u + 7), 0, 2, [1]),
        ("1er recup.: $f''=(2\\ln x-1)/x^3$ en [1; 3]",
         lambda u: (2 * np.log(u) - 1) / u ** 3, 1, 3, [np.exp(5 / 6)]),
        ("2do recup.: $f''=e^{-x}(x^2-4x+1)$ en [4; 6]",
         lambda u: np.exp(-u) * (u ** 2 - 4 * u + 1), 4, 6, [5]),
    ]
    fig, axs = plt.subplots(2, 2, figsize=(10.5, 6.4))
    for ax, (titulo, f2, a, b, crit) in zip(axs.ravel(), casos):
        t = np.linspace(a, b, 400)
        ax.plot(t, np.abs(f2(t)), color="black", lw=2, label="$|f''(x)|$")
        cand = [(a, "extremo"), (b, "extremo")] + [(c, "punto crítico") for c in crit]
        vals = [abs(f2(c)) for c, _ in cand]
        imax = int(np.argmax(vals))
        for k, ((c, tipo), v) in enumerate(zip(cand, vals)):
            col = ROJO if k == imax else (AZUL if tipo == "extremo" else NARANJA)
            ax.plot([c], [v], "o", color=col, ms=8 if k == imax else 6)
            ax.annotate(f"{v:.4f}".replace(".", ","), (c, v), textcoords="offset points",
                        xytext=(0, 8 if k != imax else -16), ha="center", color=col,
                        fontweight="bold" if k == imax else "normal")
        ax.set_title(titulo, fontsize=10)
        ax.set_ylim(0, max(vals) * 1.25)
        ax.grid(alpha=0.25)
    fig.suptitle("Los 4 parciales 2025: dónde está el máximo de |f''| (rojo). Azul = extremos, naranja = punto crítico",
                 fontsize=10.5)
    guardar(fig, "06-fig3-maximo-f-segunda-parciales.png")


# ---------------------------------------------------------------- fig 4
def fig4():
    f = lambda u: 0.35 * u ** 3 - 0.6 * u + 1.2
    df = lambda u: 1.05 * u ** 2 - 0.6
    xi, h = 1.3, 0.7
    t = np.linspace(0.3, 2.4, 300)
    fig, ax = plt.subplots(figsize=(7.2, 4.3))
    ax.plot(t, f(t), color="black", lw=2, label="f(x)")
    A, B, C = (xi - h, f(xi - h)), (xi, f(xi)), (xi + h, f(xi + h))
    tt = np.linspace(xi - 0.75, xi + 0.75, 10)
    ax.plot(tt, f(xi) + df(xi) * (tt - xi), "--", color=GRIS, lw=1.5, label="tangente en $x_i$ (derivada exacta)")
    ax.plot([B[0], C[0]], [B[1], C[1]], color=VERDE, lw=2, label="progresiva: pendiente BC")
    ax.plot([A[0], B[0]], [A[1], B[1]], color=NARANJA, lw=2, label="regresiva: pendiente AB")
    ax.plot([A[0], C[0]], [A[1], C[1]], color=ROJO, lw=2, label="central: pendiente AC (la mejor)")
    for (px, py), nombre in zip((A, B, C), "ABC"):
        ax.plot([px], [py], "o", color="black")
        ax.annotate(nombre, (px, py), textcoords="offset points", xytext=(-10, 8), fontweight="bold")
    ax.set_xticks([xi - h, xi, xi + h])
    ax.set_xticklabels(["$x_i-h$", "$x_i$", "$x_i+h$"])
    ax.set_yticks([])
    ax.legend(frameon=False, loc="upper left")
    ax.set_title("Las tres diferencias usan una secante en lugar de la tangente")
    guardar(fig, "06-fig4-diferencias-progresiva-regresiva-central.png")


# ---------------------------------------------------------------- fig 5
def fig5():
    fig, axs = plt.subplots(1, 2, figsize=(10.5, 3.7))
    ax = axs[0]
    t = np.linspace(-np.pi, np.pi, 400)
    ax.plot(t, np.sin(t), color="black", lw=2)
    xs = np.linspace(-np.pi, np.pi, 5)
    ax.plot(xs, np.sin(xs), "o-", color=AZUL)
    ax.fill_between(xs, 0, np.sin(xs), color=AZUL, alpha=0.25)
    ax.axhline(0, color="black", lw=0.8)
    ax.set_xticks([-np.pi, 0, np.pi])
    ax.set_xticklabels(["−π", "0", "π"])
    ax.set_title("sen(x) en [−π; π]: los trapecios no calcan la curva,\npero lo de abajo cancela lo de arriba ⇒ $A_T$ = 0 = exacto")

    ax = axs[1]
    t = np.linspace(-1, 1, 200)
    ax.plot(t, np.abs(t), color="black", lw=3, label="|x| (y también Trapecios con h = 1)")
    ax.plot(t, t ** 2, color=VERDE, lw=2, label="parábola de Simpson por (−1;1), (0;0), (1;1)")
    ax.fill_between(t, t ** 2, np.abs(t), color=ROJO, alpha=0.35, label="error de Simpson")
    ax.plot([-1, 0, 1], [1, 0, 1], "o", color="black")
    ax.axhline(0, color="black", lw=0.8)
    ax.set_xticks([-1, 0, 1])
    ax.set_title("|x| en [−1; 1] con h = 1: Trapecios da 1 (exacto),\nSimpson da 2/3")
    ax.legend(frameon=False, fontsize=8.5, loc="upper center")
    guardar(fig, "06-fig5-contraejemplos.png")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    fig4()
    fig5()
    print("OK: 06-fig1 … 06-fig5 en", OUT)
