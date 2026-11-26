# Repaso primer parcial (clase grabada)

> Fuente: fuentes/clases/repaso primer parcial/Repaso Primer Parcial.mp4 (transcripción local con Whisper) + OneNote de la clase

---

## Índice

- [00:00] — Lo que el profe dice del parcial (resumen de todos los comentarios sobre el examen)
- [00:00] — Consultas de arranque: impar desplazada, qué se puede llevar, espectro con módulo
- [05:18] — Números complejos: ecuación cuadrática con coeficientes complejos
- [05:18] — 📝 Ejercicio 1: raíces de $z^2 + 2z + 3 + j(2z+6) = 0$ (multiple choice)
- [15:24] — Raíces enésimas en forma polar y el chequeo del cuadrante del argumento
- [15:24] — 📝 Ejercicio 2: raíces cuartas de $j$ (producto y suma)
- [26:59] — Series de Fourier: graficar, $T$/$L$/$\omega_0$, paridad y el puente $C_n = \frac{1}{2}(a_n - b_n j)$
- [26:59] — 📝 Ejercicio 3: completar para que haya solo cosenos + serie exponencial
- [42:07] — Impar desplazada, integrar un período completo y sumar series con la serie hallada
- [42:07] — 📝 Ejercicio 4: completar como impar desplazada con valor medio 1 + calcular $\sum \frac{(-1)^k}{2k+1}$
- [1:01:31] — Transformada de Laplace: miembro a miembro, fracciones simples, transformadas por definición
- [1:02:01] — 📝 Ejercicio 5: EDO $y' - y = 2t - t^2$ por Laplace
- [1:11:26] — 📝 Ejercicio 6: $\int_0^\infty t\,\mathrm{sen}(at)\,e^{-2t}\,dt$ (multiplicación por $t$)
- [1:16:40] — 📝 Ejercicio 7: $\int_0^\infty \frac{e^{-3t} - e^{-6t}}{t}\,dt$ (división por $t$, pedido por un alumno)
- [1:21:00] — Sistemas estables: estabilidad por polos, cancelar el polo inestable, corte por el eje real
- [1:21:00] — 📝 Ejercicio 8: hallar $K$ para que sea estable, corte por el eje real y respuesta al impulso
- [1:37:45] — Sistemas desde el gráfico del corte: leer polos y ceros, constelación y método vectorial
- [1:37:45] — 📝 Ejercicio 9: $G(s)$ desde el corte por el eje real con $|G(1+j)| = 2$ + respuesta a $x(t)$
- [1:47:54] — Preguntas de sistemas: tipo de respuesta, valor estable, módulo analítico vs. gráfico, la constante $K$
- [1:52:37] — Transformada Z: ecuaciones en diferencias, "dejar una $z$ afuera", región de convergencia
- [1:52:37] — 📝 Ejercicio 10: $x(n+1) = 3x(n) + 2$, $x(0) = 2$ + verificación con $x(2)$
- [1:58:58] — 📝 Ejercicio 11: región de convergencia de una sucesión definida por múltiplos de 3
- [2:07:17] — Complejos (si sobra tiempo): potencia enésima y raíces cuartas en forma binómica
- [2:07:49] — 📝 Ejercicio 12: hallar $n$ tal que $(1-2j)^n = 117 - 44j$
- [2:12:59] — 📝 Ejercicio 13: $z^4 + 16 = 0$ con $|z + 1 - j| \le 1$
- [2:18:46] — Cierre: consultas por foro/mail y preguntas finales

---

## Lo que el profe dice del parcial

Todo comentario sobre el examen que aparece en la clase, en orden cronológico.

**Qué se puede llevar y formato**

- [02:40] — Se puede llevar **la hoja de ayuda para el primer parcial** (la que tiene las tablas y propiedades de Laplace y Z) **sola**: no se pueden llevar apuntes propios aparte. Comenta que la hoja "tiene demasiadas cosas" y que para el cuatrimestre que viene la va a cortar a la mitad.
- [03:11] — Además se puede llevar **tabla de integrales** (integrales, derivadas e identidades trigonométricas; la tabla de la guía ya incluye algunas identidades). "Con esto ya deberían andar".
- [1:06:12] — **Todos los profesores toman lo mismo**: "los mismos ejercicios y los mismos tipos de ejercicios". "Hay muchos ejercicios, honestamente, se reciclan, se les cambian dos numeritos". [1:06:42] Cualquier parcial o final de cualquier profesor (Piñeiro, Santi, etc.) lo tendrían que poder resolver con cualquier cursada.

**Cómo corrige / cuánto justificar**

- [1:33:03] — **No hace falta justificar con palabras** lo que es directo (por ejemplo, el corte por el eje real): "con el gráfico alcanza". [1:33:34] Si tienen alguna duda o el resultado "se puede interpretar de una manera o de otra", **escriban y justifiquen, "eso siempre se valora"**. "Si son cosas directas, se resuelven y chau."
- [11:39] — En un multiple choice dudoso ($z_2 = -3j$ "¿pertenece al tercer cuadrante?") él diría falso porque está sobre el eje, pero "si me lo justifican bien tampoco va a estar mal… siempre y cuando lo ubiquen bien en el planito".
- [14:19]–[14:50] — **Cálculos auxiliares con calculadora**: las raíces de una cuadrática con coeficientes reales que aparece en el medio de fracciones simples, sistemas estables, Laplace, etc. las pueden sacar con la calculadora ("estos cálculos simples no me interesan"). **Pero en los ejercicios de complejos** (cuadrática con coeficientes complejos, raíz cuadrada de un complejo con las fórmulas) **"eso sí necesito que lo hagan a mano"**.
- [54:34] — $\cos(n\pi) = (-1)^n$ **no hace falta justificarlo con la tablita**: "ponemos menos 1 a la n y listo".
- [33:13] — Sacar $a_0/2$ **por gráfico es válido** ("pueden poner por gráfico"), y la integral sirve para chequear.
- [29:04]–[29:35] — Completar la función para forzar paridad: hallarla gráfica o analíticamente "te tiene que dar lo mismo".

**Errores y detalles de presentación que marca**

- [17:02]–[18:04] — **Argumento de un complejo: chequeen siempre el cuadrante** contra los signos de parte real e imaginaria (la calculadora devuelve primer y cuarto cuadrante). En el 2.º y 3.er cuadrante, no sumar $\pi$ **es error**; en el 4.º, dejarlo negativo **no es error** pero es preferible sumar $2\pi$ y dejarlo en el primer giro positivo.
- [38:25] — Si solo sobreviven armónicas impares, expresar la serie con $2k+1$ (o $2k-1$): dejarla en función de $n$ "no es un error", pero "no está pipicucú el ejercicio".
- [41:35] — En la serie exponencial sin distinción par/impar, lo correcto es aclarar $n \neq 0$ debajo de la sumatoria porque $C_0$ ya está afuera ("es un detalle", "hilar muy fino").
- [59:27] — Al reescribir $\mathrm{sen}(n\pi/2)$ como $(-1)^k$: cuidar que **la primera armónica quede positiva** (si usan $2k-1$ y arrancan en $k=1$, ajustar con $k+1$ o $k-1$) — "hilando muy fino".
- [1:25:44] — En el corte por el eje real, poner el **cero en el infinito** "está copado si lo ponen, pero si se lo olvidan no es un error muy grave"; el cero finito "sí es más importante".
- [1:31:30] — En el corte por el eje imaginario, si dibujan las dos montañitas de los polos complejos "no estaría mal"; lo importante ahí es marcar el polo en el cero. [1:30:58] El corte por $\mathrm{Re}(s) = -2$ "nunca se lo van a pedir".
- [1:51:29]–[1:52:01] — **No olvidarse la constante $K$** al calcular módulos (multiplica el módulo); en cambio no afecta a los argumentos.
- [1:54:45] — **"Por favor, por favor, encarecidamente": en fracciones simples de transformada Z hay que dejar una $z$ afuera** (en el OneNote: "DEJAR UNA Z AFUERA!!!!!!" [OneNote p. 12]).
- [2:05:41] — En la región de convergencia, las circunferencias con desigualdad estricta se dibujan **punteadas**.
- [2:07:17] — El resultado de la transformada Z "expresado así [sin simplificar] está bien… no está mal", pero si pueden, trabajen un poco más la forma y simplifiquen.
- [1:13:30]/[1:16:06] — Multiplicación por $t^n$ en Laplace: derivar $n$ veces y cambiar el signo $n$ veces; cambiar de signo al final o en cada paso da lo mismo.

**Qué temas pueden caer**

