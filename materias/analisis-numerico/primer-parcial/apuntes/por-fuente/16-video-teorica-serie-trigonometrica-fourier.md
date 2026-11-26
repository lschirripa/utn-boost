# Serie trigonométrica de Fourier (clase teórica grabada)

> Fuente: fuentes/clases/series de fourier/T_serie_trigonometrica_fourier.mp4 (transcripción local con Whisper)

---

## Índice

- Lo que el profe remarca (resumen de todos los comentarios sobre examen y cursada)
- [00:31] — Fasores: por qué van antes de Fourier
- [01:02] — Sinusoides: amplitud, frecuencia y fase; definición de fasor
- [05:21] — Propiedades del fasor y condiciones para sumar con fasores
- [09:07] — Interpretación gráfica: vectores que giran (GeoGebra)
- [16:34] — 📝 Ejercicio 1: $5\cos(2t + \pi/3) + 3\cos(2t - \pi/5)$ con fasores
- [23:02] — Seno y coseno mezclados: identidades para llevar todo a la misma función
- [23:02] — 📝 Ejercicio 2: $2\cos(4t) + 4\,\mathrm{sen}(4t)$ con fasores
- [29:20] — Serie trigonométrica de Fourier: la guía de la cátedra
- [30:22] — Funciones periódicas, período $T$ y semiperíodo $L$
- [32:35] — Qué funciones se pueden desarrollar: funciones seccionalmente continuas
- [36:50] — La base ortonormal (muy por arriba)
- [40:07] — La serie trigonométrica de Fourier: valor medio, armónicas, frecuencia fundamental
- [45:47] — De dónde sale $a_0$
- [51:02] — De dónde salen $a_n$ y $b_n$
- [57:15] — Síntesis: lo que hay que llevarse de la clase
- [59:53] — 📝 Ejercicio 3: pulso $f(x) = 1$ en $(0,3)$, $0$ en $(-3,0)$, $T = 6$
- [1:13:31] — Solo armónicas impares: reescribir con $n = 2k+1$
- [1:18:45] — Propiedades: coeficientes que tienden a cero, espectros discretos y teorema de Dirichlet
- [1:25:00] — 📝 Ejercicio 4: $f(x) = x^2$ en $(0, 2\pi)$, $T = 2\pi$
- [1:38:30] — Espectro de frecuencias y usos del análisis de Fourier
- [1:43:41] — 📝 Ejercicio 5: suma de $\sum 1/n^2$ (problema de Basilea) con la serie del ejercicio 4
- [1:51:05] — Qué puntos elegir para sumar series numéricas
- [1:53:46] — Funciones pares e impares: qué coeficientes se anulan
- [2:01:49] — Paridad en los ejemplos de la clase
- [2:03:54] — Lo que quedó para la próxima clase (simetría de media onda)

---

## Lo que el profe remarca

Todo comentario sobre examen, cursada y errores típicos que aparece en la clase, en orden
cronológico.

**Qué hay que llevarse (y qué no)**

- [04:49] — En las teóricas explica de dónde salen las cosas, pero va a marcar "a la hora de hacer ejercicios o a la hora de pensar en un examen, qué es lo que se tiene que llevar": "todas las demostraciones y de dónde viene cada cosa no es necesario". De fasores hay que llevarse **cómo se obtiene el fasor** de una función.
- [29:50] — La guía teórica oficial de la cátedra (campus virtual) tiene una explicación "súper algebraica" de dónde sale la serie: es válida y recomienda leerla si les interesa, pero él no entra en esos detalles.
- [45:47] — Las demostraciones de los coeficientes "no es lo fundamental": lo fundamental es **la forma de la serie trigonométrica de Fourier**.
- [57:48] — "**Esto es lo que se tienen que llevar de hoy**": la forma general de la serie y **las tres integrales** de $a_0$, $a_n$ y $b_n$. En muchos ejercicios "el ejercicio se reduce a este cálculo de estas tres integrales".
- [1:13:31] — Por qué solo tienen sentido las armónicas impares en el ejemplo del pulso: "esto sí es importante y esto lo tienen que saber".
- [1:19:18] — De las propiedades, la primera ($a_n, b_n \to 0$) "no se le da demasiada pelota"; la importante es la segunda (valor de la serie en un punto, semisuma de límites laterales).

**Material permitido / herramientas**

- [53:36] — En series de Fourier "se va a usar muchísimo la **tabla de integrales**, es válido tenerla". "Tenganla, porque hay veces que no la llevan y nada, es una lástima".
- [1:30:16] — Las integrales que se usan "casi siempre o siempre": $x\cos$, $x\,\mathrm{sen}$, $x^2\cos$, $x^2\,\mathrm{sen}$ (o senos y cosenos sueltos); "creo que no va a salir de ahí nunca". Se copian de la tabla.

**Método y hábitos que pide**

- [40:37] — En todos los ejercicios de Fourier las integrales se hacen **en un período completo**: $(-L, L)$ o $(0, T)$ (o cualquier otro período completo). [59:23] Las fórmulas cambian de límites según convenga.
- [1:00:25] — "**Siempre grafiquen**" y siempre calculen $T$, $L$ y $\omega_0$, "por más fácil que se vea una función", aunque uno ya sea "canchero" y vea la paridad.
- [1:26:03] — Elegir el intervalo de integración según el "dibujo central": si la función viene definida en $(0, T)$ conviene integrar entre $0$ y $T$ (entre $-L$ y $L$ hay que partir la integral).
- [1:29:14] — El $a_0/2$ muchas veces sale "a ojo" (funciones constantes o lineales); "yo, que soy a veces desconfiado, **si tengo tiempo en un examen, hago la integral para chequear**". Con curvas como $x^2$ a ojo no se puede.
- [54:38] — Paridad e imparidad: "en el tema de Fourier en general, **esto es clave**": repasar cómo identificar una función par/impar y qué pasa al multiplicarlas.
- [1:58:35] — Si al graficar detectan una función par, "ya no calculo el $b_n$, me ahorro la integral, me ahorro equivocarme en eso".
- [1:52:10] — Para sumar series numéricas los puntos que se usan son siempre "o con cero, o con $\pi$, o con $2\pi$", fáciles, en los extremos de cada repetición.

