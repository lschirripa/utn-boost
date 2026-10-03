# Transformada de Laplace, antitransformada y propiedades (clase teórica grabada)

> Fuente: fuentes/clases/Transformadas de Laplace/T_TLaplace.mp4 (transcripción local con Whisper)

---

> **Cómo usar este apunte.** Es la **teoría** de la unidad tal como la da el profe en la
> clase grabada (PDF de la cátedra con la tabla, un PDF propio con las propiedades
> "que vamos a usar" y una carilla de fracciones simples). La práctica está en
> `04-practica-transformada-laplace.md` (OneNote) y las aplicaciones (EDO, convolución,
> etc.) en `14-video-teorica-aplicaciones-laplace.md`. Los timestamps `[mm:ss]` son del
> video local (sin enlace público). Las fórmulas se reconstruyeron solo donde lo dictado
> no deja dudas; lo que se apoya en el ayudamemoria oficial (permitido en el parcial)
> va marcado `[ayudamemoria]`. **Esta clase NO desarrolla** cambio de escala,
> transformada de las integrales ni convolución: ver la sección final.

## Índice

- [00:00] — Por qué Laplace es el tema central del primer parcial
- [01:31] — Definición, dominio del tiempo y dominio de Laplace
- [03:06] — 📝 Ejercicio 1: $\mathcal{L}\{1\}$ por definición (y $\mathcal{L}\{t\}$)
- [05:13] — Se trabaja con tabla (pero hay que saber la definición)
- [06:15] — Tabla básica de transformadas
- [08:27] — Condiciones de existencia: seccionalmente continua y de orden exponencial
- [12:48] — Condiciones suficientes pero no necesarias: $1/\sqrt{t}$
- [13:50] — Uso de la tabla: $\cos 3t$
- [15:24] — Qué propiedades se ven (y cuáles están en el ayudamemoria)
- [16:59] — Propiedad A: linealidad
- [18:00] — 📝 Ejercicio 2: $\mathcal{L}\{4t^2 - 3\cos 2t + 5e^{-t}\}$
- [19:38] — 📝 Ejercicio 3: $\mathcal{L}\{3t - 5\,\mathrm{sen}\,4t + 8\}$
- [20:40] — Propiedad B: primera propiedad de la traslación
- [22:49] — 📝 Ejercicio 4: primera traslación ($\mathrm{sen}\,3t\,e^{-5t}$, $t\,e^{2t}$, $e^{at}$)
- [25:53] — Propiedad C: segunda propiedad de la traslación
- [29:42] — 📝 Ejercicio 5: seno desplazado 4 unidades
- [30:46] — Transformada de las derivadas
- [33:00] — 📝 Ejercicio 6: $\mathcal{L}\{3t^2\}$ a partir de $t^3$
- [34:34] — 📝 Ejercicio 7: $\mathcal{L}\{\cos 3t\}$ a partir de $\mathrm{sen}\,3t$
- [36:05] — Derivada segunda y derivada enésima
- [38:43] — Multiplicación por $t^n$
- [39:15] — 📝 Ejercicio 8: $\mathcal{L}\{t^2 e^{2t}\}$ por dos caminos
- [41:53] — 📝 Ejercicio 9: $\mathcal{L}\{t\,\mathrm{sen}\,3t\}$
- [43:30] — División por $t$ (con la condición del límite)
- [45:02] — 📝 Ejercicio 10: $\mathcal{L}\{\mathrm{sen}\,t / t\}$
- [48:10] — Teorema del valor inicial
- [50:15] — 📝 Ejercicio 11: TVI con $4e^{-3t}$
- [51:18] — Teorema del valor final
- [52:53] — 📝 Ejercicio 12: TVF con $4e^{-3t}$
- [55:29] — Función escalón unitario (Heaviside)
- [59:08] — Transformada del escalón
- [1:00:39] — Funciones partidas en un renglón con escalones
- [1:03:55] — 📝 Ejercicio 13 (guía, ej. 3 a): constante $1/a^2$ entre $0$ y $a$
- [1:08:10] — 📝 Ejercicio 14: la identidad prendida entre $1$ y $2$
- [1:17:48] — Función impulso unitario (delta de Dirac)
- [1:23:27] — 📝 Ejercicio 15: por qué $\mathcal{L}\{\delta(t)\} = 1$
- [1:29:20] — Antitransformada de Laplace: por tabla
- [1:32:26] — Propiedades de la antitransformada: linealidad
- [1:32:57] — 📝 Ejercicio 16: antitransformada por linealidad (multiplicar y dividir por una constante)
- [1:36:26] — Primera propiedad de la traslación para antitransformar
- [1:36:58] — 📝 Ejercicio 17: $\mathcal{L}^{-1}\{1/(s^2 - 2s + 5)\}$ completando cuadrados
- [1:39:02] — 📝 Ejercicio 18: $\mathcal{L}^{-1}\{6/(s+4)^3\}$
- [1:42:08] — Segunda propiedad de la traslación para antitransformar
- [1:42:41] — 📝 Ejercicio 19: $\mathcal{L}^{-1}\{e^{-\pi s/3}/(s^2+1)\}$
- [1:43:46] — Método de fracciones simples
- [1:46:55] — Los cuatro casos de fracciones simples
- [1:50:04] — 📝 Ejercicio 20: para qué sirven las fracciones simples al antitransformar
- — Propiedades del ayudamemoria que esta clase no desarrolla (escala, integrales, convolución)

## Lo que el profe remarca

**Sobre el parcial (qué se toma y cómo)**

- **[00:00]** Laplace es "el tema más importante de la primera parte de la materia", lo que va hasta el primer parcial; **[00:30]** sistemas estables usa todo Laplace y la transformada Z "es lo mismo" pero para funciones discretas.
- **[01:00]** A la transformada de Fourier "no le íbamos a dar muchas bolillas": el foco del curso es Laplace.
- **[05:13]**–**[06:15]** **No se calculan las integrales** para transformar: se usa la tabla (y al revés para antitransformar). Pero **sí hay que saber la definición**, porque "vamos a resolver algunos ejercicios a partir de la definición".
- **[15:24]**–**[15:54]** De las muchas propiedades de la guía teórica trae **solo las que se usan**; las otras "no la vamos a usar para ningún ejercicio nunca". La **tabla y las propiedades están en el resumen (ayudamemoria) que pueden usar en el parcial**. En sus parciales no va a pasar, pero en un final podría aparecer una propiedad que no se usa en la guía: con el machete "debería ser fácil" aplicarla.
- **[17:30]**, **[1:27:45]**–**[1:28:16]** Las **demostraciones no se piden**, "ni para final": están en el PDF "para que vean de dónde sale"; "no le importan a nadie en la materia".
- **[28:41]** La segunda propiedad de la traslación es "importante": se usa en otros ejercicios y hay **ejercicios de la guía** sobre esto.
- **[31:22]**–**[33:00]** La transformada de las derivadas es la propiedad "a la que la transformada de Laplace le debe la fama" (ecuaciones diferenciales → ecuaciones algebraicas). Se va a usar siempre en **forma genérica** ($sF(s) - f(0)$ con $f$ incógnita), no con funciones concretas.
- **[37:08]**–**[37:40]** La de la **derivada primera y segunda se usa "un montón"**; la tercera, "la verdad es que no".
- **[46:37]**–**[47:08]** La **división por $t$** "es importante, aparece en varios ejercicios": se llega a arcotangentes o logaritmos y la integral siempre es directa ("la idea es aplicar la propiedad", no integrales súper complicadas).
- **[48:10]**–**[48:42]** TVI y TVF se usan sobre todo en **sistemas estables** (más el del valor final), "y pueden llegar a servir a ejercicio seguro". **[51:18]**–**[51:50]** El TVF da el **valor estable** de la función.
- **[1:26:40]**–**[1:27:12]** "Nunca les van a pedir" de dónde sale $\mathcal{L}\{\delta\} = 1$ (está en la tabla); el **concepto** de impulso sí es importante. **[1:21:40]**–**[1:23:27]** Las otras dos propiedades del impulso ($\int_0^\infty \delta(t)f(t)\,dt = f(0)$ y su versión corrida) no se usan en la materia ("anecdótico").
- **[1:41:03]**–**[1:42:08]** Una antitransformada directa sola **no es ejercicio de examen** ("esto es directísima"): aparecen en el medio de ejercicios más grandes, con **fracciones simples**, ecuaciones diferenciales y convolución.
- **[1:46:22]** El caso grado del numerador ≥ grado del denominador (dividir polinomios antes) "no es muy importante"; lo que importa es el caso normal.
- **[1:50:04]**, **[1:52:47]** Fracciones simples es "lo más importante cuando resolvamos ecuaciones diferenciales": "vamos a usar muchísimo, muchísimo el método". **[1:52:47]** "Es un tema súper importante en la cursada".