- [04:48] — La clase trae "en general dos [ejercicios] por cada tema" (más un par extra de complejos al final).
- [1:02:01] — **Simetría de media onda en Fourier:** "puede pasar, está dentro de las posibilidades".
- [1:02:32] — La EDO por Laplace es un "ejercicio típico de Laplace". Una parte tachada del enunciado original es de la segunda parte de la materia ("un tema que todavía no vimos", no entra).
- [1:04:04]–[1:04:36] — **Fracciones simples: "sí o sí va a haber alguna"** en alguno de los ejercicios (Laplace, sistemas estables "siempre aparece", o transformada Z). Sepan resolver raíces reales simples y múltiples y raíces complejas.
- [1:04:36]/[1:07:16] — **Raíces complejas múltiples: "eso no lo voy a tomar"**. **Complejas conjugadas simples "pueden entrar tranquilamente"**.
- [1:10:54] — Ecuaciones íntegro-diferenciales y ecuaciones integrales (convolución): "no deberían tener inconveniente tampoco".
- [1:14:33] — Transformada por definición con **división por $t$**: "otra también que puede tocar, que es un ejercicio bastante típico, clásico, así que ténganlo en cuenta".
- [1:24:42] — Elegir $K$ para cancelar el polo inestable: "una idea básica, pero que aparece en un montón de ejercicios de sistemas estables".
- [1:37:45] — Completar cuadrados y armar $s+2$ en el numerador para antitransformar con senos/cosenos: "esto también puede aparecer".
- [1:47:54]–[1:48:24] — Si piden el **tipo de respuesta**, lo importante es decir **oscilatoria amortiguada** (seno/coseno por exponencial negativa); el **valor estable** sale con el límite.
- [2:19:50] — Un alumno comenta que en un parcial vino un ejercicio de **conjuntos de complejos** (hallar elementos y la intersección de conjuntos), raro y no visto en la guía; el profe le pide que se lo mande por mail.

**Otros avisos de la clase (no son del examen)**

- [01:36]–[02:09] — Una respuesta de la guía de transformada Z estaba mal (lo verificaron dos alumnos); el profe lo va a hablar con la jefa de cátedra para corregirla. [poco claro en la transcripción cuál era el ejercicio]
- [1:58:26] — Sube el OneNote actualizado y la grabación al aula.
- [2:18:46]–[2:20:21] — Consultas por el foro del aula, por mensaje privado del campus o por mail: si no responde en unas 6 horas, mandar mail.

---

## Consultas de arranque — [00:00]

- **Impar desplazada ($f(t) = g(t) + k$, con $g$ impar):** $a_n = 0$ y el $b_n$ se puede calcular con $f$ o con $g$, "te van a dar igual": la constante $k$, integrada contra el seno en un período, se compensa y se anula [00:30]. Se repite en [54:02]: el $b_n$ de la impar sin desplazar y el de la desplazada coinciden.
- **Qué llevar al parcial** [02:40]–[03:11]: ver la sección anterior.
- **Espectro de frecuencias** [03:45]–[04:16]: en general se grafica con **módulo** de $C_n$; "si no te dice nada, hacelo con módulo, que está bien".

---

## Números complejos: ecuación cuadrática con coeficientes complejos — [05:18]

- Las cuadráticas con coeficientes complejos se resuelven **con la misma resolvente de siempre**. Primero hay que distribuir y acomodar para identificar bien $a$ (lo que acompaña a $z^2$), $b$ (lo que acompaña a $z$, incluida la parte con $j$) y $c$ (términos independientes) [06:50].
- Lo nuevo aparece **adentro de la raíz** [07:27]: el cuadrado de un binomio complejo tiene el tercer término **negativo** porque $(2j)^2 = -4$ — "no entren como caballos porque toda la vida el tercer término fue positivo".
- La raíz cuadrada de $a + bj$ se saca en forma binómica con las fórmulas de la hoja [07:58]: con $\rho = |a + bj|$,

$$
x = \sqrt{\frac{\rho + a}{2}}, \qquad y = \sqrt{\frac{\rho - a}{2}}
$$

- **El signo de la parte imaginaria $b$ define los signos** [09:00]: si $b > 0$, signos iguales ($+,+$ y $-,-$); si $b < 0$, signos alternados ($+,-$ y $-,+$).
- También se puede hacer en polar, pero hay que pasar a polar y volver a binómica "medio inútilmente" [06:20].
- **Identificar bien cuál es $z_1$ y cuál $z_2$** según el módulo es "súper importante", porque después las opciones preguntan por cada una [10:36].
- **Conjugado** [12:10]: misma parte real, parte imaginaria con signo cambiado; gráficamente se espejan respecto del eje real y quedan sobre la misma vertical.

<details>
<summary>📝 Ejercicio 1 — [05:18]: raíces de una cuadrática con coeficientes complejos (multiple choice)</summary>

Sea $z_1$ la raíz de menor módulo de la ecuación $z^2 + 2z + 3 + j(2z + 6) = 0$ y $z_2$ la de mayor módulo [OneNote p. 1]:

a) $z_1$ es imaginaria pura · b) $z_2 \in$ III cuadrante · c) $\bar{z}_1 = z_2$ · d) $z_2^2$ es real · e) ninguna es correcta.

<details>
<summary>Ver resolución</summary>

**Paso 1:** distribuir y acomodar para identificar $a$, $b$, $c$ [OneNote p. 1].

$$
z^2 + (2 + 2j)\,z + 3 + 6j = 0 \quad\Rightarrow\quad a = 1,\; b = 2 + 2j,\; c = 3 + 6j
$$

**Paso 2:** resolvente. Ojo con el cuadrado del binomio: $(2+2j)^2 = 4 + 8j - 4$.

$$
z_{1,2} = \frac{-2 - 2j \pm \sqrt{(2+2j)^2 - 4\cdot 1\cdot(3+6j)}}{2} = \frac{-2 - 2j \pm \sqrt{-12 - 16j}}{2}
$$

**Paso 3:** raíz cuadrada de $-12 - 16j$ con las fórmulas. El módulo es $\sqrt{12^2 + 16^2} = \sqrt{400} = 20$ y la parte real es $-12$:

$$
x = \sqrt{\frac{20 + (-12)}{2}} = 2, \qquad y = \sqrt{\frac{20 - (-12)}{2}} = 4
$$

Como $b = -16 < 0$, los signos van alternados: las raíces son $2 - 4j$ y $-2 + 4j$.

**Paso 4:** las dos soluciones y sus módulos [OneNote p. 2].

$$
z = \frac{-2 - 2j + 2 - 4j}{2} = -3j \quad (|z| = 3) \;\Rightarrow\; z_2
$$

$$
z = \frac{-2 - 2j - 2 + 4j}{2} = -2 + j \quad (|z| = \sqrt{5}) \;\Rightarrow\; z_1
$$

Como $\sqrt{5} < 3$, la de menor módulo ($z_1$) es $-2 + j$.

**Paso 5:** opciones [11:07]–[13:16].

- a) **Falso**: la imaginaria pura es $z_2 = -3j$, no $z_1$.
- b) **Falso**: $z_2 = -3j$ está sobre el eje imaginario, no "en el área" del tercer cuadrante (si se justifica bien la otra lectura, no lo considera mal).
- c) **Falso**: $\bar{z}_1 = -2 - j \neq -3j$.
- d) **Verdadero**: $z_2^2 = (-3j)^2 = -9$, real.
- e) **Falso**, porque d) es correcta.

</details>

</details>

---

## Raíces enésimas en forma polar y el chequeo del cuadrante del argumento — [15:24]

- Primero se pasa el número a **forma polar** $[\rho, \varphi]$ (módulo, argumento). Para $j$: está sobre el eje imaginario a una unidad del origen, así que $j = [1, \pi/2]$ [15:57].
- **Pregunta de un alumno: ¿cuándo hay que sumarle giros al ángulo?** [17:02] "El chequeo lo tienen que hacer siempre": mirar los signos de la parte real e imaginaria. La calculadora siempre devuelve un ángulo en el primer o cuarto cuadrante, entonces:
  - 1.er cuadrante: está todo bien.
  - 2.º cuadrante (real negativa, imaginaria positiva): la calculadora devuelve uno en el 4.º → **sumar $\pi$**.
  - 3.er cuadrante: la calculadora lo da en el 1.º → **sumar $\pi$**.
  - 4.º cuadrante: es preferible sumar $2\pi$ para dejarlo en el primer giro positivo (no sumarlo no es error; los otros casos sí).
  - Más que la regla, "lo que me interesa es que entiendan de dónde sale": si el número está en un cuadrante y el resultado da en otro, "ahí no está mi número complejo" [18:04].
- **Fórmula de las raíces enésimas** [18:34] [OneNote p. 2]: con $n$ el índice y $k$ variando para que las raíces no se repitan cíclicamente,

$$
w_k = \left[\sqrt[n]{\rho}\,,\; \frac{\varphi + 2k\pi}{n}\right], \qquad k = 0, \dots, n-1
$$

- Todas las raíces comparten el módulo y los argumentos van sumando $2\pi/n$ (para raíces cuartas, un cuarto de giro = $\pi/2$) [19:36].
- **Imaginario puro / real** [20:37]–[21:42]: un número es real si está sobre el eje $x$ (argumento $0$, $\pi$ o congruentes) e imaginario puro si está sobre el eje $y$ (argumento $\pi/2$, $3\pi/2$ o congruentes).
- **Producto en polar/exponencial** [21:42]: los módulos se multiplican y los argumentos (o exponentes) se suman. **Suma**: en polar no se puede; hay que pasar a binómica pasando por la trigonométrica $r(\cos\varphi + j\,\mathrm{sen}\,\varphi)$ [23:45]–[24:22].

<details>
<summary>📝 Ejercicio 2 — [15:24]: raíces cuartas de la unidad imaginaria</summary>

Sean $w_0, w_1, w_2, w_3$ las raíces cuartas de la unidad imaginaria $z = j$. Se puede asegurar que [OneNote p. 2]:

a) sólo una de ellas es imaginaria pura · b) sólo una de ellas es real · c) $w_0 \cdot w_1 \cdot w_2 \cdot w_3 = -j$ · d) $w_0 + w_1 + w_2 + w_3 = 1$ · e) n.a.