**Errores típicos / detalles de presentación**

- [08:32] — Fasores: chequear siempre **misma frecuencia** ($2t$ y $2t$) y **misma función trigonométrica** (dos cosenos o dos senos): "el fasor no se da cuenta" de si es seno o coseno.
- [20:53] — Al sacar el argumento del fasor suma: los mismos cuidados de cuadrante de siempre (si la calculadora devuelve el cuarto cuadrante y el número está en otro, sumar $\pi$, etc.).
- [19:19] — "En general los ejercicios están pensados para que haya números lindos; **fasores creo que es la única excepción** que hay en la primera parte de la materia": acá hay números feos.
- [28:47] — Redondeo: dejar $\sqrt{20}$ o ponerle "cuatro o cinco dígitos decimales" está bien. "No se vuelvan locos con eso."
- [23:02] / [27:14] — La guía teórica tiene un error en el resultado del ejemplo de fasores con seno y coseno mezclados (el desfasaje expresado como seno está mal).
- [1:18:14] — Con $n = 2k+1$ la sumatoria arranca en $k = 0$; con $n = 2k-1$ arranca en $k = 1$: la primera armónica tiene que ser siempre la $1$. Equivocarse "no es un error garrafal", pero para que quede "prolijita y perfecta" hay que cuidar el límite. [1:18:14] En las próximas series se escribe directamente con $2k+1$.

**Organización de la cursada (lo que se dice en esta clase)**

- [16:34] — Todos los ejemplos de fasores se hacen en la teoría: "meterlo en la práctica es inútil, porque los ejercicios son iguales"; "con esto ya nos damos por practicados el tema de fasores". [27:46] Hay solo dos tipos de ejercicio de fasores: los dos términos con la misma función, o mezcla de seno y coseno (aplicar la identidad).
- [28:16] — Fasores "es parte de la unidad y había que explicarlo".
- [1:53:14] — El martes siguiente es la clase práctica de este tema; la simetría de media onda queda para el jueves (clase virtual) [2:03:54].
- **Números complejos en el primer parcial:** en esta clase **no dice nada** sobre si los números complejos entran o no en el primer parcial. Solo menciona al arrancar que viene del "PDF de números complejos" [00:00] y que hasta ahora practicaron el álgebra de complejos [01:02]. Tampoco habla de promoción, TP ni ayudamemoria.

---

## Fasores: por qué van antes de Fourier — [00:31]

- Fourier es una manera de **representar funciones sumando senos y cosenos de distintas frecuencias**.
- Los **fasores** son una herramienta para **sumar senos o cosenos de la misma frecuencia**.
- Por eso el tema está más relacionado con Fourier que con el álgebra de números complejos vista hasta ahora (el material está en el PDF de números complejos, "síntesis teórica", subido al aula [09:37]).

## Sinusoides y definición de fasor — [01:02]

Las funciones que se suman son sinusoides (senos o cosenos), de forma genérica:

$$
g(t) = A\cos(\omega t + \varphi)
$$

- $A$: **amplitud** — qué tan alto y qué tan bajo llega [01:37].
- $\omega$: **frecuencia** (velocidad angular) — qué tan rápido oscila.
- $\varphi$: **fase o desfasaje** [02:08] — corre la sinusoide a izquierda o derecha sin cambiarle velocidad ni amplitud.

Se asocia el coseno a un número complejo [02:40]:

$$
A\cos(\omega t + \varphi) + j\,A\,\mathrm{sen}(\omega t + \varphi)
$$

$g(t)$ es la **parte real** de ese complejo [03:11]. Pasándolo a forma exponencial y separando por propiedad de potencias de igual base:

$$
g(t) = \mathrm{Re}\left\{A\,e^{j(\omega t + \varphi)}\right\} = \mathrm{Re}\left\{A\,e^{j\varphi}\,e^{j\omega t}\right\}
$$

Se denomina **fasor** de $g(t)$ al número complejo [03:45]:

$$
F = A\,e^{j\varphi}
$$

con $A$ la amplitud y $\varphi$ el desfasaje del coseno (o seno) original. La misma explicación se puede hacer con seno y parte imaginaria [04:16]; según el libro aparece una u otra, es indistinto.

## Propiedades del fasor — [05:21]

- El fasor es un **número complejo** en forma exponencial, y se escribe siempre con **mayúscula**.
- **No depende de la frecuencia** $\omega$ [05:52]: depende solo de la amplitud y del desfasaje. Por lo tanto **un mismo fasor representa infinitas sinusoides** de igual amplitud y desfasaje y distintas frecuencias [08:01].
- El fasor **representa seno o coseno indistintamente** [08:01] (es una técnica "medio caprichosa", útil pero sin un desarrollo teórico súper formal).
- **Condiciones para sumar con fasores** [08:32]: las sinusoides tienen que tener **la misma frecuencia** y ser **la misma función trigonométrica** (dos cosenos o dos senos).

Ejemplo de obtención [06:23]: para $f_1 = 5\cos(2t + \pi/3)$ y $f_2 = 3\cos(2t - \pi/5)$, la amplitud va al módulo y el desfasaje al exponente; el $2t$ no entra en el fasor [06:58]:

$$
F_1 = 5\,e^{j\pi/3}, \qquad F_2 = 3\,e^{-j\pi/5}
$$

## Interpretación gráfica: vectores que giran — [09:07]

- La expresión $A\cos(\omega t + \varphi) + jA\,\mathrm{sen}(\omega t + \varphi)$, a medida que avanza $t$, recorre una **circunferencia** [10:08]: cada sinusoide corresponde a un vector que gira.
- Distinta amplitud → circunferencias de distinto radio [11:10]. Igual $\omega$ → los vectores giran **a la misma velocidad** [11:42]. La diferencia de fase $\varphi_1 - \varphi_2$ es la apertura entre los vectores.
- Cada vector al girar, proyectado sobre un eje, dibuja la sinusoide asociada [12:47].
- En vez de sumar sinusoides se **suman los vectores** (regla del paralelogramo) [13:49]; el vector suma, al girar, dibuja la sinusoide suma [14:25].
- Como giran todos juntos, la resultante es siempre la misma: se toman las **posiciones en $t = 0$**, se suman, y al vector resultante se le asocia la misma velocidad angular [16:01]. Por eso se puede despreciar $e^{j\omega t}$ [14:57].

<details>
<summary>📝 Ejercicio 1 — [16:34]: suma de $5\cos(2t + \pi/3) + 3\cos(2t - \pi/5)$ con fasores</summary>

Obtener, usando fasores, la función suma

$$
g(t) = 5\cos\!\left(2t + \frac{\pi}{3}\right) + 3\cos\!\left(2t - \frac{\pi}{5}\right)
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** chequear que se puede usar fasores [17:05]: misma frecuencia ($2t$ y $2t$) y misma función (dos cosenos). Fasores:

$$
F_1 = 5\,e^{j\pi/3}, \qquad F_2 = 3\,e^{-j\pi/5}
$$

**Paso 2:** la forma exponencial no sirve para sumar, hay que pasar a **binómica** a través de la trigonométrica [18:13]:

$$
F_1 + F_2 = 5\left[\cos\frac{\pi}{3} + j\,\mathrm{sen}\frac{\pi}{3}\right] + 3\left[\cos\left(-\frac{\pi}{5}\right) + j\,\mathrm{sen}\left(-\frac{\pi}{5}\right)\right]
$$

(En la guía se juega con los signos usando propiedades de seno y coseno [18:48]; con la calculadora y $-\pi/5$ directo da lo mismo [19:19].)

**Paso 3:** juntar parte real con parte real e imaginaria con imaginaria [19:50]: queda un complejo con parte real "4,90 y pico" y parte imaginaria "2,5 y pico" [los decimales exactos están en el pizarrón, ver video].

**Paso 4:** módulo y argumento del fasor suma [20:22]:

$$
|F_1 + F_2| = \sqrt{\mathrm{Re}^2 + \mathrm{Im}^2} \approx 5{,}56, \qquad \arg(F_1 + F_2) = \arctan\frac{\mathrm{Im}}{\mathrm{Re}} \approx 0{,}48
$$

Está en el primer cuadrante, así que el arcotangente no trae problemas [20:53].

**Paso 5:** reconstruir la función [21:25]: el módulo es la nueva amplitud, la frecuencia **no se toca** ($2t$) y el argumento es el nuevo desfasaje:

$$
g(t) \approx 5{,}56\cos(2t + 0{,}48)
$$

En GeoGebra la suma de las dos funciones originales y esta función se superponen: son la misma función [22:27].

</details>

</details>

## Seno y coseno mezclados: identidades — [23:02]

Si los dos términos tienen la misma frecuencia pero uno es seno y otro coseno, hay que **llevar los dos a la misma función** (cualquiera de las dos) con [24:05]:

$$
\mathrm{sen}(x) = \cos\!\left(x - \frac{\pi}{2}\right), \qquad \cos(x) = \mathrm{sen}\!\left(x + \frac{\pi}{2}\right)
$$

Seno y coseno son la misma función desfasada $\pi/2$ [24:05].

<details>
<summary>📝 Ejercicio 2 — [23:02]: $g(t) = 2\cos(4t) + 4\,\mathrm{sen}(4t)$ con fasores (ejemplo de la guía teórica)</summary>

Obtener $g(t)$ como la suma

$$
g(t) = 2\cos(4t) + 4\,\mathrm{sen}(4t)
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** chequeo de frecuencias: $4t$ y $4t$, ok [23:35]. Pero hay un seno y un coseno: llevar todo a coseno [24:36].

**Paso 2:** el primero ya es coseno, sin desfasaje [24:36]:

$$
2\cos(4t) \;\rightarrow\; F_1 = 2\,e^{j0} = 2
$$

**Paso 3:** al seno se le resta $\pi/2$ al argumento [25:08]:

$$
4\,\mathrm{sen}(4t) = 4\cos\!\left(4t - \frac{\pi}{2}\right) \;\rightarrow\; F_2 = 4\,e^{-j\pi/2} = -4j
$$

**Paso 4:** sumar en binómica [25:41]: $F_1 + F_2 = 2 - 4j$. Módulo y argumento [26:12]:

$$
|F_1 + F_2| = \sqrt{2^2 + 4^2} \approx 4{,}472, \qquad \arg = \arctan\frac{-4}{2} \approx -1{,}107
$$

Se puede dejar en el cuarto cuadrante; sumarle $2\pi$ también vale, en fasores no cambia [26:12].

**Paso 5:** reconstruir con coseno (porque se sumaron cosenos) [26:42]:

$$
g(t) \approx 4{,}472\cos(4t - 1{,}107)
$$

**Paso 6:** expresado como seno [27:14]: con $\cos(x) = \mathrm{sen}(x + \pi/2)$, al $-1{,}107$ se le suma $1{,}57$ ($\pi/2$) [27:46]:

$$
g(t) \approx 4{,}472\,\mathrm{sen}(4t - 1{,}107 + 1{,}57)
$$

El profe lee el desfasaje resultante como "0,40 y pico" [poco claro en la transcripción]. Las dos formas (coseno y seno) son la misma función y las dos están bien. El resultado de la guía (expresado como seno) tiene el desfasaje mal [27:14].

</details>

</details>

## Serie trigonométrica de Fourier: la guía de la cátedra — [29:20]

La guía oficial de la cátedra explica de dónde sale la serie de forma muy algebraica; en la clase solo se menciona por arriba [29:50].

## Funciones periódicas, período y semiperíodo — [30:22]

La serie de Fourier sirve para **representar funciones periódicas**. Una función es periódica si

$$
f(x) = f(x + T)
$$

con $T \in \mathbb{R}$ el **período**: la función se repite cada $T$.

- Ejemplo: $\cos x$ y $\mathrm{sen}\,x$ se repiten cada $2\pi$ [30:57].
- Ejemplo [31:29]: $f(x) = x$ en $(-1, 1)$ con $f(x) = f(x + 2)$: la identidad entre $-1$ y $1$ que se repite cada 2 unidades ($T = 2$), "bastoncitos" [32:04].

**Semiperíodo** [32:04]:

$$
L = \frac{T}{2}
$$

Para $\cos x$: $T = 2\pi$, $L = \pi$. Para la identidad: $T = 2$, $L = 1$ [32:35].

## Qué funciones se pueden desarrollar: seccionalmente continuas — [32:35]

La serie trigonométrica desarrolla en serie de senos y cosenos **de distinta frecuencia** una función periódica tal que **la integral entre $-L$ y $L$ exista** (no tienda a infinito).

- La identidad en $(-1, 1)$: el área existe (da 0, se compensan positiva y negativa) [33:07].
- Lo que se busca es que no haya **asíntotas verticales** [33:37]: la $\tan x$ es periódica pero tiene saltos infinitos, no cumple [34:08].
- Estas funciones se llaman **seccionalmente continuas** [34:39]: tienen un **número finito de saltos finitos** (sin asíntotas verticales ni infinitos saltos).

Otros ejemplos desarrollables (STF = serie trigonométrica de Fourier) [35:11]:

- $f(x) = x^2$ en $(-2, 2)$, repetida cada 4: se repite la parábola completa [35:42].
- $f(x) = x^2$ en $(0, 2\pi)$, repetida cada $2\pi$: misma fórmula, pero al estar definida distinto se repite solo la rama derecha [36:13].

## La base ortonormal (muy por arriba) — [36:50]

- Todas las funciones seccionalmente continuas forman un conjunto $F$ (la guía habla de un espacio vectorial de dimensión infinita).
- La serie de Fourier escribe cada función de $F$ como **combinación lineal** de las funciones de una **base ortonormal** [37:25].
- Con la integral como operación [37:56]: la base es **ortogonal** si

$$
\int_a^b f_i\, f_j \, dx = 0 \quad (i \neq j)
$$

y **ortonormal** si además [38:29]

$$
\int_a^b f_i\, f_i \, dx = 1
$$

- La base que se usa: $1$, $\cos(nx)$, $\mathrm{sen}(nx)$ [38:29]. Para que sea ortonormal hay que dividir por la norma; el profe dice "creo que" $1/\sqrt{2\pi}$, $1/\sqrt{\pi}$ y $1/\sqrt{\pi}$ [39:00]. Como cada $n$ da un seno y un coseno distinto, la base es infinita.
- "De esto no se tienen que llevar mucho" [39:31]: se escriben combinaciones lineales de senos, cosenos y constantes.

## La serie trigonométrica de Fourier — [40:07]

Dada una función periódica $f(x) = f(x + T)$ integrable en su período (la integral entre $-L$ y $L$, o entre $0$ y $T$, existe) [40:37]:

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty}\left[a_n\cos(n\omega_0 x) + b_n\,\mathrm{sen}(n\omega_0 x)\right]
$$

- **Siempre se integra en un período completo** [40:37]: $(-L, L)$ o $(0, T)$ son los dos que se usan [41:08] (cualquier período completo sirve).
- $\dfrac{a_0}{2}$ es el **valor medio** [42:11]: una constante tal que **el área encerrada entre la función y esa constante por arriba y por abajo es la misma** (se compensan) [42:41].
- Cada par $a_n\cos(n\omega_0 x) + b_n\,\mathrm{sen}(n\omega_0 x)$ es una **armónica** [43:14]; hay infinitas. $n = 1$ es la primera armónica, $n = 2$ la segunda, etc. [43:45].
- $\omega_0$ es la **frecuencia fundamental** [43:45]:

$$
\omega_0 = \frac{\pi}{L} = \frac{2\pi}{T}
$$

- $a_0, a_n, b_n \in \mathbb{R}$ [44:46] y **son lo único que hay que calcular**: $\omega_0$ sale del período, $x$ es la variable y $n$ el índice [45:17].

## De dónde sale $a_0$ — [45:47]

**Paso 1:** integrar miembro a miembro en $(-L, L)$; intercambiar sumatoria e integral es válido [46:19].

**Paso 2:** término constante [47:23]:

$$
\int_{-L}^{L}\frac{a_0}{2}\,dx = \frac{a_0}{2}\cdot 2L = a_0 L
$$

