# Práctica de sistemas estables (clase grabada)

> Fuente: fuentes/clases/Sistemas Estables/P_SE - Practica.mp4 (transcripción local con Whisper) + OneNote de la clase

---

> **Cómo usar este apunte.** Es el complemento oral de `05-practica-sistemas-estables.md`
> (que transcribe el OneNote de la misma clase). Acá van los **porqués** del profe: cómo
> elige cada paso, cómo lee los gráficos, qué trucos usa y qué advierte para el parcial.
> Las cuentas largas no se repiten: se remite a "ver 05, ej. N". Los enunciados y
> fórmulas salen del OneNote (`[OneNote p. N]`), porque Whisper transcribe mal lo dictado.
> Los timestamps `[mm:ss]` son del video local (sin enlace público).

## Índice

- [00:00] — Polos, ceros, la $K$ y el cero en el infinito
- [00:31] — 📝 Ejercicio 1 a) y e): constelación de polos y ceros
- [05:19] — Hallar $K$ con un dato de módulo: método gráfico de los vectores
- [05:19] — 📝 Ejercicio 2: $K$ con $|G(j)| = \sqrt{13/5}$
- [12:41] — Corte de $|G(s)|$ por el eje real
- [12:41] — 📝 Ejercicio 3: $K$ con $|G(j)| = 1$ y corte por el eje real
- [18:29] — Corte por el eje imaginario: $|G(j\omega)|$ y el cero como "comodín"
- [18:29] — 📝 Ejercicio 4: $K$ para que $3j$ sea polo + $|G(j\omega)|$
- [24:49] — Construir una transferencia: el factor cuadrático de un par conjugado
- [24:49] — 📝 Ejercicio 6 b): transferencia con $G(0) = -2$
- [28:25] — 📝 Ejercicio 5 (consulta de un alumno): polos complejos con parte real $\neq 0$ en el corte imaginario
- [34:39] — Leer la constelación desde el gráfico del corte: montaña marcada vs. rebote suave
- [34:39] — 📝 Ejercicio 6 i): transferencia desde el corte con $G(0) = 3$, $G(1) = 5$
- [40:51] — Consulta: $K$ como cociente de coeficientes principales
- [42:23] — 📝 Ejercicio 7: $G(s) = \mathcal{L}[e^{-3t}\,\mathrm{sen}(at)]$ con polo en $-3 + j$
- [44:25] — Estabilidad y tipo de respuesta: solo importan los polos
- [44:25] — 📝 Ejercicio 8: tipo de respuesta y estabilidad
- [46:58] — Marginalmente estable; módulo y argumento por el método gráfico
- [46:58] — 📝 Ejercicio 10: marginalmente estable, $G(-1+j)$ y respuesta a $e^{-t}$
- [55:26] — 📝 Ejercicio 13: transferencia a partir de la salida ("vueltita de tuerca")
- [1:01:40] — Sistemas físicos: lo único que hay que saber de física
- [1:01:40] — 📝 Ejercicio 19: sistema mecánico de traslación + ¿qué $B$ para que no se amortigüe?
- [1:19:51] — Barrido de $B$ en GeoGebra: cómo se mueven los polos
- [1:24:35] — Ejercicio integrador: respuesta natural (entrada impulso) y teorema del valor final
- [1:24:35] — 📝 Ejercicio 20 (integrador): ¿cuál da oscilatoria amortiguada con V.E. 2?
- [1:36:48] — Consulta final: ¿marginalmente estable cuenta como estable?

## Lo que el profe remarca

**Sobre el parcial y la forma de responder**

- **[00:31]** El ejercicio 1 (constelación de polos y ceros) es muy fácil, pero "a veces es la parte A de un ejercicio un poquito más largo", así que hay que saber hacerlo.
- **[17:58]** (consulta) El dibujo del corte **no tiene que ser exacto**: alcanza con que se noten bien los polos y los ceros. El profe confirma: "Exacto".
- **[18:59]** Los únicos cortes que pueden pedir son dos: **por el eje real** o **por el eje imaginario**. "Graficar $|G(j\omega)|$" es sinónimo de corte por el eje imaginario. **[33:07]** Los cortes "siempre se piden en el cero" ($\mathrm{Im} = 0$ o $\mathrm{Re} = 0$), nunca en otra recta.
- **[50:36]** En estos ejercicios "les puede aparecer tanto módulo como argumento".
- **[1:07:52]** El ejercicio 19 (sistema físico resuelto por Laplace): "estos ejercicios son importantes, esto sí es un ejercicio de parcial o de final".
- **[1:10:33]** En el 19 b) la justificación **física/lógica** (sin rozamiento nada frena al carrito) "está bien justificado"; la matemática es más intrincada.
- **[1:34:11]** Si un ejercicio se puede resolver por análisis de polos o antitransformando, **las dos valen**: "el enunciado no te obliga a usar una cosa o la otra", antitransformar solo lo hace más largo.
- **[1:36:48]–[1:37:48]** (consulta) Si piden clasificar **estable / inestable** (por ejemplo, redondear o tachar en un examen), un sistema **marginalmente estable se clasifica como estable** ("no se va al infinito"); si querés, aclarás que es marginalmente estable.
- **[55:58]** El ejercicio 13 (hallar la transferencia desde la salida) es "un poquito más raro", "no es algo que se suele pedir mucho", "una vueltita de tuerca".
- **[1:22:29]** **Polos múltiples:** "no le damos importancia" (están en el apunte teórico del profe, pero no se trabajan).
- **[1:19:19]** **Factor de amortiguamiento:** concepto "muy por arriba", "no se toca demasiado" (el profe dice que se enteró en la última fecha de final después de 10 años en la cátedra).
- **[14:17]** En esta clase las cuentas (Ruffini, resolvente, fracciones simples) se dan por sabidas: el foco es la parte conceptual.

**Errores típicos y trucos**

