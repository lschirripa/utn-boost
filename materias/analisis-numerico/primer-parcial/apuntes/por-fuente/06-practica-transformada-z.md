# Práctica de Transformada Z: definición, ROC, antitransformadas y ecuaciones en diferencias

> Fuente: fuentes/clases/Transformada Z/Transformada Z.pdf, págs. 1–6

---

## Índice

- [p. 1] — Definición, series que hay que recordar y receta para sucesiones definidas por paridad
- [p. 1] — 📝 Ejercicio 1 a), b), d), e): transformadas por definición (sin resolver)
- [p. 1] — 📝 Ejercicio 1c: $x(n) = 4^n$ si $n$ par, $3^{-n}$ si $n$ impar, con región de convergencia
- [p. 1] — 📝 Ejercicio adicional: $x(n) = 4^n$ si $n$ múltiplo de 3, $3^{-n}$ si no
- [p. 2] — Series de $e^x$ y de $\ln(1+x)$ como transformadas
- [p. 2] — 📝 Ejercicio 1g (optativo): $x(n) = 2^n/n!$
- [p. 2] — 📝 Ejercicio 1f (optativo): $x(n) = 1/(n+1)$
- [p. 2] — Secuencias finitas
- [p. 2] — 📝 Ejercicio 2: transformada de una secuencia finita dada por su gráfico
- [p. 2] — Transformada por tabla y propiedades: desplazamiento
- [p. 2] — 📝 Ejercicio 3 a), c): por tabla y propiedades (sin resolver)
- [p. 2] — 📝 Ejercicio 3b: $x(n) = u(n-2)$
- [p. 2] — Antitransformada: fracciones simples con la $z$ afuera, y series conocidas
- [p. 2] — 📝 Ejercicio 5 b), c), e), g), h), i): antitransformadas (sin resolver)
- [p. 3] — 📝 Ejercicio 5a: $X(z) = \dfrac{3z(z-3)}{z^2-5z+4}$
- [p. 3] — 📝 Ejercicio 5d: $X(z) = \operatorname{senh}(2/z)$
- [p. 3] — 📝 Ejercicio 5f: $X(z) = \left(\dfrac{1}{z-1}\right)^2$
- [p. 3] — Ecuaciones en diferencias de orden 1: propiedad de $x(n+1)$
- [p. 3] — 📝 Ejercicio 6 a), b), c), d): orden 1 (sin resolver)
- [p. 3] — 📝 Ejercicio 6e: $a_{n+1} - 4a_n = 4(1-n)2^n$, $a_0 = 3$
- [p. 3] — Ecuaciones en diferencias de orden 2: propiedad de $x(n+2)$ y análisis del denominador
- [p. 3] — 📝 Ejercicio 7 a), b), c), d), e): orden 2 (sin resolver)
- [p. 4] — 📝 Ejercicio 7f: serie de Fibonacci $a_{n+2} = a_{n+1} + a_n$
- [p. 4] — 📝 Ejercicio 7g: $a_{n+2} - a_n = \operatorname{sen}(n\pi/2)$
- [p. 4] — 📝 Ejercicio 8 a), c): orden 2, escribir $X(z)$ y $x(n)$ (sin resolver)
- [p. 5] — 📝 Ejercicio 8b: $x(n+2) - 4x(n+1) + 4x(n) = 4^{n+1}$
- [p. 5] — Propiedades de la transformada Z: verdadero o falso
- [p. 5] — 📝 Ítem de opción múltiple: $\mathcal{Z}[a_n \cdot b_n]$, $\mathcal{Z}[a_n^2]$, linealidad, $\mathcal{Z}[a_{n+1}]$
- [p. 5] — La región de convergencia sale sin resolver la transformada
- [p. 5] — 📝 Ejercicio 4c (V/F): ROC de $x(n) = 3$ si $n$ múltiplo de 5, $(-2)^n$ si no, ¿es $|z| > 2$?

---

## Definición, series que hay que recordar y receta para sucesiones definidas por paridad — [p. 1]

La transformada Z de una sucesión $x(n)$ definida para $n \ge 0$ es, por definición,

$$
X(z) = \mathcal{Z}\{x(n)\} = \sum_{n=0}^{\infty} x(n)\, z^{-n}
$$

**Recuerde** (recuadro de la guía):

$$
\sum_{n=0}^{\infty} k\, r^n = \frac{k}{1-r} \quad \text{con } 0 < r < 1 \qquad ; \qquad e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!}
$$

$$
\ln(1+x) = x - \frac{x^2}{2} + \frac{x^3}{3} + \dots + (-1)^{n+1}\frac{x^n}{n} \quad \text{con } x \in (-1\,;\,1]
$$

**Receta del profe para sucesiones definidas por paridad (o por "múltiplo de")** — es lo que hace en 1c, en el ejercicio adicional y en 4c:

1. Escribir los primeros términos de la definición $\sum x(n) z^{-n}$ para ver el patrón: $4^0 z^0 + 3^{-1} z^{-1} + 4^2 z^{-2} + 3^{-3} z^{-3} + \dots$
2. **Separar en una serie por cada "clase" de $n$**: los pares se escriben $n = 2k$ y los impares $n = 2k+1$ (si es "múltiplo de 3", son tres series: $n = 3k$, $3k+1$, $3k+2$; si es "múltiplo de 5", cinco series). Cada una queda como $\sum_{k=0}^{\infty} (\cdot)^k$ por una constante que sale afuera (por ejemplo $3^{-(2k+1)} z^{-(2k+1)} = 3^{-2k} \cdot 3^{-1} \cdot z^{-2k} \cdot z^{-1}$, y el $\tfrac{1}{3z}$ sale fuera de la sumatoria).
3. Cada serie geométrica se suma con $\dfrac{1}{1-r}$ y después se simplifica multiplicando numerador y denominador por la potencia de $z$ que corresponda.
4. **Región de convergencia:** cada serie geométrica pide $|r| < 1$ para su razón $r$; se despeja $|z|$ en cada una y la ROC total es la **intersección** de todas (gana la condición más restrictiva).

<details>
<summary>📝 Ejercicio 1 a), b), d), e) — [p. 1]: transformadas por definición (sin resolver)</summary>

**Ejercicio n° 1.** Halle, por definición, la transformada Z de las siguientes sucesiones definidas para $n \ge 0$ e indique en cada caso la región de convergencia correspondiente:

a) $x(n) = \left(\dfrac{1}{3}\right)^n$