**Paso 3:** término de cosenos [47:54], reemplazando $\omega_0 = \pi/L$ [48:25]:

$$
\int_{-L}^{L} a_n\cos\!\left(\frac{n\pi}{L}x\right)dx = a_n\left[\frac{\mathrm{sen}\left(\frac{n\pi}{L}x\right)}{\frac{n\pi}{L}}\right]_{-L}^{L} = a_n\,\frac{\mathrm{sen}(n\pi) - \mathrm{sen}(-n\pi)}{\frac{n\pi}{L}} = 0
$$

porque **$\mathrm{sen}(n\pi) = 0$ para todo $n$ natural** [48:56] ("algo con lo que nos vamos a cruzar mucho").

**Paso 4:** término de senos [49:29]: no hace falta calcular la primitiva. El seno es **impar**, y **toda función impar integrada en un intervalo simétrico $(-a, a)$ da cero** (se compensan las áreas) [50:01].

**Paso 5:** solo sobrevive $a_0 L$ [50:32]:

$$
a_0 = \frac{1}{L}\int_{-L}^{L} f(x)\,dx
$$

## De dónde salen $a_n$ y $b_n$ — [51:02]

**Paso 1:** multiplicar cada término de la serie por $\cos(m\omega_0 x)$ [51:32], reemplazar $\omega_0 = \pi/L$ e integrar en $(-L, L)$ [52:03].

**Paso 2:** el término $\frac{a_0}{2}\cos\left(\frac{m\pi}{L}x\right)$ da cero por lo mismo de antes ($\mathrm{sen}(n\pi) - \mathrm{sen}(-n\pi)$) [52:34].

**Paso 3:** el producto de cosenos [53:05] (está en la tabla de integrales [53:36]):

$$
\int_{-L}^{L}\cos\!\left(\frac{n\pi}{L}x\right)\cos\!\left(\frac{m\pi}{L}x\right)dx =
\begin{cases} 0 & n \neq m \\ L & n = m \end{cases}
$$

(relacionado con la base ortonormal: con otra frecuencia se anula, consigo misma da un valor).

**Paso 4:** el término seno por coseno [54:08]: impar por par = **impar**, integrado en intervalo simétrico da cero [55:09].

**Paso 5:** sobrevive solo $n = m$ [55:39]:

$$
\int_{-L}^{L} f(x)\cos\!\left(\frac{m\pi}{L}x\right)dx = a_n\int_{-L}^{L}\cos^2\!\left(\frac{n\pi}{L}x\right)dx = a_n L
$$

$$
a_n = \frac{1}{L}\int_{-L}^{L} f(x)\cos(n\omega_0 x)\,dx
$$

**Paso 6:** para $b_n$ se hace lo mismo multiplicando por un seno [56:41]; sobrevive el tercer término, con una integral que vale $0$ si $n \neq m$ y $L$ si son iguales:

$$
b_n = \frac{1}{L}\int_{-L}^{L} f(x)\,\mathrm{sen}(n\omega_0 x)\,dx
$$

## Síntesis: lo que hay que llevarse — [57:15]

Dada $f(x) = f(x + T)$, con $L = T/2$ y $\omega_0 = \pi/L = 2\pi/T$ [57:15]:

$$
f(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty}\left[a_n\cos(n\omega_0 x) + b_n\,\mathrm{sen}(n\omega_0 x)\right]
$$

$$
a_0 = \frac{1}{L}\int_{-L}^{L} f(x)\,dx, \qquad a_n = \frac{1}{L}\int_{-L}^{L} f(x)\cos(n\omega_0 x)\,dx, \qquad b_n = \frac{1}{L}\int_{-L}^{L} f(x)\,\mathrm{sen}(n\omega_0 x)\,dx
$$

(La serie y las fórmulas de $a_n$, $b_n$ con $L = T/2$ están en el ayudamemoria [ayudamemoria].)

- "Esto es lo que se tienen que llevar de hoy" [57:48]: la forma general y las tres integrales.
- Los límites $(-L, L)$ se pueden cambiar por $(0, T)$ según convenga: lo importante es tomar un período completo [59:23].

<details>
<summary>📝 Ejercicio 3 — [59:53]: STF del pulso $f(x) = 1$ en $(0, 3)$, $0$ en $(-3, 0)$, $f(x) = f(x+6)$</summary>

Desarrollar en serie trigonométrica de Fourier la función periódica

$$
f(x) = \begin{cases} 1 & 0 < x < 3 \\ 0 & -3 < x < 0 \end{cases}, \qquad f(x) = f(x + 6)
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** datos y gráfico [59:53]: $T = 6$, $L = 3$, $\omega_0 = \pi/3$. El gráfico es un pulso de altura 1 entre 0 y 3, pegado al eje entre $-3$ y 0, repetido cada 6 [1:00:56].

**Paso 2:** $a_0$ [1:01:26]: la integral se parte como la función; entre $-3$ y $0$ la función es nula y no aporta [1:01:57]:

$$
a_0 = \frac{1}{3}\int_0^3 1\,dx = \frac{1}{3}\cdot 3 = 1 \quad\Rightarrow\quad \frac{a_0}{2} = \frac{1}{2}
$$

A la serie va $a_0/2$, no $a_0$ [1:02:27]. En el gráfico, el rectángulo por debajo de $y = 1/2$ compensa al de arriba [1:03:31].

**Paso 3:** $a_n$ [1:04:02]:

$$
a_n = \frac{1}{3}\int_0^3 \cos\!\left(\frac{n\pi}{3}x\right)dx = \frac{1}{3}\left[\frac{\mathrm{sen}\left(\frac{n\pi}{3}x\right)}{\frac{n\pi}{3}}\right]_0^3
$$

