# Práctica — Serie Trigonométrica de Fourier

> Fuente: fuentes/clases/series de fourier/Series Fourier - STF.pdf, págs. 1–10

---

## Índice

- [p. 1] — Regla de oro: siempre graficar y anotar $T$, $L$, $\omega_0$
- [p. 1] — Fórmulas de la STF y de sus coeficientes
- [p. 1] — Interpretación del $a_0/2$
- [p. 1] — Valores de $\cos(m\pi)$ y $\operatorname{sen}(m\pi)$
- [p. 1] — 📝 Ejercicio 1c — STF de $f(t)=t^2$ en $(-\pi,\pi)$
- [p. 2] — Usar la serie para sumar una serie numérica
- [p. 2] — 📝 Ejercicio 1d — Suma de $\sum (-1)^n/n^2$ a partir de la serie
- [p. 2] — Enunciado del Ejercicio 2
- [p. 2] — Funciones pares e impares y Series de Fourier
- [p. 2] — 📝 Ejercicio 2a — Onda cuadrada impar, $T=6$
- [p. 3] — Sumatoria en función de $k$: sólo armónicas impares
- [p. 3] — 📝 Ejercicio 2b — Pulso par de altura 6, $T=8$
- [p. 2] — 📝 Ejercicio 2c — Onda cuadrada $\pm 8$, $T=4$ (sin resolución)
- [p. 5] — Resumen: función impar vs. función par
- [p. 5] — Funciones impares desplazadas
- [p. 5] — 📝 Ejercicio 2d — Diente de sierra $f(t)=4t$, $T=10$
- [p. 6] — 📝 Ejercicio 3 — Onda triangular, $T=8$, y suma de $\sum 1/(2k-1)^2$
- [p. 7] — Completar una función definida en un intervalo (serie de cosenos / de senos)
- [p. 7] — 📝 Ejercicio 4b — $f(x)=x$ en $(0,2)$: serie de cosenos y de senos
- [p. 8] — 📝 Ejercicio 4a — $f(x)=\operatorname{sen}x$ en $(0,\pi)$: serie de senos y de cosenos
- [p. 8] — Tabla de integrales: ortogonalidad de senos y cosenos
- [p. 7] — 📝 Ejercicios 4c, 4d, 4e — $\cos t$, $e^t$, $\pi-t$ (sin resolución)
- [p. 8] — Simetría de media onda (S.M.O.)
- [p. 8] — 📝 Ejercicio 5 — Onda triangular: por qué sólo senos y sólo frecuencias impares
- [p. 9] — Cómo completar una función para que tenga simetría de media onda
- [p. 9] — 📝 Ejercicio 6 — Completar en $[-\pi,\pi]$ con S.M.O.
- [p. 9] — 📝 Ejercicio 7 — Términos nulos con paridad + S.M.O.; ¿puede ser par o impar?
- [p. 9] — 📝 Bonus track — $f(t)=t^3$ en $(0,1)$ en serie de cosenos y suma de $\sum 1/(2k+1)^4$

---

## Regla de oro: siempre graficar y anotar $T$, $L$, $\omega_0$ — [p. 1]

El profesor arranca la práctica con una regla que repite en TODOS los ejercicios
("Siempre:"):

- ✓ **Graficar** la función (y su extensión periódica).
- ✓ **Poner los datos fundamentales:** $T$, $L$ y $\omega_0$.

En todos los ejercicios se usan las relaciones

$$
L = \frac{T}{2}, \qquad \omega_0 = \frac{\pi}{L}
$$

## Fórmulas de la STF y de sus coeficientes — [p. 1]

$$
S(t) = \frac{a_0}{2} + \sum_{m=1}^{\infty} a_m \cos(m\,\omega_0\,t) + b_m \operatorname{sen}(m\,\omega_0\,t)
$$

$$
a_0 = \frac{1}{L}\int_{-L}^{L} f(t)\,dt
$$

$$
a_m = \frac{1}{L}\int_{-L}^{L} f(t)\cos(m\,\omega_0\,t)\,dt
$$

$$
b_m = \frac{1}{L}\int_{-L}^{L} f(t)\operatorname{sen}(m\,\omega_0\,t)\,dt
$$

## Interpretación del $a_0/2$ — [p. 1]

(Texto tipeado en la fuente.) El $a_0/2$ es el término independiente de la Serie
Trigonométrica de Fourier, y es la **componente de continua** de la señal: es un valor
constante tal que el área encerrada entre la función y esta constante por arriba y por
abajo es la misma (en el gráfico de la fuente, una recta punteada horizontal con las
áreas amarillas por encima y por debajo iguales).

En el caso de una función que es lineal en cada período, el valor del $a_0/2$ se ve a
simple vista. En cambio, si la función no fuera lineal, se debe hacer el cálculo.

## Valores de $\cos(m\pi)$ y $\operatorname{sen}(m\pi)$ — [p. 1]

Al evaluar los coeficientes en $\pm\pi$ aparecen siempre $\cos(m\pi)$ y $\operatorname{sen}(m\pi)$.
El profesor lo resuelve con la circunferencia trigonométrica: los puntos $m\pi$ caen
sobre el eje horizontal en $\pm 1$, por lo tanto el seno es $0$ y el coseno alterna.

| $m$ | $\cos(m\pi)$ |
|---|---|
| 0 | 1 |
| 1 | −1 |
| 2 | 1 |
| 3 | −1 |

$$
\cos(m\pi) = (-1)^m, \qquad \operatorname{sen}(m\pi) = 0, \qquad \cos(m\pi) = \cos(-m\pi)
$$

<details>
<summary>📝 Ejercicio 1c — [p. 1]: STF de f(t) = t² en (−π, π)</summary>

**1) c)** $f(t) = t^2$ en $(-\pi,\pi)$, $f(t+2\pi) = f(t)$.

*(En la fuente sólo aparecen los ítems c) y d) del Ejercicio 1; a) y b) no están.)*

<details>
<summary>Ver resolución</summary>

