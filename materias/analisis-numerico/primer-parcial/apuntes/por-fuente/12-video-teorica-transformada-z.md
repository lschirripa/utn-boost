# Transformada Z (clase teórica grabada)

> Fuente: fuentes/clases/Transformada Z/T_TZ.mp4 (transcripción local con Whisper)

---

## Índice

- [00:00] — Lo que el profe remarca (resumen de todos los comentarios sobre parciales y ejercicios)
- [00:00] — Señales en tiempo discreto: la Z es "Laplace para dominios discretos"
- [03:41] — Cómo se dan las señales en los ejercicios: forma analítica y forma gráfica
- [05:49] — Señales discretas comunes: impulso, escalón, rampa y exponencial
- [12:02] — Definición de transformada Z y paralelo con Laplace
- [16:45] — 📝 Ejercicio 1: transformada Z del impulso unitario
- [19:24] — Suma de la serie geométrica (la herramienta de toda la unidad)
- [24:07] — 📝 Ejercicio 2: transformada Z del escalón unitario y región de convergencia
- [27:41] — 📝 Ejercicio 3: transformada Z de $a^n$
- [29:47] — 📝 Ejercicio 4: secuencia finita dada por partes
- [32:57] — 📝 Ejercicio 5: $x(n) = 5$ si $n$ par, $0$ si $n$ impar
- [36:04] — 📝 Ejercicio 6: una expresión para los pares y otra para los impares, con región de convergencia
- [44:24] — Región de convergencia de toda la $X(z)$: intersección de las regiones
- [47:35] — Tabla de transformadas Z
- [49:38] — Propiedad de linealidad
- [50:41] — 📝 Ejercicio 7: $x(n) = 3(-2)^n - 2\cdot 5^n$ por linealidad y tabla
- [52:18] — Desplazamiento a derecha
- [55:28] — Desplazamiento a izquierda (el análogo de la derivada de Laplace)
- [1:02:18] — Multiplicación por $n$
- [1:03:52] — 📝 Ejercicio 8: transformadas de $n$ y de $n^2$ con la multiplicación por $n$
- [1:05:36] — Resumen de los desplazamientos laterales
- [1:06:38] — Antitransformada Z: por tabla o por fracciones simples "dejando una $z$ afuera"
- [1:08:44] — 📝 Ejercicio 9: antitransformar $X(z) = \dfrac{z^2+2z}{(z-1)(z-3)}$
- [1:13:24] — 📝 Ejercicio 10 (5f de la guía): antitransformar $X(z) = \dfrac{1}{(z-1)^2}$
- [1:15:31] — Ecuaciones en diferencias: la mecánica
- [1:16:33] — 📝 Ejercicio 11: $x(n+1) - x(n) = 7$, $x(0) = 3$, con verificación
- [1:23:25] — Ecuaciones en diferencias de segundo orden
- [1:23:58] — 📝 Ejercicio 12: $x(n+2) - 4x(n+1) + 3x(n) = -2$, $x(0) = 7$, $x(1) = 12$, con verificación

---

## Lo que el profe remarca

Todo comentario sobre qué se toma, qué importa y cómo conviene trabajar, en orden cronológico.

**Qué se toma y qué no**

- [10:31] — Las señales exponenciales $a^n$ y sus gráficos según el valor de $a$: "esto la verdad es que no le asigno demasiada importancia" (ya en [08:56] dijo que es "más a modo de ejemplo").
- [16:13] — Igual que en Laplace, la **tablita de transformadas Z se puede usar en el parcial**.
- [16:45] — "Hay un montón de transformadas que son perfectamente **ejercicios de parcial** que vamos a resolver **por definición**".
- [36:04] — El ejercicio con una expresión para los pares y otra para los impares "ya sí podría ser **bastante de parcial**". [43:22] "Esto es algo que **se toma bastante, se toma mucho, tanto en finales como en parciales**: una expresión para los pares, una expresión distinta para los impares, y operar". Es "bastante mecánico todo, porque siempre es lo mismo".
- [44:24] — Los enunciados **suelen pedir "hallar transformada Z y la región de convergencia"**. [44:57] Siempre que trabajen con series geométricas tienen que hallar la región de convergencia (no en las secuencias de "puntitos sueltos").
- [47:35] — Impulso corrido: "no me acuerdo si hay algún ejercicio donde se use esto". [48:07]–[48:38] Seno y coseno: "hay un solo ejercicio creo donde se usa el seno". $a^n/n!$: hay un ejercicio que se ve en la práctica del martes.
- [58:38] — "**Nunca les vamos a pedir más de 2 desplazamientos**" a izquierda (siempre 1 o 2 unidades); a derecha puede ser cualquier cosa.
- [1:03:21] — Multiplicación por $n$: "no vamos a trabajar más que con $n$ o $n^2$".
- [1:08:12] — Para antitransformar, **la linealidad es la única propiedad que importa**; las otras propiedades de la guía "son extra".
- [1:23:58] — Las ecuaciones en diferencias "o van a ser de primer orden o van a ser de segundo orden. Más que eso ya sería un despropósito".
- [1:26:02] — En general los polos (raíces del denominador) salen **reales**; hay un solo ejercicio (de la práctica del martes) con raíces complejas conjugadas: se resuelve igual, con $Az + B$ en el numerador.

**Cómo conviene trabajar**

