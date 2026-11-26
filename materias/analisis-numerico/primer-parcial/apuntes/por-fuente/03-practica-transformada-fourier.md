# Práctica: transformada de Fourier (ejercicios 11 y 12)

> Fuente: fuentes/clases/Transformadas de Laplace/Series Fourier - Transformada de Fourier.pdf, págs. 1–4

---

## Índice

- [p. 1] — Definición de transformada de Fourier (cómo la plantea el profe)
- [p. 1] — 📝 Ejercicio 11.b — transformada de $f(t) = e^{-t}$ para $t > 0$
- [p. 2] — 📝 Ejercicio 11.a — transformada del pulso rectangular $|t| < 3$
- [p. 3] — Definición de antitransformada de Fourier
- [p. 3] — Truco: evaluar la antitransformada en $t = 0$ para calcular una integral impropia
- [p. 2] — 📝 Ejercicio 12 — valor de $\int_0^{\infty} \frac{\operatorname{sen}(x)}{x}\,dx$ a partir del 11.a

> Nota sobre el archivo: el OneNote lleva el título "Transformada de Fourier" (13/09/2020) y
> contiene SOLO los ejercicios 11 y 12 de transformada de Fourier. No hay ejercicios de
> Laplace en esta fuente.

## Definición de transformada de Fourier — [p. 1]

El profe arranca cada transformada escribiendo la definición y reemplazando $f(t)$ por su
expresión en el único tramo donde no es nula, lo que recorta los límites de integración:

$$
\mathcal{F}[f(t)] = F(\omega) = \int_{-\infty}^{\infty} f(t)\, e^{-j\omega t}\, dt
$$

- Si $f(t)$ vale cero fuera de un intervalo, la integral se escribe directamente sobre ese
  intervalo (en el 11.b queda $\int_0^{\infty}$; en el 11.a queda $\int_{-3}^{3}$).
- Antes de integrar, el profe dibuja la función $f(t)$ a mano (gráfico de $e^{-t}$ para
  $t > 0$, gráfico del pulso entre $-3$ y $3$).
- Las exponenciales con el mismo exponente en $t$ se juntan en una sola: $e^{-t} \cdot
  e^{-j\omega t} = e^{-t(1 + j\omega)}$.

<details>
<summary>📝 Ejercicio 11.b — [p. 1]: transformada de Fourier de f(t) = e^(−t) para t &gt; 0</summary>

**Ejercicio n.º 11.** Halle las transformadas de Fourier de las siguientes funciones y
dibuje su espectro continuo de amplitud:

$$
\text{b)}\quad f(t) =
\begin{cases}
e^{-t} & \text{si } t > 0 \\
0 & \text{si } t < 0
\end{cases}
$$

(El profe resuelve primero el ítem b y después el a.)

<details>
<summary>Ver resolución</summary>

**Paso 1:** gráfico de $f(t)$: la exponencial decreciente que arranca en $f(0) = 1$ y
tiende a cero para $t \to \infty$; para $t < 0$ la función es nula (en el dibujo el profe
tacha en rojo la rama de $e^{-t}$ a la izquierda del eje, que NO forma parte de $f$).

**Paso 2:** definición de la transformada:

$$
\mathcal{F}[f(t)] = F(\omega) = \int_{-\infty}^{\infty} f(t)\, e^{-j\omega t}\, dt
$$

**Paso 3:** como $f(t) = 0$ para $t < 0$, la integral queda solo de $0$ a $\infty$ con
$f(t) = e^{-t}$:

$$
F(\omega) = \int_0^{\infty} e^{-t} \cdot e^{-j\omega t}\, dt
$$

**Paso 4:** se juntan las exponenciales:

$$
= \int_0^{\infty} e^{-t(1 + j\omega)}\, dt
$$

**Paso 5:** se integra (primitiva de la exponencial dividida por la constante del
exponente) y se evalúa entre $0$ e $\infty$:

$$
= \left. \frac{e^{-t(1 + j\omega)}}{-1 - j\omega} \right|_{0}^{\infty}
$$

**Paso 6:** en $t \to \infty$ la exponencial vale $0$ y en $t = 0$ vale $1$:

$$
= \frac{0 - 1}{-1 - j\omega}
$$

**Paso 7:** resultado (recuadrado):

$$
F(\omega) = \frac{1}{1 + j\omega}
$$

*(El espectro continuo de amplitud que pide el enunciado no está dibujado en la fuente.)*

</details>

</details>

<details>
<summary>📝 Ejercicio 11.a — [p. 2]: transformada de Fourier del pulso rectangular |t| &lt; 3</summary>

**Ejercicio n.º 11.** Halle las transformadas de Fourier de las siguientes funciones y
dibuje su espectro continuo de amplitud:

$$
\text{a)}\quad f(t) =
\begin{cases}
1 & \text{si } |t| < 3 \\
0 & \text{si } |t| > 3
\end{cases}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** gráfico de $f(t)$: un pulso de altura $1$ entre $t = -3$ y $t = 3$, cero
fuera.

**Paso 2:** definición con los límites recortados al intervalo donde $f(t) = 1$:

$$
F(\omega) = \int_{-3}^{3} 1 \cdot e^{-j\omega t}\, dt
$$

