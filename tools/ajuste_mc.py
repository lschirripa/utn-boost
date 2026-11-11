"""Ajuste por mínimos cuadrados (aproximación discreta) con desarrollo paso a paso.

Pensado para el TP de Análisis Numérico: a partir de una tabla (x, y) ajusta varios
modelos, y para cada uno deja escrito TODO lo que pide la consigna:

- el cambio de variables (si el modelo no es polinómico) y la tabla transformada,
- la tabla de sumatorias,
- el sistema de ecuaciones normales con los números puestos,
- su solución y la vuelta a los parámetros originales,
- la función aproximante,
- la tabla de residuos en las variables ORIGINALES y el error cuadrático
  (suma de (y - ŷ)²), que es lo que se compara para elegir el mejor modelo,
- el gráfico de la nube de puntos con la curva.

Uso:
    venv/bin/python tools/ajuste_mc.py datos.csv \
        --modelos recta,parabola,exponencial,potencial --x0 2030 \
        --out-dir materias/analisis-numerico/tp-minimos-cuadrados/resultados

El CSV tiene dos columnas con encabezado (``x,y`` o nombres descriptivos, que se
usan como rótulos de los ejes). Separador coma o punto y coma.

Modelos disponibles (``--modelos``):
    recta        y = a0 + a1 x
    parabola     y = a0 + a1 x + a2 x²
    cubica       y = a0 + a1 x + a2 x² + a3 x³
    exponencial  y = a0 e^(a1 x)          (Y = ln y)
    potencial    y = a0 x^a1              (Y = ln y, X = ln x)
    logaritmico  y = a0 + a1 ln x         (X = ln x)
    reciproco    y = a0 + a1 / x          (X = 1/x)          [guía, ej. 29c]
    hiperbolico  y = a1 / (a0 + x)        (Y = 1/y)          [teórica]
    saturacion   y = a x / (b + x)        (Y = 1/y, X = 1/x)

Salida en ``--out-dir``: ``reporte.md`` (LaTeX, renderizable con md_to_html.py),
``resultados.json`` y los PNG ``nube.png``, ``modelo-<nombre>.png``, ``comparacion.png``.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable

import numpy as np


# ---------------------------------------------------------------- modelos


@dataclass
class Modelo:
    clave: str
    nombre: str
    formula: str                      # LaTeX de la forma general
    grado: int                        # grado del polinomio en la variable X
    tx: Callable[[np.ndarray], np.ndarray] | None = None   # X = tx(x)
    ty: Callable[[np.ndarray], np.ndarray] | None = None   # Y = ty(y)
    tx_tex: str = "x"
    ty_tex: str = "y"
    linealizacion: list[str] = field(default_factory=list)  # pasos LaTeX
    nombres_lin: list[str] = field(default_factory=list)    # nombres de las incógnitas del sistema
    # de los coeficientes del sistema lineal (A) a los parámetros del modelo
    volver: Callable[[np.ndarray], dict[str, float]] | None = None
    volver_tex: list[str] = field(default_factory=list)
    requiere_x_pos: bool = False
    requiere_y_pos: bool = False
    requiere_x_no_nulo: bool = False
    requiere_y_no_nulo: bool = False

    def evaluar(self, p: dict[str, float], x: np.ndarray) -> np.ndarray:
        return EVALUADORES[self.clave](p, x)

    def expresion(self, p: dict[str, float], d: int) -> str:
        return EXPRESIONES[self.clave](p, d)


def _poly_names(g: int) -> list[str]:
    return [f"a_{i}" for i in range(g + 1)]


def _fmt(v: float, d: int) -> str:
    """Número con coma decimal (convención rioplatense), sin -0.

    - Enteros exactos (datos, sumatorias de enteros): sin decimales.
    - |v| < 1: al menos 6 cifras significativas, para que valores chicos como 1/y con
      y ~ 10⁵ (≈ 0,0000052) no queden en 0,0000.
    - Resto: d decimales.
    """
    if not math.isfinite(v):
        return str(v)
    if abs(v) < 1e-12:  # ruido de punto flotante (p. ej. SSE de un interpolante)
        return "0"
    if round(v) != 0 and abs(v - round(v)) < 1e-9 * max(1.0, abs(v)):
        return f"{round(v):d}"
    if abs(v) < 1:
        d = max(d, -math.floor(math.log10(abs(v))) + 5)
    if abs(v) < 0.5 * 10 ** (-d):
        v = 0.0
    s = f"{v:.{d}f}"
    return s.replace(".", "{,}")


def _signo(v: float, d: int) -> str:
    return ("+ " if v >= 0 else "- ") + _fmt(abs(v), d)


MODELOS: dict[str, Modelo] = {
    "recta": Modelo(
        "recta", "Recta", r"y = a_0 + a_1\,x", 1,
        nombres_lin=_poly_names(1),
        volver=lambda A: {"a_0": A[0], "a_1": A[1]},
    ),
    "parabola": Modelo(
        "parabola", "Parábola", r"y = a_0 + a_1\,x + a_2\,x^2", 2,
        nombres_lin=_poly_names(2),
        volver=lambda A: {"a_0": A[0], "a_1": A[1], "a_2": A[2]},
    ),
    "cubica": Modelo(
        "cubica", "Polinomio cúbico", r"y = a_0 + a_1\,x + a_2\,x^2 + a_3\,x^3", 3,
        nombres_lin=_poly_names(3),
        volver=lambda A: {"a_0": A[0], "a_1": A[1], "a_2": A[2], "a_3": A[3]},
    ),
    "exponencial": Modelo(
        "exponencial", "Exponencial", r"y = a_0\,e^{a_1 x}", 1,
        ty=np.log, ty_tex=r"\ln y",
        linealizacion=[
            r"y = a_0\,e^{a_1 x}",
            r"\ln y = \ln a_0 + a_1\,x",
            r"\underbrace{\ln y}_{Y} = \underbrace{\ln a_0}_{A_0} + a_1\,\underbrace{x}_{X}",
        ],
        nombres_lin=["A_0", "a_1"],
        volver=lambda A: {"a_0": math.exp(A[0]), "a_1": A[1]},
        volver_tex=[r"a_0 = e^{A_0}"],
        requiere_y_pos=True,
    ),
    "potencial": Modelo(
        "potencial", "Potencial", r"y = a_0\,x^{a_1}", 1,
        tx=np.log, ty=np.log, tx_tex=r"\ln x", ty_tex=r"\ln y",
        linealizacion=[
            r"y = a_0\,x^{a_1}",
            r"\ln y = \ln a_0 + a_1 \ln x",
            r"\underbrace{\ln y}_{Y} = \underbrace{\ln a_0}_{A_0} + a_1\,\underbrace{\ln x}_{X}",
        ],
        nombres_lin=["A_0", "a_1"],
        volver=lambda A: {"a_0": math.exp(A[0]), "a_1": A[1]},
        volver_tex=[r"a_0 = e^{A_0}"],
        requiere_x_pos=True, requiere_y_pos=True,
    ),
    "logaritmico": Modelo(
        "logaritmico", "Logarítmico", r"y = a_0 + a_1 \ln x", 1,
        tx=np.log, tx_tex=r"\ln x",
        linealizacion=[
            r"y = a_0 + a_1\,\underbrace{\ln x}_{X}",
        ],
        nombres_lin=["a_0", "a_1"],
        volver=lambda A: {"a_0": A[0], "a_1": A[1]},
        requiere_x_pos=True,
    ),
    "reciproco": Modelo(
        "reciproco", "Recíproco", r"y = a_0 + a_1\,\frac{1}{x}", 1,
        tx=lambda x: 1.0 / x, tx_tex=r"\tfrac{1}{x}",
        linealizacion=[
            r"y = a_0 + a_1\,\underbrace{\frac{1}{x}}_{X}",
        ],
        nombres_lin=["a_0", "a_1"],
        volver=lambda A: {"a_0": A[0], "a_1": A[1]},
        requiere_x_no_nulo=True,
    ),
    "hiperbolico": Modelo(
        "hiperbolico", "Hiperbólico", r"y = \frac{a_1}{a_0 + x}", 1,
        ty=lambda y: 1.0 / y, ty_tex=r"\tfrac{1}{y}",
        linealizacion=[
            r"y = \frac{a_1}{a_0 + x}",
            r"\frac{1}{y} = \frac{a_0 + x}{a_1} = \frac{a_0}{a_1} + \frac{1}{a_1}\,x",
            r"\underbrace{\frac{1}{y}}_{Y} = \underbrace{\frac{a_0}{a_1}}_{A_0} + "
            r"\underbrace{\frac{1}{a_1}}_{A_1}\,x",
        ],
        nombres_lin=["A_0", "A_1"],
        volver=lambda A: {"a_0": A[0] / A[1], "a_1": 1.0 / A[1]},
        volver_tex=[r"a_1 = \frac{1}{A_1}", r"a_0 = A_0 \cdot a_1"],
        requiere_y_no_nulo=True,
    ),
    "saturacion": Modelo(
        "saturacion", "Crecimiento con saturación", r"y = \frac{a\,x}{b + x}", 1,
        tx=lambda x: 1.0 / x, ty=lambda y: 1.0 / y,
        tx_tex=r"\tfrac{1}{x}", ty_tex=r"\tfrac{1}{y}",
        linealizacion=[
            r"y = \frac{a\,x}{b + x}",
            r"\frac{1}{y} = \frac{b + x}{a\,x} = \frac{1}{a} + \frac{b}{a}\cdot\frac{1}{x}",
            r"\underbrace{\frac{1}{y}}_{Y} = \underbrace{\frac{1}{a}}_{A_0} + "
            r"\underbrace{\frac{b}{a}}_{A_1}\,\underbrace{\frac{1}{x}}_{X}",
        ],
        nombres_lin=["A_0", "A_1"],
        volver=lambda A: {"a": 1.0 / A[0], "b": A[1] / A[0]},
        volver_tex=[r"a = \frac{1}{A_0}", r"b = A_1 \cdot a = \frac{A_1}{A_0}"],
        requiere_x_no_nulo=True, requiere_y_no_nulo=True,
    ),
}

EVALUADORES: dict[str, Callable[[dict[str, float], np.ndarray], np.ndarray]] = {
    "recta": lambda p, x: p["a_0"] + p["a_1"] * x,
    "parabola": lambda p, x: p["a_0"] + p["a_1"] * x + p["a_2"] * x**2,
    "cubica": lambda p, x: p["a_0"] + p["a_1"] * x + p["a_2"] * x**2 + p["a_3"] * x**3,
    "exponencial": lambda p, x: p["a_0"] * np.exp(p["a_1"] * x),
    "potencial": lambda p, x: p["a_0"] * np.power(x, p["a_1"]),
    "logaritmico": lambda p, x: p["a_0"] + p["a_1"] * np.log(x),
    "reciproco": lambda p, x: p["a_0"] + p["a_1"] / x,
    "hiperbolico": lambda p, x: p["a_1"] / (p["a_0"] + x),
    "saturacion": lambda p, x: p["a"] * x / (p["b"] + x),
}


def _poly_expr(p: dict[str, float], g: int, d: int) -> str:
    s = _fmt(p["a_0"], d)
    for i in range(1, g + 1):
        pot = "x" if i == 1 else f"x^{i}"
        s += f" {_signo(p[f'a_{i}'], d)}\\,{pot}"
    return "y = " + s


EXPRESIONES: dict[str, Callable[[dict[str, float], int], str]] = {
    "recta": lambda p, d: _poly_expr(p, 1, d),
    "parabola": lambda p, d: _poly_expr(p, 2, d),
    "cubica": lambda p, d: _poly_expr(p, 3, d),
    "exponencial": lambda p, d: f"y = {_fmt(p['a_0'], d)}\\,e^{{{_fmt(p['a_1'], d)}\\,x}}",
    "potencial": lambda p, d: f"y = {_fmt(p['a_0'], d)}\\,x^{{{_fmt(p['a_1'], d)}}}",
    "logaritmico": lambda p, d: f"y = {_fmt(p['a_0'], d)} {_signo(p['a_1'], d)}\\,\\ln x",
    "reciproco": lambda p, d: f"y = {_fmt(p['a_0'], d)} {_signo(p['a_1'], d)}\\,\\frac{{1}}{{x}}",
    "hiperbolico": lambda p, d: f"y = \\frac{{{_fmt(p['a_1'], d)}}}{{{_fmt(p['a_0'], d)} + x}}",
    "saturacion": lambda p, d: f"y = \\frac{{{_fmt(p['a'], d)}\\,x}}{{{_fmt(p['b'], d)} + x}}",
}


# ---------------------------------------------------------------- cálculo


def leer_csv(ruta: Path) -> tuple[str, str, np.ndarray, np.ndarray]:
    texto = ruta.read_text(encoding="utf-8-sig")
    dialecto = csv.Sniffer().sniff(texto.splitlines()[0], delimiters=",;\t")
    filas = [f for f in csv.reader(texto.splitlines(), dialecto) if f and any(c.strip() for c in f)]
    encabezado, datos = filas[0], filas[1:]
    def num(s: str) -> float:
        s = s.strip()
        # admite coma decimal si el separador de campos no es la coma
        if dialecto.delimiter != "," and "," in s and "." not in s:
            s = s.replace(",", ".")
        return float(s)
    x = np.array([num(f[0]) for f in datos])
    y = np.array([num(f[1]) for f in datos])
    return encabezado[0].strip(), encabezado[1].strip(), x, y


def ajustar(m: Modelo, x: np.ndarray, y: np.ndarray) -> dict:
    if m.requiere_x_pos and np.any(x <= 0):
        raise ValueError(f"{m.nombre}: requiere x > 0 (hay x ≤ 0 en los datos)")
    if m.requiere_y_pos and np.any(y <= 0):
        raise ValueError(f"{m.nombre}: requiere y > 0 (hay y ≤ 0 en los datos)")
    if m.requiere_x_no_nulo and np.any(x == 0):
        raise ValueError(f"{m.nombre}: requiere x ≠ 0")
    if m.requiere_y_no_nulo and np.any(y == 0):
        raise ValueError(f"{m.nombre}: requiere y ≠ 0")

    X = m.tx(x) if m.tx else x.astype(float)
    Y = m.ty(y) if m.ty else y.astype(float)
    g = m.grado
    n = len(x)
    # sumatorias Σ X^k (k = 0..2g) y Σ X^k Y (k = 0..g)
    sx = [float(np.sum(X**k)) for k in range(2 * g + 1)]
    sxy = [float(np.sum(X**k * Y)) for k in range(g + 1)]
    M = np.array([[sx[i + j] for j in range(g + 1)] for i in range(g + 1)])
    b = np.array(sxy)
    A = np.linalg.solve(M, b)
    p = m.volver(A)
    yhat = m.evaluar(p, x)
    res = y - yhat
    sse = float(np.sum(res**2))
    sst = float(np.sum((y - y.mean()) ** 2))
    r2 = 1 - sse / sst if sst > 0 else float("nan")
    k = g + 1  # parámetros
    polo = {"hiperbolico": lambda q: -q["a_0"], "saturacion": lambda q: -q["b"]}.get(m.clave)
    aviso = None
    if polo is not None and x.min() <= polo(p) <= x.max():
        aviso = (f"la función hallada tiene una asíntota vertical en x = {polo(p):.4g}, dentro del "
                 f"rango de los datos: el modelo no sirve para estos puntos")
    return {
        "aviso": aviso,
        "X": X, "Y": Y, "sx": sx, "sxy": sxy, "M": M, "b": b, "A": A, "p": p,
        "yhat": yhat, "res": res, "sse": sse, "ecm": sse / n,
        "rmse": math.sqrt(sse / n),
        "s": math.sqrt(sse / (n - k)) if n > k else float("nan"),
        "r2": r2, "n": n, "k": k,
    }


# ---------------------------------------------------------------- reporte


def _pot_tex(base: str, k: int) -> str:
    if k == 0:
        return "1"
    if k == 1:
        return base
    if base in ("x", "X"):
        return f"{base}^{k}"
    return f"({base})^{k}"


def tabla_sumatorias(m: Modelo, x, y, r, d: int) -> str:
    g = m.grado
    X, Y = r["X"], r["Y"]
    Xn = "X" if m.tx else "x"
    Yn = "Y" if m.ty else "y"
    cols: list[tuple[str, np.ndarray]] = [("i", np.arange(1, len(x) + 1)), ("x", x), ("y", y)]
    if m.tx:
        cols.append((f"X = {m.tx_tex}", X))
    if m.ty:
        cols.append((f"Y = {m.ty_tex}", Y))
    for k in range(2, 2 * g + 1):
        cols.append((_pot_tex(Xn, k), X**k))
    for k in range(1, g + 1):
        cols.append((f"{_pot_tex(Xn, k)}\\,{Yn}", X**k * Y))
    enc = "| " + " | ".join(f"${c}$" if c != "i" else "$i$" for c, _ in cols) + " |"
    sep = "|" + "|".join(":---:" for _ in cols) + "|"
    filas = []
    for i in range(len(x)):
        celdas = [str(i + 1)] + [f"${_fmt(float(v[i]), d)}$" for _, v in cols[1:]]
        filas.append("| " + " | ".join(celdas) + " |")
    tot = ["$\\Sigma$"] + [f"$\\mathbf{{{_fmt(float(np.sum(v)), d)}}}$" for _, v in cols[1:]]
    filas.append("| " + " | ".join(tot) + " |")
    return "\n".join([enc, sep, *filas])


def sistema_tex(m: Modelo, r, d: int, numerico: bool) -> str:
    g = m.grado
    Xn = "X" if m.tx else "x"
    Yn = "Y" if m.ty else "y"
    inc = m.nombres_lin
    lineas = []
    for i in range(g + 1):
        terms = []
        for j in range(g + 1):
            k = i + j
            if numerico:
                coef = _fmt(r["sx"][k], d)
            else:
                coef = "m" if k == 0 else f"\\sum {_pot_tex(Xn, k)}"
            terms.append(f"{coef}\\;{inc[j]}")
        if numerico:
            rhs = _fmt(r["sxy"][i], d)
        else:
            rhs = f"\\sum {Yn}" if i == 0 else f"\\sum {_pot_tex(Xn, i)}\\,{Yn}"
        lineas.append(" + ".join(terms) + " &= " + rhs)
    return "\\left\\{\\begin{aligned}\n" + " \\\\\n".join(lineas) + "\n\\end{aligned}\\right."


def residuos_tex(x, y, r, d: int) -> str:
    enc = "| $i$ | $x_i$ | $y_i$ | $\\hat y_i$ | $y_i - \\hat y_i$ | $(y_i - \\hat y_i)^2$ |"
    sep = "|:---:|:---:|:---:|:---:|:---:|:---:|"
    filas = []
    for i in range(len(x)):
        filas.append(
            f"| {i + 1} | ${_fmt(x[i], d)}$ | ${_fmt(y[i], d)}$ | ${_fmt(r['yhat'][i], d)}$ | "
            f"${_fmt(r['res'][i], d)}$ | ${_fmt(r['res'][i] ** 2, d)}$ |"
        )
    filas.append(f"| $\\Sigma$ | | | | | $\\mathbf{{{_fmt(r['sse'], d)}}}$ |")
    return "\n".join([enc, sep, *filas])


def seccion_modelo(num: int, m: Modelo, x, y, r, d: int, img: str | None) -> str:
    out = [f"## {num}. Modelo {m.nombre.lower()}: ${m.formula}$", ""]
    if m.linealizacion:
        out += ["**Paso 1 — cambio de variables.** El modelo no es lineal en sus parámetros; "
                "lo llevamos a una forma aparentemente lineal:", ""]
        for l in m.linealizacion:
            out += ["$$", l, "$$", ""]
        out += [f"Queda una recta $Y = {m.nombres_lin[0]} + {m.nombres_lin[1]}\\,X$ en las "
                f"variables $X = {m.tx_tex}$, $Y = {m.ty_tex}$.", ""]
    else:
        out += ["**Paso 1 — cambio de variables.** No hace falta: el modelo ya es lineal en "
                "sus parámetros.", ""]
    out += ["**Paso 2 — sistema de ecuaciones normales** (forma general, $m$ = cantidad de puntos):", "",
            "$$", sistema_tex(m, r, d, numerico=False), "$$", ""]
    out += ["**Paso 3 — tabla de sumatorias:**", "", tabla_sumatorias(m, x, y, r, d), ""]
    out += ["**Paso 4 — sistema con los valores** ($m = " + str(r["n"]) + "$):", "",
            "$$", sistema_tex(m, r, d, numerico=True), "$$", ""]
    sol = ",\\qquad ".join(f"{n} = {_fmt(v, d)}" for n, v in zip(m.nombres_lin, r["A"]))
    out += ["**Paso 5 — solución del sistema:**", "", "$$", sol, "$$", ""]
    if m.volver_tex:
        vuelta = ",\\qquad ".join(m.volver_tex)
        params = ",\\qquad ".join(f"{k} = {_fmt(v, d)}" for k, v in r["p"].items())
        out += ["Volvemos a los parámetros del modelo original:", "", "$$", vuelta, "$$", "",
                "$$", params, "$$", ""]
    out += ["**Paso 6 — función aproximante:**", "", "$$", m.expresion(r["p"], d), "$$", ""]
    if img:
        out += [f"![{m.nombre} junto a la nube de puntos]({img})", ""]
    out += ["**Paso 7 — residuos en las variables originales:**", "", residuos_tex(x, y, r, d), "",
            f"Error cuadrático (suma de residuos al cuadrado): $\\sum (y_i - \\hat y_i)^2 = "
            f"{_fmt(r['sse'], d)}$ · coeficiente de determinación $R^2 = {_fmt(r['r2'], d)}$.", ""]
    if r["aviso"]:
        out += [f"> ⚠️ Ojo: {r['aviso']}.", ""]
    return "\n".join(out)


# ---------------------------------------------------------------- gráficos


def graficar(out: Path, xl: str, yl: str, x, y, resultados, x0):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.rcParams.update({"figure.dpi": 150, "font.size": 10})
    lo, hi = float(x.min()), float(x.max())
    if x0 is not None:
        lo, hi = min(lo, x0), max(hi, x0)
    pad = 0.05 * (hi - lo or 1)
    xs = np.linspace(lo - pad, hi + pad, 400)
    colores = plt.rcParams["axes.prop_cycle"].by_key()["color"]

    def base(titulo):
        fig, ax = plt.subplots(figsize=(6.4, 4.2))
        ax.scatter(x, y, color="black", zorder=3, label="Datos", s=22)
        ax.set_xlabel(xl)
        ax.set_ylabel(yl)
        ax.set_title(titulo)
        ax.grid(alpha=0.3)
        return fig, ax

    fig, ax = base("Nube de puntos")
    fig.tight_layout()
    fig.savefig(out / "nube.png")
    plt.close(fig)

    def curva(m, r):
        with np.errstate(all="ignore"):
            ys = m.evaluar(r["p"], xs)
        ok = np.isfinite(ys)
        if m.requiere_x_pos:
            ok &= xs > 0
        return xs[ok], ys[ok]

    for i, (m, r) in enumerate(resultados):
        fig, ax = base(f"Ajuste {m.nombre.lower()}")
        cx, cy = curva(m, r)
        ax.plot(cx, cy, color=colores[i % len(colores)], label=f"${m.expresion(r['p'], 4)}$".replace("{,}", ","))
        if x0 is not None:
            y0 = float(m.evaluar(r["p"], np.array([x0]))[0])
            ax.scatter([x0], [y0], marker="*", s=120, color=colores[i % len(colores)], zorder=4,
                       label=f"Estimación en x = {x0:g}")
        ax.legend(fontsize=8)
        fig.tight_layout()
        fig.savefig(out / f"modelo-{m.clave}.png")
        plt.close(fig)

    fig, ax = base("Comparación de modelos")
    for i, (m, r) in enumerate(resultados):
        cx, cy = curva(m, r)
        ax.plot(cx, cy, color=colores[i % len(colores)], label=f"{m.nombre} (SSE = {(r['sse'] if r['sse'] > 1e-9 else 0):.4g})")
    if x0 is not None:
        ax.axvline(x0, color="gray", ls="--", lw=0.8)
    ax.legend(fontsize=8)
    fig.tight_layout()
    fig.savefig(out / "comparacion.png")
    plt.close(fig)


# ---------------------------------------------------------------- main


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("csv", type=Path)
    ap.add_argument("--modelos", default="recta,parabola,exponencial,potencial")
    ap.add_argument("--x0", type=float, help="valor de x donde se quiere estimar y")
    ap.add_argument("--decimales", type=int, default=4)
    ap.add_argument("--out-dir", type=Path, default=Path("."))
    ap.add_argument("--sin-graficos", action="store_true")
    a = ap.parse_args()

    xl, yl, x, y = leer_csv(a.csv)
    a.out_dir.mkdir(parents=True, exist_ok=True)
    d = a.decimales
    resultados: list[tuple[Modelo, dict]] = []
    avisos = []
    for clave in [c.strip() for c in a.modelos.split(",") if c.strip()]:
        m = MODELOS[clave]
        try:
            resultados.append((m, ajustar(m, x, y)))
        except ValueError as e:
            avisos.append(str(e))

    if not a.sin_graficos:
        graficar(a.out_dir, xl, yl, x, y, resultados, a.x0)

    md = [f"# Ajuste por mínimos cuadrados — {yl} en función de {xl}", "",
          f"Datos: $m = {len(x)}$ puntos; $x$ = «{xl}», $y$ = «{yl}».", ""]
    if not a.sin_graficos:
        md += ["![Nube de puntos](nube.png)", ""]
    for i, (m, r) in enumerate(resultados, 1):
        md.append(seccion_modelo(i, m, x, y, r, d, None if a.sin_graficos else f"modelo-{m.clave}.png"))
    md += ["## Comparación", "",
           "| Modelo | Función aproximante | $\\sum (y_i-\\hat y_i)^2$ | $R^2$ |"
           + (f" $\\hat y({a.x0:g})$ |" if a.x0 is not None else ""),
           "|---|---|:---:|:---:|" + (":---:|" if a.x0 is not None else "")]
    for m, r in sorted(resultados, key=lambda t: t[1]["sse"]):
        fila = f"| {m.nombre} | ${m.expresion(r['p'], d)}$ | ${_fmt(r['sse'], d)}$ | ${_fmt(r['r2'], d)}$ |"
        if a.x0 is not None:
            fila += f" ${_fmt(float(m.evaluar(r['p'], np.array([a.x0]))[0]), d)}$ |"
        md.append(fila)
    md.append("")
    if not a.sin_graficos:
        md += ["![Comparación de modelos](comparacion.png)", ""]
    if avisos:
        md += ["> Modelos descartados por el dominio de los datos: " + "; ".join(avisos), ""]
    (a.out_dir / "reporte.md").write_text("\n".join(md) + "\n", encoding="utf-8")

    js = {
        "x": x.tolist(), "y": y.tolist(), "x0": a.x0, "modelos": [
            {"modelo": m.clave, "parametros": r["p"], "solucion_sistema": dict(zip(m.nombres_lin, r["A"].tolist())),
             "matriz_normal": r["M"].tolist(), "termino_independiente": r["b"].tolist(),
             "sse": r["sse"], "r2": r["r2"], "rmse": r["rmse"],
             "y0": (float(m.evaluar(r["p"], np.array([a.x0]))[0]) if a.x0 is not None else None)}
            for m, r in resultados],
        "descartados": avisos,
    }
    (a.out_dir / "resultados.json").write_text(json.dumps(js, indent=2, ensure_ascii=False), encoding="utf-8")

    for m, r in sorted(resultados, key=lambda t: t[1]["sse"]):
        extra = ""
        if a.x0 is not None:
            extra = f"  ŷ({a.x0:g}) = {float(m.evaluar(r['p'], np.array([a.x0]))[0]):.6g}"
        expr = m.expresion(r["p"], 5).replace("{,}", ",").replace("\\,", " ")
        print(f"{m.nombre:28s} {expr:50s} SSE = {r['sse']:.6g}  R² = {r['r2']:.5f}{extra}")
        if r["aviso"]:
            print(f"{'':28s} ⚠️  {r['aviso']}")
    for av in avisos:
        print("descartado:", av)
    print(f"✓ Reporte: {a.out_dir / 'reporte.md'}")


if __name__ == "__main__":
    main()