- **[01:04] / [04:17] / [44:25]** **Siempre simplificar primero.** Una raíz común a numerador y denominador se cancela y **no es ni cero ni polo** (no cumple la definición formal: polo ⇒ $|G| \to \infty$, cero ⇒ $|G| \to 0$). "Siempre algo se va a cancelar", "en el 95% de los casos hay algo". Error típico: decir que esa raíz es cero y polo a la vez.
- **[06:22]** Truco para encontrar la raíz compartida: factorizar el polinomio fácil (el cuadrático), y **probar sus raíces en el otro** (el cúbico). **[07:25]** Ruffini se arranca cuando ya **sabés** (no sospechás) que es raíz: primero evaluás y verificás que da 0.
- **[01:35] / [10:00]** **Siempre hay una $K$.** Si no se ve, vale 1. Hay que ponerla en la fórmula del módulo: "si de repente es un 2, el resultado ahí sí te cambia".
- **[51:40]** La $K$ **cambia el módulo pero no el argumento**: por eso no aparece cuando se calcula la fase.
- **[41:53]** "Siempre hay que dejar todo factorizado": constante por $(s - \text{algo})$… sobre $(s - \text{algo})$…, así se trabaja fácil.
- **[02:41] / [20:37] / [43:54]** Coeficientes reales ⇒ las raíces son reales o **complejas conjugadas**: si te dan un polo complejo, su conjugado también es polo (aunque no lo digan).
- **[02:06] / [59:07]** El **cero en el infinito** (grado del denominador mayor que el del numerador) es "muy teórico", pero conviene ponerlo en la lista de ceros. No cuenta para el método gráfico de los vectores ([07:57]).
- **[16:22]** El gráfico de $|G|$ es **siempre positivo** (es un módulo) y se achata hacia el eje a izquierda y derecha por el cero en el infinito.
- **[45:27]** Para estabilidad **solo importan los polos**; los ceros "no cortan ni pinchan", se ponen por costumbre.
- **[45:57]** Truco para el tipo de respuesta sin saberlo de memoria: plantear las fracciones simples **sin resolverlas** y mirar qué antitransformada da cada término.
- **[1:32:35]** En el integrador, la constante $A$ de $\frac{A}{s}$ sale también con el "truquito" (tapar el factor) y da el valor estable.
- **[1:05:16]** Las transformadas de las derivadas están "en la tablita de fórmulas, en la ayuda memoria".

---

## Polos, ceros, la $K$ y el cero en el infinito — [00:00]

La práctica arranca con los conceptos de la teórica: polos, ceros, entrada, transferencia, salida y estabilidad según los polos.

- **Ceros:** raíces del numerador. **Polos:** raíces del denominador ([01:35], respondiendo una consulta).
- Definición más formal (de la teórica): en un **polo** la función tiende a infinito; en un **cero** tiende a cero. Por eso una raíz **compartida** se cancela y no es ninguna de las dos cosas ([01:04]).
- Las transferencias siempre están multiplicadas por una $K$; si no se ve, $K = 1$ ([01:35]).
- **Cero teórico en $\pm\infty$** ([02:06]): aparece porque el grado del denominador es mayor que el del numerador; es lo que hace que la superficie (en 3D) o la curva (en 2D) se achate y se acerque asintóticamente al piso a los costados ([02:41]).
- Como los coeficientes son reales, las raíces son **reales o complejas conjugadas** ([02:41]).
- Constelación: **cruces** para los polos, **circulitos** para los ceros ([03:16]).

<details>
<summary>📝 Ejercicio 1 a) y e) — 00:31: constelación de polos y ceros</summary>

Represente la constelación de polos y ceros de [OneNote p. 1]:

**a)**

$$
G(s) = \frac{s}{s^2 + 2s + 2}
$$

**e)**

$$
G(s) = \frac{s^2 - s}{(s^2 + 5s + 6)(s - 1)}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1 (ítem a):** $K = 1$ (no se ve). Ceros: el "obvio" en el origen y el teórico en el infinito. Polos: raíces de $s^2 + 2s + 2$, "fáciles de sacar": $-1 \pm j$, complejos conjugados [02:06]–[03:16].

**Paso 2 (ítem a):** constelación: dos cruces con parte real $-1$ y partes imaginarias $\pm 1$, circulito en el origen [03:16]. Ver 05, ej. 1.

**Paso 3 (ítem e):** acá está la trampa [03:47]: el numerador es $s(s - 1)$ y el $(s - 1)$ se cancela con el del denominador.

$$
G(s) = \frac{s(s - 1)}{(s^2 + 5s + 6)(s - 1)} = \frac{s}{(s + 2)(s + 3)}
$$

El profe advierte [04:17]: "ustedes podrían haberse visto tentados a decir, che, uno es cero porque anula el numerador, también es polo porque anula el denominador, pero en realidad no es ninguno de los dos porque se cancela". Se trabaja siempre con la versión simplificada.

**Paso 4 (ítem e):** cero en $0$, polos reales en $-2$ y $-3$; cruces y circulito sobre el eje real [04:49].

</details>

</details>

## Hallar $K$ con un dato de módulo: método gráfico de los vectores — [05:19]

Cuando dan $|G(s_0)|$ y hay que hallar $K$, el profe **no empieza por el ítem a)**: primero hace el b) (polos, ceros y constelación), porque la constelación sirve para calcular el módulo gráficamente [05:19]–[05:51]. Orden de trabajo:

1. Buscar raíces compartidas y cancelarlas [05:51].
2. Marcar en la constelación el punto de referencia $s_0$ (en el ej. 2, $j$). "Podría haber sido $1 + j$, podría haber sido un número real": cualquier complejo vale [08:57].
3. Trazar vectores desde cada cero y desde cada polo hasta $s_0$ [09:27].
4. Plantear el módulo con la $K$ adelante: producto de los módulos de los vectores de los ceros sobre producto de los módulos de los vectores de los polos [10:00]–[10:32]. Cada módulo sale por Pitágoras con los catetos horizontal y vertical.

$$
|G(s_0)| = K \cdot \frac{\prod |s_0 - z_i|}{\prod |s_0 - p_i|}
$$

5. Igualar al dato y despejar $K$ [11:06].

El cero en el infinito "para esto no cuenta" [07:57].

<details>
<summary>📝 Ejercicio 2 — 05:19: hallar K con |G(j)| = √(13/5)</summary>

Sea $G(s) = \dfrac{k\,(s^2 - 4s - 5)}{s^3 - 7s^2 + 17s + 25}$ la transferencia de un sistema [OneNote p. 2].

a) Halle $k \in \mathbb{R}^+$ tal que $|G(j)| = \sqrt{\dfrac{13}{5}}$.

b) Indique los polos y ceros de $G(s)$ y grafique la constelación.

<details>
<summary>Ver resolución</summary>

**Paso 1:** arrancar por el numerador, que es de grado 2 y "lo sabemos manejar un poquito mejor": raíces $5$ y $-1$, o sea $(s + 1)(s - 5)$ [06:22].

**Paso 2:** "confiar en mi palabra" de que algo se cancela: probar $-1$ (y $5$, si quieren) en el denominador. El $-1$ lo anula ⇒ raíz compartida, se tacha [06:22]–[06:54].

**Paso 3:** cociente por Ruffini con $-1$: $s^2 - 8s + 25$, de raíces $4 \pm 3j$ [06:54]–[08:27]. Ver 05, ej. 2.