**Paso 1:** Graficar (parábolas repetidas con período $2\pi$, picos de altura $\pi^2$ en
$\pm\pi$, $\pm 3\pi$) y anotar los datos fundamentales:

$$
T = 2\pi, \qquad L = \frac{T}{2} = \pi, \qquad \omega_0 = \frac{\pi}{L} = 1
$$

**Paso 2:** Escribir la serie y calcular $a_0$.

$$
S(t) = \frac{a_0}{2} + \sum_{m=1}^{\infty} a_m \cos(m\,\omega_0\,t) + b_m \operatorname{sen}(m\,\omega_0\,t)
$$

$$
a_0 = \frac{1}{L}\int_{-L}^{L} f(t)\,dt = \frac{1}{\pi}\int_{-\pi}^{\pi} t^2\,dt = \frac{1}{\pi}\cdot\left.\frac{t^3}{3}\right|_{-\pi}^{\pi} = \frac{1}{3\pi}\left(\pi^3 + \pi^3\right) = \frac{2}{3}\pi^2
$$

$$
\frac{a_0}{2} = \frac{\pi^2}{3}
$$

**Paso 3:** Calcular $a_m$ (la primitiva se escribe directamente; en el margen se anota
$f(x) = f(-x)$ y $\cos(m\pi)=\cos(-m\pi)$).

$$
a_m = \frac{1}{L}\int_{-L}^{L} f(t)\cos(m\,\omega_0\,t)\,dt = \frac{1}{\pi}\int_{-\pi}^{\pi} t^2\cos(mt)\,dt
$$

$$
= \left[\frac{(m^2t^2 - 2)\operatorname{sen}(mt) + 2\,m\,t\cos(mt)}{\pi\,m^3}\right]_{-\pi}^{\pi}
$$

El término con $\operatorname{sen}(mt)$ se anula en $\pm\pi$ (porque $\operatorname{sen}(m\pi) = 0$) y queda

$$
= \frac{2m\pi\cos(m\pi)}{\pi\,m^3} + \frac{2m\pi\cos(m\pi)}{\pi\,m^3} = \frac{4\cos(m\pi)}{m^2}
$$

Con $\cos(m\pi) = (-1)^m$:

$$
a_m = \frac{4(-1)^m}{m^2}
$$

**Paso 4:** Calcular $b_m$.

$$
b_m = \frac{1}{L}\int_{-L}^{L} f(t)\operatorname{sen}(m\,\omega_0\,t)\,dt = \frac{1}{\pi}\int_{-\pi}^{\pi} t^2\operatorname{sen}(mt)\,dt
$$

$$
= \left[\frac{(2 - m^2t^2)\cos(mt) + 2\,m\,t\operatorname{sen}(mt)}{\pi\,m^3}\right]_{-\pi}^{\pi}
$$

$$
= \frac{(2 - m^2\pi^2)\cos(m\pi)}{\pi\,m^3} - \frac{(2 - m^2\pi^2)\cos(-m\pi)}{\pi\,m^3} = 0
$$

**Paso 5:** Serie resultante.

$$
S(t) = \frac{\pi^2}{3} + \sum_{m=1}^{\infty} \frac{4(-1)^m}{m^2}\cos(m\,t)
$$

</details>

</details>

## Usar la serie para sumar una serie numérica — [p. 2]

Cuando la serie converge a la función, $S(x) = f(x)$. Evaluando ambos lados en un
punto cómodo (típicamente $x = 0$) se obtiene el valor de una serie numérica.

Nota tipeada en la fuente: **ojo que puede haber $S(x)$ con senos y cosenos, e igual se
puede hallar el valor al que converge una serie**, porque por ejemplo si $x = 0$ aparecen
$\cos(n\pi)$ y $\operatorname{sen}(n\pi)$: el coseno vale 1 y el seno vale 0 *[así está
escrito en la fuente; en $x=0$ los argumentos son $\cos(0)=1$ y $\operatorname{sen}(0)=0$]*.

<details>
<summary>📝 Ejercicio 1d — [p. 2]: suma de Σ (−1)ⁿ/n² a partir de la serie de 1c</summary>

**d)** A partir de la Serie obtenida en c), halle el resultado de la serie numérica

$$
\sum_{n=1}^{\infty} \frac{(-1)^n}{n^2}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Evaluar la serie en $t = 0$ (el $\cos(0)$ se marca como $= 1$).

$$
S(0) = \frac{\pi^2}{3} + \sum_{m=1}^{\infty} \frac{4(-1)^m}{m^2}\cos(0)
$$

**Paso 2:** Usar que la serie representa a la función:

$$
S(x) = f(x) \quad\Rightarrow\quad S(0) = f(0)
$$

$$
f(0) = ? \qquad f(0) = 0
$$

**Paso 3:** Despejar la suma.

$$
\frac{\pi^2}{3} + \sum_{m=1}^{\infty} \frac{4(-1)^m}{m^2} = 0
$$

$$
\sum_{m=1}^{\infty} \frac{(-1)^m}{m^2} = -\frac{\pi^2}{12}
$$

</details>

</details>

## Enunciado del Ejercicio 2 — [p. 2]

**Ejercicio n° 2:** Desarrolle las siguientes funciones de período $T$ en Serie
Trigonométrica de Fourier:

a) $f(x) = \begin{cases} 1 & \text{si } x \in (0,3) \\ -1 & \text{si } x \in (-3,0)\end{cases}$ y $f(x) = f(x+6)$

b) $f(t) = \begin{cases} 6 & \text{si } |t| < 2 \\ 0 & \text{si } 2 < |t| < 4\end{cases}$ y $f(t) = f(t+8)$

c) $f(t) = \begin{cases} 8 & 0 < t < 2 \\ -8 & 2 < t < 4\end{cases}$ y $f(t) = f(t+4)$

d) $f(t) = 4t$, $0 < t < 10$ y $f(t) = f(t+10)$

## Funciones pares e impares y Series de Fourier — [p. 2–3]

- **Función impar:** $f(x) = -f(-x)$.
- **Función par:** $f(t) = f(-t)$.
- **¡La integral de una función impar en un intervalo simétrico da cero!** (las áreas a
  izquierda y derecha del origen se cancelan). Por eso

