# Práctica de Transformada de Laplace (OneNote de la clase)

> Fuente: fuentes/clases/Transformadas de Laplace/Transformada de Laplace.pdf, págs. 1–27

---

## Índice

- [p. 1] — Parte 1: transformada directa y tabla básica
- [p. 1] — 📝 Ejercicio 1: transformadas por tabla y linealidad (a–d)
- [p. 2] — Propiedades: 1ª traslación, multiplicación por tⁿ, 2ª traslación
- [p. 2] — 📝 Ejercicio 2: transformadas usando propiedades (a–f)
- [p. 4] — Escalón, forma alternativa de la 2ª traslación, exponenciales complejas y binomio
- [p. 3] — 📝 Ejercicio 3: transformadas con pasos algebraicos (a–f)
- [p. 7] — Teorema del valor inicial (TVI)
- [p. 7] — 📝 Ejercicio 4: hallar k con el TVI
- [p. 8] — Antitransformada directa: ajustar constantes, completar cuadrados, reconocer t·sen
- [p. 8] — 📝 Ejercicio 5: antitransformadas directas (a–h)
- [p. 10] — Fracciones simples: el método del profe (tapado, división previa, factor repetido, cuadrático irreducible, e^{-as})
- [p. 10] — 📝 Ejercicio 6: antitransformadas por fracciones simples (a, b, c, h, j resueltos; d, e, f, g, i sin resolver)
- [p. 14] — Teorema del valor final (TVF)
- [p. 14] — 📝 Ejercicio 7: TVF y TVI (a resuelto; b, c sin resolver)
- [p. 15] — Parte 3: ecuaciones diferenciales por Laplace
- [p. 15] — 📝 Ejercicio 8: EDO por Laplace (a, i resueltos; b–h y optativo sin resolver)
- [p. 18] — Sistemas de ecuaciones diferenciales
- [p. 18] — 📝 Ejercicio 9: sistemas de EDO (b resuelto; a, c, d, e y optativo sin resolver)
- [p. 19] — Parte 4: teorema de convolución
- [p. 19] — 📝 Ejercicio 10: transformar una integral de convolución
- [p. 20] — 📝 Ejercicio 11: antitransformar por convolución (a–c)
- [p. 22] — Ecuaciones integrales e integro-diferenciales
- [p. 22] — 📝 Ejercicio 12: ecuaciones integrales (a, e resueltos; b, c, d, f sin resolver)
- [p. 25] — Parte 5: evaluación de integrales impropias (definición y división por t)
- [p. 25] — 📝 Ejercicio 13: integrales por Laplace (c, d resueltos; a, b, e sin resolver)
- [p. 25] — 📝 Ejercicio extra (retomado de la clase pasada): ∫₀^∞ sen t / t dt

---

## Parte 1: transformada directa y tabla básica — [p. 1]

La primera parte de la guía es transformada directa usando la **tabla** y la
**propiedad de linealidad**. Las fórmulas de tabla que el profe anota al margen
mientras resuelve:

$$
\mathcal{L}\{t^n\} = \frac{n!}{s^{n+1}}
$$

$$
\mathcal{L}\{e^{at}\} = \frac{1}{s-a}
$$

$$
\mathcal{L}\{\cos(at)\} = \frac{s}{s^2+a^2}
\qquad
\mathcal{L}\{\operatorname{sen}(at)\} = \frac{a}{s^2+a^2}
$$

<details>
<summary>📝 Ejercicio 1 — [p. 1]: transformadas por tabla y linealidad</summary>

Calcule las Transformadas de Laplace de las siguientes funciones, utilizando la tabla y la propiedad de linealidad:

a) $y(t) = 3 + 5t - 2t^2 + t^3$ ; $t>0$

b) $y(t) = \dfrac{1}{4}\,(e^{4t} - 1)$ ; $t>0$

c) $y(t) = \dfrac{1}{a^2}\,(e^{at} - at - 1)$ ; $t>0$

d) $y(t) = 4\cos(3t) - 5\operatorname{sen}(2t)$ ; $t>0$

<details>
<summary>Ver resolución</summary>

**a)** $y(t) = 3 + 5t - 2t^2 + t^3$, $t>0$.

**Paso 1:** se transforma término a término con $\mathcal{L}(t^n) = \dfrac{n!}{s^{n+1}}$:

$$
Y(s) = \frac{3}{s} + \frac{5}{s^2} - \frac{2\cdot 2}{s^3} + \frac{6}{s^4}
$$

$$
Y(s) = \frac{3}{s} + \frac{5}{s^2} - \frac{4}{s^3} + \frac{6}{s^4}
$$

**b)** $y(t) = \dfrac{1}{4}\,(e^{4t} - 1)$, $t>0$.

**Paso 1:** con $\mathcal{L}(e^{at}) = \dfrac{1}{s-a}$:

$$
Y(s) = \frac{1}{4}\left(\frac{1}{s-4} - \frac{1}{s}\right)
$$

**Paso 2:** se suman las fracciones:

$$
Y(s) = \frac{1}{4}\left(\frac{4}{s(s-4)}\right) = \frac{1}{s(s-4)}
$$

**c)** $y(t) = \dfrac{1}{a^2}\,(e^{at} - at - 1)$, $t>0$.

**Paso 1:**

$$
Y(s) = \frac{1}{a^2}\left(\frac{1}{s-a} - \frac{a}{s^2} - \frac{1}{s}\right)
$$

**Paso 2:** al sumar las fracciones, en el numerador se cancelan $s^2$ con $-s^2$ y $-as$ con $+as$ (el profe los tacha), y el $a^2$ que queda se simplifica con el $\frac{1}{a^2}$ de afuera:

$$
Y(s) = \frac{1}{a^2}\left(\frac{s^2 - as + a^2 - s^2 + as}{s^2(s-a)}\right) = \frac{1}{s^2(s-a)}
$$

**d)** $y(t) = 4\cos(3t) - 5\operatorname{sen}(2t)$, $t>0$.

$$
Y(s) = 4\cdot\frac{s}{s^2+9} - 5\cdot\frac{2}{s^2+4} = \frac{4s}{s^2+9} - \frac{10}{s^2+4}
$$

</details>

</details>

## Propiedades: 1ª traslación, multiplicación por tⁿ, 2ª traslación — [p. 2]

Las tres propiedades que el profe anota en rojo/verde al margen del ejercicio 2:

**Primera propiedad de traslación** (una exponencial $e^{at}$ multiplicando desplaza $F$ en $s$):

$$
\mathcal{L}\left[f(t)\,e^{at}\right] = F(s-a)
$$

**Multiplicación por $t^n$** (derivar $n$ veces y cambiar de signo $n$ veces):

$$
\mathcal{L}\left[f(t)\,t^n\right] = (-1)^n\,F^{(n)}(s)
$$

Receta del profe para $t\cdot f(t)$: tomar $F(s)$ de tabla → **"Derivo"** → **"Cambio de
signo (una vez)"**. Si hay además una exponencial, primero se resuelve la multiplicación
por $t^n$ y *después* se aplica la 1ª traslación (reemplazar $s$ por $s-a$).

**Segunda propiedad de traslación** (función desplazada y apagada antes de $a$):

$$
g(t) = \begin{cases} f(t-a) & t>a \\ 0 & t<a \end{cases}
\qquad\Longrightarrow\qquad
\mathcal{L}[g(t)] = \mathcal{L}[f(t-a)] = F(s)\,e^{-as}
$$

(con el dibujo de $f(t-a)$: la misma campana de $f$ corrida hasta empezar en $t=a$).

<details>
<summary>📝 Ejercicio 2 — [p. 2]: transformadas usando propiedades</summary>

Utilizando las propiedades de la Transformada de Laplace halle $\mathcal{L}[f(t)]$:

a) $f(t) = t^2 e^{4t}$ ; $t>0$

b) $f(t) = 5e^{-5t}\cos(3t)$ ; $t>0$

c) $f(t) = e^{-t}\,t\,\operatorname{sen}(2t)$ ; $t>0$

d) $f(t) = (t-1)^4$ ; $t>1$

e) $f(t) = e^{-2t}\operatorname{sen}(2t) + t^2 e^{3t}$ ; $t>0$

f) $f(t) = 2t^2 e^{-t} - t + \cos(4t)$

<details>
<summary>Ver resolución</summary>

**a)** $f(t) = t^2\,e^{4t}$, $t>0$ — el $e^{4t}$ es **1ª traslación**: se transforma $t^2$ y se reemplaza $s$ por $s-4$.

$$
F(s) = \frac{2}{(s-4)^3}
$$

**b)** $f(t) = 5\,e^{-5t}\cos(3t)$, $t>0$ — 1ª traslación sobre $\cos(3t)$ con $a=-5$:

$$
F(s) = 5\cdot\frac{(s+5)}{(s+5)^2+9}
$$

**c)** $f(t) = e^{-t}\cdot t\cdot\operatorname{sen}(2t)$, $t>0$ — hay **1ª traslación** ($e^{-t}$) y **multiplicación por $t^n$** ($t$).

**Paso 1 (mult. × $t^n$):**

$$
\mathcal{L}[\operatorname{sen}(2t)] = \frac{2}{s^2+4}
$$

Derivo:

$$
\frac{-4s}{(s^2+4)^2}
$$

Cambio de signo (una vez):

$$
\frac{4s}{(s^2+4)^2}
$$

**Paso 2 (1ª prop. traslación):** se reemplaza $s$ por $s+1$:

$$
\mathcal{L}\left[e^{-t}\,t\,\operatorname{sen}(2t)\right] = \frac{4(s+1)}{\left[(s+1)^2+4\right]^2}
$$

**d)** $f(t) = (t-1)^4$, $t>1$ — **segunda propiedad de traslación** (la función está definida a partir de $t=1$):

$$
Y(s) = \frac{24}{s^5}\cdot e^{-s}
$$

**e)** $f(t) = e^{-2t}\operatorname{sen}(2t) + t^2 e^{3t}$, $t>0$ — los dos sumandos son 1ª traslación (en el segundo "también puede usarse mult. × $t^n$"):

$$
F(s) = \frac{2}{(s+2)^2+4} + \frac{2}{(s-3)^3}
$$

**f)** $f(t) = 2t^2 e^{-t} - t - \cos(4t)$ *(en el manuscrito el profe escribió el coseno con signo menos; el enunciado tipeado dice $+\cos(4t)$)*:

$$
F(s) = \frac{4}{(s+1)^3} - \frac{1}{s^2} - \frac{s}{s^2+16}
$$

</details>

</details>

## Escalón, forma alternativa de la 2ª traslación, exponenciales complejas y binomio — [p. 4]

Herramientas que aparecen a lo largo del ejercicio 3:

**Función definida en un intervalo** ($0<t<a$): se escribe como diferencia de dos
escalones, $y(t)\cdot E(t) - y(t)\cdot E(t-a)$; el primer término se transforma por tabla
y el segundo por 2ª propiedad de traslación (sale el factor $e^{-as}$).

**Forma alternativa de la 2ª prop. de traslación** (nota tipeada al margen, p. 4):

$$
\mathcal{L}\left[u(t-a)\cdot f(t)\right] = e^{-as}\cdot\mathcal{L}\left[f(t+a)\right]
$$

Ejemplo de la nota: $f(t) = t$ si $0\le t<1$, $0$ si $t\ge 1$. "$f(t)$ vale $t$ entre 0 y 1, y a
partir del 1 vale 0. Lo que valía, menos lo que valía a partir del $t=1$":

$$
f(t) = t - t\cdot u(t-1)
$$

$$
\mathcal{L}[f(t)] = \mathcal{L}[t] - \mathcal{L}\left[u(t-1)\cdot t\right]
$$

con $f(t)=t \Rightarrow f(t+1) = t+1$:

$$
\mathcal{L}[f(t)] = \mathcal{L}[t] - e^{-s}\,\mathcal{L}[t+1] = \frac{1}{s^2} - e^{-s}\left(\mathcal{L}[t] + \mathcal{L}[1]\right) = \frac{1}{s^2} - e^{-s}\left(\frac{1}{s^2} + \frac{1}{s}\right)
$$

**Senos y cosenos con fase, potencias y productos:** el profe los pasa a exponenciales
complejas, opera y vuelve a seno/coseno:

$$
\operatorname{sen}(x) = \frac{e^{jx} - e^{-jx}}{2j}
\qquad
\cos(x) = \frac{e^{jx} + e^{-jx}}{2}
$$

Como alternativa cita la tabla de integrales ("Funciones de la suma o diferencia de ángulos"):

$$
\operatorname{sen}(x\pm y) = \operatorname{sen}x\cos y \pm \operatorname{sen}y\cos x
$$

y la identidad trigonométrica para productos:

$$
\operatorname{sen}(x)\cos(y) = \frac{1}{2}\left[\operatorname{sen}(x+y) + \operatorname{sen}(x-y)\right]
$$

**Para potencias mayores a 3** (triángulo de Pascal, p. 6): coeficientes de $(a+b)^n$ por
grado: $1$; $1\,1$; $1\,2\,1$; $1\,3\,3\,1$; $1\,4\,6\,4\,1$; $1\,5\,10\,10\,5\,1$. Las potencias de
$a$ bajan de $n$ a $0$ y las de $b$ suben de $0$ a $n$ ($a^n b^0,\ a^{n-1}b^1,\ \dots,\ a^0 b^n$).
Para $(a-b)^n$: signos alternados, empezando con $+$.

**Exponencial de base cualquiera** $a^t$: aplicar logaritmo miembro a miembro y volver a
exponenciar, $a^t = e^{t\ln a}$.

**Ojo con la 2ª traslación:** $(t-1)^4$ con $t>1$ es 2ª traslación (ej. 2d), pero $(t-1)^4$
con $t>0$ **no**: hay que desarrollar el binomio y transformar término a término (ej. 3e).

<details>
<summary>📝 Ejercicio 3 — [p. 3]: transformadas con pasos algebraicos</summary>

Calcule las Transformadas de Laplace aplicando adecuadamente alguna propiedad conveniente o algún paso algebraico:

a) $y(t) = \dfrac{1}{a^2}$ ; $0<t<a$

b) $y(t) = \operatorname{sen}(5t + \pi/3)$ ; $t>0$

c) $y(t) = \cos^3(t)$ ; $t>0$

d) $y(t) = a^t$ ; $t>0$ ; $a\in\mathbb{R}^+$

e) $y(t) = (t-1)^4$ ; $t>0$

f) $y(t) = \operatorname{sen}(5t)\cos(2t)$ ; $t>0$

<details>
<summary>Ver resolución</summary>

**a)** $y(t) = \dfrac{1}{a^2}$, $0<t<a$.

**Paso 1:** gráfico: un escalón de altura $1/a^2$ entre $0$ y $a$. Se escribe como

$$
\text{①} = y(t)\cdot E(t) \qquad \text{②} = y(t)\cdot E(t-a)
$$

**Paso 2:** se transforma cada pedazo:

$$
\text{①} \;\to\; \frac{1}{a^2}\cdot\frac{1}{s}
$$

$$
\text{②} \;\to\; \frac{1}{a^2}\cdot\frac{1}{s}\cdot e^{-as} \qquad (2^{\text{da}}\text{ prop. traslación})
$$

**Paso 3:** $F(s) = \text{①} - \text{②}$:

$$
F(s) = \frac{1}{s\,a^2} - \frac{e^{-as}}{s\,a^2}
$$

$$
F(s) = \frac{1 - e^{-as}}{s\,a^2}
$$

**b)** $y(t) = \operatorname{sen}(5t + \pi/3)$, $t>0$.

**Paso 1:** se pasa a exponenciales complejas:

$$
y(t) = \frac{e^{j(5t+\pi/3)} - e^{-j(5t+\pi/3)}}{2j}
$$

$$
y(t) = \frac{1}{2j}\left[e^{j\pi/3}\,e^{j5t} - e^{-j\pi/3}\,e^{-j5t}\right]
$$

**Paso 2:** cada exponencial se escribe como $\cos + j\,\operatorname{sen}$:

$$
y(t) = \frac{1}{2j}\Big[\left(\cos(\pi/3) + j\operatorname{sen}(\pi/3)\right)\left(\cos(5t) + j\operatorname{sen}(5t)\right) - \left(\cos(-\pi/3) + j\operatorname{sen}(-\pi/3)\right)\left(\cos(-5t) + j\operatorname{sen}(-5t)\right)\Big]
$$

**Paso 3:** se distribuye; los términos en $\cos(5t)$ y en $\operatorname{sen}(5t)$ sin $j$ se cancelan (tachados en rojo):

$$
= \frac{1}{2j}\left[\frac{1}{2}\cos(5t) + \frac{j}{2}\operatorname{sen}(5t) + \frac{\sqrt{3}}{2}\,j\cos(5t) - \frac{\sqrt{3}}{2}\operatorname{sen}(5t)\right] - \left[\frac{1}{2}\cos(5t) - \frac{1}{2}\,j\operatorname{sen}(5t) - \frac{\sqrt{3}}{2}\,j\cos(5t) - \frac{\sqrt{3}}{2}\operatorname{sen}(5t)\right]
$$

$$
= \frac{1}{2j}\left[j\operatorname{sen}(5t) + \sqrt{3}\,j\cos(5t)\right]
$$

$$
f(t) = \frac{1}{2}\operatorname{sen}(5t) + \frac{\sqrt{3}}{2}\cos(5t)
$$