<details>
<summary>Ver resolución</summary>

**Paso 1:** como todas las opciones dependen de las $w$, se calculan primero. $j = [1, \pi/2]$ y con la fórmula de raíces enésimas ($n = 4$) [OneNote p. 2]:

$$
w_k = \left[\sqrt[4]{1}\,,\; \frac{\pi/2 + 2k\pi}{4}\right], \qquad k = 0, \dots, 3
$$

$$
w_0 = [1, \pi/8], \quad w_1 = [1, 5\pi/8], \quad w_2 = [1, 9\pi/8], \quad w_3 = [1, 13\pi/8]
$$

**Paso 2:** a) y b). Ninguno de esos argumentos (octavos que no se simplifican) cae sobre los ejes, así que ninguna raíz es imaginaria pura ni real: a) **falso**, b) **falso** [20:37].

**Paso 3:** c) producto. Se suman los exponentes y los módulos (todos 1) se multiplican [OneNote p. 3]:

$$
w_0 w_1 w_2 w_3 = e^{j\pi/8}\, e^{j5\pi/8}\, e^{j9\pi/8}\, e^{j13\pi/8} = e^{j\,28\pi/8} = 1\, e^{j\,7\pi/2}
$$

$7\pi/2$ es un múltiplo impar de $\pi/2$, así que apunta arriba o abajo; restando $2\pi$ queda $3\pi/2$, que apunta hacia abajo: es $-j$. c) **verdadero** [23:15]. (Un alumno pregunta cómo reconocerlo [25:23]: se puede contar de a $\pi/2$ — "acá tenés 1, acá 2, … acá 7" — o restar giros de $2\pi$ hasta caer en el primer giro.)

**Paso 4:** d) suma. Hay que pasar a binómica vía la trigonométrica (con módulo 1 no hace falta escribir el $r$; si el módulo fuera 2, sí) [24:22]:

$$
\sum_{k=0}^{3} w_k = \cos\tfrac{\pi}{8} + j\,\mathrm{sen}\tfrac{\pi}{8} + \cos\tfrac{5\pi}{8} + j\,\mathrm{sen}\tfrac{5\pi}{8} + \cos\tfrac{9\pi}{8} + j\,\mathrm{sen}\tfrac{9\pi}{8} + \cos\tfrac{13\pi}{8} + j\,\mathrm{sen}\tfrac{13\pi}{8} = 0
$$

"Se simplifica todo" y da 0, no 1: d) **falso**; e) **falso** porque c) es correcta [OneNote p. 3].

</details>

</details>

---

## Series de Fourier: graficar, $T$/$L$/$\omega_0$, paridad y el puente con la exponencial — [26:59]

- **Dos pasos fundamentales siempre** [27:30]: **graficar** y **anotar los tres datos** $T$ (período), $L$ (semiperíodo) y $\omega_0 = \pi/L$ (frecuencia fundamental).
- **La parte conceptual** que se juega "en todos los ejercicios de Fourier o en la gran mayoría" [28:01]–[28:32] [OneNote p. 3]:
  - **solo cosenos** (STF) $\Leftrightarrow$ **función par** $\Leftrightarrow$ **coeficientes $C_n$ reales** (SEF);
  - **solo senos** (STF) $\Leftrightarrow$ **función impar** $\Leftrightarrow$ **coeficientes $C_n$ imaginarios puros** (SEF).
- **Para la serie exponencial conviene calcular $a_n$ y $b_n$** de la trigonométrica y pasar con el puente [30:06]–[30:38]: se aprovecha mejor la paridad y son integrales a las que estamos más acostumbrados (las que tienen la $j$ adentro pueden ser más difíciles). Igual, encararlo por la integral de $C_n$ también es válido.

$$
C_n = \frac{1}{2}\left(a_n - b_n\, j\right)
$$

- **Pregunta: ¿por qué $1/L$ en una y $1/(2L)$ en la otra?** [31:38]–[32:42] Es una convención: $a_0$ se calcula con $1/L$ (igual que $a_n$ y $b_n$) y después se divide por 2; $C_0$ se calcula con $1/(2L)$ (igual que la integral de $C_n$). "Es lo mismo": si querés poner el 2 directo en vez de dividir después, da igual.
- **Valor medio por gráfico** [33:13]–[34:15]: es válido. En funciones constantes o lineales que abarcan todo el período, el valor medio es el promedio entre arriba y abajo. La integral sirve para chequear.
- **Paridad en intervalos simétricos** [34:15]: en $[-L, L]$, si la función es par se puede tomar una sola rama y multiplicar por 2 ($\frac{2}{L}\int_0^L$).
- **Integrales típicas** [35:18]–[35:50]: siempre son $t\cos$ o $t\,\mathrm{sen}$, están en la tabla de integrales. Al aplicar Barrow, el término $t\,\mathrm{sen}(n\pi\ldots)$ suele anularse dos veces: en el extremo superior por $\mathrm{sen}(n\pi) = 0$ y en el 0 porque además está multiplicado por $t$. Hay que prestarle atención al término del coseno: $\cos(n\pi) = (-1)^n$.
- **Armónicas impares** [37:54]–[38:25]: cuando el coeficiente se anula para $n$ par, expresar la serie con $2k+1$ (o $2k-1$) en vez de $n$.
- **Dos formatos de la SEF** [38:58]–[40:32]: con $k$ de $-\infty$ a $\infty$ (el que él prefiere, "más cómodo") o de $0$ (o $1$) a $\infty$ con las dos exponenciales $e^{+j\ldots}$ y $e^{-j\ldots}$. Los dos son válidos. Sacar la constante afuera de la sumatoria es gusto personal.
- **Pregunta sobre $C_0$ en la fórmula** [41:05]–[41:35]: si no hay distinción de armónicas pares/impares, lo correcto es poner $n \neq 0$ bajo la sumatoria, porque $C_0$ ya está afuera y si no "lo está sumando dos veces".

<details>
<summary>📝 Ejercicio 3 — [26:59]: completar para que la STF tenga solo cosenos + serie exponencial</summary>

Dada la función [OneNote p. 3]

$$
f(t) = \begin{cases} 2t & 0 < t < 2 \\ k(t) & -2 < t < 0 \end{cases}, \qquad f(t) = f(t+4)
$$

a) Halle la función $k(t)$ para que la Serie Trigonométrica de Fourier tenga (solo) términos con cosenos. b) Desarrolle $f(t)$ en Serie Exponencial de Fourier.

<details>
<summary>Ver resolución</summary>

**Paso 1:** graficar la rama dada ($2t$ entre 0 y 2, llega a 4) [27:30].

**Paso 2:** interpretar. Solo cosenos = función par = coeficientes reales de la SEF, así que hay que completar **en espejo** respecto del eje vertical, "para hacer una V corta" [29:04] [OneNote p. 3]:

$$
k(t) = -2t \quad (-2 < t < 0)
$$

Un alumno pregunta si alcanza con decir que es par o hay que hacerlo analítico: "si lo querés hallar gráficamente o analíticamente te tiene que dar lo mismo" [29:35].

**Paso 3:** datos [29:35] [OneNote p. 3–4].

$$
T = 4, \qquad L = 2, \qquad \omega_0 = \frac{\pi}{L} = \frac{\pi}{2}
$$

**Paso 4:** como es par, $b_n = 0$ y el puente queda $C_n = \frac{1}{2} a_n$ [31:08]. Valor medio aprovechando la paridad (por gráfico: el promedio entre 0 y 4 es 2) [34:15] [OneNote p. 4]:

$$
a_0 = \frac{2}{L}\int_0^L f(t)\,dt = \frac{2}{2}\int_0^2 2t\,dt = 4 \quad\Rightarrow\quad \frac{a_0}{2} = C_0 = 2
$$

**Paso 5:** $a_n$ con la integral de tabla de $t\cos$ [35:18] [OneNote p. 4]:

$$
a_n = \frac{2}{2}\int_0^2 2t\cos\!\left(\frac{n\pi}{2}t\right)dt = 2\left[\frac{\cos\!\left(\frac{n\pi}{2}t\right)}{\left(\frac{n\pi}{2}\right)^2} + \frac{t\,\mathrm{sen}\!\left(\frac{n\pi}{2}t\right)}{\frac{n\pi}{2}}\right]_0^2 = 2\left(\frac{4(-1)^n}{n^2\pi^2} + 0 - \frac{4}{n^2\pi^2} - 0\right)
$$

El término con seno se anula en los dos extremos; solo queda el del coseno [36:20]–[37:22].

**Paso 6:** separar por paridad de $n$ [37:22]–[37:54]: para $n$ par queda "4 sobre algo menos 4 sobre lo mismo" = 0; para $n$ impar, $-8$ por el 2 de afuera:

$$
a_n = \begin{cases} 0 & n \text{ par} \\[4pt] -\dfrac{16}{n^2\pi^2} & n \text{ impar} \end{cases} \qquad\Rightarrow\qquad C_n = \frac{1}{2}a_n = -\frac{8}{n^2\pi^2} \;(n \text{ impar})
$$

**Paso 7:** armar la SEF con $2k+1$ porque solo hay armónicas impares [38:58] [OneNote p. 4]:

$$
S(t) = 2 - \frac{8}{\pi^2}\sum_{k=-\infty}^{+\infty} \frac{1}{(2k+1)^2}\, e^{\,j(2k+1)\frac{\pi}{2}t}
$$

