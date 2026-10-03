# Sistemas estables (clase teórica grabada)

> Fuente: fuentes/clases/Sistemas Estables/T_SE - Teorica.mp4 (transcripción local con Whisper)

---

> **Cómo usar este apunte.** Es la **teoría** de la unidad, tal como la da el profe en la
> clase grabada (dos PDFs: "Función de transferencia" y "Sistemas estables"). La práctica
> está en `05-practica-sistemas-estables.md` (OneNote) y `11-video-practica-sistemas-estables.md`
> (práctica grabada). Los timestamps `[mm:ss]` son del video local (sin enlace público).
> Las fórmulas se reconstruyeron solo donde lo dictado no deja dudas.

## Índice

- [00:00] — Función de transferencia: entrada, salida y diagrama de bloques
- [02:40] — $G(s)$ como cociente de polinomios: coeficientes reales, grados y la constante $K$
- [06:23] — Ceros y polos: definición por límite y factores que se simplifican
- [07:27] — 📝 Ejercicio 1: una raíz común que no es ni cero ni polo
- [09:31] — Constelación de polos y ceros y el cero en el infinito
- [10:39] — 📝 Ejercicio 2: constelación de $\frac{5(s+2)}{(s-1)(s^2+4s+13)}$
- [13:55] — Gráfica de $|G(s)|$: la función módulo en 3D (volcanes, pozos y aplanamiento)
- [17:14] — 📝 Ejercicio 3: superficie $|G(s)|$ de $\frac{3s}{(s-2)(s+4)}$
- [21:57] — Cortes de la superficie: corte por el eje real
- [29:16] — Corte por el eje imaginario (respuesta en frecuencia, $j\omega$)
- [35:07] — 📝 Ejercicio 4: $\frac{3(s-1)s}{(s-2)(s^3+s)}$: simplificar, constelación y cortes
- [40:19] — Polos complejos conjugados en el corte por el eje real: la "montañita"
- [47:15] — Consulta: ¿y los ceros complejos conjugados en los cortes?
- [51:24] — Módulo de $G$ en un punto: tres métodos (analítico, con módulos, gráfico)
- [51:55] — 📝 Ejercicio 5: $|G(2j)|$ de $\frac{3s}{(s+2)(s^2+1)}$ por los tres métodos
- [1:01:20] — Argumento de $G$ en un punto por el método gráfico
- [1:02:23] — 📝 Ejercicio 6: $\arg G(2j)$ de la misma función
- [1:06:37] — Sistemas estables: entrada, transferencia y salida en $t$ y en $s$
- [1:08:47] — 📝 Ejercicio 7 (guía, ej. 9): constelación y respuesta a $f(t) = e^{-2t}$
- [1:14:02] — Valor estable y definición de sistema estable
- [1:17:11] — Estabilidad según los polos: polos simples y múltiples
- [1:19:16] — Caso 1: polo real negativo → exponencial decreciente
- [1:21:56] — Caso 2: polos complejos conjugados con parte real negativa → oscilatoria amortiguada (factor $\alpha$)
- [1:27:40] — Caso 3: polo nulo
- [1:29:11] — Caso 4: polos imaginarios puros → oscilatoria de amplitud constante
- [1:32:52] — Marginalmente (o críticamente) estable
- [1:33:24] — Casos 5 y 6: polos con parte real positiva → inestable
- [1:36:00] — Conclusión: condición necesaria y suficiente de estabilidad
- [1:38:45] — 📝 Ejercicio 8 (guía, ej. 6 g): construir $G(s)$ con polos, ceros y $|G(j)| = \sqrt{5/2}$
- [1:45:02] — 📝 Ejercicio 9 (guía, ej. 6 h): construir $G(s)$ desde el corte por el eje real, $G(0)$ y $G(1)$
- [1:49:13] — Consultas finales: estabilidad y tipo de respuesta de 6 g y 6 h, entradas acotadas

## Lo que el profe remarca

**Sobre el parcial (qué se toma y cómo)**

- **[1:05:05]** "Esto se toma bastante": graficar la **constelación de polos y ceros** y hallar el **módulo** (más que el argumento, "aunque el argumento también puede aparecer") de $G$ en un punto es "el típico primer punto de un ejercicio de sistemas estables".
- **[1:50:15]** Decir el **tipo de respuesta** (p. ej. oscilatoria amortiguada) "es algo muy típico que se pida".
- **[16:37]** "Nunca" les van a pedir un gráfico en 3D a mano. **[21:57]** Lo que **sí** es parte de los ejercicios son los **cortes** de la superficie, y siempre con dos planos: el del eje real o el del eje imaginario **[22:27]**.
- **[27:12]** Los gráficos de los cortes son **conceptuales**: no importa el ancho de las asíntotas ni la altura; hay que marcar los **hitos** (asíntotas verticales en los polos, asíntota horizontal en el infinito, ceros donde toca el eje, montañitas). **[44:36]**–**[45:08]** Si la montañita en GeoGebra cae en otro lugar o es menos marcada, "no me importa".
- **[45:08]** Hay ejercicios donde **les dan el corte por el eje real y tienen que reconstruir la función de transferencia**; esos gráficos vienen **exagerados** a propósito para que se note el par de polos complejos **[45:43]** (ver Ejercicio 9).
- **[50:52]** En los ejercicios de la cátedra, el corte por el eje imaginario suele ser "menos interesante" que el corte por el eje real.
- **[1:01:20]** Para el módulo en un punto pueden usar cualquiera de los métodos "a discreción", **salvo que el ejercicio diga "por el método gráfico"**.
- **[1:04:33]**–**[1:05:05]** El argumento se puede dejar negativo ($-3\pi/4$) o en el primer giro positivo ($5\pi/4$): "lo mismo, salvo que se aclare".
- **[1:13:00]** Las fracciones simples se dan por sabidas: en estos ejercicios "voy directamente con cuánto dan el A, B, C".
- **[1:26:06]** **Factor de amortiguamiento $\alpha$**: lo vio por primera vez en el enunciado del "último final, o el anteúltimo"; lo cuenta "por si les aparece".
- **[1:17:42]**–**[1:19:16]** **Polos múltiples**: en todos los ejercicios que vio "siempre hablamos de polos simples"; los menciona por arriba **[1:37:05]** ("no le damos mucha pelota").
- **[1:06:07]** La segunda parte (sistemas estables, análisis de polos) le parece la más importante de la clase, aunque es más aplicada que teórica.