- [24:07] — La suma de la serie geométrica "se va a usar muchísimo, muchísimo, muchísimo en los ejercicios de transformada, así que tengan a bien tenerlo presente".
- [28:13] — La idea de los ejercicios por definición "es siempre llevarlos a una serie geométrica": "algo elevado a la $n$, no importa el choclo que les quede adentro". [35:34] "Siempre tienen que dejar una $k$ o una $n$ afuera de exponente de algo. Y ese algo va a ser la razón".
- [30:19] — En los ejercicios de pocos puntos, "está bueno siempre hacerse un grafiquito" para ver qué se transforma.
- [32:27] — Para una secuencia finita espera que escriban la transformada como suma de potencias de $1/z$ o con denominador común (las dos formas aparecen en las respuestas de la guía).
- [34:30] — Al separar pares e impares se usa $k$ ($2k$, $2k+1$) por comodidad; usar $n$ "no pasa nada".
- [43:22]–[43:53] — Los pasos intermedios de separar factores él se los saltea; "hagan todos los pasos que necesiten", lo importante es llegar a "sumatoria de algo a la $k$".
- [47:01] — En este tipo de ejercicio la región de convergencia total es **siempre la más grande** (el círculo de afuera).
- [1:13:24] — "La recomendación es siempre, cuando trabajamos con transformada Z, para hacer fracciones simples **dejar una $z$ afuera**" (ver [1:10:46] por qué). [1:26:35] Lo repite: "por favor".
- [1:19:12] — En la ecuación en diferencias, al despejar $X(z)$ conviene pasar dividiendo **a cada término por separado**: quedan antitransformadas directas.
- [1:29:44] — **Verificar** la solución de la ecuación en diferencias con los datos iniciales (o calculando términos con la recurrencia) "lleva 40 segundos" y con eso "ya se pueden quedar tranquilos que el ejercicio que hicieron en el parcial está bien".

---

## Señales en tiempo discreto — [00:00]

- La transformada Z es "muy parecida" a la de Laplace, pero **aplicada a dominios discretos**: Laplace transforma funciones continuas $f(t)$; la Z transforma funciones cuyo dominio son **puntitos discretos**.
- Esas sucesiones o **señales de tiempo discreto** se notan $x(n)$ (el equivalente de la $f(t)$ de Laplace), con

$$
n \in \mathbb{N}_0 = \{0, 1, 2, 3, \dots\}
$$

y valores $x(n)$ reales (cualquier número real: $\pi$, $e$, $-3$, …). El tiempo está representado en unidades discretas (milisegundos, segundos, minutos, según el caso de estudio).
- [01:35] Motivación: el análisis de señales en la práctica se hace con componentes electrónicos que **muestrean** la señal continua (cada un milisegundo, cada un segundo…), por eso se trabaja tanto con funciones discretas (la transformada discreta de Fourier también nace de la continua).

## Cómo se dan las señales en los ejercicios — [03:41]

Dos maneras equivalentes de dar la misma señal:

- **Forma analítica** (función partida): se dice cuánto vale $x(n)$ para cada $n$. Ejemplo de la clase [04:17]:

$$
x(n) = \begin{cases} 1 & n = 0 \\ 3 & 1 \le n \le 3 \\ -1 & n = 4 \\ 0 & n \ge 5 \end{cases}
$$

Se usa sobre todo cuando son pocos valores ("valor a valor"); cuando la señal se extiende al infinito se usan otras notaciones.
- **Forma gráfica** [05:18]: los mismos valores dibujados como puntos sobre el eje $n$ (vale 1 en $n=0$, 3 entre 1 y 3, $-1$ en 4 y se anula de 5 en adelante).

## Señales discretas comunes — [05:49]

**Impulso unitario** $\delta(n)$ [06:20]: mucho más fácil de definir que en Laplace (donde salía de un límite con $\tau \to 0$ y área 1), pero representa el mismo fenómeno, un instante de señal:

$$
\delta(n) = \begin{cases} 1 & n = 0 \\ 0 & n \ne 0 \end{cases}
$$

**Escalón unitario** $u(n)$ [06:50]: es el $E(t)$ de Laplace (acá, "por alguna razón que desconozco", se llama con $u$) [07:53]. Representa la **función constante 1**: todos los puntos a la misma altura desde $n = 0$ hasta el infinito.

$$
u(n) = 1 \quad (n \ge 0)
$$

**Rampa unitaria** [08:23]: el equivalente discreto de la función identidad; se trabaja menos que las dos anteriores.

$$
x(n) = n
$$

**Señal exponencial** $x(n) = a^n$ [08:56] (a modo de ejemplo):

- $0 < a < 1$: exponencial decreciente, se hace asintótica al eje horizontal.
- $a > 1$: crece, como una $e^x$ pero con puntitos [09:56].
- $-1 < a < 0$ [10:31]: en $n = 0$ vale 1; con $n$ impar los puntos quedan del lado negativo y con $n$ par del lado positivo, alternando arriba/abajo y tendiendo a 0 cuando $n \to \infty$ [11:01].

## Definición de transformada Z — [12:02]

Dada $x(n) = a_n$ (en los ejercicios se usan como sinónimos $x(n)$ y $a_n$), con $n \in \mathbb{N}_0$, se define

$$
\mathcal{Z}\left[x(n)\right] = \sum_{n=0}^{\infty} x(n)\, z^{-n} = X(z)
$$

- $\mathcal{Z}$ es el operador (una Z mayúscula, como la $\mathcal{L}$ de Laplace) y $X(z)$ va en mayúscula, como las $X(s)$ de Laplace. **La $z$ es el equivalente de la $s$.**
- **Paralelo con Laplace** [13:05]:

$$
\mathcal{L}\left[f(t)\right] = \int_0^{\infty} f(t)\, e^{-st}\, dt
$$

En el dominio discreto las integrales pasan a ser **sumatorias**, la $f(t)$ pasa a ser $x(n)$ y el $e^{-st}$ pasa a ser $z^{-n}$ [13:36]. Más adelante aparece el paralelo entre multiplicar por $e^{-as}$ en Laplace y multiplicar por $z^{-a}$ (desplazamiento lateral).
- [14:38] **$z$ es una variable compleja**, igual que la $s$: $n$ toma valores naturales, $z$ toma valores complejos y se representa en el plano.
- [15:12] Igual que en Laplace existe la **antitransformada Z**, que lleva $X(z)$ a su $x(n)$.
- [16:13] Igual que en Laplace hay una **tabla** de pares $x(n) \leftrightarrow X(z)$ que se puede usar en el parcial; algunas entradas se deducen en clase por definición.

