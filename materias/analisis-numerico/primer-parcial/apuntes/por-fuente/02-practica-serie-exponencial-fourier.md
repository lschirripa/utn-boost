# Práctica: Serie Exponencial de Fourier (SEF)

> Fuente: fuentes/clases/series de fourier/Series Fourier - SEF.pdf, págs. 1–6

---

## Índice

- [p. 1] — Cuándo conviene la STF y cuándo la SEF
- [p. 1] — Fórmulas de la SEF y relación con los coeficientes de la STF
- [p. 2] — Recomendación del profe: calcular $a_m$ y $b_m$ y pasar a $C_m$
- [p. 2] — Función impar desplazada
- [p. 1] — 📝 Ejercicio 8a: pulso rectangular, $T = 20$ *(sin resolución)*
- [p. 3] — 📝 Ejercicio 8b: onda triangular, $T = 4$ *(solo planteo)*
- [p. 1] — 📝 Ejercicio 8c: diente de sierra $f(t) = 2t$, $T = 2$ *(resuelto completo)*
- [p. 1] — 📝 Ejercicio 8 optativo: $f(t) = t^2$ en medio período *(sin resolución)*
- [p. 4] — Coeficientes reales o imaginarios puros según la paridad
- [p. 5] — Completar una función con dos condiciones: cuadruplicar el intervalo
- [p. 4] — 📝 Ejercicio 9a: completar $f(t) = t^2$ para que la SEF tenga $C_m$ imaginarios puros y SMO
- [p. 5] — 📝 Ejercicio 9b: función con $T = 2$, $C_m$ imaginarios puros y $C_0 = 3$

---

## Cuándo conviene la STF y cuándo la SEF — [p. 1]

Nota del profe en el encabezado de la clase (textual):

> Lo importante es que sepan distinguir **cuándo conviene utilizar los coeficientes de la STF y cuándo los de la SEF**. Para funciones **pares e impares, mejor la STF**. Si no hay nada de eso, quizás es mejor ya trabajar directamente con el $C_n$.

## Fórmulas de la SEF y relación con los coeficientes de la STF — [p. 1]

Desarrollo en Serie Exponencial de Fourier de una función de período $T = 2L$, con $\omega_0 = \dfrac{2\pi}{T} = \dfrac{\pi}{L}$:

$$
S(t) = C_0 + \sum_{\substack{m=-\infty \\ m \neq 0}}^{\infty} C_m \, e^{j m \omega_0 t}
$$

Coeficientes (el profe escribe los límites $-L$ a $L$ y, en verde, la alternativa equivalente $0$ a $T$: se integra sobre **un período cualquiera**):

$$
C_0 = \frac{1}{2L} \int_{-L}^{L} f(t)\, dt
$$

$$
C_m = \frac{1}{2L} \int_{-L}^{L} f(t)\, e^{-j m \omega_0 t}\, dt
$$

**Relación con la STF** (fórmula clave de toda la práctica):

$$
C_m = \frac{1}{2}\left(a_m - j\, b_m\right)
$$

## Recomendación del profe: calcular $a_m$ y $b_m$ y pasar a $C_m$ — [p. 2]

Recomendación (textual de la guía):

> Usar los $a_n$ y $b_n$ de la STF en vez del $C_n$ de la SEF. Fundamentalmente porque se pueden aprovechar las **propiedades de funciones pares e impares**. También es cierto que en la cursada practicamos más la STF, así que estamos más acostumbrados a esas integrales, y son más sencillas que trabajar con la $j$ metida en el medio de la integral.

En la práctica, entonces, el camino es: graficar → detectar paridad (o paridad desplazada) → calcular con la STF solo el coeficiente que no se anula → armar $C_m = \frac{1}{2}(a_m - j b_m)$ → escribir la SEF y el espectro.

## Función impar desplazada — [p. 2]

Si la función es **impar desplazada** (una función impar corrida verticalmente, como el diente de sierra $2t$ en $[0,2)$ que oscila alrededor de $2$):