Formato alternativo, de $k = 0$ a $\infty$ (con $2k+1$ la primera armónica es la 1) [40:02]:

$$
S(t) = 2 - \frac{8}{\pi^2}\sum_{k=0}^{\infty} \frac{1}{(2k+1)^2}\left(e^{\,j(2k+1)\frac{\pi}{2}t} + e^{-j(2k+1)\frac{\pi}{2}t}\right)
$$

</details>

</details>

---

## Impar desplazada, período completo y sumas de series — [42:07]

- **Interpretar el enunciado** [43:11]: "sin cosenos" (y sin ser constante) = solo senos = impar. Pero las impares "puras del libro" tienen valor medio cero; si además piden **valor medio 1**, lo que piden es una **impar desplazada** una unidad hacia arriba.
- **Siempre hay que integrar un período completo** [47:24]–[47:54]: entre $0$ y $T$, entre $-L$ y $L$, o cualquier otro (incluso entre $3T$ y $4T$, "sería rarísimo pero el resultado tendría que ser el mismo").
- **El truco del "2 por" solo vale en intervalos simétricos** [47:54]–[48:24]: nace de las propiedades de funciones pares/impares en $[-a, a]$. Si se integra entre $0$ y $T$ (todo de un mismo lado), no aplica.
- **Usar el intervalo donde está definida la función** [49:56]: si la definición está entre $0$ y $T$, conviene integrar ahí. Integrar entre $-L$ y $L$ usando la misma fórmula es un error típico: fuera del intervalo de definición la función es la copia corrida un período (acá $t + 2$, no $t$) [50:28], [53:01]. Un alumno confirma que ese era su error ("siempre me daba mal").
- **Tres caminos para el $b_n$ de este ejercicio** [51:29]–[52:30]: (1) $\frac{1}{L}\int_0^2$ (el elegido); (2) $\frac{2}{L}\int_0^1 t\,\mathrm{sen}(\ldots)$ aprovechando la imparidad, que da lo mismo; (3) $\frac{1}{L}\int_{-1}^{1}$ partiendo la integral en $t$ (de 0 a 1) y $t+2$ (de −1 a 0): "este camino es el peor de todos, lejos". El "2 por" solo sirve por ser impar (o par para $a_n$, $a_0$).
- **Sumar una serie numérica con la serie hallada** [55:37]–[56:40]: la idea es siempre elegir un $t$ conveniente que haga que el seno o el coseno "se vaya" y quede lo que interesa. **Truco de este ejercicio:** el seno no puede valer fijo 1 para todas las armónicas; con $t = 1/2$, $\mathrm{sen}(n\pi/2)$ vale $1, 0, -1, 0, 1, \dots$: se anulan las armónicas pares y en las impares alterna el signo, o sea se convierte en $(-1)^k$ con $n = 2k+1$ [57:46]–[58:17].

<details>
<summary>📝 Ejercicio 4 — [42:07]: impar desplazada con valor medio 1 + suma de una serie numérica</summary>

a) Dada $f(t) = t$ en $(1, 2)$, complete en $(0, 1)$ con $T = 2$ para que la STF no tenga cosenos y su valor medio sea 1. Desarrolle la serie. b) A partir de la serie hallada, calcule el valor de [OneNote p. 4–5]

$$
\sum_{k=0}^{\infty} \frac{(-1)^k}{2k+1}
$$

(Lo trajo un alumno, Alessandro, por mail: "este ejercicio tiene su truquito" en la parte b [42:07].)

<details>
<summary>Ver resolución</summary>

**Paso 1:** sin cosenos y con valor medio 1 ⇒ **impar desplazada una unidad hacia arriba** [43:42] [OneNote p. 5]. Se completa con la continuación natural de la recta identidad entre 0 y 1: quedan "bastoncitos" que, mirados desde un eje en $y = 1$, son impares.

$$
f(t) = t \quad (0 \le t \le 2), \qquad f(t) = f(t+2)
$$

**Paso 2:** datos [44:45] [OneNote p. 5].

$$
T = 2, \qquad L = 1, \qquad \omega_0 = \pi
$$

**Paso 3:** valor medio por gráfico y $a_n$ nulo por enunciado [44:45]:

$$
\frac{a_0}{2} = 1, \qquad a_n = 0
$$

**Paso 4:** $b_n$ integrando todo el período de 0 a 2, con $1/L = 1$ (sin el "2 por", porque no es intervalo simétrico) [45:17] [OneNote p. 5]:

$$
b_n = \frac{1}{1}\int_0^2 t\,\mathrm{sen}(n\pi t)\,dt = \left[\frac{\mathrm{sen}(n\pi t)}{n^2\pi^2} - \frac{t\cos(n\pi t)}{n\pi}\right]_0^2 = -\frac{2}{n\pi}
$$

De los cuatro términos solo sobrevive el del coseno evaluado en 2: $-\frac{2\cos(2n\pi)}{n\pi}$, y **ojo: $\cos(2n\pi) = 1$ siempre, no $(-1)^n$** (eso es $\cos(n\pi)$) [45:49]–[46:21].

**Paso 5:** la serie [46:21] [OneNote p. 5]:

$$
S(t) = 1 - \frac{2}{\pi}\sum_{n=1}^{\infty} \frac{1}{n}\,\mathrm{sen}(n\pi t)
$$

**Paso 6 (parte b):** la serie pedida tiene $(-1)^k$ y $2k+1$, mientras que la hallada está en función de $n$ sin distinguir pares e impares. La primera idea es hacer que el seno valga 1: $\pi/2$ ⇒ $t = 1/2$ [56:40]–[57:14]. Tabla de $\mathrm{sen}(n\pi/2)$ [OneNote p. 5]:

| $n$ | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| $\mathrm{sen}(n\pi/2)$ | 1 | 0 | −1 | 0 | 1 | 0 |

Solo sobreviven las armónicas impares y con signo alternado ⇒ $(-1)^k$ con $n = 2k+1$ (la primera armónica tiene que quedar positiva: con $k = 0$, $(-1)^0 = 1$) [59:27].

**Paso 7:** por gráfico, $f(1/2) = 1/2$ (es la identidad). Igualar a la serie evaluada en $t = 1/2$ [58:49] [OneNote p. 6]:

$$
f\!\left(\tfrac{1}{2}\right) = \frac{1}{2} = 1 - \frac{2}{\pi}\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}
$$

**Paso 8:** despejar (pasar el 1 restando, multiplicar por −1) [59:58]–[1:00:29]:

$$
\frac{2}{\pi}\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1} = \frac{1}{2} \quad\Rightarrow\quad \boxed{\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1} = \frac{\pi}{4}}
$$

</details>

</details>

---

## Transformada de Laplace: miembro a miembro, fracciones simples y transformadas por definición — [1:01:31]

- **EDO:** transformar **miembro a miembro** ("me cansé de repetirlo") usando las condiciones iniciales, agrupar todas las $Y(s)$ de un lado y despejar [1:02:32].
- **¿Pasar dividiendo término a término o juntar todo?** [1:03:34]–[1:05:39] Es "medio de elección". Si un término queda listo para antitransformar (como $1/(s-1) \to e^t$) se puede separar, pero si igual hay que hacer fracciones simples para los otros, conviene juntar todo con denominador común y hacer fracciones simples de una sola vez ("así no tenés que hacer fracciones simples varias veces"). En los ejemplos más simples, separar alcanza y no hace falta fracciones simples.
- **Fracciones simples** [1:04:04]–[1:04:36]: "sí o sí va a haber alguna" en Laplace, sistemas estables o Z. Saber raíces reales simples y múltiples, y complejas conjugadas simples; complejas múltiples no las toma.
- **El "truquito"** [1:07:47]–[1:08:49]: la incógnita de la raíz de mayor multiplicidad y las de raíces simples salen reemplazando $s$ por la raíz que anula su denominador en el resto de la función (tapando ese factor). Las demás salen igualando coeficientes (cúbicos con cúbicos, cuadráticos con cuadráticos, etc.), eligiendo los que despejan fácil. "Sáquense de encima todas las incógnitas que puedan con el truquito", porque el sistema queda mucho más fácil [1:08:49].
- **Íntegro-diferenciales / ecuaciones integrales** [1:10:23]–[1:10:54]: identificar las dos funciones dentro de la integral de convolución; su transformada es el producto de las transformadas.
- **Integral impropia como transformada por definición** [1:11:56]–[1:12:58]:

$$
\mathcal{L}[f(t)] = F(s) = \int_0^{\infty} f(t)\,e^{-st}\,dt
$$

Hay que identificar $f(t)$ = todo lo que no es la exponencial; si en vez de $e^{-st}$ aparece $e^{-2t}$, el resultado es $F(2)$, la transformada **evaluada en 2**, no la genérica en $s$.
- **Multiplicación por $t^n$** [1:12:58]–[1:13:30]: derivar $n$ veces y cambiar el signo $n$ veces (regla mnemotécnica). Cambiar el signo en cada derivada o todo al final da lo mismo: "cambiar de signo un número par de veces es lo mismo que nada" y el menos queda afuera como constante [1:16:06].
- **División por $t$** [1:14:33]–[1:15:35]: también puede tocar ("ejercicio bastante típico, clásico"). **Solo para la división por $t$** hay que verificar que exista el límite de $f(t)/t$ cuando $t \to 0$; para la multiplicación por $t^n$ no hay condiciones de ese tipo.