**Paso 4:** constelación: circulito en $5$, cruces en $4 \pm 3j$, punto de referencia $j$ marcado en azul; vectores desde el cero (verde) y desde los polos (otro color) hasta $j$ [08:27]–[09:27].

**Paso 5:** módulos por Pitágoras [10:32]–[11:06]: desde el cero, catetos $5$ y $1$ ⇒ $\sqrt{26}$; desde $4 + 3j$, catetos $4$ y $2$ ⇒ $\sqrt{20}$; desde $4 - 3j$, catetos $4$ y $4$ ⇒ $\sqrt{32}$.

$$
\frac{K\,\sqrt{26}}{\sqrt{20}\,\sqrt{32}} = \sqrt{\frac{13}{5}} \quad \Rightarrow \quad K = \sqrt{64} = 8
$$

**Paso 6:** transferencia final [11:36]–[12:07]:

$$
G(s) = \frac{8\,(s - 5)}{s^2 - 8s + 25}
$$

"Igual lo importante era hallar esta $K$" [12:07].

</details>

</details>

## Corte de $|G(s)|$ por el eje real — [12:41]

- $|G(s)|$ es una superficie en 3D; cuando se pide graficar algo, es **un corte con un plano** que deja una figura en 2D. El corte con el plano $\mathrm{Im}(s) = 0$ es el **corte por el eje real** [12:41]–[13:13].
- Receta [15:49]–[16:22]: en el corte por el eje real se miran **solo los ceros y polos reales** (los "puntos notables" o **singularidades**). Los **ceros** hacen que la curva **toque el eje**; los **polos** son **asíntotas verticales**.
- La curva es siempre positiva (es un módulo) y se achata a izquierda y derecha por el cero del infinito [16:22].
- En GeoGebra [16:54]–[17:26]: el cero se ve como un "hundimiento" de la superficie y cada polo como un "volcán" o "montaña"; el plano corta "como una guillotina" y la intersección (línea punteada) es el mismo dibujo que se hace a mano.

<details>
<summary>📝 Ejercicio 3 — 12:41: constelación, K con |G(j)| = 1 y corte por el eje real</summary>

Sea $G(s) = \dfrac{k\,(s^2 - 4s - 5)}{s^3 - 3s^2 - 25s + 75}$ la transferencia de un sistema [OneNote p. 2].

a) Grafique la constelación de polos y ceros de $G(s)$.

b) Halle $k \in \mathbb{R}^+$ sabiendo que $|G(j)| = 1$.

c) Grafique aproximadamente $|G(s)|$ a lo largo del eje $\sigma = \mathrm{Re}[s]$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** los ítems a) y b) son "muy parecidos a los de recién" [12:41]; el denominador se parece al del ej. 2 pero no es el mismo [13:13]. Esta vez la raíz compartida es $5$; Ruffini con $5$ en el denominador y queda [13:45]–[14:17]:

$$
G(s) = \frac{K\,(s + 1)}{(s - 3)(s + 5)}
$$

Ver 05, ej. 3.

**Paso 2:** ceros en $-1$ y en el infinito; polos en $3$ y $-5$ [14:48].

**Paso 3:** $K$ con el mismo planteo de vectores hasta $j$: $K = \sqrt{130}$, "un número más feo, pero es lo que da" [14:48]–[15:18].

**Paso 4 (lo que más le interesa mostrar al profe):** corte por el eje real [15:18]–[16:22]. Todo es real ($-1$, $3$, $-5$), así que: asíntotas verticales en $-5$ y en $3$, toca el piso en $-1$, y a los costados se achata hacia el eje.

**Paso 5:** recorrido de la curva (verificado en GeoGebra) [17:26]–[17:58]: viene asintótica desde la izquierda, sube a infinito en $-5$, baja, toca en $-1$, sube a la asíntota de $3$ y a la derecha vuelve a hacerse asintótica horizontal.

Gráfico: <https://www.geogebra.org/m/czrrzpcu> [OneNote p. 3].

</details>

</details>

## Corte por el eje imaginario: $|G(j\omega)|$ y el cero como "comodín" — [18:29]

- "Graficar aproximadamente $|G(j\omega)|$" es un sinónimo de **corte por el eje imaginario** ($\mathrm{Re}(s) = 0$) [18:59].
- Así como en el corte real se miran los ceros/polos reales, en el corte imaginario se miran los **imaginarios puros** [21:09]–[21:43].
- El **cero en el origen** es un **comodín**: es real (no tiene parte imaginaria) e imaginario puro (no tiene parte real), así que cuenta en los dos cortes [21:43]–[22:14].
- Mismas reglas: ceros ⇒ toca el piso; polos ⇒ asíntotas verticales; a los costados se achata por el cero del infinito [22:14]–[22:44].

<details>
<summary>📝 Ejercicio 4 — 18:29: K para que 3j sea polo + |G(jω)|</summary>

Sea $G(s) = \dfrac{s(s + 2)}{s^3 + 2s^2 + 9s + k}$ la transferencia de un sistema [OneNote p. 3].

a) Halle $k \in \mathbb{R}$ sabiendo que $3j$ es un polo.

b) Grafique aproximadamente $|G(j\omega)|$.

<details>
<summary>Ver resolución</summary>

Ojo: acá la $k$ no es la constante que multiplica a toda la transferencia, sino un coeficiente "metido en el medio" del denominador [18:29].

**Paso 1:** pregunta del profe a la clase: ¿cómo hallo $k$ sabiendo que $3j$ es polo? Respuesta de un alumno: igualar a cero el denominador con $s = 3j$ y despejar. "Esa es la manera normal", sirve para cualquier polo que te den [18:59]–[19:32]. Da $k = 18$. Ver 05, ej. 4.

**Paso 2:** con $k = 18$, el $-2$ (raíz del numerador) también anula el denominador ⇒ se cancela. Ruffini deja $s^2 + 9$ [20:05].

$$
G(s) = \frac{s}{s^2 + 9}
$$

**Paso 3:** "¿Por qué tiene sentido que me dé $s^2 + 9$?" Porque sus raíces son $\pm 3j$: si te dijeron que $3j$ es polo, **estás obligado** a que $-3j$ también lo sea (coeficientes reales ⇒ conjugados) [20:37].

**Paso 4:** corte por el eje imaginario [22:14]–[22:44]: asíntotas en $-3$ y $3$ del eje $j\omega$, toca el eje en el origen, asintótico a los costados. Fue "un poquito fácil" porque en el corte real todo era real y acá todo es imaginario [22:44].