**Errores típicos y trucos**

- **[05:53]** **La constante $K$ siempre está**, aunque "entre comillas" no se vea (vale 1). Al **armar** una transferencia a partir de datos "muchas veces se olvidan de esta constante". **[1:43:29]**–**[1:43:59]** Si en el 6 g ponés $K = 1$, no se cumple el dato $|G(j)| = \sqrt{5/2}$.
- **[08:29]**–**[09:00]** "Casi todos los ejercicios" tienen **algo que se simplifica** entre numerador y denominador: chequear raíces de arriba y de abajo y **cancelar las comunes**, porque no son ni ceros ni polos. Lo repite "hasta el hartazgo" en **[1:09:49]**.
- **[12:12]** El **cero en el infinito** siempre existe; "no es súper grave olvidárselo, pero si pedimos cuáles son los polos y los ceros, está bueno que lo pongan".
- **[13:22]** Si un polo o cero está fuera del eje real, **sí o sí** está también su conjugado (coeficientes reales).
- **[19:50]**–**[20:21]** $|G|$ nunca es negativo: en un cero el gráfico **toca el piso y rebota**, no lo perfora.
- **[30:18]** El **origen es un "comodín"**: cuenta como real y como imaginario puro, así que un cero (o polo) en $0$ aparece en los **dos** cortes.
- **[46:44]** La montañita de un par conjugado va en la **parte real** del par, que no tiene por qué ser $0$ ("para que no se queden que siempre tiene que ser con parte real cero").
- **[48:18]** Los **ceros complejos conjugados no se ven** en ninguno de los dos cortes: "no hay que marcarlo de ninguna manera".
- **[1:44:32]** En el corte, que un **cero sea doble o simple no importa**: simplemente toca el eje.
- **[1:12:28]** La **entrada suele estar pensada para simplificar** algo con la transferencia (no siempre).
- **[1:28:41]** El **polo nulo simple sigue siendo estable** ("Eso es importante"), aunque ya no tiende a cero.
- **[1:38:14]** "Por más que tengan 52.000 polos del lado izquierdo", **un solo polo del lado derecho** hace inestable al sistema.
- **[1:51:46]** Un sistema **marginalmente estable se considera estable** (una constante o algo que oscila sin parar, sin exponencial decreciente).
- **[1:15:37]** Ojo con el video: al cerrar el ejercicio 9 de la guía dice "decimos que el sistema es estable", pero el límite da infinito y en **[1:16:39]** lo corrige: es **inestable**. Lo mismo en **[1:33:55]**: en el caso 5 del PDF "creo que me quedó mal" el signo de $a$.

## Función de transferencia: entrada, salida y diagrama de bloques — [00:00]

- La unidad se llama **sistemas estables** y se ve en dos partes (dos PDFs): **función de transferencia** y **sistemas estables** [00:00].
- Todo se apoya en lo último que vieron: la **transformada de Laplace** es la herramienta para resolver los ejercicios de la unidad [00:31].
- Una **función de transferencia** $G(s)$ es una función de variable compleja, de los complejos en los complejos (técnicamente los complejos ampliados, con el infinito, vía la esfera de Riemann, que está en la guía teórica) [00:31]–[01:03]: le das un complejo y devuelve un complejo.
- **Diagrama de bloques** [01:03]: a la transferencia $G(s)$ (la "cajita") le entra una **entrada** $F(s)$ y devuelve una **salida o respuesta** $Y(s)$. Se usa para modelizar problemas físicos, económicos, circuitos, un carrito atado a un resorte con rozamiento, etc. [01:36].
- Todo está en la variable $s$ porque se trabaja en el dominio de Laplace [02:10].

La "biblia" del tema [02:10]–[02:40]: **transferencia = salida sobre entrada**.

$$
G(s) = \frac{Y(s)}{F(s)} \qquad\Longleftrightarrow\qquad Y(s) = G(s)\,F(s)
$$

## $G(s)$ como cociente de polinomios: coeficientes reales, grados y la constante $K$ — [02:40]

$G(s)$ es un cociente de dos polinomios de variable compleja con **coeficientes reales** [02:40], con dos características [03:11]:

- los coeficientes $a_i$ y $b_j$ son **números reales** (siempre se trabaja así);
- el **grado del denominador es mayor que el del numerador** (lo mismo que ya pasaba al hacer fracciones simples [03:43]).

Se escribe factorizada, dejando claras las raíces de arriba y de abajo [03:11], con la notación de productoria [04:45]:

$$
G(s) = K\,\frac{\prod_{i}(s - z_i)}{\prod_{j}(s - p_j)}
$$

- **Raíces reales o complejas conjugadas** [03:43]–[04:14]: por el teorema fundamental del álgebra, si el polinomio tiene coeficientes reales sus raíces son reales o pares de complejas conjugadas. En los ejercicios solo aparecen "pares de complejas conjugadas o números reales sueltos".
- **La constante $K$** [04:45]–[05:21]: es el cociente entre el coeficiente del término de mayor grado del numerador y el del denominador (al factorizar "hay que sacar siempre para afuera el coeficiente del término de mayor grado"). Si no se ve, es un 1, "pero siempre está" [05:53].

## Ceros y polos: definición por límite y factores que se simplifican — [06:23]

- A las raíces del numerador $z_i$ se las llama **ceros**; a las del denominador $p_j$, **polos** [06:23].
- Definición formal [06:57]:

$$
z_i \text{ es cero de } G \iff \lim_{s \to z_i} G(s) = 0
\qquad\qquad
p_j \text{ es polo de } G \iff \lim_{s \to p_j} G(s) = \infty
$$

- Esta definición permite **descartar** los números que anulan factores que se **simplifican** entre numerador y denominador [06:57]–[07:27]: en esos puntos el límite da un número finito no nulo, así que no son ni ceros ni polos.
- Una vez cancelado todo y reducido a la mínima expresión, los ceros son las raíces del numerador y los polos las del denominador, sin pensar en el límite [09:00].
- Polos y ceros se llaman **singularidades** de la función [09:00].

