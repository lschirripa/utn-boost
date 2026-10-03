# Serie exponencial y transformada de Fourier (clase teórica grabada)

> Fuente: fuentes/clases/series de fourier/T_serie_exponencial_y_transf_fourier.mp4 (transcripción local con Whisper)

---

> **Cómo usar este apunte.** Es la **teoría** de la clase grabada: cierre de la serie
> trigonométrica (simetría de media onda), **serie exponencial de Fourier** (SEF), relación
> entre período y espectro, y una introducción a la **transformada de Fourier** como puente
> hacia Laplace. La práctica de la SEF está en `02-practica-serie-exponencial-fourier.md`.
> Los timestamps `[mm:ss]` son del video local (sin enlace público). Las fórmulas se
> reconstruyeron solo donde lo dictado no deja dudas; los gráficos (OneNote, GeoGebra,
> video externo) quedaron en pantalla.
>
> **Esta clase no tiene repaso de números complejos:** solo se apoya en lo visto "en la
> primera clase" (formas exponenciales del seno y del coseno, módulo y argumento).

## Índice

- [01:05] — Repaso: fórmula de la serie trigonométrica de Fourier
- [02:38] — Simetría de media onda (funciones periódicas alternadas)
- [07:26] — Consecuencia: solo armónicas impares; combinaciones con paridad
- [11:10] — De la serie trigonométrica a la exponencial (fórmulas de Euler)
- [13:51] — $C_n$, $C_{-n}$, $C_0$ y la forma compacta de la SEF
- [18:09] — $C_n = \tfrac12(a_n - b_n j)$: el puente entre las dos series y la fórmula integral del $C_n$
- [21:46] — Con funciones pares o impares conviene calcular $a_n$ / $b_n$ y traducir
- [25:55] — Resumen de la SEF y por qué el $C_0$ ya viene dividido por 2
- [27:29] — Consulta: error de signo en la hoja de fórmulas del campus
- [28:30] — $C_n$ complejo: coeficientes reales (función par) o imaginarios puros (función impar)
- [31:48] — 📝 Ejercicio 1: SEF del pulso que vale $0$ en $(-\pi, 0)$ y $\pi$ en $(0, \pi)$
- [39:34] — Espectro de frecuencias: amplitudes y fase
- [40:41] — 📝 Ejercicio 2: espectros de amplitud y de fase del Ejercicio 1
- [45:57] — Relación entre período y espectro (y un error de la guía teórica)
- [47:35] — 📝 Ejercicio 3: tren de pulsos de ancho 1 y período $T$ ($T = 2, 4, 10$)
- [58:14] — $T \to \infty$: de espectro discreto a espectro continuo
- [1:02:33] — Lo que está mal en el ejercicio 10 de la guía (achicar el ancho del pulso)
- [1:06:12] — Consultas: pulso cada vez más ancho, frecuencia vs. pulso, qué se grafica
- [1:15:09] — Transformadas integrales y antitransformadas
- [1:18:22] — Condiciones para aplicar la transformada de Fourier
- [1:19:24] — Definición de la transformada de Fourier y su antitransformada
- [1:23:02] — 📝 Ejercicio 4: transformada de Fourier del pulso $|t| < a$
- [1:26:42] — 📝 Ejercicio 5: transformada de Fourier de $e^{-ct}$ para $t > 0$
- [1:31:31] — La transformada de Fourier no se toma
- [1:32:04] — 📝 Ejercicio 6: de la transformada de Fourier a la de Laplace
- [1:35:13] — Tablas de transformadas
- [1:35:44] — Cierre de series trigonométricas: par, impar y media onda son condicionales de ida
- [1:38:26] — Consulta final: serie (aproximar) vs. transformada (cambiar de dominio)

## Lo que el profe remarca

**Sobre parcial y final (qué se toma y cómo)**

- **[1:31:31]** "**Transformada de Fourier no se toma.** Vamos a trabajar siempre con transformada de Laplace". La usa "como puente entre un tema y el otro"; "no se va a tomar en un examen. Así que en eso pueden quedarse tranquilos". **[1:34:11]** Para Fourier solo hay "un ejemplito" en la clase práctica. **[1:35:44]** La tabla de transformadas de Fourier "ni la llegamos a ver".
- **[1:15:09]** La cátedra no hace foco en la transformada de Fourier: la usa como introducción a Laplace, que **[1:32:04]** es "el tema central de la primera parte de la materia (…) hasta el primer parcial".
- **[1:02:01]** "Esto se viene preguntando **mucho en los finales** de forma teórica": dada una función, ¿su espectro es discreto o continuo? **Periódica → discreto; aperiódica → continuo**. De la tabla de la guía importan "más que nada estos dos primeros renglones"; los otros "son más avanzados y en la cátedra no se toca el tema" **[1:02:33]**.
- **[1:36:46]** "Es algo que **se tomó en el último final y nadie lo hizo bien**" (aunque "no era un error grave"): par ⇒ $b_n = 0$, impar ⇒ $a_0 = a_n = 0$, media onda ⇒ solo armónicas impares son **condicionales de ida**. **[1:37:24]** No vale el recíproco: puede haber funciones con $b_n = 0$ que no son pares.
- **[29:00]** "En un **montonazo de ejercicios**" se pide **completar la función** para que su serie sea solo de cosenos (→ par) o solo de senos (→ impar); **[30:39]** en la SEF la misma consigna aparece como "que los coeficientes sean **todos reales**" (→ par) o "**imaginarios puros**" (→ impar). **[31:09]** "Esos términos se los van a encontrar mucho".
- **[40:41]** En la cátedra se le da "mucha más bola al **espectro de amplitud**" que al de fase; **[44:55]** "se usa más y **se va a pedir más** el espectro de amplitudes".
- **[18:09]** "No hay demasiados ejercicios de serie exponencial": la cátedra le da más énfasis a la **serie trigonométrica** (lo repite en **[24:53]**: la guía hace mucho más foco en la trigonométrica).
- **[02:38]** Lo que se anula según la paridad "es muy importante y va a pasar en muchísimos de los ejercicios".
- **[10:39]** En la guía hay ejercicios de **simetría de media onda** para practicar; **[09:33]** la "simetría de media onda desplazada" la ve en la práctica.
- **[13:51]** El desarrollo de trigonométrica a exponencial "no es algo que tengan que saber", pero sí de dónde viene.