b) $x(n) = \begin{cases} 1 & \text{si } n \text{ es par} \\ 0 & \text{si } n \text{ es impar} \end{cases}$

d) $x(n) = \begin{cases} 5 & \text{si } n \text{ es impar} \\ 3\,(2)^{-n} & \text{si } n \text{ es par} \end{cases}$

e) $x(n) = \begin{cases} 2 & \text{si } n = 1 \\ n & \text{si } 1 < n < 4 \\ 0 & \text{en otro caso} \end{cases}$

*(sin resolución en la fuente)*

</details>

<details>
<summary>📝 Ejercicio 1c — [p. 1]: x(n) = 4ⁿ si n es par, 3⁻ⁿ si n es impar, con región de convergencia</summary>

**Ejercicio n° 1 c).** Halle, por definición, la transformada Z de la siguiente sucesión definida para $n \ge 0$ e indique la región de convergencia correspondiente:

$$
x(n) = \begin{cases} 4^n & \text{si } n \text{ es par} \\ 3^{-n} & \text{si } n \text{ es impar} \end{cases}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Aplicar la definición y escribir los primeros términos para ver el patrón.

$$
X(z) = \mathcal{Z}\{x(n)\} = \sum_{n=0}^{\infty} x(n)\, z^{-n} = 4^0 z^{0} + 3^{-1} z^{-1} + 4^2 z^{-2} + 3^{-3} z^{-3} + \dots
$$

**Paso 2:** Separar en dos series: los pares con $n = 2k$ y los impares con $n = 2k+1$, y sacar fuera las constantes.

$$
X(z) = \sum_{k=0}^{\infty} 4^{2k} z^{-2k} + \sum_{k=0}^{\infty} 3^{-(2k+1)} z^{-(2k+1)} = \sum_{k=0}^{\infty} \left(4^2\right)^k \left(\frac{1}{z}\right)^{2k} + \sum_{k=0}^{\infty} 3^{-2k} \cdot 3^{-1} \cdot z^{-2k} \cdot z^{-1}
$$

$$
X(z) = \sum_{k=0}^{\infty} \left(\frac{16}{z^2}\right)^k + \frac{1}{3z} \sum_{k=0}^{\infty} \left(\frac{1}{9z^2}\right)^k
$$

**Paso 3:** Sumar cada geométrica con $\frac{1}{1-r}$ (el profe encierra en círculo cada uno de los dos factores $\frac{1}{1-r}$: de ahí sale la región de convergencia) y simplificar.

$$
X(z) = \frac{1}{1 - \dfrac{16}{z^2}} + \frac{1}{3z} \cdot \frac{1}{1 - \dfrac{1}{9z^2}} = \frac{z^2}{z^2 - 16} + \frac{1}{3z} \cdot \frac{9z^2}{9z^2 - 1}
$$

Simplificando $\dfrac{9z^2}{3z} = 3z$:

$$
X(z) = \frac{z^2}{z^2 - 16} + \frac{3z}{9z^2 - 1}
$$

**Paso 4:** Región de convergencia: cada razón tiene que tener módulo menor que 1.

$$
\left| \frac{16}{z^2} \right| < 1 \;\Rightarrow\; \left| \frac{z^2}{16} \right| > 1 \;\Rightarrow\; |z^2| > 16 \;\Rightarrow\; \boxed{|z| > 4}
$$

$$
\left| \frac{1}{9z^2} \right| < 1 \;\Rightarrow\; |9z^2| > 1 \;\Rightarrow\; |z| > \frac{1}{3}
$$

El profe dibuja el plano complejo con la circunferencia de radio 4 y marca: **parte exterior de la circunferencia de radio 4** (la condición $|z| > 4$ ya contiene a $|z| > \tfrac{1}{3}$).

</details>

</details>

<details>
<summary>📝 Ejercicio adicional — [p. 1]: x(n) = 4ⁿ si n es múltiplo de 3, 3⁻ⁿ si no lo es</summary>

**Ejercicio adicional.** Hallar la transformada Z y la región de convergencia de

$$
x(n) = \begin{cases} 4^n & n \text{ múltiplo de } 3 \\ 3^{-n} & n \text{ no es múltiplo de } 3 \end{cases}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Definición y primeros términos (el profe marca con colores los términos de cada clase: $n = 0, 3, 6, \dots$ con $4^n$; $n = 1, 4, \dots$ y $n = 2, 5, \dots$ con $3^{-n}$).

$$
X(z) = \sum_{n=0}^{\infty} x(n)\, z^{-n} = 4^0 z^{0} + 3^{-1} z^{-1} + 3^{-2} z^{-2} + 4^3 z^{-3} + 3^{-4} z^{-4} + 3^{-5} z^{-5} + 4^6 z^{-6} + \dots
$$

**Paso 2:** Separar en **tres** series: $n = 3k$, $n = 3k+1$ y $n = 3k+2$.

$$
X(z) = \sum_{k=0}^{\infty} 4^{3k} z^{-3k} + \sum_{k=0}^{\infty} 3^{-(3k+1)} z^{-(3k+1)} + \sum_{k=0}^{\infty} 3^{-(3k+2)} z^{-(3k+2)}
$$

$$
X(z) = \sum_{k=0}^{\infty} \left(\frac{64}{z^3}\right)^k + \frac{1}{3z} \sum_{k=0}^{\infty} 3^{-3k} \cdot z^{-3k} + \sum_{k=0}^{\infty} 3^{-3k} \cdot 3^{-2} \cdot z^{-3k} \cdot z^{-2}
$$

$$
X(z) = \sum_{k=0}^{\infty} \left(\frac{64}{z^3}\right)^k + \frac{1}{3z} \sum_{k=0}^{\infty} \left(\frac{1}{27z^3}\right)^k + \frac{1}{9z^2} \sum_{k=0}^{\infty} \left(\frac{1}{27z^3}\right)^k
$$

**Paso 3:** Sumar las tres geométricas (el profe numera los tres factores $\frac{1}{1-r}$ como (1), (2) y (3)).

$$
X(z) = \underbrace{\frac{1}{1 - \dfrac{64}{z^3}}}_{(1)} + \frac{1}{3z} \cdot \underbrace{\frac{1}{1 - \dfrac{1}{27z^3}}}_{(2)} + \frac{1}{9z^2} \cdot \underbrace{\frac{1}{1 - \dfrac{1}{27z^3}}}_{(3)}
$$