<details>
<summary>📝 Ejercicio 1 — 07:27: una raíz común que no es ni cero ni polo</summary>

Ejemplo inventado en clase: ¿es $s = 3$ cero o polo de la siguiente $G$?

$$
G(s) = \frac{2(s-1)(s-3)}{(s-j)(s+j)(s-3)}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** $s = 3$ anula el numerador y el denominador, así que "podrían decir, che, el 3 es tanto un cero como un polo" [07:58].

**Paso 2:** pero el límite de $G(s)$ cuando $s \to 3$ no tiende ni a $0$ ni a $\infty$: da un número que no es cero ni infinito [07:58]–[08:29].

**Paso 3:** por lo tanto $3$ no es ni cero ni polo; equivale a simplificar el factor $(s-3)$ y no tenerlo en cuenta [08:29].

</details>

</details>

## Constelación de polos y ceros y el cero en el infinito — [09:31]

- Como polos y ceros pueden ser complejos, se representan en el **plano complejo** (el mismo de la primera unidad): la **constelación de polos y ceros** [09:31]–[10:07].
- **Polos con crucecitas, ceros con circulitos** [10:07].
- Los reales quedan sobre el eje horizontal; si un polo o cero está fuera del eje de abscisas es complejo y **debe estar también su conjugado** [13:22].
- **Cero en el infinito** [11:11]–[12:12]: como el grado del denominador es mayor que el del numerador, $\lim_{s\to\infty} G(s) = 0$, que cumple la definición de cero. "Siempre va a existir un cero en el infinito". Es lo que hace que las gráficas se achaten y se acerquen asintóticamente al eje real a los costados. Para la constelación no se le da mucha importancia, pero si piden los polos y ceros conviene ponerlo [12:12].

<details>
<summary>📝 Ejercicio 2 — 10:39: constelación de 5(s+2)/((s−1)(s²+4s+13))</summary>

Hallar los polos y ceros y graficar la constelación de

$$
G(s) = \frac{5(s+2)}{(s-1)(s^2 + 4s + 13)}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** no hay nada para simplificar ("es un ejemplo fácil") [10:39].

**Paso 2 (polos):** raíces del denominador: $1$ y el par complejo conjugado $-2 \pm 3j$ [10:39].

**Paso 3 (ceros):** $-2$ y el cero en el infinito [10:39]–[11:42].

**Paso 4 (constelación):** circulito en $-2$ y cruz en $1$, ambos sobre el eje real; dos cruces con parte real $-2$ y partes imaginarias $3$ y $-3$ [12:12]–[12:50].

</details>

</details>

## Gráfica de $|G(s)|$: la función módulo en 3D (volcanes, pozos y aplanamiento) — [13:55]

- Graficar $G$ completa necesitaría **cuatro dimensiones** (parte real e imaginaria de la entrada y de la salida) [13:55]–[14:28]. En su lugar se grafica solo la **función módulo** [14:28]–[15:03]:

$$
|G| : \mathbb{C} \to \mathbb{R}_{\geq 0}, \qquad s \mapsto |G(s)|
$$

- También existe la **función argumento**, pero no se le da importancia (además habría que fijar en qué giro se toma el argumento) [15:36]–[16:07].
- Con el módulo quedan **tres dimensiones**: parte real y parte imaginaria de la entrada, y el módulo hacia arriba [16:07]–[16:37]. Los gráficos 3D se ven en GeoGebra; nunca se piden a mano [16:37]–[17:14].
- **Polos → "volcanes" o "montañas"**: es la versión en 3D de las asíntotas verticales; representan un punto de discontinuidad [18:15]–[19:20].
- **Ceros → "pozos"**: la superficie se hunde, toca el piso y vuelve a subir. Como es un módulo, **siempre está para arriba**: donde hay un cero la superficie cae pero **rebota**, no perfora el piso [19:50]–[20:21].
- **Cero en el infinito → aplanamiento**: hacia los costados la superficie se achata y tiende a $0$; es la versión en 3D de la asíntota horizontal [20:53]–[21:25].

<details>
<summary>📝 Ejercicio 3 — 17:14: superficie |G(s)| de 3s/((s−2)(s+4))</summary>

Sea

$$
G(s) = \frac{3s}{(s-2)(s+4)}
$$

Describir la gráfica de $|G(s)|$ (hecha en GeoGebra).

<details>
<summary>Ver resolución</summary>

**Paso 1 (polos y ceros):** cero en el origen ($s = 0$), cero en el infinito y polos en $2$ y $-4$ [17:45].

**Paso 2 (volcanes):** en $2$ y $-4$ hay dos "volcanes"; si fuera la función real $\frac{3x}{(x-2)(x+4)}$ serían asíntotas verticales [18:15]–[18:50].

**Paso 3 (pozo):** en el origen la superficie se hunde, toca el cero y vuelve a subir [19:20]–[19:50].

**Paso 4 (aplanamiento):** hacia izquierda y derecha la superficie se aplana: es el cero en el infinito [20:53]–[21:25].

</details>

</details>

## Cortes de la superficie: corte por el eje real — [21:57]

- Como graficar en 3D a mano no es sencillo, se **corta la superficie con planos convenientes** (esto "sí va a ser parte de ejercicios"): siempre el plano del **eje real** o el del **eje imaginario** [21:57]–[22:27].
- **Corte por el eje real**: intersección de la superficie $|G|$ con el plano donde la parte imaginaria se anula [22:27]–[22:59]. El dominio es real: se elimina la parte imaginaria y se mira solo $x = \mathrm{Re}(s)$ (al eje también se lo nota $\mathrm{Re}(z)$ o $\sigma$) [24:03]–[25:06]:

$$
s = x + yj,\ y = 0 \quad\Longrightarrow\quad |G(x)|, \quad x \in \mathbb{R}
$$

Cómo se dibuja [25:06]–[26:41]: mirar de la lista de polos y ceros **solo los que son números reales**:

- **polo real → asíntota vertical**;
- **cero real → el gráfico toca el eje** (y rebota, porque es un módulo);
- **a los costados se achata** (asíntota horizontal en $0$, por el cero en el infinito).