(El profe anota que lo mismo sale con la tabla de integrales: $\operatorname{sen}(x\pm y) = \operatorname{sen}x\cos y \pm \operatorname{sen}y\cos x$.)

**Paso 4:** se transforma por tabla:

$$
Y(s) = \frac{1}{2}\cdot\frac{5}{s^2+25} + \frac{\sqrt{3}}{2}\cdot\frac{s}{s^2+25}
$$

**c)** $y(t) = \cos^3(t)$, $t>0$.

**Paso 1:** exponenciales complejas y cubo:

$$
y(t) = \left(\frac{e^{jt} + e^{-jt}}{2}\right)^3 = \frac{1}{8}\left(e^{jt} + e^{-jt}\right)^3
$$

$$
y(t) = \frac{1}{8}\left(e^{3jt} + 3e^{2jt}e^{-jt} + 3e^{jt}e^{-2jt} + e^{-3jt}\right)
$$

**Paso 2:** se reagrupa para volver a cosenos:

$$
y(t) = \frac{1}{4}\left(\frac{e^{3jt} + e^{-3jt}}{2}\right) + \frac{3}{4}\left(\frac{e^{jt} + e^{-jt}}{2}\right)
$$

$$
y(t) = \frac{1}{4}\cos(3t) + \frac{3}{4}\cos(t)
$$

**Paso 3:**

$$
Y(s) = \frac{1}{4}\cdot\frac{s}{s^2+9} + \frac{3}{4}\cdot\frac{s}{s^2+1}
$$

**d)** $y(t) = a^t$, $t>0$, $a\in\mathbb{R}^+$.

**Paso 1:** logaritmo m.a.m. y volver a exponenciar:

$$
\ln y(t) = \ln a^t \qquad\Rightarrow\qquad e^{\ln a^t} = y(t) = e^{t\ln a}
$$

**Paso 2:**

$$
Y(s) = \frac{1}{s - \ln a}
$$

**e)** $f(t) = (t-1)^4$, $t>0$ — **"No se puede usar 2ª traslación"** (el dominio es $t>0$, no $t>1$).

**Paso 1:** se desarrolla el binomio:

$$
f(t) = t^4 - 4t^3 + 6t^2 - 4t + 1
$$

**Paso 2:**

$$
Y(s) = \frac{24}{s^5} - \frac{24}{s^4} + \frac{12}{s^3} - \frac{4}{s^2} + \frac{1}{s}
$$

**f)** $y(t) = \operatorname{sen}(5t)\cos(2t)$, $t>0$.

**Paso 1:** exponenciales complejas:

$$
y(t) = \left(\frac{e^{5jt} - e^{-5jt}}{2j}\right)\cdot\left(\frac{e^{2jt} + e^{-2jt}}{2}\right)
$$

$$
y(t) = \frac{1}{4j}\left(e^{7jt} + e^{3jt} - e^{-3jt} - e^{-7jt}\right)
$$

**Paso 2:** se reagrupa en senos:

$$
y(t) = \frac{1}{2}\left(\frac{e^{7jt} - e^{-7jt}}{2j}\right) + \frac{1}{2}\left(\frac{e^{3jt} - e^{-3jt}}{2j}\right)
$$

$$
y(t) = \frac{1}{2}\operatorname{sen}(7t) + \frac{1}{2}\operatorname{sen}(3t)
$$

**Paso 3:**

$$
Y(s) = \frac{1}{2}\cdot\frac{7}{s^2+49} + \frac{1}{2}\cdot\frac{3}{s^2+9}
$$

(Identidad trigonométrica equivalente: $\operatorname{sen}(x)\cos(y) = \frac{1}{2}[\operatorname{sen}(x+y) + \operatorname{sen}(x-y)]$.)

</details>

</details>

## Teorema del valor inicial (TVI) — [p. 7]

$$
\lim_{t\to 0} f(t) = \lim_{s\to\infty} s\,F(s)
$$

<details>
<summary>📝 Ejercicio 4 — [p. 7]: hallar k con el TVI</summary>

Sea $f(t) = k\,\operatorname{sen}\!\left(2t + \dfrac{\pi}{6}\right)$. Determine el valor de $k$ sabiendo que $\displaystyle\lim_{s\to\infty} s\,F(s) = 4$. Recuerde el Teorema de valor inicial.

<details>
<summary>Ver resolución</summary>

**Paso 1:** T.V.I.:

$$
\lim_{t\to 0} f(t) = \lim_{s\to\infty} s\,F(s)
$$

**Paso 2:** el dato dice que ese límite vale 4, entonces se evalúa $f$ en $t\to 0$:

$$
\lim_{t\to 0} k\,\operatorname{sen}(2t + \pi/6) = 4
$$

$$
\frac{k}{2} = 4 \qquad\Rightarrow\qquad k = 8
$$

</details>

</details>

## Antitransformada directa: ajustar constantes, completar cuadrados, reconocer t·sen — [p. 8]

Recetas que usa el profe en el ejercicio 5:

- **Ajustar la constante de tabla** multiplicando y dividiendo por lo que falta: para $\frac{25}{s^3}$ se multiplica y divide por $2$ (para que aparezca $\frac{2}{s^3} = \mathcal{L}\{t^2\}$); para $\frac{8}{s^2+3}$ se lee $3 = a^2$ y se multiplica y divide por $\sqrt{3}$.
- **Completar cuadrados** cuando el denominador cuadrático no factoriza: $s^2+6s+13 = (s+3)^2+4$, $s^2+2s+2 = (s+1)^2+1$. Después, 1ª traslación al revés: lo que está en $(s+a)$ sale como $e^{-at}$.
- **Partir el numerador** para que aparezca el mismo corrimiento que en el denominador: $s-1 = (s+1) - 1 - 1$.
- **Denominador al cuadrado** $\frac{4s}{(s^2+4)^2}$: "hace pensar en $t\cos(2t)$ o $t\,\operatorname{sen}(2t)$". Se **prueba**: se toma $\mathcal{L}[\operatorname{sen}(2t)]$, se deriva y se cambia el signo; si da lo pedido, listo.

<details>
<summary>📝 Ejercicio 5 — [p. 8]: antitransformadas directas</summary>

Calcule las Antitransformadas de Laplace de las siguientes funciones:

a) $Y(s) = \dfrac{25}{s^3}$

b) $Y(s) = \dfrac{8}{s^2+3} + \dfrac{1}{s}$

c) $Y(s) = \dfrac{12}{s-3} - \dfrac{8s}{s^2+4}$

d) $Y(s) = \dfrac{-1}{s+3}$

e) $Y(s) = \dfrac{6}{(s-1)^4}$

f) $Y(s) = \dfrac{s+3}{s^2+6s+13}$

g) $Y(s) = \dfrac{s-1}{s^2+2s+2}$

h) $Y(s) = \dfrac{4s}{(s^2+4)^2}$

<details>
<summary>Ver resolución</summary>

**a)** $Y(s) = \dfrac{25}{s^3}$. Se multiplica y divide por $2$:

$$
Y(s) = \frac{25}{s^3}\cdot\frac{2}{2} \qquad\Rightarrow\qquad y(t) = \frac{25}{2}\,t^2
$$

**b)** $Y(s) = \dfrac{8}{s^2+3} + \dfrac{1}{s}$. Se lee $3 = a^2$ y se multiplica y divide por $\sqrt{3}$:

$$
Y(s) = \frac{8}{s^2+3}\cdot\frac{\sqrt{3}}{\sqrt{3}} + \frac{1}{s}
$$

$$
y(t) = \frac{8}{\sqrt{3}}\operatorname{sen}(\sqrt{3}\,t) + 1
$$

**c)** $Y(s) = \dfrac{12}{(s-3)} - \dfrac{8s}{s^2+4}$:

$$
y(t) = 12\,e^{3t} - 8\cos(2t)
$$

**d)** $Y(s) = \dfrac{-1}{s+3}$:

$$
y(t) = -e^{-3t}
$$

**e)** $Y(s) = \dfrac{6}{(s-1)^4}$:

$$
y(t) = t^3\,e^{t}
$$

**f)** $Y(s) = \dfrac{s+3}{s^2+6s+13}$. Se completa el cuadrado:

$$
Y(s) = \frac{(s+3)}{(s+3)^2+4}
$$

$$
y(t) = \cos(2t)\,e^{-3t}
$$

**g)** $Y(s) = \dfrac{s-1}{s^2+2s+2}$. Se completa el cuadrado y se parte el numerador:

$$
Y(s) = \frac{s-1}{(s+1)^2+1}
$$

$$
Y(s) = \frac{(s+1)}{(s+1)^2+1} + \frac{-1-1}{(s+1)^2+1}
$$