<details>
<summary>📝 Ejercicio 1 — [16:45]: transformada Z del impulso unitario</summary>

Hallar $\mathcal{Z}\left[\delta(n)\right]$ por definición.

<details>
<summary>Ver resolución</summary>

**Paso 1:** reemplazar en la definición la $x(n)$ genérica por $\delta(n)$:

$$
\mathcal{Z}\left[\delta(n)\right] = \sum_{n=0}^{\infty} \delta(n)\, z^{-n}
$$

**Paso 2:** desarrollar la sumatoria término a término [17:51]. Para $n = 0$ el impulso vale 1 y queda $1 \cdot z^{-0}$; para $n = 1$ vale 0 y el $z^{-1}$ se anula, y lo mismo pasa con todos los términos desde $n = 1$ [18:23]:

$$
\mathcal{Z}\left[\delta(n)\right] = 1\cdot z^{0} + 0\cdot z^{-1} + 0\cdot z^{-2} + \dots = 1
$$

**Resultado:** $\mathcal{Z}\left[\delta(n)\right] = 1$. Coincide con Laplace, donde la transformada del impulso también es 1 [18:54] (en cambio la del escalón ya no se parece).

</details>

</details>

## Suma de la serie geométrica — [19:24]

Concepto de Análisis 1 que se usa todo el tiempo: una **progresión geométrica** es una del tipo $a^n$ ($a$ es la **razón**). Su suma:

$$
S = \sum_{n=0}^{\infty} a^n = 1 + a + a^2 + a^3 + \dots
$$

**Deducción** [19:57]: multiplicar miembro a miembro por la razón $a$,

$$
aS = a + a^2 + a^3 + a^4 + \dots
$$

y restar [20:59]: se cancelan todos los términos menos el 1, que no tiene contraparte,

$$
S - aS = 1 \quad\Rightarrow\quad S(1 - a) = 1
$$

$$
\boxed{\sum_{n=0}^{\infty} a^n = \frac{1}{1-a} \qquad \text{si } |a| < 1}
$$

- La condición $|a| < 1$ es la de convergencia [22:02]. Con razón 1, por ejemplo, la suma se va sumando sin parar y **diverge** [22:33].
- Ejemplo con $a = \frac{1}{2}$ [23:05]:

$$
\sum_{n=0}^{\infty} \left(\frac{1}{2}\right)^n = 1 + \frac{1}{2} + \frac{1}{4} + \frac{1}{8} + \dots = \frac{1}{1 - \frac{1}{2}} = 2
$$

<details>
<summary>📝 Ejercicio 2 — [24:07]: transformada Z del escalón unitario</summary>

Hallar $\mathcal{Z}\left[u(n)\right]$ por definición, con su región de convergencia.

<details>
<summary>Ver resolución</summary>

**Paso 1:** definición con $x(n) = u(n) = 1$ [24:41]; pasar la potencia negativa al denominador:

$$
\mathcal{Z}\left[u(n)\right] = \sum_{n=0}^{\infty} 1 \cdot z^{-n} = \sum_{n=0}^{\infty} \left(\frac{1}{z}\right)^n
$$

**Paso 2:** es una serie geométrica de razón $a = \frac{1}{z}$, así que

$$
\mathcal{Z}\left[u(n)\right] = \frac{1}{1 - \frac{1}{z}} = \frac{z}{z-1}
$$

(sacando denominador común $z$; las dos expresiones son la misma) [25:28].

**Paso 3 — región de convergencia:** el resultado solo vale si el módulo de la razón es menor que 1:

$$
\left|\frac{1}{z}\right| < 1 \quad\Leftrightarrow\quad |z| > 1
$$

[25:59] Esto es la **región de convergencia**: los valores de $z$ para los que converge la transformada. Como $z$ es complejo, $|z| > 1$ son todos los puntos del plano **por afuera de la circunferencia de radio 1, sin el borde** (por eso se dibuja punteada) [26:31].

**Resultado:**

$$
\mathcal{Z}\left[u(n)\right] = \frac{z}{z-1}, \qquad |z| > 1
$$

Ya no se parece al $1/s$ de Laplace, y aparece el concepto de región de convergencia, que en general sale de la condición sobre la razón de la serie geométrica [27:05].

</details>

</details>

<details>
<summary>📝 Ejercicio 3 — [27:41]: transformada Z de una progresión geométrica general $a^n$</summary>

Hallar $\mathcal{Z}\left[a^n\right]$ con $a \in \mathbb{R}$, $a \ne 0$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** llevar la definición a "algo elevado a la $n$" [28:13]:

$$
\mathcal{Z}\left[a^n\right] = \sum_{n=0}^{\infty} a^n z^{-n} = \sum_{n=0}^{\infty} \left(\frac{a}{z}\right)^n
$$

**Paso 2:** serie geométrica de razón $\frac{a}{z}$ [28:43]:

$$
\mathcal{Z}\left[a^n\right] = \frac{1}{1 - \frac{a}{z}} = \frac{z}{z-a}
$$

**Paso 3 — región de convergencia:** siempre hay que localizar la razón (aparece en la sumatoria y en el primer paso del resultado) [29:15]:

$$
\left|\frac{a}{z}\right| < 1 \quad\Leftrightarrow\quad |z| > |a|
$$

Es como la del escalón pero con circunferencia de radio $|a|$ en vez de 1.

**Resultado:**

$$
\mathcal{Z}\left[a^n\right] = \frac{z}{z-a}, \qquad |z| > |a|
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 4 — [29:47]: secuencia finita dada por partes</summary>

Hallar la transformada Z de (función "inventada", no está en ninguna tabla):

$$
x(n) = \begin{cases} 2 & n = 0 \\ n & 1 \le n \le 3 \\ 1 & n = 4 \\ 0 & \text{en otro caso} \end{cases}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** hacerse un grafiquito [30:19]: vale 2 en $n = 0$; 1, 2 y 3 en $n = 1, 2, 3$; 1 en $n = 4$; 0 para todo lo demás. Hay solo 5 puntos no nulos.