**Paso 5:** en GeoGebra las montañas son "muy finitas", pero el corte da el mismo gráfico [23:16]. Gráfico: <https://www.geogebra.org/m/pgmyudtt> [OneNote p. 3].

**Consulta de un alumno [23:48]–[24:18]:** ¿y el corte por el eje real de este mismo ejercicio? Toca en el origen (el cero), y entre medio de los dos conjugados queda una montañita: el profe lo describe como "una gaviota cuando la dibujás en el horizonte"; "rebota apenitas" en el cero y se hace asintótica a los costados. "Este corte no tiene gracia en este caso".

</details>

</details>

## Construir una transferencia: el factor cuadrático de un par conjugado — [24:49]

- Ceros y polos se escriben directo: $(s - z)\cdots$ sobre $(s - p)\cdots$, siempre acompañados de una $K$ [25:19].
- La $K$ se saca con el **dato extra** que dan, "que no es ni un cero ni un polo" (por ejemplo $G(0)$) [25:49].
- Para un par complejo conjugado se puede multiplicar $(s - p)(s - \bar{p})$ y operar, pero "no está bien dejar esta versión así fea con las $j$ ahí metidas". Operando siempre se llega a [25:49]–[26:20]:

$$
s^2 - 2\,\mathrm{Re}(p)\,s + \mathrm{Re}(p)^2 + \mathrm{Im}(p)^2
$$

"No es necesario que se acuerden de la formulita": haciendo la distributiva se llega igual [26:20], [27:22].

<details>
<summary>📝 Ejercicio 6 b) — 24:49: transferencia con G(0) = −2 y polos/ceros dados</summary>

Construya una función de transferencia que cumpla [OneNote p. 4]: $G(0) = -2$; ceros $z_{1,2} = -3 \pm j$; polos $p_{1,2} = -2 \pm 3j$, $p_3 = 1$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** con la formulita, los ceros $-3 \pm j$ dan $s^2 - 2(-3)s + (-3)^2 + 1^2 = s^2 + 6s + 10$ [26:50]. Igual con los polos $-2 \pm 3j$; el polo real $1$ da $(s - 1)$ [27:22].

**Paso 2:** con la $K$ todavía desconocida, "esta no es la versión final" [27:22]. Reemplazar $s = 0$ y usar $G(0) = -2$ (el profe se corrige en voz alta: "menos 2, perdón") [27:54]:

$$
\frac{10\,K}{-13} = -2 \quad \Rightarrow \quad K = \frac{13}{5}
$$

**Paso 3:** reescribir todo con $K$: ver 05, ej. 6 b).

**Nota:** el 6 g) **no se resuelve en este video** ("el g no, porque ya está hecho en la clase teórica") [34:39]; su resolución está en ver 05, ej. 6 g).

</details>

</details>

<details>
<summary>📝 Ejercicio 5 (consulta de un alumno) — 28:25: polos complejos con parte real ≠ 0 en el corte imaginario</summary>

Un alumno pregunta por el ejercicio 5 de la guía, cuya respuesta tiene un gráfico del corte imaginario con "dos montañitas" raras: ¿pasa siempre con polos complejos conjugados? [28:25]. **Este ejercicio no está en el OneNote**; lo que sigue es lo que el profe arma en el pizarrón. Del enunciado se entiende que el denominador es $s^3 - s^2 - 4s + k$ y que "$3$ no es un cero" aunque es raíz del numerador [30:00]–[30:31] (el numerador completo: [poco claro en la transcripción]).

<details>
<summary>Ver resolución</summary>

**Paso 1:** si $3$ es raíz del numerador pero **no es cero**, es porque se cancela: entonces también anula el denominador [30:31]:

$$
27 - 9 - 12 + k = 0 \quad \Rightarrow \quad k = -6
$$

**Paso 2:** Ruffini con $3$ sobre $1,\ -1,\ -4,\ -6$ deja $s^2 + 2s + 2$; el $(s - 3)$ se cancela arriba y abajo [31:03]–[31:33]. Polos: $-1 \pm j$ [32:05].

**Paso 3 (la explicación):** son complejos conjugados pero **no imaginarios puros** [32:05]. Si fueran imaginarios puros, el corte con $\mathrm{Re} = 0$ "le emboca al cráter del volcán" y aparecen asíntotas verticales (como en el ej. 4). Acá los polos tienen parte real $-1$: el corte en $x = 0$ no pasa por el centro de la montaña, agarra solo una sección, y por eso se ven **montañitas que suben pero bajan** [32:36]–[33:38]. Si se hiciera el corte en $x = -1$ sí se verían los volcanes, "pero no te lo pide nadie, porque siempre se piden en el cero" [33:07].

**Paso 4:** lo muestra en el GeoGebra del ej. 4 corriendo el plano a $x = 0{,}3$: deja de embocarle a los volcanes y aparecen montañitas [33:38]–[34:09].

</details>

</details>

## Leer la constelación desde el gráfico del corte: montaña marcada vs. rebote suave — [34:39]

Concepto de la teórica que en la práctica todavía no se había tocado [35:10]: cuando dan el **gráfico del corte por el eje real**, hay que extraer la información:

- **Asíntota vertical** ⇒ **polo real** ahí [35:41].
- **Toque con el eje horizontal** ⇒ **cero real**. Si no hay otro toque, no hay otro cero; si no hay otra asíntota, no hay otro polo real [35:41]–[36:11].
- **Montaña bien marcada, de punta redondita** ("está hecha así a propósito, para que se note que acá hay algo") ⇒ **polos complejos conjugados con esa parte real**. El corte real pasa justo por el medio de los dos volcanes, sin embocarle a ningún cráter: por eso no hay asíntotas, solo una montaña que sube y baja [36:11]–[37:14]. La parte imaginaria **no se lee** del gráfico (queda como incógnita $b$) [38:48].
- **Montañita suave pegada a un cero** ⇒ **no es un polo**: es el **rebote obligado** de la función, que "como es una función módulo no puede ir para abajo, tiene que rebotar sí o sí" y después se acomoda asintótica [37:46]–[38:48].
- Contar incógnitas: si quedan $K$ y $b$, hacen falta dos datos ⇒ **sistema de ecuaciones** [39:18].

<details>
<summary>📝 Ejercicio 6 i) — 34:39: transferencia desde el corte por el eje real con G(0) = 3, G(1) = 5</summary>

Construya una función de transferencia sabiendo que $G(0) = 3$, $G(1) = 5$ y que el corte con el eje real es el gráfico dado: lomo chico a la izquierda que baja a tocar el eje en $\sigma = -3$, asíntota vertical en $\sigma = -1$, lomo redondeado centrado en $\sigma = 2$ y decaimiento hacia el eje a la derecha [OneNote p. 6].

