# Aplicaciones de la transformada de Laplace (clase grabada)

> Fuente: fuentes/clases/Transformadas de Laplace/P_TLaplace.mp4 (transcripción local con Whisper)

---

> **Cómo usar este apunte.** Es la clase donde el profe aplica todo lo de Laplace
> (transformadas, antitransformadas, fracciones simples) a **ecuaciones diferenciales,
> sistemas de EDO, convolución, ecuaciones integrales y evaluación de integrales
> impropias**. Los ejercicios son de la guía práctica; su resolución manuscrita completa
> está en el OneNote (`fuentes/clases/Transformadas de Laplace/Transformada de Laplace.pdf`,
> citado `[OneNote p. N]`) y en `04-practica-transformada-laplace.md`. Acá se prioriza el
> **razonamiento oral** del profe. Los timestamps `[mm:ss]` son del video local (sin enlace
> público). Las fórmulas se reconstruyeron solo donde lo dictado no deja dudas.

## Índice

- [00:00] — Ecuaciones diferenciales con Laplace: la idea
- [02:36] — El método de los tres pasos
- [02:36] — 📝 Ejercicio 1: $y'' + 9y = 0$ (ejemplo corto)
- [07:30] — 📝 Ejercicio 2 (guía, ej. 8 a): $2x'' + 7x' + 3x = 6$ con condiciones nulas
- [14:51] — Sistemas de ecuaciones diferenciales
- [15:54] — 📝 Ejercicio 3 (guía, ej. 9 b): sistema $x' = x - y$, $y' = 2x + 4y$ por sustitución
- [20:13] — Regla de Cramer para el sistema transformado
- [20:45] — 📝 Ejercicio 4: el mismo 9 b por Cramer
- [25:55] — Ojo con la notación sin $(t)$
- [27:29] — Teorema de convolución (teorema de Borel)
- [29:02] — 📝 Ejercicio 5: $\mathcal{L}\left[\int_0^t e^{u} e^{2(t-u)}\,du\right]$
- [30:46] — 📝 Ejercicio 6 (guía, ej. 10): $\mathcal{L}\left[\int_0^t u\cos u \, e^{t-u}\,du\right]$
- [33:26] — Convolución para antitransformar: cuándo conviene y a quién darle el $t-u$
- [34:27] — 📝 Ejercicio 7 (guía, ej. 11 a): antitransformar $\frac{6}{(s+1)(s^2+4)}$ por convolución
- [41:51] — Ecuaciones integrales e íntegro-diferenciales
- [42:25] — 📝 Ejercicio 8 (guía, ej. 12 a): $y(t) + 4\int_0^t (t-u)^2 y(u)\,du = t^2$
- [52:29] — Resumen del método y consultas
- [55:05] — Factorizar y cancelar antes de fracciones simples
- [56:06] — Evaluación de integrales impropias con la definición de Laplace
- [58:44] — 📝 Ejercicio 9: $\int_0^\infty t^2 e^{-2t}\,dt$
- [1:00:18] — 📝 Ejercicio 10: $\int_{-\infty}^{\infty} \frac{\operatorname{sen} t}{t}\,dt$
- [1:04:31] — Propiedad de división por $t$ y la condición del límite
- [1:08:42] — 📝 Ejercicio 11 (guía, ej. 13 d): $\int_0^\infty \frac{e^{-3t} - e^{-6t}}{t}\,dt$
- [1:16:04] — Cierre: qué ya es nivel parcial

## Lo que el profe remarca

**Sobre el parcial y el final (qué se toma)**

- **[00:31]** Lo de la clase anterior (transformadas y antitransformadas sueltas) no era todavía nivel parcial/final: era "una partecita de un todo un poquito más grande", que es lo de esta clase. Pero toda la complejidad algebraica ya está practicada.
- **[14:17]** "Es casi seguro que entre el ejercicio de transformada de Laplace o el de sistemas estables [...] en el parcial o en el final, **alguna ecuación diferencial sí o sí** van a tener que resolver". Tema muy importante.
- **[14:51]**–**[15:24]** El **sistema de ecuaciones diferenciales** "creo que lo tomaron hace poco en un final o en un recuperatorio".
- **[1:04:00]**–**[1:04:31]** La propiedad de **división por $t$** "en este tipo de ejercicios se toma bastante" (con $\operatorname{sen} t / t$ o exponenciales sobre $t$).
- **[1:08:42]** El ejercicio $\int_0^\infty \frac{e^{-3t}-e^{-6t}}{t}\,dt$ "se toma mucho [...] lo he visto bastante". **[1:16:04]** Si no es con 3 y 6, lo vio con 4 y 8; a veces da $\ln 2$, a veces $\ln 3$, pero los pasos son los mismos: "es un ejercicio tomable".
- **[1:16:04]** "Hoy ya vimos ejercicios que son de parcial": los de integrales por definición y las ecuaciones diferenciales, integrales e íntegro-diferenciales.
- **[1:07:09]** La **transformada de Fourier** se ve solo como introducción a Laplace "y después no se toma".

**Sobre el método**