En el ejemplo $G(s) = \frac{3s}{(s-2)(s+4)}$ todos los polos y ceros son reales: asíntotas verticales en $-4$ y en $2$, toca el eje en $0$, y se achata a los costados [25:37]–[26:10]. El gráfico es el de la función real [28:14]:

$$
|G(x)| = \left|\frac{3x}{(x-2)(x+4)}\right|
$$

## Corte por el eje imaginario (respuesta en frecuencia, $j\omega$) — [29:16]

- También llamado **respuesta en frecuencia** o corte $j\omega$ (la parte imaginaria se asocia a la frecuencia) [29:16].
- Es la intersección con el plano donde la **parte real** se anula ($x = 0$) [29:47]. Ahora se mira la lista de polos y ceros buscando los **imaginarios puros** [29:47]–[30:18].
- **El $0$ es un "comodín"**: es tanto real como imaginario puro, así que cuenta para los dos cortes [30:18].

En el ejemplo $G(s) = \frac{3s}{(s-2)(s+4)}$ [30:18]–[31:56]: $-4$ y $2$ son reales (no cuentan); el único elemento interesante es el cero en el origen. El gráfico viene pegado al eje desde $-\infty$, sube un poco, baja a tocar el $0$, rebota y vuelve a achatarse hacia $+\infty$ ("como un pajarito en el horizonte" [32:31]). Evaluando en $s = yj$ y distribuyendo los módulos [33:35]–[34:06]:

$$
|G(yj)| = \frac{3\,|y|}{\sqrt{(-2)^2 + y^2}\,\sqrt{4^2 + y^2}}
$$

<details>
<summary>📝 Ejercicio 4 — 35:07: 3(s−1)s/((s−2)(s³+s)): simplificar, constelación y cortes</summary>

Dada

$$
G(s) = \frac{3(s-1)\,s}{(s-2)(s^3+s)}
$$

hallar la constelación de polos y ceros y los cortes por el eje real y por el eje imaginario.

<details>
<summary>Ver resolución</summary>

**Paso 1 (simplificar):** del denominador se saca $s$ factor común, $s^3 + s = s(s^2+1)$, y se cancela con la $s$ del numerador [35:07]–[35:38]. El origen **no es cero**: el límite de la $G$ original cuando $s \to 0$ da $\tfrac{3}{2}$, ni cero ni infinito [36:08].

$$
G(s) = \frac{3(s-1)}{(s-2)(s^2+1)}
$$

**Paso 2 (polos y ceros):** ceros: $1$ y el infinito. Polos: $2$ (real) y, por primera vez, un par complejo conjugado: $j$ y $-j$, raíces de $s^2+1$ [36:08]–[36:41].

**Paso 3 (constelación):** cruces en $j$, $-j$ y $2$; circulito en $1$ [36:41]–[37:13]. En 3D se ven tres volcanes [37:43].

**Paso 4 (corte por el eje real):** reales: cero en $1$ (toca el eje y rebota) y polo en $2$ (asíntota vertical) [38:15]. Leído de derecha a izquierda: viene pegado al eje, sube al infinito en el polo $2$, baja, toca en $1$, rebota, y en $x = 0$ (la parte real del par $\pm j$) aparece una **montañita** marcada, para después achatarse hacia $-\infty$ [39:49]–[40:19]. Ver la sección siguiente.

**Paso 5 (corte por el eje imaginario):** imaginarios puros: los polos $j$ y $-j$; el $1$ y el $2$ son reales y no cuentan [48:49]–[49:19]. Asíntotas verticales en $y = 1$ e $y = -1$; no toca el eje salvo en $\pm\infty$ (no hay raíz en este corte) [49:19]–[49:49].

**Paso 6 (ordenada al origen):** el corte del eje vertical se obtiene evaluando en $0$:

$$
G(0) = \frac{-3}{-2} = \frac{3}{2}
$$

"es súper fácil de calcular", está en $1{,}5$ [50:20]–[50:52].

</details>

</details>

## Polos complejos conjugados en el corte por el eje real: la "montañita" — [40:19]

- Un par complejo conjugado comparte la parte real y difiere en el signo de la parte imaginaria: sus dos volcanes están **alineados** en un plano perpendicular al eje real [40:49]–[41:21].
- El corte por el eje real **pasa justo en el medio de los dos volcanes**, a una distancia igual a la parte imaginaria del par (en el ejemplo, a distancia 1 de cada uno) [41:21]–[41:54]. No "emboca" a ninguno, por eso no hay asíntota: queda una **montañita** marcada [43:28]–[44:04].
- Si los volcanes se acercan al plano de corte (parte imaginaria más chica), la montañita es más pronunciada; si se alejan (por ejemplo $\pm 2j$), es menos marcada [41:54]–[42:56].
- Si se cortara con el plano $\mathrm{Im} = 1$ o $\mathrm{Im} = -1$ se "embocaría" a uno de los volcanes y aparecería una asíntota; pero el corte por el eje real siempre es con parte imaginaria $0$ [44:04]–[44:36].
- La montañita va **en la parte real del par**: si los polos fueran $-2 \pm j$, la montañita estaría en $-2$ [46:13]–[46:44].
- En el dibujo se la hace **exagerada**, para que se note que ahí hay un par de polos complejos conjugados [45:08]–[45:43].

Resumen de los hitos del corte por el eje real [46:13]: asíntotas horizontales a los costados, asíntotas verticales en los polos reales, toques en los ceros reales y montañitas en la parte real de los polos complejos conjugados.

## Consulta: ¿y los ceros complejos conjugados en los cortes? — [47:15]

- Un alumno pregunta qué pasa con ceros complejos conjugados [47:15]. Respuesta: **no se ven** en los cortes, porque para tocar el piso habría que cortar justo por ese punto, y los cortes que se hacen son $\mathrm{Im} = 0$ o $\mathrm{Re} = 0$ [47:46]–[48:18].
- No hay que marcarlos de ninguna manera, ni darles importancia a concavidades; además, en la segunda parte se le da "muchísima más pelota" a los polos que a los ceros [48:18].

## Módulo de $G$ en un punto: tres métodos (analítico, con módulos, gráfico) — [51:24]