**Paso 2:** como no está en tabla, por definición [30:55]; al haber solo 5 términos no nulos se escribe la suma completa [31:26]:

$$
X(z) = 2z^{0} + 1\cdot z^{-1} + 2z^{-2} + 3z^{-3} + 1\cdot z^{-4}
$$

Eso **ya es la transformada** [31:57].

**Paso 3:** escribirla "más linda" [32:27]:

$$
X(z) = 2 + \frac{1}{z} + \frac{2}{z^2} + \frac{3}{z^3} + \frac{1}{z^4}
$$

o con denominador común $z^4$:

$$
X(z) = \frac{2z^4 + z^3 + 2z^2 + 3z + 1}{z^4}
$$

Son maneras distintas de escribir lo mismo; en las respuestas de la guía aparecen estas dos últimas.

</details>

</details>

<details>
<summary>📝 Ejercicio 5 — [32:57]: $x(n) = 5$ si $n$ par, $0$ si $n$ impar</summary>

Hallar la transformada Z de

$$
x(n) = \begin{cases} 5 & n \text{ par} \\ 0 & n \text{ impar} \end{cases}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** por definición, escribir algunos términos (el 0 se considera par) [33:29]; las impares se anulan y solo sobreviven las pares [34:00]:

$$
X(z) = 5z^{0} + 0\cdot z^{-1} + 5z^{-2} + 0\cdot z^{-3} + 5z^{-4} + \dots
$$

**Paso 2:** forma genérica con $n = 2k$ (los pares) [34:30]:

$$
X(z) = \sum_{k=0}^{\infty} 5\, z^{-2k}
$$

**Paso 3:** llevarlo a serie geométrica [35:04]: el 5 no depende de $k$ y sale afuera; lo demás se escribe como algo a la $k$:

$$
X(z) = 5 \sum_{k=0}^{\infty} \left(\frac{1}{z^2}\right)^k
$$

**Paso 4:** aplicar $\frac{1}{1 - \text{razón}}$ y sacar denominador común [35:34]:

$$
X(z) = 5 \cdot \frac{1}{1 - \frac{1}{z^2}} = \frac{5z^2}{z^2 - 1}
$$

**Paso 5 — región de convergencia** [36:04]: $\left|\frac{1}{z^2}\right| < 1$, o sea

$$
|z| > 1
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 6 — [36:04]: una expresión para los pares y otra para los impares (ejercicio "bastante de parcial")</summary>

Hallar la transformada Z y su región de convergencia de

$$
x(n) = \begin{cases} 2\cdot 3^{-n} & n \text{ par} \\ \left(\frac{1}{2}\right)^n & n \text{ impar} \end{cases}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** por definición, alternando las ramas [36:36]: $n = 0$ entra por la de pares, $n = 1$ por la de impares, y así:

$$
X(z) = 2\cdot 3^{-0} z^{-0} + \left(\frac{1}{2}\right)^1 z^{-1} + 2\cdot 3^{-2} z^{-2} + \left(\frac{1}{2}\right)^3 z^{-3} + \dots
$$

**Paso 2:** forma genérica, con una sumatoria para los pares ($n = 2k$) y otra para los impares ($n = 2k+1$) [37:37]–[38:08]:

$$
X(z) = 2\sum_{k=0}^{\infty} 3^{-2k} z^{-2k} + \sum_{k=0}^{\infty} \left(\frac{1}{2}\right)^{2k+1} z^{-(2k+1)}
$$

**Paso 3 — pares:** escribir cada factor como algo a la $k$ y juntarlos (mismo exponente) [38:41]–[41:16]:

$$
3^{-2k} = \left(\frac{1}{9}\right)^k, \qquad z^{-2k} = \left(\frac{1}{z^2}\right)^k \quad\Rightarrow\quad 2\sum_{k=0}^{\infty} \left(\frac{1}{9z^2}\right)^k
$$

**Paso 4 — impares:** el "+1" del exponente sobra y hay que sacarlo afuera como constante (con los impares "siempre tienen algún pasito extra") [39:42]–[40:15]:

$$
\left(\frac{1}{2}\right)^{2k+1} z^{-(2k+1)} = \frac{1}{2}\cdot\frac{1}{z}\cdot\left(\frac{1}{4}\right)^k \left(\frac{1}{z^2}\right)^k
\quad\Rightarrow\quad
\frac{1}{2z}\sum_{k=0}^{\infty} \left(\frac{1}{4z^2}\right)^k
$$

($\frac{1}{2z}$ no depende de $k$, por eso sale de la sumatoria) [41:16].

**Paso 5:** ya son dos series geométricas; aplicar el resultado a cada una [41:47]:

$$
X(z) = 2\cdot\frac{1}{1 - \frac{1}{9z^2}} + \frac{1}{2z}\cdot\frac{1}{1 - \frac{1}{4z^2}}
$$

**Paso 6:** expresarlo "más lindo" [42:19]. En la parte impar siempre sobra algo con $z$ que se simplifica (el cuadrado con la $z$, el 4 con el 2) [42:50]:

$$
X(z) = \frac{18z^2}{9z^2 - 1} + \frac{2z}{4z^2 - 1}
$$

**Paso 7 — regiones de convergencia** de cada sumatoria (módulo de la razón menor que 1) [45:27]:

$$
\left|\frac{1}{9z^2}\right| < 1 \;\Rightarrow\; |9z^2| > 1 \;\Rightarrow\; |z|^2 > \frac{1}{9} \;\Rightarrow\; |z| > \frac{1}{3}
$$

$$
\left|\frac{1}{4z^2}\right| < 1 \;\Rightarrow\; |z| > \frac{1}{2}
$$