$$
a_0 = \frac{1}{L}\int_{-L}^{L} f(x)\,dx = 0 \quad \text{para toda función impar}
$$

- **Paridad del producto.** Para decidir qué coeficientes se anulan, se mira la paridad
  del integrando completo:
  - $f(x)\cdot\cos(m\omega_0 x)$ con $f$ impar: impar × par = **impar** ⇒ $a_m = 0$ para toda
    función impar.
  - $f(x)\cdot\operatorname{sen}(m\omega_0 x)$ con $f$ impar: impar × impar = **par** ⇒ $b_m \neq 0$.
  - $f(t)\cdot\cos(m\omega_0 t)$ con $f$ par: par × par = **par** ⇒ $a_m \neq 0$.
  - $f(t)\cdot\operatorname{sen}(m\omega_0 t)$ con $f$ par: par × impar = **impar** ⇒ $b_m = 0$.
- **Integral de una función par en intervalo simétrico:**

$$
\int_{-L}^{L} f(x)\,dx = 2\int_{0}^{L} f(x)\,dx
$$

  **Ventaja:** sólo se analiza una de las ramas de la función. Así, para $f$ impar:

$$
b_m = \frac{2}{L}\int_{0}^{L} f(x)\operatorname{sen}(m\,\omega_0\,x)\,dx
$$

  y para $f$ par:

$$
a_0 = \frac{2}{L}\int_{0}^{L} f(t)\,dt, \qquad a_m = \frac{2}{L}\int_{0}^{L} f(t)\cos(m\,\omega_0\,t)\,dt
$$

<details>
<summary>📝 Ejercicio 2a — [p. 2–3]: onda cuadrada impar ±1, T = 6</summary>

**a)** $f(x) = \begin{cases} 1 & \text{si } x \in (0,3) \\ -1 & \text{si } x \in (-3,0)\end{cases}$, $f(x) = f(x+6)$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Graficar (escalones de altura $+1$ en $(0,3)$ y $-1$ en $(-3,0)$) y datos:

$$
T = 6, \qquad L = 3, \qquad \omega_0 = \frac{\pi}{3}
$$

**Paso 2:** Reconocer la paridad: ✓ función impar, $f(x) = -f(-x)$.

**Paso 3:** $a_0$: la integral de una función impar en un intervalo simétrico da cero.

$$
a_0 = \frac{1}{L}\int_{-L}^{L} f(x)\,dx = 0
$$

**Paso 4:** $a_m$: el integrando $f(x)\cos(m\omega_0 x)$ es impar × par = impar.

$$
a_m = 0 \quad \text{para toda función impar}
$$

**Paso 5:** $b_m$: el integrando $f(x)\operatorname{sen}(m\omega_0 x)$ es impar × impar = par, así
que se integra sólo una rama y se duplica.

$$
b_m = \frac{2}{L}\int_{0}^{L} f(x)\operatorname{sen}(m\,\omega_0\,x)\,dx = \frac{2}{3}\int_{0}^{3} 1\cdot\operatorname{sen}\!\left(m\tfrac{\pi}{3}x\right)dx
$$

$$
= \frac{2}{3}\cdot\left.\frac{-\cos\!\left(m\tfrac{\pi}{3}x\right)}{m\pi/3}\right|_{0}^{3} = \left.\frac{-2}{m\pi}\cos\!\left(m\tfrac{\pi}{3}x\right)\right|_{0}^{3} = \frac{-2}{m\pi}\left[(-1)^m - 1\right]
$$

**Paso 6:** Separar por paridad de $m$:

- Si $m$ es par: $b_m = 0$.
- Si $m$ es impar: $b_m = \dfrac{4}{m\pi}$.

**Paso 7:** Escribir la serie con la sumatoria en función de $k$ (ver sección
siguiente):

$$
S(x) = \frac{4}{\pi}\sum_{k=0}^{\infty} \frac{\operatorname{sen}\!\left[(2k+1)\tfrac{\pi}{3}x\right]}{2k+1}
$$

</details>

</details>

## Sumatoria en función de $k$: sólo armónicas impares — [p. 3]

Cuando los coeficientes se anulan para $m$ par, **se pone a la sumatoria en función de
$k$, de forma tal de hacer explícito que sólo habrá armónicas impares**: se reemplaza
$m = 2k+1$ y la suma arranca en $k = 0$.

Si les gusta $(2k-1)$, arrancar la sumatoria en $1$.

<details>
<summary>📝 Ejercicio 2b — [p. 3–4]: pulso par de altura 6, T = 8</summary>

**b)** $f(t) = \begin{cases} 6 & \text{si } |t| < 2 \\ 0 & \text{si } 2 < |t| < 4\end{cases}$, $f(t) = f(t+8)$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Graficar (pulso de altura 6 entre $-2$ y $2$, cero entre $2$ y $4$, repetido) y
datos:

$$
T = 8, \qquad L = 4, \qquad \omega_0 = \frac{\pi}{4}
$$

**Paso 2:** Paridad: función par, $f(t) = f(-t)$.

**Paso 3:** $a_0$ (integrando par ⇒ se duplica la mitad). La función y su área entre 2 y 4
son nulas.

$$
a_0 = \frac{1}{L}\int_{-L}^{L} f(t)\,dt = \frac{2}{L}\int_{0}^{L} f(t)\,dt = \frac{2}{4}\int_{0}^{2} 6\,dt = 6
$$

$$
\frac{a_0}{2} = 3
$$

**Paso 4:** $a_m$ (par × par = par).

$$
a_m = \frac{1}{L}\int_{-L}^{L} f(t)\cos(m\,\omega_0\,t)\,dt = \frac{2}{L}\int_{0}^{L} f(t)\cos(m\,\omega_0\,t)\,dt
$$