Hay ejercicios que piden el **módulo** (o el argumento) de $G$ en un punto $s = a + bj$, que puede ser real, imaginario puro o con ambas partes no nulas [51:24]–[52:26]. Tres formas:

1. **Analítica** [52:26]–[53:27]: reemplazar $s$ por el número, operar con complejos (multiplicar por el conjugado del denominador, distribuir) y recién al final calcular el módulo. "Camino largo, válido", el "súper molesto".
2. **Con módulos directamente** [53:57]: reemplazar $s$ pero trabajar con módulos desde el principio, usando que el módulo de un producto o cociente es el producto o cociente de los módulos. Cada módulo es la **distancia al origen** del complejo [55:01].
3. **Gráfica** [56:03]: sobre la constelación, marcar el punto de referencia y trazar **vectores desde cada cero y cada polo hasta ese punto** [56:36]–[57:10]. Entonces [57:41]–[58:42]:

$$
|G(s_0)| = K \cdot \frac{\prod_i |\,s_0 - z_i\,|}{\prod_j |\,s_0 - p_j\,|}
$$

con $K$ la constante de la transferencia, en el numerador el producto de los módulos de los vectores que nacen en los **ceros** y en el denominador el de los que nacen en los **polos**.

Los métodos 2 y 3 son "lo mismo", uno con cuentas y otro con dibujo; pueden usar cualquiera salvo que el ejercicio pida explícitamente el método gráfico [1:00:49]–[1:01:20].

<details>
<summary>📝 Ejercicio 5 — 51:55: |G(2j)| de 3s/((s+2)(s²+1)) por los tres métodos</summary>

Dada

$$
G(s) = \frac{3s}{(s+2)(s^2+1)}
$$

calcular $|G(2j)|$.

<details>
<summary>Ver resolución</summary>

**Paso 1 (analítico):** se reemplaza $s = 2j$, se multiplica por el conjugado del denominador y se distribuye [52:26]–[52:56]. Se llega a un complejo cuya parte real al cuadrado es $\tfrac14$ y cuya parte imaginaria al cuadrado es $\tfrac14$ [la expresión exacta del complejo quedó poco clara en la transcripción]; su módulo es [52:56]:

$$
|G(2j)| = \sqrt{\tfrac14 + \tfrac14} = \frac{1}{\sqrt 2}
$$

**Paso 2 (con módulos):** se distribuyen los módulos [53:57]–[55:01]:

$$
|G(2j)| = \frac{3\,|2j|}{|2j+2|\,\cdot\,|(2j)^2+1|} = \frac{3 \cdot 2}{2\sqrt2 \cdot |-3|}
$$

$|2j| = 2$ (distancia al origen); $2 + 2j$ tiene catetos 2 y 2, módulo $\sqrt8 = 2\sqrt2$; $(2j)^2 + 1 = -4 + 1 = -3$, módulo $3$. Haciendo las cuentas da otra vez $\tfrac{1}{\sqrt2}$ [55:01]–[55:32].

**Paso 3 (gráfico):** constelación: cruces en $j$, $-j$ y $-2$; circulito en el origen; punto de referencia $2j$ en rojo [56:36]. Vectores hasta $2j$ [57:10]–[1:00:17]:

- desde el cero $0$: módulo $2$;
- desde el polo $j$: módulo $1$; desde el polo $-j$: módulo $3$;
- desde el polo $-2$: catetos 2 y 2, módulo $\sqrt8 = 2\sqrt2$.

Con $K = 3$ [58:12]:

$$
|G(2j)| = 3 \cdot \frac{2}{1 \cdot 3 \cdot 2\sqrt2} = \frac{1}{\sqrt2}
$$

Mismo resultado por los tres métodos [1:00:17]–[1:00:49].

</details>

</details>

## Argumento de $G$ en un punto por el método gráfico — [1:01:20]

- Es el correlato de la forma polar/exponencial: al multiplicar complejos los módulos se multiplican y **los argumentos se suman** [1:01:20]–[1:01:51]. Por eso, para el argumento, los productos pasan a sumas y los cocientes a restas.
- Con la misma constelación y los mismos vectores, ahora importa el **argumento de cada flechita**, medido respecto del semieje real positivo (con arco tangente si hace falta) [1:02:23]–[1:02:54].
- **La $K$ no aparece**: multiplicar por una constante no cambia el argumento [1:03:28]. La fórmula [1:03:28]–[1:04:00]:

$$
\arg G(s_0) = \sum_i \arg(s_0 - z_i) - \sum_j \arg(s_0 - p_j)
$$

- En general da negativo, porque hay más polos que ceros (grado del denominador mayor) [1:04:33]; se puede dejar negativo o pasarlo al primer giro positivo, salvo que se aclare [1:05:05].

<details>
<summary>📝 Ejercicio 6 — 1:02:23: arg G(2j) de 3s/((s+2)(s²+1))</summary>

Con la misma función del ejercicio 5, hallar $\arg G(2j)$ por el método gráfico.

<details>
<summary>Ver resolución</summary>

**Paso 1 (argumentos de los vectores):** el vector desde $-2$ hasta $2j$ tiene catetos iguales: $\tfrac{\pi}{4}$ ($45^\circ$). Los otros tres (desde $0$, $j$ y $-j$) son verticales: $\tfrac{\pi}{2}$ ($90^\circ$) [1:02:54]–[1:03:28].

**Paso 2 (fórmula):** suma de los de los ceros (solo uno, $\tfrac{\pi}{2}$) menos suma de los de los polos (dos de $\tfrac{\pi}{2}$ y uno de $\tfrac{\pi}{4}$) [1:04:00]:

$$
\arg G(2j) = \frac{\pi}{2} - \left(\frac{\pi}{2} + \frac{\pi}{2} + \frac{\pi}{4}\right) = -\frac{3\pi}{4}
$$

**Paso 3:** expresado en el primer giro positivo, $\tfrac{5\pi}{4}$; es lo mismo [1:04:33].

</details>

</details>

## Sistemas estables: entrada, transferencia y salida en $t$ y en $s$ — [1:06:37]