$$
y(t) = \cos(t)\,e^{-t} - 2\operatorname{sen}(t)\,e^{-t}
$$

**h)** $Y(s) = \dfrac{4s}{(s^2+4)^2}$. "Hace pensar en $t\cos(2t)$ o $t\,\operatorname{sen}(2t)$". Probamos con $t\,\operatorname{sen}(2t)$:

$$
\mathcal{L}[\operatorname{sen}(2t)] = \frac{2}{s^2+4}
$$

Derivo:

$$
\frac{-4s}{(s^2+4)^2}
$$

Cambio de signo:

$$
\frac{4s}{(s^2+4)^2} \quad\checkmark
$$

$$
y(t) = t\,\operatorname{sen}(2t)
$$

</details>

</details>

## Fracciones simples: el método del profe — [p. 10]

Cómo arma las fracciones simples (F.S.) en todo el OneNote:

- **Coeficientes por "tapado":** para cada factor lineal simple $\frac{A}{s-p}$, el profe
  anota al lado una flecha con el valor que sale de **evaluar en $s=p$ el resto de la
  fracción** (numerador sobre los demás factores), por ejemplo
  $\frac{12}{4} = 3$ y $\frac{8}{-4} = -2$ en el ej. 6a. En el 6a además plantea el sistema
  completo (sumar fracciones e igualar coeficientes) y aclara que "se puede resolver más
  fácil" — es decir, con el tapado.
- **Condición para usar F.S.:** en $\frac{P(x)}{Q(x)}$ hace falta $\operatorname{gr}[P] < \operatorname{gr}[Q]$.
  Si no, primero se **divide**: $P(x) = C(x)\cdot Q(x) + R(x)$, con lo que
  $F(s) = \frac{P(x)}{Q(x)} = C(x) + \frac{R(x)}{Q(x)}$, y las F.S. se hacen sobre $\frac{R}{Q}$.
  La antitransformada de la constante $1$ es $\delta(t)$.
- **Factor repetido** $(s+2)^2(s+1)$: se plantea $\frac{A}{(s+2)^2} + \frac{B}{(s+2)} + \frac{C}{s+1}$;
  $A$ y $C$ salen por tapado, $B$ igualando los coeficientes del numerador (se mira un solo
  grado, el cuadrático).
- **Cuadrático irreducible** ($b^2 - 4ac < 0$): va $\frac{Bs+C}{s^2 - 4s + 13}$; el coeficiente
  del factor lineal sale por tapado y $B$, $C$ igualando coeficientes. Después se completa el
  cuadrado y se parte el numerador para que quede $(s-a)$ arriba: $2s = 2(s-2+2)$.
- **Factor $e^{-as}$ afuera:** se hacen las F.S. de lo que queda y al antitransformar se
  aplica la 2ª propiedad de traslación al revés:

$$
\mathcal{L}^{-1}\left[F(s)\,e^{-as}\right] = f(t-a)
$$

<details>
<summary>📝 Ejercicio 6 — [p. 10]: antitransformadas por fracciones simples</summary>

Calcule las Antitransformadas de Laplace de las siguientes funciones previamente separando en fracciones simples:

a) $F(s) = \dfrac{s+7}{s^2-6s+5}$

b) $F(s) = \dfrac{s^2+2s+2}{s^2+3s+2}$

c) $F(s) = \dfrac{1}{(s+2)^2(s+1)}$

d) $F(s) = \dfrac{s^2+9s+19}{(s+1)(s+2)(s+4)}$

e) $F(s) = \dfrac{2e^{-0.5s}}{s^2+6s+3}$

f) $F(s) = \dfrac{6s^2-13s+12}{s(s-1)(s-6)}$

g) $s^2F(s) - 4F(s) = \dfrac{s}{s+1}$

h) $F(s) = \dfrac{7s^2-41s+84}{(s-1)(s^2-4s+13)}$

i) $F(s) = \dfrac{-2s^2+8s-14}{(s+1)(s^2-2s+5)}$

j) $F(s) = \dfrac{(4s+2)\,e^{-2s}}{(s-1)(s+2)}$

Ítems d, e, f, g, i: *(sin resolución en la fuente)*.

<details>
<summary>Ver resolución (a, b, c, h, j)</summary>

**a)** $F(s) = \dfrac{s+7}{s^2-6s+5}$.

**Paso 1:** se factoriza y se plantean las F.S.; por tapado, $A = \frac{12}{4} = 3$ y $B = \frac{8}{-4} = -2$:

$$
F(s) = \frac{A}{s-5} + \frac{B}{s-1}
$$

**Paso 2:** el profe también lo hace por sistema:

$$
= \frac{A(s-1) + B(s-5)}{(s-5)(s-1)} = \frac{As - A + Bs - 5B}{(s-5)(s-1)} = \frac{s+7}{s^2-6s+5}
$$

$$
\begin{cases} A + B = 1 \;\Rightarrow\; A = 1 - B \\ -A - 5B = 7 \end{cases}
$$

$$
-1 + B - 5B = 7 \quad\Rightarrow\quad -4B = 8 \quad\Rightarrow\quad B = -2,\quad A = 3
$$

("se puede resolver más fácil")

**Paso 3:**

$$
F(s) = \frac{3}{s-5} - \frac{2}{s-1}
$$

$$
f(t) = 3\,e^{5t} - 2\,e^{t}
$$

**b)** $F(s) = \dfrac{s^2+2s+2}{s^2+3s+2}$.

**Paso 1:** "Para usar F.S. en $\frac{P(x)}{Q(x)}$, $\operatorname{gr}[P(x)] < \operatorname{gr}[Q(x)]$". Acá los grados son iguales, así que primero se divide: $P(x) = C(x)\cdot Q(x) + R(x)$,

$$
F(s) = \frac{P(x)}{Q(x)} = C(x) + \frac{R(x)}{Q(x)}
$$

División: $s^2+2s+2$ entre $s^2+3s+2$ → se resta $s^2 + 3s + 2$ → cociente $C(x) = 1$, resto $R(x) = -s$.

$$
F(s) = 1 - \frac{s}{s^2+3s+2}
$$

(Alternativa que anota al margen: sumar y restar $s$ en el numerador, $\frac{s^2+2s+2+s-s}{s^2+3s+2} = 1 - \frac{s}{s^2+3s+2}$.)

**Paso 2:** F.S. sobre el resto; por tapado $A = \frac{2}{-1} = -2$, $B = \frac{1}{1} = 1$:

$$
\frac{-s}{s^2+3s+2} = \frac{A}{s+2} + \frac{B}{s+1}
$$

$$
F(s) = 1 - \frac{2}{s+2} + \frac{1}{s+1}
$$

**Paso 3:**

$$
f(t) = \delta(t) - 2\,e^{-2t} + e^{-t}
$$

**c)** $F(s) = \dfrac{1}{(s+2)^2(s+1)}$.

**Paso 1:** planteo con factor repetido; por tapado $A = \frac{1}{-1} = -1$ y $C = \frac{1}{1} = 1$:

$$
F(s) = \frac{A}{(s+2)^2} + \frac{B}{(s+2)} + \frac{C}{s+1}
$$

**Paso 2:** se suma y se iguala el numerador a $1$:

$$
\frac{-1\,(s+1) + B\,(s+1)(s+2) + 1\,(s+2)^2}{(s+2)^2(s+1)} = \frac{1}{(s+2)^2(s+1)}
$$

$$
\Rightarrow\quad -s - 1 + Bs^2 + 2Bs + Bs + 2B + s^2 + 4s + 4 = 1
$$

Mirando los términos cuadráticos: $B + 1 = 0 \Rightarrow B = -1$.

**Paso 3:**

$$
F(s) = \frac{-1}{(s+2)^2} - \frac{1}{s+2} + \frac{1}{s+1}
$$

$$
f(t) = -t\,e^{-2t} - e^{-2t} + e^{-t}
$$

**h)** $F(s) = \dfrac{7s^2-41s+84}{(s-1)(s^2-4s+13)}$ — el cuadrático tiene $b^2 - 4ac < 0$.

**Paso 1:** planteo; por tapado $A = \frac{50}{10} = 5$:

$$
F(s) = \frac{A}{s-1} + \frac{Bs+C}{s^2-4s+13}
$$

**Paso 2:** se suma e iguala:

$$
= \frac{5\,(s^2-4s+13) + (Bs+C)(s-1)}{(s-1)(s^2-4s+13)}
$$

$$
\Rightarrow\quad 5s^2 - 20s + 65 + Bs^2 - Bs + Cs - C = 7s^2 - 41s + 84
$$

$$
\begin{cases} 5 + B = 7 \\ 65 - C = 84 \end{cases}
\qquad\Rightarrow\qquad B = 2,\quad C = -19
$$

**Paso 3:** se completa el cuadrado y se parte el numerador:

$$
F(s) = \frac{5}{s-1} + \frac{2s}{s^2-4s+13} - \frac{19}{s^2-4s+13}
$$

$$
F(s) = \frac{5}{s-1} + \frac{2\,(s-2+2)}{(s-2)^2+9} - \frac{19}{(s-2)^2+9}
$$

$$
F(s) = \frac{5}{s-1} + \frac{2\,(s-2)}{(s-2)^2+9} - \frac{15}{(s-2)^2+9}
$$

**Paso 4:**

$$
f(t) = 5\,e^{t} + 2\cos(3t)\,e^{2t} - 5\operatorname{sen}(3t)\,e^{2t}
$$

**j)** $F(s) = \dfrac{(4s+2)\,e^{-2s}}{(s-1)(s+2)}$.

**Paso 1:** se saca el $e^{-2s}$ afuera y se hacen F.S. de lo que queda; por tapado $A = \frac{6}{3} = 2$, $B = \frac{-6}{-3} = 2$:

$$
F(s) = e^{-2s}\cdot\left(\frac{A}{s-1} + \frac{B}{s+2}\right) = e^{-2s}\left(\frac{2}{s-1} + \frac{2}{s+2}\right)
$$

**Paso 2:** 2ª prop. de traslación, $\mathcal{L}^{-1}[F(s)\,e^{-as}] = f(t-a)$:

$$
f(t) = 2\,e^{(t-2)} + 2\,e^{-2(t-2)}
$$

</details>

</details>

## Teorema del valor final (TVF) — [p. 14]

$$
\lim_{t\to\infty} f(t) = \lim_{s\to 0} s\,F(s)
$$

Cuando el enunciado pide "verifique", el profe antitransforma $F(s)$ (por F.S.) y toma el
límite directamente sobre $f(t)$.

<details>
<summary>📝 Ejercicio 7 — [p. 14]: TVF y TVI</summary>

a) Aplicando el Teorema de valor Final, halle el valor de $f(t)$ para $t\to\infty$, siendo $F(s) = \dfrac{10}{s^2+s}$. Verifique el resultado obtenido.

b) Dada $F(s) = \dfrac{1}{(s+2)^2}$, halle $f(0)$ por Teorema del valor inicial. Verifique los resultados obtenidos.

c) Dada $F(s) = \dfrac{2s+1}{s^2+2s}$, halle el valor de $f(t)$ para: i) $t=0$ ii) $t=\infty$ iii) $t=0.5$. Verifique i) y ii) con los Teoremas de Valor inicial y final.

Ítems b, c: *(sin resolución en la fuente)*.

<details>
<summary>Ver resolución (a)</summary>

**Paso 1:** T.V.F.:

$$
\lim_{t\to\infty} f(t) = \lim_{s\to 0} s\,F(s) = \lim_{s\to 0}\frac{10s}{s^2+s} = \lim_{s\to 0}\frac{10}{s+1} = 10
$$

**Paso 2 (verificar):** F.S. de $F(s)$; por tapado $A = \frac{10}{-1} = -10$, $B = \frac{10}{1} = 10$:

$$
F(s) = \frac{10}{s^2+s} = \frac{A}{s+1} + \frac{B}{s} = \frac{-10}{s+1} + \frac{10}{s}
$$

$$
\mathcal{L}^{-1}(F(s)) = f(t) = -10\,e^{-t} + 10
$$

$$
\lim_{t\to\infty} f(t) = 10 \quad\checkmark
$$

</details>

</details>

## Parte 3: ecuaciones diferenciales por Laplace — [p. 15]

Se aplica "T. Laplace m.a.m." (miembro a miembro) usando la transformada de la derivada
con las condiciones iniciales:

$$
\mathcal{L}[x''(t)] = s^2 X(s) - s\,x(0) - x'(0)
\qquad
\mathcal{L}[x'(t)] = s\,X(s) - x(0)
$$

Se despeja $X(s)$, se factoriza el denominador (sacando el coeficiente principal, p. ej.
$2s^2+7s+3 = 2\,(s+3)(s+\tfrac{1}{2})$), F.S. por tapado y se antitransforma.

**Condición en un punto que no es $t=0$** (ej. 8i, $y(\pi/2) = -1$, marcado "??"): se deja
$y'(0) = k$ como incógnita, se resuelve todo en función de $k$ y al final se impone la
condición dada sobre $y(t)$ para hallar $k$.

**F.S. con dos cuadráticos irreducibles** $(s^2+4)(s^2+9)$: numeradores $As+B$ y $Cs+D$;
al igualar coeficientes (cúbico, cuadrático, lineal, independiente) quedan "dos sistemas de
2×2 independientes".

<details>
<summary>📝 Ejercicio 8 — [p. 15]: EDO por Laplace</summary>

Resuelva las siguientes Ecuaciones Diferenciales por Transformada de Laplace:

a) $2x''(t) + 7x'(t) + 3x(t) = 6$ con $x(0)=0 \wedge x'(0)=0$

b) $x''(t) + 3x'(t) + 6x(t) = 2$ con $x(0)=0 \wedge x'(0)=0$

c) $3y'(t) + 5y(t) = 6$ con $y(0)=0$

d) $x'(t) + x(t) = e^{-2t}$ con $x(0)=0$

e) $y''(t) + 4y'(t) + 4y(t) = 3x'(t) + 2x(t)$ con $x(t) = e^{-5t} \wedge y(0)=0 \wedge y'(0)=0$

f) $y''(t) + 6y'(t) + 18y(t) = 13e^{-3t}$ con $y(0)=1 \wedge y'(0)=-2$

g) $y''(t) - 2y'(t) + 5y(t) = -8e^{-t}$ con $y(0)=2 \wedge y'(0)=12$

h) $y''(t) - 3y'(t) + 2y(t) = \cos(t)$ con $y(0)=0 \wedge y'(0)=-1$

i) $y''(t) + 9y(t) = \cos(2t)$ con $y(0)=1 \wedge y(\tfrac{\pi}{2}) = -1$

OPTATIVO: $y''(t) + 3y'(t) + 2y(t) = t\,\operatorname{sen}(2t)$ con $y(0)=0 \wedge y'(0)=0$

Ítems b, c, d, e, f, g, h y optativo: *(sin resolución en la fuente)*.

<details>
<summary>Ver resolución (a, i)</summary>

**a)** $2x''(t) + 7x'(t) + 3x(t) = 6$, $x(0)=0 \wedge x'(0)=0$.

**Paso 1:** T. Laplace m.a.m.:

$$
\mathcal{L}\left[2x''(t) + 7x'(t) + 3x(t)\right] = \mathcal{L}(6)
$$

$$
2\left[s^2 X(s) - s\,x(0) - x'(0)\right] + 7\left[s\,X(s) - x(0)\right] + 3X(s) = \frac{6}{s}
$$

(los términos con $x(0)$ y $x'(0)$ son 0).

**Paso 2:** se despeja:

$$
X(s)\,(2s^2 + 7s + 3) = \frac{6}{s}
$$

$$
X(s) = \frac{6}{s\,(2s^2+7s+3)} = \frac{6}{2\cdot s\,(s+3)(s+\tfrac{1}{2})}
$$

**Paso 3:** F.S. (simplificando el 2); por tapado $A = \frac{3}{3/2} = 2$, $B = \frac{3}{15/2} = \frac{2}{5}$, $C = \frac{3}{-5/4} = -\frac{12}{5}$:

$$
\frac{3}{s\,(s+3)(s+\tfrac{1}{2})} = \frac{A}{s} + \frac{B}{s+3} + \frac{C}{s+\tfrac{1}{2}}
$$

$$
X(s) = \frac{2}{s} + \frac{2}{5}\cdot\frac{1}{s+3} - \frac{12}{5}\cdot\frac{1}{s+\tfrac{1}{2}}
$$

**Paso 4:**

$$
\mathcal{L}^{-1}[X(s)] = x(t) = 2 + \frac{2}{5}\,e^{-3t} - \frac{12}{5}\,e^{-\frac{1}{2}t}
$$

**i)** $y''(t) + 9y(t) = \cos(2t)$, $y(0)=1 \wedge y(\pi/2) = -1$ ("??": la segunda condición no es en $t=0$).

**Paso 1:** se transforma dejando $y'(0) = k$:

$$
s^2 Y(s) - s\,y(0) - y'(0) + 9\,Y(s) = \frac{s}{s^2+4}
$$

con $y(0) = 1$, $y'(0) = k$:

$$
Y(s)\,(s^2+9) = \frac{s}{s^2+4} + s + k
$$

$$
Y(s) = \frac{s}{(s^2+4)(s^2+9)} + \frac{s}{s^2+9} + \frac{k}{s^2+9}
$$

(el primer término va a F.S.; los otros dos están "listos p/ antitransformar").

**Paso 2:** F.S.:

$$
\frac{s}{(s^2+4)(s^2+9)} = \frac{As+B}{s^2+4} + \frac{Cs+D}{s^2+9}
$$

$$
= \frac{(As+B)(s^2+9) + (Cs+D)(s^2+4)}{(s^2+4)(s^2+9)} = \frac{As^3 + 9As + Bs^2 + 9B + Cs^3 + 4Cs + Ds^2 + 4D}{(s^2+4)(s^2+9)} = \frac{s}{(s^2+4)(s^2+9)}
$$

$$
\begin{cases}
\text{cúbico:} & A + C = 0 \\
\text{cuadrático:} & B + D = 0 \\
\text{lineal:} & 9A + 4C = 1 \\
\text{indepte.:} & 9B + 4D = 0
\end{cases}
\qquad \text{(dos sistemas de 2×2 independientes)}
$$

$$
B = 0,\quad D = 0,\quad A = -C,\quad -9C + 4C = 1 \;\Rightarrow\; C = -\tfrac{1}{5},\quad A = \tfrac{1}{5}
$$

**Paso 3:** se reagrupa (los dos términos en $\frac{s}{s^2+9}$ suman $\frac{4}{5}\cdot\frac{s}{s^2+9}$):

$$
Y(s) = \frac{1}{5}\cdot\frac{s}{s^2+4} - \frac{1}{5}\cdot\frac{s}{s^2+9} + \frac{s}{s^2+9} + \frac{k}{s^2+9}
$$

$$
y(t) = \frac{1}{5}\cos(2t) + \frac{4}{5}\cos(3t) + \frac{k}{3}\operatorname{sen}(3t)
$$

**Paso 4:** se impone $y(\pi/2) = -1$:

$$
-\frac{1}{5} - \frac{k}{3} = -1 \qquad\Rightarrow\qquad k = \frac{12}{5}
$$

$$
y(t) = \frac{1}{5}\cos(2t) + \frac{4}{5}\cos(3t) + \frac{4}{5}\operatorname{sen}(3t)
$$

</details>

</details>

## Sistemas de ecuaciones diferenciales — [p. 18]

Se transforman las dos ecuaciones (cada derivada con su condición inicial), queda un
sistema algebraico en $X(s)$ e $Y(s)$: se despeja una de la ecuación más cómoda, se
sustituye en la otra, se antitransforma por F.S. y después se vuelve a la despejada para
obtener la segunda función.

<details>
<summary>📝 Ejercicio 9 — [p. 18]: sistemas de EDO</summary>

Resuelva los siguientes sistemas de Ecuaciones Diferenciales por medio de la Transformada de Laplace:

a) $\begin{cases} y'(t) - \tfrac{1}{2}x(t) = 1 \\ x'(t) + 2y(t) = 2t \end{cases}$ con $x(0)=0,\ y(0)=0$

b) $\begin{cases} x'(t) = x(t) - y(t) \\ y'(t) = 2x(t) + 4y(t) \end{cases}$ con $x(0)=-1,\ y(0)=0$

c) $\begin{cases} x'(t) + 2y(t) = 0 \\ x'(t) - y'(t) = 0 \end{cases}$ con $x(0)=-1,\ y(0)=2$

d) $\begin{cases} x'(t) + 2y'(t) + 5x(t) = 0 \\ y'(t) + y(t) + 2x(t) = 0 \end{cases}$ ; $y(0)=1 \wedge x(0)=0$

e) $\begin{cases} 2x'(t) - y'(t) = 4t - 3 \\ x'(t) = y(t) - t \end{cases}$ ; $y(0)=2 \wedge x(0)=1$

OPTATIVO: $\begin{cases} y'(t) + 2z'(t) = t \\ y'(t) - z(t) = e^t \end{cases}$ con $y(0)=3,\ y'(0)=-2,\ z(0)=0$

Ítems a, c, d, e y optativo: *(sin resolución en la fuente)*.

<details>
<summary>Ver resolución (b)</summary>

**b)** $x'(t) = x(t) - y(t)$ ; $y'(t) = 2x(t) + 4y(t)$ ; $x(0) = -1 \wedge y(0) = 0$.

**Paso 1:** Laplace en las dos ecuaciones:

$$
\begin{cases}
s\,X(s) - x(0) = X(s) - Y(s) & \text{①} \quad (x(0) = -1) \\
s\,Y(s) - y(0) = 2X(s) + 4Y(s) & \text{②} \quad (y(0) = 0)
\end{cases}
$$

**Paso 2:** en ② se despeja $X$:

$$
X(s) = \frac{s\,Y(s) - 4Y(s)}{2} = \frac{1}{2}\,Y(s)\,(s-4)
$$

**Paso 3:** en ①:

$$
s\cdot\frac{1}{2}\,Y(s)(s-4) + 1 = \frac{1}{2}\,Y(s)(s-4) - Y(s)
$$

$$
Y(s)\left[\frac{1}{2}s(s-4) - \frac{1}{2}(s-4) + 1\right] = -1
$$

$$
Y(s)\left[\frac{1}{2}s^2 - 2s - \frac{1}{2}s + 2 + 1\right] = -1
$$

$$
Y(s)\left[\frac{1}{2}s^2 - \frac{5}{2}s + 3\right] = -1
$$

$$
Y(s) = \frac{-2}{(s^2 - 5s + 6)}
$$

**Paso 4:** F.S.; por tapado $A = \frac{-2}{1} = -2$, $B = \frac{-2}{-1} = 2$:

$$
Y(s) = \frac{A}{s-3} + \frac{B}{s-2} = \frac{-2}{s-3} + \frac{2}{s-2}
$$

$$
y(t) = -2\,e^{3t} + 2\,e^{2t}
$$

**Paso 5:** se vuelve a $X(s) = \frac{1}{2}(s-4)\,Y(s)$:

$$
X(s) = \frac{-s+4}{s-3} + \frac{s-4}{s-2} = \frac{-s^2 + 2s + 4s - 8 + s^2 - 3s - 4s + 12}{(s-3)(s-2)}
$$

$$
X(s) = \frac{-s+4}{(s-3)(s-2)} = \frac{A}{s-3} + \frac{B}{s-2}
$$

por tapado $A = \frac{1}{1} = 1$, $B = \frac{2}{-1} = -2$:

$$
X(s) = \frac{1}{s-3} - \frac{2}{s-2}
$$

$$
x(t) = e^{3t} - 2\,e^{2t}
$$

</details>

</details>

## Parte 4: teorema de convolución — [p. 19]

$$
\mathcal{L}\left[\int_0^t f(u)\,g(t-u)\,du\right] = F(s)\cdot G(s)
$$

$$
\mathcal{L}^{-1}\left[F(s)\cdot G(s)\right] = \int_0^t f(u)\,g(t-u)\,du
$$

Recetas del profe:

- En la integral, identificar quién es $f(u)$ (lo que depende solo de $u$) y quién es
  $g(t-u)$; a $g(t-u) = e^{(t-u)}$ hay que "pensarlo como $e^t$" para transformarlo.
- Al antitransformar un producto, **elegir qué factor lleva el $(t-u)$**: "más fácil que el
  $(t-u)$ sea para la exponencial", porque $e^{-(t-u)} = e^{-t}\,e^{u}$ y el $e^{-t}$ sale de
  la integral.
- Productos de senos/cosenos adentro de la integral se abren con identidades
  trigonométricas (seno por seno → diferencia de cosenos; coseno por coseno → suma de
  cosenos) y recién después se integra en $u$.

<details>
<summary>📝 Ejercicio 10 — [p. 19]: transformar una integral de convolución</summary>

Halle $\mathcal{L}\left[\displaystyle\int_0^t u\cos(u)\,e^{(t-u)}\,du\right]$ utilizando el Teorema de Convolución.

<details>
<summary>Ver resolución</summary>

**Paso 1:** T. de Convolución:

$$
\mathcal{L}\left[\int_0^t f(u)\,g(t-u)\,du\right] = F(s)\cdot G(s)
\qquad
\mathcal{L}^{-1}\left[F(s)\cdot G(s)\right] = \int_0^t f(u)\,g(t-u)\,du
$$

Se identifica $f(u) = u\cos(u)$ y $g(t-u) = e^{(t-u)}$:

$$
\mathcal{L}\left[\int_0^t u\cos(u)\,e^{(t-u)}\,du\right] = F(s)\cdot G(s)
$$

**Paso 2:** $F(s)$ por multiplicación por $t^n$:

$$
\mathcal{L}[\cos(u)] = \frac{s}{s^2+1}
$$

Derivo:

$$
\frac{s^2 + 1 - 2s^2}{(s^2+1)^2}
$$

Cambio de signo:

$$
F(s) = \frac{s^2-1}{(s^2+1)^2}
$$