**Recomendaciones, errores típicos y trucos**

- **[18:09]** $C_n = \tfrac12(a_n - b_n j)$ es "**súper importante**": es el puente entre las dos series.
- **[23:52]**–**[25:24]** **Recomendación**: si la función es **par o impar**, calculá $a_n$ y/o $b_n$ con las fórmulas de la trigonométrica (aprovechando lo que se anula) y traducilos al $C_n$. Con la integral del $C_n$ se pierde esa ventaja, porque $e^{-jn\omega x}$ no es ni par ni impar **[23:20]**. Usar directo el $C_n$ "será más largo, más complicado, pero no pasa nada".
- **[27:29]**–**[28:30]** **Error en la hoja de fórmulas del campus** (la que señaló un alumno, con secciones de números complejos, series de Fourier y serie exponencial): ahí el $C_n$ aparece con **exponente positivo** y como $a_n + b_n j$. "Esto está mal. Es con el menos": $-\,b_n j$ y $-$ en el exponente. [En el ayudamemoria oficial del repo, pág. 1, la SEF figura solo como $S(x)$, sin la fórmula del $C_n$.]
- **[26:26]** El $C_0$ **ya incluye la división por 2** ($C_0 = a_0/2$): sigue siendo el valor medio.
- **[31:48]** "Lo primero que yo quiero que hagan en estos ejercicios es **graficar**".
- **[42:12]** "Muy muy importante": los espectros se grafican con $n\omega$ en el eje horizontal; la separación entre dos puntos es $\omega$ (la frecuencia fundamental).
- **[45:57]**–**[46:29]** La **guía teórica tiene una explicación mal** desde hace años (ejercicio 10, pulso rectangular): la conclusión es correcta pero el razonamiento no. **[1:04:39]** Si en una clase vieja o en un ejercicio ven que achicando el **ancho del pulso** sin tocar el período el espectro se vuelve continuo, "**eso está mal**": lo correcto es que la función **deje de ser periódica** ($T \to \infty$).
- **[1:13:35]** "No me importa que $T$ sea infinito, eso no es el punto. Lo importante es que la función **deje de ser periódica**".
- **[1:14:38]** El gráfico de $C_n$ (que cruza el eje, con valores positivos y negativos) **no es** el espectro de amplitudes: las amplitudes son módulos y son siempre positivas.
- **[1:27:19]** En la transformada de Fourier de $e^{-ct}$ es "muy importante" que la exponencial sea **negativa** ($c > 0$): si creciera, no sería integrable y no se le podría aplicar la transformada.

**Números complejos y el primer parcial:** en esta clase el profe **no dice nada** sobre si los números complejos entran como ejercicio en el parcial; solo remite a "la primera clase" / "la unidad de complejos" para las formas exponenciales y para módulo y argumento.

## Repaso: fórmula de la serie trigonométrica de Fourier — [01:05]

La serie trigonométrica representa una función periódica como suma de senos y cosenos [01:05]:

$$
S(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ a_n \cos(n\omega x) + b_n \operatorname{sen}(n\omega x) \right]
$$

- $\frac{a_0}{2}$ es el **valor medio** [01:05].
- Las "tres formulitas" de los coeficientes son "lo más importante que se tiene que haber llevado" de la clase anterior [01:37]. Según el [ayudamemoria], con $L = T/2$:

$$
a_n = \frac{1}{L} \int_{-L}^{L} f(x) \cos(n\omega x)\, dx
\qquad
b_n = \frac{1}{L} \int_{-L}^{L} f(x) \operatorname{sen}(n\omega x)\, dx
$$

- Contexto histórico [01:37]–[02:07]: la trigonométrica fue la primera forma que encontró Fourier, pero se pueden construir series de Fourier con cualquier base ortonormal; las más famosas son la trigonométrica y la exponencial.

## Simetría de media onda (funciones periódicas alternadas) — [02:38]

No es un concepto propio de la serie trigonométrica sino de funciones en general: aplica a cualquiera de las dos series [02:38].

- Recordatorio [03:11]: $f$ es **par** si $f(x) = f(-x)$ y es **impar** si $f(x) = -f(-x)$.
- **Simetría de media onda** [03:46]–[04:18] (con $L = T/2$, la mitad del período):

$$
f(x) = -f(x \pm L) \qquad \left(\text{en el [ayudamemoria]: } f(x) = -f\!\left(x + \tfrac{T}{2}\right)\right)
$$

**Cómo verla en el gráfico (dos pasos)** [04:18]–[05:52]:

**Paso 1:** tomá una de las "ramas" de la función en medio período y **trasladala $L$** (un semiperíodo) a izquierda o a derecha.

**Paso 2:** al trozo trasladado aplicale el **menos**: espejalo respecto del eje $x$.

Si el dibujo trasladado y dado vuelta **coincide con la gráfica**, la función tiene simetría de media onda [05:52].

- Ejemplo del **seno** [05:52]–[06:54]: período $2\pi$, $L = \pi$. Tomás la "jorobita" de $(0, \pi)$, la corrés $\pi$ a la izquierda, la espejás respecto del eje $x$ y obtenés la jorobita negativa: el seno tiene simetría de media onda.
- Es una simetría que "cuesta un poquito más verla" que la paridad, porque no estamos tan acostumbrados [06:54].

## Consecuencia: solo armónicas impares; combinaciones con paridad — [07:26]

Si una función tiene simetría de media onda, su serie de Fourier **solo tiene armónicas impares** [07:26]: $a_n = b_n = 0$ para todo $n$ par. De $a_0$, $a_n$ y $b_n$ (separados en pares e impares), **no tiene $a_0$**, ni $a_n$ de subíndice par, ni $b_n$ de subíndice par [08:28]–[09:00]: solo sobreviven $a_n$ y $b_n$ con $n$ impar.

- Pista práctica [07:56]–[08:28]: cuando en un ejercicio aparece algo como $1 - (-1)^n$ y terminan escribiendo la sumatoria en función de $2k+1$ (solo armónicas impares), puede ser porque la función tiene simetría de media onda.
- **Combinaciones** [09:00]: la simetría de media onda puede darse sola, junto con paridad o junto con imparidad (y una función puede ser par o impar sin media onda). Las conclusiones se combinan: par → solo $a_n$; impar → solo $b_n$; media onda → solo armónicas impares [09:33].
- Hay una "simetría de media onda **desplazada**" (nombre del profe) que se ve en la práctica [09:33]–[10:06].