$$
= \frac{2}{4}\int_{0}^{2} 6\cos\!\left(m\tfrac{\pi}{4}t\right)dt = 3\cdot\left.\frac{\operatorname{sen}\!\left(m\tfrac{\pi}{4}t\right)}{m\pi/4}\right|_{0}^{2} = \frac{12}{m\pi}\left[\operatorname{sen}\!\left(m\tfrac{\pi}{2}\right) - \operatorname{sen}(0)\right]
$$

(el $\operatorname{sen}(0)$ se tacha porque vale 0).

**Paso 5:** Tabular $\operatorname{sen}(m\pi/2)$ sobre la circunferencia trigonométrica
(los $m$ pares caen en el eje horizontal, los impares alternan arriba/abajo):

| $m$ | $\operatorname{sen}(m\pi/2)$ |
|---|---|
| 0 | 0 |
| 1 | 1 (+) |
| 2 | 0 |
| 3 | −1 (−) |
| 4 | 0 |
| 5 | 1 (+) |
| ⋮ | ⋮ |

- Si $m$ es par ⇒ $a_m = 0$.
- Si $m$ es impar ⇒ $a_m = \pm\dfrac{12}{m\pi}$, alternadamente. Con $m = 2k+1$:

$$
a_m = \frac{12}{(2k+1)\pi}(-1)^k
$$

**Paso 6:** $b_m$ (par × impar = impar ⇒ integral nula).

$$
b_m = \frac{1}{L}\int_{-L}^{L} f(t)\operatorname{sen}(m\,\omega_0\,t)\,dt = 0
$$

**Paso 7:** Serie.

$$
S(t) = 3 + \sum_{k=0}^{\infty} \frac{12}{(2k+1)\pi}(-1)^k\cos\!\left[(2k+1)\tfrac{\pi}{4}t\right]
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 2c — [p. 2]: onda cuadrada ±8, T = 4</summary>

**c)** $f(t) = \begin{cases} 8 & 0 < t < 2 \\ -8 & 2 < t < 4\end{cases}$, $f(t) = f(t+4)$.

*(sin resolución en la fuente)*

</details>

## Resumen: función impar vs. función par — [p. 5]

**Función impar:**

$$
a_0 = 0, \qquad a_m = 0, \qquad b_m \neq 0 \quad \left(\int_{-L}^{L} f(x)\,dx = 2\int_{0}^{L} f(x)\,dx \text{ para el integrando par}\right)
$$

**Función par:**

$$
a_0 \neq 0, \qquad a_m \neq 0, \qquad b_m = 0 \quad \left(\int_{-L}^{L} f(x)\,dx = 2\int_{0}^{L} f(x)\,dx\right)
$$

## Funciones impares desplazadas — [p. 5–6]

Si una función se puede escribir como $f(t) = g(t) + k$ con $g$ impar y $k$ constante,
$f$ es una **función impar desplazada**. Su serie se arma a partir de la de $g$:

$$
S_g(t) = \sum_{m=1}^{\infty} b_m\operatorname{sen}(m\,\omega_0\,t) = g(t)
$$

$$
S_f(t) = k + \sum_{m=1}^{\infty} b_m\operatorname{sen}(m\,\omega_0\,t) = g(t) + k = f(t)
$$

donde el **$k$ es el $a_0/2$** (el valor medio de $f$, que se lee del gráfico), y los
$b_m$ son los de $g$.

Texto tipeado en la fuente: *las funciones impares desplazadas no son funciones impares
puras porque no se cumple que $f(x) = -f(-x)$, pero sus series de Fourier comparten
similitudes: el $a_n$ se anula.*

Además, por periodicidad, integrar sobre un período cualquiera da lo mismo:

$$
\int_{-L}^{L} = \int_{0}^{T}
$$

<details>
<summary>📝 Ejercicio 2d — [p. 5]: diente de sierra f(t) = 4t, T = 10</summary>

**d)** $f(t) = 4t$, $0 < t < 10$, $f(t) = f(t+10)$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Graficar (rampas de 0 a 40 en cada período, repetidas en $(-10,0)$, $(0,10)$,
$(10,20)$) y datos:

$$
T = 10, \qquad L = 5, \qquad \omega_0 = \frac{\pi}{5}
$$

**Paso 2:** Reconocer la estructura. Se define $g(t) = 4t - 20$ (la misma rampa bajada 20):

- Valor medio de $g(t)$ $= 0$.
- Valor medio de $f(t)$ $= 20$.
- ✓ $f(t) = g(t) + k$, con $k = 20$.
- ✓ $g(t)$ es impar.
- ✓ $f(t)$ es una función impar desplazada.

**Paso 3:** Series.

$$
S_g(t) = \sum_{m=1}^{\infty} b_m\operatorname{sen}(m\,\omega_0\,t) = g(t)
$$

$$
S_f(t) = k + \sum_{m=1}^{\infty} b_m\operatorname{sen}(m\,\omega_0\,t) = g(t) + k = f(t)
$$

El $k$ es el $a_0/2$: en el gráfico de $f$ se marca $a_0/2 = 20$.

**Paso 4:** $a_m = 0$ (por ser impar desplazada). Para $b_m$ se integra sobre un período
$(0, T)$ usando $\int_{-L}^{L} = \int_{0}^{T}$:

$$
b_m = \frac{1}{L}\int_{0}^{T} f(t)\operatorname{sen}(m\,\omega_0\,t)\,dt = \frac{1}{5}\int_{0}^{10} 4t\operatorname{sen}\!\left(m\tfrac{\pi}{5}t\right)dt
$$

$$
= \frac{4}{5}\left[\frac{\operatorname{sen}\!\left(m\tfrac{\pi}{5}t\right)}{m^2\pi^2/25} - \frac{t\cos\!\left(m\tfrac{\pi}{5}t\right)}{m\pi/5}\right]_{0}^{10}
$$

$$
= \frac{4}{5}\left[\frac{-10\cos(m\cdot 2\pi)}{m\pi/5}\right]
$$

($\cos(m\cdot 2\pi) = 1$: el punto $2m\pi$ cae en $+1$ sobre la circunferencia.)

$$
b_m = \frac{-40}{m\pi}
$$

**Paso 5:** Serie de $f$ (el término $k = 20$ más la serie $S_g(t)$):