**Paso 8 — región de toda la $X(z)$:** la **intersección** de las dos [45:58]–[47:01]: los $z$ por fuera de las dos circunferencias, o sea por fuera de la más grande:

$$
|z| > \frac{1}{2}
$$

</details>

</details>

## Región de convergencia de toda la $X(z)$ — [44:24]

- Los ejercicios suelen pedir "hallar la transformada Z **y la región de convergencia**". Siempre que se trabaja con series geométricas hay que hallarla (no en las secuencias de puntitos sueltos) [44:57].
- La razón de cada serie se lee en la sumatoria (lo que queda elevado a la $k$) o en el primer paso del resultado ($\frac{1}{1 - \text{razón}}$); se impone **$|\text{razón}| < 1$** y se despeja $|z|$ [45:27].
- [45:58] Si $X(z)$ tiene varias sumatorias (p. ej. pares e impares), la región de convergencia de toda la $X(z)$ es la **intersección** de las regiones de cada una. Como todas son del tipo $|z| > R$ (exteriores de circunferencias concéntricas), la intersección es **siempre la región de la circunferencia más grande** [47:01]:

$$
|z| > \max(R_1, R_2, \dots)
$$

## Tabla de transformadas Z — [47:35]

Algunas se deducen en clase, otras se toman de la tabla. La tercera columna es el radio $R$ de la región de convergencia $|z| > R$ [51:12].

| $x(n)$, $n \ge 0$ | $X(z)$ | $R$ | Comentario en clase |
|---|---|---|---|
| $\delta(n)$ | $1$ | $0$ [ayudamemoria] | Ejercicio 1 |
| $\delta(n-m)$ (impulso corrido) | $z^{-m}$ | — | "No me acuerdo si hay algún ejercicio donde se use" |
| $u(n) = 1$ | $\dfrac{z}{z-1}$ | $1$ | Ejercicio 2 |
| $n$ | $\dfrac{z}{(z-1)^2}$ | $1$ | Ejercicio 8 |
| $n^2$ | $\dfrac{z(z+1)}{(z-1)^3}$ | $1$ | Ejercicio 8 |
| $a^n$ | $\dfrac{z}{z-a}$ | $\lvert a\rvert$ | Ejercicio 3 |
| $n\,a^n$ | $\dfrac{az}{(z-a)^2}$ [ayudamemoria] | $\lvert a\rvert$ | La nombra sin desarrollar |
| $(n+1)\,a^n$ | [fórmula no dictada] | — | La nombra en la tabla de la clase; no está en el ayudamemoria |
| $\cos(an)$ | $\dfrac{z\,(z - \cos a)}{z^2 - 2z\cos a + 1}$ [ayudamemoria] | $1$ | "Feas"; salen de escribir el coseno en forma exponencial y meterlo en la definición |
| $\mathrm{sen}(an)$ | $\dfrac{z\,\mathrm{sen}\, a}{z^2 - 2z\cos a + 1}$ [ayudamemoria] | $1$ | Un solo ejercicio usa el seno |
| $\dfrac{a^n}{n!}$ | [fórmula no dictada] | — | Hay un ejercicio en la práctica del martes; no está en el ayudamemoria |
| $e^{-an}$ | $\dfrac{z}{z - e^{-a}}$ [ayudamemoria] | $e^{-a}$ | No la nombra en clase |

**Cómo se usa** [48:38]–[49:08]: igual que en Laplace, en las dos direcciones. Si hay que transformar una $n^2$, se entra por la fila de $n^2$; si al antitransformar aparece algo de la forma $\frac{z}{z-a}$, se sabe que viene de $a^n$.

Además hay una **segunda tabla, de desplazamientos laterales** [49:08], de referencia para los ejercicios (ver más abajo).

## Propiedad de linealidad — [49:38]

"La primera, la más fácil, la más querida y la más usada", igual que en Laplace [50:09]:

$$
\mathcal{Z}\left[\alpha\, x(n) + \beta\, y(n)\right] = \alpha\, X(z) + \beta\, Y(z)
$$

<details>
<summary>📝 Ejercicio 7 — [50:41]: $x(n) = 3(-2)^n - 2\cdot 5^n$ por linealidad y tabla</summary>

Hallar la transformada Z y la región de convergencia de

$$
x(n) = 3\,(-2)^n - 2\cdot 5^n
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** linealidad:

$$
X(z) = 3\,\mathcal{Z}\left[(-2)^n\right] - 2\,\mathcal{Z}\left[5^n\right]
$$

**Paso 2:** tabla, fila $a^n \to \frac{z}{z-a}$, con $a = -2$ y con $a = 5$ [51:12]:

$$
X(z) = 3\cdot\frac{z}{z+2} - 2\cdot\frac{z}{z-5}
$$

**Paso 3 — región de convergencia:** de la tercera columna, $|z| > |a|$ para cada término [51:45]: $|z| > 2$ y $|z| > 5$. Son dos circunferencias concéntricas; la intersección es lo exterior a la más grande [52:18]:

$$
|z| > 5
$$

</details>

</details>

## Desplazamiento a derecha — [52:18]

- A diferencia de Laplace (donde una sola fórmula servía para correr a izquierda o a derecha), **en Z desplazar a derecha y desplazar a izquierda son propiedades distintas** [52:50].
- Restar en la variable corre la función a la derecha; sumar la corre a la izquierda (vale tanto para continuas como para discretas) [53:53].
- Es el análogo de la segunda traslación de Laplace [53:21]: si $f(t-a)$ es la función corrida $a$ unidades, su transformada es $F(s)\,e^{-as}$. En Z, en vez de multiplicar por $e^{-as}$ se multiplica por $z^{-a}$:

$$
\mathcal{Z}\left[x(n-1)\right] = z^{-1} X(z)
$$

$$
\mathcal{Z}\left[x(n-a)\right] = z^{-a} X(z)
$$

- **Interpretación gráfica** [54:25]: correr la señal 3 unidades a la derecha es mover todo el bloque de "palitos" 3 lugares a la derecha, y eso es $z^{-3}X(z)$ [54:57].