## De la serie trigonométrica a la exponencial (fórmulas de Euler) — [11:10]

Mismo concepto que antes (sumar cosas para llegar a una función periódica), pero ahora se suman **exponenciales** [11:10]. La SEF **sale de la trigonométrica** [11:41], reemplazando seno y coseno por sus formas exponenciales (vistas en la primera clase):

$$
\cos \varphi = \frac{e^{j\varphi} + e^{-j\varphi}}{2}
\qquad
\operatorname{sen} \varphi = \frac{e^{j\varphi} - e^{-j\varphi}}{2j} = \frac{j\left(e^{-j\varphi} - e^{j\varphi}\right)}{2}
$$

(las dos formas del seno "son básicamente lo mismo": una tiene $2j$ en el denominador y la otra la $j$ en el numerador con los signos cambiados [11:41]–[12:14]).

Se reemplaza en la serie trigonométrica (donde decía $\cos(n\omega x)$ ahora va $\frac{e^{jn\omega x} + e^{-jn\omega x}}{2}$, y lo correspondiente para el seno), se hacen las distributivas y quedan cuatro términos [12:14]–[12:48]. Se agrupan sacando factor común según el **exponente positivo o negativo** [12:48]–[13:20]:

$$
S(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} \left[ \tfrac12 (a_n - b_n j)\, e^{jn\omega x} + \tfrac12 (a_n + b_n j)\, e^{-jn\omega x} \right]
$$

## $C_n$, $C_{-n}$, $C_0$ y la forma compacta de la SEF — [13:51]

Por comodidad se ponen nombres [13:51]–[14:22]:

$$
C_n = \tfrac12 (a_n - b_n j)
\qquad
C_{-n} = \tfrac12 (a_n + b_n j)
\qquad
C_0 = \frac{a_0}{2}
$$

- $C_0$ es la misma constante de antes (el valor medio) y se calcula igual [14:22].

Con eso la serie queda [14:55] (es la forma que figura en el [ayudamemoria]):

$$
S(x) = C_0 + \sum_{n=1}^{\infty} \left[ C_n\, e^{jn\omega x} + C_{-n}\, e^{-jn\omega x} \right]
$$

- $\omega$ y $n$ siguen siendo lo mismo que antes; ahora aparece la unidad imaginaria $j$ [15:26].

**Forma reducida (la que se usa)** [15:26]–[15:57]: en vez de separar $C_n$ y $C_{-n}$, se cambian los límites de la sumatoria para que vaya de $-\infty$ a $+\infty$ (todos los enteros):

$$
S(x) = \sum_{n=-\infty}^{\infty} C_n\, e^{jn\omega x}
$$

- Sobre el $C_{-n}$ [15:57]–[16:28]: el profe no quiere "ahondar demasiado en estos detalles"; dice que "termina siendo lo mismo que el $C_n$", que "solo sirve para mostrar el desarrollo" y que **solo se calcula un término, el $C_n$** (en los ejemplos, los $n$ negativos salen de la misma fórmula del $C_n$).
- **El $C_0$ aparte** [16:28]–[17:37]: igual que en la trigonométrica, donde $a_0$ se calculaba aparte. "Entiendo que se puede sacar con el límite", pero él siempre calcula $C_0$ aparte y escribe:

$$
S(x) = C_0 + \sum_{\substack{n=-\infty \\ n \neq 0}}^{\infty} C_n\, e^{jn\omega x}
$$

- Son formas equivalentes; siempre se trabaja con las reducidas que tienen $C_n$ y no $C_{-n}$ [17:37].

## $C_n = \tfrac12(a_n - b_n j)$: el puente entre las dos series y la fórmula integral del $C_n$ — [18:09]

$$
C_n = \tfrac12 (a_n - b_n j)
$$

- "Súper importante": es **el puente** entre la serie trigonométrica y la exponencial [18:09]. Si ya sabés cuánto valen $a_n$ y $b_n$, reemplazás, multiplicás el $b_n$ por $j$, dividís todo por 2 y tenés el $C_n$ [18:39]–[19:09].
- La cátedra le da más énfasis a la trigonométrica: "no hay demasiados ejercicios de serie exponencial" [18:09]–[18:39].

**Deducción de la fórmula integral** [19:09]–[21:16]:

**Paso 1:** reemplazar $a_n$ y $b_n$ por sus integrales. Como los dos van multiplicados por $\frac1L$ y se integran en el mismo intervalo $[-L, L]$, se juntan en una sola integral; el $\frac12$ da el $\frac{1}{2L}$ [19:42]:

$$
C_n = \frac{1}{2L} \int_{-L}^{L} f(x) \left[ \cos(n\omega x) - j \operatorname{sen}(n\omega x) \right] dx
$$

**Paso 2:** por paridad, $\cos(n\omega x) = \cos(-n\omega x)$ (coseno par) y $-\operatorname{sen}(n\omega x) = \operatorname{sen}(-n\omega x)$ (seno impar) [20:15]–[20:45]:

$$
\cos(n\omega x) - j \operatorname{sen}(n\omega x) = \cos(-n\omega x) + j \operatorname{sen}(-n\omega x) = e^{-jn\omega x}
$$

**Paso 3:** queda la fórmula que se usa siempre que haya que calcular el $C_n$ [21:16]:

$$
C_n = \frac{1}{2L} \int_{-L}^{L} f(x)\, e^{-jn\omega x}\, dx
$$

## Con funciones pares o impares conviene calcular $a_n$ / $b_n$ y traducir — [21:46]

- Recordatorio [21:46]–[22:18]: con $f$ **par** se anula $b_n$; con $f$ **impar** se anulan $a_0$ y $a_n$. Ventaja: lo que se anula **ni se calcula**.
- Eso salía de que en $a_n$ siempre se integra $f$ por un **coseno** (par) y en $b_n$ por un **seno** (impar) [22:48]–[23:20], y se aprovecha el producto par·par, par·impar, etc.
- Con el $C_n$ esa ventaja **se pierde** [23:20]: aunque $f$ sea par o impar, $e^{-jn\omega x}$ no es ni par ni impar, así que no se pueden hacer "estos truquitos".

**Recomendación del profe** [23:52]–[25:24]:

- $f$ **par**: no calcules $b_n$; calculá $a_n$ como siempre y $C_n = \tfrac12 a_n$.
- $f$ **impar**: no calcules $a_n$; calculá $b_n$, cambiale el signo, dividilo por 2 y multiplicalo por $j$: $C_n = -\tfrac12 b_n\, j$.
- En general: "yo trabajo con los coeficientes (…) de la serie trigonométrica y a eso los traduzco al $C_n$", salvo que sea muy fácil con el $C_n$ directo. Además están más "cancheros" con las integrales de seno y coseno que con la $e$ y la $j$ [24:53].

## Resumen de la SEF y por qué el $C_0$ ya viene dividido por 2 — [25:55]

Lo que hay que llevarse [25:55]: cómo se escribe la SEF, cómo se pasa de trigonométrica a exponencial y viceversa con la relación entre $a_n$, $b_n$ y $C_n$, la integral del $C_n$ ("válida para usarla siempre") y cómo se calcula el $C_0$:

$$
C_0 = \frac{1}{2L} \int_{-L}^{L} f(x)\, dx = \frac{a_0}{2}
$$

- La única diferencia con el $a_0$ es el **2** en el denominador [25:55]–[26:26]: la división por 2 que antes se hacía después ya viene metida en el cálculo. El profe cree que es "por una cuestión de consistencia": las fórmulas de la trigonométrica llevan $\frac1L$ y las de la exponencial $\frac{1}{2L}$ [26:57]. $C_0$ **sigue siendo el valor medio** [27:29].

## Consulta: error de signo en la hoja de fórmulas del campus — [27:29]

Un alumno señala que en la hoja de fórmulas del campus virtual (con secciones de números complejos, series de Fourier y serie exponencial) el $C_n$ figura con $e^{+jn\omega_0 x}$ dentro de la integral y como $a_n + b_n j$ [27:29]. El profe la revisa: "**esto está mal. Es con el menos**", tanto en $-\,b_n j$ como en el exponente [27:59]–[28:30]. Las correctas son las de este apunte.

## $C_n$ complejo: coeficientes reales (función par) o imaginarios puros (función impar) — [28:30]

- $a_n$ y $b_n$ son **reales**, pero $C_n = \tfrac12(a_n - b_n j)$ es un **número complejo**: tiene parte real ($a_n$) y parte imaginaria (lo que acompaña a la $j$, el $b_n$) [28:30]–[29:00].
- Traducción de las consignas típicas [29:00]–[31:09]:

| Consigna | Qué se anula | Condición sobre $f$ | $C_n$ |
|---|---|---|---|
| Serie trigonométrica **solo de cosenos** / SEF con coeficientes **todos reales** | $b_n$ | **par** | $C_n = \tfrac12 a_n$ (real) |
| Serie trigonométrica **solo de senos** / SEF con coeficientes **imaginarios puros** | $a_n$ | **impar** | $C_n = -\tfrac12 b_n\, j$ (imaginario puro) |

- "Las funciones pares son solo de cosenos y están asociadas a coeficientes reales de la serie exponencial. Y las impares (…) a series de senos (…) y sus coeficientes (…) son imaginarios puros" [31:09].

<details>
<summary>📝 Ejercicio 1 — 31:48: SEF del pulso que vale 0 en (−π, 0) y π en (0, π)</summary>

Desarrollar en serie exponencial de Fourier la función periódica (período $2\pi$):

$$
f(t) =
\begin{cases}
0 & -\pi < t < 0 \\
\pi & 0 < t < \pi
\end{cases}
$$

(Gráfico: un pulso de altura $\pi$ entre $0$ y $\pi$ que se repite, y $0$ en el medio [32:22]. "A priori no se ve paridad", aunque sí tiene una que se charla en la práctica.)

<details>
<summary>Ver resolución</summary>

**Paso 1 (datos):** $T = 2\pi$, $L = \pi$, $\omega = \frac{\pi}{L} = 1$ [32:54].

**Paso 2 ($C_0$):** como la función vale $0$ en la mitad del período, solo se integra entre $0$ y $\pi$ [32:54]–[33:26]:

$$
C_0 = \frac{1}{2\pi} \int_{0}^{\pi} \pi\, dt = \frac{\pi^2}{2\pi} = \frac{\pi}{2}
$$

Es el valor medio: la recta que deja la misma área por arriba y por abajo [33:26].

**Paso 3 ($C_n$):** aplicando la fórmula, directamente entre $0$ y $\pi$ [33:26]–[33:58]; los $\pi$ se cancelan:

$$
C_n = \frac{1}{2\pi} \int_{0}^{\pi} \pi\, e^{-jnt}\, dt = \frac12 \int_{0}^{\pi} e^{-jnt}\, dt
$$

**Paso 4 (Barrow):** se divide por lo que acompaña a la $t$ ($-jn$), se evalúa primero en $\pi$ y después en $0$ ($e^0 = 1$) y se pasa el menos al numerador cambiando el orden [33:58]–[34:59]:

$$
C_n = \frac{e^{-jn\pi} - 1}{-2jn} = \frac{1 - e^{-jn\pi}}{2jn}
$$

**Paso 5 ($e^{\pm jn\pi}$):** como $\operatorname{sen}(n\pi) = 0$ siempre y $\cos(n\pi) = \cos(-n\pi) = (-1)^n$ [34:59]–[36:00]:

$$
e^{\pm jn\pi} = \cos(n\pi) \pm j \operatorname{sen}(n\pi) = (-1)^n
$$

$$
C_n = \frac{1}{2jn} \left[ 1 - (-1)^n \right]
$$

**Paso 6 (pares e impares):** [36:30]–[37:33]

- $n$ **par**: $1 - 1 = 0$, así que $C_n = 0$ (se anulan todas las armónicas pares).
- $n$ **impar**: $1 - (-1) = 2$, el 2 se simplifica y queda $\frac{1}{jn}$. Multiplicando y dividiendo por $j$ para no dejar la $j$ en el denominador (así está en la guía):

$$
C_n = \frac{1}{jn} = -\frac{j}{n} \qquad (n \text{ impar})
$$

**Paso 7 (algunos valores):** [37:33]–[38:33]