<details>
<summary>📝 Ejercicio 5 — [1:02:01]: EDO de primer orden por transformada de Laplace</summary>

Dada la siguiente ecuación diferencial: $y' - y = 2t - t^2$ con $y(0) = 1$. a) Resuelva analíticamente por Transformada de Laplace [OneNote p. 6].

(La parte tachada del enunciado original es de la segunda parte de la materia [1:02:32].)

<details>
<summary>Ver resolución</summary>

**Paso 1:** Laplace miembro a miembro [1:02:32] [OneNote p. 6]:

$$
s\,Y(s) - \underbrace{y(0)}_{1} - Y(s) = \frac{2}{s^2} - \frac{2}{s^3}
$$

**Paso 2:** agrupar las $Y(s)$:

$$
Y(s)\,(s - 1) = \frac{2}{s^2} - \frac{2}{s^3} + 1
$$

**Paso 3:** denominador común y recién después pasar dividiendo el $s - 1$ [1:03:34] [OneNote p. 6]:

$$
Y(s) = \frac{s^3 + 2s - 2}{s^3\,(s - 1)}
$$

**Paso 4:** fracciones simples: raíz triple en 0 y simple en 1 [1:07:47].

$$
\frac{s^3 + 2s - 2}{s^3(s-1)} = \frac{A}{s^3} + \frac{B}{s^2} + \frac{C}{s} + \frac{D}{s - 1}
$$

Con el truquito: para $A$, $s = 0$ en el resto: $\frac{-2}{-1} = 2$; para $D$, $s = 1$: $\frac{1}{1} = 1$ [1:08:18]–[1:08:49].

**Paso 5:** $B$ y $C$ igualando coeficientes [1:09:19] [OneNote p. 6]:

$$
2(s-1) + B\,s(s-1) + C\,s^2(s-1) + 1\cdot s^3 = s^3 + 2s - 2
$$

Cúbicos: $C + 1 = 1 \Rightarrow C = 0$. Cuadráticos: $B = 0$.

**Paso 6:** reescribir y antitransformar [1:09:52]–[1:10:23] [OneNote p. 6–7]:

$$
Y(s) = \frac{2}{s^3} + \frac{1}{s - 1} \quad\Rightarrow\quad y(t) = t^2 + e^{t}
$$

El $\frac{1}{s-1}$ es el mismo que salía separando término a término.

</details>

</details>

<details>
<summary>📝 Ejercicio 6 — [1:11:26]: integral impropia por definición (multiplicación por $t$)</summary>

El valor de la siguiente integral es [OneNote p. 7]:

$$
\int_0^{\infty} t\,\mathrm{sen}(at)\,e^{-2t}\,dt
$$

a) $\frac{4}{4+a^2}$ · b) $\frac{-4a}{(4-a^2)^2}$ · c) $\frac{4a}{(4+a^2)^2}$ · d) $\frac{-4}{(a^2+4)^2}$ · e) n.a.

<details>
<summary>Ver resolución</summary>

**Paso 1:** reconocer la definición: $f(t) = t\,\mathrm{sen}(at)$ y en lugar de $e^{-st}$ está $e^{-2t}$, así que es la transformada evaluada en $s = 2$ [1:11:56]–[1:12:58] [OneNote p. 7]:

$$
\int_0^{\infty} t\,\mathrm{sen}(at)\,e^{-2t}\,dt = \mathcal{L}[t\,\mathrm{sen}(at)]\Big|_{s=2}
$$

**Paso 2:** multiplicación por $t^n$ con $n = 1$: derivar una vez [1:13:30] [OneNote p. 7]:

$$
\frac{d}{ds}\left(\frac{a}{s^2 + a^2}\right) = \frac{-2as}{(s^2 + a^2)^2}
$$

**Paso 3:** cambiar el signo una vez:

$$
\mathcal{L}[t\,\mathrm{sen}(at)] = \frac{2as}{(s^2 + a^2)^2}
$$

**Paso 4:** evaluar en $s = 2$ [1:14:00]:

$$
\mathcal{L}[t\,\mathrm{sen}(at)]\Big|_{s=2} = \frac{4a}{(4 + a^2)^2} \quad\Rightarrow\quad \text{opción c)}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 7 — [1:16:40]: integral impropia con división por $t$ (pedido por un alumno)</summary>

Un alumno pide repasar uno de división por $t$ que no termina de entender. Calcular (enunciado dictado oralmente; no está en el OneNote del repaso, el profe lo busca en el de la práctica de Laplace [1:17:45]):

$$
\int_0^{\infty} \frac{e^{-3t} - e^{-6t}}{t}\,dt
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** sacar factor común $e^{-3t}$; lo que queda acompañándolo es la $f(t)$ [1:17:45]–[1:18:17]:

$$
\int_0^{\infty} \frac{1 - e^{-3t}}{t}\,e^{-3t}\,dt = \mathcal{L}\!\left[\frac{1 - e^{-3t}}{t}\right]\Bigg|_{s=3}
$$

**Paso 2:** antes de aplicar la propiedad de división por $t$, verificar que exista el límite (0/0, sale con L'Hôpital) [1:18:48]:

$$
\lim_{t\to 0}\frac{1 - e^{-3t}}{t} = 3 \quad (\text{existe})
$$

**Paso 3:** la transformada de algo dividido por $t$ es la integral entre $s$ e $\infty$ de la transformada del numerador, escrita en función de $u$ [1:18:48]–[1:19:28]:

$$
\mathcal{L}\!\left[\frac{1 - e^{-3t}}{t}\right] = \int_s^{\infty}\left(\frac{1}{u} - \frac{1}{u + 3}\right)du
$$

**Paso 4:** la primitiva da logaritmos; al evaluar en $\infty$ aparece $\infty - \infty$. Para salvar la indeterminación, juntar en el logaritmo de un cociente [1:19:28]–[1:20:30]:

$$
\Big[\ln u - \ln(u+3)\Big]_s^{\infty} = \left[\ln\frac{u}{u+3}\right]_s^{\infty} = 0 - \ln\frac{s}{s+3} = \ln\frac{s+3}{s}
$$

En el infinito el argumento tiende a 1 y el logaritmo a 0.

**Paso 5:** evaluar en $s = 3$ [1:20:30]–[1:21:00]:

$$
\ln\frac{3+3}{3} = \ln 2
$$

</details>

</details>

---

## Sistemas estables: estabilidad por polos, cancelar el polo inestable y corte por el eje real — [1:21:00]

- **La estabilidad depende de los polos** [1:21:33]: analizar qué pasa con los polos de cada factor del denominador.
  - Polos en el semiplano izquierdo (parte real negativa): no molestan.
  - Polo en el origen: lo hace **marginalmente estable**, "pero no me joden, no me hacen que sea inestable" [1:22:35]–[1:23:06] (en el OneNote: "Marg. estable es estable" [OneNote p. 8]).
  - Polo real positivo (semiplano derecho): hace al sistema inestable.
- **Cancelar el polo inestable con $K$** [1:23:39]–[1:24:42]: elegir $K$ para que el numerador también tenga esa raíz y se simplifique arriba y abajo. "Idea básica, pero que aparece en un montón de ejercicios."
- **Elementos para el corte por el eje real** [1:25:13]–[1:27:17]:
  - **Cero real finito**: la gráfica toca y "rebota" en el eje horizontal.
  - **Cero en el infinito**: está siempre que el grado del denominador supera al del numerador; implica asíntotas horizontales a izquierda y derecha. Ponerlo "está copado", olvidarlo "no es un error muy grave".
  - **Polos complejos conjugados**: una **montañita** en su parte real, porque el plano $\mathrm{Im}(s) = 0$ corta justo en el medio de los dos "volcanes" sin embocarle a ninguno [1:28:53].
  - **Polo real**: asíntota vertical (el plano corta justo "en la boquita del volcán") [1:29:24].
- **Pregunta: ¿y si hubiera un solo polo complejo?** [1:29:24]–[1:29:55] No puede pasar: las $G(s)$ tienen coeficientes reales, y los polinomios con coeficientes reales tienen raíces reales o complejas conjugadas, "en pares".
- **Pregunta: ¿y en el corte por el eje imaginario?** [1:30:27]–[1:32:32] Tampoco se ven asíntotas de los polos complejos (están en $\mathrm{Re} = -2$, no en $\mathrm{Re} = 0$); dibujar dos montañitas no estaría mal. Lo importante en ese corte sería el polo en el **cero**, que "es como un comodín": es real e imaginario a la vez, así que "cae parado en los dos" cortes. En el corte real se mira qué pasa con los números reales; en el imaginario, con los imaginarios.
- **Respuesta al impulso = respuesta natural** [1:33:34]–[1:34:35]: como $Y(s) = G(s)\,F(s)$ y la transformada del impulso es $F(s) = 1$, queda $Y(s) = G(s)$.
- **Polos complejos ⇒ senos y cosenos** [1:35:07]–[1:37:45]: completar cuadrados en el denominador, $(s + a)^2 + b^2$: el $b$ dice el $\mathrm{sen}(bt)$/$\cos(bt)$ y el $s + a$ dice el factor $e^{-at}$. Hay que **hacer aparecer el mismo $s + a$ en el numerador** "prestando" del término independiente y separar el resto en otro término (con el seno). "Este tipo de truquitos también puede aparecer."

<details>
<summary>📝 Ejercicio 8 — [1:21:00]: hallar $K$ para que sea estable, corte por el eje real y respuesta al impulso</summary>

Sea [OneNote p. 7–8]

$$
G(s) = \frac{25\,(s^2 - Ks + 12)}{(s^2 + 4s + 5)(s^2 - 3s)}
$$

la transferencia de un sistema. a) Halle el valor de $K \in \mathbb{R}$ sabiendo que el sistema es estable, y grafique aproximadamente el corte de $|G(s)|$ con el eje real. b) Halle la respuesta del sistema a una entrada impulso unitario.