$$
X(z) = \frac{z^3}{z^3 - 64} + \frac{1}{3z} \cdot \frac{27z^3}{27z^3 - 1} + \frac{1}{9z^2} \cdot \frac{27z^3}{27z^3 - 1}
$$

Simplificando $\dfrac{27z^3}{3z} = 9z^2$ y $\dfrac{27z^3}{9z^2} = 3z$:

$$
\boxed{X(z) = \frac{z^3}{z^3 - 64} + \frac{9z^2 + 3z}{27z^3 - 1}}
$$

**Paso 4:** Región de convergencia (RC), al principio de la [p. 2]: la condición (1) da $|z| > 4$; las condiciones (2) y (3) dan $|z| > \tfrac{1}{3}$. La intersección es

$$
|z| > 4
$$

</details>

</details>

## Series de $e^x$ y de $\ln(1+x)$ como transformadas — [p. 2]

Para los optativos el profe **no** usa geométricas sino que reconoce la serie de una función conocida: la definición $\sum x(n) z^{-n}$ se reescribe hasta que aparezca una de las series del recuadro "Recuerde", evaluada en $x = \tfrac{1}{z}$ o $x = \tfrac{2}{z}$:

$$
e^x = \sum_{n=0}^{\infty} \frac{x^n}{n!} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots
$$

Para el logaritmo pega la salida de Wolfram "series $\log(1-x)$, expansion at $x = 0$":

$$
\log(1-x) = -x - \frac{x^2}{2} - \frac{x^3}{3} - \frac{x^4}{4} - \frac{x^5}{5} - \frac{x^6}{6} + O(x^7)
$$

<details>
<summary>📝 Ejercicio 1g (optativo) — [p. 2]: x(n) = 2ⁿ/n!</summary>

**Ejercicio n° 1 g) (optativo).** Halle, por definición, la transformada Z de $x(n) = \dfrac{2^n}{n!}$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Definición.

$$
X(z) = \sum_{n=0}^{\infty} \frac{2^n}{n!}\, z^{-n}
$$

**Paso 2:** Reconocer la serie de $e^x$ con $x = \dfrac{2}{z}$ (el profe anota $\tfrac{2}{z}$ arriba de la $x$ en $e^x = \sum \frac{x^n}{n!}$).

$$
X(z) = \sum_{n=0}^{\infty} \frac{\left(\dfrac{2}{z}\right)^n}{n!} = e^{2/z} \qquad \text{si } z \neq 0
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 1f (optativo) — [p. 2]: x(n) = 1/(n+1)</summary>

**Ejercicio n° 1 f) (optativo).** Halle, por definición, la transformada Z de $x(n) = \dfrac{1}{n+1}$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Definición y primeros términos.

$$
X(z) = \sum_{n=0}^{\infty} \frac{1}{n+1} \cdot z^{-n} = \frac{1}{1} z^{0} + \frac{1}{2} z^{-1} + \frac{1}{3} z^{-2} + \dots
$$

**Paso 2:** Multiplicar por $z^{-1}$ para que el exponente de $z$ coincida con el denominador y aparezca la serie del logaritmo.

$$
z^{-1} X(z) = \frac{1}{1} \cdot z^{-1} + \frac{1}{2} z^{-2} + \frac{1}{3} z^{-3} + \dots = \frac{\left(\frac{1}{z}\right)}{1} + \frac{\left(\frac{1}{z}\right)^2}{2} + \frac{\left(\frac{1}{z}\right)^3}{3} + \dots
$$

**Paso 3:** Comparar con la serie de $\ln(1-x)$ en $x = \tfrac{1}{z}$ (sacando un signo menos afuera).

$$
z^{-1} X(z) = -\left( -\frac{1/z}{1} - \frac{1/z^2}{2} - \frac{1/z^3}{3} - \dots \right) = -\ln\left(1 - \frac{1}{z}\right)
$$

**Paso 4:** Despejar $X(z)$.

$$
z^{-1} X(z) = -\ln\left(1 - \frac{1}{z}\right) \;\Longrightarrow\; \boxed{X(z) = -z \ln\left(1 - \frac{1}{z}\right)}
$$

</details>

</details>

## Secuencias finitas — [p. 2]

Si la sucesión tiene finitos términos no nulos, la definición es una suma finita: $X(z)$ queda como un polinomio en $z^{-1}$, que se lleva a una sola fracción con denominador $z^N$. Primero se lee cada valor $x(n)$ del gráfico.

<details>
<summary>📝 Ejercicio 2 — [p. 2]: transformada de una secuencia finita dada por su gráfico</summary>

**Ejercicio n° 2.** Dada la siguiente secuencia finita, halle la transformada Z de la misma.

Gráfico de bastones $x(n)$ vs. $n$ (de $n = -1$ a $n = 6$): $x(1) = 1$, $x(2) = 3$, $x(3) = 2$, $x(4) = 1$, y vale $0$ en $n = 0$, $n = 5$ y $n = 6$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Leer la secuencia del gráfico. El profe la escribe por casos y observa que para $n = 2$ a $n = 5$ vale $-n + 5$:

$$
x(n) = \begin{cases} 0 & n = 0 \\ 1 & n = 1 \\ 3 & n = 2 \\ 2 & n = 3 \\ 1 & n = 4 \\ 0 & n = 5 \\ 0 & n > 5 \end{cases}
$$

**Paso 2:** Aplicar la definición término a término.

$$
X(z) = 0\, z^{-0} + 1\, z^{-1} + 3\, z^{-2} + 2\, z^{-3} + 1 \cdot z^{-4}
$$

**Paso 3:** Reunir en una sola fracción.

$$
X(z) = \frac{1}{z} + \frac{3}{z^2} + \frac{2}{z^3} + \frac{1}{z^4} = \frac{z^3 + 3z^2 + 2z + 1}{z^4}
$$

</details>

</details>

## Transformada por tabla y propiedades: desplazamiento — [p. 2]

Lo que usa el profe en 3b:

- Tabla: $\mathcal{Z}\{u(n)\} = \dfrac{z}{z-1}$ (escalón, $x(n) = 1$).
- Propiedad de desplazamiento hacia la derecha: $\mathcal{Z}\{u(n-2)\} = z^{-2}\, X(z)$, donde $X(z)$ es la transformada de la sucesión sin desplazar.

<details>
<summary>📝 Ejercicio 3 a), c) — [p. 2]: transformadas por tabla y propiedades (sin resolver)</summary>

**Ejercicio n° 3.** Utilizando la tabla y las propiedades, halle la transformada Z de las siguientes sucesiones:

a) $x(n) = 2^n + 3\left(\dfrac{1}{2}\right)^n$ ; $n \ge 0$

c) $x(n) = 3^{n+1}$ ; $n \ge 0$

*(sin resolución en la fuente)*

</details>

<details>
<summary>📝 Ejercicio 3b — [p. 2]: x(n) = u(n−2)</summary>

**Ejercicio n° 3 b).** Utilizando la tabla y las propiedades, halle la transformada Z de $x(n) = u(n-2)$ ; $n \ge 2$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Interpretar la sucesión: $x(n) = 1$ para $n \ge 2$. Es el escalón desplazado dos lugares, así que por propiedad

$$
\mathcal{Z}\{u(n-2)\} = z^{-2} \cdot X(z) \qquad \text{con } X(z) = \frac{z}{z-1}
$$

**Paso 2:** Multiplicar y simplificar la $z$.

$$
\mathcal{Z}\{u(n-2)\} = \frac{z}{z-1} \cdot z^{-2} = \frac{z}{z-1} \cdot \frac{1}{z^2} = \boxed{\frac{1}{z\,(z-1)}}
$$

</details>

</details>

## Antitransformada: fracciones simples con la $z$ afuera, y series conocidas — [p. 2]

**Recuerde** (recuadro de la guía, [p. 3]):

$$
\cosh(x) = \frac{e^x + e^{-x}}{2} \qquad ; \qquad \operatorname{senh}(x) = \frac{e^x - e^{-x}}{2}
$$

Recetas que aplica el profe en el Ejercicio 5:

- **Fracciones simples con la $z$ afuera** (5a): las entradas de la tabla son de la forma $\dfrac{z}{z-a} \leftrightarrow a^n$, así que antes de descomponer se saca factor común $z$: $X(z) = z \cdot \dfrac{P(z)}{(z-1)(z-4)} = z\left(\dfrac{A}{z-1} + \dfrac{B}{z-4}\right)$. Las constantes $A$, $B$ se calculan evaluando (anota $A = \tfrac{-6}{-3} = 2$, $B = \tfrac{3}{3} = 1$) y después cada $z\cdot\dfrac{A}{z-a}$ se antitransforma por tabla.
- **Series conocidas** (5d): $e^{a/z} \leftrightarrow \dfrac{a^n}{n!}$ (es lo mismo del 1g leído al revés); $\operatorname{senh}$ se abre con la definición exponencial.
- **Corrimiento** (5f): si falta la $z$ del numerador, se escribe $X(z) = z^{-1} \cdot X_1(z)$ con $X_1(z)$ de tabla, y el $z^{-1}$ desplaza la sucesión un lugar hacia la derecha. Fila de tabla usada: $n \leftrightarrow \dfrac{z}{(z-1)^2}$.

<details>
<summary>📝 Ejercicio 5 b), c), e), g), h), i) — [p. 2]: antitransformadas (sin resolver)</summary>

**Ejercicio n° 5.** Halle las antitransformadas Z de las siguientes funciones:

b) $X(z) = \dfrac{2z^2}{z^2 - 9}$

c) $X(z) = \dfrac{z}{z^2 + z - 2}$

e) $X(z) = z\left(e^{\frac{1}{z}} - 1\right)$

g) $X(z) = \dfrac{2z^2 + z}{(z-2)^2 (z-1)}$

h) $X(z) = \dfrac{-z^2 + 4z}{(z-2)(z-1)^2}$

i) $X(z) = \dfrac{4z^3 - 14z^2 + 10z}{(z-3)(z^2 - 4z + 4)}$

*(sin resolución en la fuente)*

</details>

<details>
<summary>📝 Ejercicio 5a — [p. 3]: X(z) = 3z(z−3)/(z²−5z+4)</summary>

**Ejercicio n° 5 a).** Halle la antitransformada Z de $X(z) = \dfrac{3z(z-3)}{z^2 - 5z + 4}$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Factorizar el denominador y sacar la $z$ afuera para descomponer en fracciones simples.

$$
X(z) = \frac{3z(z-3)}{z^2 - 5z + 4} = z\left(\frac{3(z-3)}{(z-1)(z-4)}\right) = z\left(\frac{A}{z-1} + \frac{B}{z-4}\right)
$$

**Paso 2:** Calcular las constantes (anotadas en rojo): $A = \dfrac{-6}{-3} = 2$, $B = \dfrac{3}{3} = 1$.

$$
X(z) = 2\,\frac{z}{z-1} + \frac{z}{z-4}
$$

**Paso 3:** Antitransformar por tabla cada término.

$$
\boxed{x(n) = 2 + 4^n}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 5d — [p. 3]: X(z) = senh(2/z)</summary>

**Ejercicio n° 5 d).** Halle la antitransformada Z de $X(z) = \operatorname{senh}\left(\dfrac{2}{z}\right)$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Abrir el seno hiperbólico con su definición exponencial.

$$
X(z) = \operatorname{senh}\left(\frac{2}{z}\right) = \frac{e^{\frac{2}{z}} - e^{-\frac{2}{z}}}{2} = \frac{1}{2}\left(e^{\frac{2}{z}} - e^{-\frac{2}{z}}\right)
$$

**Paso 2:** Antitransformar cada exponencial con $e^{a/z} \leftrightarrow \dfrac{a^n}{n!}$ (con $a = 2$ y $a = -2$).

$$
x(n) = \left(\frac{2^n}{n!} - \frac{(-2)^n}{n!}\right) \cdot \frac{1}{2}
$$

**Paso 3:** O sea, los pares se cancelan y los impares se duplican:

$$
x(n) = \begin{cases} 0 & n \text{ par} \\ \dfrac{2^n}{n!} & n \text{ impar} \end{cases}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 5f — [p. 3]: X(z) = 1/(z−1)²</summary>

**Ejercicio n° 5 f).** Halle la antitransformada Z de $X(z) = \left(\dfrac{1}{z-1}\right)^2$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Escribir $X(z) = \dfrac{1}{(z-1)^2}$ y compararla con la fila de tabla $n \leftrightarrow \dfrac{z}{(z-1)^2}$: falta una $z$ en el numerador.

**Paso 2:** Sacar un $z^{-1}$ para que quede la entrada de tabla $X_1(z)$.

$$
X(z) = z^{-1} \underbrace{\frac{z}{(z-1)^2}}_{X_1(z)}
$$