$$
C_1 = -j \qquad C_{-1} = j \qquad C_3 = -\frac{j}{3} \qquad C_{-3} = \frac{j}{3} \qquad C_{\pm 2} = C_{\pm 4} = \dots = 0 \qquad C_0 = \frac{\pi}{2}
$$

**Paso 8 (la serie):** el valor medio más la sumatoria; el menos sale del $-\frac{j}{n}$, y $n$ se escribe como $2k+1$ para mostrar que solo hay armónicas impares; $\omega = 1$ [38:33]–[39:34]:

$$
S(t) = \frac{\pi}{2} - j \sum_{k} \frac{1}{2k+1}\, e^{j(2k+1)t}
$$

[los límites de la sumatoria en $k$, paso en el pizarrón, ver video]

</details>

</details>

## Espectro de frecuencias: amplitudes y fase — [39:34]

- Para lo que realmente se usa una serie de Fourier: tomar una señal en función del tiempo y **traducirla en sus frecuencias** [39:34]–[40:04]. Esa descomposición sale del **espectro de frecuencias de los $C_n$**.
- Por eso en la práctica (fuera de la facultad) se usa más la exponencial: el $C_n$ ya contiene la información de $a_n$ y $b_n$ juntos [40:04].
- Como el $C_n$ es complejo, tiene **módulo (amplitud)** y **argumento (fase)** [40:41]:
  - **Espectro de amplitudes**: $|C_n|$ para cada $n$. Es el que más se usa y se pide.
  - **Espectro de fase**: $\arg C_n$ para cada $n$. "No le damos tanta pelota".
- A medida que $n$ crece, el módulo se achica. Característica de $a_n$, $b_n$ y $C_n$ [41:41]: los gráficos se hacen asintóticos al eje hacia $\pm\infty$.

$$
\lim_{n \to \infty} C_n = 0
$$

- **Eje horizontal: $n\omega$** ("muy muy importante") [42:12]: cada separación entre un punto y el siguiente es un $\omega$, la **frecuencia fundamental**, que es justamente "la separación entre una frecuencia y la otra".

<details>
<summary>📝 Ejercicio 2 — 40:41: espectros de amplitud y de fase del Ejercicio 1</summary>

Con $C_0 = \frac{\pi}{2}$, $C_n = -\frac{j}{n}$ para $n$ impar y $C_n = 0$ para $n$ par (Ejercicio 1), graficar el espectro de amplitudes y el de fase.

<details>
<summary>Ver resolución</summary>

**Paso 1 (amplitudes):** se calcula el módulo de $C_n$ para cada $n$ [40:41]–[41:41]. Para $n = 1$, $C_1 = -j$, de módulo $1$. Los pares se anulan. En general:

$$
|C_n| = \left| -\frac{j}{n} \right| = \frac{1}{|n|} \quad (n \text{ impar}), \qquad |C_n| = 0 \quad (n \text{ par})
$$

Los módulos se achican a medida que $n$ crece. En el eje horizontal va $n\omega$; acá $\omega = 1$, así que la separación entre puntos es $1$ [42:12]–[42:42]. [gráfico en el pizarrón, ver video]

**Paso 2 (fase de los pares):** $C_n = 0$, y "el número cero tiene ángulo cero": fase $0$ [43:15].

**Paso 3 (fase de los impares negativos):** por ejemplo $C_{-1} = -\frac{j}{-1} = j$, imaginario puro positivo: argumento $\frac{\pi}{2}$ (90°). Pasa para **todos** los impares negativos [43:15]–[43:50].

**Paso 4 (fase de los impares positivos):** por ejemplo $C_1 = -j$, imaginario puro negativo: argumento $\frac{3\pi}{2}$. Pasa para todos los impares positivos [43:50]–[44:24].

**Paso 5 (lectura):** el módulo va cambiando, pero la fase de los impares es siempre la misma porque son siempre imaginarios puros; solo cambia si son positivos ($\frac{\pi}{2}$) o negativos ($\frac{3\pi}{2}$) [44:24]–[44:55]. En el gráfico: palitos "más bajitos" hasta $\frac{\pi}{2}$ de un lado y "más altos" hasta $\frac{3\pi}{2}$ del otro.

</details>

</details>

## Relación entre período y espectro (y un error de la guía teórica) — [45:57]

- "Hay algo que se viene dando mal en la cátedra hace muchísimos años": algo mal explicado en la guía teórica. El profe ya lo habló con la jefa de cátedra, que está de acuerdo, pero todavía no se modificó [45:57]–[46:29].
- Lo trabaja con un OneNote propio, "**Relación entre período y espectro**" [47:02], vinculado al **ejercicio 10 de la guía** (serie exponencial): un pulso rectangular con un parámetro $k$ que modifica el ancho del pulso y pregunta qué conclusiones se sacan [47:02]–[47:35]. "La conclusión a la que llega es correcta, pero llega de forma equívoca".
- Plantea un ejercicio parecido (no igual) para llegar a la conclusión correcta [47:35].

<details>
<summary>📝 Ejercicio 3 — 47:35: tren de pulsos de ancho 1 y período T (T = 2, 4, 10)</summary>

Pulso rectangular de **ancho fijo 1** y período $T$ genérico, $L = \frac{T}{2}$, $\omega_0 = \frac{2\pi}{T}$ [48:07]–[48:39]:

$$
f(t) =
\begin{cases}
0 & -\frac{T}{2} < t < -\frac12 \\
1 & -\frac12 < t < \frac12 \\
0 & \frac12 < t < \frac{T}{2}
\end{cases}
$$

Calcular $C_0$ y $C_n$ y ver qué pasa con el espectro cuando $T$ aumenta.

<details>
<summary>Ver resolución</summary>

**Paso 1 ($C_0$):** la integral sería entre $-\frac{T}{2}$ y $\frac{T}{2}$, pero solo es no nula entre $-\frac12$ y $\frac12$, donde vale $1$ [48:39]–[49:10]:

$$
C_0 = \frac{1}{2L} \int_{-1/2}^{1/2} 1\, dt = \frac{1}{2L} = \frac{1}{T}
$$

**Paso 2 ($C_n$):** misma fórmula, con $\omega_0 = \frac{2\pi}{T}$ y $2L = T$ [49:10]–[49:43]:

$$
C_n = \frac{1}{T} \int_{-1/2}^{1/2} e^{-jn\frac{2\pi}{T}t}\, dt = \frac{1}{T} \left[ \frac{e^{-jn\frac{2\pi}{T}t}}{-jn\frac{2\pi}{T}} \right]_{-1/2}^{1/2}
$$