<details>
<summary>Ver resolución</summary>

**Paso 1:** leer el gráfico [35:41]–[38:48]: polo en $-1$ (asíntota), cero en $-3$ (toque), polos complejos $2 \pm bj$ (montaña marcada). La montañita de la izquierda es el rebote después del cero, no aporta nada.

**Paso 2:** armar el cuadrático con la formulita ($-2$ veces la parte real; más parte real al cuadrado más parte imaginaria al cuadrado) [39:18]–[39:50]:

$$
G(s) = \frac{K\,(s + 3)}{(s^2 - 4s + 4 + b^2)(s + 1)}
$$

**Paso 3:** dos incógnitas, dos datos: $G(0) = 3$ y $G(1) = 5$ (el profe se corrige: "igual a 3, a 5 perdón"). "No tiene mucha ciencia el sistema": $K = 5$, $b = \pm 1$ [39:50]–[40:20]. Cuentas: ver 05, ej. 6 i).

**Paso 4:** $b$ da los dos signos y **valen los dos**, porque son polos complejos conjugados [40:20].

Gráfico: <https://www.geogebra.org/m/hncqz6fy> [OneNote p. 6].

</details>

</details>

**Consulta sobre la $K$ [40:51]–[41:53].** Un alumno pregunta: si ya tengo la $G(s)$ escrita, ¿la $K$ sale como el cociente entre los coeficientes de mayor grado del numerador y del denominador? El profe confirma: si no se ve, es un 1; por ejemplo, con $3s$ arriba y $5s^2$ abajo, $K = \frac{3}{5}$. Remata: **siempre dejar todo factorizado**, constante por $(s - \text{algo})$… sobre $(s - \text{algo})$… [41:53].

<details>
<summary>📝 Ejercicio 7 — 42:23: G(s) = L[e^(−3t)·sen(at)] con polo en −3 + j</summary>

Dada $G(s) = \mathcal{L}[g(t)]$ con $g(t) = e^{-3t}\,\mathrm{sen}(at)$ [OneNote p. 7]:

a) Halle $a \in \mathbb{R}^+$ tal que uno de los polos de $G(s)$ sea $p_1 = -3 + j$.

b) Halle el otro polo.

<details>
<summary>Ver resolución</summary>

Acá "ya nos empezamos a meter con Laplace, que es lo que hace importante a esta unidad" [42:23].

**Paso 1:** transformar: el $e^{-3t}$ da el desplazamiento $s + 3$ [42:53]:

$$
G(s) = \frac{a}{(s + 3)^2 + a^2}
$$

**Paso 2 (ítem b, pregunta a la clase):** el otro polo es el **conjugado**, $-3 - j$, "por más que todavía no sepa cuál es la $a$". El b) "sale simplemente de ver el enunciado del a); ni siquiera hay que trabajar la función": es "bastante redundante" [42:23], [43:24]–[43:54].

**Paso 3 (ítem a):** reemplazar $s = -3 + j$ (o $-3 - j$, "si les pinta"), igualar a $0$ y despejar: $a = 1$ [43:54]. Ver 05, ej. 7.

</details>

</details>

## Estabilidad y tipo de respuesta: solo importan los polos — [44:25]

- Dos maneras complementarias de verlo: la **constelación** y las **fracciones simples** [44:56].
- **Solo importan los polos** para la estabilidad; los ceros se ponen por costumbre [44:56]–[45:27].
- Reglas [45:27]:
  - todos los polos en el **semiplano izquierdo** ⇒ **estable**;
  - algún polo **sobre el eje** imaginario ⇒ **marginalmente estable** (también llamado **críticamente estable**, [48:32]);
  - algún polo, aunque sea uno, en el **semiplano derecho** ⇒ **inestable**.
- **Tipo de respuesta "así rápido"** [45:57]: plantear las fracciones simples **sin resolverlas** ("no me importa cuál es $A$ y cuál es $B$") y mirar la antitransformada de cada término: $\frac{A}{s} \to$ constante; $\frac{B}{s - 3} \to B\,e^{3t}$ (exponencial positiva ⇒ "se me va a ir al diablo").

<details>
<summary>📝 Ejercicio 8 — 44:25: tipo de respuesta y estabilidad desde la constelación</summary>

Sea $G(s) = \dfrac{s^2 + 3s + 2}{s^3 - 2s^2 - 3s}$ la transferencia de un sistema. De acuerdo a la configuración de polos y ceros, indique el tipo de respuesta y si es estable [OneNote p. 7].

<details>
<summary>Ver resolución</summary>

**Paso 1:** simplificar: $-1$ es raíz compartida, se tacha [44:25]–[44:56]:

$$
G(s) = \frac{s + 2}{s\,(s - 3)}
$$

Ver 05, ej. 8.

**Paso 2:** hay un polo real **positivo** en $3$ ⇒ **inestable**, "solo de ver la ubicación de los polos" [45:57].

**Paso 3:** tipo de respuesta: $\frac{A}{s} + \frac{B}{s - 3} \to A + B\,e^{3t}$ ⇒ **respuesta exponencial creciente**; inestable porque el límite cuando $t \to \infty$ no está acotado [46:27]–[46:58].

</details>

</details>

## Marginalmente estable; módulo y argumento por el método gráfico — [46:58]

- Un polo **sobre el eje imaginario** (por ejemplo en el origen) ⇒ **marginalmente estable**: $\frac{A}{s}$ da una constante y los polos reales negativos dan exponenciales decrecientes ⇒ "respuesta exponencial decreciente desplazada $A$ unidades"; ese $A$ es el **valor estable** [48:01]–[49:04].

El módulo ya se hizo en los primeros ejercicios; el **argumento** es "parecido" [49:04]:

- Se trazan los mismos vectores desde ceros y polos hasta el punto de referencia, pero en vez de su largo se usa el **ángulo que forman con el semieje real positivo** [49:34]. Se puede sacar con tangente; en los ejercicios suelen ser casos fáciles de catetos iguales [50:05].
- Módulo: **producto** (ceros) **sobre producto** (polos), con la $K$. Argumento: **suma** de ángulos de los ceros **menos suma** de ángulos de los polos [50:36]. "Uno es con división y producto, otro es con resta y suma" [50:36].

$$
\arg G(s_0) = \sum \arg(s_0 - z_i) - \sum \arg(s_0 - p_i)
$$

- La $K$ **no aparece en el argumento**: multiplicar por una constante (positiva) cambia el módulo pero no el argumento [51:08]–[51:40].