**Errores típicos y trucos**

- **[23:49]**–**[24:20]** No hace falta sacar denominador común en el resultado de una transformada: "es mejor dejarlo así separado, que es claro de dónde viene cada cosa".
- **[28:41]**–**[29:42]** Segunda traslación: **todas las $t$ de la fórmula tienen que tener el mismo desplazamiento y ese mismo desplazamiento tiene que estar en el dominio**. $\cos(t - 2\pi/3)$ con $t > 0$ **no** sirve. Se repite en **[1:15:44]**–**[1:16:46]**: "tiene que haber un match" entre las $t - a$ y el escalón $E(t-a)$.
- **[1:07:03]**, **[1:11:24]** Si lo que se desplaza es una **constante** (no hay $t$), la condición de la fórmula se da por cumplida.
- **[1:10:20]**–**[1:11:59]** Si la fórmula tiene $t$ suelta y el escalón está corrido, hay que **sumar y restar** para que aparezca $t - a$ ($t = (t-1) + 1$) y compensar.
- **[1:13:08]** Al escribir con escalones "casi siempre voy a terminar aplicando las segundas propiedades de traslación". **[1:14:10]** Escribirlo en un renglón sirve para darse cuenta del truco de sumar y restar; si transformás solo "$t$" te da $1/s^2$, que es otra cosa.
- **[40:16]**–**[40:49]** En la multiplicación por $t^n$, con $n$ **par** el cambio de signo no cambia nada; con $n$ impar sí. **[41:21]**–**[41:53]** A veces hay un camino más fácil (traslación): "tienen esta libertad de elegir la propiedad que más les convenga".
- **[47:39]**–**[48:10]** Nunca van a tener que evaluar $F(s)$ (p. ej. una arcotangente) en un complejo: "siempre que tengamos que evaluar alguna $F(s)$ va a ser con un número real".
- **[1:30:52]**–**[1:31:55]** Denominador $s^2 + a^2$: si hay **$s$ en el numerador viene de un coseno**, si hay **una constante viene de un seno**.
- **[1:35:15]**–**[1:36:26]** Truco que "se usa mucho": **multiplicar y dividir por una constante conveniente** para llegar a una antitransformada directa.
- **[1:37:29]** "Practiquen si no se acuerdan cómo **completar el cuadrado**, porque lo vamos a usar bastante".
- **[1:40:33]**–**[1:41:03]** Antitransformar es "más artesanal": "jugar siempre a qué se parece esta transformada".
- **[1:49:02]** En fracciones simples con raíces **complejas conjugadas** el numerador lleva **dos incógnitas** ($Ax + B$).
- Deslices del video: **[39:46]** arranca el ejemplo de $t^2 e^{2t}$ por el camino raro y se marea (**[40:49]**); **[53:23]** en el TVF escribe los límites al revés y lo corrige; **[1:39:02]** dice "6 sobre $s^3$" como transformada de $t^2$ y se corrige: es $2/s^3$.

## Por qué Laplace es el tema central del primer parcial — [00:00]

- Es una herramienta "súper útil" que en las clases siguientes se usa para **resolver ecuaciones diferenciales** [00:00].
- **Sistemas estables** usa todo Laplace, y la **transformada Z** es lo mismo pero para funciones discretas [00:30].
- En la teórica anterior ya se había presentado Laplace a partir de la transformada de Fourier; acá se rehace la introducción [01:00].

## Definición, dominio del tiempo y dominio de Laplace — [01:31]

Dada $f(t)$ con $t > 0$ (se trabaja con $t$ positivo porque se piensa como función del tiempo) [01:00], su **transformada de Laplace** es [01:31]:

$$
\mathcal{L}\{f(t)\} = F(s) = \int_0^{\infty} f(t)\, e^{-st}\, dt
$$

- $f(t)$ está en el **dominio del tiempo** (variable real); $F(s)$ en el **dominio de Laplace**, con $s$ **variable compleja** [02:02]–[02:34].
- El operador se simboliza $\mathcal{L}$ (en general en cursiva) [02:02]. El proceso inverso es la **antitransformada** $\mathcal{L}^{-1}$, que lleva $F(s)$ de nuevo a $f(t)$ [02:34].
- Notación: $\mathcal{L}\{f(t)\}$ es "transformar $f(t)$" y devuelve una $F(s)$ [03:06].

<details>
<summary>📝 Ejercicio 1 — 03:06: $\mathcal{L}\{1\}$ por definición (y $\mathcal{L}\{t\}$)</summary>

Hallar la transformada de $f(t) = 1$ para $t > 0$ (constante que arranca en $0$, no definida para los negativos). Después, la de $f(t) = t$, $t > 0$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** se aplica la definición con $f(t) = 1$ (el 1 "está acompañando a la $e^{-st}$, pero no se escribe") [03:39]:

$$
F(s) = \int_0^{\infty} 1 \cdot e^{-st}\, dt
$$

**Paso 2:** al resolver la integral (Barrow), tener en cuenta que **las exponenciales negativas tienden a $0$ en el infinito** ("se van acercando asintóticamente al eje $x$"), algo que se van a cruzar bastante [04:09]:

$$
\mathcal{L}\{1\} = \frac{1}{s}
$$

**Paso 3:** con $f(t) = t$ se pone $t$ en la definición y la integral da [04:42]:

$$
\mathcal{L}\{t\} = \frac{1}{s^2}
$$

El profe no la resuelve: usa la misma primitiva que el $c_n$ de la serie exponencial de Fourier, "si quieren después chequearla ustedes" [04:42].

</details>

</details>

## Se trabaja con tabla (pero hay que saber la definición) — [05:13]

- A diferencia de Fourier, **no se van a resolver estas integrales** cada vez: se trabaja con una **tablita** que dice cuál es la transformada de cada función, y que también sirve al revés para antitransformar (de derecha a izquierda) [05:13].
- Si meten esas funciones en la definición llegan a la segunda columna, "pero lo vamos a dar por sabido": $\mathcal{L}\{e^{at}\}$ es directamente $\frac{1}{s-a}$ [05:43].
- **Importante:** saber la definición, porque hay ejercicios que se resuelven a partir de ella (sin resolver la integral en sí) [05:43]–[06:15].

## Tabla básica de transformadas — [06:15]

| $f(t)$ | $F(s) = \mathcal{L}\{f(t)\}$ |
|---|---|
| $1$ | $\dfrac{1}{s}$ |
| $t^n$ ($n$ natural) | $\dfrac{n!}{s^{n+1}}$ |
| $e^{at}$ | $\dfrac{1}{s-a}$ |
| $\cos at$ | $\dfrac{s}{s^2 + a^2}$ |
| $\mathrm{sen}\, at$ | $\dfrac{a}{s^2 + a^2}$ |
| $\delta(t)$ (impulso unitario) | $1$ |