**Paso 3:** al evaluar se cancelan los 2; "no es lo importante, el álgebra de todo esto" [49:43]–[50:17] [paso en el pizarrón, ver video]. El $2j$ que sobra se lo "presta" a la resta de exponenciales para formar un seno [50:17]–[50:49]:

$$
C_n = \frac{1}{n\pi} \cdot \frac{e^{jn\pi/T} - e^{-jn\pi/T}}{2j} = \frac{1}{n\pi} \operatorname{sen}\!\left( \frac{n\pi}{T} \right)
$$

**Paso 4 (forma "seno de algo sobre algo"):** para que aparezca la función conocida de Análisis 1, $\frac{\operatorname{sen} x}{x}$, se multiplica y divide por $\frac1T$ [50:49]–[51:50]:

$$
C_n = \frac{1}{T} \cdot \frac{\operatorname{sen}\!\left( \frac{n\pi}{T} \right)}{\frac{n\pi}{T}}
$$

**Paso 5 (GeoGebra: qué hace el período):** con el ancho del pulso fijo en 1, al agrandar $T$ los pulsos se **separan** cada vez más; en el infinito solo queda el pulso del medio, los otros "están infinitamente lejanos, es como si no existieran" [52:54]–[53:26].

**Paso 6 ($T = 2$):** $\omega = \frac{2\pi}{2} = \pi$ [53:56]–[54:29]. El seno queda $\operatorname{sen}\frac{n\pi}{2}$, que se anula cuando $\frac{n\pi}{2}$ es múltiplo entero de $\pi$: en **todos los $n$ pares** [54:29]–[54:59]. Para $n = 1$ [55:36]–[56:10] (las $T$ se cancelan):

$$
C_1 = \frac12 \cdot \frac{\operatorname{sen}\frac{\pi}{2}}{\frac{\pi}{2}} = \frac{1}{\pi}
\qquad
C_2 \propto \operatorname{sen}(\pi) = 0
\qquad
C_0 = \frac12
$$

El gráfico queda espejado ($C_n$ es par en $n$: lo que le pasa al $1$ le pasa al $-1$) [56:10]. Entre $C_0$ y la primera raíz hay **una sola** armónica ($n = 1$) [56:41].

**Paso 7 ($T = 4$):** las raíces caen en los **múltiplos de 4** y $C_0 = \frac14$ [56:41]–[57:12]. Entre $C_0$ y la primera raíz ahora hay **3 puntitos** ($C_1$, $C_2$, $C_3$); se anula en $4$, después $5, 6, 7$ y se vuelve a anular en $8$ [57:12].

**Paso 8 ($T = 10$):** las raíces caen en los múltiplos de 10, así que entre el origen y la primera raíz hay muchos más puntos: el espectro se va volviendo "más denso, con más puntitos en el medio, más poblado" [57:44]–[58:14].

**Paso 9 (por qué):** el eje horizontal es $n\omega$ y $\omega = \frac{2\pi}{T}$: cuanto más grande $T$, más chico $\omega$, que es la separación entre una frecuencia y la siguiente [58:14]–[58:48]:

$$
T = 2 \Rightarrow \omega = \pi \approx 3{,}14
\qquad
T = 4 \Rightarrow \omega = \frac{\pi}{2} \approx 1{,}57
\qquad
T = 10 \Rightarrow \omega = \frac{\pi}{5}
$$

</details>

</details>

## $T \to \infty$: de espectro discreto a espectro continuo — [58:14]

- La separación entre frecuencias se hace cada vez más chica; cuando $T \to \infty$ ya no hay separación y el espectro deja de ser **discreto** (puntitos separados) para volverse **continuo** [58:48]–[59:19]. Es la conclusión a la que quiere llegar la guía, y es cierta.
- ¿Por qué? Con $T$ infinito queda un solo pulso: la función **deja de ser periódica** [59:50]. "Solo las funciones periódicas tienen espectros discretos"; cuando dejan de serlo (lo que se trabaja con la **transformada de Fourier**), el espectro se vuelve continuo [1:00:21].
- En GeoGebra: al agrandar el período los pulsos se alejan y los puntitos verdes del espectro se acercan [1:00:21]–[1:00:56]. Lo mismo se ve en un video externo (desde el minuto 30): $\tau$ (ancho del pulso) constante y $T$ creciendo; dentro de la primera "campanita" del espectro se ven tres líneas al principio y se va poblando [1:12:00]–[1:13:35].

**Conclusión de la guía de Fourier (tabla final)** [1:01:29]–[1:02:01], [1:05:40]:

| Señal | Herramienta | Espectro |
|---|---|---|
| Continua y **periódica** (todas las de series) | Serie de Fourier (trigonométrica o exponencial) | **Discreto** y aperiódico |
| Continua y **aperiódica** | Transformada de Fourier | **Continuo** (y aperiódico) |

- De la tabla importan "más que nada estos dos primeros renglones"; los otros son más avanzados y no se tocan en la cátedra [1:02:33].
- "No me importa que $T$ sea infinito, eso no es el punto. Lo importante es que la función deje de ser periódica. Cuando una función es aperiódica, el espectro es continuo. (…) Y cuando una función es periódica, su espectro es discreto" [1:13:35]–[1:14:05].

## Lo que está mal en el ejercicio 10 de la guía (achicar el ancho del pulso) — [1:02:33]

- Clases viejas encaran el ejercicio 10 por el **ancho del pulso** en vez de agrandar el período [1:02:33].
- En la guía el pulso va de $-\frac{\pi}{k}$ a $\frac{\pi}{k}$ con el **período fijo**, y se hace $k \to \infty$ [1:03:04]: los pulsos se vuelven cada vez más cortitos (con $k$ = un millón, entre $-\frac{\pi}{10^6}$ y $\frac{\pi}{10^6}$).
- Lo que queda son **puntos separados que se repiten cada $T$** [1:03:38]: eso **sigue siendo periódico**, así que no se puede concluir que el espectro sea continuo, porque "solo tienen espectro continuo las funciones que son aperiódicas" [1:03:38]–[1:04:09].
- En realidad el tren de pulsos se transforma en un **tren de impulsos** (Delta de Dirac, que se ve en Laplace) y habría que usar la transformada de Fourier discreta, "algo que ni siquiera se ve en la materia" [1:04:09]–[1:04:39].
- Regla: si ven que **sin tocar el período** el espectro se vuelve continuo por el ancho del pulso, **está mal**; lo correcto es cuando la función **deja de ser periódica** [1:04:39].