## Desplazamiento a izquierda — [55:28]

**Interpretación gráfica** [56:00]: al correr la señal (por ejemplo) 2 unidades a la izquierda, todos los palitos se mueven 2 lugares. Pero el dominio de $x(n)$ son los naturales con el 0: **no admite $n$ negativos**, así que los valores que quedan del lado de los $n$ negativos **hay que descartarlos (restarlos)** [56:32]. Eso es lo que hace que la propiedad se vea distinta [57:03]:

$$
\mathcal{Z}\left[x(n+1)\right] = z\,X(z) - z\,x(0)
$$

$$
\mathcal{Z}\left[x(n+2)\right] = z^2 X(z) - z^2 x(0) - z\,x(1)
$$

- **Paralelo con la derivada de Laplace** [57:35]: $\mathcal{L}[y'] = sY(s) - y(0)$ y $\mathcal{L}[y''] = s^2 Y(s) - s\,y(0) - y'(0)$ [58:07]. En Z aparece una $z$ extra: donde estaba $y(0)$ queda $z\,x(0)$; donde estaba $s\,y(0)$ queda $z^2 x(0)$; donde estaba $y'(0)$ queda $z\,x(1)$. **El desplazamiento a izquierda está asociado a las derivadas.**
- Nunca se piden más de 2 unidades a izquierda [58:38]. La forma general [ayudamemoria]:

$$
\mathcal{Z}\left[x(n+a)\right] = z^a \left(X(z) - x(0) - x(1)z^{-1} - x(2)z^{-2} - \dots - x(a-1)z^{-a+1}\right)
$$

- **Por qué se restan esos términos** [59:10]–[1:01:16], con la de 2 unidades distribuida:
  - $z^2 X(z)$ es toda la función corrida 2 lugares a la izquierda.
  - $z^2 x(0)$: el palito que estaba en $n = 0$, corrido 2 lugares, queda en $n = -2$ (por eso el $z^2$); al restarlo, se va [1:00:14].
  - $z\,x(1)$: el palito que estaba en $n = 1$ queda en $n = -1$ (por eso $z^1$); al restarlo, se va [1:00:46].
  - Solo sobreviven los palitos desde el tercero de los originales.
- Por eso, así como las ecuaciones diferenciales se resolvían transformando miembro a miembro con la propiedad de las derivadas, las **ecuaciones en diferencias** se resuelven transformando miembro a miembro con el **desplazamiento a izquierda** [1:01:48].

## Multiplicación por $n$ — [1:02:18]

Análogo a la multiplicación por $t$ de Laplace ($-F'(s)$), pero con una $z$ extra:

$$
\mathcal{Z}\left[n\,x(n)\right] = -z\,\frac{dX(z)}{dz}
$$

- Para $n^2$, $n^3$, …: se toma el resultado de $\mathcal{Z}[n\,x(n)]$, **se vuelve a derivar y se vuelve a multiplicar por $-z$**, y así sucesivamente [1:02:49]–[1:03:21].
- En clase se dicta como generalización "$(-z)^k$ por la derivada de orden $k$ de $X(z)$" [1:03:21]. Ojo (nota del apunte, no del profe): aplicado al pie de la letra eso no coincide con iterar el operador; para $n^2$ lo correcto es aplicar $-z\frac{d}{dz}$ dos veces, que es como se calcula en el Ejercicio 8.
- Solo se trabaja con $n$ o $n^2$ [1:03:21].

<details>
<summary>📝 Ejercicio 8 — [1:03:52]: transformadas de $n$ y de $n^2$ con la multiplicación por $n$</summary>

Deducir las entradas de tabla $\mathcal{Z}[n]$ y $\mathcal{Z}[n^2]$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** $n = n\cdot u(n)$ (el escalón vale 1), así que se parte de $\mathcal{Z}[u(n)] = \frac{z}{z-1}$ y, como se multiplica por $n$, se deriva y se multiplica por $-z$ [1:03:52]:

$$
\mathcal{Z}\left[n\right] = -z\,\frac{d}{dz}\left(\frac{z}{z-1}\right)
$$

**Paso 2:** "hacen las cuentitas" [1:04:28] (desarrolladas acá; en clase solo se da el resultado):

$$
\frac{d}{dz}\left(\frac{z}{z-1}\right) = \frac{(z-1) - z}{(z-1)^2} = \frac{-1}{(z-1)^2}
\quad\Rightarrow\quad
\mathcal{Z}\left[n\right] = \frac{z}{(z-1)^2}
$$

**Paso 3:** $n^2 = n\cdot n\,u(n)$: se toma la transformada de $n$ recién hallada, se vuelve a derivar y a multiplicar por $-z$ [1:04:28]:

$$
\mathcal{Z}\left[n^2\right] = -z\,\frac{d}{dz}\left(\frac{z}{(z-1)^2}\right)
$$

**Paso 4:** cuentas (desarrolladas acá) [1:05:04]:

$$
\frac{d}{dz}\left(\frac{z}{(z-1)^2}\right) = \frac{(z-1)^2 - 2z(z-1)}{(z-1)^4} = \frac{-z-1}{(z-1)^3}
\quad\Rightarrow\quad
\mathcal{Z}\left[n^2\right] = \frac{z(z+1)}{(z-1)^3}
$$

**Resultado:** las dos coinciden con la tabla y tienen región de convergencia $|z| > 1$ [1:05:36].

</details>

</details>

## Resumen de los desplazamientos laterales — [1:05:36]

La segunda tablita resume las propiedades de desplazamiento, ordenadas de izquierda a derecha [1:06:06]: los desplazamientos a izquierda ($x(n+2)$, $x(n+1)$: los que "se corresponden con las derivadas" y se usan en las ecuaciones en diferencias), la $x(n)$ sin desplazar ($X(z)$) y los desplazamientos a derecha ($x(n-1)$, $x(n-2)$, …: multiplicar por $z^{-1}$, $z^{-2}$, …).

## Antitransformada Z — [1:06:38]

- Mismo concepto que en Laplace: se aplica a una función de $z$ y se vuelve a $x(n)$. Pero las maneras de antitransformar "están muy reducidas" (en Laplace hay más cintura) [1:07:09]. Dos caminos:
  1. **Tabla directa**, para los casos fáciles: por ejemplo $\frac{z}{z-5}$ se parece a $\frac{z}{z-a}$, entonces su antitransformada es $5^n$.
  2. **Fracciones simples** [1:07:41], igual que en Laplace, con una pequeña diferencia (dejar una $z$ afuera).
- La **linealidad** también vale para la antitransformada y es la única propiedad que importa acá [1:08:12].

**El truco: dejar una $z$ afuera** [1:08:44]–[1:09:14]: antes de hacer fracciones simples se saca una $z$ como factor y las fracciones simples se hacen sobre lo que queda; después se distribuye esa $z$.

**Por qué** [1:10:46]–[1:11:49]: en la tabla **todas** las transformadas (las de cociente de polinomios) tienen una $z$ en el numerador. Si se hacen fracciones simples sin dejar la $z$ afuera, quedan términos $\frac{A}{z-1}$, $\frac{B}{z-3}$ que no están en la tabla. Distribuyendo la $z$ que quedó afuera aparecen los $\frac{z}{z-a}$ de la tabla.

**Alternativa (que "nunca se hace, pero que se puede")** [1:12:21]: si quedó un término sin $z$ en el numerador, multiplicar y dividir por $z$. Queda la $z$ en el numerador y sobra un $z^{-1}$, que es un **desplazamiento a derecha** de una unidad: se antitransforma lo que tiene la $z$ y se escribe en función de $n - 1$ en vez de $n$ [1:12:52]. Se llega al mismo resultado.

<details>
<summary>📝 Ejercicio 9 — [1:08:44]: antitransformar por fracciones simples dejando una $z$ afuera</summary>

Hallar la antitransformada Z de

$$
X(z) = \frac{z^2 + 2z}{(z-1)(z-3)}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** dejar una $z$ afuera [1:09:14]:

$$
X(z) = z\cdot\frac{z+2}{(z-1)(z-3)}
$$

**Paso 2:** fracciones simples de lo que quedó ("salen la A y la B con el truquito"):

$$
\frac{z+2}{(z-1)(z-3)} = \frac{A}{z-1} + \frac{B}{z-3}, \qquad A = -\frac{3}{2}, \quad B = \frac{5}{2}
$$

**Paso 3:** distribuir la $z$ que quedó afuera [1:09:44]:

$$
X(z) = -\frac{3}{2}\cdot\frac{z}{z-1} + \frac{5}{2}\cdot\frac{z}{z-3}
$$

**Paso 4:** antitransformadas directas por tabla [1:10:16]: $\frac{z}{z-1}$ es el escalón y $\frac{z}{z-3}$ es $3^n$:

$$
x(n) = -\frac{3}{2}\,u(n) + \frac{5}{2}\cdot 3^n
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 10 — [1:13:24]: antitransformar $X(z) = \dfrac{1}{(z-1)^2}$ (ejercicio 5f de la guía)</summary>

Hallar la antitransformada Z de

$$
X(z) = \frac{1}{(z-1)^2}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** no hay $z$ en el numerador y no hay fracciones simples con las que dejar una $z$ afuera, así que acá **es obligatorio** multiplicar por $z$ y por $z^{-1}$ [1:13:55]:

$$
X(z) = z^{-1}\cdot\frac{z}{(z-1)^2}
$$

**Paso 2:** por tabla, $\frac{z}{(z-1)^2}$ es la transformada de $n$ [1:14:29].

**Paso 3:** el $z^{-1}$ es un desplazamiento a derecha de una unidad: en vez de $n$ queda la $n$ corrida, $n - 1$, que toma valor a partir de $n = 1$; en $n = 0$ vale 0 [1:15:00]:

$$
x(n) = \begin{cases} 0 & n = 0 \\ n - 1 & n \ge 1 \end{cases}
$$

</details>

</details>

## Ecuaciones en diferencias — [1:15:31]

- Así como Laplace se usa para resolver ecuaciones diferenciales, la Z se usa para resolver **ecuaciones en diferencias**: lo mismo, pero en dominios discretos [1:16:01]. En Matemática Discreta se ven como **relaciones de recurrencia** con un desarrollo más largo [1:17:07].
- **Mecánica:**
  1. Transformar miembro a miembro (linealidad).
  2. En vez de la propiedad de las derivadas, usar el **desplazamiento a izquierda**.
  3. Despejar $X(z)$, dejarla solita.
  4. Antitransformar todo el resto, en general con **fracciones simples** (dejando una $z$ afuera).
- Notación: $a_n$ y $x(n)$, $a_{n+1}$ y $x(n+1)$ son lo mismo [1:16:33].
- [1:19:12] Al despejar $X(z)$ hay dos opciones: juntar todo con denominador común y después pasar dividiendo, o **pasar dividiendo a cada término por separado**. En primer orden conviene lo segundo, porque quedan antitransformadas directas.
- **Verificación** [1:20:47]: la ecuación es una recurrencia que permite calcular los términos uno por uno desde los valores iniciales; la fórmula cerrada obtenida tiene que dar lo mismo para cualquier $n$. Con eso se chequea el resultado [1:22:52]. (En la práctica del martes se trabaja, por ejemplo, con Fibonacci: la fórmula cerrada da el término 523 sin calcular todos los anteriores.)

<details>
<summary>📝 Ejercicio 11 — [1:16:33]: ecuación en diferencias de primer orden $x(n+1) - x(n) = 7$, $x(0) = 3$</summary>

Hallar la sucesión $x(n)$ que cumple

$$
a_{n+1} - a_n = 7, \qquad a_0 = 3
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** transformar miembro a miembro [1:17:39]; el 7 es $7\,u(n)$:

$$
\mathcal{Z}\left[x(n+1)\right] - \mathcal{Z}\left[x(n)\right] = 7\,\mathcal{Z}\left[u(n)\right]
$$

**Paso 2:** desplazamiento a izquierda y tabla [1:18:09]:

$$
z\,X(z) - z\,x(0) - X(z) = 7\cdot\frac{z}{z-1}
$$

**Paso 3:** reemplazar $x(0) = 3$ y sacar factor común $X(z)$ [1:18:39]:

$$
X(z)\,(z - 1) - 3z = \frac{7z}{z-1}
$$

**Paso 4:** pasar el $z - 1$ dividiendo **a cada término por separado** [1:19:12]:

$$
X(z) = \frac{7z}{(z-1)^2} + \frac{3z}{z-1}
$$

**Paso 5:** antitransformadas directas [1:19:45]: $\frac{z}{(z-1)^2} \to n$ y $\frac{z}{z-1} \to u(n)$:

$$
x(n) = 7n + 3\,u(n) = 7n + 3
$$

**Paso 6 — verificación** [1:20:47]–[1:22:52]: la ecuación dice $x(n+1) = x(n) + 7$ (el siguiente es el anterior más 7). Desde $x(0) = 3$:

$$
x(1) = 3 + 7 = 10, \qquad x(2) = 10 + 7 = 17, \qquad x(3) = 17 + 7 = 24
$$

Con la fórmula: $x(3) = 7\cdot 3 + 3 = 24$. Coincide.

</details>

</details>

## Ecuaciones en diferencias de segundo orden — [1:23:25]

- Equivalentes a las ecuaciones diferenciales de segundo orden: en vez de derivadas segundas aparece $x(n)$ desplazada dos unidades a la izquierda, $x(n+2)$.
- Igual que en las EDO de segundo orden, hacen falta **dos condiciones iniciales**: $x(0)$ y $x(1)$ [1:23:58].
- Acá sí conviene juntar todo el segundo miembro en un solo cociente ("el choclazo"), porque hay que pasar dividiendo un polinomio de segundo grado y después hacer fracciones simples [1:24:58].
- [1:26:02] En general las raíces del denominador ("polos", en el lenguaje de sistemas estables) son **reales** (simples o dobles, como en este ejemplo). Si aparecen raíces complejas conjugadas, es lo mismo que en Laplace pero con $Az + B$ en vez del $As + B$ de siempre.

<details>
<summary>📝 Ejercicio 12 — [1:23:58]: $x(n+2) - 4x(n+1) + 3x(n) = -2$, $x(0) = 7$, $x(1) = 12$</summary>

Resolver la ecuación en diferencias

$$
x(n+2) - 4x(n+1) + 3x(n) = -2, \qquad x(0) = 7, \quad x(1) = 12
$$

(En [1:24:58] la transcripción dice "$x$ en 1 vale 2", pero en [1:28:40] el profe dice que el dato es $x(1) = 12$ y la verificación da 12.)

<details>
<summary>Ver resolución</summary>

**Paso 1:** transformar miembro a miembro con el desplazamiento de dos unidades, el de una unidad, la transformada directa de $x(n)$ y la del escalón para el $-2$ [1:24:28]–[1:24:58]:

$$
\left[z^2 X(z) - z^2 x(0) - z\,x(1)\right] - 4\left[z\,X(z) - z\,x(0)\right] + 3X(z) = -2\cdot\frac{z}{z-1}
$$

**Paso 2:** reemplazar $x(0) = 7$, $x(1) = 12$ y despejar $X(z)$. El polinomio que multiplica a $X(z)$ es $z^2 - 4z + 3 = (z-1)(z-3)$ (raíces reales y distintas), y al juntar todo el segundo miembro en un solo cociente el denominador queda $(z-1)^2 (z-3)$ [1:25:30]. El numerador no se dicta [paso en el pizarrón, ver video]; haciendo el álgebra (cuenta del apunte, consistente con los coeficientes que da el profe en el paso siguiente):

$$
X(z)\,(z-1)(z-3) = 7z^2 - 16z - \frac{2z}{z-1}
\quad\Rightarrow\quad
X(z) = \frac{z\left(7z^2 - 23z + 14\right)}{(z-1)^2\,(z-3)}
$$

**Paso 3:** dejar una $z$ afuera y hacer fracciones simples con una raíz doble [1:26:35]–[1:27:08]:

$$
X(z) = z\left[\frac{A}{(z-1)^2} + \frac{B}{z-1} + \frac{C}{z-3}\right]
$$

$A$ y $C$ salen con el truquito; $B$ obliga a plantear el sistemita [1:27:08]:

$$
A = 1, \qquad B = 5, \qquad C = 2
$$

**Paso 4:** distribuir la $z$ [1:27:38]:

$$
X(z) = \frac{z}{(z-1)^2} + 5\cdot\frac{z}{z-1} + 2\cdot\frac{z}{z-3}
$$

**Paso 5:** antitransformar por tabla [1:28:10]: $n$, $5$ veces el escalón y $2$ veces $3^n$:

$$
x(n) = n + 5 + 2\cdot 3^n
$$

**Paso 6 — verificación con los datos** [1:28:40]–[1:29:44]:

$$
x(1) = 1 + 5 + 2\cdot 3^1 = 12 \;\checkmark \qquad x(0) = 0 + 5 + 2\cdot 3^0 = 7 \;\checkmark
$$

"Tienen que tener muchísima mala suerte para que les dé de casualidad iguales de los dos métodos."

</details>

</details>

---

_Apunte generado el 2026-10-02 desde la transcripción local (Whisper) de la clase teórica grabada de Transformada Z. Fórmulas marcadas [ayudamemoria] tomadas de `fuentes/AYUDAMEMORIA-OFICIAL.pdf` (pág. 2)._