<details>
<summary>📝 Ejercicio 10 — 46:58: marginalmente estable, G(−1+j) y respuesta a e^(−t)</summary>

Sea $G(s) = \dfrac{3s^2 - 6s - 24}{s^3 - 3s^2 - 4s}$ la transferencia de un sistema [OneNote p. 8].

a) Grafique la constelación de polos y ceros e indique si es estable.

b) Halle módulo y fase de $G(-1 + j)$ por método gráfico y analítico (en clase el profe **solo hace el gráfico** [46:58]).

c) ¿Cuál será la respuesta del sistema si se lo excita con $v_1(t) = e^{-t}$?

<details>
<summary>Ver resolución</summary>

**Paso 1:** "ya mecánico", se cancela algo arriba y abajo [47:29]:

$$
G(s) = \frac{3\,(s + 2)}{s\,(s + 1)}
$$

**Paso 2 (ítem a):** cero en $-2$, polos en $-1$ y en $0$. Hay un polo **sobre el eje imaginario** ⇒ **marginalmente estable** [47:29]–[48:01].

**Paso 3:** tipo de respuesta: $\frac{A}{s} \to$ constante, $\frac{B}{s + 1} \to$ exponencial decreciente (tiende a $0$) ⇒ **respuesta exponencial decreciente desplazada $A$ unidades**; ese desplazamiento $A$ es el **valor estable** [48:01]–[49:04].

**Paso 4 (ítem b):** ángulos de los vectores hasta $-1 + j$ [49:34]–[50:05]: desde el polo $0$ (diagonal), $\frac{3\pi}{4}$; desde el polo $-1$ (vertical), $\frac{\pi}{2}$; desde el cero $-2$, $\frac{\pi}{4}$. Resultado: argumento $-\pi$ [50:36]. La $K$ del módulo sale de dividir los coeficientes principales, $3$ y $1$: $K = 3$ [51:08]. Ver 05, ej. 10.

**Paso 5 (ítem c, "el que más me interesa"):** $Y(s) = G(s)\,F(s)$; para hallar $y(t)$ primero se halla $Y(s)$ y después se antitransforma. $F(s) = \mathcal{L}[e^{-t}] = \frac{1}{s + 1}$ [51:40]–[52:44]:

$$
Y(s) = \frac{3\,(s + 2)}{s\,(s + 1)^2}
$$

El $(s + 1)$ estaba en $G$ y en $F$, por eso queda al cuadrado; no hay nada para simplificar [52:44]–[53:16].

**Paso 6:** fracciones simples $\frac{A}{s} + \frac{B}{(s + 1)^2} + \frac{C}{s + 1}$: $A$ y $B$ salen con el "truquito rápido"; $C$ obliga a plantear ecuaciones. $A = 6$, $B = -3$, $C = -6$ [53:16]–[53:46].

**Paso 7:** antitransformar [53:46]–[54:22]: $\frac{-3}{(s+1)^2} \to -3\,t\,e^{-t}$ ("como la de $t$ pero desplazada"), $\frac{-6}{s+1} \to -6\,e^{-t}$:

$$
y(t) = 6 - 3\,t\,e^{-t} - 6\,e^{-t}
$$

**Paso 8 (cierre conceptual):** $\lim_{t \to \infty} y(t) = 6$ ("este límite es la definición de valor estable"). Esto **se condice** con el análisis de polos: marginalmente estable, exponencial decreciente desplazada 6 unidades [54:22]–[55:26].

</details>

</details>

<details>
<summary>📝 Ejercicio 13 — 55:26: transferencia a partir de la salida ("vueltita de tuerca")</summary>

Sea $y(t) = 5 - 5\,e^{-2t}\cos(3t)$ la respuesta de un sistema a una entrada escalón $E(t)$ [OneNote p. 9].

a) Indique la función transferencia $G(s)$.

b) Haga la constelación de polos y ceros y grafique aproximadamente el corte de $|G(s)|$ por el eje real.

<details>
<summary>Ver resolución</summary>

"Raro en el sentido de que no es algo que se suele pedir mucho" [55:26]. Al revés de lo habitual (dan transferencia y entrada, se busca la salida), acá dan salida y entrada y se busca la transferencia: es un **despeje** [55:58]–[56:29]:

$$
G(s) = \frac{Y(s)}{F(s)}, \qquad F(s) = \frac{1}{s}
$$

**Paso 1 (dato extra que "no sirve para el ejercicio pero es interesante"):** $y(t)$ es **oscilatoria** (por el coseno), **amortiguada** (por la exponencial decreciente) y **desplazada** 5 unidades [57:01].

**Paso 2:** transformar $y(t)$ ("no tiene nada raro"); lo que "tiene feo" es sacar denominador común, se vuelve largo [57:31]–[58:02]:

$$
Y(s) = \frac{10s + 65}{s\,(s^2 + 4s + 13)}
$$

**Paso 3:** dividir por $F(s) = \frac{1}{s}$: la $s$ "pasa multiplicando para arriba" y se simplifica con la $s$ de la salida [58:02]–[58:35]:

$$
G(s) = \frac{10s + 65}{s^2 + 4s + 13}
$$

"Es más cuentitas que otra cosa" [58:35]. Ver 05, ej. 13.

**Paso 4:** cero en $-6{,}5$ ("no es el más lindo de todos, pero es fácil") y el cero en el infinito, que en la resolución escrita le faltó ("muy teórico, pero si se puede poner, mejor"); polos $-2 \pm 3j$ [59:07]–[59:39].

**Paso 5:** corte por el eje real: el cero real hace que la curva toque y rebote en $-6{,}5$; no hay polos reales, así que los complejos dan una **montaña bien marcada** ("una buena panza") a la altura de su parte real, $-2$ [1:00:09]–[1:00:39].

**Paso 6:** en GeoGebra, el corte real pasa siempre por el medio de los dos volcanes conjugados, "por definición", simétricamente: misma parte imaginaria hacia un lado y hacia el otro [1:00:39]–[1:01:09]. Gráfico: <https://www.geogebra.org/m/qb7ahfvr> [OneNote p. 10].

</details>

</details>

## Sistemas físicos: lo único que hay que saber de física — [1:01:40]

- Con las ecuaciones diferenciales de esta unidad se modelan fenómenos físicos (el carrito con resorte, circuitos, un péndulo en la guía) [1:02:11]–[1:02:43].
- "No es necesario saber física": la ecuación diferencial viene dada; "con Matemática Superior alcanza, y con saber que cuando estás en reposo no te estás moviendo" [1:02:43].
- **Parte del reposo** ⇒ posición inicial $y(0) = 0$ y velocidad inicial $y'(0) = 0$; $y(t)$ es la posición del carrito en función del tiempo [1:03:45], [1:05:16]–[1:05:48].
- Método "bastante mecánico": **Laplace miembro a miembro**, se cancelan los términos de condiciones iniciales, factor común $Y(s)$, despeje, fracciones simples y antitransformada [1:04:45]–[1:06:50].