- $a_m = 0$ para $m \geq 1$ (la parte "impar" mata los cosenos),
- pero el valor medio **no** es cero: $\dfrac{a_0}{2}$ se lee directo del gráfico (la altura del desplazamiento),
- por lo tanto $C_m = -\dfrac{1}{2}\, j\, b_m$ para $m \neq 0$ (imaginarios puros) y $C_0 = \dfrac{a_0}{2} \neq 0$.

<details>
<summary>📝 Ejercicio 8a — [p. 1]: pulso rectangular con T = 20 (SEF + espectro de amplitudes)</summary>

**Ejercicio n° 8.** Dadas las siguientes funciones, grafíquelas, desarróllelas en Serie Exponencial de Fourier y grafique el espectro de amplitud de frecuencias:

a)

$$
f(t) = \begin{cases} 1 & \text{si } -2 < t < 2 \\ 0 & \text{si } 2 < |t| < 10 \end{cases} \qquad \text{y} \qquad f(t) = f(t+20)
$$

*(sin resolución en la fuente)*

</details>

<details>
<summary>📝 Ejercicio 8b — [p. 3]: onda triangular con T = 4 (solo el planteo)</summary>

b)

$$
f(t) = \begin{cases} t & \text{si } t \in (0,2) \\ 4-t & \text{si } t \in (2,4) \end{cases} \qquad \text{y} \qquad f(t+4) = f(t)
$$

Graficarla, desarrollarla en SEF y graficar el espectro de amplitud de frecuencias.

<details>
<summary>Ver planteo (la fuente solo trae el planteo, no la resolución completa)</summary>

**Paso 1:** Gráfico y parámetros. Es un triángulo que sube de $0$ a $2$ en $(0,2)$ y baja de $2$ a $0$ en $(2,4)$; repitiéndolo hacia la izquierda (en rojo en el manuscrito) queda el triángulo simétrico en $(-4,0)$ con pico $2$ en $t=-2$.

$$
T = 4, \qquad L = 2, \qquad \omega_0 = \frac{\pi}{2}
$$

**Paso 2:** Paridad. La función es **par**, entonces $b_m = 0$ y:

$$
C_m = \frac{1}{2}\, a_m
$$

**Paso 3:** Planteo por la STF (aprovechando la paridad, integrando en medio período y duplicando):

$$
a_m = \frac{2}{2} \int_0^2 x \cos\!\left(m \tfrac{\pi}{2} x\right) dx
$$

**Paso 4:** Comparación con el planteo directo por la SEF (para ver por qué NO conviene):

$$
C_m = \frac{1}{4} \int_{-2}^{2} f(x)\, e^{-j m \frac{\pi}{2} x}\, dx = \frac{1}{4} \left[ \int_{-2}^{0} -t\, e^{-j m \frac{\pi}{2} x}\, dx + \int_{0}^{2} t\, e^{-j m \frac{\pi}{2} x}\, dx \right]
$$

[el profe mezcla $x$ y $t$ como variable de integración; es la misma variable]

Comentario del profe sobre la integral de la SEF: **"Hay que abrir → + trabajo"**: por la vía directa hay que partir la integral en dos tramos y lidiar con la exponencial compleja, mientras que por la STF una sola integral real resuelve el problema.

La fuente no continúa con el cálculo de $a_m$ ni con la serie final.

</details>

</details>

<details>
<summary>📝 Ejercicio 8c — [p. 1]: diente de sierra f(t) = 2t con T = 2 (SEF + espectro de amplitudes)</summary>

c) $f(t) = 2t$ si $t \in [0,2)$ y $f(t) = f(t+2)$. Graficarla, desarrollarla en Serie Exponencial de Fourier y graficar el espectro de amplitud de frecuencias.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Gráfico y parámetros. Es un diente de sierra: rectas de pendiente $2$ que van de $0$ a $4$ en cada intervalo de longitud $2$, con saltos en $t = 0, \pm 2, \pm 4, \dots$

$$
T = 2, \qquad L = 1, \qquad \omega_0 = \pi
$$

**Paso 2:** Escribir la forma de la SEF y sus coeficientes.

$$
S(t) = C_0 + \sum_{\substack{m=-\infty \\ m \neq 0}}^{\infty} C_m \, e^{j m \omega_0 t}
$$

