"""Figuras de la guía 01-fourier-desde-cero.md.

Uso (desde la raíz del repo):
    venv/bin/python materias/analisis-numerico/primer-parcial/apuntes/img/01-figuras.py
Genera 01-fig1 … 01-fig8 (PNG) en esta misma carpeta.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
AZUL, ROJO, VERDE, GRIS, NARANJA = "#1f77b4", "#d62728", "#2ca02c", "#555555", "#ff7f0e"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})
PI = np.pi


def ejes(ax):
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.grid(alpha=0.25)


def guardar(fig, nombre):
    fig.tight_layout()
    fig.savefig(OUT / nombre, dpi=140)
    plt.close(fig)


def periodica(base, a, T):
    """Devuelve g(t) = base(t reducido al período [a, a+T))."""
    return lambda t: base(a + np.mod(np.asarray(t, dtype=float) - a, T))


def trazar(ax, f, t0, t1, saltos, color=NARANJA, lw=2, **kw):
    """Dibuja f entre t0 y t1 cortando la línea en los saltos (lista de abscisas)."""
    cortes = [t0] + sorted(s for s in saltos if t0 < s < t1) + [t1]
    for a, b in zip(cortes[:-1], cortes[1:]):
        x = np.linspace(a + 1e-9, b - 1e-9, 200)
        ax.plot(x, f(x), color=color, lw=lw, **kw)
        kw.pop("label", None)


def ticks_pi(ax, mult, den=1):
    vals = [k * PI / den for k in mult]
    def nombre(k):
        if k == 0:
            return "0"
        s = "-" if k < 0 else ""
        n = abs(k)
        num = r"\pi" if n == 1 else rf"{n}\pi"
        return rf"${s}{num}$" if den == 1 else rf"${s}\frac{{{num}}}{{{den}}}$"
    ax.set_xticks(vals)
    ax.set_xticklabels([nombre(k) for k in mult])


# ---------- fig1: la idea, sumas parciales del pulso de la clase ----------
def fig1():
    f = periodica(lambda t: np.where(t > 0, 1.0, 0.0), -3, 6)
    x = np.linspace(-7.5, 7.5, 1500)
    fig, ax = plt.subplots(1, 3, figsize=(12, 3.2), sharey=True)
    for a, N in zip(ax, (1, 3, 13)):
        trazar(a, f, -7.5, 7.5, range(-9, 10, 3), color="black", lw=1.6, label="$f(x)$")
        S = 0.5 + sum(2 / (n * PI) * np.sin(n * PI * x / 3) for n in range(1, N + 1, 2))
        a.plot(x, S, color=ROJO, lw=1.4, label=f"serie hasta $n={N}$")
        a.axhline(0.5, color=VERDE, ls="--", lw=1, label="valor medio $a_0/2$")
        a.set_title(f"valor medio + armónicas hasta $n={N}$")
        a.set_xticks(range(-6, 7, 3))
        a.set_ylim(-0.3, 1.45)
        ejes(a)
    ax[0].legend(loc="upper left", fontsize=8, ncol=1)
    guardar(fig, "01-fig1-sumas-parciales.png")


# ---------- fig2: completar par / impar un dato en (0, 2) ----------
def fig2():
    fig, ax = plt.subplots(1, 2, figsize=(11, 3.4))
    par = periodica(lambda t: np.abs(t), -2, 4)
    imp = periodica(lambda t: t, -2, 4)
    trazar(ax[0], par, -6, 6, [], label="lo que completás")
    ax[0].set_title("«Solo cosenos» / $C_n$ reales → PAR (espejo en el eje $y$)")
    trazar(ax[1], imp, -6, 6, [-6, -2, 2, 6], label="lo que completás")
    ax[1].set_title("«Solo senos» / $C_n$ imaginarios puros → IMPAR (espejo en el origen)")
    for a in ax:
        a.plot([0, 2], [0, 2], color="black", lw=3.2, label="el dato: $f(x)=x$ en $(0,2)$")
        a.set_xticks(range(-6, 7, 2))
        a.set_ylim(-2.6, 3.2)
        a.annotate("", (2, -2.2), (-2, -2.2), arrowprops={"arrowstyle": "<->", "color": GRIS})
        a.text(0, -2.05, "$T=4$,  $L=2$,  $\\omega_0=\\pi/2$", ha="center", color=GRIS, fontsize=9)
        ejes(a)
        a.legend(loc="upper left", fontsize=8)
    guardar(fig, "01-fig2-completar-par-impar.png")


# ---------- fig3: los tres ítems a) de 2025 ----------
def fig3():
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.3))
    f1 = periodica(lambda t: PI - np.abs(t), -PI, 2 * PI)
    trazar(ax[0], f1, -3 * PI, 3 * PI, [])
    ax[0].plot([0, PI], [PI, 0], color="black", lw=3.2)
    ax[0].set_title("Tema 1 a): $\\pi-t$ en $(0,\\pi)$\n$C_n$ reales → par", fontsize=10)
    f2 = periodica(lambda t: PI - t, 0, 2 * PI)
    trazar(ax[1], f2, -3 * PI, 3 * PI, [-2 * PI, 0, 2 * PI])
    ax[1].plot([-PI, 0], [0, -PI], color="black", lw=3.2)
    ax[1].set_title("Tema 2 a): $-\\pi-t$ en $(-\\pi,0)$\n$C_n$ imaginarios puros → impar", fontsize=10)
    for a in ax[:2]:
        ticks_pi(a, range(-3, 4))
        a.set_yticks([-PI, 0, PI])
        a.set_yticklabels(["$-\\pi$", "0", "$\\pi$"])
        a.set_ylim(-3.8, 3.8)
    f3 = periodica(lambda t: 2 * t, -2, 4)
    trazar(ax[2], f3, -6, 6, [-6, -2, 2, 6])
    ax[2].plot([0, 2], [0, 4], color="black", lw=3.2)
    ax[2].set_title("1er recuperatorio a): $2x$ en $(0,2)$\nserie de senos → impar", fontsize=10)
    ax[2].set_xticks(range(-6, 7, 2))
    ax[2].set_yticks([-4, 0, 4])
    for a in ax:
        ejes(a)
    guardar(fig, "01-fig3-parciales-2025-item-a.png")


# ---------- fig4: simetría de media onda, los dos pasos ----------
def fig4():
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 3.5))
    tri = lambda t: 1 - np.abs(t - 1)  # joroba triangular en (0, 2)
    x = np.linspace(0, 2, 100)
    ax[0].plot(x, tri(x), color="black", lw=3, label="media onda dada, en $(0, L)$")
    ax[0].plot(x + 2, tri(x), color=GRIS, ls=":", lw=1.6, label="paso 1: la corrés $L$")
    ax[0].plot(x + 2, -tri(x), color=NARANJA, lw=2.4, label="paso 2: la das vuelta")
    ax[0].annotate("", (3, 0.95), (1, 0.95), arrowprops={"arrowstyle": "->", "color": GRIS})
    ax[0].annotate("", (3, -0.9), (3, 0.9), arrowprops={"arrowstyle": "->", "color": NARANJA})
    ax[0].set_xticks([0, 2, 4])
    ax[0].set_xticklabels(["0", "$L=T/2$", "$T$"])
    ax[0].set_ylim(-1.5, 1.9)
    ax[0].set_title("Media onda: $f(t+T/2)=-f(t)$")
    ax[0].legend(loc="upper right", fontsize=8)
    ejes(ax[0])
    # contraejemplo: triángulo par 3|x| no tiene SMO
    g = periodica(lambda t: np.abs(t), -2, 4)
    trazar(ax[1], g, -4, 6, [], color="black", lw=2.2, label="$f(x)=|x|$ en $(-2,2)$, $T=4$")
    xx = np.linspace(-2, 0, 50)
    ax[1].plot(xx + 2, -np.abs(xx), color=ROJO, ls="--", lw=1.8, label="corrida $L=2$ y dada vuelta: NO coincide")
    ax[1].axhline(1, color=VERDE, ls="--", lw=1, label="valor medio $=1\\neq0$")
    ax[1].set_xticks(range(-4, 7, 2))
    ax[1].set_ylim(-2.6, 3.9)
    ax[1].set_title("Solo armónicas impares, pero SIN media onda")
    ax[1].legend(loc="upper left", fontsize=8)
    ejes(ax[1])
    guardar(fig, "01-fig4-media-onda.png")


# ---------- fig5: completar con paridad + media onda (ítems c) ----------
def fig5():
    fig, ax = plt.subplots(2, 2, figsize=(12, 6.4))
    def imp_smo(t):  # impar + SMO, dato t en (0,1), T=4, definida en [-2,2)
        return np.where(np.abs(t) < 1, t, np.where(t >= 1, 2 - t, -2 - t))
    def par_smo(t):
        return np.where(np.abs(t) < 1, np.abs(t), np.where(t >= 1, t - 2, -t - 2))
    a = ax[0, 0]
    trazar(a, periodica(imp_smo, -2, 4), -6, 6, [])
    a.plot([0, 1], [0, 1], color="black", lw=3.2)
    a.set_title("2025 Tema 1 c): $t$ en $(0,1)$, impar + media onda ($T=4$)")
    a.set_xticks(range(-6, 7)); a.set_ylim(-1.5, 1.5)
    a = ax[0, 1]
    trazar(a, periodica(par_smo, -2, 4), -6, 6, [-5, -3, -1, 1, 3, 5])
    a.plot([0, 1], [0, 1], color="black", lw=3.2)
    a.set_title("2025 Tema 2 c): $t$ en $(0,1)$, par + media onda ($T=4$)")
    a.set_xticks(range(-6, 7)); a.set_ylim(-1.5, 1.5)
    def cuad(t):  # 2024-1C T2 c): t^2 en (0,2), impar + SMO, T=8, definida en [-4,4)
        return np.where(np.abs(t) < 2, np.sign(t) * t**2, np.where(t >= 2, (t - 4) ** 2, -(t + 4) ** 2))
    a = ax[1, 0]
    trazar(a, periodica(cuad, -4, 8), -12, 12, [])
    xx = np.linspace(0, 2, 50)
    a.plot(xx, xx**2, color="black", lw=3.2)
    a.set_title("2024-1C Tema 2 c): $t^2$ en $(0,2)$, impar + media onda ($T=8$)")
    a.set_xticks(range(-12, 13, 2)); a.set_ylim(-5, 5)
    def t2(t):  # 2024-1C T1 b): |t|+2 en (-2,2) y media onda, T=8, definida en [-2,6)
        return np.where(t < 2, np.abs(t) + 2, -(np.abs(t - 4) + 2))
    a = ax[1, 1]
    trazar(a, periodica(t2, -2, 8), -8, 8, [-6, -2, 2, 6])
    xx = np.linspace(-2, 2, 50)
    a.plot(xx, np.abs(xx) + 2, color=AZUL, lw=2.6)
    a.plot([0, 2], [2, 4], color="black", lw=3.2)
    a.set_title("2024-1C Tema 1 b): la par de a) (azul) + media onda en $(-8,8)$")
    a.set_xticks(range(-8, 9, 2)); a.set_ylim(-5, 5)
    for a in ax.flat:
        ejes(a)
    fig.text(0.5, 0.005, "negro: el dato · naranja: lo que completás", ha="center", color=GRIS, fontsize=9)
    guardar(fig, "01-fig5-paridad-mas-media-onda.png")


# ---------- fig6: espectros de amplitud ----------
def bastones(ax, xs, ys, color=AZUL):
    ax.vlines(xs, 0, ys, color=color, lw=2)
    ax.plot(xs, ys, "o", color=color, ms=4)
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    ax.grid(alpha=0.25)


def fig6():
    fig, ax = plt.subplots(1, 3, figsize=(13.5, 3.5))
    n = np.arange(-6, 7)
    # clase SEF: pulso 0 / pi
    y = np.array([PI / 2 if k == 0 else (1 / abs(k) if k % 2 else 0) for k in n])
    bastones(ax[0], n, y)
    ax[0].set_title("Clase: pulso $0/\\pi$, $\\omega_0=1$\n$|C_0|=\\pi/2$, $|C_n|=1/|n|$ ($n$ impar)", fontsize=9)
    ax[0].set_xlabel("$n\\omega_0$"); ax[0].set_ylabel("$|C_n|$"); ax[0].set_xticks(n)
    # recuperatorio 2025
    y = np.array([0 if k == 0 else 4 / (abs(k) * PI) for k in n])
    bastones(ax[1], n * PI / 2, y, color=ROJO)
    xx = np.linspace(0.6, 6.5, 100)
    for s in (1, -1):
        ax[1].plot(s * xx * PI / 2, 4 / (xx * PI), color=GRIS, ls=":", lw=1)
    ax[1].set_title("1er recuperatorio 2025 c): $|C_n|=\\frac{4}{|n|\\pi}$, $\\omega_0=\\pi/2$\n(bastones cada $\\pi/2$, nada en $n=0$)", fontsize=9)
    ax[1].set_xlabel("$n\\omega_0$")
    ax[1].set_xticks(np.arange(-6, 7, 2) * PI / 2)
    ax[1].set_xticklabels(["$-3\\pi$", "$-2\\pi$", "$-\\pi$", "0", "$\\pi$", "$2\\pi$", "$3\\pi$"])
    # recuperatorio 2024-2C: pulso de ancho 2pi/5
    n2 = np.arange(-11, 12)
    y = np.array([0.2 if k == 0 else abs(np.sin(k * PI / 5) / (k * PI)) for k in n2])
    bastones(ax[2], n2, y, color=VERDE)
    ax[2].set_title("Recuperatorio 2024-2C: pulso en $(-\\pi/5,\\pi/5)$, $\\omega_0=1$\n$|C_n|=\\left|\\frac{\\mathrm{sen}(n\\pi/5)}{n\\pi}\\right|$, ceros en $n=\\pm5,\\pm10$", fontsize=9)
    ax[2].set_xlabel("$n\\omega_0$"); ax[2].set_xticks(range(-10, 11, 5))
    guardar(fig, "01-fig6-espectros-amplitud.png")


# ---------- fig7: impar desplazada ----------
def fig7():
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 3.4))
    f = periodica(lambda t: np.where(t > 0, 4.0, 2.0), -2, 4)
    trazar(ax[0], f, -6, 6, range(-6, 7, 2), color=NARANJA)
    for a0 in (-4, 0, 4):
        ax[0].plot([a0, a0 + 2], [4, 4], color="black", lw=3.2)
    ax[0].axhline(3, color=VERDE, ls="--", lw=1.2)
    ax[0].text(5.9, 3.12, "valor medio $=3$", color=VERDE, ha="right", fontsize=9)
    ax[0].set_title("$f=4$ en $(0,2)$, $k=2$ en $(-2,0)$: impar desplazada")
    ax[0].set_ylim(-0.6, 5.2); ax[0].set_xticks(range(-6, 7, 2))
    g = periodica(lambda t: 4 * t, 0, 10)
    trazar(ax[1], g, -10, 20, [0, 10], color="black", lw=2.2)
    ax[1].axhline(20, color=VERDE, ls="--", lw=1.2)
    ax[1].text(19.8, 21.5, "$a_0/2=20$", color=VERDE, ha="right", fontsize=9)
    ax[1].set_title("OneNote 2d: $f(t)=4t$ en $(0,10)$: mirada desde $y=20$ es impar")
    ax[1].set_ylim(-4, 46); ax[1].set_xticks(range(-10, 21, 5))
    for a in ax:
        ejes(a)
    guardar(fig, "01-fig7-impar-desplazada.png")


# ---------- fig8: período y espectro (tren de pulsos de ancho 1) ----------
def fig8():
    fig, ax = plt.subplots(1, 3, figsize=(13, 3.2), sharey=False)
    for a, T in zip(ax, (2, 4, 10)):
        w0 = 2 * PI / T
        nmax = int(4 * PI / w0)
        n = np.arange(-nmax, nmax + 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = np.where(n == 0, 1 / T, np.sin(n * PI / T) / (n * PI))
        bastones(a, n * w0, c, color=ROJO)
        w = np.linspace(-4 * PI, 4 * PI, 400)
        a.plot(w, np.sinc(w / (2 * PI)) / T, color=GRIS, ls=":", lw=1)
        a.set_title(f"$T={T}$,  $\\omega_0=2\\pi/T={w0:.2f}$,  $C_0=1/{T}$")
        a.set_xlabel("$n\\omega_0$")
        a.set_xticks([-4 * PI, -2 * PI, 0, 2 * PI, 4 * PI])
        a.set_xticklabels(["$-4\\pi$", "$-2\\pi$", "0", "$2\\pi$", "$4\\pi$"])
    ax[0].set_ylabel("$C_n$")
    guardar(fig, "01-fig8-periodo-y-espectro.png")


if __name__ == "__main__":
    for f in (fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8):
        f()
    print("ok")