**Paso 3:** $g(t-u) = e^{(t-u)}$ (pensarlo como $e^t$):

$$
G(s) = \frac{1}{s-1}
$$

**Paso 4:**

$$
F(s)\cdot G(s) = \frac{s^2-1}{(s^2+1)^2}\cdot\frac{1}{s-1} = \frac{s+1}{(s^2+1)^2}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 11 — [p. 20]: antitransformar por convolución</summary>

Antitransforme utilizando Convolución:

a) $Y(s) = \dfrac{6}{(s+1)(s^2+4)}$

b) $Y(s) = \dfrac{1}{(s^2+1)^2}$

c) $Y(s) = \dfrac{s^2}{(s^2+1)^2}$

<details>
<summary>Ver resolución</summary>

**a)** $Y(s) = \dfrac{6}{(s+1)(s^2+4)}$.

**Paso 1:** se separa en dos factores conocidos:

$$
F(s) = \frac{6}{s+1} \;\Rightarrow\; f(t) = 6\,e^{-t}
\qquad
G(s) = \frac{1}{s^2+4} \;\Rightarrow\; g(t) = \frac{1}{2}\operatorname{sen}(2t)
$$

**Paso 2:** "Más fácil que el $(t-u)$ sea para la exponencial":

$$
y(t) = 3\int_0^t e^{-(t-u)}\,\operatorname{sen}(2u)\,du
$$

$$
y(t) = 3\,e^{-t}\int_0^t e^{u}\,\operatorname{sen}(2u)\,du
$$

**Paso 3:** se integra (primitiva de tabla):

$$
y(t) = 3\,e^{-t}\left[\frac{1}{5}\,e^{u}\left(\operatorname{sen}(2u) - 2\cos(2u)\right)\right]_0^t
$$

$$
y(t) = 3\,e^{-t}\left[\frac{1}{5}\,e^{t}\left(\operatorname{sen}(2t) - 2\cos(2t)\right) - \frac{1}{5}\cdot(-2)\right]
$$

$$
y(t) = \frac{3}{5}\operatorname{sen}(2t) - \frac{6}{5}\cos(2t) + \frac{6}{5}\,e^{-t}
$$

**b)** $Y(s) = \dfrac{1}{(s^2+1)^2}$.

**Paso 1:**

$$
F(s) = G(s) = \frac{1}{s^2+1} \qquad f(t) = g(t) = \operatorname{sen}t
$$

$$
y(t) = \int_0^t \operatorname{sen}(u)\,\operatorname{sen}(t-u)\,du
$$

**Paso 2:** identidad trigonométrica:

$$
y(t) = -\frac{1}{2}\int_0^t \left[\cos(t) - \cos(2u-t)\right]du
$$

$$
y(t) = -\frac{1}{2}\,t\cos(t) + \frac{1}{2}\left[\frac{\operatorname{sen}(2u-t)}{2}\right]_0^t
$$

$$
y(t) = -\frac{1}{2}\,t\cos(t) + \frac{1}{4}\left(\operatorname{sen}t - \operatorname{sen}(-t)\right)
$$

(el paréntesis es $2\operatorname{sen}(t)$)

$$
y(t) = -\frac{1}{2}\,t\cos(t) + \frac{1}{2}\operatorname{sen}t
$$

**c)** $Y(s) = \dfrac{s^2}{(s^2+1)^2}$.

**Paso 1:**

$$
F(s) = \frac{s}{s^2+1} \qquad G(s) = \frac{s}{s^2+1} \qquad f(t) = g(t) = \cos(t)
$$

$$
y(t) = \int_0^t \cos(u)\cos(t-u)\,du
$$

**Paso 2:** identidad trigonométrica e integración:

$$
y(t) = \frac{1}{2}\int_0^t \left[\cos t + \cos(2u-t)\right]du
$$

$$
y(t) = \frac{1}{2}\,t\cos t + \frac{1}{2}\operatorname{sen}t
$$

</details>

</details>

## Ecuaciones integrales e integro-diferenciales — [p. 22]

La integral $\int_0^t (\cdot)\,y(u)\,du$ es una convolución: al transformar queda el **producto**
de $Y(s)$ por la transformada del núcleo (p. ej. $(t-u)^2 \to \frac{2}{s^3}$, $(t-u) \to \frac{1}{s^2}$).
Si además hay $y'(t)$, se usa $s\,Y(s) - y(0)$. Se despeja $Y(s)$ y se antitransforma por F.S.

**Factorizar denominadores cúbicos con Ruffini:** $s^3 + 8 = (s+2)(s^2-2s+4)$ (raíz $-2$),
$s^3 + 1 = (s+1)(s^2-s+1)$ (raíz $-1$). Después de factorizar, conviene probar si el
numerador es divisible por el factor cuadrático ("Además:" en el 12e), porque la fracción
se simplifica mucho.

<details>
<summary>📝 Ejercicio 12 — [p. 22]: ecuaciones integrales e integro-diferenciales</summary>

Resuelva las siguientes ecuaciones integrales e integrodiferenciales por medio de la Transformada de Laplace, utilizando el Teorema de Convolución:

a) $y(t) + 4\displaystyle\int_0^t (t-u)^2\,y(u)\,du = t^2$

b) $y(t) = t + 2\displaystyle\int_0^t \cos(t-u)\,y(u)\,du$

c) $\displaystyle\int_0^t y(u)\,(t-u)\,du = \frac{t}{2} - \frac{\operatorname{sen}(2t)}{4}$

d) $y(t) = \displaystyle\int_0^t y(u)\,du + \cos(t)$

e) $\displaystyle\int_0^t y(u)\,(t-u)\,du + y'(t) = \frac{t^4}{12} + t + 1$ con $y(0) = -1$

f) $y'(t) = 1 - \displaystyle\int_0^t y(u)\,e^{2(t-u)}\,du$ con $y(0) = 1$

Ítems b, c, d, f: *(sin resolución en la fuente)*.

<details>
<summary>Ver resolución (a, e)</summary>

**a)** $y(t) + 4\displaystyle\int_0^t (t-u)^2\,y(u)\,du = t^2$.

**Paso 1:** se transforma; la integral es convolución de $t^2$ con $y$:

$$
Y(s) + 4\cdot\frac{2}{s^3}\cdot Y(s) = \frac{2}{s^3}
$$

$$
Y(s)\left(1 + \frac{8}{s^3}\right) = \frac{2}{s^3}
$$

$$
Y(s)\left(\frac{s^3+8}{s^3}\right) = \frac{2}{s^3}
$$

$$
Y(s) = \frac{2}{s^3+8}
$$

**Paso 2:** F.S. Ruffini sobre $s^3+8$ con raíz $-2$ (coeficientes $1\ 0\ 0\ 8$ → $1\ -2\ 4\ |\ 0$): $s^3+8 = (s+2)(s^2-2s+4)$. Por tapado $A = \frac{2}{12} = \frac{1}{6}$:

$$
\frac{2}{s^3+8} = \frac{A}{s+2} + \frac{Bs+C}{s^2-2s+4}
$$

$$
\frac{1}{6}\,(s^2-2s+4) + (Bs+C)(s+2) = 2
$$

$$
\frac{1}{6}s^2 - \frac{1}{3}s + \frac{2}{3} + Bs^2 + 2Bs + Cs + 2C = 2
$$

$$
\begin{cases} \frac{1}{6} + B = 0 \;\Rightarrow\; B = -\frac{1}{6} \\ \frac{2}{3} + 2C = 2 \;\Rightarrow\; C = \frac{2}{3} \end{cases}
$$

**Paso 3:** se completa el cuadrado $s^2-2s+4 = (s-1)^2+3$ y se parte el numerador:

$$
Y(s) = \frac{(1/6)}{s+2} - \frac{(1/6)\,s}{(s-1)^2+3} + \frac{2/3}{(s-1)^2+3}
$$

$$
Y(s) = \frac{(1/6)}{s+2} - \frac{(1/6)(s-1)}{(s-1)^2+3} + \frac{(2/3) - (1/6)}{(s-1)^2+3}
$$

$$
Y(s) = \frac{1}{6}\cdot\frac{1}{s+2} - \frac{1}{6}\cdot\frac{(s-1)}{(s-1)^2+3} + \frac{1}{2}\cdot\frac{1}{(s-1)^2+3}\cdot\frac{\sqrt{3}}{\sqrt{3}}
$$

**Paso 4:**

$$
y(t) = \frac{1}{6}\,e^{-2t} - \frac{1}{6}\cos(\sqrt{3}\,t)\,e^{t} + \frac{1}{2\sqrt{3}}\operatorname{sen}(\sqrt{3}\,t)\,e^{t}
$$

**e)** $\displaystyle\int_0^t y(u)\,(t-u)\,du + y'(t) = \frac{t^4}{12} + t + 1$, $y(0) = -1$.