**Paso 3:** El $z^{-1}$ desplaza un lugar la sucesión $n$:

$$
x(n) = \begin{cases} 0 & n = 0 \\ n - 1 & n > 0 \end{cases}
$$

</details>

</details>

## Ecuaciones en diferencias de orden 1: propiedad de $x(n+1)$ — [p. 3]

Para pasar la ecuación al dominio $z$ el profe usa la propiedad de desplazamiento hacia la izquierda (la misma que aparece en el ítem d) del múltiple choice de la [p. 5]):

$$
\mathcal{Z}\{x(n+1)\} = z\, X(z) - z\, x(0)
$$

Receta (6e): transformar miembro a miembro usando la tabla para el segundo miembro ($2^n \leftrightarrow \dfrac{z}{z-2}$, $n\,2^n \leftrightarrow \dfrac{2z}{(z-2)^2}$), reemplazar la condición inicial, despejar $X(z)$, poner todo sobre un denominador común **sacando la $z$ afuera**, descomponer en fracciones simples (con un término por cada potencia de cada raíz múltiple) y antitransformar por tabla.

<details>
<summary>📝 Ejercicio 6 a), b), c), d) — [p. 3]: ecuaciones en diferencias de orden 1 (sin resolver)</summary>

**Ejercicio n° 6.** Resuelva las siguientes ecuaciones en diferencias de orden 1 utilizando la transformada Z:

a) $a_{n+1} - 5a_n = 12$ con $a_0 = -1$

b) $a_{n+1} - 2a_n = 2$ con $a_0 = 3$

c) $a_{n+1} - 2a_n = 2 \cdot 3^n$ con $a_0 = 2$

d) $a_{n+1} = 2a_n + 3n - 1$ con $a_0 = 0$

*(sin resolución en la fuente)*

</details>

<details>
<summary>📝 Ejercicio 6e — [p. 3]: aₙ₊₁ − 4aₙ = 4(1−n)·2ⁿ con a₀ = 3</summary>

**Ejercicio n° 6 e).** Resuelva la siguiente ecuación en diferencias de orden 1 utilizando la transformada Z: $a_{n+1} - 4a_n = 4(1-n)\,2^n$ con $a_0 = 3$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Distribuir el segundo miembro para que queden sucesiones de tabla.

$$
x(n+1) - 4x(n) = 4 \cdot 2^n - 4 \cdot n \cdot 2^n
$$

**Paso 2:** Transformar miembro a miembro, con $\mathcal{Z}\{x(n+1)\} = zX(z) - z\,x(0)$ y $x(0) = 3$.

$$
zX(z) - z\,x(0) - 4X(z) = 4\,\frac{z}{z-2} - 4\,\frac{2z}{(z-2)^2}
$$

$$
(z-4)\,X(z) = \frac{4z}{z-2} - \frac{8z}{(z-2)^2} + 3z
$$

**Paso 3:** Despejar $X(z)$ con denominador común y sacar la $z$ afuera.

$$
X(z) = \frac{4z(z-2) - 8z + 3z(z-2)^2}{(z-2)^2 (z-4)} = z\left(\frac{4(z-2) - 8 + 3(z-2)^2}{(z-2)^2 (z-4)}\right)
$$

**Paso 4:** Fracciones simples (raíz doble en $z = 2$: dos términos).

$$
X(z) = z\left(\frac{A}{(z-2)^2} + \frac{B}{z-2} + \frac{C}{z-4}\right)
$$

Constantes anotadas en rojo: $A = \dfrac{-8}{-2} = 4$, $C = \dfrac{12}{4} = 3$, y $B = 0$. Para $B$ el profe iguala numeradores:

$$
4(z-4) + B(z-2)(z-4) + 3(z-2)^2 = 4z - 8 - 8 + 3z^2 - 12z + 12
$$

Comparando el coeficiente de $z^2$: $B + 3 = 3 \Rightarrow B = 0$. Comparando el de $z$: $4 - 6B - 12 = -8 \Rightarrow -6B - 8 = -8 \;\therefore\; B = 0$.

**Paso 5:** Antitransformar por tabla (anota $4 = 2 \cdot 2$ para usar $n\,2^n \leftrightarrow \dfrac{2z}{(z-2)^2}$).

$$
X(z) = \frac{4z}{(z-2)^2} + \frac{3z}{z-4} \;\therefore\; x(n) = 2n \cdot 2^n + 3 \cdot 4^n
$$

$$
\boxed{x(n) = n \cdot 2^{n+1} + 3 \cdot 4^n}
$$

</details>

</details>

## Ecuaciones en diferencias de orden 2: propiedad de $x(n+2)$ y análisis del denominador — [p. 3]

Propiedad que usa el profe para el término $x(n+2)$ (aplicada en 7f, 7g y 8b):

$$
\mathcal{Z}\{x(n+2)\} = z^2 X(z) - z^2\, x(0) - z\, x(1)
$$

Receta de orden 2:

1. Transformar miembro a miembro; reemplazar $x(0)$ y $x(1)$ (el profe tacha en verde los términos que se anulan por condiciones iniciales nulas).
2. Agrupar $X(z)\cdot(\text{polinomio característico})$ y despejar.
3. **Análisis del denominador:** factorizar el polinomio característico hallando sus raíces (en Fibonacci, con la resolvente: $z^2 - z - 1 = (z - \varphi_1)(z - \varphi_2)$).
4. Sacar la $z$ afuera, fracciones simples (si hay factor cuadrático irreducible como $z^2 + 1$, el numerador es $Cz + D$), igualar numeradores y comparar coeficientes.
5. Antitransformar por tabla. Filas usadas: $a^n \leftrightarrow \dfrac{z}{z-a}$, $(-1)^n \leftrightarrow \dfrac{z}{z+1}$, $1 \leftrightarrow \dfrac{z}{z-1}$, $n\,2^n \leftrightarrow \dfrac{2z}{(z-2)^2}$ y la fila del seno (tal como figura en la tabla pegada en la [p. 4]):

$$
\operatorname{sen}(an) \;\leftrightarrow\; \frac{z \cdot \operatorname{sen}(a)}{z^2 - 2\cos(a) + 1}
$$

que con $a = \tfrac{\pi}{2}$ ($\operatorname{sen}\tfrac{\pi}{2} = 1$, $\cos\tfrac{\pi}{2} = 0$) da $\operatorname{sen}\left(n\tfrac{\pi}{2}\right) \leftrightarrow \dfrac{z}{z^2 + 1}$.