<details>
<summary>Ver resolución</summary>

**Paso 1:** factorizar el denominador y analizar polos [1:22:04]–[1:23:06] [OneNote p. 8]:

$$
G(s) = \frac{25\,(s^2 - Ks + 12)}{(s^2 + 4s + 5)\cdot s\cdot(s - 3)}
$$

- $s^2 + 4s + 5$: complejos conjugados $-2 \pm j$, parte real negativa → no molestan.
- $s$: polo en el origen → marginalmente estable, no inestable.
- $s - 3$: polo real positivo → **este es el que hace inestable al sistema**.

**Paso 2:** para cancelar el $s - 3$, el numerador tiene que tener raíz 3 [1:23:39]–[1:24:11] [OneNote p. 8]:

$$
\left[s^2 - Ks + 12\right]_{s=3} = 9 - 3K + 12 = 0 \quad\Rightarrow\quad K = 7
$$

**Paso 3:** con $K = 7$, $s^2 - 7s + 12 = (s - 3)(s - 4)$ (en el OneNote, por Ruffini) y se cancela el $s - 3$ [1:24:42] [OneNote p. 8]:

$$
G(s) = \frac{25\,(s - 4)}{(s^2 + 4s + 5)\,s}
$$

**Paso 4:** ceros y polos [1:25:13]–[1:26:14] [OneNote p. 8]: $z_1 = 4$, $z_2 = \infty$; $p_{1,2} = -2 \pm j$, $p_3 = 0$.

**Paso 5:** corte por el eje real [1:27:48] [OneNote p. 8]: asíntotas horizontales a izquierda y derecha (cero en el infinito), montañita en $\sigma = -2$ (parte real de los polos complejos), asíntota vertical sobre el eje $y$ (polo en 0) y toca el eje en $\sigma = 4$ (cero). El profe lo muestra también en 3D (GeoGebra) [1:28:22]: en el 4 "lo hace en una escala muy bajita" pero rebota. [paso en el pizarrón, ver video]

**Paso 6 (parte b):** impulso ⇒ $F(s) = 1$ ⇒ $Y(s) = G(s)$ [1:34:04] [OneNote p. 9]. Fracciones simples con polos complejos conjugados:

$$
Y(s) = \frac{25(s - 4)}{s\,(s^2 + 4s + 5)} = \frac{A}{s} + \frac{Bs + C}{s^2 + 4s + 5}
$$

$A$ con el truquito: $\frac{-100}{5} = -20$. Igualando coeficientes [OneNote p. 9]:

$$
-20(s^2 + 4s + 5) + Bs^2 + Cs = 25s - 100
$$

Cuadráticos: $-20 + B = 0 \Rightarrow B = 20$. Lineales: $-80 + C = 25 \Rightarrow C = 105$.

**Paso 7:** completar el cuadrado y hacer aparecer $s + 2$ arriba: $20s + 105 = 20(s + 2) + 65$ (el 105 le "presta" 40) [1:35:39]–[1:37:12] [OneNote p. 9]:

$$
Y(s) = -\frac{20}{s} + \frac{20\,(s + 2)}{(s + 2)^2 + 1} + \frac{65}{(s + 2)^2 + 1}
$$

**Paso 8:** antitransformar (el $+1$ da $\cos t$ y $\mathrm{sen}\,t$; el $s + 2$, la traslación $e^{-2t}$) [1:37:12] [OneNote p. 9]:

$$
y(t) = -20 + 20\cos(t)\,e^{-2t} + 65\,\mathrm{sen}(t)\,e^{-2t}
$$

</details>

</details>

---

## Sistemas desde el gráfico del corte: leer polos y ceros, constelación y método vectorial — [1:37:45]

- Es el camino inverso: "antes, a partir de los elementos hicimos el gráfico; ahora, a partir del gráfico vamos a ver los elementos" [1:38:49].
  - Asíntotas horizontales → cero en el infinito.
  - Toca el eje en el origen → cero en $0$.
  - Asíntota vertical en $\sigma = 1$ → polo en $1$.
  - Montañita en $\sigma = -2$ → polos complejos conjugados con parte real $-2$.
- **Polinomio a partir de raíces complejas $a \pm bj$** [1:40:25]–[1:41:00]: hacer la distributiva de $(s - (a + bj))(s - (a - bj))$ o usar la forma genérica: el coeficiente lineal es menos dos veces la parte real y el independiente es $a^2 + b^2$.
- **Todas las $G(s)$ llevan una constante $K$** [1:41:00]; se halla con el dato de módulo.
- **Método gráfico (vectorial)** [1:41:38]–[1:42:42]: armar la **constelación de polos y ceros** (cruces para polos, circulitos para ceros), marcar el punto donde se evalúa y trazar vectores desde cada cero y cada polo hasta ese punto:

$$
|G(s_0)| = K\,\frac{\prod |\text{vectores desde los ceros}|}{\prod |\text{vectores desde los polos}|}
$$

<details>
<summary>📝 Ejercicio 9 — [1:37:45]: $G(s)$ desde el corte por el eje real + respuesta a una entrada dada</summary>

El siguiente gráfico muestra el corte de $|G(s)|$ por el eje real (asíntotas horizontales, montañita en $-2$, toca el eje en 0 y asíntota vertical en 1) [OneNote p. 9]. a) Escriba la expresión de $G(s)$ sabiendo que tiene únicamente 3 polos (cuya distancia al eje real es entera y no mayor a 1) y un cero finito y simple, y además $|G(1+j)| = 2$. b) Halle la respuesta del sistema a una entrada

$$
x(t) = \frac{1}{\sqrt{26}}\,(1 - t) \qquad (t > 0)
$$

<details>
<summary>Ver resolución</summary>

**Paso 1:** leer el gráfico [1:38:49]–[1:39:21] [OneNote p. 10]: $z_1 = 0$, $p_1 = 1$, $p_{2,3} = -2 \pm bj$.

**Paso 2:** la distancia de los polos al eje real es entera y no mayor a 1, y por ser distancia es positiva ⇒ $b = 1$ ("una forma medio rebuscada de decir que los polos son $-2 \pm j$") [1:39:52] [OneNote p. 10]:

$$
[s - (-2 + j)]\,[s - (-2 - j)] = s^2 + 4s + 5
$$

**Paso 3:** la transferencia con la constante [1:41:00] [OneNote p. 10]:

$$
G(s) = \frac{K\,s}{(s - 1)(s^2 + 4s + 5)}
$$

**Paso 4:** constelación y vectores hasta $1 + j$ [1:42:08]–[1:43:14] [OneNote p. 10–11]: desde el cero en 0, $\sqrt{1^2 + 1^2} = \sqrt{2}$; desde el polo en 1, vertical de longitud 1; desde $-2 + j$, horizontal de longitud 3; desde $-2 - j$, componentes 3 y 2: $\sqrt{9 + 4} = \sqrt{13}$.

$$
|G(1+j)| = \frac{K\sqrt{2}}{3\cdot\sqrt{13}\cdot 1} = 2 \quad\Rightarrow\quad K = 3\sqrt{26}
$$

"Número feo, pero da eso" [1:43:14].

$$
G(s) = \frac{3\sqrt{26}\,s}{(s - 1)(s^2 + 4s + 5)}
$$

**Paso 5 (parte b):** transformar la entrada y sacar denominador común $s^2$, porque después se cancelan muchas cosas [1:44:16] [OneNote p. 11]:

$$
X(s) = \frac{1}{\sqrt{26}}\left(\frac{1}{s} - \frac{1}{s^2}\right) = \frac{1}{\sqrt{26}}\cdot\frac{s - 1}{s^2}
$$

**Paso 6:** $Y(s) = G(s)\,X(s)$: se cancelan las $\sqrt{26}$, el $s - 1$ (el polo inestable en 1) y una $s$ [1:44:48]–[1:45:19] [OneNote p. 11]:

$$
Y(s) = \frac{3}{s\,(s^2 + 4s + 5)} = \frac{A}{s} + \frac{Bs + C}{s^2 + 4s + 5}
$$

**Paso 7:** $A = 3/5$ con el truquito; igualando coeficientes [OneNote p. 11–12]:

$$
\frac{3}{5}(s^2 + 4s + 5) + Bs^2 + Cs = 3
$$

Cuadráticos: $\frac{3}{5} + B = 0 \Rightarrow B = -\frac{3}{5}$. Lineales: $\frac{12}{5} + C = 0 \Rightarrow C = -\frac{12}{5}$.

**Paso 8:** hacer aparecer $s + 2$: $\frac{3}{5}s + \frac{12}{5} = \frac{3}{5}(s + 2) + \frac{6}{5}$ (el $\frac{12}{5}$ "presta" $\frac{6}{5}$ y se queda con $\frac{6}{5}$) [1:46:20]–[1:46:51] [OneNote p. 12]:

$$
Y(s) = \frac{3/5}{s} - \frac{3}{5}\cdot\frac{s + 2}{(s + 2)^2 + 1} - \frac{6/5}{(s + 2)^2 + 1}
$$