$$
C_0 = \frac{1}{2L} \int_{-L}^{L} f(t)\, dt, \qquad C_m = \frac{1}{2L} \int_{-L}^{L} f(t)\, e^{-j m \omega_0 t}\, dt
$$

y la relación con la STF:

$$
C_m = \frac{1}{2}\left(a_m - j\, b_m\right)
$$

**Paso 3:** Reconocer la paridad. Dibujando la línea de valor medio (en rojo, a altura $2$) se ve que la función es **impar desplazada**, entonces:

$$
a_m = 0
$$

y el valor medio se lee del gráfico:

$$
\frac{a_0}{2} = 2 \quad \text{(gráfico)}
$$

**Paso 4:** Calcular $b_m$ con la STF ($L = 1$, integrando sobre el período $[0,2]$):

$$
b_m = \frac{1}{1} \int_0^2 2 t \, \operatorname{sen}(m \pi t)\, dt
$$

$$
= 2 \left[ \frac{\operatorname{sen}(m\pi t)}{m^2 \pi^2} - \frac{t \cos(m \pi t)}{m \pi} \right]_0^2
$$

$$
= \frac{-4}{m \pi}
$$

**Paso 5:** Pasar a $C_m$. Como $a_m = 0$ (tachado en el manuscrito):

$$
C_m = \frac{1}{2}\left(\cancel{a_m} - j\, b_m\right) = -\frac{1}{2}\, j\, b_m
$$

$$
C_m = \frac{2j}{m\pi}
$$

**Paso 6:** Espectro de amplitudes $|C_m|$ en función de $m$: puntos en $m = 0, \pm 1, \pm 2, \pm 3, \dots$; en $m = 0$ vale $C_0 = 2$, en $m = \pm 1$ vale $\dfrac{2}{\pi}$, y las amplitudes decrecen simétricamente a ambos lados (envolvente tipo $\dfrac{2}{|m|\pi}$).

**Paso 7:** Escribir la SEF.

$$
S(t) = 2 + \sum_{\substack{m=-\infty \\ m \neq 0}}^{+\infty} \frac{2j}{m\pi}\, e^{j m \pi t}
$$

o, agrupando los términos $m$ y $-m$:

$$
= 2 + \sum_{m=1}^{\infty} \frac{2j}{m\pi}\, e^{j m \pi t} - \frac{2j}{m\pi}\, e^{-j m \pi t}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 8 optativo — [p. 1]: f(t) = t² en medio período, T = 4</summary>

OPTATIVO:

$$
f(t) = \begin{cases} 0 & \text{si } -2 < t < 0 \\ t^2 & \text{si } 0 < t < 2 \end{cases} \qquad \text{y} \qquad f(t+4) = f(t)
$$

Graficarla, desarrollarla en SEF y graficar el espectro de amplitud de frecuencias.

*(sin resolución en la fuente)*

</details>

## Coeficientes reales o imaginarios puros según la paridad — [p. 4]

De $C_m = \frac{1}{2}(a_m - j\, b_m)$ salen las dos reglas que el profe escribe en rojo:

- **SEF con coeficientes imaginarios puros** $\Rightarrow$ hay que anular $a_m$:

$$
C_m = \frac{1}{2}\left(\cancel{a_m} - b_m\, j\right) \quad \Longrightarrow \quad f \text{ impar}
$$

- **SEF con coeficientes reales** $\Rightarrow$ hay que anular $b_m$:

$$
C_m = \frac{1}{2}\left(a_m - \cancel{b_m\, j}\right) \quad \Longrightarrow \quad f \text{ par}
$$

Y combinando con lo anterior [p. 5]: si piden $C_m$ imaginarios puros **pero** $C_0 \neq 0$, la función tiene que ser **impar desplazada** (impar + una constante).

## Completar una función con dos condiciones: cuadruplicar el intervalo — [p. 5]

Cuando dan $f$ en un tramo y piden completarla cumpliendo **dos** condiciones de simetría (por ejemplo, impar **y** simetría de media onda), el profe anota (en azul):

> Necesitamos **cuadruplicar la longitud del intervalo** porque tenemos **dos condiciones**.