$$
S_f(t) = 20 - \frac{40}{\pi}\sum_{m=1}^{\infty} \frac{\operatorname{sen}\!\left(m\tfrac{\pi}{5}t\right)}{m}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 3 — [p. 6–7]: onda triangular T = 8, paridad y suma de Σ 1/(2k−1)²</summary>

**Ejercicio n° 3:** Sea $f(t) = \begin{cases} 2-t & 0 < t < 4 \\ t-6 & 4 < t < 8\end{cases}$ y $f(t) = f(t+8)$.

a) Grafique la función $f(t)$ y redefínala para el período $(-4;4)$.

b) En función al punto anterior desarrolle la STF teniendo en cuenta la paridad de la
función.

c) En base a la respuesta anterior calcule

$$
\sum_{k=1}^{\infty} \frac{1}{(2k-1)^2}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** Graficar. En $(0,4)$ la recta baja de 2 a $-2$; en $(4,8)$ sube de $-2$ a 2;
trasladando el tramo $(4,8)$ a $(-4,0)$ (en rojo en la fuente) queda una onda triangular
simétrica respecto del eje vertical. Redefinida en $(-4;4)$:

$$
f(t) = \begin{cases} t+2 & \text{si } -4 < t < 0 \\ 2-t & \text{si } 0 < t < 4\end{cases}
$$

$$
T = 8, \qquad L = 4, \qquad \omega_0 = \frac{\pi}{4}
$$

**Paso 2 (b):** Función par ⇒ $b_m = 0$ (sólo cosenos). Además

$$
\frac{a_0}{2} = 0 \quad \text{(se observa gráficamente)}
$$

**Paso 3:** $a_m$ integrando una sola rama:

$$
a_m = \frac{2}{L}\int_{0}^{L} f(t)\cos(m\,\omega_0\,t)\,dt = \frac{2}{4}\int_{0}^{4} (2-t)\cos\!\left(m\tfrac{\pi}{4}t\right)dt
$$

$$
= \frac{1}{2}\int_{0}^{4}\left[2\cos\!\left(m\tfrac{\pi}{4}t\right) - t\cos\!\left(m\tfrac{\pi}{4}t\right)\right]dt
$$

$$
= \frac{1}{2}\left[\frac{2\operatorname{sen}\!\left(m\tfrac{\pi}{4}t\right)}{m\pi/4} - \frac{\cos\!\left(m\tfrac{\pi}{4}t\right)}{m^2\pi^2/16} - \frac{t\operatorname{sen}\!\left(m\tfrac{\pi}{4}t\right)}{m\pi/4}\right]_{0}^{4}
$$

$$
= \frac{1}{2}\left[-\frac{16(-1)^m}{m^2\pi^2} + \frac{16}{m^2\pi^2}\right]
$$

- $m$ par: $a_m = 0$.
- $m$ impar: $a_m = \dfrac{16}{m^2\pi^2}$.

**Paso 4:** El profesor anota: *sólo frecuencias impares… ¿tiene simetría de media onda?*
La serie, con $m = 2k+1$:

$$
S(t) = \frac{16}{\pi^2}\sum_{k=0}^{\infty} \frac{\cos\!\left[(2k+1)\tfrac{\pi}{4}t\right]}{(2k+1)^2}
$$

**Paso 5 (c):** Se pide $\sum_{k=1}^{\infty} \frac{1}{(2k-1)^2}$. Se reescribe la serie con
$(2k-1)$ arrancando en $k=1$ para que coincida con la suma pedida:

$$
S(t) = \frac{16}{\pi^2}\sum_{k=1}^{\infty} \frac{\cos\!\left[(2k-1)\tfrac{\pi}{4}t\right]}{(2k-1)^2}
$$

**Paso 6:** Evaluar en $t = 0$:

$$
S(0) = \frac{16}{\pi^2}\sum_{k=1}^{\infty} \frac{1}{(2k-1)^2}
$$

$$
S(0) = f(0), \qquad f(0) = 2
$$

$$
\frac{16}{\pi^2}\sum_{k=1}^{\infty} \frac{1}{(2k-1)^2} = 2 \quad\Rightarrow\quad \sum_{k=1}^{\infty} \frac{1}{(2k-1)^2} = \frac{\pi^2}{8}
$$

</details>

</details>

## Completar una función definida en un intervalo (serie de cosenos / de senos) — [p. 7]

**Ejercicio n° 4 (enunciado):** Dadas las siguientes funciones definidas sólo en un
intervalo:

a) $f(x) = \operatorname{sen} x$, $x \in (0,\pi)$
b) $f(x) = x$, $x \in (0,2)$
c) $f(t) = \cos(t)$, $0 < t < \pi$
d) $f(t) = e^t$, $0 < t < 1$
e) $f(t) = \pi - t$, $0 < t < \pi$

i) Complete cada función en todo el eje real para que la Serie Trigonométrica de Fourier
sea sólo de cosenos y desarrolle cada Serie.

ii) Ídem anterior pero Serie de Senos.

La regla que aplica el profesor en cada ítem:

- **Sólo de cosenos ⇒ completar como función PAR** (se refleja la rama dada respecto del
  eje vertical). Entonces $b_m = 0$ y quedan $a_0$, $a_m$.
- **Sólo senos ⇒ completar como función IMPAR** (se refleja respecto del origen). Entonces
  $a_0 = a_m = 0$ y queda $b_m$.
- El intervalo dado es **medio período**: si la función está definida en $(0, L)$, el
  período es $T = 2L$ y $\omega_0 = \pi/L$.
- Los coeficientes se calculan sobre la rama dada con las fórmulas $\frac{2}{L}\int_0^L$.

*(En la fuente el profesor resuelve primero el ítem b) y después el a); acá se respeta ese
orden.)*

<details>
<summary>📝 Ejercicio 4b — [p. 7–8]: f(x) = x en (0,2) — serie de cosenos (i) y de senos (ii)</summary>

**b)** $f(x) = x$, $x \in (0,2)$. i) Completar para serie sólo de cosenos y desarrollar;
ii) ídem para serie de senos.