**Paso 3:** se integra la exponencial:

$$
= \left. \frac{e^{-j\omega t}}{-j\omega} \right|_{-3}^{3}
$$

**Paso 4:** se evalúa en los extremos:

$$
= \frac{-1}{j\omega} \left( e^{-3j\omega} - e^{3j\omega} \right)
$$

**Paso 5:** se invierte el orden de la resta (para absorber el signo menos) y se multiplica
y divide por $2$ (anotado en verde) para que aparezca la forma del seno:

$$
= \frac{1}{\omega} \left( \frac{e^{3j\omega} - e^{-3j\omega}}{2j} \right) \cdot 2
$$

**Paso 6:** como $\dfrac{e^{3j\omega} - e^{-3j\omega}}{2j} = \operatorname{sen}(3\omega)$,
queda el resultado:

$$
F(\omega) = \frac{2}{\omega} \cdot \operatorname{sen}(3\omega) \qquad (\text{si } \omega \neq 0)
$$

La aclaración "(si $\omega \neq 0$)" está en rojo en el manuscrito: la expresión no vale
en $\omega = 0$ porque se dividió por $\omega$.

*(El espectro continuo de amplitud que pide el enunciado no está dibujado en la fuente.)*

</details>

</details>

## Definición de antitransformada de Fourier — [p. 3]

$$
f(t) = \mathcal{F}^{-1}[F(\omega)] = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega)\, e^{j\omega t}\, d\omega
$$

## Truco: evaluar la antitransformada en $t = 0$ para calcular una integral impropia — [p. 3]

Para calcular una integral impropia del tipo $\int \frac{\operatorname{sen}(x)}{x}\,dx$ a
partir de una transformada ya conocida, el profe:

1. Escribe la antitransformada de $F(\omega)$, que contiene el factor $e^{j\omega t}$.
   Ese factor "no lo queremos ahí" (anotación en rojo): hay que hacerlo desaparecer.
2. Evalúa en $t = 0$: $e^{j\omega \cdot 0} = 1$, y el valor $f(0)$ se lee directamente
   del gráfico de la función original.
3. Así queda una igualdad entre un número ($f(0)$) y la integral impropia de $F(\omega)$.
4. Hace un cambio de variable para llevar el integrando a la forma pedida.
5. Usa la paridad del integrando para pasar de $(-\infty, \infty)$ a $(0, \infty)$:
   si el integrando es par, la integral sobre $(0, \infty)$ es la mitad.

<details>
<summary>📝 Ejercicio 12 — [p. 2]: calcular ∫₀^∞ sen(x)/x dx a partir del ejercicio 11.a</summary>

**Ejercicio n.º 12.** En base al ejercicio anterior (parte a), calcule el valor de la
integral:

$$
\int_0^{\infty} \frac{\operatorname{sen}(x)}{x}\, dx
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** definición de antitransformada de Fourier:

$$
f(t) = \mathcal{F}^{-1}[F(\omega)] = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega)\, e^{j\omega t}\, d\omega
$$

**Paso 2:** se reemplaza $F(\omega) = \dfrac{2}{\omega} \operatorname{sen}(3\omega)$
(resultado del 11.a):

$$
f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{2}{\omega} \cdot \operatorname{sen}(3\omega) \cdot e^{j\omega t}\, d\omega
$$

El profe marca en rojo el factor $e^{j\omega t}$: "No lo queremos ahí".

**Paso 3:** se evalúa en $t = 0$. Del gráfico del pulso (ejercicio 11.a) se lee
$f(0) = 1$ ("Gráfico"), y $e^{j\omega \cdot 0} = 1$:

$$
f(0) = \frac{1}{2\pi} \int_{-\infty}^{\infty} \frac{2 \operatorname{sen}(3\omega)}{\omega}\, d\omega
$$

**Paso 4:** se simplifica el $2$ del numerador con el $2$ de $2\pi$ (tachados en azul):

$$
\frac{1}{\pi} \int_{-\infty}^{\infty} \frac{\operatorname{sen}(3\omega)}{\omega}\, d\omega = 1
$$

**Paso 5:** cambio de variable (en verde):

$$
3\omega = x, \qquad \omega = \frac{x}{3}, \qquad d\omega = \frac{dx}{3}
$$

$$
\frac{1}{\pi} \int_{-\infty}^{\infty} \frac{\operatorname{sen}(x)}{x/3} \cdot \frac{dx}{3} = 1
$$

**Paso 6:** el $3$ del denominador $x/3$ se cancela con el $\frac{1}{3}$ del diferencial:

$$
\frac{1}{\pi} \int_{-\infty}^{\infty} \frac{\operatorname{sen}(x)}{x}\, dx = 1
$$

$$
\int_{-\infty}^{\infty} \frac{\operatorname{sen}(x)}{x}\, dx = \pi
$$

**Paso 7:** como el integrando $\dfrac{\operatorname{sen}(x)}{x}$ es par ("Porque $f(x)$
es par", con un bosquejo de la función oscilante simétrica respecto del eje vertical),
la integral de $0$ a $\infty$ es la mitad. Resultado (recuadrado):

$$
\int_0^{\infty} \frac{\operatorname{sen}(x)}{x}\, dx = \frac{\pi}{2}
$$

</details>

</details>