<details>
<summary>📝 Ejercicio 7 a), b), c), d), e) — [p. 3]: ecuaciones en diferencias de orden 2 (sin resolver)</summary>

**Ejercicio n° 7.** Resuelva las siguientes ecuaciones en diferencias de orden 2 utilizando la transformada Z:

a) $a_{n+2} + 3a_{n+1} + 2a_n = 3^n$ con $a_0 = 0 \;\wedge\; a_1 = 1$

b) $a_{n+2} + 4a_{n+1} + 4a_n = 7$ con $a_0 = 1 \;\wedge\; a_1 = 2$

c) $x(n+2) - 4x(n+1) + 3x(n) = -2$ $\wedge$ $x(0) = 7 \;\wedge\; x(1) = 12$

d) $x(n+2) - 4x(n+1) + 4x(n) = 4 \cdot 3^n$ $\wedge$ $x(0) = 4 \;\wedge\; x(1) = 14$

e) $x(n+2) - 6x(n+1) + 9x(n) = 5 \cdot 2^n$ $\wedge$ $x(0) = 5 \;\wedge\; x(1) = 13$

*(sin resolución en la fuente)*

</details>

<details>
<summary>📝 Ejercicio 7f — [p. 4]: serie de Fibonacci aₙ₊₂ = aₙ₊₁ + aₙ con a₀ = 0, a₁ = 1</summary>

**Ejercicio n° 7 f).** Resuelva la siguiente ecuación en diferencias de orden 2 utilizando la transformada Z: $a_{n+2} = a_{n+1} + a_n$ con $a_0 = 0 \;\wedge\; a_1 = 1$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** El profe la identifica como la **serie de Fibonacci** y escribe los primeros términos para verificar después: $0, 1, 1, 2, 3, 5, 8, 13$ para $n = 0, 1, \dots, 7$ (o sea $a_7 = 13$).

$$
x(n+2) = x(n+1) + x(n) \qquad x(0) = 0 \;;\; x(1) = 1
$$

**Paso 2:** Transformar miembro a miembro; los términos con $x(0) = 0$ se tachan y $x(1) = 1$.

$$
z^2 X(z) - z^2 x(0) - z\,x(1) = zX(z) - z\,x(0) + X(z)
$$

$$
X(z)\left(z^2 - z - 1\right) = z
$$

**Paso 3:** Despejar y sacar la $z$ afuera; el denominador se factoriza como $(z - \varphi_1)(z - \varphi_2)$.

$$
X(z) = \frac{z}{z^2 - z - 1} = z \cdot \left(\frac{1}{z^2 - z - 1}\right) = z\left(\frac{A}{z - \varphi_1} + \frac{B}{z - \varphi_2}\right)
$$

**Paso 4:** Análisis del denominador (en rojo): raíces de $z^2 - z - 1$.

$$
\varphi_{1,2} = \frac{1 \pm \sqrt{1 + 4}}{2} = \frac{1 \pm \sqrt{5}}{2} \;\Rightarrow\; \varphi_1 = \frac{1 + \sqrt{5}}{2} \;;\; \varphi_2 = \frac{1 - \sqrt{5}}{2}
$$

**Paso 5:** Constantes de las fracciones simples (anotadas en celeste): $A = \dfrac{1}{\sqrt{5}}$, $B = -\dfrac{1}{\sqrt{5}}$.

$$
X(z) = \frac{1}{\sqrt{5}} \cdot \frac{z}{z - \varphi_1} - \frac{1}{\sqrt{5}} \cdot \frac{z}{z - \varphi_2}
$$

**Paso 6:** Antitransformar por tabla.

$$
x(n) = \frac{1}{\sqrt{5}} \cdot \varphi_1^{\,n} - \frac{1}{\sqrt{5}} \cdot \varphi_2^{\,n} \qquad \text{o sea} \qquad x(n) = \frac{1}{\sqrt{5}}\left(\frac{1 + \sqrt{5}}{2}\right)^n - \frac{1}{\sqrt{5}}\left(\frac{1 - \sqrt{5}}{2}\right)^n
$$

**Paso 7:** Verificación (Wolfram): $\dfrac{1}{\sqrt{5}}\left(\tfrac{1}{2}(1+\sqrt{5})\right)^7 - \dfrac{1}{\sqrt{5}}\left(\tfrac{1}{2}(1-\sqrt{5})\right)^7 = 13$, es decir $x(7) = 13$, coincide con la lista del Paso 1.

</details>

</details>

<details>
<summary>📝 Ejercicio 7g — [p. 4]: aₙ₊₂ − aₙ = sen(nπ/2) con a₀ = 1, a₁ = 1</summary>

**Ejercicio n° 7 g).** Resuelva la siguiente ecuación en diferencias de orden 2 utilizando la transformada Z: $a_{n+2} - a_n = \operatorname{sen}\left(\dfrac{n\pi}{2}\right)$ con $a_0 = 1 \;\wedge\; a_1 = 1$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Transformar miembro a miembro usando la fila $\operatorname{sen}(an)$ de la tabla con $a = \tfrac{\pi}{2}$.

$$
x(n+2) - x(n) = \operatorname{sen}\left(n\frac{\pi}{2}\right)
$$

$$
z^2 X(z) - z^2 x(0) - z\,x(1) - X(z) = \frac{z\,\operatorname{sen}\left(\frac{\pi}{2}\right)}{z^2 - 2\cos\left(\frac{\pi}{2}\right) + 1}
$$

Con $\operatorname{sen}\frac{\pi}{2} = 1$ y $\cos\frac{\pi}{2} = 0$ (anotados en rojo): $\operatorname{sen}\left(n\frac{\pi}{2}\right) \leftrightarrow \dfrac{z}{z^2 + 1}$.

**Paso 2:** Reemplazar $x(0) = 1$, $x(1) = 1$ y despejar.

$$
z^2 X(z) - z^2 - z - X(z) = \frac{z}{z^2 + 1}
$$

$$
X(z)\left(z^2 - 1\right) = \frac{z}{z^2 + 1} + z^2 + z
$$

$$
X(z) = \frac{z}{(z^2 + 1)(z+1)(z-1)} + \frac{z\,(z+1)}{(z+1)(z-1)}
$$

En el segundo término se simplifica $(z+1)$ (tachado en rojo):

$$
X(z) = z\left(\frac{1}{(z^2 + 1)(z+1)(z-1)}\right) + \frac{z}{z-1}
$$