<details>
<summary>📝 Ejercicio 19 — 1:01:40: sistema mecánico de traslación + ¿qué B para que no se amortigüe?</summary>

Sistema mecánico de traslación (carro de masa $M$ unido a la pared por un resorte $K$, con rozamiento $B$ con el piso), con E.D. de movimiento [OneNote p. 10]:

$$
F(t) - K\,y(t) - B\,y'(t) = M\,y''(t)
$$

a) Con $M = 1$ [Kg], $B = 5$ [Kg/s], $K = 4$ [N/m], hallar la respuesta a un escalón unitario sabiendo que parte del reposo (por Laplace).

b) ¿Qué valor debería tener $B$ para que el movimiento no sea amortiguado? Justifique.

<details>
<summary>Ver resolución</summary>

**Paso 1:** la fuerza $F(t)$ se modela como escalón unitario; reemplazar $M$, $B$, $K$ [1:03:14]–[1:04:45].

**Paso 2:** Laplace miembro a miembro: escalón $\to \frac{1}{s}$; $4\,y \to 4\,Y(s)$; $5\,y' \to 5\,[s\,Y(s) - y(0)]$; $y'' \to s^2\,Y(s) - s\,y(0) - y'(0)$. Las fórmulas de las derivadas "las tienen en la tablita, en la ayuda memoria" [1:04:45]–[1:05:16]. Por el reposo se cancelan $y(0)$ e $y'(0)$ [1:05:48].

**Paso 3:** factor común y despeje [1:06:19]–[1:06:50]:

$$
Y(s) = \frac{1}{s\,(s + 1)(s + 4)}
$$

**Paso 4:** raíces reales y distintas: "el caso más fácil de fracciones simples", las tres constantes salen con el truquito: $A = \frac{1}{4}$, $B = -\frac{1}{3}$, $C = \frac{1}{12}$ [1:06:50]. Ver 05, ej. 19.

$$
y(t) = \frac{1}{4} - \frac{1}{3}\,e^{-t} + \frac{1}{12}\,e^{-4t}
$$

(En el audio [1:07:21] el último coeficiente suena como "un medio"; el OneNote y la constante $C = \frac{1}{12}$ que se acaba de calcular dan $\frac{1}{12}$.) Reemplazando $t$ (segundo 10, segundo 100) se obtiene la posición del carrito en ese instante [1:07:21]–[1:07:52].

**Paso 5 (ítem b), manera física/lógica, "muchísimo más fácil"** [1:08:23]–[1:10:33]: $B$ es el coeficiente de rozamiento del carrito con el piso. Un alumno pregunta si lo que amortigua no es el resorte: no, "el resorte lo que te hace es rebotar" (en condiciones ideales solo lo tira para atrás y para adelante); **lo que frena es el rozamiento**. Si $B = 0$ (como los ejercicios de física "considere que el piso es de hielo"), nada lo frena y rebota infinitamente. "Con eso está bien justificado":

$$
B = 0
$$

**Paso 6 (ítem b), manera matemática, "más intrincada"** [1:10:33]–[1:14:39]: el $B$ queda como coeficiente lineal de $s^2 + Bs + 4$. Escribiendo el cuadrático como $(s - \alpha)(s - \beta) = s^2 - (\alpha + \beta)\,s + \alpha\beta$:

- el término independiente es $\alpha\beta = 4 > 0$ ⇒ las dos raíces (si son reales) tienen **el mismo signo** [1:12:04]–[1:12:36];
- el signo lo decide $-\frac{b}{2a}$: con $b = 5$, $-\frac{5}{2} < 0$ ⇒ las dos raíces del lado izquierdo [1:12:36]–[1:13:37]. (El profe se corrige en vivo: "esto no es $-b/2a$, $5$ es $b$" [1:13:06]; y aclara que lo confunden la $B$ mayúscula del rozamiento y la $b$ minúscula del cuadrático [1:14:08].)
- si fueran complejos conjugados, su parte real es justamente $-\frac{b}{2a}$ [1:14:39]–[1:15:11];
- con $B > 0$: polos reales o complejos **del lado izquierdo** ⇒ algo frena al carrito, estable [1:15:11]–[1:15:43];
- con $B < 0$ (físicamente imposible, "la física ya me lo restringió"): polos del lado derecho ⇒ en vez de frenar, **acelera** al carrito, inestable [1:14:08], [1:15:43]–[1:16:14];
- con $B = 0$: queda $s^2 + 4$, polos $\pm 2j$ **sobre el eje**. En fracciones simples aparece $\frac{Xs + Y}{s^2 + 4}$ (el profe usa otras letras para no confundir) ⇒ senos y cosenos de $2t$ **sin desplazamiento en $s$**, o sea sin exponencial que amortigüe ni que acelere ⇒ **marginalmente estable**, el carrito "va y viene, va y viene, nada lo frena" [1:16:14]–[1:17:45].

**Consulta [1:17:45]–[1:19:51]:** ¿tiene que ver con el **factor de amortiguamiento**? El profe dice que sí en parte (el $\alpha$ que acompaña a la $t$), pero la guía no especifica qué pasa con varios polos, y el $\alpha$ se asigna más bien a respuestas **oscilatorias amortiguadas**; la respuesta del ítem a) es **exponencial decreciente** sin seno ni coseno, "así que capaz hablar de ese factor de amortiguamiento no sería del todo correcto". Es un concepto "muy por arriba", que "no se toca demasiado".

</details>

</details>

## Barrido de $B$ en GeoGebra: cómo se mueven los polos — [1:19:51]

El profe muestra un GeoGebra que varía el coeficiente de rozamiento en $s^2 + Bs + 4$ [1:19:51]–[1:23:31]:

| Situación de $B$ | Polos | Respuesta |
|---|---|---|
| $B = 5$ (original) | reales negativos, $-1$ y $-4$ | exponenciales decrecientes |
| un valor intermedio | polo doble real negativo en $-2$, $(s + 2)^2$ | $t\,e^{-\alpha t}$: sigue siendo estable (el $t$ no está acotado, pero la exponencial decreciente lo baja) |
| más chico, todavía positivo | complejos conjugados con parte real negativa | **oscilatoria amortiguada** |
| $B = 0$ | imaginarios puros, sobre el eje | **oscilatoria de amplitud constante** (marginalmente estable) |
| $B < 0$ (la física no lo permite) | complejos con parte real positiva | oscilatoria de **amplitud creciente** |
| $B < 0$ más negativo | reales positivos (ej. $1$ y $4$) | **exponenciales crecientes**, inestable |