<details>
<summary>Ver resolución</summary>

**Paso 1 (i):** Sólo de cosenos ⇒ **par**. Se completa con la reflexión $-x$ en $(-2,0)$
(en verde en el gráfico de la fuente, un "techo" en $|x|$). Datos:

$$
T = 4, \qquad L = 2, \qquad \omega_0 = \frac{\pi}{2}
$$

**Paso 2:** Coeficientes nulos y valor medio:

$$
b_m = 0, \qquad \frac{a_0}{2} = 1 \quad \text{(gráfico)}
$$

**Paso 3:** $a_m$:

$$
a_m = \frac{2}{2}\int_{0}^{2} x\cos\!\left(m\tfrac{\pi}{2}x\right)dx = \left[\frac{\cos\!\left(m\tfrac{\pi}{2}x\right)}{m^2\pi^2/4} + \frac{x\operatorname{sen}\!\left(m\tfrac{\pi}{2}x\right)}{m\pi/2}\right]_{0}^{2}
$$

$$
= \frac{4(-1)^m}{m^2\pi^2} - \frac{4}{m^2\pi^2}
$$

- $m$ par: $a_m = 0$.
- $m$ impar: $a_m = \dfrac{-8}{m^2\pi^2}$.

**Paso 4:** El profesor pregunta *¿S.M.O.? ¡No!* (la función completada no tiene simetría
de media onda a pesar de tener sólo armónicas impares en esta serie). Serie:

$$
S(x) = 1 - \frac{8}{\pi^2}\sum_{k=1}^{\infty} \frac{\cos\!\left[(2k+1)\tfrac{\pi}{2}x\right]}{(2k+1)^2}
$$

*[así está escrito en la fuente: sumatoria desde $k=1$ con $(2k+1)$]*

**Paso 5 (ii):** Sólo senos ⇒ **impar**. Se completa prolongando la recta $x$ hacia
$(-2,0)$ (en rojo en la fuente). Datos:

$$
T = 4, \qquad L = 2, \qquad \omega_0 = \frac{\pi}{2}
$$

$$
a_0 = a_m = 0
$$

**Paso 6:** $b_m$:

$$
b_m = \frac{2}{2}\int_{0}^{2} x\operatorname{sen}\!\left(m\tfrac{\pi}{2}x\right)dx = \left[\frac{\operatorname{sen}\!\left(m\tfrac{\pi}{2}x\right)}{m^2\pi^2/4} - \frac{t\cos\!\left(m\tfrac{\pi}{2}x\right)}{m\pi/2}\right]_{0}^{2}
$$

*[en la fuente aparece una $t$ en el numerador del segundo término, donde la variable es $x$]*

$$
b_m = \frac{-4(-1)^m}{m\pi}
$$

**Paso 7:** Serie:

$$
S(x) = \frac{-4}{\pi}\sum_{m=1}^{\infty} \frac{(-1)^m\operatorname{sen}\!\left(m\tfrac{\pi}{2}x\right)}{m}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 4a — [p. 8]: f(x) = sen x en (0,π) — serie de senos (ii) y de cosenos (i)</summary>

**a)** $f(x) = \operatorname{sen} x$, $x \in (0,\pi)$. ii) Completar para serie sólo de senos;
i) completar para serie sólo de cosenos.

<details>
<summary>Ver resolución</summary>

**Paso 1 (ii):** Sólo serie de senos ⇒ **impar**. Al reflejar respecto del origen, la
media onda de $(0,\pi)$ se completa con la media onda negativa en $(-\pi,0)$: queda
exactamente $f(x) = \operatorname{sen}(x)$ en todo el eje. Datos:

$$
T = 2\pi, \qquad L = \pi, \qquad \omega_0 = 1
$$

**Paso 2:** Razonamiento (texto tipeado en la fuente): una Serie de Fourier es, por
definición, una suma de senos y cosenos que representan a una función periódica. La
función $f(x) = \operatorname{sen}(x)$ es una función periódica, por definición. ¿Qué senos y
qué cosenos debo sumar para obtener al $\operatorname{sen}(x)$? Simplemente el
$\operatorname{sen}(x)$. Su serie de Fourier tiene un solo término (no es infinita, a
diferencia de las que veníamos trabajando).

$$
S(x) = \operatorname{sen}(x)
$$

**Paso 3:** Verificación con las fórmulas. $a_0 = a_m = 0$ y

$$
b_m = \frac{2}{\pi}\int_{0}^{\pi} \operatorname{sen}(x)\operatorname{sen}(mx)\,dx = \frac{2\operatorname{sen}(m\pi)}{\pi - \pi m^2}
$$

- Si $m \neq 1$ ⇒ $b_m = 0$.
- Si $m = 1$ ⇒ $b_m = \dfrac{0}{0}$ (indeterminado). Se resuelve por L'Hôpital:

$$
\lim_{m\to 1} \frac{2\operatorname{sen}(m\pi)}{\pi - \pi m^2} = \lim_{m\to 1} \frac{2\pi\cos(m\pi)}{-2\pi m} = 1
$$

Por lo tanto $S(x) = \operatorname{sen}(x)$, como se había razonado.

**Paso 4:** También sale más fácil usando la tabla de integrales (ver sección siguiente):
la integral de $\operatorname{sen}(nx)\operatorname{sen}(kx)$ en $(0,\pi)$ vale $0$ si $n \neq k$ y
$\pi/2$ si $n = k$. El profesor anota: *algo similar va a suceder en el ej. 4) c) i)
(cosenos – par)*.

**Paso 5 (i):** Serie de cosenos (resolución inserta como imagen en la fuente, con otra
letra). PAR ⇒ $b_m = 0$. Al reflejar la media onda respecto del eje vertical queda
$|\operatorname{sen} x|$, de período $\pi$:

$$
T = \pi, \qquad L = \frac{\pi}{2}, \qquad \omega_0 = 2
$$