**Paso 3:** Fracciones simples del primer término (el factor $z^2 + 1$ es cuadrático: numerador $Cz + D$).

$$
X(z) = z\left(\frac{A}{z+1} + \frac{B}{z-1} + \frac{Cz + D}{z^2 + 1}\right) + \frac{z}{z-1}
$$

Constantes en rojo: $A = -\dfrac{1}{4}$, $B = \dfrac{1}{4}$, $C = 0$, $D = -\dfrac{1}{2}$. Cálculo (FS, en rojo a la derecha):

$$
-\frac{1}{4}(z^2 + 1)(z - 1) + \frac{1}{4}(z^2 + 1)(z + 1) + (Cz + D)(z^2 - 1) = 1
$$

$$
-\frac{1}{4}z^3 + \frac{1}{4}z^2 - \frac{1}{4}z + \frac{1}{4} + \frac{1}{4}z^3 + \frac{1}{4}z^2 + \frac{1}{4}z + \frac{1}{4} + Cz^3 - Cz + Dz^2 - D = 1
$$

Los $z^3$ de las dos primeras se cancelan, así que $C = 0$; en $z^2$: $\dfrac{1}{4} + \dfrac{1}{4} + D = 0 \Rightarrow \dfrac{1}{2} + D = 0 \Rightarrow D = -\dfrac{1}{2}$.

**Paso 4:** Reescribir y juntar los dos términos en $\dfrac{z}{z-1}$.

$$
X(z) = -\frac{1}{4}\,\frac{z}{z+1} + \frac{1}{4}\,\frac{z}{z-1} - \frac{1}{2}\,\frac{z}{z^2 + 1} + \frac{z}{z-1}
$$

$$
X(z) = -\frac{1}{4}\,\frac{z}{z+1} + \frac{5}{4}\,\frac{z}{z-1} - \frac{1}{2}\,\frac{z}{z^2 + 1}
$$

**Paso 5:** Antitransformar por tabla.

$$
\boxed{x(n) = -\frac{1}{4}(-1)^n + \frac{5}{4} - \frac{1}{2}\operatorname{sen}\left(n\frac{\pi}{2}\right)}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 8 a), c) — [p. 4]: ecuaciones de orden 2, escribir X(z) y x(n) (sin resolver)</summary>

**Ejercicio n° 8.** Para las siguientes ecuaciones en diferencias de orden 2 escriba la $X(z)$ y la $x(n)$ correspondiente a cada una:

a) $x(n+2) - 6x(n+1) + 9x(n) = 100\,(-2)^n$ con $x(0) = 4 \;\wedge\; x(1) = -5$

c) $a_{n+2} - 2a_{n+1} - 3a_n = 24 \cdot 3^n + 12 \cdot 5^n$ con $a_0 = 1 \;\wedge\; a_1 = 11$

*(sin resolución en la fuente)*

</details>

<details>
<summary>📝 Ejercicio 8b — [p. 5]: x(n+2) − 4x(n+1) + 4x(n) = 4ⁿ⁺¹ con x(0) = 1, x(1) = 10</summary>

**Ejercicio n° 8 b).** Para la siguiente ecuación en diferencias de orden 2 escriba la $X(z)$ y la $x(n)$ correspondiente: $x(n+2) - 4x(n+1) + 4x(n) = 4^{n+1}$ con $x(0) = 1 \;\wedge\; x(1) = 10$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Reescribir el segundo miembro como $4^{n+1} = 4^n \cdot 4$ para usar la tabla ($4^n \leftrightarrow \dfrac{z}{z-4}$).

**Paso 2:** Transformar miembro a miembro con $x(0) = 1$ y $x(1) = 10$.

$$
z^2 X(z) - z^2 x(0) - z\,x(1) - 4\left(zX(z) - z\,x(0)\right) + 4X(z) = \frac{4z}{z-4}
$$

$$
z^2 X(z) - z^2 - 10z - 4zX(z) + 4z + 4X(z) = \frac{4z}{z-4}
$$

**Paso 3:** Agrupar y despejar.

$$
X(z)\left(z^2 - 4z + 4\right) = \frac{4z}{z-4} + z^2 + 6z
$$

$$
X(z) = \frac{4z + z^2(z-4) + 6z(z-4)}{(z-4)(z-2)^2} = z\left(\frac{4 + z(z-4) + 6(z-4)}{(z-4)(z-2)^2}\right)
$$

**Paso 4:** Fracciones simples (raíz doble en $z = 2$).

$$
X(z) = z\left(\frac{A}{z-4} + \frac{B}{(z-2)^2} + \frac{C}{z-2}\right)
$$

Constantes en rojo: $A = \dfrac{4}{4} = 1$, $B = \dfrac{-12}{-2} = 6$, $C = 0$. Para $C$ iguala numeradores:

$$
1\,(z-2)^2 + 6(z-4) + C(z-2)(z-4) = 4 + z^2 - 4z + 6z - 24
$$

Coeficiente de $z^2$: $1 + C = 1 \Rightarrow C = 0$.

**Paso 5:** Antitransformar (anota $6 = 3 \cdot 2$ para usar $n\,2^n \leftrightarrow \dfrac{2z}{(z-2)^2}$).

$$
X(z) = \frac{z}{z-4} + 6\,\frac{z}{(z-2)^2}
$$

$$
\boxed{x(n) = 4^n + 3 \cdot n \cdot 2^n}
$$

</details>

</details>

## Propiedades de la transformada Z: verdadero o falso — [p. 5]

Las propiedades que valen son las de **linealidad** (suma y producto por constante) y la de **desplazamiento** $\mathcal{Z}\{x(n+1)\} = z\,\mathcal{Z}\{x(n)\} - z\,x(0)$ (ojo con la $z$ que multiplica a $x(0)$). La transformada **no** es multiplicativa: $\mathcal{Z}$ de un producto no es el producto de las transformadas. Para refutar una propiedad falsa el profe da un **contraejemplo** con sucesiones de tabla. Filas usadas:

$$
n \leftrightarrow \frac{z}{(z-1)^2} \qquad ; \qquad n^2 \leftrightarrow \frac{z(z+1)}{(z-1)^3}
$$

<details>
<summary>📝 Ítem de opción múltiple — [p. 5]: propiedades de Z sobre aₙ y bₙ</summary>

**Ítem 4 (opción múltiple).** Sean las sucesiones $a_n$ y $b_n$, entonces se cumple:

a) $\mathcal{Z}[a_n \cdot b_n] = \mathcal{Z}[a_n] \cdot \mathcal{Z}[b_n]$

b) $\mathcal{Z}[a_n^2] = \mathcal{Z}[a_n]^2$

c) $\mathcal{Z}[a_n - k\,b_n] = \mathcal{Z}[a_n] - k\,\mathcal{Z}[b_n]$

d) $\mathcal{Z}[a_{n+1}] = z\,\mathcal{Z}[a_n] - a_0$

e) n.a.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Marcas en verde del profe: a) **F**, b) **F**, c) **V**, d) **F**, e) **F**.

**Paso 2:** a) Falsa, por contraejemplo:

$$
\mathcal{Z}(2 \cdot 3^n) \neq \mathcal{Z}(2) \cdot \mathcal{Z}(3^n)
$$

ya que

$$
\mathcal{Z}(2 \cdot 3^n) = 2\,\frac{z}{z-3} \qquad \text{y} \qquad \mathcal{Z}(2) \cdot \mathcal{Z}(3^n) = \frac{2z}{z-1} \cdot \frac{z}{z-3}
$$

**Paso 3:** b) Falsa, contraejemplo con $x(n) = n$: por tabla $n \leftrightarrow \dfrac{z}{(z-1)^2}$ y $n^2 \leftrightarrow \dfrac{z(z+1)}{(z-1)^3}$, que no es el cuadrado de la anterior.

**Paso 4:** c) Verdadera, por propiedad de linealidad.

**Paso 5:** d) Falsa: la propiedad es

$$
\mathcal{Z}\{x(n+1)\} = z\,\mathcal{Z}\{x(n)\} - z\,x(0)
$$

(el profe subraya la $z$ que multiplica a $x(0)$ y que falta en el enunciado).

</details>

</details>

## La región de convergencia sale sin resolver la transformada — [p. 5]

Idea clave del profe (anotada en verde en la [p. 5]): **"El área de convergencia sale sin necesidad de resolver el resto de la Transformada Z."** Alcanza con separar la definición en las series geométricas (una por clase de $n$), identificar la razón de cada una, imponer $|r| < 1$ y hacer la **intersección**. Terminar de sumar las series solo hace falta si piden $X(z)$.

<details>
<summary>📝 Ejercicio 4c (V/F) — [p. 5]: ROC de x(n) = 3 si n es múltiplo de 5, (−2)ⁿ si no, ¿es |z| > 2?</summary>

**Ejercicio n° 4.** Indique el valor de verdad de las siguientes proposiciones, justificando correctamente:

c) Dada la secuencia $x(n) = \begin{cases} 3 & \text{si } n \text{ es múltiplo de } 5 \\ (-2)^n & \text{si } n \text{ no es múltiplo de } 5 \end{cases}$, la región de convergencia de su transformada Z es: $|z| > 2$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Definición y primeros términos.

$$
X(z) = \sum_{n=0}^{\infty} x(n)\, z^{-n} = 3 \cdot z^{-0} + (-2)^1 z^{-1} + (-2)^2 z^{-2} + (-2)^3 z^{-3} + (-2)^4 z^{-4} + 3\, z^{-5} + \dots
$$

**Paso 2:** Separar en **cinco** series: $n = 5k$, $5k+1$, $5k+2$, $5k+3$, $5k+4$.

$$
X(z) = \sum_{k=0}^{\infty} 3\left(\frac{1}{z}\right)^{5k} + \sum_{k=0}^{\infty} \left(\frac{-2}{z}\right)^{5k+1} + \sum_{k=0}^{\infty} \left(\frac{-2}{z}\right)^{5k+2} + \sum_{k=0}^{\infty} \left(\frac{-2}{z}\right)^{5k+3} + \sum_{k=0}^{\infty} \left(\frac{-2}{z}\right)^{5k+4}
$$

$$
X(z) = \sum_{k=0}^{\infty} 3\left(\frac{1}{z^5}\right)^k - \frac{2}{z} \sum_{k=0}^{\infty} \left(\frac{-32}{z^5}\right)^k + \frac{4}{z^2} \sum_{k=0}^{\infty} \left(\frac{-32}{z^5}\right)^k - \frac{8}{z^3} \sum_{k=0}^{\infty} \left(\frac{-32}{z^5}\right)^k + \frac{16}{z^4} \sum_{k=0}^{\infty} \left(\frac{-32}{z^5}\right)^k
$$

**Paso 3:** La región de convergencia sale acá, sin sumar nada: hay solo dos razones distintas.

$$
\text{①}\quad \left|\frac{1}{z^5}\right| < 1 \;\Rightarrow\; |z^5| > 1 \;\Rightarrow\; |z| > 1
$$

$$
\text{②}\quad \left|\frac{-32}{z^5}\right| < 1 \;\Rightarrow\; |z^5| > 32 \;\Rightarrow\; |z| > 2
$$

Intersección:

$$
\boxed{|z| > 2} \qquad \text{✓ (la proposición es verdadera)}
$$

**Paso 4:** El resto de la transformada quedaría ([p. 6]):

$$
X(z) = 3 \cdot \frac{1}{1 - \left(\frac{1}{z^5}\right)} - \frac{2}{z} \cdot \frac{1}{1 - \left(\frac{-32}{z^5}\right)} + \frac{4}{z^2} \cdot \frac{1}{1 - \left(\frac{-32}{z^5}\right)} - \frac{8}{z^3} \cdot \frac{1}{1 - \left(\frac{-32}{z^5}\right)} + \frac{16}{z^4} \cdot \frac{1}{1 - \left(\frac{-32}{z^5}\right)}
$$

$$
= \frac{3z^5}{z^5 - 1} - \frac{2z^4}{z^5 + 32} + \frac{4z^3}{z^5 + 32} - \frac{8z^2}{z^5 + 32} + \frac{16z}{z^5 + 32}
$$

$$
\boxed{X(z) = \frac{3z^5}{z^5 - 1} + \frac{-2z^4 + 4z^3 - 8z^2 + 16z}{z^5 + 32}}
$$

</details>

</details>

---

*Generado el 2026-10-02 a partir de `fuentes/clases/Transformada Z/Transformada Z.pdf` (OneNote de la clase práctica de Transformada Z, jueves 6 de mayo de 2021, 6 páginas: guía tipeada + resolución manuscrita del profesor). Transcripción fiel del manuscrito: no se corrigieron ni completaron cuentas; la fila `sen(an)` de la tabla se copió tal como figura en la fuente.*