El polo doble "no aparece en la guía": los polos múltiples "no les damos bola" [1:22:29]–[1:23:01].

**Conclusión que "quiero que se lleven"** [1:23:31]: $B > 0$ ⇒ polos del lado izquierdo; $B = 0$ ⇒ sobre el eje, marginalmente estable, "nada me frena ni nada me acelera"; $B < 0$ (solo matemáticamente) ⇒ inestable. Y la explicación física es mucho más simple que la matemática [1:24:02].

## Ejercicio integrador: respuesta natural (entrada impulso) y teorema del valor final — [1:24:35]

- Algo que el profe **no había dicho en la teórica** (y dice que lo va a agregar al documento) [1:25:06]: como $Y(s) = G(s)\,F(s)$, si la entrada es el **impulso** $\delta(t)$, entonces $F(s) = 1$ y

$$
Y(s) = G(s)
$$

A eso se lo llama **respuesta natural** del sistema [1:25:37].

- **Teorema del valor final** [1:32:35]–[1:33:06]: el segundo miembro es el valor estable; como las funciones están en el dominio de Laplace, se usa el primero.

$$
\lim_{s \to 0} s\,Y(s) = \lim_{t \to \infty} y(t) = \text{V.E.}
$$

- Lectura rápida de cada forma de transferencia [1:28:18]–[1:32:01]: polos imaginarios puros ⇒ oscila sin amortiguar; desplazamiento $s + 3$ en un cuadrático ⇒ $e^{-3t}$ que amortigua; un término $\frac{A}{s}$ ⇒ corre la respuesta "para arriba o para abajo" (valor estable distinto de $0$).

<details>
<summary>📝 Ejercicio 20 — 1:24:35: ¿cuál da oscilatoria amortiguada con valor estable 2?</summary>

Dadas las transferencias [OneNote p. 11]:

$$
G_1(s) = \frac{6}{s^2 + 9}, \qquad G_2(s) = \frac{2}{s^2 + 6s + 10}, \qquad G_3(s) = \frac{6s + 20}{s^3 + 6s^2 + 10s}
$$

indique cuál corresponde a un sistema cuya respuesta a la entrada impulso $f(t) = \delta(t)$ es **oscilatoria amortiguada con valor estable 2**. Justifique.

<details>
<summary>Ver resolución</summary>

"Se llama integrador, pero la verdad que no integra tanto: es un análisis de los polos" [1:24:35].

**Paso 1:** entrada impulso ⇒ cada $G_i$ es igual a su $Y_i$ [1:26:10]–[1:26:43].

**Paso 2:** dos alternativas [1:26:43]–[1:27:45]: (1) antitransformar las tres y buscar algo del tipo "2 más $e^{-t}$ por $\mathrm{sen}(2t)$" (ejemplo inventado por el profe) — "aburrido"; (2) **teorema del valor final + análisis de polos**, que es la que usa. Ver 05, ej. 20.

**Paso 3 ($G_1$):** polos $\pm 3j$, imaginarios puros, sobre el eje ⇒ marginalmente estable; su antitransformada es directa, $2\,\mathrm{sen}(3t)$: **amplitud constante**, nada la amortigua. Se descarta [1:28:18]–[1:29:21].

**Paso 4 ($G_2$):** $\frac{As + B}{(s + 3)^2 + 1}$ ⇒ el desplazamiento $s + 3$ trae un $e^{-3t}$ y el $+1$ da senos/cosenos de $t$ ⇒ **oscilatoria amortiguada, check**. Pero no tiene nada que la corra: se va apagando hacia $0$ ⇒ valor estable $0$. Se descarta [1:29:21]–[1:30:57].

**Paso 5 ($G_3$):** "medio que por descarte": factor común $s$ en el denominador, $s\,(s^2 + 6s + 10)$ ⇒ $\frac{A}{s} + \frac{Bs + C}{(s + 3)^2 + 1}$. El segundo término da la oscilación amortiguada y el $\frac{A}{s}$ un valor estable distinto de $0$ [1:30:57]–[1:32:01].

**Paso 6:** en vez de fracciones simples, TVF: la $s$ que agrega el teorema se simplifica con la $s$ de $G_3$ y queda $\frac{20}{10} = 2$ ⇒ **Rta.: $G_3$** [1:33:06]–[1:33:37]. "Spoiler alert": la $A$ por el truquito también da $\frac{20}{10} = 2$ [1:32:35]. La respuesta "oscila y se va apagando, pero dos unidades más arriba" [1:33:37].

**Paso 7 (solo comprobación, no es parte del ejercicio)** [1:34:11]–[1:35:47]: fracciones simples dan $\frac{2}{s} + \frac{-2s - 6}{(s + 3)^2 + 1}$; sacando factor común $-2$ queda $s + 3$ arriba y abajo, "no pasa como en otros ejercicios que había que sumar y restar para llegar al mismo desplazamiento":

$$
y(t) = -2\,e^{-3t}\cos(t) + 2
$$

Coseno por la oscilación, exponencial decreciente por el amortiguamiento y el $+2$ como valor estable.

</details>

</details>

## Consulta final: ¿marginalmente estable cuenta como estable? — [1:36:48]

- Un alumno pregunta si está bien poner "estable" cuando es marginalmente estable. Respuesta: **sí, clasifica como estable**. Si te piden estable/inestable y tenés polos (o un par conjugado) sobre el eje, es **estable** porque "no se va al infinito"; si querés aclarar que es marginalmente estable, vale [1:36:48]–[1:37:18].
- Aplica también a exámenes del tipo "el sistema es estable / inestable" para redondear o tachar: si es marginalmente estable, es **estable** [1:37:18]–[1:37:48].
- Aviso de cierre: el jueves siguiente (virtual) se da la teórica de **Transformada Z**, el último tema del primer parcial [1:35:47]–[1:36:18].

---

*Generado el 2026-10-02 a partir de `fuentes/clases/Sistemas Estables/P_SE - Practica.mp4` (transcripción local con Whisper, `apuntes/transcripts/11-video-practica-sistemas-estables.json`, 98 min) y del OneNote de la misma clase (`fuentes/clases/Sistemas Estables/Sistemas Estables.pdf`). Enunciados y fórmulas tomados del OneNote; las cuentas completas están en `05-practica-sistemas-estables.md`.*