$$
a_0 = \frac{1}{L}\int_{0}^{T} f(x)\,dx = \frac{2}{\pi}\int_{0}^{\pi} \operatorname{sen}(x)\,dx = \frac{2}{\pi}\left(-\cos x\right)\Big|_{0}^{\pi} = \frac{2}{\pi}(1+1) = \frac{4}{\pi}
$$

$$
\frac{a_0}{2} = \frac{2}{\pi}
$$

$$
a_m = \frac{1}{L}\int_{0}^{T} f(x)\cos(2mx)\,dx = \frac{2}{\pi}\int_{0}^{\pi} \operatorname{sen}(x)\cos(2mx)\,dx
$$

La integral se toma de Wolfram:

$$
\int_{0}^{\pi} \sin(x)\cos(2nx)\,dx = \frac{2\cos^2(\pi n)}{1 - 4n^2}
$$

y como $\cos^2(m\pi) = 1$:

$$
a_m = \frac{2\cos^2(m\pi)}{1 - 4m^2}\cdot\frac{2}{\pi} \quad\Rightarrow\quad a_m = \frac{4}{(1-4m^2)\pi}
$$

$$
S(x) = \frac{2}{\pi} + \sum_{n=1}^{\infty} \frac{4}{(1-4n^2)\pi}\cos(2nx)
$$

</details>

</details>

## Tabla de integrales: ortogonalidad de senos y cosenos — [p. 8]

Fórmula 688 de la tabla ("Integrales definidas o impropias de funciones
trigonométricas"), que el profesor recomienda para los casos donde la función dada ya es
un seno o un coseno:

$$
\int_{0}^{\pi} \operatorname{sen}(nx)\operatorname{sen}(kx)\,dx = \int_{0}^{\pi} \cos(nx)\cos(kx)\,dx = \begin{cases} 0 & \text{si } n \neq k \\ \dfrac{\pi}{2} & \text{si } n = k\end{cases} \qquad n, k \in \mathbb{Z}
$$

<details>
<summary>📝 Ejercicios 4c, 4d, 4e — [p. 7]: cos t, eᵗ y π − t en medio período</summary>

c) $f(t) = \cos(t)$, $0 < t < \pi$
d) $f(t) = e^t$, $0 < t < 1$
e) $f(t) = \pi - t$, $0 < t < \pi$

i) Complete cada función en todo el eje real para que la STF sea sólo de cosenos y
desarrolle cada Serie. ii) Ídem anterior pero Serie de Senos.

*(sin resolución en la fuente; para 4c i el profesor sólo anticipa que va a pasar "algo
similar" al 4a ii: serie de un solo término, resuelta con la tabla de integrales)*

</details>

## Simetría de media onda (S.M.O.) — [p. 8]

Una función tiene **simetría de media onda** cuando

$$
f(x) = -f(x \pm L)
$$

es decir: desplazando medio período ($L$) y cambiando el signo se recupera la función.

**Consecuencia: S.M.O. = sólo armónicas impares** (los coeficientes de índice par se
anulan, tanto $a_m$ como $b_m$).

En el gráfico de la fuente se marca el procedimiento en dos pasos: **1°** desplazar la
primera mitad en $L$ (flecha horizontal) y **2°** espejarla respecto del eje $x$ (flecha
hacia abajo); si coincide con la segunda mitad, hay S.M.O.

<details>
<summary>📝 Ejercicio 5 — [p. 8–9]: onda triangular — por qué sólo senos y sólo frecuencias impares</summary>

**Ejercicio n° 5:** El desarrollo en serie de Fourier de la onda triangular (ver figura)
es:

$$
S(x) = \frac{8}{\pi^2}\left(\operatorname{sen}(wt) - \frac{1}{9}\operatorname{sen}(3wt) + \frac{1}{25}\operatorname{sen}(5wt) - \frac{1}{49}\operatorname{sen}(7wt) + \cdots\right)
$$

Figura: triángulo que sube de 0 a 1 en $(0, \pi/2)$, baja de 1 a $-1$ en $(\pi/2, 3\pi/2)$ y
vuelve a 0 en $2\pi$.

a) ¿Por qué sólo aparecen términos con senos?

b) ¿Por qué sólo aparecen términos con frecuencias impares?

<details>
<summary>Ver resolución</summary>

**Paso 1:** Completar la función hacia la izquierda (en rojo en la fuente: en $(-\pi, 0)$
la onda baja a $-1$ en $-\pi/2$ y sube a 0 en el origen, continuando el patrón).

**Paso 2 (a):** La función completada es **impar** ⇒ sólo senos.

**Paso 3 (b):** Tiene **simetría de media onda**: $f(x) = -f(x \pm L)$. En el gráfico, la
primera mitad (el triángulo de $(0,\pi)$) se desplaza $L = \pi$ (paso 1°) y se espeja
respecto del eje $x$ (paso 2°), y coincide con la segunda mitad (dibujada punteada en
rojo). S.M.O. ⇒ sólo armónicas impares.

</details>

</details>

## Cómo completar una función para que tenga simetría de media onda — [p. 9]

Dada la función en medio período, se completa el otro medio así:

1. **Desplazar $L$** (a izquierda o a derecha).
2. **Espejar con respecto al eje $x$** (cambiar el signo).

<details>
<summary>📝 Ejercicio 6 — [p. 9]: completar en [−π, π] para que tenga S.M.O.</summary>

**Ejercicio n° 6:** Dada la siguiente función definida en $\left[-\frac{\pi}{2}, \frac{\pi}{2}\right]$:
vale $0$ en $[-\pi/2, 0]$, vale $1$ en $[0, \pi/4]$ y sube linealmente de $1$ a $2$ en
$[\pi/4, \pi/2]$.

Complete la función en $[-\pi, \pi]$ para que tenga simetría de media onda.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Acá el período es $T = 2\pi$ y $L = \pi$; el tramo dado $[-\pi/2, \pi/2]$ es medio
período.

**Paso 2:** Desplazar $L$ (izq. o der.). En la fuente el tramo dado se desplaza $\pi$ hacia
la izquierda (dibujado punteado en rojo arriba, sobre $[-\pi, -\pi/2]$: un escalón en 1 y
luego la rampa hasta 2).