En $3$ queda $\mathrm{sen}(n\pi) = 0$ y en $0$ queda $\mathrm{sen}(0) = 0$ [1:05:02]:

$$
a_n = 0
$$

(Más adelante va a mostrar cómo saber de antemano que $a_n$ da cero y ahorrarse la cuenta [1:05:02].)

**Paso 4:** $b_n$ [1:05:33]:

$$
b_n = \frac{1}{3}\int_0^3 \mathrm{sen}\!\left(\frac{n\pi}{3}x\right)dx = \frac{1}{3}\left[\frac{-\cos\left(\frac{n\pi}{3}x\right)}{\frac{n\pi}{3}}\right]_0^3
$$

Barrow: en $3$ queda $-\cos(n\pi)$ y en $0$ queda $\cos 0 = 1$ [1:06:04].

**Paso 5:** el coseno de múltiplos enteros de $\pi$ alterna [1:06:35]: $\cos\pi = -1$, $\cos 2\pi = 1$, $\cos 3\pi = -1$, … [1:07:07]:

$$
\cos(n\pi) = (-1)^n
$$

(análogo a $\mathrm{sen}(n\pi) = 0$) [1:08:14].

**Paso 6:** reacomodando signos [1:08:44]:

$$
b_n = \frac{1}{n\pi}\left[1 - (-1)^n\right]
$$

**Paso 7:** serie [1:09:16]: no hay cosenos porque $a_n = 0$:

$$
f(x) = \frac{1}{2} + \sum_{n=1}^{\infty}\frac{1 - (-1)^n}{n\pi}\,\mathrm{sen}\!\left(\frac{n\pi}{3}x\right)
$$

**Paso 8:** interpretación [1:09:47]: a medida que se agregan términos, la suma se parece cada vez más a la función original (GeoGebra con deslizador hasta 100 términos [1:11:54]); en el límite $n \to \infty$ son iguales, salvo una diferencia "súper teórica" en los saltos [1:12:25].

**Paso 9:** solo armónicas impares [1:14:03]: si $n$ es par, $1 - 1 = 0$; si $n$ es impar, $1 - (-1) = 2$ [1:15:06]:

$$
b_n = \begin{cases} \dfrac{2}{n\pi} & n \text{ impar} \\[2mm] 0 & n \text{ par} \end{cases}
$$

**Paso 10:** reemplazar $n = 2k+1$ en todos lados (denominador y argumento del seno), con $k$ desde $0$ [1:16:39]–[1:17:44]:

$$
f(x) = \frac{1}{2} + \sum_{k=0}^{\infty}\frac{2}{(2k+1)\pi}\,\mathrm{sen}\!\left((2k+1)\frac{\pi}{3}x\right)
$$

Las dos series son válidas, pero esta es "más eficiente" porque se ahorra las armónicas pares [1:18:45].

</details>

</details>

## Solo armónicas impares: $n = 2k+1$ — [1:13:31]

- Cuando un coeficiente queda de la forma $1 - (-1)^n$, **las armónicas pares valen cero** [1:14:03]: sumarlas es sumar ceros (en GeoGebra, pasar de 1 a 2 armónicas no cambia nada [1:14:35]). "Esto nos lo vamos a encontrar un montón" [1:15:06].
- Se reescribe la serie con **$n = 2k+1$** (o $n = 2k-1$) reemplazando **todas** las $n$ [1:16:08]–[1:16:39].
- **Límite de la sumatoria** [1:17:44]: la primera armónica tiene que ser siempre la 1:
  - con $2k+1$, $k$ arranca en $0$;
  - con $2k-1$, $k$ arranca en $1$ [1:18:14].
- De ahora en más, cuando pase esto se escribe directamente la serie con $2k+1$ [1:18:14].

## Propiedades de la serie — [1:18:45]

**Propiedad 1** [1:19:18] (no se le da demasiada importancia):

$$
\lim_{n \to \infty} a_n = \lim_{n \to \infty} b_n = 0
$$

Los valores de $a_n$ y $b_n$ se denominan **espectros discretos** (discretos porque $n$ es natural) [1:19:48].

**Propiedad 2 — teorema de Dirichlet** [1:19:48]: si $S(x)$ es la serie trigonométrica de Fourier y $a$ un valor del dominio,

$$
S(a) = \frac{f(a^-) + f(a^+)}{2}
$$

- La serie toma en cada punto la **semisuma de los límites laterales** de la función [1:20:18].
- Según el profe, la serie es una función continua y la original no (tiene saltos) [1:20:49]: la única diferencia entre ambas está en las discontinuidades, donde la serie toma un valor y la función puede no tenerlo [1:21:20]. El nombre de teorema de Dirichlet "no está escrito" en el PDF, lo comenta él [1:22:54].
- Ejemplo con el pulso del ejercicio 3 [1:21:20]–[1:21:50]: en $x = 0$ (discontinuidad; la función ni siquiera está definida ahí porque los intervalos son abiertos [1:22:23]):

$$
S(0) = \frac{0 + 1}{2} = \frac{1}{2}
$$

- En un punto de continuidad, por ejemplo $x = 1$, la semisuma da el valor de la función: $S(1) = \frac{1 + 1}{2} = 1$ [1:22:54]–[1:23:25]. Ahí "es un poco obvio", alcanza con ver el gráfico.

<details>
<summary>📝 Ejercicio 4 — [1:25:00]: STF de $f(x) = x^2$ en $(0, 2\pi)$, $f(x) = f(x + 2\pi)$</summary>

