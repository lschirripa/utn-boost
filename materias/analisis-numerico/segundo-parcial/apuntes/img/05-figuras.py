"""Figuras de la guía 05 (Ecuaciones diferenciales desde cero).

Uso (desde la raíz del repo):
    venv/bin/python materias/analisis-numerico/segundo-parcial/apuntes/img/05-figuras.py
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

AQUI = Path(__file__).parent
AZUL, ROJO, VERDE, GRIS, NARANJA = "#1f5fa8", "#c0392b", "#2e8b57", "#666666", "#e67e22"
plt.rcParams.update({"font.size": 11, "axes.grid": True, "grid.alpha": 0.3, "figure.dpi": 150})


def f(t, y):
    """PVI de la clase: y' = -y + t + 1, y(0) = 1 (exacta: y = t + e^-t)."""
    return -y + t + 1


def exacta(t):
    return t + np.exp(-t)


def fig1_euler():
    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    tt = np.linspace(0, 1, 300)
    ax.plot(tt, exacta(tt), color=AZUL, lw=2, label=r"Solución exacta $y=t+e^{-t}$")
    for h, color, marca in ((0.25, NARANJA, "s"), (0.1, ROJO, "o")):
        n = round(1 / h)
        t = np.arange(n + 1) * h
        w = [1.0]
        for i in range(n):
            w.append(w[-1] + h * f(t[i], w[-1]))
        ax.plot(t, w, color=color, marker=marca, ms=5, lw=1.4, label=f"Euler con $h={str(h).replace('.', ',')}$")
    ax.annotate("cada tramo recto usa la\npendiente $f(t_i,w_i)$ del punto\ndonde está parado",
                xy=(0.45, 1.073), xytext=(0.03, 1.2), arrowprops=dict(arrowstyle="->", color=GRIS), color=GRIS)
    ax.annotate("el error crece\nal alejarse de $t_0$", xy=(1.0, 1.358), xytext=(0.6, 1.3),
                arrowprops=dict(arrowstyle="->", color=GRIS), color=GRIS)
    ax.set_xlabel("$t$")
    ax.set_ylabel("$y$")
    ax.set_title(r"Euler: avanzar de $h$ en $h$ por la tangente ($y'=-y+t+1$, $y(0)=1$)")
    ax.legend(loc="lower right")
    fig.tight_layout()
    fig.savefig(AQUI / "05-fig1-euler-poligonal.png")
    plt.close(fig)


def fig2_heun():
    fig, ax = plt.subplots(figsize=(7.5, 4.6))
    t0, h = 0.4, 1.0
    w0 = exacta(t0)
    tt = np.linspace(t0 - 0.05, t0 + h + 0.1, 300)
    ax.plot(tt, exacta(tt), color=AZUL, lw=2, label="Solución exacta")
    m1 = f(t0, w0)
    w_pred = w0 + h * m1
    m2 = f(t0 + h, w_pred)
    w_heun = w0 + h / 2 * (m1 + m2)
    ax.plot([t0, t0 + h], [w0, w_pred], color=ROJO, lw=1.6, label=r"Pendiente inicial $f(t_i,w_i)$ → predicción $w^*_{i+1}$ (Euler)")
    dt = 0.22
    ax.plot([t0 + h - dt, t0 + h + dt], [w_pred - dt * m2, w_pred + dt * m2], color=NARANJA, lw=1.6,
            label=r"Pendiente en la predicción $f(t_{i+1},w^*_{i+1})$")
    ax.plot([t0, t0 + h], [w0, w_heun], color=VERDE, lw=2, label=r"Pendiente promedio → $w_{i+1}$ (Heun)")
    ax.plot([t0], [w0], "ko", ms=6)
    ax.plot([t0 + h], [w_pred], "s", color=ROJO, ms=7)
    ax.plot([t0 + h], [w_heun], "o", color=VERDE, ms=7)
    ax.plot([t0 + h], [exacta(t0 + h)], "o", color=AZUL, ms=7)
    ax.annotate("$(t_i,\\ w_i)$", (t0, w0), textcoords="offset points", xytext=(6, -18), ha="left")
    ax.annotate("$w^*_{i+1}$: se queda corto", (t0 + h, w_pred), textcoords="offset points", xytext=(-150, -34), color=ROJO)
    ax.annotate("$w_{i+1}$ corregido", (t0 + h, w_heun), textcoords="offset points", xytext=(-118, -4), color=VERDE)
    ax.axvline(t0 + h, color=GRIS, lw=0.8, ls=":")
    ax.set_xlabel("$t$")
    ax.set_ylabel("$y$")
    ax.set_title("Heun: predecir con Euler y corregir con el promedio de pendientes\n(un paso exagerado, $h=1$, para que se vea)")
    ax.set_ylim(1.0, 2.05)
    ax.legend(loc="upper left", fontsize=9)
    fig.tight_layout()
    fig.savefig(AQUI / "05-fig2-heun-prediccion-correccion.png")
    plt.close(fig)