(En el ayudamemoria la tabla también incluye $t \to 1/s^2$ y las condiciones $s > 0$, $s > a$ [ayudamemoria].)

- $t^n$ [06:53]–[07:24]: con $n = 1$, $1!/s^2 = 1/s^2$ (el ejemplo calculado); con $n = 2$, $2/s^3$; con $n = 3$, $3! = 6$, $6/s^4$.
- $e^{at}$ [07:24]–[07:55]: $a$ puede ser negativo: $\mathcal{L}\{e^{-t}\} = \frac{1}{s+1}$ ("menos por menos más").
- El **impulso unitario** se ve al final de la clase [07:55].

## Condiciones de existencia: seccionalmente continua y de orden exponencial — [08:27]

¿A cualquier función se le puede aplicar Laplace? No: hay dos condiciones [08:27].

- **Seccionalmente continua** (la misma condición de las series de Fourier): una cantidad finita de saltos, y saltos finitos. "No tiene que tener asíntotas", porque ese salto es infinito [08:27]–[09:01].
- **De orden exponencial** (condición nueva) [09:01]–[09:33]: existen $M$ y $\alpha$ tales que, a partir de cierto $t_0$,

$$
|f(t)| \le M\, e^{\alpha t} \qquad \forall\, t \ge t_0
$$

  es decir, $f$ queda **acotada entre $-Me^{\alpha t}$ y $Me^{\alpha t}$** [10:04].

- Ejemplo gráfico [10:04]–[11:45]: una sinusoide "medio extraña" (verde) que en algún pico se pasa de la exponencial roja, pero **a partir de cierto punto** ya no sale de entre la roja ($Me^{\alpha t}$) y la azul ($-Me^{\alpha t}$) [paso en el pizarrón, ver video].
- "Hablando en criollo": la función **no puede crecer más rápido que una exponencial** [11:45]. **No** quiere decir que esté acotada entre dos valores: $t$ tiende a infinito y tiene transformada, porque lo hace más lento que una exponencial [11:45]–[12:15].
- Si es seccionalmente continua y de orden exponencial, **se le puede aplicar Laplace** [12:15].

## Condiciones suficientes pero no necesarias: $1/\sqrt{t}$ — [12:48]

- El recíproco no se cumple ("como suele pasar en el 90% de las cosas en esta materia"): hay funciones que no cumplen las dos condiciones y tienen transformada [12:48].
- Contraejemplo ("no importa", es complejo calcularla) [12:48]–[13:19]: $f(t) = 1/\sqrt{t}$ no es seccionalmente continua (asíntota vertical en $0$, salto infinito), y sin embargo

$$
\mathcal{L}\left\{\frac{1}{\sqrt{t}}\right\} = \frac{\sqrt{\pi}}{\sqrt{s}}
$$

- Conclusión: son **condiciones suficientes, pero no necesarias** [13:50].

## Uso de la tabla: $\cos 3t$ — [13:50]

Para $\cos 3t$ se busca en la tabla la fila de $\cos at$ con $a = 3$ ($a^2 = 9$) [13:50]–[14:23]:

$$
\mathcal{L}\{\cos 3t\} = \frac{s}{s^2 + 9}
$$

"Así de fácil es como se usa la tabla" [14:53]. Como la tabla es básica, se complementa con **propiedades** para transformar funciones más difíciles [14:53].

## Qué propiedades se ven (y cuáles están en el ayudamemoria) — [15:24]

- La guía teórica oficial tiene muchas propiedades; el profe trae (en un PDF propio subido al campus [16:25]) **solo las que se usan** [15:24].
- La tabla (quizás con alguna función más) y las propiedades **están en el resumen que pueden usar en el parcial** [15:24]–[15:54].
- En un final podrían tomar una propiedad que no se usa en la guía; con el machete a la vista debería ser fácil aplicarla [15:54].

## Propiedad A: linealidad — [16:59]

Si $F(s) = \mathcal{L}\{f(t)\}$, $G(s) = \mathcal{L}\{g(t)\}$ y $k_1, k_2$ son constantes reales [16:59]–[17:30]:

$$
\mathcal{L}\{k_1 f(t) + k_2 g(t)\} = k_1 F(s) + k_2 G(s)
$$

- Justificación: la transformada es una integral, y a la integral se le aplica linealidad (las constantes salen y se separa en términos) [17:30]–[18:00].
- Es "la que más se usa", después se aplica sin pensar [18:31], [20:40].

<details>
<summary>📝 Ejercicio 2 — 18:00: $\mathcal{L}\{4t^2 - 3\cos 2t + 5e^{-t}\}$</summary>

Ejemplo del PDF: transformar $4t^2 - 3\cos 2t + 5e^{-t}$.

Al leer el enunciado dice "más 5 por $e$ a la menos $5t$", pero después transforma $e^{-t}$ y escribe $\frac{1}{s+1}$ [poco claro en la transcripción]. Se transcribe lo que resuelve.

<details>
<summary>Ver resolución</summary>

**Paso 1:** tres términos que están en la tabla: se sacan las constantes y se separa en tres transformadas [18:00]–[18:31]:

$$
4\,\mathcal{L}\{t^2\} - 3\,\mathcal{L}\{\cos 2t\} + 5\,\mathcal{L}\{e^{-t}\}
$$

**Paso 2:** por tabla [18:31]–[19:03]: $\mathcal{L}\{t^2\} = 2/s^3$, $\mathcal{L}\{\cos 2t\} = s/(s^2+4)$, $\mathcal{L}\{e^{-t}\} = 1/(s+1)$.

**Paso 3:** se agrupa ($4 \cdot 2 = 8$) [19:03]:

$$
\frac{8}{s^3} - \frac{3s}{s^2+4} + \frac{5}{s+1}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 3 — 19:38: $\mathcal{L}\{3t - 5\,\mathrm{sen}\,4t + 8\}$</summary>

Transformar $3t - 5\,\mathrm{sen}\,4t + 8$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** por linealidad (el 8 se puede pensar como $8 \cdot 1$ para verlo en la tabla) [19:38]:

$$
3\,\mathcal{L}\{t\} - 5\,\mathcal{L}\{\mathrm{sen}\,4t\} + 8\,\mathcal{L}\{1\}
$$

**Paso 2:** $\mathcal{L}\{t\} = 1/s^2$ (el cuadrado "es con un 2, no con un 3; el 3 va arriba"); $\mathcal{L}\{\mathrm{sen}\,4t\} = 4/(s^2+16)$; $\mathcal{L}\{1\} = 1/s$ [19:38]–[20:40]:

$$
\frac{3}{s^2} - \frac{20}{s^2+16} + \frac{8}{s}
$$

**Consulta [23:19]–[24:20]:** ¿hay que operar y sacar denominador común? No: "es mejor dejarlo así separado, que es claro de dónde viene cada cosa".

</details>

</details>

## Propiedad B: primera propiedad de la traslación — [20:40]

Si $F(s) = \mathcal{L}\{f(t)\}$ [21:12]:

$$
\mathcal{L}\{e^{at} f(t)\} = F(s - a)
$$

- **Multiplicar por $e^{at}$ en el tiempo equivale a trasladar $a$ unidades hacia la derecha en el dominio de Laplace** [21:12].
- Receta: se toma la transformada "normal" y en **todas** las apariciones de $s$ se pone $s - a$. Si $a$ es negativo, "menos por menos más" y se corre para el otro lado [21:45]–[22:17].
- Ejemplo [21:45]–[22:49]: $\mathcal{L}\{\cos 2t\} = \frac{s}{s^2+4}$; con $e^{-t}$ se reemplaza $s$ por $s+1$:

$$
\mathcal{L}\{e^{-t}\cos 2t\} = \frac{s+1}{(s+1)^2 + 4}
$$

<details>
<summary>📝 Ejercicio 4 — 22:49: primera traslación ($\mathrm{sen}\,3t\,e^{-5t}$, $t\,e^{2t}$, $e^{at}$)</summary>

Transformar: a) $\mathrm{sen}\,3t \cdot e^{-5t}$; b) $t\,e^{2t}$; c) $e^{at}$ pensada como $1 \cdot e^{at}$.

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** $\mathcal{L}\{\mathrm{sen}\,3t\} = \frac{3}{s^2+9}$; está multiplicada por $e^{-5t}$, desplazamiento de 5 unidades: $s \to s + 5$ [22:49]–[23:19]:

$$
\mathcal{L}\{e^{-5t}\,\mathrm{sen}\,3t\} = \frac{3}{(s+5)^2 + 9}
$$

**Paso 2 (b):** $\mathcal{L}\{t\} = \frac{1}{s^2}$; con $e^{2t}$, en cada $s$ se pone $s - 2$ [24:20]–[24:51]:

$$
\mathcal{L}\{t\,e^{2t}\} = \frac{1}{(s-2)^2}
$$

**Paso 3 (c):** $\mathcal{L}\{1\} = \frac{1}{s}$ y se desplaza [24:51]–[25:22]. Llega a lo mismo que la tabla ("este ejemplo es básicamente la definición"):

$$
\mathcal{L}\{e^{at}\} = \frac{1}{s-a}
$$

</details>

</details>

## Propiedad C: segunda propiedad de la traslación — [25:53]

Si $F(s) = \mathcal{L}\{f(t)\}$ y [26:24]

$$
g(t) = \begin{cases} f(t-a) & t > a \\ 0 & t < a \end{cases}
\qquad\Longrightarrow\qquad
\mathcal{L}\{g(t)\} = e^{-as}\, F(s)
$$

- **Una traslación de $a$ unidades a la derecha en el tiempo equivale a multiplicar por $e^{-as}$ en el dominio de Laplace** [26:24]–[26:56].
- $g$ es la función **corrida**: vale $0$ entre $0$ y $a$ y arranca a tener valores en $a$ [26:56].
- Ejemplo [27:33]–[28:41]: $\cos(t - 2\pi/3)$ para $t > 2\pi/3$ es un coseno corrido $2\pi/3$ a la derecha. Se piensa la transformada del coseno sin desplazamiento, $\frac{s}{s^2+1}$, y se multiplica por $e^{-as}$ con $a = 2\pi/3$:

$$
\mathcal{L}\{g(t)\} = e^{-\frac{2\pi}{3}s}\, \frac{s}{s^2+1}
$$

- **Condición doble** [28:41]–[29:42]: todas las $t$ de la fórmula tienen que tener **el mismo desplazamiento**, y ese desplazamiento tiene que estar **reflejado en el dominio**. Si te dan $\cos(t - 2\pi/3)$ para $t > 0$, **no** se puede usar la propiedad.
- Hay una propiedad "D" en la guía teórica que el profe saltea "porque no tiene sentido" (dice que queda resuelta indirectamente con la tabla) [30:46]; no la nombra [poco claro en la transcripción].

<details>
<summary>📝 Ejercicio 5 — 29:42: seno desplazado 4 unidades</summary>

Transformar $g(t) = \mathrm{sen}(t-4)$ si $t > 4$, $0$ si $t < 4$ (un seno "normal" a partir del 4).

<details>
<summary>Ver resolución</summary>

**Paso 1:** se piensa el seno sin desplazamiento: $\mathcal{L}\{\mathrm{sen}\,t\} = \frac{1}{s^2+1}$ [29:42]–[30:13].

**Paso 2:** desplazamiento de 4 unidades → por la segunda traslación se multiplica por $e^{-4s}$ [30:13]:

$$
\mathcal{L}\{g(t)\} = \frac{e^{-4s}}{s^2+1}
$$

</details>

</details>

## Transformada de las derivadas — [30:46]

- Es la razón por la que Laplace "es buena": las **ecuaciones diferenciales** en el tiempo se vuelven **ecuaciones algebraicas** en el dominio de Laplace, mucho más fáciles [31:22].
- Si $F(s) = \mathcal{L}\{f(t)\}$ [31:53]:

$$
\mathcal{L}\{f'(t)\} = s\,F(s) - f(0)
$$

- "Esto es muy importante" [31:53]. Pero no se usa con ejemplos concretos sino en **forma genérica**: en las EDO la incógnita es $f$ (o $i$), así que se escribe tal cual $sF(s) - f(0)$ o $sI(s) - i(0)$ [32:26]–[33:00].
- La demostración usa integración por partes [34:03].

<details>
<summary>📝 Ejercicio 6 — 33:00: $\mathcal{L}\{3t^2\}$ a partir de $t^3$</summary>

Sabiendo que $\mathcal{L}\{t^3\} = \frac{6}{s^4}$, hallar $\mathcal{L}\{3t^2\}$ (que es la derivada de $t^3$) y de ahí $\mathcal{L}\{t^2\}$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** con $f(t) = t^3$, $f'(t) = 3t^2$ y $f(0) = 0^3 = 0$ [33:32]:

$$
\mathcal{L}\{3t^2\} = s \cdot \frac{6}{s^4} - 0 = \frac{6}{s^3}
$$

**Paso 2:** dividiendo por 3 [34:03]:

$$
\mathcal{L}\{t^2\} = \frac{2}{s^3}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 7 — 34:34: $\mathcal{L}\{\cos 3t\}$ a partir de $\mathrm{sen}\,3t$</summary>

Con $f(t) = \mathrm{sen}\,3t$, calcular la transformada de $\cos 3t$. Ojo: la derivada de $\mathrm{sen}\,3t$ no es $\cos 3t$, es $3\cos 3t$, así que hay "un pasito extra" [34:34].

<details>
<summary>Ver resolución</summary>

**Paso 1:** $sF(s) - f(0)$ con $F(s) = \frac{3}{s^2+9}$ y $f(0) = \mathrm{sen}(3 \cdot 0) = 0$ [35:04]–[35:35]:

$$
\mathcal{L}\{3\cos 3t\} = s\cdot\frac{3}{s^2+9} - 0 = \frac{3s}{s^2+9}
$$

**Paso 2:** se multiplica por $\frac{1}{3}$ [36:05]:

$$
\mathcal{L}\{\cos 3t\} = \frac{s}{s^2+9}
$$

que coincide con la tabla.

</details>

</details>

## Derivada segunda y derivada enésima — [36:05]

Aplicando dos veces la propiedad (primero a $f'$, después se abre $\mathcal{L}\{f'\}$) [36:05]–[37:08]:

$$
\mathcal{L}\{f''(t)\} = s\,\mathcal{L}\{f'(t)\} - f'(0) = s\,[\,s F(s) - f(0)\,] - f'(0)
$$

$$
\mathcal{L}\{f''(t)\} = s^2 F(s) - s\,f(0) - f'(0)
$$

- Primera y segunda derivada **se usan muy seguido**; la tercera "la verdad es que no" [37:08].
- Con la misma forma recursiva se obtiene la de la derivada $n$-ésima; la fórmula general está en el PDF ("creo que también está en el resumen") [37:40] [paso en el pizarrón, ver video].

## Multiplicación por $t^n$ — [38:43]

Si $F(s) = \mathcal{L}\{f(t)\}$ [38:43]:

$$
\mathcal{L}\{t^n f(t)\} = (-1)^n\, F^{(n)}(s)
$$

- Lectura: si $f(t)$ está multiplicada por $t^n$, se toma la transformada de $f$, **se deriva $n$ veces y se le cambia el signo $n$ veces** [38:43]–[39:15].
- Con exponente **par** el cambio de signo no cambia nada; con **impar** sí [40:16]–[40:49].
- Consulta [54:28]–[54:58]: el $(-1)^n$ es "multiplicar por $-1$ $n$ veces": con $t^1$ cambia el signo; con $t^2$, $(-1)(-1) = 1$, "como que no hubo cambio de signo".

<details>
<summary>📝 Ejercicio 8 — 39:15: $\mathcal{L}\{t^2 e^{2t}\}$ por dos caminos</summary>

Ejemplo del PDF: transformar $t^2 e^{2t}$.

<details>
<summary>Ver resolución</summary>

**Paso 1 (camino del PDF, multiplicación por $t^2$):** $\mathcal{L}\{e^{2t}\} = \frac{1}{s-2} = (s-2)^{-1}$ [39:46]. Hay que derivarla dos veces y cambiarle el signo dos veces. La primera derivada [39:46]–[40:16]:

$$
\frac{d}{ds}(s-2)^{-1} = -\frac{1}{(s-2)^2}
$$

Después se vuelve a derivar (llega a $F''(s)$) y se vuelve a cambiar el signo [40:16]; con $n = 2$ los dos cambios de signo se cancelan. El desarrollo quedó escrito "todo en una línea" en el PDF [paso en el pizarrón, ver video].

**Paso 2 (camino más obvio, primera traslación):** $\mathcal{L}\{t^2\} = \frac{2}{s^3}$ y por estar multiplicada por $e^{2t}$ se corre $s \to s-2$ [40:49]–[41:21]:

$$
\mathcal{L}\{t^2 e^{2t}\} = \frac{2}{(s-2)^3}
$$

"Fíjense que es igual": los dos caminos llegan al mismo resultado; se puede elegir la propiedad que más convenga [41:21]–[41:53].

</details>

</details>

<details>
<summary>📝 Ejercicio 9 — 41:53: $\mathcal{L}\{t\,\mathrm{sen}\,3t\}$</summary>

Transformar $t\,\mathrm{sen}\,3t$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** transformada de lo que está multiplicado por $t$ [42:24]:

$$
F(s) = \mathcal{L}\{\mathrm{sen}\,3t\} = \frac{3}{s^2+9}
$$

**Paso 2:** se deriva una vez (cociente: derivada de arriba $0$, queda $-3 \cdot 2s$ sobre el denominador al cuadrado) [42:24]–[42:56]:

$$
F'(s) = \frac{-6s}{(s^2+9)^2}
$$

**Paso 3:** se cambia el signo una vez ($n = 1$) [42:56]–[43:30]:

$$
\mathcal{L}\{t\,\mathrm{sen}\,3t\} = \frac{6s}{(s^2+9)^2}
$$

</details>

</details>

## División por $t$ (con la condición del límite) — [43:30]

Así como la multiplicación por $t$ está asociada a las derivadas, la división por $t$ está asociada a las **integrales** [43:30]. Si $F(s) = \mathcal{L}\{f(t)\}$ [44:01]–[44:31]:

$$
\mathcal{L}\left\{\frac{f(t)}{t}\right\} = \int_s^{\infty} F(u)\, du
\qquad \text{siempre que exista } \lim_{t \to 0} \frac{f(t)}{t}
$$

- **Condición:** tiene que existir el límite de $f(t)/t$ cuando $t \to 0$ [44:31].
- Se integra en $u$ porque **$s$ forma parte de los límites de integración**; al aplicar Barrow queda una función de $s$ [44:31], [46:37].
- El ejemplo del PDF "es malo"; usa otro ejercicio [44:31]–[45:02].

<details>
<summary>📝 Ejercicio 10 — 45:02: $\mathcal{L}\{\mathrm{sen}\,t / t\}$</summary>

Transformar $\dfrac{\mathrm{sen}\,t}{t}$.

<details>
<summary>Ver resolución</summary>

**Paso 1 (condición):** ¿existe el límite? "Ya lo vimos 50.000 veces en la carrera" [45:02]:

$$
\lim_{t \to 0} \frac{\mathrm{sen}\,t}{t} = 1
$$

Existe: se puede aplicar la propiedad.

**Paso 2:** integral entre $s$ e $\infty$ de la transformada de $\mathrm{sen}\,t$, escrita en $u$ [45:35]:

$$
\mathcal{L}\left\{\frac{\mathrm{sen}\,t}{t}\right\} = \int_s^{\infty} \frac{1}{u^2+1}\, du
$$

**Paso 3:** es una integral directa, la arcotangente [45:35]–[46:06]:

$$
\arctan u \,\Big|_s^{\infty}
$$

**Paso 4:** Barrow: en el infinito la arcotangente tiende a $\pi/2$ (asíntota horizontal), menos la arcotangente en $s$ [46:06]–[46:37]:

$$
\mathcal{L}\left\{\frac{\mathrm{sen}\,t}{t}\right\} = \frac{\pi}{2} - \arctan s
$$

</details>

</details>

## Teorema del valor inicial — [48:10]

Si existen los límites indicados [48:42]–[49:13]:

$$
\lim_{t \to 0} f(t) = \lim_{s \to \infty} s\,F(s)
$$

- Ejemplo del PDF [49:13]–[49:44]: $f(t) = 3e^{-2t}$, $\lim_{t\to 0} f(t) = 3$; $F(s) = \frac{3}{s+2}$ y $\lim_{s\to\infty} \frac{3s}{s+2} = 3$ (L'Hôpital: derivo arriba, 3; abajo, 1; o dividir todo por $s$).

<details>
<summary>📝 Ejercicio 11 — 50:15: TVI con $4e^{-3t}$</summary>

Verificar el teorema del valor inicial con $f(t) = 4e^{-3t}$.

<details>
<summary>Ver resolución</summary>

**Paso 1 (lado del tiempo):** [50:15]

$$
\lim_{t \to 0} 4e^{-3t} = 4 \cdot 1 = 4
$$

**Paso 2 (lado de Laplace):** $F(s) = \frac{4}{s+3}$ [50:48]; la indeterminación $\infty/\infty$ se salva con L'Hôpital o dividiendo por $s$ [50:48]–[51:18]:

$$
\lim_{s \to \infty} \frac{4s}{s+3} = 4
$$

**Paso 3:** $4 = 4$: los límites son iguales [51:18].

</details>

</details>

## Teorema del valor final — [51:18]

Si existen los límites indicados (solo se invierten hacia dónde tienden $t$ y $s$) [51:18]:

$$
\lim_{t \to \infty} f(t) = \lim_{s \to 0} s\,F(s)
$$

- Es útil porque en **sistemas estables** $\lim_{t\to\infty} f(t)$ es el **valor estable** de la función: "una manera fácil de llegar a ese valor estable" [51:50].
- Ejemplo del PDF [52:21]: $f(t) = 3e^{-2t}$; $\lim_{t\to\infty} = 0$ (constante por exponencial negativa); $\lim_{s \to 0} \frac{3s}{s+2} = \frac{0}{2} = 0$, sin indeterminación.

<details>
<summary>📝 Ejercicio 12 — 52:53: TVF con $4e^{-3t}$</summary>

Verificar el teorema del valor final con $f(t) = 4e^{-3t}$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** $\lim_{t \to \infty} 4e^{-3t} = 0$ (exponencial decreciente) [52:53]–[53:23].

**Paso 2:** $F(s) = \frac{4}{s+3}$ [53:23]. Al principio escribe los límites al revés y lo corrige [53:23]: el de $s$ es $s \to 0$ [53:57]:

$$
\lim_{s \to 0} \frac{4s}{s+3} = \frac{0}{3} = 0
$$

**Paso 3:** se verifica que los límites son iguales [53:57].

</details>

</details>

Con esto termina la lista de propiedades "que yo seleccioné, que son las que realmente vamos a estar usando" [53:57].

## Función escalón unitario (Heaviside) — [55:29]

Primera de dos funciones especiales (la otra es el impulso). "Siempre le vamos a decir escalón unitario" [55:29].

$$
E(t) = 1 \quad (t > 0)
\qquad\qquad
E(t-a) = \begin{cases} 1 & t > a \\ 0 & 0 < t < a \end{cases}
$$

- A veces se la llama $u$ (de unitario), pero en general se usa $E$ [56:31].
- $E(t-a)$ es la constante 1 que en vez de arrancar en $0$ arranca en $a$: corrida $a$ unidades a la derecha [56:31].
- **Para qué sirve:** "prender o apagar funciones" [57:04]. Si $f(t)$ se multiplica por $E(t - t_1)$, queda la función solo a partir de $t_1$ y $0$ entre $0$ y $t_1$ [57:35]–[58:05].
- Permite escribir una función partida **en un solo renglón**, mucho más conveniente para transformar [58:05]–[58:36]:

$$
g(t) = \begin{cases} f(t) & t > t_1 \\ 0 & t < t_1 \end{cases}
\qquad = \qquad f(t)\, E(t - t_1)
$$

## Transformada del escalón — [59:08]

$$
\mathcal{L}\{E(t)\} = \mathcal{L}\{1\} = \frac{1}{s}
\qquad\qquad
\mathcal{L}\{E(t-a)\} = \frac{e^{-as}}{s}
$$

- La primera es la de la constante 1 para $t > 0$ [59:08]–[59:39].
- La segunda sale por definición o, "si lo piensan", por la **segunda propiedad de la traslación**: la función 1 (transformada $1/s$) con el mismo desplazamiento en la fórmula y en el dominio → se multiplica por $e^{-as}$ [59:39]–[1:00:09]. Por los dos caminos se llega a lo mismo [1:00:09].

## Funciones partidas en un renglón con escalones — [1:00:39]

Función genérica en tres trozos [1:00:39]–[1:01:13]: $f_1$ entre $0$ y $t_1$, $f_2$ entre $t_1$ y $t_2$, $f_3$ de $t_2$ en adelante. Idea: **curva entera menos la parte desde donde se apaga** [1:01:44]–[1:02:52]:

$$
f(t) = f_1(t)\,E(t) - f_1(t)\,E(t-t_1) + f_2(t)\,E(t-t_1) - f_2(t)\,E(t-t_2) + f_3(t)\,E(t-t_2)
$$

- $f_1 E(t)$ es la curva entera desde $0$; se le resta $f_1$ a partir de $t_1$ y queda solo el primer tramo [1:01:44]–[1:02:52].
- $f_2$ arranca en $t_1$ y se le resta la continuación desde $t_2$ [1:02:52].
- $f_3$ solo se prende a partir de $t_2$ [1:03:25].
- Después se puede sacar factor común; "lo importante es que sepan llegar a este paso" [1:03:25].

<details>
<summary>📝 Ejercicio 13 — 1:03:55: (guía, ej. 3 a) constante $1/a^2$ entre $0$ y $a$</summary>

Hallar la transformada de

$$
i(t) = \begin{cases} \dfrac{1}{a^2} & 0 < t < a \\ 0 & t > a \end{cases}
$$

(Si fuera para todo $t > 0$ sería "súper fácil": $\frac{1}{a^2 s}$; pero solo vale entre $0$ y $a$ [1:04:27]–[1:04:57].)

<details>
<summary>Ver resolución</summary>

**Paso 1:** "curva entera menos segunda parte de la curva igual a primera parte" [1:05:28]:

$$
\mathcal{L}\{i(t)\} = \mathcal{L}\left\{\frac{1}{a^2}E(t)\right\} - \mathcal{L}\left\{\frac{1}{a^2}E(t-a)\right\}
$$

**Paso 2:** el primer término es la transformada de una constante ($E(t) = 1$ para $t > 0$): $\frac{1}{a^2 s}$ [1:06:00].

**Paso 3:** el segundo término es una constante corrida $a$ unidades: segunda traslación [1:06:31]. Condiciones [1:07:03]: el desplazamiento en el dominio está (arranca en $a$); en la fórmula no hay $t$ (es constante), así que esa condición se da por cumplida.

**Paso 4:** transformada sin desplazar por $e^{-as}$, siendo $a$ el desplazamiento [1:07:36] (dice "$e$ a la menos $at$", pero la propiedad es $e^{-as}$):

$$
\mathcal{L}\{i(t)\} = \frac{1}{a^2 s} - \frac{e^{-as}}{a^2 s}
$$

**Paso 5:** después "es un factor común solo para que quede un poquito más lindo" [1:07:36]:

$$
\mathcal{L}\{i(t)\} = \frac{1 - e^{-as}}{a^2 s}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 14 — 1:08:10: la identidad prendida entre $1$ y $2$</summary>

Ejemplo propio del profe: transformar

$$
f(t) = \begin{cases} t & 1 < t < 2 \\ 0 & \text{si no } (0 < t < 1 \text{ o } t > 2) \end{cases}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1 (planteo en un renglón):** la identidad prendida desde 1 menos la identidad desde 2 [1:08:42]–[1:09:13]:

$$
f(t) = t\,E(t-1) - t\,E(t-2)
$$

**Paso 2 (chequear condiciones):** el desplazamiento en el dominio está, pero en la fórmula hay $t$ y no $t-1$ ni $t-2$: **no se puede aplicar directamente** la segunda traslación [1:09:48]–[1:10:20].

**Paso 3 (sumar y restar):** se escribe $t = (t-1) + 1$ y $t = (t-2) + 2$ y se agrupa [1:10:20]–[1:11:59]:

$$
f(t) = (t-1)\,E(t-1) + E(t-1) - (t-2)\,E(t-2) - 2\,E(t-2)
$$

Los términos con constante también admiten la segunda traslación porque no hay $t$ en la fórmula [1:11:24].

**Paso 4:** cuatro veces la segunda traslación; los términos de la función $t$ llevan $s^2$ en el denominador ($\mathcal{L}\{t\} = 1/s^2$) y los de las constantes compensadoras, $s$ [1:11:59]–[1:12:38]:

$$
\mathcal{L}\{f(t)\} = \frac{e^{-s}}{s^2} + \frac{e^{-s}}{s} - \frac{e^{-2s}}{s^2} - \frac{2e^{-2s}}{s}
$$

**Paso 5:** al final saca factor común [1:13:08] [paso en el pizarrón, ver video].

**Consultas [1:13:08]–[1:17:48]:** ¿y si no lo escribo en un renglón? Igual terminás planteándolo así: no podés transformar solo $t$ (da $1/s^2$, otra cosa). Escribirlo con escalones sirve para darse cuenta de que hay que sumar y restar; la segunda traslación pide el **match** entre el escalón $E(t-a)$ y que todas las $t$ aparezcan como $t - a$. Si no compensás, "sería otra función".

</details>

</details>

## Función impulso unitario (delta de Dirac) — [1:17:48]

- Modela algo que ocurre en un lapso muy pequeño: aplicar una fuerza a un bloque y soltarlo, una explosión de energía en un infinitésimo de tiempo [1:17:48]–[1:18:21].
- Se arma con el pulso rectangular [1:18:55]:

$$
f_\delta(t) = \begin{cases} \dfrac{1}{\tau} & 0 < t < \tau \\ 0 & t > \tau \end{cases}
$$

- A medida que $\tau$ achica, el rectángulo se hace más angosto y más alto, pero **su área es siempre 1** (base $\tau$ por altura $1/\tau$) [1:19:28]–[1:20:31].
- **Definición** [1:20:31]–[1:21:02]:

$$
\delta(t) = \lim_{\tau \to 0} f_\delta(t)
$$

- No es una función en sentido estricto, pero se usa como tal para modelizar problemas físicos [1:21:02].
- Propiedades [1:21:40]–[1:22:11]: $\int_0^{\infty} \delta(t)\,dt = 1$; $\int_0^{\infty} \delta(t) f(t)\,dt = f(0)$; con el impulso corrido $a$ unidades da $f(a)$. Las dos últimas **no se usan en la materia**; sirven para la transformada de Fourier del "tren de impulsos" de la clase anterior [1:22:11]–[1:23:27].

<details>
<summary>📝 Ejercicio 15 — 1:23:27: por qué $\mathcal{L}\{\delta(t)\} = 1$</summary>

Deducir la transformada del impulso unitario (spoiler: ya está en la tabla, da 1).

<details>
<summary>Ver resolución</summary>

**Paso 1:** se escribe $f_\delta$ en un renglón con escalones: la constante $1/\tau$ desde $0$ menos la que arranca en $\tau$ (como el ejercicio 13) [1:23:58]–[1:24:30]:

$$
f_\delta(t) = \frac{1}{\tau}E(t) - \frac{1}{\tau}E(t-\tau)
$$

**Paso 2:** constante y segunda traslación [1:25:01]:

$$
\mathcal{L}\{f_\delta(t)\} = \frac{1}{s\tau} - \frac{e^{-\tau s}}{s\tau}
$$

**Paso 3:** como $\delta$ es el límite, "doy como dado" que el límite de la transformada es la transformada del límite [1:25:32]:

$$
\mathcal{L}\{\delta(t)\} = \lim_{\tau \to 0} \frac{1}{s}\cdot\frac{1 - e^{-\tau s}}{\tau}
$$

**Paso 4:** indeterminación $0/0$; L'Hôpital derivando respecto de $\tau$ (arriba baja el $-s$, con el menos queda $+s$; abajo, 1) [1:26:09]–[1:26:40]:

$$
\frac{1}{s}\lim_{\tau \to 0} s\,e^{-\tau s} = \lim_{\tau \to 0} e^{-\tau s} = 1
$$

</details>

</details>

## Antitransformada de Laplace: por tabla — [1:29:20]

- Antitransformar es volver de $F(s)$ a la $f(t)$ cuya transformada es esa $F(s)$ [1:29:20]–[1:29:50].
- Tiene una definición con integral (parecida a la antitransformada de Fourier) que ni está en la guía teórica; **se trabaja por tabla** [1:29:50].
- Ejemplo [1:30:20]–[1:30:52]: $\frac{1}{s+3}$ encaja en $\frac{1}{s-a}$ con $a = -3$:

$$
\mathcal{L}^{-1}\left\{\frac{1}{s+3}\right\} = e^{-3t}
$$

- Denominador $s^2 + a^2$: **con $s$ en el numerador viene de un coseno; con una constante, de un seno** [1:30:52]–[1:31:23]. Así, una fracción con $s^2 + 25$ y constante arriba viene de $\mathrm{sen}\,5t$ [1:31:23]–[1:31:55] (el numerador quedó en pantalla [paso en el pizarrón, ver video]).
- $\frac{24}{s^5}$: $24 = 4!$, entra por $t^n$ [1:31:55]:

$$
\mathcal{L}^{-1}\left\{\frac{24}{s^5}\right\} = t^4
$$

## Propiedades de la antitransformada: linealidad — [1:32:26]

Hay tres propiedades para antitransformar, "muy parecidas o iguales" a las primeras de la transformada: linealidad y las dos traslaciones [1:32:26]. **Linealidad**: las constantes quedan afuera y se separa en términos, igual que con la transformada [1:32:57].

<details>
<summary>📝 Ejercicio 16 — 1:32:57: antitransformada por linealidad (multiplicar y dividir por una constante)</summary>

Antitransformar una $F(s)$ con tres términos: $\frac{4}{s-2}$, $\frac{3s}{s^2+16}$ y $\frac{5}{s^2+4}$ (los signos entre los dos primeros términos quedaron en pantalla [poco claro en la transcripción]).

<details>
<summary>Ver resolución</summary>

**Paso 1:** $\frac{4}{s-2}$ viene de $e^{2t}$ por 4 → $4e^{2t}$ [1:33:31].

**Paso 2:** $\frac{3s}{s^2+16}$ es la del coseno → $3\cos 4t$ [1:33:31].

**Paso 3:** $\frac{5}{s^2+4}$: $s^2$ más algo con constante arriba → viene de un seno; $a^2 = 4$, $a = 2$, de algo como $\mathrm{sen}\,2t$ [1:34:04]–[1:34:43]. Pero $\mathcal{L}\{\mathrm{sen}\,2t\} = \frac{2}{s^2+4}$, no $\frac{5}{s^2+4}$ [1:34:43].

**Paso 4:** se **hace aparecer** el 2 y se compensa: multiplico y divido por 2 [1:35:15]–[1:35:50]:

$$
\frac{5}{s^2+4} = \frac{5}{2}\cdot\frac{2}{s^2+4}
\quad\Longrightarrow\quad
\mathcal{L}^{-1}\left\{\frac{5}{s^2+4}\right\} = \frac{5}{2}\,\mathrm{sen}\,2t
$$

"Esto se usa mucho": multiplicar y dividir por una constante conveniente para llegar a una antitransformada directa; lo que sobra es una constante que acompaña [1:35:50].

</details>

</details>

## Primera propiedad de la traslación para antitransformar — [1:36:26]

Funciona igual que para la transformada, "leída de derecha a izquierda", por eso no lleva demostración [1:36:26]. Si $F(s)$ está desplazada $a$ unidades [1:36:58]:

$$
\mathcal{L}^{-1}\{F(s-a)\} = e^{at} f(t)
$$

<details>
<summary>📝 Ejercicio 17 — 1:36:58: $\mathcal{L}^{-1}\{1/(s^2 - 2s + 5)\}$ completando cuadrados</summary>

Antitransformar $\dfrac{1}{s^2 - 2s + 5}$ (no está en la tabla: constante sobre polinomio de grado 2) [1:36:58]–[1:37:29].

<details>
<summary>Ver resolución</summary>

**Paso 1:** completar el cuadrado [1:37:29]:

$$
\frac{1}{s^2 - 2s + 5} = \frac{1}{(s-1)^2 + 4}
$$

**Paso 2:** se parece a $\mathcal{L}\{\mathrm{sen}\,2t\} = \frac{2}{s^2+4}$; falta el 2 arriba: multiplico y divido por 2 [1:37:59]–[1:38:29].

**Paso 3:** cada $s$ está desplazada una unidad ($s - 1$) → se multiplica por $e^{t}$ en el tiempo [1:38:29]:

$$
\mathcal{L}^{-1}\left\{\frac{1}{s^2 - 2s + 5}\right\} = \frac{1}{2}\,e^{t}\,\mathrm{sen}\,2t
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 18 — 1:39:02: $\mathcal{L}^{-1}\{6/(s+4)^3\}$</summary>

Antitransformar $\dfrac{6}{(s+4)^3}$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** ¿a qué se parece? A $\frac{2}{s^3} = \mathcal{L}\{t^2\}$ (al principio dice "6 sobre $s^3$" y se corrige) [1:39:02].

**Paso 2:** hago aparecer el 2; sobra $6/2 = 3$ [1:39:33]:

$$
\frac{6}{(s+4)^3} = 3\cdot\frac{2}{(s+4)^3}
$$

**Paso 3:** cada $s$ está corrida 4 unidades ($s + 4$) → $e^{-4t}$ [1:40:03]:

$$
\mathcal{L}^{-1}\left\{\frac{6}{(s+4)^3}\right\} = 3\,t^2\,e^{-4t}
$$

</details>

</details>

- Las antitransformadas son "más artesanales": ver a qué se parece la función y, sabiendo las propiedades, deducir (p. ej. si todas las $s$ están corridas, hay que multiplicar por una exponencial en el tiempo) [1:40:33]–[1:41:03].
- Consulta [1:41:03]–[1:42:08]: ¿esto es de examen? No, "esto es directísima". En los ejercicios aparecen antitransformadas de funciones más complejas, con **fracciones simples**, en el medio de ejercicios más grandes (EDO, convolución).

## Segunda propiedad de la traslación para antitransformar — [1:42:08]

"Creo que es un poquito más fácil verla desde el lado de la antitransformada" [1:42:08]: si $F(s)$ está multiplicada por $e^{-as}$, la antitransformada es la función corrida que arranca en $a$:

$$
\mathcal{L}^{-1}\{e^{-as} F(s)\} = \begin{cases} f(t-a) & t > a \\ 0 & t < a \end{cases}
$$

<details>
<summary>📝 Ejercicio 19 — 1:42:41: $\mathcal{L}^{-1}\{e^{-\pi s/3}/(s^2+1)\}$</summary>

Antitransformar $\dfrac{e^{-\frac{\pi}{3}s}}{s^2+1}$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** $\frac{1}{s^2+1}$ sería $\mathrm{sen}\,t$ [1:42:41].

**Paso 2:** está multiplicada por $e^{-\frac{\pi}{3}s}$: es el seno a partir de $\pi/3$, y el desplazamiento también aparece en la variable [1:42:41]–[1:43:15]:

$$
f(t) = \begin{cases} \mathrm{sen}\left(t - \dfrac{\pi}{3}\right) & t > \dfrac{\pi}{3} \\ 0 & t < \dfrac{\pi}{3} \end{cases}
$$

</details>

</details>

Con estas tres propiedades (linealidad y las dos traslaciones) "vamos a estar bien" para antitransformar; las demás de la guía "no se usan nunca" [1:43:15].

## Método de fracciones simples — [1:43:46]

(Carilla aparte, sin ejemplos específicos; se practica en las clases siguientes [1:43:46].) Dado un cociente de polinomios $\frac{P(x)}{Q(x)}$ con $\mathrm{gr}\,P = n$ y $\mathrm{gr}\,Q = m$ [1:44:17]:

- Si $n < m$, el cociente se puede expresar como **suma de fracciones simples** [1:44:17].
- Si $n \ge m$, primero se **divide**: $P = Q\cdot C + R$ (cociente $C$, resto $R$), y dividiendo por $Q$ [1:44:49]–[1:46:22]:

$$
\frac{P(x)}{Q(x)} = C(x) + \frac{R(x)}{Q(x)}
$$

  y a $R/Q$ se le aplican fracciones simples. Hay un ejercicio así, pero "no es muy importante" [1:46:22].

- Fracciones simples es expresar el cociente **en base a las raíces del denominador** $Q(x)$ [1:46:22]–[1:46:55].

## Los cuatro casos de fracciones simples — [1:46:55]

**Caso 1: raíces reales y distintas** $\alpha, \beta, \dots, \gamma$ [1:46:55]–[1:47:29]:

$$
\frac{P(x)}{Q(x)} = \frac{A}{x-\alpha} + \frac{B}{x-\beta} + \dots + \frac{H}{x-\gamma}
$$

**Caso 2: raíces reales múltiples** ($\alpha$ de multiplicidad $n$): se va bajando el exponente hasta 1 [1:47:29]–[1:48:00]:

$$
\frac{A}{(x-\alpha)^n} + \frac{B}{(x-\alpha)^{n-1}} + \dots + \frac{\cdots}{x-\alpha}
$$

**Caso 3: raíces complejas conjugadas simples**: en vez de una constante, el numerador lleva **dos incógnitas** $Ax + B$ sobre el polinomio de grado 2 que tiene esas raíces; otro par conjugado lleva $Cx + D$ sobre su propio cuadrático [1:48:00]–[1:49:02] (los coeficientes genéricos de los cuadráticos quedaron en pantalla [paso en el pizarrón, ver video]).

**Caso 4: complejas conjugadas múltiples**: combinación de 2 y 3: $Ax+B$ sobre el cuadrático a la $n$, $Cx+D$ sobre el cuadrático a la $n-1$, …, hasta la potencia 1, siempre con dos incógnitas arriba [1:49:02]–[1:49:33].

Cómo se hallan $A, B, C, \dots$: no se ve en esta clase ("después les voy a decir, o pueden ir repasando ustedes") [1:51:11]–[1:51:44]; ver `04-practica-transformada-laplace.md`.

<details>
<summary>📝 Ejercicio 20 — 1:50:04: para qué sirven las fracciones simples al antitransformar</summary>

Ejemplo inventado en clase de lo que aparece al resolver EDO: antitransformar

$$
F(s) = \frac{s^2 - s + 3}{(s-1)(s+2)^2}
$$

"Esto ya no se parece a nada" de la tabla [1:50:36].

<details>
<summary>Ver resolución</summary>

**Paso 1:** el denominador tiene una raíz real simple ($s = 1$) y una real doble: combinación de los casos 1 y 2 [1:50:36]–[1:51:11]:

$$
F(s) = \frac{A}{s-1} + \frac{B}{(s+2)^2} + \frac{C}{s+2}
$$

(Whisper transcribe "$S-2$" en la descomposición, pero el denominador dictado es $(s+2)^2$ y la antitransformada que da es con $e^{-2t}$ [poco claro en la transcripción].)

**Paso 2:** cada fracción simple **sí** se antitransforma directo por tabla, cualesquiera sean $A, B, C$ [1:51:44]–[1:52:16]:

$$
f(t) = A\,e^{t} + B\,t\,e^{-2t} + C\,e^{-2t}
$$

(La de $B$ viene de la función $t$ desplazada: $e^{-2t}$ por primera traslación.)

**Paso 3:** $A$, $B$ y $C$ "se pueden calcular"; no se hace en la clase [1:52:47].

</details>

</details>

## Propiedades del ayudamemoria que esta clase no desarrolla

En esta clase el profe no da estas propiedades (la convolución la menciona como algo que "todavía nos falta ver" [1:42:08]). Se dejan con la notación del ayudamemoria oficial, permitido en el parcial [ayudamemoria]:

**Cambio de escala:**

$$
\mathcal{L}\{f(at)\} = \frac{1}{a}\,F\!\left(\frac{s}{a}\right)
$$

**Transformada de las integrales:**

$$
\mathcal{L}\left\{\int_0^t f(u)\,du\right\} = \frac{F(s)}{s}
$$

**Teorema de convolución (de Borel):**

$$
\mathcal{L}^{-1}\{F(s)\,G(s)\} = \int_0^t f(u)\,g(t-u)\,du
$$

Su uso está en `04-practica-transformada-laplace.md` (Parte 4) y en `14-video-teorica-aplicaciones-laplace.md`.

---

*Generado el 2026-10-02 a partir de `fuentes/clases/Transformadas de Laplace/T_TLaplace.mp4` (transcripción local con Whisper, `apuntes/transcripts/15-video-teorica-transformada-laplace.json`, 114 min) y, donde se indica, `fuentes/AYUDAMEMORIA-OFICIAL.pdf` (págs. 1–2). Las fórmulas se reconstruyeron de lo dictado; los gráficos y anotaciones en pantalla no se transcriben.*