Dada la función periódica $f(x) = x^2$ en $(0, 2\pi)$ con período $2\pi$, desarrollar la serie trigonométrica de Fourier.

<details>
<summary>Ver resolución</summary>

**Paso 1:** gráfico y datos [1:25:00]–[1:25:32]: la rama derecha de la parábola entre $0$ y $2\pi$, repetida cada $2\pi$. $T = 2\pi$, $L = \pi$, $\omega_0 = \pi/\pi = 1$.

**Paso 2:** elegir el intervalo [1:26:03]: la función viene definida entre $0$ y $T$, así que conviene integrar entre $0$ y $2\pi$. Entre $-\pi$ y $\pi$ también se puede, pero hay que partir la integral: en $(0, \pi)$ vale $x^2$ y en $(-\pi, 0)$ vale $(x + 2\pi)^2$ [1:27:05].

**Paso 3:** $a_0$ [1:27:05]–[1:27:36]:

$$
a_0 = \frac{1}{\pi}\int_0^{2\pi} x^2\,dx = \frac{8\pi^2}{3} \quad\Rightarrow\quad \frac{a_0}{2} = \frac{4\pi^2}{3}
$$

Acá no se puede ver a ojo que las áreas se compensan [1:28:43].

**Paso 4:** $a_n$ [1:29:46]: ahora la $x^2$ multiplica al coseno; la primitiva se copia de la tabla de integrales [1:30:46] [paso en el pizarrón, ver video]:

$$
a_n = \frac{1}{\pi}\int_0^{2\pi} x^2\cos(nx)\,dx
$$

**Paso 5:** Barrow término a término [1:30:46]–[1:32:49]:

- El término con $2x\cos(nx)$ en $2\pi$: $\cos(2n\pi) = 1$ siempre [1:31:18], queda $\frac{4\pi}{\pi n^2}$ y se simplifica a $\frac{4}{n^2}$ [1:31:49].
- Los términos con $\mathrm{sen}(nx)$ en $2\pi$: $\mathrm{sen}(2n\pi) = 0$ [1:32:19].
- En $0$: el término con $2x$ se anula por la $x$, y $\mathrm{sen}(0) = 0$ [1:32:49].

$$
a_n = \frac{4}{n^2}
$$

**Paso 6:** $b_n$ [1:33:19]:

$$
b_n = \frac{1}{\pi}\int_0^{2\pi} x^2\,\mathrm{sen}(nx)\,dx
$$

Por tabla [paso en el pizarrón, ver video]. El primer término (con seno) se anula en $2\pi$ y en $0$ [1:33:50]. El segundo, $\left(\frac{2}{n^3} - \frac{x^2}{n}\right)\cos(nx)$, en $2\pi$ da $\frac{2}{n^3} - \frac{4\pi^2}{n}$ (con $\cos(2n\pi) = 1$) y en $0$ da $\frac{2}{n^3}$ [1:34:21]–[1:34:53]:

$$
b_n = \frac{1}{\pi}\left(\frac{2}{n^3} - \frac{4\pi^2}{n} - \frac{2}{n^3}\right) = -\frac{4\pi^2}{n\pi} = -\frac{4\pi}{n}
$$

Acá no aparece $(-1)^n$, así que no hay análisis de par/impar [1:35:24].

**Paso 7:** serie [1:35:57]:

$$
f(x) = \frac{4\pi^2}{3} + \sum_{n=1}^{\infty}\left[\frac{4}{n^2}\cos(nx) - \frac{4\pi}{n}\,\mathrm{sen}(nx)\right]
$$

**Paso 8:** con una sola armónica queda $\frac{4\pi^2}{3} + 4\cos x - 4\pi\,\mathrm{sen}\,x$ [1:37:29]; agregando armónicas se parece cada vez más a la original [1:36:58]. Cada armónica tiene **una frecuencia distinta** (1, 2, 3, …): Fourier suma senos y cosenos de **distintas** frecuencias, mientras que fasores suma los de la **misma** [1:38:00].

</details>

</details>

## Espectro de frecuencias y usos — [1:38:30]

- Graficar $a_n$ (y $b_n$) en función de $n$ da **puntos discretos** separados de a 1 [1:39:02]. En el ejercicio 4: $a_1 = 4$, $a_2 = 1$, … tienden a 0 (propiedad 1) [1:39:33]; $b_n$, negativo, tiende a 0 desde abajo.
- Aplicar Fourier a una señal la **descompone en sus frecuencias**: por eso estos gráficos se llaman **espectro de frecuencias** [1:40:04]–[1:40:34] (se ve mejor en la clase de serie exponencial).
- Usos que comenta [1:41:06]–[1:43:10] (con transformada de Fourier, "para el caso es lo mismo"): compresión de audio descartando frecuencias inaudibles o ruido, compresión de imágenes, el acorde inicial de *A Hard Day's Night* reconstruido por sus frecuencias [1:42:08], análisis de sismógrafos para detectar pruebas nucleares [1:42:39]. Dejó en el campus un link para dibujar con series de Fourier [1:43:10].

<details>
<summary>📝 Ejercicio 5 — [1:43:41]: hallar $\sum_{n=1}^{\infty} \frac{1}{n^2}$ (problema de Basilea) con la serie del ejercicio 4</summary>

A partir de la serie obtenida en el ejercicio 4, hallar el valor de

$$
\sum_{n=1}^{\infty}\frac{1}{n^2}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** "jugar a las diferencias y similitudes" [1:44:43]: en la serie aparece $\frac{4}{n^2}\cos(nx)$, parecido a lo buscado. Hay que sacarse de encima el coseno y el seno [1:45:14]; las constantes ("las constantes son amigas") no molestan [1:46:47].