**Paso 9:** antitransformar [1:46:51]–[1:47:21] [OneNote p. 12]:

$$
y(t) = \frac{3}{5} - \frac{3}{5}\cos(t)\,e^{-2t} - \frac{6}{5}\,\mathrm{sen}(t)\,e^{-2t}
$$

</details>

</details>

---

## Preguntas de sistemas: tipo de respuesta, valor estable, módulo analítico vs. gráfico y la constante $K$ — [1:47:54]

- **Tipo de respuesta** [1:47:54]–[1:48:24]: la del ejercicio 9 es **oscilatoria** (por el seno/coseno) **amortiguada** (por la exponencial con exponente negativo, $e^{-2t}$) y desplazada (por el $3/5$). "Lo importante que me diga es oscilatoria amortiguada."
- **Valor estable** [1:48:24]: se saca con el límite; en el ejercicio 9 es $3/5$.
- **Forma analítica vs. gráfica del módulo** [1:48:57]–[1:50:27]: son equivalentes. La analítica es evaluar $G$ en el punto y tomar módulo; por propiedades del módulo se distribuye en cada factor, y cada factor coincide con un vector del método gráfico (por ejemplo, $|1 + j| = \sqrt{2}$ y $|1 + j - 1| = |j| = 1$). "Solo hace como este paso extra."
- **La constante $K$** [1:50:58]–[1:52:01]: se dejan las $s$ "solitas" ($s - a$, $s^2 + \ldots$) arriba y abajo y todo lo que queda afuera es la $K$. Si ya viene dada (por ejemplo un 3), **hay que ponerla al calcular el módulo**; un alumno cuenta que se la olvidaba "y me daba cualquier cosa". La $K$ cambia el módulo pero **no el argumento** (multiplicar por 5, por 100 o por 1 no cambia el ángulo de giro).

---

## Transformada Z: ecuaciones en diferencias, "dejar una $z$ afuera" y región de convergencia — [1:52:37]

- **Ecuaciones en diferencias** de primer y segundo orden se resuelven igual: como en Laplace, aplicar la transformada Z **a ambos miembros** [1:52:37]–[1:53:07]. Desplazamiento una unidad a izquierda:

$$
\mathcal{Z}[x(n+1)] = z\,X(z) - z\,x(0)
$$

- La constante 2 es "2 por el escalón unitario" $u(n)$; en la tabla aparece como la función 1: $\mathcal{Z}[u(n)] = \frac{z}{z - 1}$ [1:53:39].
- **Fracciones simples en Z: dejar una $z$ afuera** ("por favor, por favor, encarecidamente") [1:54:45]: se hacen fracciones simples de $X(z)/z$ y después se reincorpora la $z$, para que queden términos $\frac{z}{z - a}$ listos para antitransformar a $a^n$.
- Igual que en Laplace, separar términos antes "también es válido"; el profe primero pensó que un término daría $2\cdot 3^n$ y se corrigió: al hacer fracciones simples aparecía un $\frac{z}{z-3}$ extra que no estaba considerando ("hubieran llegado al mismo resultado, solo que necesitaba un pasito extra") [1:55:49].
- **Verificación**: calcular $x(2)$ iterando la ecuación ("el valor siguiente es igual a 3 veces el anterior más 2") y con la solución; si coinciden está bien, "o tienen mucha mala suerte y justo les da igual" [1:56:51]–[1:57:54].
- **Región de convergencia por geométricas** [1:59:30]–[2:03:38]: plantear la definición, escribir los primeros términos, agrupar en sumatorias según el caso (antes era par/impar; acá múltiplos de 3 o restos 1 y 2 de dividir por 3) y llevar cada sumatoria a "algo elevado a la $k$". "Siempre el objetivo es dejar a algo elevado a la $k$" [2:02:06].

$$
X(z) = \sum_{n=0}^{\infty} x(n)\,z^{-n}
$$

$$
\sum_{k=0}^{\infty} a^k \text{ converge} \iff |a| < 1, \qquad \text{y converge a } \frac{1}{1 - a}
$$

- Si solo piden la región de convergencia **no hace falta llegar a la transformada**: alcanza con las condiciones de cada sumatoria [2:03:08]. Las constantes que multiplican (como $3/z$, $3/z^2$) no importan para la condición; importa lo que queda dentro de la sumatoria [2:04:08].
- La región final es la **intersección** de las condiciones. $|z| > r$ es el exterior de una circunferencia de centro en el origen; con desigualdad estricta, dibujarla **punteada** [2:04:40]–[2:05:41].

<details>
<summary>📝 Ejercicio 10 — [1:52:37]: ecuación en diferencias de primer orden + verificación</summary>

Usando Transformada Z hallar la solución de la siguiente ecuación en diferencia [OneNote p. 12]:

$$
x(n+1) = 3x(n) + 2, \qquad x(0) = 2
$$

Verifique el resultado obtenido hallando el valor $x(2)$ usando la ecuación en diferencia y su solución.

<details>
<summary>Ver resolución</summary>

**Paso 1:** transformada Z miembro a miembro [1:53:07] [OneNote p. 12]:

$$
z\,X(z) - z\,\underbrace{x(0)}_{2} = 3X(z) + \frac{2z}{z - 1}
$$

**Paso 2:** agrupar [1:53:39] [OneNote p. 12]:

$$
X(z)\,(z - 3) = \frac{2z}{z - 1} + 2z \quad\Rightarrow\quad X(z) = \frac{2z^2}{(z - 1)(z - 3)}
$$

**Paso 3:** fracciones simples **dejando una $z$ afuera** (de $2z$, no de $2z^2$). Dos polos simples reales: las dos salen con el truquito [1:54:45]–[1:55:17] [OneNote p. 12–13]:

$$
\frac{2z}{(z - 1)(z - 3)} = \frac{A}{z - 1} + \frac{B}{z - 3}, \qquad A = \frac{2}{-2} = -1, \quad B = \frac{6}{2} = 3
$$

**Paso 4:** reincorporar la $z$ y antitransformar [1:55:17]–[1:56:19] [OneNote p. 13]:

$$
X(z) = -\frac{z}{z - 1} + \frac{3z}{z - 3} \quad\Rightarrow\quad x(n) = -1 + 3\cdot 3^n = -1 + 3^{n+1}
$$

**Paso 5:** verificación con la ecuación en diferencia [1:56:51] [OneNote p. 13]:

$$
x(0) = 2, \qquad x(1) = 3\cdot 2 + 2 = 8, \qquad x(2) = 3\cdot 8 + 2 = 26
$$

**Paso 6:** con la solución hallada [1:57:22]–[1:57:54] [OneNote p. 13]:

$$
x(2) = -1 + 3\cdot 3^2 = 26 \quad ✓
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 11 — [1:58:58]: región de convergencia con una sucesión definida por múltiplos de 3</summary>

La región de convergencia de la transformada Z de [OneNote p. 13]

$$
x(n) = \begin{cases} -3 & \text{si } n \text{ no es múltiplo de } 3 \\ (-2)^n & \text{si } n \text{ es múltiplo de } 3 \end{cases}
$$

es: a) $|z| > 2$ · b) $|z| \ge 3$ · c) $|z| \ge 2$ · d) $|z| < 3$ · e) $2 < |z| < 3$ · f) n.a.

<details>
<summary>Ver resolución</summary>

**Paso 1:** definición y primeros términos: $n = 0$ y $n = 3$ entran por los múltiplos de 3; $n = 1, 2, 4$ valen $-3$ [1:59:30]–[2:00:31] [OneNote p. 13]:

$$
X(z) = \sum_{n=0}^{\infty} x(n)\,z^{-n} = \frac{(-2)^0}{z^0} + \frac{-3}{z} + \frac{-3}{z^2} + \frac{(-2)^3}{z^3} + \frac{-3}{z^4} + \cdots
$$

**Paso 2:** agrupar en tres sumatorias según el resto de dividir por 3 (resto 0, 1 y 2). El $-3$ no depende de $n$, sale como constante [2:00:31]–[2:01:35] [OneNote p. 13]:

$$
X(z) = \sum_{k=0}^{\infty}\left(\frac{-2}{z}\right)^{3k} - 3\sum_{k=0}^{\infty}\left(\frac{1}{z}\right)^{3k+1} - 3\sum_{k=0}^{\infty}\left(\frac{1}{z}\right)^{3k+2}
$$

**Paso 3:** propiedades de la potencia para dejar "algo elevado a la $k$" [2:02:06]–[2:02:37] [OneNote p. 13]:

$$
X(z) = \sum_{k=0}^{\infty}\left(\frac{-8}{z^3}\right)^{k} - \frac{3}{z}\sum_{k=0}^{\infty}\left(\frac{1}{z^3}\right)^{k} - \frac{3}{z^2}\sum_{k=0}^{\infty}\left(\frac{1}{z^3}\right)^{k}
$$

**Paso 4:** solo importa la región de convergencia: condición de cada geométrica (la segunda y la tercera tienen la misma) [2:03:38]–[2:04:40] [OneNote p. 14]:

$$
\left|\frac{-8}{z^3}\right| < 1 \Rightarrow |z^3| > 8 \Rightarrow |z| > 2, \qquad \left|\frac{1}{z^3}\right| < 1 \Rightarrow |z^3| > 1 \Rightarrow |z| > 1
$$