## Consultas: pulso cada vez más ancho, frecuencia vs. pulso, qué se grafica — [1:06:12]

- **¿Y si el pulso se hace cada vez más ancho?** [1:06:12]–[1:08:13]: hay que tener cuidado de no pasarse del período; en un momento el pulso ocupa todo y la función se vuelve **constante** ($= 1$), que tampoco es "algo periódico" en el sentido buscado. Su serie vale $1$: todas las integrales de los $C_n$ dan cero y solo queda $C_0$ (el término medio). El espectro es nulo porque $C_n$ es el número cero ("no es que no existe").
- **Frecuencia vs. pulso** [1:08:45]–[1:09:47]: la frecuencia, "para lo que a nosotros nos importa", es la diferencia entre una armónica y la otra. "Pulso" es solo el nombre de un tipo de función (cuadradita), como "diente de sierra". **Tren de pulsos**: muchos pulsos (infinitos) seguidos [1:10:17].
- **¿Por qué es aperiódica cuando $T \to \infty$?** [1:09:47]–[1:10:49]: el pulso del medio no cambia de ancho; las repeticiones se alejan hasta que ya no se pueden localizar: la función es solo ese pulso.
- **¿El gráfico del video es el espectro de amplitud?** [1:14:05]–[1:15:09]: no, es el gráfico de $C_n$ en función de $n\omega$ (en el video, $C_k$ en función de $k$). Las amplitudes son **módulos, siempre positivas**, y ese gráfico cruza el eje. El profe prefiere poner $n\omega$ en el eje porque deja ver que, cuanto más chico $\omega$, menor la separación entre componentes.

## Transformadas integrales y antitransformadas — [1:15:09]

- La transformada de Fourier "es un universo en sí", pero la cátedra la usa como introducción a la **transformada de Laplace**, que se ve las clases siguientes [1:15:09]–[1:15:39]. "Todo esto (…) no es lo más importante que se lleven de hoy" [1:15:39].
- **Transformada integral** [1:16:11]: un operador $T$ que a una $f(t)$ le hace una integral con un núcleo $K(u, t)$ y devuelve una función de otra variable $u$:

$$
T\{f(t)\} = \int_{t_1}^{t_2} K(u, t)\, f(t)\, dt = F(u)
$$

- Los límites de integración dependen de la transformada (no son los mismos en Fourier que en Laplace) [1:16:44].
- **Antitransformada** $T^{-1}$ [1:16:44]–[1:17:48]: a $F(u)$ le aplicás otra integral y te devuelve $f(t)$. Son procesos inversos. Notación: $\mathcal{L}$ y $\mathcal{L}^{-1}$ para Laplace, $\mathcal{F}$ y $\mathcal{F}^{-1}$ para Fourier. [la integral de la antitransformada genérica, paso en el pizarrón, ver video]

## Condiciones para aplicar la transformada de Fourier — [1:18:22]

Dos condiciones [1:18:22]–[1:19:24]:

1. **Seccionalmente continua**: una cantidad **finita** de saltos **finitos** (no asíntotas verticales). Toda función continua también lo es.
2. **Integrable en todo el eje real**: su integral entre $-\infty$ e $\infty$ da un valor real, no se va a infinito.

## Definición de la transformada de Fourier y su antitransformada — [1:19:24]

Dada $f(t)$ seccionalmente continua e integrable en todo el eje real [1:19:24]–[1:20:27] (también en el [ayudamemoria]):

$$
\mathcal{F}\{f(t)\} = F(\omega) = \int_{-\infty}^{\infty} f(t)\, e^{-j\omega t}\, dt
$$

**Antitransformada** (dada, sin deducción) [1:20:27]–[1:20:58]:

$$
\mathcal{F}^{-1}\{F(\omega)\} = f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega)\, e^{j\omega t}\, d\omega
$$

- "Así también, con una mínima diferencia, trabaja la transformada de Laplace" [1:20:27].
- **Dominio del tiempo → dominio de la frecuencia** [1:21:28]–[1:22:31]: se habla de $f(t)$ porque Fourier se usa en análisis de señales, que vienen en función del tiempo. Serie o transformada "hacen lo mismo, pero se aplican a distintos tipos de funciones": descomponen la señal en sus frecuencias.
- $\omega$ es una **frecuencia angular, real**; pero la **imagen** de $F(\omega)$ es compleja: $F$ va de los reales en los complejos [1:22:31]–[1:23:02].

<details>
<summary>📝 Ejercicio 4 — 1:23:02: transformada de Fourier del pulso |t| < a</summary>

Hallar la transformada de Fourier del pulso (no periódico, un solo pulso):

$$
f(t) =
\begin{cases}
1 & |t| < a \\
0 & |t| > a
\end{cases}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** fuera de $(-a, a)$ la función es nula, así que los límites de integración quedan $-a$ y $a$ [1:23:33]–[1:24:04]:

$$
F(\omega) = \int_{-a}^{a} 1 \cdot e^{-j\omega t}\, dt
$$

**Paso 2:** la exponencial se divide por $-j\omega$; con "un par de movimientos" se llega a la resta de exponenciales y se usa el $2j$ del denominador para formar el seno [1:24:04]–[1:24:35]:

$$
F(\omega) = \left[ \frac{e^{-j\omega t}}{-j\omega} \right]_{-a}^{a} = \frac{e^{j\omega a} - e^{-j\omega a}}{j\omega} = \frac{2 \operatorname{sen}(\omega a)}{\omega}
\qquad (\omega \neq 0)
$$

La aclaración $\omega \neq 0$ es solo para no dividir por cero [1:25:37].

**Paso 3 (relación con el tren de pulsos):** es otra vez un "seno de algo sobre algo", igual que en el Ejercicio 3 [1:24:35]–[1:25:06]: como se trabaja con casos límite, la transformada y la serie se terminan relacionando. Escrito como $\frac{\operatorname{sen}(ax)}{ax}$ con $\omega$ como si fuera la $x$ [1:26:08]:

$$
F(\omega) = 2a\, \frac{\operatorname{sen}(a\omega)}{a\omega}
$$

**Paso 4 (conclusión):** $\omega$ es una variable real y continua, así que el espectro de frecuencias es una **función continua** [1:26:08]–[1:26:42]: función no periódica → espectro continuo. [gráfico en el pizarrón, ver video]

</details>

</details>

<details>
<summary>📝 Ejercicio 5 — 1:26:42: transformada de Fourier de e^(−ct) para t > 0</summary>

Hallar la transformada de Fourier de

$$
f(t) =
\begin{cases}
e^{-ct} & t > 0 \\
0 & t < 0
\end{cases}
\qquad c > 0
$$

Es "muy importante" que la exponencial sea negativa: si creciera no sería integrable y no se le podría aplicar la transformada [1:27:19].

<details>
<summary>Ver resolución</summary>

**Paso 1:** se integra entre $0$ e $\infty$ (la otra mitad se anula) y se juntan los exponentes [1:27:50]:

$$
F(\omega) = \int_{0}^{\infty} e^{-ct}\, e^{-j\omega t}\, dt = \int_{0}^{\infty} e^{-(c + j\omega)t}\, dt
$$

**Paso 2:** se divide por lo que acompaña a la $t$ y se evalúa entre $0$ e $\infty$. Como es impropia, en el infinito va un **límite**: la exponencial negativa tiende a $0$. En $0$ queda $e^0 = 1$, restado por la regla de Barrow [1:28:23]–[1:28:54]:

$$
F(\omega) = \left[ \frac{e^{-(c + j\omega)t}}{-(c + j\omega)} \right]_{0}^{\infty} = 0 - \frac{1}{-(c + j\omega)} = \frac{1}{c + j\omega}
$$

**Paso 3 (conclusión):** $F(\omega)$ tiene una $j$ en el denominador: es claramente una **función compleja** (de los reales en los complejos) [1:28:54]–[1:29:55].

**Paso 4 (espectro):** con $c = 1$ se grafica el **módulo** $|F(\omega)|$ (el $\rho$ del número complejo $\frac{1}{c + j\omega}$) en función de $\omega$ [1:30:26]–[1:31:01]. [gráfico en el pizarrón, ver video]

</details>

</details>

## La transformada de Fourier no se toma — [1:31:31]

"Lo que es importante para ustedes: **transformada de Fourier no se toma**. Vamos a trabajar siempre con transformada de Laplace. Se usa como puente entre un tema y el otro" [1:31:31]. Es muy útil en la vida real, pero "no se va a tomar en un examen". Laplace es el tema central de la primera parte de la materia, hasta el primer parcial [1:32:04].

<details>
<summary>📝 Ejercicio 6 — 1:32:04: de la transformada de Fourier a la de Laplace</summary>

(Ejemplo 3 del PDF, "el puente entre transformada de Fourier y transformada de Laplace".) Sea

$$
f_1(t) = e^{-ct} f(t) \qquad t > 0,\ c > 0 \text{ real}
$$

Aplicarle la transformada de Fourier.

<details>
<summary>Ver resolución</summary>

**Paso 1:** se mete $f_1$ en la definición, junto con el $e^{-j\omega t}$ [1:32:36]:

$$
\mathcal{F}\{f_1(t)\} = \int_{0}^{\infty} e^{-ct} f(t)\, e^{-j\omega t}\, dt = \int_{0}^{\infty} f(t)\, e^{-(c + j\omega)t}\, dt
$$

**Paso 2 (cambio de variable):** se llama $s = c + j\omega$ [1:33:08]:

$$
F(s) = \int_{0}^{\infty} f(t)\, e^{-st}\, dt
$$

Es la **definición de la transformada de Laplace** de $f$: ya no está en función de $\omega$ sino de $s$ [1:33:08]–[1:33:40].

**Paso 3:** $s = c + j\omega$ (real más $j$ por otro real) es un complejo en forma binómica: $s$ es una **variable compleja**, y $F(s)$ también es una función compleja ("entra la variable compleja y sale también la imagen compleja") [1:33:40]–[1:34:11].

</details>

</details>

## Tablas de transformadas — [1:35:13]

- En Laplace no siempre se van a hacer las integrales: va a haber una **tabla** con las transformadas de funciones comunes (constantes, lineales, cuadráticas, seno, coseno…) [1:35:13]–[1:35:44].
- Para Fourier también existe tabla, pero "nosotros ni la llegamos a ver, porque no nos hace falta" [1:35:44].

## Cierre de series trigonométricas: par, impar y media onda son condicionales de ida — [1:35:44]

Las tres conclusiones [1:36:15]:

- $f$ **par** $\Rightarrow$ $b_n = 0$.
- $f$ **impar** $\Rightarrow$ $a_0 = 0$ y $a_n = 0$.
- $f$ con **simetría de media onda** $\Rightarrow$ solo armónicas impares.

Son **condicionales que van solo para un lado** [1:36:46]: "hay funciones donde el $b_n$ es cero, pero no es par, o sea, no se cumple el recíproco" [1:37:24]. Lo mismo con los otros: que se anule un coeficiente no implica que la función sea par, impar o con media onda. Se tomó en el último final y "nadie lo hizo bien".

## Consulta final: serie (aproximar) vs. transformada (cambiar de dominio) — [1:38:26]

- Pregunta: ¿la serie aproxima una función periódica con armónicos y la transformada aproxima una aperiódica? [1:38:26]
- Respuesta [1:38:56]–[1:39:27]: la transformada de Fourier **no** se usa para aproximar; su utilidad es reescribir una señal en función del tiempo para pasarla al **dominio de la frecuencia**. Las series sí se pueden usar para ir aproximando la función original a medida que se suman armónicas.

---

*Generado el 2026-10-02 a partir de `fuentes/clases/series de fourier/T_serie_exponencial_y_transf_fourier.mp4` (transcripción local con Whisper, `apuntes/transcripts/17-video-teorica-serie-exponencial-fourier.json`, 101 min). Las fórmulas se reconstruyeron de lo dictado; las de STF, simetría de media onda, SEF con $C_{-n}$ y transformada de Fourier se contrastaron con `fuentes/AYUDAMEMORIA-OFICIAL.pdf` (pág. 1). Los gráficos (OneNote, GeoGebra, video externo) quedaron en pantalla y no se transcriben.*