- El diagrama de bloques también se piensa en el **dominio del tiempo**: $f(t)$ entra a $g(t)$ y sale $y(t)$ [1:07:08].
- El cociente $G = Y/F$ **solo vale en el dominio de Laplace** [1:07:44]. Cuando dan funciones del tiempo y piden $y(t)$ o cómo se comporta, hay que pasar a $s$, hallar $Y(s)$ y volver con la antitransformada [1:07:44]–[1:08:16], igual que con las ecuaciones diferenciales [1:08:16]–[1:08:47].

<details>
<summary>📝 Ejercicio 7 — 1:08:47: guía ej. 9, constelación y respuesta a e^{−2t}</summary>

Dada

$$
G(s) = \frac{s^2 + 2s}{s^3 - 2s^2 - 3s}
$$

a) Graficar la constelación de polos y ceros. b) Escribir la salida $y(t)$ del sistema para la entrada $f(t) = e^{-2t}$ [1:09:17].

<details>
<summary>Ver resolución</summary>

**Paso 1 (simplificar):** factor común $s$ arriba y abajo; el $0$ es raíz de los dos y se cancela [1:09:49]:

$$
G(s) = \frac{s+2}{(s+1)(s-3)}
$$

**Paso 2 (constelación):** cero en $-2$; polos reales y distintos en $-1$ y $3$; todo sobre el eje horizontal [1:10:21]–[1:10:53].

**Paso 3 (transformar la entrada):** $g(t)$ no se usa; se necesita $F(s)$ [1:11:25]–[1:11:56]:

$$
F(s) = \mathcal{L}\{e^{-2t}\} = \frac{1}{s+2}
$$

**Paso 4 (salida en $s$):** $Y(s) = G(s)\,F(s)$; la entrada está pensada para cancelar el $(s+2)$ [1:12:28]:

$$
Y(s) = \frac{1}{(s+1)(s-3)}
$$

**Paso 5 (antitransformar):** fracciones simples, caso de polos reales y distintos ("sale con el truquito"); el profe va directo al resultado [1:13:00]–[1:13:30]:

$$
y(t) = -\frac14\,e^{-t} + \frac14\,e^{3t}
$$

**Paso 6 (estabilidad):** $e^{-t} \to 0$ pero $e^{3t} \to \infty$, así que $y(t) \to \infty$ cuando $t \to \infty$: no se estabiliza, el sistema es **inestable** [1:14:32]–[1:15:37] (en [1:15:37] dice "estable" por error; lo corrige en [1:16:39]).

</details>

</details>

## Valor estable y definición de sistema estable — [1:14:02]

- **Valor estable**: el valor al que tiende la respuesta $y(t)$ cuando $t \to \infty$ (puede ser $0$, $8$, el número que sea) [1:14:02]–[1:14:32].
- Si $\lim_{t\to\infty} y(t) = \infty$ (no acotada), el sistema es **inestable** [1:15:03].

**Definición** [1:15:37]–[1:16:08]: un sistema es **estable** si, cuando $t \to \infty$, $y(t)$ tiende a un cierto $k$ **o bien permanece acotada**. El valor $k$ se denomina **valor estable**.

$$
\lim_{t \to \infty} y(t) = k \quad \text{o} \quad y(t) \text{ acotada} \quad\Longrightarrow\quad \text{estable}
$$

- "Permanecer acotada": por ejemplo una respuesta seno oscila sin tender a ningún valor, pero queda entre $-1$ y $1$; no se va al infinito, así que es estable aunque no tenga valor estable $k$ [1:16:08]. "Sos inestable si te vas al infinito" [1:16:39].
- Con la versión de la guía teórica (consulta final, [1:52:48]–[1:53:48]): un sistema es estable si **para cualquier entrada acotada** responde de manera estable. Por eso se analiza la $G(s)$ sin mirar la entrada; si le metés una entrada no acotada (una exponencial creciente), obviamente la salida se va. Entradas acotadas: exponenciales decrecientes, constantes, senos, cosenos.

## Estabilidad según los polos: polos simples y múltiples — [1:17:11]

- **Solo importan los polos**, no los ceros: mirando dónde están los polos en la constelación se puede decir si el sistema es estable o no [1:17:11]–[1:17:42].
- **Polo simple / múltiple** = multiplicidad de la raíz del denominador: en $\frac{3}{s-1}$ el polo es simple; con $(s-1)^2$ es doble; con $(s-1)^3$, triple [1:18:13]–[1:18:44]. En los ejercicios siempre aparecen polos simples; los múltiples se mencionan por arriba [1:18:44]–[1:19:16].
- Se analiza barriendo el plano **de izquierda a derecha**: parte real negativa, sobre el eje imaginario, parte real positiva [1:21:56].

## Caso 1: polo real negativo → exponencial decreciente — [1:19:16]

Con un polo real negativo en $-a$ (el profe lo escribe con $K$ constante cualquiera) [1:19:16]–[1:19:47]:

$$
G(s) = \frac{K}{s+a} \quad\Longrightarrow\quad g(t) = K\,e^{-at}
$$

- Es una **exponencial decreciente**: baja y tiende a $0$ en el infinito; valor estable $k = 0$ [1:20:21]–[1:20:56].
- **Polo doble**: $g(t) = K\,t\,e^{-at}$, que también tiende a $0$ [1:21:26].
- Nombre: sistema **estable, exponencial decreciente** [1:21:26]–[1:21:56].

## Caso 2: polos complejos conjugados con parte real negativa → oscilatoria amortiguada (factor $\alpha$) — [1:21:56]

$$
G(s) = \frac{K}{as^2 + bs + c}, \qquad b^2 - 4ac < 0, \qquad -\frac{b}{2a} < 0
$$

($b^2 - 4ac < 0$: raíces complejas conjugadas; $-\tfrac{b}{2a}$ es su parte real, negativa: a la izquierda del eje) [1:21:56]–[1:22:27]. Al antitransformar se llega a algo de la forma [1:22:57]:

$$
g(t) = M\,\mathrm{sen}(\omega t)\,e^{-\alpha t}
$$

