# Mini-simulacro del martes — solo lo que estudiaste (Fourier · Laplace · Z)

> Fuente: enunciados reales del **2025-1C** (Tema 2 y 1er recuperatorio, `examenes/INDICE.md`); resultados de `examenes/resueltos/RESOLUCIONES-2025.md`. Generado 2026-10-06, 13:00.
>
> **Cómo usarlo:** 8 ítems de 1 punto, **90 minutos de reloj**, solo con el ayudamemoria oficial y la tabla de integrales. Antes de resolver cada ítem, **escribí en una línea qué receta es** ("división por $t$", "completar impar", …). Esa línea es el entrenamiento de identificación: en el parcial tenés que hacer eso mismo en 30 segundos. Después abrí la corrección: primero fijate si identificaste bien, después el resultado. Si identificaste bien y llegaste al resultado: ese ítem **está**. Si dudaste en la identificación: releé esa fila de la tabla de decisión del machete. Si identificaste bien pero no salió: rehacé solo ese "tu turno" de la guía.

---

## Ej1 — Fourier (2025-1C recuperatorio, Ej1)

$f(x) = 2x$ en $(0, 2)$.

**a)** Completar para que la STF sea de senos y desarrollarla.

**b)** Con ese resultado, calcular los $C_n$ de la SEF.

**c)** Graficar el espectro de amplitudes ($|C_n|$ en función de $\omega_0 n$).

<div style="height: 6cm"></div>

<details>
<summary><strong>Corrección Ej1</strong></summary>

**Identificación.** a) "Serie de senos" ⇒ completar **impar** (guía 01 §6). b) "$C_n$ a partir de la STF" ⇒ $C_n = \tfrac12(a_n - j\,b_n)$, sin integrar. c) "Espectro" ⇒ bastones de $|C_n|$ en $\pm\omega_0, \pm2\omega_0, \dots$

**a)** Impar: $f(x) = 2x$ en $(-2, 2)$, $T = 4$, $L = 2$, $\omega_0 = \pi/2$. $a_0 = a_n = 0$.

$$
b_n = \frac{2}{2}\int_0^2 2x\,\operatorname{sen}\!\left(\frac{n\pi}{2}x\right)dx = -\frac{8(-1)^n}{n\pi}
\qquad
S(x) = -\frac{8}{\pi}\sum_{n=1}^{\infty}\frac{(-1)^n}{n}\operatorname{sen}\!\left(\frac{n\pi}{2}x\right)
$$

**b)** $C_n = \tfrac12(0 - j\,b_n) = \dfrac{4(-1)^n}{n\pi}\,j$, $C_0 = 0$.

**c)** $|C_n| = \dfrac{4}{|n|\pi}$: bastones simétricos en $\pm\frac{\pi}{2}, \pm\pi, \pm\frac{3\pi}{2}, \dots$ de altura $\frac{4}{\pi}, \frac{2}{\pi}, \frac{4}{3\pi}, \dots$; nulo en $n = 0$.

</details>

<div style="break-before: page"></div>

## Ej2 — Laplace

**a)** (2025-1C rec, Ej2a) Calcular

$$
\int_0^{\infty}\frac{e^{-5t} - e^{-10t}}{t}\,dt
$$

**b)** (2025-1C T2, Ej2a) Transformada de Laplace de $\operatorname{sen}^3 t$, $t > 0$.

**c)** (2025-1C T2, Ej2b) Antitransformar **usando convolución**:

$$
Y(s) = \frac{s^2}{(s^2+1)^2}
$$

<div style="height: 6cm"></div>

<details>
<summary><strong>Corrección Ej2</strong></summary>

**Identificación.** a) Integral de $0$ a $\infty$ con un $/t$ ⇒ **división por $t$** (guía 02 §5): sacar factor $e^{-st}$, transformar lo que queda, integrar de $s$ a $\infty$ y evaluar. b) Potencia de seno ⇒ **Euler** (§6). c) "Antitransformar por convolución" un producto de dos cosas de tabla ⇒ $Y = F \cdot G$, $y = \int_0^t f(u)\,g(t-u)\,du$ (§10).

