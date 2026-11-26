"""Figuras de la guía 03-sistemas-estables-desde-cero.md.

Uso (desde la raíz del repo):
    venv/bin/python materias/analisis-numerico/primer-parcial/apuntes/img/03-figuras.py
Genera 03-fig1 … 03-fig7 (PNG) en esta misma carpeta.

Los cortes de |G| se dibujan con la escala vertical comprimida (arcsinh) para que se
vean a la vez las asíntotas, los ceros y los lomos: son gráficos cualitativos, como los
que pide la cátedra.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
AZUL, ROJO, VERDE, GRIS, NARANJA, VIOLETA = "#1f77b4", "#d62728", "#2ca02c", "#555555", "#ff7f0e", "#7d3c98"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})


def guardar(fig, nombre):
    fig.tight_layout()
    fig.savefig(OUT / nombre, dpi=140)
    plt.close(fig)


def plano(ax, polos, ceros, xlim, ylim, titulo=""):
    """Constelación: cruces en los polos, círculos en los ceros."""
    ax.axhline(0, color="black", lw=0.8)
    ax.axvline(0, color="black", lw=0.8)
    for p in polos:
        ax.plot(p.real, p.imag, "x", color=ROJO, ms=11, mew=2.5, zorder=5)
        if abs(p.imag) > 1e-9:
            ax.plot([p.real, p.real], [0, p.imag], ":", color=GRIS, lw=0.9)
            ax.plot([0, p.real], [p.imag, p.imag], ":", color=GRIS, lw=0.9)
    for z in ceros:
        ax.plot(z.real, z.imag, "o", mfc="white", mec=AZUL, ms=10, mew=2, zorder=5)
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.set_xlabel(r"$\sigma=\mathrm{Re}(s)$")
    ax.set_ylabel(r"$j\omega=\mathrm{Im}(s)$")
    ax.set_aspect("equal")
    ax.grid(alpha=0.25)
    if titulo:
        ax.set_title(titulo, fontsize=10)


# ---------- fig1: constelación + mapa de estabilidad ----------
def fig1():
    fig, ax = plt.subplots(1, 2, figsize=(11.5, 4.6), gridspec_kw={'width_ratios': [1, 1.35]})
    plano(ax[0], [1, -2 + 3j, -2 - 3j], [-2], (-4.5, 3), (-4, 4),
          r"Constelación de $G(s)=\frac{5(s+2)}{(s-1)(s^2+4s+13)}$")
    ax[0].annotate("polo real $1$", (1, 0), (1.1, 1.2), arrowprops={"arrowstyle": "->"})
    ax[0].annotate("polos $-2\\pm3j$\n(siempre de a pares)", (-2, 3), (-4.3, 1.2), arrowprops={"arrowstyle": "->"})
    ax[0].annotate("cero $-2$", (-2, 0), (-4.2, -1.5), arrowprops={"arrowstyle": "->"})

    a = ax[1]
    a.axvspan(-6, 0, color=VERDE, alpha=0.13)
    a.axvspan(0, 6, color=ROJO, alpha=0.13)
    a.axvline(0, color=NARANJA, lw=4, alpha=0.6)
    a.axhline(0, color="black", lw=0.8)
    for p in [-3.5, -3 + 2.5j, -3 - 2.5j, 0j, 2.5j, -2.5j, 3.5, 3 + 2.5j, 3 - 2.5j]:
        p = complex(p)
        a.plot(p.real, p.imag, "x", color="black", ms=10, mew=2.2, zorder=5)
    for x, y, txt, ha in [
        (-3.5, 0.75, "real negativo:\nexponencial decreciente", "center"),
        (-3, 3.45, "complejos con Re < 0:\noscilatoria amortiguada", "center"),
        (0.3, 0.45, "nulo: constante", "left"),
        (0.3, 1.45, "imaginarios puros:\noscilatoria de\namplitud constante", "left"),
        (4.1, 0.75, "real positivo:\nexponencial creciente", "center"),
        (3.6, 3.45, "complejos con Re > 0:\noscilatoria creciente", "center"),
    ]:
        a.text(x, y, txt, fontsize=8.3, ha=ha, va="center",
               bbox={"boxstyle": "round,pad=0.15", "fc": "white", "ec": "none", "alpha": 0.8})
    a.text(-3.2, -4.3, "ESTABLE", color=VERDE, fontsize=13, weight="bold", ha="center")
    a.text(3.3, -4.3, "INESTABLE", color=ROJO, fontsize=13, weight="bold", ha="center")
    a.text(0.3, -1.4, "sobre el eje: marginalmente\nestable (cuenta como estable)", color="#b35900", fontsize=8.3, va="center",
           bbox={"boxstyle": "round,pad=0.15", "fc": "white", "ec": "none", "alpha": 0.8})
    a.set_xlim(-6, 6)
    a.set_ylim(-5, 4.4)
    a.set_xlabel(r"$\sigma=\mathrm{Re}(s)$")
    a.set_ylabel(r"$j\omega=\mathrm{Im}(s)$")
    a.set_title("Dónde está el polo (simple) → qué hace la respuesta", fontsize=10)
    guardar(fig, "03-fig1-plano-s-polos-ceros.png")


# ---------- fig2: los seis tipos de respuesta ----------
def fig2():
    t = np.linspace(0, 6, 600)
    casos = [
        ("1) Polo real negativo\n$e^{-t}$: exponencial decreciente", np.exp(-t), VERDE),
        ("2) Complejos con Re < 0\n$e^{-0{,}5t}\\,\\mathrm{sen}(4t)$: oscilatoria amortiguada", np.exp(-0.5 * t) * np.sin(4 * t), VERDE),
        ("3) Polo nulo\n$k$: constante", np.ones_like(t), NARANJA),
        ("4) Imaginarios puros\n$\\mathrm{sen}(4t)$: oscilatoria de amplitud constante", np.sin(4 * t), NARANJA),
        ("5) Polo real positivo\n$e^{0{,}5t}$: exponencial creciente", np.exp(0.5 * t), ROJO),
        ("6) Complejos con Re > 0\n$e^{0{,}4t}\\,\\mathrm{sen}(4t)$: oscilatoria creciente", np.exp(0.4 * t) * np.sin(4 * t), ROJO),
    ]
    fig, axs = plt.subplots(2, 3, figsize=(11, 5.6))
    for ax, (tit, y, c) in zip(axs.T.flat, casos):
        ax.plot(t, y, color=c, lw=1.8)
        ax.axhline(0, color="black", lw=0.8)
        ax.set_title(tit, fontsize=9)
        ax.set_xlabel("$t$")
        ax.set_xticks([])
        ax.set_yticks([0])
        if c == NARANJA and "constante" in tit and "nulo" in tit:
            ax.set_ylim(-0.3, 1.6)
    fig.suptitle("Los seis casos: verde = estable · naranja = marginalmente estable (cuenta como estable) · rojo = inestable",
                 fontsize=10)
    guardar(fig, "03-fig2-seis-respuestas.png")


# ---------- cortes ----------
def corte(ax, f, xlim, titulo, polos_r=(), ceros_r=(), lomos=(), tope=None, eje="real", p=0.4):
    """Corte cualitativo: se grafica |G|^p (p < 1 comprime la escala vertical)."""
    x = np.linspace(xlim[0], xlim[1], 8000)
    with np.errstate(divide="ignore", invalid="ignore"):
        y = np.abs(f(x)) ** p
    alturas = [abs(f(np.array([float(l)]))[0]) ** p for l in lomos]
    if tope is None:
        tope = 1.45 * max(alturas) if alturas else np.nanpercentile(y[np.isfinite(y)], 97)
    y[y > tope * 1.2] = np.nan
    ax.plot(x, y, color=VERDE, lw=1.9)
    ax.axhline(0, color="black", lw=0.9)
    ax.axvline(0, color="black", lw=0.6, ls=":")
    for q in polos_r:
        ax.axvline(q, color=ROJO, ls="--", lw=1)
    for z in ceros_r:
        ax.plot(z, 0, "o", mfc="white", mec=AZUL, ms=8, mew=1.8, zorder=5)
    ticks = sorted(set(list(polos_r) + list(ceros_r) + list(lomos) + [0]))
    ax.set_xticks(ticks)
    ax.set_xticklabels([f"{v:g}".replace("-", "−") for v in ticks])
    for l, h in zip(lomos, alturas):
        ax.annotate("lomo", (l, h), textcoords="offset points", xytext=(0, 7), ha="center", color=VIOLETA, fontsize=8.5)
    ax.set_yticks([])
    ax.set_ylim(-0.04 * tope, tope)
    ax.set_xlim(*xlim)
    ax.set_xlabel(r"$\sigma=\mathrm{Re}(s)$" if eje == "real" else r"$\omega$  (con $s=j\omega$)")
    ax.set_title(titulo, fontsize=9.5)


def fig3():
    fig, ax = plt.subplots(1, 3, figsize=(12.5, 3.7))
    corte(ax[0], lambda s: 3 * s / ((s - 2) * (s + 4)), (-10, 8),
          r"$|G(\sigma)|$ de $\frac{3s}{(s-2)(s+4)}$: todo real", polos_r=(-4, 2), ceros_r=(0,))
    ax[0].annotate("asíntota\n(polo real)", (-4, 1.5), (-9.6, 1.6), fontsize=8.5, arrowprops={"arrowstyle": "->"})
    ax[0].annotate("toca y rebota\n(cero real)", (0, 0), (3.2, 0.45), fontsize=8.5, arrowprops={"arrowstyle": "->"})
    ax[0].annotate("se pega al eje\n(cero en $\\infty$)", (7.4, 0.72), (4.0, 1.5), fontsize=8.5, arrowprops={"arrowstyle": "->"})
    corte(ax[1], lambda s: 3 * (s - 1) / ((s - 2) * (s**2 + 1)), (-6, 6),
          r"$|G(\sigma)|$ de $\frac{3(s-1)}{(s-2)(s^2+1)}$: polos $\pm j$ y $2$", polos_r=(2,), ceros_r=(1,), lomos=(0,))
    corte(ax[2], lambda s: 10 * (s - 3) / (s**2 + 6 * s + 10), (-12, 9),
          r"$|G(\sigma)|$ de $\frac{10(s-3)}{s^2+6s+10}$ (el reciclado, $k=3$)", ceros_r=(3,), lomos=(-3,))
    guardar(fig, "03-fig3-corte-eje-real-hitos.png")


def fig4():
    fig, axs = plt.subplots(2, 3, figsize=(12.5, 6.6))
    corte(axs[0, 0], lambda s: 2 * (s + 3) / ((s + 2) * (s**2 + 8 * s + 17)), (-9, 3),
          "A) 1er recuperatorio 2025, ítem b: $|G(\\sigma)|$", polos_r=(-2,), ceros_r=(-3,), lomos=(-4,))
    corte(axs[0, 1], lambda s: 25 * (s - 4) / (s * (s**2 + 4 * s + 5)), (-7, 9),
          "B) Repaso 2026 F = 2015 T2 ($K=7$): $|G(\\sigma)|$", polos_r=(0,), ceros_r=(4,), lomos=(-2,))
    corte(axs[0, 2], lambda s: (s + 1) * (41 * s**2 + 87) / (s * (s + 3) * (s**2 + 10 * s + 29)), (-11, 5),
          "C) ≈2019 K3521 T1, ítem b: $|G(\\sigma)|$", polos_r=(-3, 0), ceros_r=(-1,), lomos=(-5,))
    corte(axs[1, 0], lambda s: 17 * (s + 3) / (s * (s**2 + 8 * s + 17)), (-9, 4),
          "D) 2022, ítem b: $|Y(\\sigma)|$ con escalón", polos_r=(0,), ceros_r=(-3,), lomos=(-4,))
    corte(axs[1, 1], lambda s: 52 * (s + 1) / (s * (s**2 + 10 * s + 26)), (-11, 4),
          "E) 2024-1C T1, ítem c: $|Y(\\sigma)|$ con escalón", polos_r=(0,), ceros_r=(-1,), lomos=(-5,))
    corte(axs[1, 2], lambda s: 5 / ((s + 3) * (s**2 + 2 * s + 2)), (-7, 4),
          "F) 2024-2C T2, ítem c: $|Y(\\sigma)|$ con $f=e^{-t}$", polos_r=(-3,), lomos=(-1,))
    guardar(fig, "03-fig4-cortes-parciales.png")


def fig5():
    """Corte por el eje imaginario: 2015 T1 y los dos ejemplos de la práctica."""
    fig, ax = plt.subplots(1, 3, figsize=(12.5, 3.7))
    corte(ax[0], lambda w: np.abs((1j * w + 1) / ((1j * w + 2) * ((1j * w) ** 2 + 4))), (-6, 6),
          "2015 T1, ítem a: $|G(j\\omega)|$ de $\\frac{K(s+1)}{(s+2)(s^2+4)}$", polos_r=(-2, 2), eje="imag")
    corte(ax[1], lambda w: np.abs(1j * w / ((1j * w) ** 2 + 9)), (-8, 8),
          "Guía ej. 4: $|G(j\\omega)|$ de $\\frac{s}{s^2+9}$", polos_r=(-3, 3), ceros_r=(0,), eje="imag")
    corte(ax[2], lambda w: np.abs(1 / ((1j * w) ** 2 + 2 * 1j * w + 2)), (-6, 6),
          "Guía ej. 5: $|G(j\\omega)|$ de $\\frac{1}{s^2+2s+2}$ (polos $-1\\pm j$)", lomos=(-1, 1), eje="imag")
    guardar(fig, "03-fig5-corte-eje-imaginario.png")


# ---------- fig6: método gráfico del módulo ----------
def vectores(ax, polos, ceros, s0, xlim, ylim, titulo, etiquetas):
    plano(ax, polos, ceros, xlim, ylim, titulo)
    for z in ceros:
        ax.annotate("", (s0.real, s0.imag), (z.real, z.imag), arrowprops={"arrowstyle": "->", "color": VERDE, "lw": 1.8})
    for p in polos:
        ax.annotate("", (s0.real, s0.imag), (p.real, p.imag), arrowprops={"arrowstyle": "->", "color": ROJO, "lw": 1.5})
    ax.plot(s0.real, s0.imag, "o", color="black", ms=7, zorder=6)
    for (x, y, txt, col) in etiquetas:
        ax.text(x, y, txt, color=col, fontsize=9.5, ha="center", va="center",
                bbox={"boxstyle": "round,pad=0.15", "fc": "white", "ec": "none", "alpha": 0.85})


def fig6():
    fig, ax = plt.subplots(1, 2, figsize=(11, 4.6))
    vectores(ax[0], [-2, 1j, -1j], [0], 2j, (-3.2, 2.2), (-1.8, 2.8),
             r"$|G(2j)|$ de $\frac{3s}{(s+2)(s^2+1)}$ (PDF de clase)",
             [(0.85, 0.55, "desde el cero $0$: $2$", VERDE), (-1.35, 1.1, r"$\sqrt{8}$", ROJO), (0.7, 1.5, "desde $j$: $1$", ROJO),
              (0.75, -0.5, "desde $-j$: $3$", ROJO), (0.45, 2.25, "$s=2j$", "black")])
    ax[0].plot([0.07, 0.07], [-1, 2], color=ROJO, lw=0)  # (el vector desde −j pasa por j: se superponen)
    vectores(ax[1], [-3, -1 + 1j, -1 - 1j], [-1], 2 + 1j, (-4, 3.2), (-2, 2.2),
             r"$|G(2+j)|$ de $\frac{5(s+1)}{(s+3)(s^2+2s+2)}$ (parcial 2024-1C T2)",
             [(0.7, 0.2, r"$\sqrt{10}$", VERDE), (-0.9, 0.75, r"$\sqrt{26}$", ROJO), (0.4, 1.3, "$3$", ROJO),
              (0.2, -0.45, r"$\sqrt{13}$", ROJO), (2.45, 1.35, "$s=2+j$", "black")])
    guardar(fig, "03-fig6-metodo-grafico-modulo.png")


# ---------- fig7: respuestas temporales de los parciales ----------
def fig7():
    t = np.linspace(0, 4, 800)
    fig, axs = plt.subplots(2, 3, figsize=(12.5, 6.2))
    datos = [
        ("Reciclado (2025 T2), escalón:\n$-3+3\\cos(t)e^{-3t}+19\\,\\mathrm{sen}(t)e^{-3t}$",
         -3 + 3 * np.cos(t) * np.exp(-3 * t) + 19 * np.sin(t) * np.exp(-3 * t), -3, VERDE, t),
        ("2025 T1 (carrito), $f=-e^{-t}$:\n$\\cos(t)e^{-t}-e^{-t}$",
         np.cos(np.linspace(0, 8, 800)) * np.exp(-np.linspace(0, 8, 800)) - np.exp(-np.linspace(0, 8, 800)), 0, VERDE,
         np.linspace(0, 8, 800)),
        ("1er rec. 2025, $f=e^{-3t}$:\n$\\frac{2}{5}e^{-2t}-\\frac{2}{5}\\cos(t)e^{-4t}-\\frac{4}{5}\\mathrm{sen}(t)e^{-4t}$",
         0.4 * np.exp(-2 * t) - 0.4 * np.cos(t) * np.exp(-4 * t) - 0.8 * np.sin(t) * np.exp(-4 * t), 0, VERDE, t),
        ("Repaso 2026 F, impulso:\n$-20+20\\cos(t)e^{-2t}+65\\,\\mathrm{sen}(t)e^{-2t}$",
         -20 + 20 * np.cos(t) * np.exp(-2 * t) + 65 * np.sin(t) * np.exp(-2 * t), -20, NARANJA, t),
        ("2015 T1, $f=e^{-t}$:\n$e^{-2t}-\\cos(2t)+\\mathrm{sen}(2t)$ (no se amortigua)",
         np.exp(-2 * np.linspace(0, 10, 800)) - np.cos(2 * np.linspace(0, 10, 800)) + np.sin(2 * np.linspace(0, 10, 800)),
         None, NARANJA, np.linspace(0, 10, 800)),
        ("2do rec. 2025-02-13, $f=e^{t}(1+2t)$:\n$e^{t}-\\cos(2t)e^{-3t}-2\\,\\mathrm{sen}(2t)e^{-3t}$ (entrada no acotada)",
         np.exp(t) - np.cos(2 * t) * np.exp(-3 * t) - 2 * np.sin(2 * t) * np.exp(-3 * t), None, ROJO, t),
    ]
    for ax, (tit, y, ve, c, tt) in zip(axs.flat, datos):
        ax.plot(tt, y, color=c, lw=1.8)
        ax.axhline(0, color="black", lw=0.8)
        if ve is not None:
            ax.axhline(ve, color=GRIS, ls="--", lw=1)
            ax.text(tt[-1], ve, f" V.E. = {ve:g}".replace("-", "−"), va="bottom", ha="right", fontsize=9, color=GRIS)
        ax.set_title(tit, fontsize=9)
        ax.set_xlabel("$t$")
        ax.grid(alpha=0.25)
    guardar(fig, "03-fig7-respuestas-parciales.png")


if __name__ == "__main__":
    fig1(); fig2(); fig3(); fig4(); fig5(); fig6(); fig7()
    print("ok")