- **[03:41]** "Todos los ejercicios arrancan así": **transformada de Laplace miembro a miembro** (salvo alguna distributiva muy sencilla antes, **[08:00]**–**[08:30]**).
- **[02:36]**–**[03:11]** Es clave que den las **condiciones iniciales**; si no las dan, se trabaja con constantes genéricas ($K$, $H$).
- **[16:28]** La **cantidad de condiciones iniciales** depende del orden: con derivada segunda, dos condiciones por función; con derivada primera, una por función.
- **[07:30]** La dificultad está en la **antitransformada** (fracciones simples); "todo lo demás va a ser muy parecido siempre". **[53:00]** En "el 99 % de los casos" hay que usar fracciones simples.
- **[20:45]**, **[25:24]** Para el sistema transformado vale **cualquier método** (sustitución, igualación, sumas y restas, Cramer). El profe recomienda **Cramer** porque evita operar "con choclos muy grandes".
- **[25:24]**–**[25:55]** "Supongo que esto no te lo despeja una calculadora": la calculadora sirve cuando las incógnitas son números, no funciones. Hay que resolverlo **a mano**.
- **[33:56]**–**[34:27]** La convolución se usa sobre todo para **transformar** integrales. Para **antitransformar**, "me parece más fácil" fracciones simples (la integral de convolución puede complicarse). Usen convolución si la consigna lo pide.
- **[37:05]**–**[37:36]** Criterio para el $t-u$: dárselo a la **exponencial**, porque las exponenciales "son un poquito más manejables" que las trigonométricas en las integrales.
- **[41:51]**, **[45:05]** "Esto es donde más vamos a usar convolución": en las **ecuaciones integrales** (no para antitransformar).
- **[45:36]** **Ruffini** "vamos a usar muchísimo" en las próximas clases.
- **[49:13]** Sacarse de encima **todas las incógnitas que se pueda** (con el truco de tapar) **antes** de armar el sistema de fracciones simples: lo que parecía un 3×3 queda en dos ecuaciones independientes.

**Errores típicos**

- **[10:36]**–**[11:07]** Al factorizar $as^2+bs+c$ **hay que sacar afuera el coeficiente principal**: $a(s-r_1)(s-r_2)$. La calculadora o la resolvente dan las raíces ($-3$ y $-\tfrac12$ en el ej. 8 a), pero el $2$ hay que sacarlo; "si no, el resultado de fracciones simples no les va a dar bien". **[12:10]**–**[12:41]** No es por ser múltiplo de nada: es regla general.
- **[26:27]**–**[26:57]** En el ejercicio de parcial o final que se tomó hace poco escribieron $x' = x - y$, $y' = 2x + 4y$ **sin el $(t)$**, y "la gente lo volvió bastante loca": pensaron que las incógnitas eran números. Si aparecen $x'$ y $x$, es una ecuación diferencial y las incógnitas son **funciones**.
- **[1:09:45]**, **[1:10:15]**–**[1:11:22]** División por $t$: **chequear que exista** $\lim_{t\to 0} f(t)/t$. El "primer impulso" de separar $\frac{e^{-3t}-e^{-6t}}{t}$ en dos integrales con $1/t$ no sirve: $\lim_{t\to0} 1/t$ no existe. "No vayan por ahí porque no van a llegar a nada".
- **[1:13:58]** Al aplicar Barrow en $\infty$ con logaritmos queda $\infty - \infty$: se salva juntando los logaritmos en uno solo.

## Ecuaciones diferenciales con Laplace: la idea — [00:00]

- Una **ecuación diferencial** es una ecuación cuya incógnita es una función $y(t)$ y que relaciona funciones con sus derivadas [01:02].
- **Ventaja de Laplace** [01:02]–[02:06]: gracias a las propiedades de la transformada de las **derivadas**, la ecuación diferencial en el dominio del tiempo se transforma en una **ecuación algebraica** en el dominio de Laplace. Ahí ya no se trabaja con derivadas: se **despeja $Y(s)$** y, cuando tiene una forma fácil de antitransformar, se antitransforma para volver a la $y(t)$ buscada.
- Se ven **ecuaciones diferenciales**, **ecuaciones integrales** e **íntegro-diferenciales** (un mix de las dos), y "siempre se resuelven de la misma manera" [02:06]–[02:36].

## El método de los tres pasos — [02:36]

**Paso 1 — Transformada de Laplace miembro a miembro** [03:41], usando linealidad y las transformadas de las derivadas [04:12]–[04:48], [08:30]–[09:01]:

$$
\mathcal{L}[y'(t)] = sY(s) - y(0)
$$

$$
\mathcal{L}[y''(t)] = s^2 Y(s) - s\,y(0) - y'(0)
$$

y se reemplazan las **condiciones iniciales** [05:19].

**Paso 2 — Despejar $Y(s)$** [05:51]: dejarla sola de un lado, sacando factor común y pasando lo demás al otro miembro, hasta la forma "más cómoda posible".

**Paso 3 — Antitransformar** [06:24]: casi siempre por **fracciones simples** (lo de la clase anterior), y se llega a $y(t)$.

> El profe usa la propiedad con la notación genérica del enunciado ($y'$, $f'$, $x'$): "siempre lo mismo es $s^2$ por la transformada de la función menos $s$ por la función evaluada en cero menos la derivada evaluada en cero" [04:12]–[04:48]. Que en la ecuación queden $Y(s)$ sueltas "está bien": es la incógnita en el lado de Laplace [04:48].

<details>
<summary>📝 Ejercicio 1 — 02:36: y'' + 9y = 0 (ejemplo corto para ordenar los pasos)</summary>

Resolver

$$
y''(t) + 9\,y(t) = 0
$$

con las condiciones iniciales que da el enunciado (de los reemplazos que se dictan: $y(0) = 0$, $y'(0) = 2$).

<details>
<summary>Ver resolución</summary>

**Paso 1:** transformada miembro a miembro [03:41]–[04:48]:

$$
s^2 Y(s) - s\,y(0) - y'(0) + 9\,Y(s) = 0
$$

**Paso 2:** reemplazar las condiciones iniciales [05:19]:

$$
s^2 Y(s) - s\cdot 0 - 2 + 9\,Y(s) = 0
$$

**Paso 3:** despejar: pasar el $2$ sumando y sacar factor común $s^2 + 9$ [05:51]–[06:24]:

$$
Y(s) = \frac{2}{s^2 + 9}
$$

**Paso 4:** antitransformar. Acá no hacen falta fracciones simples: viene del seno de $3t$, así que se divide y multiplica por $3$ y "me sobra este dos tercios" [06:24]–[06:59]:

$$
Y(s) = \frac{2}{3}\cdot\frac{3}{s^2 + 9} \quad\Longrightarrow\quad y(t) = \frac{2}{3}\operatorname{sen}(3t)
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 2 — 07:30: guía, ej. 8 a — 2x'' + 7x' + 3x = 6 con x(0) = 0, x'(0) = 0</summary>

Resolver por transformada de Laplace [08:00] (también en [OneNote p. 15–16]):

$$
2x''(t) + 7x'(t) + 3x(t) = 6, \qquad x(0) = 0,\quad x'(0) = 0
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** transformada miembro a miembro [08:30]–[09:01]. Aparece por primera vez la transformada de la derivada primera, multiplicada por $7$ por linealidad; la de $6$ es $6/s$:

$$
2\left[s^2X(s) - s\,x(0) - x'(0)\right] + 7\left[sX(s) - x(0)\right] + 3X(s) = \frac{6}{s}
$$

**Paso 2:** agrupar con factor común $X(s)$; todos los términos de condiciones iniciales se anulan porque son nulas [09:31]:

$$
X(s)\left(2s^2 + 7s + 3\right) = \frac{6}{s}
$$

**Paso 3:** despejar [10:03]:

$$
X(s) = \frac{6}{s\,(2s^2 + 7s + 3)}
$$

**Paso 4 — factorizar sacando el coeficiente principal** [10:36]–[11:07]: las raíces de $2s^2+7s+3$ son $-3$ y $-\tfrac12$, pero el $2$ se saca afuera y se simplifica con el $6$:

$$
2s^2 + 7s + 3 = 2\,(s+3)\left(s+\tfrac12\right) \quad\Longrightarrow\quad X(s) = \frac{3}{s\,(s+3)\left(s+\tfrac12\right)}
$$

**Paso 5:** tres raíces **reales y simples** ($0$, $-3$, $-\tfrac12$) [11:38]:

$$
\frac{3}{s\,(s+3)\left(s+\tfrac12\right)} = \frac{A}{s} + \frac{B}{s+3} + \frac{C}{s+\tfrac12}
$$

**Paso 6:** coeficientes con el "truquito" de tapar (repaso) [12:10], [12:41]–[13:11]: para $A$, el valor que anula su denominador es $0$; se tapa el factor $s$ y se evalúa el resto en $0$:

$$
A = \frac{3}{(0+3)\left(0+\tfrac12\right)} = \frac{3}{3/2} = 2
$$

"Y así se hace con los otros" [13:11]: $B = \tfrac25$, $C = -\tfrac{12}{5}$ [13:43] [cuentas en el pizarrón, ver video; también en OneNote p. 15].

**Paso 7:** reescribir y antitransformar (tres términos "súper fáciles") [13:43]–[14:17]:

$$
X(s) = \frac{2}{s} + \frac{2}{5}\cdot\frac{1}{s+3} - \frac{12}{5}\cdot\frac{1}{s+\tfrac12}
$$

$$
x(t) = 2 + \frac{2}{5}\,e^{-3t} - \frac{12}{5}\,e^{-\frac12 t}
$$

</details>

</details>

## Sistemas de ecuaciones diferenciales — [14:51]

- No hay teoría extra [15:24]: la metodología es la misma (Laplace miembro a miembro) y se suma la complejidad de **resolver un sistema** cuyas incógnitas son **funciones** ($X(s)$, $Y(s)$), no números.
- Se puede resolver con **el método que quieran** [15:54]. El profe lo hizo primero por **sustitución** ("un poquito engorroso") y después por **Cramer**, "que es lo que recomienda la guía".
- Cantidad de condiciones iniciales [16:28]: una por función si hay derivadas primeras; dos por función si hay derivadas segundas.
- **Inevitable** [23:52]: tomen el método que tomen, se llega a una $X(s)$ (y una $Y(s)$) que hay que antitransformar por **fracciones simples**.

<details>
<summary>📝 Ejercicio 3 — 15:54: guía, ej. 9 b — sistema x' = x − y, y' = 2x + 4y por sustitución</summary>

Resolver (enunciado según [26:27] y [OneNote p. 18]):

$$
\begin{cases} x'(t) = x(t) - y(t) \\ y'(t) = 2x(t) + 4y(t) \end{cases} \qquad x(0) = -1,\quad y(0) = 0
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Laplace miembro a miembro en cada ecuación [16:59]:

$$
sX(s) - x(0) = X(s) - Y(s) \qquad (1)
$$

$$
sY(s) - y(0) = 2X(s) + 4Y(s) \qquad (2)
$$

con $x(0) = -1$ e $y(0) = 0$.

**Paso 2:** de la ecuación (2) despejar $X(s)$ (pasar todo al otro lado y dividir por $2$) [17:30], [19:09]:

$$
X(s) = \frac12\,(s-4)\,Y(s)
$$

**Paso 3:** reemplazar en (1) y operar ("la parte engorrosa": factor común, dejar $Y(s)$ sola) [18:01] [paso en el pizarrón, ver video]. Se llega a:

$$
Y(s) = \frac{-2}{s^2 - 5s + 6}
$$

**Paso 4:** fracciones simples con raíces reales y simples [18:38] (el denominador es $(s-2)(s-3)$, como confirma en [22:20]; en el audio dice "menos 2 y 2" [poco claro en la transcripción]) y antitransformar:

$$
y(t) = -2\,e^{3t} + 2\,e^{2t}
$$

**Paso 5:** volver a la fórmula $X(s) = \tfrac12 (s-4)\,Y(s)$ con la $Y(s)$ hallada [19:09]–[19:43]; con denominador común queda "un choclo medio feo" pero, operado bien, da algo simple:

$$
X(s) = \frac{-s + 4}{(s-3)(s-2)}
$$

**Paso 6:** fracciones simples (otra vez raíces reales y simples), antitransformar y llegar a $x(t)$ [20:13]. El resultado no se dicta; en [OneNote p. 19]: $x(t) = e^{3t} - 2e^{2t}$.

</details>

</details>

## Regla de Cramer para el sistema transformado — [20:13]

- Siempre arranca igual: Laplace miembro a miembro [20:45]. Después se **reacomoda** cada ecuación como "algo por $X(s)$ + algo por $Y(s)$ = términos independientes" [20:45]–[21:17].
- Con eso se arman la **matriz de coeficientes** y la de **términos independientes** [21:17].
- $\Delta$ = determinante de la matriz de coeficientes (en $2\times2$: "este por este menos este por este") [21:49].
- $\Delta_X$: en $\Delta$, se reemplaza la **columna de la $X$** (la primera) por los términos independientes; $\Delta_Y$: lo mismo en la **columna de la $Y$** (la segunda) [22:51], [24:23].

$$
X(s) = \frac{\Delta_X}{\Delta}, \qquad Y(s) = \frac{\Delta_Y}{\Delta}
$$

<details>
<summary>📝 Ejercicio 4 — 20:45: el mismo ej. 9 b resuelto por Cramer</summary>

Mismo sistema del Ejercicio 3, reordenado para Cramer.

<details>
<summary>Ver resolución</summary>

**Paso 1:** reacomodar las ecuaciones transformadas (coeficientes que dicta en [21:49]; términos independientes $-1$ y $0$ [22:51]):

$$
\begin{cases} (s-1)\,X(s) + 1\cdot Y(s) = -1 \\ -2\,X(s) + (s-4)\,Y(s) = 0 \end{cases}
$$

**Paso 2:** determinante de coeficientes [21:49]–[22:20]:

$$
\Delta = \begin{vmatrix} s-1 & 1 \\ -2 & s-4 \end{vmatrix} = (s-1)(s-4) + 2 = (s-2)(s-3)
$$

Es el mismo denominador $s^2 - 5s + 6$ al que se había llegado por sustitución [22:20].

**Paso 3:** $\Delta_X$, con la primera columna reemplazada por $(-1, 0)$ [22:51]–[23:22]. (En la diapositiva había un error de signo que el profe corrige en vivo: $-1\cdot(s-4) = -s+4$ [23:22].)

$$
\Delta_X = \begin{vmatrix} -1 & 1 \\ 0 & s-4 \end{vmatrix} = -s + 4 \quad\Longrightarrow\quad X(s) = \frac{-s+4}{(s-2)(s-3)}
$$

Son las mismas fracciones simples que por sustitución [23:52].

**Paso 4:** $\Delta_Y$, con la segunda columna reemplazada por $(-1, 0)$; "incluso más fácil" porque $-1\cdot 0$ se anula [24:23]–[24:54]:

$$
\Delta_Y = \begin{vmatrix} s-1 & -1 \\ -2 & 0 \end{vmatrix} = -2 \quad\Longrightarrow\quad Y(s) = \frac{-2}{(s-2)(s-3)}
$$

**Paso 5:** fracciones simples, antitransformar y llegar a $y(t)$ [24:54] (mismo resultado que en el Ejercicio 3).

</details>

</details>

## Ojo con la notación sin $(t)$ — [25:55]

- En un ejercicio de parcial/final reciente el sistema se escribió $x' = x - y$, $y' = 2x + 4y$, **sin el $(t)$** [25:55]–[26:27], y muchos creyeron que las incógnitas eran números.
- Si aparecen $x'$ y $x$, se está hablando de ecuaciones diferenciales, y ahí las incógnitas son **funciones** [26:57].

## Teorema de convolución (teorema de Borel) — [27:29]

Relaciona el **producto de dos transformadas** con una integral en el dominio del tiempo [27:29]–[28:31]. Si $f(t) = \mathcal{L}^{-1}[F(s)]$ y $g(t) = \mathcal{L}^{-1}[G(s)]$:

$$
\mathcal{L}^{-1}\left[F(s)\,G(s)\right] = \int_0^t f(u)\,g(t-u)\,du
$$

y, leído al revés [29:02]:

$$
\mathcal{L}\left[\int_0^t f(u)\,g(t-u)\,du\right] = F(s)\,G(s)
$$

- La $g$ se evalúa en $t-u$: hay un **corrimiento** [28:31].
- Se usa $u$ en vez de $t$ solo porque la $t$ aparece en el límite de integración; "la función es la misma" [28:31].
- **Al transformar**, el $t-u$ "no nos tiene que preocupar": se lee como si fuera $u$ (o $t$) [29:33]–[30:04]. Hay que **identificar** cuál es la $g(t-u)$ (todo lo que tiene $t-u$) y cuál la $f(u)$ (lo que solo tiene $u$): "ahí no hay demasiado para elegir" [31:17].
- En la guía se trabaja en los dos sentidos: transformar y antitransformar [30:04].

<details>
<summary>📝 Ejercicio 5 — 29:02: transformada de ∫₀ᵗ eᵘ e^{2(t−u)} du</summary>

Hallar

$$
\mathcal{L}\left[\int_0^t e^{u}\, e^{2(t-u)}\,du\right]
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** identificar $f(u) = e^{u}$ y $g(t-u) = e^{2(t-u)}$, que se piensa como $e^{2u}$ (o $e^{2t}$): el corrimiento no importa al transformar [29:33]–[30:04].

**Paso 2:** el resultado es el producto de las transformadas [30:04]:

$$
\mathcal{L}\left[\int_0^t e^{u}\, e^{2(t-u)}\,du\right] = \frac{1}{s-1}\cdot\frac{1}{s-2}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 6 — 30:46: guía, ej. 10 — transformada de ∫₀ᵗ u cos(u) e^{t−u} du</summary>

Hallar con el teorema de convolución [30:46] (también en [OneNote p. 19–20]):

$$
\mathcal{L}\left[\int_0^t u\cos(u)\, e^{t-u}\,du\right]
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** identificar las funciones [31:17]–[31:51]:

$$
f(u) = u\cos u, \qquad g(t-u) = e^{t-u}
$$

**Paso 2:** transformada de $u\cos u$ con la propiedad de **multiplicación por $t^n$** ($n = 1$): derivar una vez la transformada del coseno y cambiar el signo una vez [31:51]–[32:21]:

$$
\mathcal{L}[\cos u] = \frac{s}{s^2+1} \quad\Longrightarrow\quad \mathcal{L}[u\cos u] = -\frac{d}{ds}\left(\frac{s}{s^2+1}\right) = \frac{s^2 - 1}{(s^2+1)^2}
$$

**Paso 3:** $e^{t-u}$ se piensa como $e^{t}$ (o $e^{u}$) [32:54]:

$$
G(s) = \frac{1}{s-1}
$$

**Paso 4:** producto y simplificación: $s^2 - 1 = (s+1)(s-1)$ es diferencia de cuadrados y se cancela el $s-1$ [32:54]–[33:26]:

$$
F(s)\,G(s) = \frac{s^2-1}{(s^2+1)^2}\cdot\frac{1}{s-1} = \frac{s+1}{(s^2+1)^2}
$$

</details>

</details>

## Convolución para antitransformar: cuándo conviene y a quién darle el $t-u$ — [33:26]

- La forma que más se trabaja es la de **transformar** una integral [33:26].
- **Antitransformar con convolución "no se usa mucho"** [33:56]: obliga a **resolver la integral** de convolución, que puede complicarse [34:27]. Esos mismos ejercicios salen con **fracciones simples**, que al profe le resulta más fácil; si les aparece en el medio de un ejercicio, elijan. En la práctica se usa convolución porque la consigna lo pide.
- **Cómo se hace** [35:01]–[36:03]:
  - Elegir $F(s)$ y $G(s)$: vienen "bastante obligadas" por los **factores del denominador**; las **constantes** se reparten como quieran (el profe le tira toda la constante a uno de los factores).
  - Antitransformar cada una para obtener $f$ y $g$.
  - Armar la integral. Los nombres $f$ y $g$ se pueden intercambiar [37:05]; lo que importa es el **criterio de a qué función darle el $t-u$**, porque puede facilitar o complicar la integral ("tiene que ver un poquito con la experiencia, con el ojo").
  - **Conviene darle el $t-u$ a la exponencial**, porque las exponenciales son más manejables que las trigonométricas en las integrales [37:36]. La otra asignación también es válida y tiene que dar el mismo resultado [38:07]–[38:38].

<details>
<summary>📝 Ejercicio 7 — 34:27: guía, ej. 11 a — antitransformar 6/((s+1)(s²+4)) por convolución</summary>

Antitransformar usando convolución (ítem a del ejercicio de la guía; en [OneNote p. 20–21] es el ej. 11 a):

$$
Y(s) = \frac{6}{(s+1)(s^2+4)}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** elegir $F$ y $G$ según los factores del denominador [35:01]–[36:03]. Se podría repartir $6$ y $1$, o $3$ y $2$ (este último "quizás convenga", porque $\frac{2}{s^2+4}$ ya es el seno de $2t$). El profe tomó:

$$
F(s) = \frac{6}{s+1}, \qquad G(s) = \frac{1}{s^2+4}
$$

**Paso 2:** antitransformar cada una [36:03]–[36:34]:

$$
f(t) = 6\,e^{-t}, \qquad g(t) = \frac12\operatorname{sen}(2t)
$$

**Paso 3:** armar la integral dándole el $t-u$ a la **exponencial** [37:36]; el $3$ sale de $6\cdot\tfrac12$:

$$
y(t) = 3\int_0^t e^{-(t-u)}\operatorname{sen}(2u)\,du
$$

(También vale $y(t) = 3\int_0^t e^{-u}\operatorname{sen}\big(2(t-u)\big)\,du$ y tiene que dar lo mismo [38:07].)

**Paso 4:** separar la exponencial, $e^{-(t-u)} = e^{-t}e^{u}$, y sacar $e^{-t}$ afuera de la integral porque no depende de $u$ (una de las razones para darle el $t-u$) [38:38]–[39:11]:

$$
y(t) = 3\,e^{-t}\int_0^t e^{u}\operatorname{sen}(2u)\,du
$$

**Paso 5:** primitiva de la **tabla de integrales** y Barrow [39:11]–[40:14]. En $t$: cambiar todas las $u$ por $t$. En $0$: $e^0 = 1$, $\operatorname{sen} 0 = 0$, $-2\cos 0 = -2$:

$$
y(t) = 3\,e^{-t}\left[\frac15\,e^{u}\big(\operatorname{sen}(2u) - 2\cos(2u)\big)\right]_0^t = 3\,e^{-t}\left[\frac15\,e^{t}\big(\operatorname{sen}(2t) - 2\cos(2t)\big) - \frac15\cdot(-2)\right]
$$

**Paso 6:** distributiva; donde $e^{-t}e^{t} = 1$ se cancela la exponencial [40:14]–[40:48]:

$$
y(t) = \frac35\operatorname{sen}(2t) - \frac65\cos(2t) + \frac65\,e^{-t}
$$

**Comentario** [40:48]–[41:51]: por fracciones simples tiene que dar lo mismo. Ahí aparecen raíces complejas conjugadas $\pm 2j$ (el término $\frac{Bs+C}{s^2+4}$). En los ítems b y c de ese ejercicio hay raíces complejas conjugadas **dobles** $\pm j$, y el planteo de fracciones simples se vuelve "un poquito más engorroso".

</details>

</details>

## Ecuaciones integrales e íntegro-diferenciales — [41:51]

- **Ecuación integral (de tipo convolutorio)** [42:25]–[42:56]: la incógnita $y(t)$ aparece también dentro de una integral $\int_0^t (\ldots)(t-u)\,(\ldots)(u)\,du$. Se reconoce la forma del teorema de convolución: integral de $0$ a $t$, una función de $t-u$, otra de $u$, $du$. "Lo primero que van a pensar es convolución".
- **Ecuación íntegro-diferencial** [42:56]: si además aparece una derivada ($y'$, $y''$). "No complica la dificultad mucho" [43:27]: es combinar la convolución con la transformada de las derivadas [43:59].
- Mismo procedimiento: Laplace miembro a miembro (la integral se transforma como **producto** de transformadas), despejar $Y(s)$, antitransformar (casi siempre por fracciones simples) [44:32], [52:29]–[53:00].

<details>
<summary>📝 Ejercicio 8 — 42:25: guía, ej. 12 a — y(t) + 4∫₀ᵗ (t−u)² y(u) du = t²</summary>

Resolver la ecuación integral (también en [OneNote p. 22–23]):

$$
y(t) + 4\int_0^t (t-u)^2\, y(u)\,du = t^2
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** Laplace miembro a miembro [43:59]–[44:32]: $y(t) \to Y(s)$, $t^2 \to \frac{2}{s^3}$. "La estrella del ejercicio" es la transformada de la integral: con $g(t-u) = (t-u)^2$ (pensada como $u^2$) y $f(u) = y(u)$, es el producto $\frac{2}{s^3}\,Y(s)$ [44:32]–[45:05]:

$$
Y(s) + 4\cdot\frac{2}{s^3}\,Y(s) = \frac{2}{s^3}
$$

**Paso 2:** agrupar y despejar ("una vez que cancelo, que agrupo") [45:05] [paso en el pizarrón, ver video]:

$$
Y(s) = \frac{2}{s^3 + 8}
$$

**Paso 3:** naturaleza de las raíces [45:36]: $-2$ es raíz real simple ($(-2)^3 + 8 = 0$), y queda un par de complejas conjugadas. Para factorizar, **Ruffini** con $-2$ sobre los coeficientes $1, 0, 0, 8$ [46:08]–[47:09]: bajar el $1$; $1\cdot(-2) = -2$, $0 + (-2) = -2$; $(-2)(-2) = 4$, $0 + 4 = 4$; $4\cdot(-2) = -8$, $8 - 8 = 0$ (tenía que dar $0$):

$$
s^3 + 8 = (s+2)\left(s^2 - 2s + 4\right)
$$

**Paso 4:** planteo de fracciones simples (raíz real simple + cuadrático con complejas conjugadas) [47:41]:

$$
\frac{2}{(s+2)(s^2-2s+4)} = \frac{A}{s+2} + \frac{Bs + C}{s^2 - 2s + 4}
$$

**Paso 5:** $A$ con el truquito [47:41]:

$$
A = \frac16
$$

**Paso 6:** con $A$ ya conocida, denominador común e igualar al numerador $2$ [48:12]:

$$
\frac16\left(s^2 - 2s + 4\right) + (Bs + C)(s+2) = 2
$$

Elegir los términos que convienen [48:12]–[48:42]. En $s^2$ (del otro lado no hay $s^2$) y en el término independiente:

$$
\frac16 + B = 0 \;\Rightarrow\; B = -\frac16, \qquad \frac23 + 2C = 2 \;\Rightarrow\; C = \frac23
$$

"Esto no es un sistema de ecuaciones": $B$ y $C$ quedaron en dos ecuaciones independientes [49:13].

**Paso 7:** reescribir para antitransformar [49:46]–[50:54]. Pasa lo mismo que la clase anterior: el denominador tiene un **desplazamiento** ($s^2 - 2s + 4 = (s-1)^2 + 3$) que no está en el numerador. Se hace aparecer $s-1$ arriba y se **compensa**, teniendo en cuenta que el $+1$ queda multiplicado por $-\tfrac16$; al $\tfrac23$ original hay que restarle ese $\tfrac16$:

$$
Y(s) = \frac16\cdot\frac{1}{s+2} - \frac16\cdot\frac{s-1}{(s-1)^2 + 3} + \left(\frac23 - \frac16\right)\frac{1}{(s-1)^2 + 3}
$$

**Paso 8:** antitransformar [50:54]–[52:29]. Lo "un poquito más feo": $a^2 = 3$, así que $a = \sqrt3$ [50:54]–[51:25]. El primer término va a la exponencial; el segundo, al coseno de $\sqrt3\,t$; el tercero, al seno, haciendo aparecer $\sqrt3$ y compensando (queda $\frac{1}{2\sqrt3}$). Los dos últimos van multiplicados por $e^{t}$ porque todo está en $s-1$:

$$
y(t) = \frac16\,e^{-2t} - \frac16\,e^{t}\cos\left(\sqrt3\,t\right) + \frac{1}{2\sqrt3}\,e^{t}\operatorname{sen}\left(\sqrt3\,t\right)
$$

</details>

</details>

## Resumen del método y consultas — [52:29]

- Para ecuaciones diferenciales, integrales o íntegro-diferenciales, el procedimiento es siempre el mismo [52:29]–[53:00]: **Laplace miembro a miembro → agrupar y dejar sola $Y(s)$ → antitransformar** (en el 99 % de los casos con fracciones simples). "Se vuelve bastante mecánico", pero no por eso es menos importante.
- Es "la gran utilidad" de Laplace: resolver ecuaciones diferenciales o integrales que aparecen en fenómenos físicos [53:00]–[53:30].
- **Consulta** [53:30]–[54:34]: los apuntes de esta clase no están en el aula virtual, pero los ejercicios salen de la **práctica** (en "clases online"). Ahí está el 9 b solo por sustitución (no por Cramer) y hay más convoluciones y ejercicios que completa en la clase siguiente.

## Factorizar y cancelar antes de fracciones simples — [55:05]

- Otra cosa que puede complicar **antes** de la antitransformada: aplicar Ruffini y **cancelar** lo que corresponda [55:05].
- Hay un ejercicio "medio jodido" donde, si no se cancela u opera convenientemente, queda un sistema de $6\times6$ [55:05]–[55:36]: no es difícil (4 de las incógnitas dan $0$ "y es muy obvio"), pero es muy largo. Si operan bien, llegan al resultado [55:36]–[56:06].

## Evaluación de integrales impropias con la definición de Laplace — [56:06]

- "Interesante y útil aplicación": calcular rápido integrales impropias cuya resolución analítica sería extensa, tediosa o hasta imposible por no existir la primitiva [56:06]–[56:36].
- Acá se usa la **definición** de la transformada [56:36]–[57:06]:

$$
F(s) = \mathcal{L}[f(t)] = \int_0^\infty f(t)\,e^{-st}\,dt
$$

- **Razonamiento del profe** [57:06]–[58:13]: si donde dice $e^{-st}$ ponen un número (por ejemplo $4$), la integral da $F(4)$. Si ponen $0$, $e^{-0t} = 1$ y queda $\int_0^\infty f(t)\,dt = F(0)$. En general, **siempre que la integral exista**:

$$
\int_0^\infty f(t)\,e^{-at}\,dt = F(a) = \mathcal{L}[f(t)]\Big|_{s=a}
$$

- El signo menos del exponente "viene fijo": el valor que se evalúa es el número que acompaña a $-t$ [59:17].

<details>
<summary>📝 Ejercicio 9 — 58:44: ∫₀^∞ t² e^{−2t} dt</summary>

Calcular (en [OneNote p. 25] es el ej. 13 c):

$$
\int_0^\infty t^2\, e^{-2t}\,dt
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** se podría buscar la primitiva en la tabla y hacer Barrow con el límite en infinito, pero por la definición es "mucho más rápido" [58:44].

**Paso 2:** con $f(t) = t^2$ y $s = 2$, la integral es $F(2)$ [59:17]:

$$
F(s) = \mathcal{L}[t^2] = \frac{2}{s^3}
$$

**Paso 3:** evaluar en $2$ [59:47]:

$$
\int_0^\infty t^2\, e^{-2t}\,dt = F(2) = \frac{2}{8} = \frac14
$$

"Esto sale en dos patadas" [59:47].

</details>

</details>

<details>
<summary>📝 Ejercicio 10 — 1:00:18: ∫ de −∞ a ∞ de sen(t)/t dt</summary>

Calcular

$$
\int_{-\infty}^{\infty} \frac{\operatorname{sen} t}{t}\,dt
$$

La función **no tiene primitiva elemental** [1:00:18] (capaz el resultado está en la tabla de integrales, por ser muy conocida, pero se ve de dónde sale).

<details>
<summary>Ver resolución</summary>

**Paso 1 — pasar a $[0, \infty)$** [1:00:49]–[1:02:55]: la definición de Laplace va de $0$ a $\infty$. $\frac{\operatorname{sen} t}{t}$ es **par** (es un seno que se va amortiguando, espejado a izquierda y derecha; o: cociente de dos funciones impares). Como en Series de Fourier, en un intervalo simétrico se calcula una rama y se multiplica por $2$:

$$
\int_{-\infty}^{\infty} \frac{\operatorname{sen} t}{t}\,dt = 2\int_0^\infty \frac{\operatorname{sen} t}{t}\,dt
$$

**Paso 2 — ¿dónde está la exponencial?** [1:02:55]–[1:03:27]: si no aparece es porque vale $1$, o sea que $s = 0$:

$$
\int_0^\infty \frac{\operatorname{sen} t}{t}\,e^{-0\cdot t}\,dt = F(0), \qquad F(s) = \mathcal{L}\left[\frac{\operatorname{sen} t}{t}\right]
$$

**Paso 3 — propiedad de división por $t$** [1:04:00]–[1:05:01]: la transformada del seno es $\frac{1}{s^2+1}$; se escribe en $u$ y se integra entre $s$ e $\infty$:

$$
F(s) = \int_s^\infty \frac{1}{u^2 + 1}\,du
$$

**Paso 4:** la primitiva es el **arco tangente** (está en la tabla) [1:05:01]–[1:05:32]. Como $\arctan$ tiene asíntota $\frac{\pi}{2}$ en $+\infty$ [1:05:32]:

$$
F(s) = \arctan u\,\Big|_s^\infty = \frac{\pi}{2} - \arctan s
$$

**Paso 5:** evaluar en $0$; $\arctan 0 = 0$ [1:06:07]:

$$
\int_0^\infty \frac{\operatorname{sen} t}{t}\,dt = F(0) = \frac{\pi}{2}
$$

**Paso 6:** multiplicar por $2$ por la paridad [1:06:38]:

$$
\int_{-\infty}^{\infty} \frac{\operatorname{sen} t}{t}\,dt = \pi
$$

**Comentarios:** la condición de la división por $t$ no se chequeó en vivo y "debería haberlo chequeado": $\lim_{t\to0} \frac{\operatorname{sen} t}{t} = 1$ existe, así que vale [1:09:45]–[1:10:15]. En la guía teórica este ejemplo también se resuelve con la **transformada de Fourier** de un pulso (que da algo del estilo seno sobre $\omega$) y la definición de la antitransformada de Fourier, y llega a lo mismo, "porque el área es única" [1:07:09]–[1:08:11].

</details>

</details>

## Propiedad de división por $t$ y la condición del límite — [1:04:31]

$$
\mathcal{L}\left[\frac{f(t)}{t}\right] = \int_s^\infty F(u)\,du \qquad \text{siempre que exista } \lim_{t\to0}\frac{f(t)}{t}
$$

- $F$ es la transformada del **numerador**, expresada en la variable $u$ [1:04:31]–[1:05:01].
- La condición está en la teoría y **hay que chequearla** [1:09:45]. Con $\operatorname{sen} t / t$ el límite es $1$ y se puede aplicar [1:09:45]–[1:10:15]; con $1/t$ el límite no existe y **no** se puede aplicar [1:10:48].
- Es una propiedad que "en este tipo de ejercicios se toma bastante" [1:04:00].

<details>
<summary>📝 Ejercicio 11 — 1:08:42: guía, ej. 13 d — ∫₀^∞ (e^{−3t} − e^{−6t})/t dt</summary>

Calcular (ejercicio 13 d de la guía [1:16:34]; también en [OneNote p. 26–27]):

$$
\int_0^\infty \frac{e^{-3t} - e^{-6t}}{t}\,dt
$$

<details>
<summary>Ver resolución</summary>

**Paso 1 — el camino que NO va** [1:10:15]–[1:11:22]: separar en dos integrales y leer cada una como la transformada de $\frac1t$ evaluada en $3$ y en $6$. No se puede aplicar la división por $t$ a $f(t) = 1$, porque $\lim_{t\to0}\frac1t$ no existe.

**Paso 2 — factor común $e^{-3t}$** [1:11:22]–[1:11:52]: queda la definición de Laplace del cociente evaluada en $3$:

$$
\int_0^\infty e^{-3t}\,\frac{1 - e^{-3t}}{t}\,dt = \mathcal{L}\left[\frac{1 - e^{-3t}}{t}\right]\Bigg|_{s=3}
$$

**Paso 3 — chequear la condición** [1:11:52]–[1:12:25]: es $\frac00$; por L'Hôpital,

$$
\lim_{t\to0}\frac{1 - e^{-3t}}{t} = \lim_{t\to0}\frac{3\,e^{-3t}}{1} = 3
$$

El límite existe: se puede aplicar la división por $t$.

**Paso 4 — división por $t$** [1:12:25]–[1:12:57]: $\mathcal{L}[1] = \frac1s \to \frac1u$ y $\mathcal{L}[e^{-3t}] = \frac{1}{s+3} \to \frac{1}{u+3}$:

$$
\mathcal{L}\left[\frac{1 - e^{-3t}}{t}\right] = \int_s^\infty \left(\frac1u - \frac{1}{u+3}\right)du = \Big[\ln|u| - \ln|u+3|\Big]_s^\infty
$$

**Paso 5 — la indeterminación $\infty - \infty$** [1:13:28]–[1:15:00]: el logaritmo no tiene asíntota horizontal. Se junta todo en un logaritmo (resta de logaritmos = logaritmo del cociente); $\frac{u}{u+3} \to 1$ en el infinito (numerador y denominador lineales), así que el logaritmo tiende a $0$:

$$
\left[\ln\left|\frac{u}{u+3}\right|\right]_s^\infty = 0 - \ln\left|\frac{s}{s+3}\right| = \ln\left|\frac{s+3}{s}\right|
$$

(Dar vuelta el cociente es opcional: "lo pueden dejar con el negativo y está bien igual" [1:15:31].)

**Paso 6 — evaluar en $3$** (el $e^{-3t}$ que quedó afuera) [1:15:31]–[1:16:04]:

$$
\int_0^\infty \frac{e^{-3t} - e^{-6t}}{t}\,dt = \ln\frac{6}{3} = \ln 2
$$

</details>

</details>

## Cierre: qué ya es nivel parcial — [1:16:04]

- Este último ejercicio "se toma bastante", también con otros números (4 y 8), y puede dar $\ln 3$ en vez de $\ln 2$: los pasos son los mismos [1:16:04].
- "Hoy ya vimos ejercicios que son de parcial": integrales por definición, ecuaciones diferenciales, integrales e íntegro-diferenciales [1:16:04]–[1:16:34]. La práctica sigue el martes siguiente.

---

*Generado el 2026-10-02 a partir de `fuentes/clases/Transformadas de Laplace/P_TLaplace.mp4` (transcripción local con Whisper, `apuntes/transcripts/14-video-teorica-aplicaciones-laplace.json`, 77 min). Las fórmulas se reconstruyeron de lo dictado; donde el profe solo señala la diapositiva se marca `[paso en el pizarrón, ver video]`. Los enunciados y resultados no dictados se tomaron solo del OneNote de la práctica (`fuentes/clases/Transformadas de Laplace/Transformada de Laplace.pdf`), citado `[OneNote p. N]`.*