**a)** Factor común $e^{-5t}$: la integral es $\mathcal{L}\!\left[\dfrac{1 - e^{-5t}}{t}\right]$ en $s = 5$.

$$
\mathcal{L}\!\left[\frac{1 - e^{-5t}}{t}\right] = \int_s^{\infty}\left(\frac{1}{u} - \frac{1}{u+5}\right)du = \ln\frac{s+5}{s}
\qquad\Longrightarrow\qquad
\ln\frac{10}{5} = \ln 2
$$

**b)** $\operatorname{sen}^3 t = \tfrac34\operatorname{sen}t - \tfrac14\operatorname{sen}3t$, entonces

$$
\mathcal{L}[\operatorname{sen}^3 t] = \frac34\cdot\frac{1}{s^2+1} - \frac14\cdot\frac{3}{s^2+9}
$$

**c)** $Y = \dfrac{s}{s^2+1}\cdot\dfrac{s}{s^2+1}$ ⇒ $y = \cos t * \cos t = \displaystyle\int_0^t \cos u\cos(t-u)\,du$. Producto a suma: $\cos u\cos(t-u) = \tfrac12[\cos t + \cos(2u - t)]$.

$$
y(t) = \frac12\,t\cos t + \frac12\operatorname{sen}t
$$

</details>

<div style="break-before: page"></div>

## Ej4 — Transformada Z

**a)** (2025-1C T2, Ej4a) Resolver mediante Z:

$$
\sum_{n=0}^{\infty}\cos(\pi n)\,3^{-n}
$$

**b)** (2025-1C rec, Ej4a) Verdadero o falso, justificando: la región de convergencia de la transformada Z de

$$
x(n) = \begin{cases}(-2)^n & n \text{ par}\\ 4^{-n} & n \text{ impar}\end{cases}
$$

es $|z| > 2$.

<div style="height: 6cm"></div>

<details>
<summary><strong>Corrección Ej4</strong></summary>

**Identificación.** a) "Resolver la suma mediante Z": es $\sum x(n)\,c^{-n} = X(z)\big|_{z=c}$ con $x(n) = \cos(\pi n)$ y $c = 3$ (guía 04 §5). b) Sucesión por paridad ⇒ dos geométricas, **ROC = intersección** (§4).

**a)** Con la tabla, $\mathcal{Z}[\cos(an)] = \dfrac{z(z - \cos a)}{z^2 - 2z\cos a + 1}$ y $a = \pi$:

$$
X(z) = \frac{z(z+1)}{z^2 + 2z + 1} = \frac{z}{z+1}
\qquad\Longrightarrow\qquad
\sum = X(3) = \frac{3}{4}
$$

(Chequeo: $\cos(\pi n) = (-1)^n$, así que la suma es $\sum (-1/3)^n = \frac{1}{1 + 1/3} = \frac34$. ✔)

**b)** Pares: $\sum_k (-2)^{2k} z^{-2k} = \sum_k (4/z^2)^k$, converge si $|z| > 2$. Impares: $\sum_k 4^{-(2k+1)} z^{-(2k+1)} = \frac{1}{4z}\sum_k \left(\frac{1}{16 z^2}\right)^k$, converge si $|z| > \frac14$. Intersección: $|z| > 2$. **Verdadero.**

$$
X(z) = \frac{z^2}{z^2 - 4} + \frac{4z}{16z^2 - 1}
$$

</details>

---

**Puntaje:** 1 punto por ítem, 8 en total. Son exactamente los 8 que necesitás. Sin Sistemas, cada ítem que falle acá es un punto que no se recupera: anotá cuáles fallaron y rehacé **solo esos** antes de las 15:00.

*Generado el 2026-10-06 a partir de `examenes/INDICE.md` (2025-1C T2 y recuperatorio) y `examenes/resueltos/RESOLUCIONES-2025.md`; resultados verificados con sympy en las guías 01, 02 y 04.*