Cada condición "gasta" una duplicación: la paridad fija el tramo simétrico respecto del origen (duplica), y la simetría de media onda fija el medio período siguiente como $-f$ (vuelve a duplicar). Si el tramo dado tiene longitud $\ell$, el período resulta $T = 4\ell$.

<details>
<summary>📝 Ejercicio 9a — [p. 4]: completar f(t) = t² para que la SEF tenga coeficientes imaginarios puros y simetría de media onda</summary>

**Ejercicio n° 9.** a) Sea $f(t) = t^2$ si $0 \leq t < 1$. Complete en forma gráfica y analítica la función para que el desarrollo en Serie Exponencial de Fourier tenga coeficientes imaginarios puros y además $f(t)$ tenga simetría de media onda.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Traducir la condición sobre los coeficientes a una condición de simetría.

$$
\text{SEF con coef. imaginarios puros} \Longrightarrow C_m = \frac{1}{2}\left(\cancel{a_m} - b_m\, j\right) \Longrightarrow f \text{ impar}
$$

(Y para referencia: SEF con coef. reales $\Rightarrow C_m = \frac{1}{2}(a_m - \cancel{b_m j}) \Rightarrow f$ par.)

**Paso 2:** Nos piden entonces dos cosas:

- **Impar** (en rojo en el gráfico),
- **S.M.O.** — simetría de media onda (en verde en el gráfico).

Como hay **dos condiciones**, hay que **cuadruplicar la longitud del intervalo**: el tramo dado es $[0,1)$, así que el período será $T = 4$ y se define la función en $(-2, 2)$.

**Paso 3:** Completar gráficamente. Partiendo de la rama $t^2$ en $[0,1)$ (negro, sube de $0$ a $1$):

- Imparidad: en $(-1,0)$ se refleja como $-t^2$ (rojo, baja de $0$ a $-1$ en $t=-1$).
- Media onda: en $(1,2)$ va la rama que, corrida medio período, es la opuesta: $(t-2)^2$ (verde, baja de $1$ en $t=1$ a $0$ en $t=2$); y en $(-2,-1)$ va $-(t+2)^2$ (verde, baja de $0$ en $t=-2$ a $-1$ en $t=-1$).
- Fuera de $(-2,2)$ se repite periódicamente (punteado verde).

**Paso 4:** Completar analíticamente.

$$
f(t) = \begin{cases} -(t+2)^2 & \text{si } -2 < t < -1 \\ -t^2 & \text{si } -1 < t < 0 \\ t^2 & \text{si } 0 < t < 1 \\ (t-2)^2 & \text{si } 1 < t < 2 \end{cases}
$$

con período $T = 4$.

</details>

</details>

<details>
<summary>📝 Ejercicio 9b — [p. 5]: ejemplo de función con T = 2, coeficientes imaginarios puros y C₀ = 3</summary>

b) Dé un ejemplo de una función periódica $f(x)$ con $T = 2$ tal que los coeficientes de la Serie Exponencial de Fourier sean todos imaginarios puros excepto el $c_0 = 3$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** Traducir las condiciones.

- SEF con coeficientes imaginarios puros: $f(x)$ **impar**.
- Además $C_0 \neq 0$.

Las dos juntas: $f(x)$ **impar desplazada**.

**Paso 2:** Proponer una función. Por ejemplo, un diente de sierra corrido:

$$
f(x) = x + k
$$

(gráfico: rectas de pendiente $1$ repetidas cada $2$, cruzando el eje vertical a altura $k$), con

$$
T = 2, \qquad L = 1, \qquad \omega_0 = \pi
$$

**Paso 3:** Ajustar $k$ con la condición $C_0 = 3$, integrando sobre un período $[0, T]$:

$$
C_0 = \frac{1}{2L} \int_0^T f(x)\, dx
$$

$$
C_0 = \frac{1}{2} \int_0^2 (x + k)\, dx = \frac{1}{2} \left[ \frac{x^2}{2} + k\, x \right]_0^2
$$

$$
= \frac{1}{2}\left(2 + 2k\right) = 3
$$

$$
k = 2
$$

**Paso 4:** Respuesta.

$$
\boxed{f(x) = x + 2}
$$

(con $f$ definida así en $(0,2)$ y extendida con período $T = 2$).

</details>

</details>