- Oscila como un seno, **amortiguada** por una exponencial decreciente, hasta hacerse asintótica a $0$: valor estable $0$ [1:23:28]–[1:24:01]. Puede ser seno, coseno o suma de ambos; la conclusión es la misma [1:24:01].
- Nombre: sistema **estable, oscilatorio amortiguado** [1:24:31].
- **Factor de amortiguamiento $\alpha$** [1:25:06]–[1:26:06]: el número que acompaña a $-t$ en el exponente. Se da **en positivo**, porque el amortiguamiento ya sobreentiende que la parte real es negativa. Ejemplo: $g(t) = 4\,\mathrm{sen}(3t)\,e^{-2t}$ tiene $\alpha = 2$ (no $-2$).
- **Polos dobles**: se agrega una $t$, $M\,t\,\mathrm{sen}(\omega t)\,e^{-\alpha t}$, que sigue tendiendo a $0$: estable [1:26:38]–[1:27:10].
- Regla: "siempre estamos tranquilos" cuando el término está multiplicado por una **exponencial decreciente**: el sistema es estable [1:27:10]–[1:27:40].

## Caso 3: polo nulo — [1:27:40]

$$
G(s) = \frac{K}{s} \quad\Longrightarrow\quad g(t) = K
$$

- Ya no tiende a $0$, tiende a $K$; no se va al infinito. **Sigue siendo estable** ("eso es importante"), aunque es una estabilidad "menos pura" [1:28:11]–[1:28:41].
- **Polo nulo doble**: $g(t) = K\,t$, no acotada: **inestable** [1:28:41]–[1:29:11].

## Caso 4: polos imaginarios puros → oscilatoria de amplitud constante — [1:29:11]

$$
G(s) = \frac{K}{s^2 + a^2} \quad\Longrightarrow\quad g(t) = \frac{K}{a}\,\mathrm{sen}(at)
$$

- No tiende a $0$ ni a ningún valor: oscila infinitamente entre $\tfrac{K}{a}$ y $-\tfrac{K}{a}$. Se sigue llamando estable, pero "no tan puramente estable" [1:29:45].
- Nombre: respuesta **oscilatoria de amplitud constante** (no hay exponencial que la amortigüe) [1:30:22].
- Consulta [1:30:54]: si en vez de seno es coseno, o suma de seno y coseno, también queda acotado: mismo resultado.
- **Polos dobles**: aparece $t$ (constante por $t$ por seno), no acotada: **inestable** [1:31:24].

## Marginalmente (o críticamente) estable — [1:32:52]

- En los casos 3 y 4 los polos están **sobre el eje imaginario** [1:31:24]. Las versiones simples no tienden a $0$ (tienden a una constante o oscilan acotadas) y las múltiples no están acotadas [1:32:19].
- A los casos 3 y 4 (simples) se los llama **marginalmente** o **críticamente estables**, "aunque lo seguimos considerando estables"; se les dice así porque ya no tienden a cero [1:32:52]–[1:33:24].

## Casos 5 y 6: polos con parte real positiva → inestable — [1:33:24]

**Caso 5, polo real positivo** ($a > 0$) [1:33:24]–[1:33:55]:

$$
G(s) = \frac{K}{s-a} \quad\Longrightarrow\quad g(t) = K\,e^{at}
$$

Exponencial **creciente**, no acotada: sistema **inestable** (exponencial) [1:33:55]–[1:34:25]. Con polos múltiples se agrega una $t$, pero sigue yendo al infinito [1:34:25].

**Caso 6, polos complejos conjugados con parte real positiva** ($b^2 - 4ac < 0$ y $-\tfrac{b}{2a} > 0$) [1:34:25]–[1:34:56]: al antitransformar queda constante por seno o coseno (o suma) por una **exponencial creciente** [1:35:26]. Oscila cada vez más fuerte, no está acotada: respuesta **oscilatoria de amplitud creciente**, sistema **inestable** [1:35:26]. Con polos múltiples no cambia nada [1:36:00].

## Conclusión: condición necesaria y suficiente de estabilidad — [1:36:00]

| Ubicación de los polos | Respuesta | Clasificación |
|---|---|---|
| Reales negativos (simples o múltiples) | exponencial decreciente, tiende a $0$ | estable |
| Complejos conjugados con parte real negativa | oscilatoria amortiguada, tiende a $0$ | estable |
| Polo nulo simple | constante $K$ | marginalmente estable |
| Imaginarios puros simples | oscilatoria de amplitud constante | marginalmente estable |
| Sobre el eje imaginario, múltiples | $K\,t$, $t\,\mathrm{sen}$ (no acotadas) | inestable |
| Real positivo | exponencial creciente | inestable |
| Complejos conjugados con parte real positiva | oscilatoria de amplitud creciente | inestable |

(Tabla armada con lo dicho en [1:19:16]–[1:37:05].)

- **Condición necesaria y suficiente** [1:37:05]–[1:37:41]: un sistema es estable si **todos los polos de su función de transferencia tienen parte real negativa o nula**. Gráficamente: todos los polos **a la izquierda del eje de ordenadas o sobre él**.
- Si todos están a la izquierda: **estable**. Si hay alguno (o un par) sobre el eje: **marginalmente estable** [1:37:41]. Las versiones múltiples de los polos sobre el eje ya son inestables [1:37:05].
- Si hay **aunque sea uno** del lado derecho: **inestable**, "por más que ustedes tengan 52.000 polos del lado izquierdo" [1:37:41]–[1:38:14].

<details>
<summary>📝 Ejercicio 8 — 1:38:45: guía ej. 6 g, construir G(s) con polos, ceros y |G(j)| = √(5/2)</summary>

Construir una función de transferencia con coeficientes reales que tenga un polo simple en $s = -4 + j$, un polo simple en $-1$, un cero doble en $-2$, y tal que

$$
|G(j)| = \sqrt{\tfrac{5}{2}}
$$

[1:38:45]–[1:39:46]

<details>
<summary>Ver resolución</summary>

**Paso 1 (por qué "coeficientes reales"):** como $-4 + j$ no es real puro ni imaginario puro, por tener coeficientes reales tiene que estar también su conjugado $-4 - j$ [1:39:16].

**Paso 2 (armar la forma):** siempre una constante $K$; cero doble en $-2$ → $(s+2)^2$ arriba; polo en $-1$ → $(s+1)$ abajo; el par conjugado → $(s-(-4+j))(s-(-4-j))$ abajo [1:39:46]–[1:40:18].