def fig3_lipschitz():
    fig, (a, b) = plt.subplots(1, 2, figsize=(9.5, 4.0))
    y = np.linspace(0, 0.5, 100)
    a.plot(y, 4 * y, color=AZUL, lw=2)
    a.axhline(2, color=ROJO, ls="--", lw=1.4)
    a.text(0.02, 2.06, "$L=2$ (el máximo, en $y=0{,}5$)", color=ROJO)
    a.set_ylim(0, 2.5)
    a.set_xlabel("$y$")
    a.set_title("Acotada: existe $L$\n" + r"$\left|\partial f/\partial y\right|=|4y|$ en $y\in[0;\,0{,}5]$ (parcial T1)", fontsize=10)
    y2 = np.linspace(0.002, 5, 600)
    b.plot(y2, 0.5 * y2 ** (-2 / 3), color=AZUL, lw=2)
    b.set_ylim(0, 8)
    b.annotate("se va a infinito\ncuando $y\\to 0$:\nno hay cota", xy=(0.03, 5.2), xytext=(1.3, 5.2),
               arrowprops=dict(arrowstyle="->", color=ROJO), color=ROJO)
    b.set_xlabel("$y$")
    b.set_title("No acotada: no existe $L$\n" + r"$\left|\partial f/\partial y\right|=\frac{1}{2}y^{-2/3}$ en $y\in[0;\,5]$ (ejemplo c de la clase)", fontsize=10)
    fig.tight_layout()
    fig.savefig(AQUI / "05-fig3-lipschitz-cota.png")
    plt.close(fig)


def fig4_comparacion():
    # Error |y(1) - w| del ejemplo de la clase con h = 0,1 (tablas del PDF de clase).
    nombres = ["Euler\n(orden 1)", "Heun\n(orden 2)", "Runge-Kutta 4\n(orden 4)"]
    errores = [0.019201, 0.00066154, 3.3324e-07]
    fig, ax = plt.subplots(figsize=(7.0, 4.0))
    barras = ax.bar(nombres, errores, color=[ROJO, NARANJA, VERDE], width=0.55)
    ax.set_yscale("log")
    ax.set_ylim(1e-8, 1)
    for barra, e, txt in zip(barras, errores, ["0,0192", "0,00066", "0,00000033"]):
        ax.text(barra.get_x() + barra.get_width() / 2, e * 1.6, txt, ha="center")
    ax.set_ylabel("error en $y(1)$ (escala logarítmica)")
    ax.set_title("Mismo problema, mismo $h=0{,}1$: cuánto se equivoca cada método")
    fig.tight_layout()
    fig.savefig(AQUI / "05-fig4-comparacion-errores.png")
    plt.close(fig)


if __name__ == "__main__":
    fig1_euler()
    fig2_heun()
    fig3_lipschitz()
    fig4_comparacion()
    print("Figuras 07 generadas en", AQUI)