**Paso 3:** Espejar con respecto al eje $x$. El resultado (en rojo, trazo continuo):

- En $[-\pi, -3\pi/4]$: vale $-1$.
- En $[-3\pi/4, -\pi/2]$: baja linealmente de $-1$ a $-2$.
- En $[\pi/2, \pi]$: vale $0$ (es el espejo del tramo nulo $[-\pi/2, 0]$ desplazado).

Así $f(x) = -f(x \pm \pi)$ en todo $[-\pi, \pi]$.

</details>

</details>

<details>
<summary>📝 Ejercicio 7 — [p. 9]: términos nulos con paridad + S.M.O.; ¿puede ser par o impar?</summary>

**Ejercicio n° 7:**

a) Si una función es par y además tiene simetría de media onda, ¿qué términos serán
nulos de la Serie Trigonométrica de Fourier?

b) Sea

$$
S(x) = -\frac{\pi}{4} + \sum_{n=1}^{\infty} \frac{2}{\pi(2n-1)^2}\cos(nx) + \frac{(-1)^{2n-1}}{n}\operatorname{sen}(nx)
$$

la S.T.F. de $f(x)$. ¿Puede ser $f(x)$ una función par? ¿O impar? Justifique.

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** Par ⇒ $b_m = 0$. S.M.O. ⇒ de los $a_m$, los **pares** $= 0$ y los **impares**
$\neq 0$.

**Paso 2 (b):** No, porque si fuera par o impar no tendría senos o cosenos, pero la $S(x)$
tiene ambos.

**Paso 3:** El profesor agrega el caso **impar desplazada** (dibujo de una rampa impar
corrida hacia arriba): ahí $a_m = 0$ (aunque haya término independiente).

</details>

</details>

<details>
<summary>📝 Bonus track — [p. 9–10]: f(t) = t³ en (0,1) en serie de cosenos y suma de Σ 1/(2k+1)⁴</summary>

a) Desarrolle la función $f(t) = t^3$ para $t \in (0,1)$ en Serie de cosenos con $T = 2$.

b) En base a dicho desarrollo, y sabiendo que

$$
\sum_{n=1}^{\infty} \frac{(-1)^n}{n^2} = -\frac{\pi^2}{12}
$$

halle el valor de

$$
\sum_{k=0}^{\infty} \frac{1}{(2k+1)^4}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** $f(t) = t^3$, $t \in (0,1)$, cosenos, $T = 2$. Serie de cosenos ⇒ completar
como **par**: en $(-1, 0)$ se refleja como $-t^3$ (en azul en la fuente). Entonces $b_m = 0$.

$$
T = 2, \qquad L = 1, \qquad \omega_0 = \pi
$$

**Paso 2:** $a_0$:

$$
a_0 = \frac{2}{1}\int_{0}^{1} t^3\,dt = 2\cdot\left.\frac{t^4}{4}\right|_{0}^{1} = \frac{1}{2} \quad\Rightarrow\quad \frac{a_0}{2} = \frac{1}{4}
$$

**Paso 3:** $a_m$:

$$
a_m = \frac{2}{1}\int_{0}^{1} t^3\cos(m\pi t)\,dt
$$

$$
= 2\left[\left(\frac{3t^2}{m^2\pi^2} - \frac{6}{m^4\pi^4}\right)\cos(m\pi t) + \left(\frac{t^3}{m\pi} - \frac{6t}{m^2\pi^2}\right)\operatorname{sen}(m\pi t)\right]_{0}^{1}
$$

El término con $\operatorname{sen}(m\pi t)$ vale $0$ en ambos extremos.

$$
= 2\left[\left(\frac{3}{m^2\pi^2} - \frac{6}{m^4\pi^4}\right)(-1)^m - \left(\frac{-6}{m^4\pi^4}\right)\cdot 1\right]
$$

$$
= 2\left(\frac{3(-1)^m}{m^2\pi^2} - \frac{6(-1)^m}{m^4\pi^4} + \frac{6}{m^4\pi^4}\right)
$$

$$
a_m = \frac{6(-1)^m}{m^2\pi^2} + \frac{12\left[1 - (-1)^m\right]}{m^4\pi^4}
$$

El segundo sumando vale $0$ si $m$ es par y $\dfrac{24}{m^4\pi^4}$ si $m$ es impar.

**Paso 4:** Serie (el primer sumando se deja en $m$, el segundo sólo con armónicas impares
$m = 2k+1$):

$$
S(t) = \frac{1}{4} + \sum_{m=1}^{\infty} \frac{6(-1)^m}{m^2\pi^2}\cos(m\pi t) + 24\sum_{k=0}^{\infty} \frac{\cos\!\left[(2k+1)\pi t\right]}{(2k+1)^4\pi^4}
$$

**Paso 5 (b):** Evaluar en $t = 0$: $S(0) = 0$ (porque $f(0) = 0$).

$$
\frac{1}{4} + \frac{6}{\pi^2}\sum_{m=1}^{\infty} \frac{(-1)^m}{m^2} + \frac{24}{\pi^4}\sum_{k=0}^{\infty} \frac{1}{(2k+1)^4} = 0
$$

**Paso 6:** Reemplazar el dato $\sum (-1)^m/m^2 = -\pi^2/12$:

$$
\frac{1}{4} - \frac{1}{2} + \frac{24}{\pi^4}\sum_{k=0}^{\infty} \frac{1}{(2k+1)^4} = 0
$$

$$
\sum_{k=0}^{\infty} \frac{1}{(2k+1)^4} = \frac{1}{4}\cdot\frac{\pi^4}{24}
$$

$$
\sum_{k=0}^{\infty} \frac{1}{(2k+1)^4} = \frac{\pi^4}{96}
$$

</details>

</details>

---

*Generado el 2026-10-02 a partir de `fuentes/clases/series de fourier/Series Fourier - STF.pdf`
(OneNote de la práctica de STF, guía tipeada + resolución manuscrita del profesor, págs.
1–10; la pág. 11 está en blanco).*
