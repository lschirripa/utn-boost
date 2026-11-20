"""Figuras de la guía 02-sistemas-lineales-desde-cero.md.

Uso (desde la raíz del repo):
    venv/bin/python materias/analisis-numerico/segundo-parcial/apuntes/img/02-figuras.py
Genera 02-fig1 … 02-fig3 (PNG) en esta misma carpeta.
"""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

OUT = Path(__file__).resolve().parent
AZUL, ROJO, VERDE, GRIS = "#1f77b4", "#d62728", "#2ca02c", "#555555"
plt.rcParams.update({"font.size": 10, "axes.spines.top": False, "axes.spines.right": False})


def guardar(fig, nombre):
    fig.tight_layout()
    fig.savefig(OUT / nombre, dpi=140)
    plt.close(fig)


def jacobi(A, b, x, n):
    out = [x.copy()]
    d = np.diag(A)
    for _ in range(n):
        x = (b - (A - np.diag(d)) @ x) / d
        out.append(x.copy())
    return np.array(out)


def gauss_seidel(A, b, x, n):
    x = x.astype(float).copy()
    out = [x.copy()]
    for _ in range(n):
        for i in range(len(b)):
            x[i] = (b[i] - A[i] @ x + A[i, i] * x[i]) / A[i, i]
        out.append(x.copy())
    return np.array(out)


# ---------- fig1: Jacobi vs Gauss-Seidel en el ejemplo 4x4 de la clase ----------
def fig1():
    A = np.array([[10, -1, 2, 0], [-1, 11, -1, 3], [2, -1, 10, -1], [0, 3, -1, 8]], float)
    b = np.array([6, 25, -11, 15], float)
    sol = np.array([1, 2, -1, 1], float)
    J = jacobi(A, b, np.zeros(4), 10)
    G = gauss_seidel(A, b, np.zeros(4), 10)
    eJ = np.abs(J - sol).max(axis=1)
    eG = np.abs(G - sol).max(axis=1)
    fig, ax = plt.subplots(figsize=(7.5, 4))
    ax.semilogy(range(11), eJ, "o-", color=AZUL, label="Jacobi")
    ax.semilogy(range(11), eG, "s-", color=ROJO, label="Gauss-Seidel")
    ax.axhline(1e-3, color=GRIS, ls="--", lw=0.8)
    ax.text(0.1, 1.25e-3, "error $10^{-3}$", color=GRIS, fontsize=9)
    ax.set_xlabel("iteración $k$")
    ax.set_ylabel(r"distancia a la solución  $\|X^{(k)}-(1;2;-1;1)\|_\infty$")
    ax.set_title("Ejemplo 4×4 de la clase: Gauss-Seidel llega en la mitad de iteraciones")
    ax.set_xticks(range(11))
    ax.grid(alpha=0.25, which="both")
    ax.legend()
    guardar(fig, "02-fig1-jacobi-vs-gauss-seidel.png")


# ---------- fig2: el sistema del parcial 2025: Jacobi no converge, Gauss-Seidel sí ----------
def fig2():
    A = np.array([[7, 5, 4], [3, 4, 2], [1, 1, 4]], float)
    b = np.array([10, 3, -8], float)
    sol = np.linalg.solve(A, b)
    n = 60
    J = jacobi(A, b, np.zeros(3), n)
    G = gauss_seidel(A, b, np.zeros(3), n)
    fig, ax = plt.subplots(1, 2, figsize=(10.5, 3.9))
    ax[0].plot(range(n + 1), J[:, 0], ".-", color=AZUL, lw=0.8, label="Jacobi")
    ax[0].plot(range(n + 1), G[:, 0], ".-", color=ROJO, lw=0.8, label="Gauss-Seidel")
    ax[0].axhline(sol[0], color=VERDE, ls="--", lw=1, label="$x$ exacto $=35/11$")
    ax[0].set_xlabel("iteración $k$")
    ax[0].set_ylabel("componente $x$")
    ax[0].set_title("Toda la corrida")
    ax[0].grid(alpha=0.25)
    ax[0].legend()
    k0 = 30
    ax[1].plot(range(k0, n + 1), J[k0:, 0], "o-", color=AZUL, lw=0.8, label="Jacobi: va y viene")
    ax[1].plot(range(k0, n + 1), G[k0:, 0], "s-", color=ROJO, lw=0.8, ms=3, label="Gauss-Seidel: clavado")
    ax[1].axhline(sol[0], color=VERDE, ls="--", lw=1)
    ax[1].set_xlabel("iteración $k$")
    ax[1].set_title("Zoom desde la iteración 30")
    ax[1].grid(alpha=0.25)
    ax[1].legend(loc="center right")
    fig.suptitle(r"Sistema del parcial 2025 ($7x+5y+4z=10$, …): $\rho(T_J)=1$, $\rho(T_{GS})=0{,}527$", fontsize=11)
    guardar(fig, "02-fig2-parcial-jacobi-no-converge.png")


# ---------- fig3: bien vs mal condicionado (esquema) ----------
def fig3():
    x = np.linspace(-1, 4, 200)
    fig, ax = plt.subplots(1, 2, figsize=(10.5, 3.9))
    # bien condicionado: rectas que se cruzan francamente
    ax[0].plot(x, 2 - x, color=AZUL, label="ecuación 1")
    ax[0].plot(x, x - 1, color=ROJO, label="ecuación 2")
    ax[0].plot(x, x - 0.7, color=ROJO, ls="--", label="ecuación 2 perturbada")
    ax[0].plot([1.5], [0.5], "o", color="black")
    ax[0].plot([1.35], [0.65], "o", color=GRIS)
    ax[0].set_title("Bien condicionado: el cruce casi no se mueve")
    # mal condicionado: casi paralelas (pendientes exageradas para que se vea)
    ax[1].plot(x, 2 - x, color=AZUL, label="ecuación 1")
    ax[1].plot(x, (2 - x) / 1.12, color=ROJO, label="ecuación 2")
    ax[1].plot(x, (2.12 - x) / 1.12, color=ROJO, ls="--", label="ecuación 2 perturbada")
    ax[1].plot([2], [0], "o", color="black")
    ax[1].plot([1], [1], "o", color=GRIS)
    ax[1].annotate("", xy=(1, 1), xytext=(2, 0), arrowprops=dict(arrowstyle="->", color=GRIS))
    ax[1].text(2.05, 0.08, "(2; 0)")
    ax[1].text(0.35, 1.12, "(1; 1)")
    ax[1].set_title("Mal condicionado: rectas casi paralelas, el cruce salta")
    for a in ax:
        a.set_xlim(-0.5, 3.5)
        a.set_ylim(-1, 2.5)
        a.axhline(0, color="black", lw=0.8)
        a.axvline(0, color="black", lw=0.8)
        a.grid(alpha=0.25)
        a.legend(fontsize=8, loc="lower left")
    guardar(fig, "02-fig3-condicionamiento.png")


if __name__ == "__main__":
    fig1()
    fig2()
    fig3()
    print("OK: 02-fig1 … 02-fig3 en", OUT)