**Paso 5:** intersección: exterior de la circunferencia más grande [2:05:41] [OneNote p. 14]:

$$
|z| > 2 \quad\Rightarrow\quad \text{opción a)}
$$

**Paso 6 (para practicar, no lo pedía):** sumar las geométricas y simplificar las $z$ [2:06:12]–[2:06:44] [OneNote p. 14–15]:

$$
X(z) = \frac{1}{1 - \left(\frac{-8}{z^3}\right)} - \frac{3}{z}\cdot\frac{1}{1 - \frac{1}{z^3}} - \frac{3}{z^2}\cdot\frac{1}{1 - \frac{1}{z^3}} = \frac{z^3}{z^3 + 8} - \frac{3z^2}{z^3 - 1} - \frac{3z}{z^3 - 1}
$$

La forma sin simplificar "está bien", pero si pueden, mejor llegar a la recuadrada [2:07:17].

</details>

</details>

---

## Complejos (si sobra tiempo): potencia enésima y raíces cuartas en forma binómica — [2:07:17]

- **Potencia enésima (De Moivre)** [2:08:19]: en polar, $[\rho, \varphi]^n = [\rho^n, n\varphi]$.
- Para igualar a un número dado hay que **chequear módulo y argumento**: el módulo da un candidato para $n$, pero "capaz tu argumento no es este"; hay que verificar que los argumentos sean **congruentes** [2:09:53]. Para comparar, llevar todo al **primer giro positivo** (sumar $2\pi$ si está en el cuarto cuadrante; restar giros de $2\pi$ si se pasó) [2:10:24]–[2:11:57].
- **Raíces cuartas en binómica** [2:13:30]–[2:15:33]: algo que no había mostrado en las prácticas. La binómica "no está buena para raíces, se vuelve tediosa", pero una raíz cuarta se puede escribir como **raíz cuadrada de una raíz cuadrada**, y la raíz cuadrada es la única que se sabe hacer en binómica (con las fórmulas de $x$ e $y$ y la regla del signo de la parte imaginaria). El orden de las $w$ puede no coincidir con el de la forma polar, "no importa, lo importante es que me digan esas cuatro cuáles son".
- **Conjuntos del tipo $|z - z_0| \le r$** [2:16:06]–[2:17:10]: escribiendo $z = a + bj$ se ve que es un círculo de centro $z_0$ y radio $r$; se puede resolver gráfico (ubicar los puntos y ver cuáles caen adentro, borde incluido) o analítico (calcular el módulo para cada punto). Él lo resolvería analítico: "es un poquito más larga pero igual es fácil" [2:17:45].

<details>
<summary>📝 Ejercicio 12 — [2:07:49]: hallar $n \in \mathbb{N}$ tal que $(1 - 2j)^n = 117 - 44j$</summary>

a) Halle el valor de $n \in \mathbb{N}$ tal que $(1 - 2j)^n = 117 - 44j$ (justifique su forma de hallarlo) [OneNote p. 15].

<details>
<summary>Ver resolución</summary>

**Paso 1:** pasar a polar y aplicar De Moivre ("el arco tangente de −2 no da ningún número lindo") [2:08:19]–[2:08:50] [OneNote p. 15]:

$$
(1 - 2j)^n = \left[\sqrt{5},\, \mathrm{arctg}(-2)\right]^n = \left[(\sqrt{5})^n,\; n\,\mathrm{arctg}(-2)\right]
$$

$$
117 - 44j = \left[125,\; \mathrm{arctg}\!\left(\frac{-44}{117}\right)\right]
$$

**Paso 2:** igualar módulos [2:09:21] [OneNote p. 15]:

$$
(\sqrt{5})^n = 125 \quad\Rightarrow\quad n = 6
$$

**Paso 3:** chequear los argumentos llevando todo al primer giro positivo. Los dos números están en el cuarto cuadrante (real positiva, imaginaria negativa) ⇒ sumar $2\pi$ [2:10:24]–[2:11:25] [OneNote p. 15]:

$$
\mathrm{arctg}\!\left(\frac{-44}{117}\right) = -0{,}3597 + 2\pi = 5{,}9235
$$

$$
6\,\mathrm{arctg}(-2) = 6\,(-1{,}1072 + 2\pi) = 31{,}0562
$$

**Paso 4:** 31,06 es positivo pero se pasó del primer giro ($0$ a $2\pi \approx 6{,}28$): restar 4 giros [2:11:57] [OneNote p. 15]:

$$
31{,}0562 - 8\pi = 5{,}9235 \quad ✓
$$

Los argumentos son congruentes (difieren en 4 giros) ⇒ $n = 6$ es correcto [2:12:29].

</details>

</details>

<details>
<summary>📝 Ejercicio 13 — [2:12:59]: resolver $z^4 + 16 = 0$ con $|z + 1 - j| \le 1$</summary>

b) Resuelva en $\mathbb{C}$: $z^4 + 16 = 0 \;\wedge\; |z + 1 - j| \le 1$ (las dos condiciones se cumplen a la vez) [OneNote p. 15].

<details>
<summary>Ver resolución</summary>

**Paso 1 (condición 1, en polar):** $z^4 = -16$, y $-16 = [16, \pi]$; con la fórmula de raíces enésimas salen las cuatro raíces: parte real e imaginaria de módulo $\sqrt{2}$ "y las cuatro combinaciones de signos" [2:13:30] [OneNote p. 15–16]:

$$
z = \sqrt[4]{[16, \pi]} \quad\Rightarrow\quad \pm\sqrt{2} \pm \sqrt{2}\,j
$$

[En el OneNote p. 16 los argumentos figuran como $\pi/4$, $5\pi/4$, $9\pi/4$, $13\pi/4$; con la fórmula $\frac{\pi + 2k\pi}{4}$ corresponden $\pi/4$, $3\pi/4$, $5\pi/4$, $7\pi/4$. Las cuatro raíces binómicas listadas son las mismas.]

**Paso 2 (condición 1, en binómica, alternativa):** escribir la raíz cuarta como raíz de raíz [2:14:00]–[2:15:01] [OneNote p. 16]:

$$
z = \sqrt[4]{-16} = \sqrt{\sqrt{-16}}, \qquad \sqrt{-16} = \pm 4j
$$

Luego la raíz cuadrada de $4j$ y de $-4j$ con las fórmulas ($|{\pm 4j}| = 4$, parte real 0):

$$
x = \sqrt{\frac{4 + 0}{2}} = \sqrt{2}, \qquad y = \sqrt{\frac{4 - 0}{2}} = \sqrt{2}
$$

Para $4j$ ($b > 0$): signos iguales ⇒ $\sqrt{2} + \sqrt{2}j$ y $-\sqrt{2} - \sqrt{2}j$. Para $-4j$ ($b < 0$): alternados ⇒ $\sqrt{2} - \sqrt{2}j$ y $-\sqrt{2} + \sqrt{2}j$ [2:15:33] [OneNote p. 16].

**Paso 3 (condición 2, gráfica):** con $z = a + bj$, $|(a + 1) + (b - 1)j| \le 1$: círculo de **centro $-1 + j$** (corrido a la izquierda y arriba) y **radio 1**, borde incluido [2:16:06]–[2:17:10]. Las cuatro raíces forman un cuadrado; la única adentro es $-\sqrt{2} + \sqrt{2}j$ (el profe lo grafica con GeoGebra) [2:17:10] [OneNote p. 17].

**Paso 4 (condición 2, analítica):** módulo de cada raíz más $1 - j$ [2:17:45]–[2:18:46] [OneNote p. 17]:

$$
|\sqrt{2} + \sqrt{2}j + 1 - j| = \sqrt{6} \approx 2{,}4495 \quad ✗
$$

$$
|-\sqrt{2} - \sqrt{2}j + 1 - j| = \sqrt{6} \quad ✗
$$

$$
|\sqrt{2} - \sqrt{2}j + 1 - j| = 2 + \sqrt{2} \approx 3{,}4142 \quad ✗
$$

$$
|-\sqrt{2} + \sqrt{2}j + 1 - j| = 2 - \sqrt{2} \approx 0{,}5858 \quad ✓
$$

**Paso 5:** solución:

$$
z = -\sqrt{2} + \sqrt{2}\,j
$$

Coincide con lo gráfico: parte real negativa, parte imaginaria positiva [2:18:46].

</details>

</details>

---

## Cierre y consultas finales — [2:18:46]

- Dudas: por el foro del aula, por mensaje privado del campus (le llega notificación al mail) o por mail; si no responde en unas 6 horas, mandar mail [2:18:46]–[2:20:21].
- **Pregunta: $f(t) = t^2$ en $(0, 2)$ repetida, ¿es par?** [2:20:21]–[2:20:52] No: repitiendo ese tramo la función no es par, así que no puede tener serie de solo cosenos. Sería par si estuviera planteada en un intervalo simétrico.

---

*Generado el 2026-10-02 a partir de la transcripción local con Whisper (`apuntes/transcripts/10-video-repaso-primer-parcial.json`, 141 min) de `fuentes/clases/repaso primer parcial/Repaso Primer Parcial.mp4`, con enunciados y fórmulas tomados del OneNote de la misma clase (`fuentes/clases/repaso primer parcial/Repaso Primer Parcial.pdf`, 17 págs.; citado como [OneNote p. N]). Las explicaciones, advertencias y respuestas a preguntas salen de la transcripción; los timestamps son los marcadores reales del audio (sin enlace público).*