**Paso 2:** elegir $x = 0$ [1:46:16]: $\cos 0 = 1$ (sobrevive el $\frac{4}{n^2}$) y $\mathrm{sen}\,0 = 0$ (desaparece el término de $b_n$).

**Paso 3:** $f(0)$ no está definida (los intervalos son abiertos) [1:47:50], así que se usa la serie y el teorema de Dirichlet [1:47:50]–[1:48:57]: por izquierda vale $(x + 2\pi)^2$ en $0$, o sea $4\pi^2$ [1:48:25]; por derecha vale $x^2$ en $0$, o sea $0$:

$$
S(0) = \frac{f(0^-) + f(0^+)}{2} = \frac{4\pi^2 + 0}{2} = 2\pi^2
$$

**Paso 4:** evaluar la serie en $x = 0$ [1:49:28]:

$$
S(0) = \frac{4\pi^2}{3} + \sum_{n=1}^{\infty}\frac{4}{n^2} = 2\pi^2
$$

**Paso 5:** despejar [1:49:59]: el $\frac{4\pi^2}{3}$ pasa restando y el $4$ pasa dividiendo [1:50:32]:

$$
\sum_{n=1}^{\infty}\frac{1}{n^2} = \frac{\pi^2}{6}
$$

(El valor al que llegó Euler.)

</details>

</details>

## Qué puntos elegir para sumar series — [1:51:05]

- En la guía (parte 2, series de Fourier, ejercicio 1) los ítems siguientes quedan de tarea [1:51:36]: hallar la serie del punto C (función definida entre $-\pi$ y $\pi$ en vez de entre $0$ y $2\pi$, lo que cambia la serie) y con ella sumar $\sum \frac{(-1)^n}{n^2}$.
- El objetivo es siempre que la serie de Fourier **se parezca lo más posible a la serie que se quiere sumar**: anular el seno o el coseno que "no pega ni con cola" y volver $1$ (o $\pm 1$) al que acompaña a la parte parecida [1:52:10]–[1:52:42].
- Los puntos que se usan son siempre fáciles: **$0$, $\pi$, $2\pi$**, en los extremos de cada repetición del gráfico [1:52:10].

## Funciones pares e impares — [1:53:46]

**Definiciones:**

- **Par:** $f(x) = f(-x)$. Ejemplos: $x^2$, $\cos x$ [1:53:46].
- **Impar:** $f(x) = -f(-x)$. Ejemplos: la identidad $x$, $\mathrm{sen}\,x$ [1:54:18].

**Productos** (usados a lo largo de la clase): par · par = par [1:57:01]; par · impar = impar [1:57:32]; impar · impar = par [2:00:43].

**Integrales en intervalo simétrico $(-L, L)$:**

- Función par: las dos ramas tienen la misma área espejada → se integra solo la mitad derecha y se multiplica por 2 [1:55:59]–[1:56:30].
- Función impar: las áreas se compensan → da cero [1:58:05].

**Si $f$ es par** [1:55:27]:

$$
a_0 = \frac{2}{L}\int_0^L f(x)\,dx, \qquad a_n = \frac{2}{L}\int_0^L f(x)\cos(n\omega_0 x)\,dx, \qquad b_n = 0
$$

- $f \cdot \cos$ es par · par = par → se puede hacer "por 2 y media rama" [1:57:01].
- El gran beneficio [1:57:32]: $f \cdot \mathrm{sen}$ es par · impar = impar → $b_n = 0$ [1:58:05]. **Una función par da una serie solo de cosenos** (más el valor medio) [1:58:35].

**Si $f$ es impar** [1:59:06]:

$$
a_0 = 0, \qquad a_n = 0, \qquad b_n = \frac{2}{L}\int_0^L f(x)\,\mathrm{sen}(n\omega_0 x)\,dx
$$

- $a_0 = 0$: integrar una impar en intervalo simétrico; **las funciones impares no tienen valor medio** [1:59:06].
- $a_n = 0$: impar · par (coseno) = impar [1:59:36]–[2:00:08].
- $b_n$: impar · impar = par → "por 2 y media rama" [2:00:43]. **Una función impar da una serie solo de senos** [2:00:08].

## Paridad en los ejemplos de la clase — [2:01:49]

- Los ejercicios 3 y 4 no tienen simetría, por eso tienen $a_n$ y $b_n$ [2:01:49].
- El pulso del ejercicio 3 es "muy particular": se le anula $a_n$ porque "es parecida a una función impar, pero no es una función impar"; se explica en la clase práctica [2:02:20].
- $x^2$ en $(-2, 2)$ es **par** → $b_n$ ni se calcula [2:02:51].
- La identidad repetida en $(-1, 1)$ es **impar** → $a_0/2 = a_n = 0$, serie solo de senos [2:03:22].
- El coseno es par → $b_n$ se anula ("es una serie muy particular", se trabaja después) [2:03:22].

## Lo que quedó para la próxima clase — [2:03:54]

- **Simetría de media onda** y sus implicaciones: queda para "5 minutos" de la clase del jueves (virtual); se puede leer antes en el PDF [2:03:54]. No se desarrolla en esta clase. (La definición figura en el ayudamemoria: $f(x) = -f(x + T/2)$ [ayudamemoria].)
- En esta clase **no** se ven la impar desplazada (solo se menciona que el pulso "es parecido a una impar" [2:02:20]) ni el completar funciones definidas en medio período.

---

*Apunte generado el 2026-10-02 a partir de la transcripción local con Whisper de `T_serie_trigonometrica_fourier.mp4` (125 min) y del ayudamemoria oficial (pág. 1) para notación.*