**Paso 3 (factor cuadrático del par):** regla mnemotécnica [1:40:49]–[1:41:26]: el producto de los dos factores de un par conjugado da $s^2$ menos dos veces la parte real por $s$, más parte real al cuadrado más parte imaginaria al cuadrado. Con parte real $-4$ e imaginaria $1$: $-2(-4) = 8$ y $16 + 1 = 17$:

$$
(s+4-j)(s+4+j) = s^2 + 8s + 17
$$

$$
G(s) = K\,\frac{(s+2)^2}{(s+1)(s^2+8s+17)}
$$

**Paso 4 (hallar $K$, método gráfico):** vectores hasta el punto $j$ [1:42:26]–[1:42:57]: desde el cero $-2$, módulo $\sqrt5$ (va **al cuadrado** porque el cero es doble); desde el polo $-1$, $\sqrt2$; desde los polos $-4 \pm j$, $4$ y $2\sqrt5$. Se plantea la fórmula del módulo igualada a $\sqrt{5/2}$ (también se puede hacer analíticamente, reemplazando $s = j$; el profe no hace la cuenta [1:41:56]–[1:42:26]):

$$
|G(j)| = K \cdot \frac{(\sqrt5)^2}{\sqrt2 \cdot 4 \cdot 2\sqrt5} = \sqrt{\tfrac{5}{2}}
$$

**Paso 5:** despejando, $K = 8$ [1:43:29]:

$$
G(s) = 8\,\frac{(s+2)^2}{(s+1)(s^2+8s+17)}
$$

Con $K = 1$ no se cumpliría el dato del módulo [1:43:59].

**Paso 6 (corte por el eje real):** cero real doble en $-2$ (en el corte, doble o simple da igual: toca el eje); asíntota vertical en $-1$; **montañita** bien pronunciada en $-4$ (parte real del par conjugado); asintótico horizontal a los costados [1:44:32]–[1:45:02].

**Paso 7 (estabilidad, de la consulta final):** todos los polos ($-1$ y $-4 \pm j$) tienen parte real negativa: **estable**; por el par complejo con parte real negativa, **oscilatorio amortiguado** [1:49:44]. Al antitransformar saldría, por fracciones simples, un término $\frac{A}{s+1}$ (que da $e^{-t}$) y otro $\frac{Bs + C}{(s+4)^2 + 1}$ (que da senos y/o cosenos de $t$ por $e^{-4t}$) [1:50:15]–[1:51:16]; $B$ y $C$ no se calculan.

</details>

</details>

<details>
<summary>📝 Ejercicio 9 — 1:45:02: guía ej. 6 h, construir G(s) desde el corte por el eje real, G(0) = 3/5 y G(1) = 1</summary>

Construir $G(s)$ sabiendo que $G(0) = \tfrac35$, $G(1) = 1$ y que su corte por el eje real es el del gráfico del PDF: toca el eje en $-1$, tiene una asíntota vertical en $-2$ y una montaña bien marcada en $1$ [paso en el pizarrón, ver video] [1:45:02]–[1:46:04].

<details>
<summary>Ver resolución</summary>

**Paso 1 (leer el gráfico):** toca el eje en $-1$ → cero $z_1 = -1$; además el cero en el infinito; no hay otro toque [1:45:32]. Asíntota vertical en $-2$ → polo en $-2$ [1:45:32]–[1:46:04]. Montaña marcada en $1$ → par de polos complejos conjugados con **parte real 1** y parte imaginaria desconocida $\pm b$ [1:46:04]–[1:46:36].

**Paso 2 (dos incógnitas):** al construir la función quedan $K$ y $b$ (que al distribuir el par conjugado queda en el denominador); por eso el enunciado da **dos datos** [1:46:36]–[1:47:08]. Con la regla del factor cuadrático del ejercicio anterior:

$$
G(s) = K\,\frac{s+1}{(s+2)\left[(s-1)^2 + b^2\right]}
$$

**Paso 3 (dato $G(0)$):** todas las $s$ valen $0$ [1:47:08]:

$$
G(0) = \frac{K}{2\,(1 + b^2)} = \frac35
$$

**Paso 4 (dato $G(1)$):** reemplazando todas las $s$ por $1$ [1:47:41]:

$$
G(1) = \frac{2K}{3\,b^2} = 1
$$

**Paso 5 (resolver):** sistema simple; da $K = 6$ y $b^2 = 4$ [1:47:41]. Con eso se reemplaza y se llega a la forma final [1:47:41]:

$$
G(s) = 6\,\frac{s+1}{(s+2)\left[(s-1)^2 + 4\right]}
$$

**Paso 6 (curiosidad):** $b^2 = 4$ da $b = \pm 2$, que son justamente las partes imaginarias de los dos polos conjugados $1 \pm 2j$ [1:48:13].

**Paso 7 (estabilidad, de la consulta final):** tiene polos complejos conjugados del lado derecho (parte real $1$): **inestable** [1:49:13].

</details>

</details>

## Consultas finales: estabilidad y tipo de respuesta de 6 g y 6 h, entradas acotadas — [1:49:13]

- 6 h es **inestable** (par conjugado con parte real $1$); 6 g es **estable** y **oscilatorio amortiguado** (todos los polos a la izquierda, par con parte real $-4$) [1:49:13]–[1:49:44].
- "Siempre que tengamos un sistema estable la exponencial decreciente va a estar, y el inestable va a ser creciente"; con la salvedad de los **marginalmente estables**: una constante o algo que oscila sin parar, sin exponencial decreciente, y **también se consideran estables** [1:51:16]–[1:51:46].
- ¿Qué tienen que ver entrada y salida con la estabilidad? [1:52:17]–[1:53:48]: estable = la respuesta no se va al infinito (tiende a un valor o queda acotada). Y un sistema es estable si **para cualquier entrada acotada** responde de manera estable; por eso se analiza solo $G(s)$.

---

*Generado el 2026-10-02 a partir de `fuentes/clases/Sistemas Estables/T_SE - Teorica.mp4` (transcripción local con Whisper, `apuntes/transcripts/13-video-teorica-sistemas-estables.json`, 114 min). Las fórmulas se reconstruyeron de lo dictado; los gráficos (superficies en GeoGebra, cortes, constelaciones) quedaron en pantalla y no se transcriben.*