**Paso 1:** se transforma (convolución con $t \to \frac{1}{s^2}$; derivada con $y(0) = -1$):

$$
Y(s)\cdot\frac{1}{s^2} + s\,Y(s) - y(0) = \frac{2}{s^5} + \frac{1}{s^2} + \frac{1}{s}
$$

$$
Y(s)\left(\frac{1}{s^2} + s\right) = \frac{2 + s^3 + s^4 - s^5}{s^5}
$$

$$
Y(s)\left(\frac{s^3+1}{s^2}\right) = \frac{2 + s^3 + s^4 - s^5}{s^5}
$$

$$
Y(s) = \frac{2 + s^3 + s^4 - s^5}{s^3\,(s^3+1)}
$$

**Paso 2:** "¡Factorearlo!" Ruffini sobre $s^3+1$ con raíz $-1$ (coeficientes $1\ 0\ 0\ 1$ → $1\ -1\ 1\ |\ 0$):

$$
Y(s) = \frac{2 + s^3 + s^4 - s^5}{s^3\,(s+1)(s^2-s+1)}
$$

**Paso 3:** "Además": se divide el numerador $-s^5 + s^4 + s^3 + 0s^2 + 0s + 2$ por $s^2 - s + 1$ (resto $0$):

$$
\begin{array}{r}
-s^5 + s^4 + s^3 + 0s^2 + 0s + 2 \;\big|\; s^2 - s + 1 \\
+s^5 - s^4 + s^3 \qquad\qquad\qquad \;\; -s^3 + 2s + 2 \\
\hline
2s^3 + 2 \\
-2s^3 + 2s^2 - 2s \\
\hline
2s^2 - 2s + 2 \\
-2s^2 + 2s - 2 \\
\hline
0
\end{array}
$$

$$
Y(s) = \frac{-s^3 + 2s + 2}{s^3\,(s+1)}
$$

**Paso 4:** F.S.; por tapado $A = \frac{2}{1} = 2$ y $D = \frac{1}{-1} = -1$:

$$
\frac{-s^3+2s+2}{s^3\,(s+1)} = \frac{A}{s^3} + \frac{B}{s^2} + \frac{C}{s} + \frac{D}{s+1}
$$

$$
2s + 2 + Bs^2 + Bs + Cs^3 + Cs^2 - 1\cdot s^3 = -s^3 + 2s + 2
$$

$$
\begin{cases} \text{cúbicos:} & C - 1 = -1 \;\Rightarrow\; C = 0 \\ \text{cuadráticos:} & B + C = 0 \;\Rightarrow\; B = 0 \end{cases}
$$

$$
Y(s) = \frac{2}{s^3} - \frac{1}{s+1}
$$

**Paso 5:**

$$
y(t) = t^2 - e^{-t}
$$

</details>

</details>

## Parte 5: evaluación de integrales impropias — [p. 25]

**Con la definición:** la integral $\int_0^\infty f(t)\,e^{-st}\,dt$ *es* $F(s)$; si el integrando tiene
la forma $f(t)\,e^{-kt}$, la integral vale $F(k)$ (se transforma $f$ por tabla y se evalúa en
$s = k$). Si no hay exponencial, es $e^{-0\cdot t}$ y la integral vale $F(0)$.

$$
\mathcal{L}[f(t)] = F(s) = \int_0^\infty f(t)\,e^{-st}\,dt
$$

**División por $t$:**

$$
\mathcal{L}\left[\frac{f(t)}{t}\right] = \int_s^\infty F(u)\,du
$$

Regla del profe: **solo se puede dividir por $t$ si existe $\displaystyle\lim_{t\to 0}\frac{f(t)}{t}$**
(se verifica, por ejemplo con L'Hôpital). Por eso en el 13d **no** se puede separar
$\int \frac{e^{-3t}}{t} - \int \frac{e^{-6t}}{t}$ (no existe $\lim_{t\to 0}\frac{1}{t}$): hay que sacar
factor común $e^{-3t}$ y transformar $\frac{1 - e^{-3t}}{t}$, cuyo límite sí existe. Cuando la
integral de $F(u)$ da $\infty - \infty$ (indeterminado), se juntan los logaritmos en uno solo
antes de tomar el límite.

<details>
<summary>📝 Ejercicio 13 — [p. 25]: integrales impropias por Laplace</summary>

Calcule el valor de las siguientes integrales utilizando Transformada de Laplace:

a) $\displaystyle\int_0^\infty t^3\,e^{-t}\operatorname{sen}(t)\,dt$

b) $\displaystyle\int_0^\infty e^{-3t}\,t\,\operatorname{sen}(t)\,dt$

c) $\displaystyle\int_0^\infty t^2\,e^{-2t}\,dt$

d) $\displaystyle\int_0^\infty \frac{e^{-3t} - e^{-6t}}{t}\,dt$

e) $\displaystyle\int_0^\infty t\,e^{-2t}\cos(4t)\,dt$

Ítems a, b, e: *(sin resolución en la fuente)*.

<details>
<summary>Ver resolución (c, d)</summary>

**c)** $\displaystyle\int_0^\infty t^2\,e^{-2t}\,dt$.

**Paso 1:** Def. Transf. Laplace:

$$
\mathcal{L}[f(t)] = F(s) = \int_0^\infty f(t)\,e^{-st}\,dt
$$

Con $f(t) = t^2$ y $s = 2$:

$$
\int_0^\infty t^2\,e^{-2t}\,dt = F(2)
$$

**Paso 2:**

$$
F(s) = \mathcal{L}(t^2) = \frac{2}{s^3}
$$

$$
F(2) = \frac{1}{4}
$$

**d)** $\displaystyle\int_0^\infty \frac{e^{-3t} - e^{-6t}}{t}\,dt$.

**Paso 1:** no se puede separar en $\int_0^\infty \frac{e^{-3t}}{t}dt - \int_0^\infty \frac{e^{-6t}}{t}dt$ porque $\nexists \lim_{t\to 0}\frac{1}{t}$. Se saca factor común:

$$
= \int_0^\infty e^{-3t}\left(\frac{1 - e^{-3t}}{t}\right)dt = \mathcal{L}\left(\frac{1 - e^{-3t}}{t}\right)\Bigg|_{[3]}
$$

"Se puede hacer porque existe el límite":

$$
\lim_{t\to 0}\frac{1 - e^{-3t}}{t} = \lim_{t\to 0}\frac{3e^{-3t}}{1} = 3
$$

**Paso 2:** Div. × $t$:

$$
\mathcal{L}\left(\frac{1 - e^{-3t}}{t}\right) = \int_s^\infty \left(\frac{1}{u} - \frac{1}{u+3}\right)du
$$

$$
= \Big[\ln|u| - \ln|u+3|\Big]_s^\infty \qquad (\infty - \infty,\ \text{Ind})
$$

$$
= \ln\left|\frac{u}{u+3}\right|\,\Bigg|_s^\infty
$$

(cuando $u\to\infty$ el cociente $\to 1$ y el logaritmo $\to 0$)

$$
= 0 - \ln\left|\frac{s}{s+3}\right| = \ln\left|\frac{s+3}{s}\right|
$$

**Paso 3:** se evalúa en $s = 3$:

$$
\Rightarrow\quad \mathcal{L}[f(t)]_{(3)} = \ln\frac{6}{3} = \ln 2
$$

</details>

</details>

<details>
<summary>📝 Ejercicio extra — [p. 25]: retomando ej. de clase pasada, ∫₀^∞ sen(t)/t dt</summary>

Calcular

$$
\int_0^\infty \frac{\operatorname{sen}(t)}{t}\,dt
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Reescribimos con la exponencial $e^{-0\cdot t}$, de modo que la integral es $F(0)$:

$$
\int_0^\infty \frac{\operatorname{sen}t}{t}\cdot e^{-0\cdot t}\,dt = F(0)
$$

**Paso 2:** Div. × $t$:

$$
\mathcal{L}\left(\frac{\operatorname{sen}t}{t}\right) = \int_s^\infty \frac{1}{u^2+1}\,du
$$

$$
= \operatorname{arctg}(u)\,\Big|_s^\infty = \frac{\pi}{2} - \operatorname{arctg}(s) = F(s)
$$

**Paso 3:**

$$
F(0) = \frac{\pi}{2} - \operatorname{arctg}(0)
$$

$$
F(0) = \int_0^\infty \frac{\operatorname{sen}t}{t}\,dt = \frac{\pi}{2}
$$

</details>

</details>

---

*Generado el 2026-10-02 a partir de `fuentes/clases/Transformadas de Laplace/Transformada de Laplace.pdf` (OneNote de la práctica, 27 págs.: guía tipeada + resolución manuscrita del profesor).*
