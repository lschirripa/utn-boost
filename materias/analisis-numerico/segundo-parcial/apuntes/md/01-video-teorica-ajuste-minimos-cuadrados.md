# Aproximación discreta y continua por mínimos cuadrados (clase teórica grabada)

> Fuente: fuentes/clases/Ajuste-Aproximacion/Ajuste-teoria.mp4 (transcripción local con Whisper)

---

> **Cómo usar este apunte.** Es la **teoría** de la segunda mitad de la unidad
> "Interpolación y ajuste", tal como la da el profe en la clase grabada (1 h 48 min). La
> práctica (ejercicios 29, 30 y 32 de la guía) está en `02-practica-ajuste-minimos-cuadrados.md`.
> Los timestamps `[mm:ss]` son del video local (sin enlace público). El ejemplo de la clase
> se hizo en un Excel con 5 puntos cuyos valores de $y$ no se dictan completos: se anotan
> solo los números que el profe dice en voz alta.
>
> **Para el TP** lo que importa es: §1–§3 (la recta y su sistema), §4–§7 (modelos no
> polinómicos y cómo llevarlos a forma lineal), §8 (polinomios de grado n) y §9 (cómo se
> compara qué modelo ajusta mejor). El ajuste continuo y Legendre (§10–§12) no entran en el
> TP, pero sí en el 2P.

## Índice

- [00:00] — Qué es el ajuste discreto y por qué se minimiza el error cuadrático
- [04:09] — Dato de color: Gauss y el planeta Ceres
- [05:13] — La recta de mínimos cuadrados: el modelo base de todo
- [07:23] — Derivadas parciales y sistema de ecuaciones normales de la recta
- [11:33] — Regla mnemotécnica para armar el sistema
- [13:40] — 📝 Ejemplo 1: recta de mínimos cuadrados con 5 puntos (tabla, sistema, Excel)
- [20:42] — $y$ ajustado y error cuadrático de la recta
- [22:23] — Cuándo conviene otro modelo: si sabés cómo se comporta el fenómeno
- [24:56] — Modelo exponencial: por qué no se resuelve "derecho"
- [27:36] — Forma aparentemente lineal del exponencial y su sistema
- [31:27] — 📝 Ejemplo 2: ajuste exponencial de los mismos 5 puntos
- [34:40] — La forma aparentemente lineal NO da la mejor exponencial (Wolfram vs. Excel)
- [37:17] — Modelo potencial
- [41:28] — 📝 Ejemplo 3: ajuste potencial y primera comparación de errores
- [45:39] — Modelo hiperbólico
- [49:55] — Modelo de crecimiento con saturación
- [53:12] — Ajuste por un polinomio de grado n: el sistema de $n+1$ ecuaciones normales
- [57:25] — 📝 Ejemplo 4: parábola de mínimos cuadrados
- [1:01:34] — Grado alto: aparece el polinomio interpolante (error cero)
- [1:05:12] — Comparación de errores de todos los modelos
- [1:05:44] — Ajuste continuo: de sumatorias a integrales
- [1:12:38] — 📝 Ejemplo 5: recta continua para $e^x$ en $[1, 2]$
- [1:16:45] — Consulta: ¿a mano o en Excel?
- [1:17:53] — 📝 Ejemplo 6: parábola continua para $e^x$ en $[1, 2]$
- [1:19:27] — Ajuste continuo con polinomios ortogonales: idea y producto interno
- [1:26:48] — Fórmula de los coeficientes $a_k$ (sin sistema de ecuaciones)
- [1:29:23] — Polinomios de Legendre y sus normas
- [1:33:07] — 📝 Ejemplo 7: recta de Legendre para $e^x$ en $[-1, 1]$
- [1:35:55] — Ventaja de Legendre: agregar grados sin rehacer todo
- [1:38:38] — 📝 Ejemplo 8: Legendre fuera de $[-1,1]$, cambio de variable ($e^x$ en $[1,2]$)
- [1:47:05] — Cierre: qué se ve en la clase práctica

## 1. Ajuste discreto y error cuadrático — [00:00]

- **Ajuste discreto:** me dan una **serie finita de puntos** $(x_i, y_i)$ y busco una
  función que pase **lo más cerca posible de todos a la vez** (no necesariamente por
  ninguno, a diferencia de la interpolación).
- La distancia de cada punto a la función es la diferencia vertical $y_i - f(x_i)$, por
  arriba o por abajo. No se pueden sumar así nomás porque **se compensan** (un exceso y un
  defecto se cancelan), y los dos son error.
- Minimizar la suma de los **módulos** sería válido, pero para minimizar hay que derivar y el
  módulo tiene puntos donde no es derivable. El "truquito" es elevar al cuadrado, que
  siempre es positivo (o cero) y se deriva fácil. De ahí el nombre del método:

$$
E = \sum_{i=1}^{n} \big(y_i - f(x_i)\big)^2 \quad \longrightarrow \quad \text{mínimo}
$$

- $y_i$ y $x_i$ son datos; las incógnitas son los **coeficientes** de $f$.

> **Dato de color [04:09]:** el método se atribuye a Gauss, que con mediciones de la
> posición del planeta (planeta enano) Ceres predijo cuándo y dónde iba a volver a aparecer,
> cuando nadie le acertaba. Sirve para **predecir y ver tendencias** cuando se conoce el
> comportamiento de la función.

## 2. La recta de mínimos cuadrados — [05:13]

El profe insiste en que **es la base de todo** lo que viene (modelos no lineales,
polinomios de grado mayor, ajuste continuo): todo se arma comparando contra este sistema.

$$
y = a_0 + a_1\,x
$$

- $a_0$ = ordenada al origen, $a_1$ = pendiente. En la bibliografía suele aparecer como
  $y = b + a\,x$; el profe usa $a_0, a_1$ porque facilita la regla mnemotécnica (se acepta
  cualquier nomenclatura si se resuelve bien).
- Se minimiza:

$$
E(a_0, a_1) = \sum_{i=1}^{n} \big(y_i - a_0 - a_1 x_i\big)^2
$$

### Derivadas parciales — [07:23]

Como hay dos incógnitas, $E$ es una función de dos variables: se igualan a cero las
**derivadas parciales** respecto de $a_0$ y de $a_1$ (problema de optimización). Por regla
de la cadena baja el 2 y sale multiplicando $-1$ (lo que acompaña a $a_0$) o $-x_i$ (lo que
acompaña a $a_1$):

$$
\frac{\partial E}{\partial a_0} = -2\sum \big(y_i - a_0 - a_1 x_i\big) = 0
\qquad
\frac{\partial E}{\partial a_1} = -2\sum x_i \big(y_i - a_0 - a_1 x_i\big) = 0
$$

Distribuyendo y pasando las $\sum y_i$ al otro miembro (el 2 se va porque se iguala a 0), y
usando que $\sum_{i=1}^n 1 = n$ (la **cantidad de puntos**), queda el **sistema de
ecuaciones normales de la recta**:

$$
\left\{\begin{aligned}
a_0\, n + a_1 \sum x_i &= \sum y_i \\
a_0 \sum x_i + a_1 \sum x_i^2 &= \sum x_i\, y_i
\end{aligned}\right.
$$

> El profe aclara que el desarrollo con derivadas "no me calienta mucho que lo sepan"; lo
> que hay que saber armar es el sistema.

### Regla mnemotécnica — [11:33]

Pensar $n$ como $\sum x_i^0$ y $\sum y_i$ como $\sum x_i^0 y_i$:

$$
\left\{\begin{aligned}
a_0 \sum x^0 + a_1 \sum x^1 &= \sum x^0\, y \\
a_0 \sum x^1 + a_1 \sum x^2 &= \sum x^1\, y
\end{aligned}\right.
$$

- **De izquierda a derecha** el exponente de $x$ sube de a 1.
- **Cada ecuación arranca un grado más arriba** que la anterior (el $\sum x^1$ aparece
  "cruzado": fin de la 1ª fila, principio de la 2ª).
- En el **segundo miembro**, siempre $y$ a la 1, multiplicada por $x^0, x^1, x^2, \dots$ de
  arriba hacia abajo.
- Es la misma lógica que después se usa para parábolas, cúbicas, etc.

<details>
<summary>📝 Ejemplo 1 — 13:40: recta de mínimos cuadrados con 5 puntos (tabla, sistema, Excel)</summary>

Tabla de 5 puntos (la parte "amarilla" del Excel). Los $x$ son $1;\ 1{,}2;\ 2;\ 2{,}5;\ 2{,}9$.
De los $y$ se dictan $y_1 = 2{,}6$ e $y_2 = 3{,}8$; el resto [paso en el pizarrón, ver video].
Hallar la recta de mínimos cuadrados.

<details>
<summary>Ver resolución</summary>

**Paso 1:** ver qué hace falta para el sistema: $n$, $\sum x$, $\sum y$, $\sum x^2$,
$\sum x y$. A la tabla de datos se le **agregan columnas** ($x^2$, $x\cdot y$) y a cada
columna se le calcula la sumatoria.

**Paso 2:** sumatorias que da el profe:

$$
n = 5,\qquad \sum x = 9{,}6,\qquad \sum y = 26{,}7,\qquad \sum x^2 = 21{,}1,\qquad \sum x\,y = 58{,}51
$$

($\sum x^2 = 1 + 1{,}44 + 4 + 6{,}25 + 8{,}41 = 21{,}1$.)

**Paso 3:** armar el sistema 2×2:

$$
\left\{\begin{aligned}
5\,a_0 + 9{,}6\,a_1 &= 26{,}7 \\
9{,}6\,a_0 + 21{,}1\,a_1 &= 58{,}51
\end{aligned}\right.
$$

**Paso 4:** resolver con el método que quieran (sustitución, Cramer, calculadora). Consejo
del profe: trabajar con **4 o 5 decimales**. En Excel se resuelve en forma matricial:

$$
A\,X = B \;\Rightarrow\; A^{-1}A\,X = A^{-1}B \;\Rightarrow\; X = A^{-1}B
$$

**Paso 5:** resultado:

$$
a_0 = 0{,}12548\ldots \qquad a_1 = 2{,}71589\ldots \qquad\Rightarrow\qquad y = 0{,}12548 + 2{,}71589\,x
$$

**Paso 6 (control):** en Excel, gráfico de dispersión → *agregar línea de tendencia* →
lineal → *mostrar ecuación*: da exactamente la misma recta.

</details>

</details>

## 3. $y$ ajustado y error cuadrático — [20:42]

- **$y$ ajustado** ($\hat y_i$): cada $x_i$ evaluado en la función hallada.
- **Error cuadrático de cada punto:** $(y_i - \hat y_i)^2$. **Error cuadrático total:** la
  suma de esa columna.
- En el ejemplo: $\hat y(1) = 2{,}84$ contra $y = 2{,}6$; $\hat y(1{,}2) = 3{,}38$ contra
  $y = 3{,}8$ (error $\approx 0{,}17$); la **suma da $0{,}39$**.
- Si está bien hecho, **no existe otra recta** con error cuadrático menor: es la que más
  cerca pasa de los puntos.

## 4. Cuándo conviene otro modelo — [22:23]

- El ajuste sirve sobre todo **si ya sé qué tipo de función sigue el fenómeno**. Ejemplo:
  COVID. La propagación de un virus responde a una **función logística** (forma de S con
  asíntota horizontal); con los contagios de las semanas 1, 2, 3… se ajusta una logística y
  se predice la semana 38.
- Si sé que un fenómeno físico, biológico, económico o social responde a cierto tipo de
  función, **siempre es mejor usar ese tipo** de ajuste y no el lineal.
- Si no tengo idea del comportamiento, **la lineal muchas veces "queda bien parada"**.

## 5. Modelo exponencial — [24:56]

$$
y = a_0\, e^{a_1 x}
$$

- Si se minimiza $E = \sum (y_i - a_0 e^{a_1 x_i})^2$ derivando, las incógnitas quedan **en
  el exponente o al cuadrado**: el sistema es muy complicado ("no tenemos las herramientas"
  para resolverlo a mano). No se resuelve así.

### Forma aparentemente lineal — [27:36]

El truco: **aplicar logaritmo a ambos miembros** (regla general: si hay exponentes,
logaritmos):

$$
\ln y = \ln a_0 + a_1\, x
$$

Es "aparentemente lineal" porque tiene la forma *(algo con $y$) = (constante sin $x$) +
(coeficiente)·(algo con $x$)*. Se renombra:

$$
\underbrace{\ln y}_{Y} = \underbrace{\ln a_0}_{A_0} + a_1\, x
$$

Se toma el sistema de la recta y **se reemplaza lo que cambió** ($y \to \ln y$,
$a_0 \to A_0$); lo que no cambió ($x$, $a_1$, $n$) queda igual:

$$
\left\{\begin{aligned}
A_0\, n + a_1 \sum x_i &= \sum \ln y_i \\
A_0 \sum x_i + a_1 \sum x_i^2 &= \sum x_i \ln y_i
\end{aligned}\right.
$$

Del sistema sale $A_0$ (no es el objetivo) y $a_1$ (ya listo). Se vuelve con:

$$
a_0 = e^{A_0}
$$

> **Receta general (el profe la repite para todos los modelos):** llevar la función a forma
> aparentemente lineal → tomar el sistema de la recta → reemplazar lo que cambió, dejar lo
> que no → resolver → volver a los coeficientes originales.

<details>
<summary>📝 Ejemplo 2 — 31:27: ajuste exponencial de los mismos 5 puntos</summary>

Con los mismos 5 puntos del ejemplo 1, ajustar $y = a_0 e^{a_1 x}$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** se **reutilizan** $n = 5$, $\sum x = 9{,}6$ y $\sum x^2 = 21{,}1$: la matriz de
coeficientes no cambia, solo cambia la de términos independientes.

**Paso 2:** columnas nuevas: $\ln y$ y $x \ln y$. Sumatorias: $\sum \ln y = 7{,}97\ldots$ y
$\sum x \ln y = 16\ldots$ [poco claro en la transcripción: los decimales no se dictan].

**Paso 3:** resolver el sistema → $A_0$ y $a_1$. Cuidado: lo que se busca es $a_0$
minúscula, así que $a_0 = e^{A_0}$.

**Paso 4:** resultado: $a_0 \approx 1{,}71$ y el exponente "$0{,}50$ y pico" (en otro momento
lo lee como $0{,}54$) [poco claro en la transcripción]:

$$
y \approx 1{,}71\, e^{0{,}5\ldots\, x}
$$

**Paso 5 (control):** Excel → línea de tendencia **exponencial** → mostrar ecuación: da lo
mismo. (Excel también usa la forma aparentemente lineal.)

</details>

</details>

### La forma linealizada NO es la mejor exponencial — [34:40]

- Si se resuelve con Wolfram el sistema "posta" (el difícil), da **otra** exponencial,
  ligeramente distinta. Su error cuadrático es $0{,}59$ contra $0{,}67$ de la nuestra.
- O sea: linealizando **no se encuentra la mejor de todas las exponenciales**, porque se
  minimiza el error de $\ln y$, no el de $y$. Pero el resultado es bastante bueno, el cálculo
  es muchísimo más fácil y se puede hacer a mano. **Siempre se pide la versión
  aparentemente lineal** (es la que usa Excel).

## 6. Modelo potencial — [37:17]

$$
y = a_0\, x^{a_1}
$$

Mismo problema que el exponencial; se aplica logaritmo:

$$
\ln y = \ln a_0 + a_1 \ln x \qquad\Rightarrow\qquad
\underbrace{\ln y}_{Y} = \underbrace{\ln a_0}_{A_0} + a_1 \underbrace{\ln x}_{X}
$$

Cambiaron $y$, $x$ y $a_0$; quedan intactos $n$ y $a_1$:

$$
\left\{\begin{aligned}
A_0\, n + a_1 \sum \ln x_i &= \sum \ln y_i \\
A_0 \sum \ln x_i + a_1 \sum \big[\ln x_i\big]^2 &= \sum \ln x_i \ln y_i
\end{aligned}\right.
$$

- **Cuidado [40:26]:** es $\sum [\ln x_i]^2$ (el logaritmo, todo al cuadrado), **no**
  $\sum \ln(x_i^2)$. El profe usa corchetes para no confundir.
- Al final, de nuevo $a_0 = e^{A_0}$.

<details>
<summary>📝 Ejemplo 3 — 41:28: ajuste potencial y primera comparación de errores</summary>

Con los mismos 5 puntos, ajustar $y = a_0 x^{a_1}$ y comparar con los anteriores.

<details>
<summary>Ver resolución</summary>

**Paso 1:** columnas nuevas: $\ln x$, $[\ln x]^2$, $\ln y$, $\ln x \cdot \ln y$, con sus
sumatorias.

**Paso 2:** armar el sistema, resolver, $a_0 = e^{A_0}$. Los coeficientes finales
[paso en el pizarrón, ver video]. Excel también lo tiene (línea de tendencia
**potencial**/*power*).

**Paso 3:** comparar errores cuadráticos:

| Modelo | Error cuadrático |
|---|:---:|
| Lineal | $0{,}392$ |
| Potencial | $0{,}395$ |
| Exponencial | $0{,}67$ (el peor) |

En el tramo de los datos la potencial "parece casi lineal", por eso dan parecido. Los
puntos del ejemplo son al azar, así que el ganador es casualidad; pero muestra que **la
lineal, tan simple, queda muy bien parada**.

</details>

</details>

## 7. Modelos que se linealizan invirtiendo — [45:39]

### Hiperbólico

$$
y = \frac{a_1}{a_0 + x}
$$

Acá no hay logaritmos: se **invierten ambos miembros** y se distribuye:

$$
\frac{1}{y} = \frac{a_0 + x}{a_1} = \underbrace{\frac{a_0}{a_1}}_{A_0} + \underbrace{\frac{1}{a_1}}_{A_1}\, x
$$

- Cambiaron $y \to 1/y$ y los dos coeficientes; **la $x$ queda igual**, así que $n$,
  $\sum x$, $\sum x^2$ no cambian. El segundo miembro pasa a $\sum \frac{1}{y_i}$ y
  $\sum \frac{x_i}{y_i}$.
- **Vuelta (primero $a_1$, después $a_0$):**

$$
a_1 = \frac{1}{A_1}, \qquad a_0 = A_0 \cdot a_1
$$

- En el ejemplo de la clase da $y = \dfrac{-8{,}24}{-3{,}70 + x}$ (graficado en GeoGebra:
  Excel no tiene este modelo).

### Crecimiento con saturación — [49:55]

$$
y = \frac{a_0\, x}{a_1 + x}
$$

(Es parecida a la hiperbólica pero con $x$ en el numerador; responde, por ejemplo, a cierto
crecimiento de bacterias.) Invirtiendo y distribuyendo:

$$
\frac{1}{y} = \frac{a_1}{a_0}\cdot\frac{1}{x} + \frac{1}{a_0}
$$

- Acá **cambia todo** respecto de la recta: $X = \frac{1}{x}$, $Y = \frac{1}{y}$ y los dos
  coeficientes son "mayúsculas". Lo único firme es $n$.
- Columnas: $\frac{1}{x}$, $\frac{1}{x^2}$, $\frac{1}{y}$, $\frac{1}{x y}$.
- Vuelta: $a_0 = 1/A_0$ y $a_1 = A_1 \cdot a_0$. En el ejemplo da "números bastante feos"
  (el profe nombra un $-275$) [poco claro en la transcripción]; tampoco está en Excel.

## 8. Ajuste por un polinomio de grado n — [53:12]

$$
P_n(x) = a_0 + a_1 x + a_2 x^2 + \cdots + a_n x^n
$$

Hay que derivar respecto de cada $a_k$: queda un sistema de **$n+1$ ecuaciones normales con
$n+1$ incógnitas**, con la misma simetría que la recta:

$$
\left\{\begin{aligned}
a_0 \sum x^0 + a_1 \sum x^1 + \cdots + a_n \sum x^n &= \sum x^0\, y \\
a_0 \sum x^1 + a_1 \sum x^2 + \cdots + a_n \sum x^{n+1} &= \sum x^1\, y \\
&\;\;\vdots \\
a_0 \sum x^n + a_1 \sum x^{n+1} + \cdots + a_n \sum x^{2n} &= \sum x^n\, y
\end{aligned}\right.
$$

Exponentes del primer miembro: fila 1 → $0,1,2,\dots$; fila 2 → $1,2,3,\dots$; fila 3 →
$2,3,4,\dots$ Segundo miembro: $y$ por $x^0, x^1, x^2, \dots$ de arriba hacia abajo.

<details>
<summary>📝 Ejemplo 4 — 57:25: parábola de mínimos cuadrados</summary>

Con los mismos 5 puntos, ajustar $y = a_0 + a_1 x + a_2 x^2$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** tres incógnitas → sistema 3×3 (las tres primeras filas y columnas del sistema
general):

$$
\left\{\begin{aligned}
a_0\, n + a_1 \sum x + a_2 \sum x^2 &= \sum y \\
a_0 \sum x + a_1 \sum x^2 + a_2 \sum x^3 &= \sum x\, y \\
a_0 \sum x^2 + a_1 \sum x^3 + a_2 \sum x^4 &= \sum x^2\, y
\end{aligned}\right.
$$

**Paso 2:** agregar columnas $x^3$, $x^4$, $x^2 y$ (las de $x$, $x^2$, $y$, $xy$ ya
estaban). Se reemplaza: $n = 5$, $\sum x = 9{,}6$, $\sum x^2 = 21{,}1$, $\sum y = 26{,}7$,
etc. [el resto de los valores, paso en el pizarrón, ver video].

**Paso 3:** resolver. Como no hubo ningún cambio de variable, $a_0, a_1, a_2$ **van directo**
a la parábola. Excel: línea de tendencia **polinómica**, orden 2: da lo mismo.

</details>

</details>

### Grado alto → aparece el polinomio interpolante — [1:01:34]

- En Excel, subiendo el orden a 3 y después a 4, con 4 la curva **pasa exactamente por los
  5 puntos**: es el **polinomio interpolante** (un alumno lo responde).
- Por el teorema de interpolación (Lagrange): con 5 puntos existe y es único el polinomio de
  grado $\le 4$ que los interpola. Entonces, probando grados 1, 2, 3, 4, **sí o sí** en
  alguno aparece el interpolante (acá en el 4; según los puntos podría ser antes).
- Es una prueba de que el método anda bien: el mínimo error cuadrático posible es **cero**,
  y si existe un polinomio con error cero, el método lo tiene que devolver.

### Comparación de todos los modelos — [1:05:12]

Con los 5 puntos del ejemplo, el **mejor fue la cuadrática** (error $\approx 0{,}38$) y el
peor la hiperbólica, "aunque queda demasiado lejos": el profe sospecha que está mal
calculada y dice que lo va a revisar. Sirve para ver que **hay tipos de funciones que
ajustan mejor que otras**.

## 9. Ajuste continuo — [1:05:44]

- **Discreto:** cantidad **finita** de puntos (5 o 10 millones, da igual: es finita).
- **Continuo:** me dan un **pedazo de curva** $f(x)$ en un intervalo $[a,b]$ (infinitos
  puntos) y busco la función (recta, parábola…) que más cerca pasa de ese trozo.
- Lo discreto va con **sumatorias**; lo continuo con **integrales**. El error a minimizar:

$$
E = \int_a^b \big(f(x) - P_n(x)\big)^2\, dx
$$

El sistema es el mismo de los polinomios, con **dos cambios**:

1. Cada $\sum x^k$ pasa a ser $\int_a^b x^k\,dx$. En particular $\sum x^0 = n$ pasa a ser
   $\int_a^b dx = b - a$ (**la longitud del intervalo** reemplaza a la cantidad de puntos).
2. Cada $\sum x^k y$ pasa a ser $\int_a^b x^k f(x)\,dx$.

$$
\left\{\begin{aligned}
a_0 \int_a^b dx + a_1 \int_a^b x\,dx + \cdots &= \int_a^b f(x)\,dx \\
a_0 \int_a^b x\,dx + a_1 \int_a^b x^2\,dx + \cdots &= \int_a^b x\,f(x)\,dx \\
&\;\;\vdots
\end{aligned}\right.
$$

Las integrales del primer miembro son siempre de $x^k$ (fáciles); las que se complican son
las del segundo miembro, que dependen de $f$.

<details>
<summary>📝 Ejemplo 5 — 1:12:38: recta continua para e^x en [1, 2]</summary>

Hallar la recta de mínimos cuadrados que aproxima a $f(x) = e^x$ en $[1, 2]$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** sistema con integrales:

$$
\left\{\begin{aligned}
a_0 \int_1^2 dx + a_1 \int_1^2 x\,dx &= \int_1^2 e^x\,dx \\
a_0 \int_1^2 x\,dx + a_1 \int_1^2 x^2\,dx &= \int_1^2 x\,e^x\,dx
\end{aligned}\right.
$$

**Paso 2:** calcular las integrales (las de $e^x$ están en la tabla):

$$
\int_1^2 dx = 1,\quad \int_1^2 x\,dx = \tfrac{3}{2},\quad \int_1^2 x^2\,dx = \tfrac{7}{3},\quad
\int_1^2 e^x\,dx = e^2 - e,\quad \int_1^2 x\,e^x\,dx = e^2
$$

**Paso 3:** resolver el 2×2:

$$
y = -2{,}22 + 4{,}5\ldots\,x
$$

**Paso 4:** gráficamente la recta pasa "promediando" por el medio de la curva. El error
cuadrático ahora es una integral, $\int_1^2 (e^x - (a_0 + a_1 x))^2 dx$, más difícil de
calcular (el profe lo hizo con Wolfram; **no se va a pedir**).

</details>

</details>

> **Consulta [1:16:45]: ¿a mano o en Excel?** Puede haber ejercicios con muchos puntos que
> obliguen a usar Excel, pero en el examen se toma **a mano** con pocos puntos (4, 5, 6).
> Consejo: cuando son pocos puntos, practicar a mano.

<details>
<summary>📝 Ejemplo 6 — 1:17:53: parábola continua para e^x en [1, 2]</summary>

Mismo trozo de $e^x$ en $[1,2]$, ahora con una parábola.

<details>
<summary>Ver resolución</summary>

**Paso 1:** sistema 3×3 con integrales de $x^0 \ldots x^4$ en el primer miembro y
$\int_1^2 x^k e^x dx$ ($k = 0,1,2$) en el segundo.

**Paso 2:** resolver → tres coeficientes [paso en el pizarrón, ver video]. El ajuste es tan
bueno que en Wolfram cuesta encontrar diferencias visuales entre la parábola y $e^x$; el
error cuadrático da $0{,}30\ldots$ "y ahí arranca con un 2" [poco claro en la transcripción:
se entiende que es un número muy chico].

</details>

</details>

## 10. Ajuste continuo con polinomios ortogonales — [1:19:27]

- Es **otro método** para el mismo ajuste continuo. Como también minimiza el error
  cuadrático, **llega a la misma función** (igual que Lagrange y Newton-Gregory llegan al
  mismo interpolante). Elegir uno u otro es cuestión de criterio y comodidad.
- Su gracia: **evita el sistema de ecuaciones** (que con 10×10 o 100×100 se vuelve
  imposible). "Tampoco es súper simpático", avisa el profe.

**Funciones ortogonales.** $\varphi_0, \varphi_1, \dots, \varphi_n$ son ortogonales en
$[a,b]$ si y solo si su **producto interno** es cero para funciones distintas:

$$
\langle \varphi_i, \varphi_j \rangle = \int_a^b \varphi_i(x)\,\varphi_j(x)\,dx = 0 \qquad (i \ne j)
$$

Si $i = j$ la integral **no** da cero; se llama **norma**:

$$
\lVert \varphi_k \rVert = \int_a^b \varphi_k(x)^2\,dx
$$

(Si diera 1 sería una base ortonormal, como en Fourier; acá no da 1, es solo ortogonal.)

### Fórmula de los coeficientes — [1:26:48]

El polinomio de ajuste se escribe como **combinación lineal** de polinomios ortogonales:

$$
P_n(x) = a_0\,\varphi_0(x) + a_1\,\varphi_1(x) + \cdots + a_n\,\varphi_n(x)
$$

Al derivar el error respecto de cada $a_k$ y distribuir, todos los productos
$\varphi_k \varphi_i$ con $i \ne k$ se anulan por ortogonalidad. Sobreviven solo
$\int \varphi_k f$ y la norma, y queda una **fórmula directa** para cada coeficiente,
**independiente de los demás**:

$$
a_k = \frac{1}{\lVert \varphi_k \rVert}\int_a^b f(x)\,\varphi_k(x)\,dx
$$

## 11. Polinomios de Legendre — [1:29:23]

- Son ortogonales **solo en $[-1, 1]$**.
- Se definen por una fórmula recurrente; se usan **los tres primeros** (son datos para
  memorizar, no hay que deducirlos):

$$
\varphi_0(x) = 1, \qquad \varphi_1(x) = x, \qquad \varphi_2(x) = \tfrac{1}{2}\big(3x^2 - 1\big)
$$

- Norma: $\lVert \varphi_k \rVert = \dfrac{2}{2k+1}$, así que la constante que va adelante de la
  integral es:

$$
\frac{1}{\lVert \varphi_k \rVert} = \frac{2k+1}{2}: \qquad \tfrac{1}{2},\ \tfrac{3}{2},\ \tfrac{5}{2},\ \tfrac{7}{2},\ \dots
$$

  (arranca en $\frac12$ y sube de a 1). El profe no recuerda si está en la hoja de fórmulas.

<details>
<summary>📝 Ejemplo 7 — 1:33:07: recta de Legendre para e^x en [-1, 1]</summary>

Hallar la recta de mínimos cuadrados para $f(x) = e^x$ en $[-1, 1]$ con polinomios de
Legendre.

<details>
<summary>Ver resolución</summary>

**Paso 1:** $P_1(x) = a_0\varphi_0(x) + a_1\varphi_1(x) = a_0 + a_1 x$.

**Paso 2:** $a_0$ por fórmula, sin sistema:

$$
a_0 = \frac{1}{2}\int_{-1}^{1} e^x \cdot 1\,dx = \frac{e - e^{-1}}{2} \approx 1{,}1752
$$

**Paso 3:** $a_1$, independiente de $a_0$:

$$
a_1 = \frac{3}{2}\int_{-1}^{1} e^x \cdot x\,dx = \frac{3}{e} \approx 1{,}1036
$$

**Paso 4:**

$$
P_1(x) = 1{,}1752 + 1{,}1036\,x
$$

</details>

</details>

### Ventaja: agregar grados — [1:35:55]

Si después piden la **parábola**, $a_0$ y $a_1$ **no cambian**; solo se calcula

$$
a_2 = \frac{5}{2}\int_{-1}^{1} e^x \cdot \tfrac{1}{2}\big(3x^2-1\big)\,dx
$$

y se agrega el término $a_2\varphi_2(x)$. Con el método del sistema habría que rehacer todo
(un 3×3 nuevo).

<details>
<summary>📝 Ejemplo 8 — 1:38:38: Legendre fuera de [-1,1], cambio de variable (e^x en [1,2])</summary>

Rehacer el ejemplo 5 ($e^x$ en $[1,2]$, recta y parábola) con Legendre. Debe dar lo mismo
que por el sistema.

<details>
<summary>Ver resolución</summary>

**Paso 1:** cambio de variable para que $t \in [-1,1]$ cuando $x \in [1,2]$. El profe no
memoriza la fórmula: dibuja $t$ en el eje horizontal ($-1$ a $1$) y $x$ en el vertical ($a$
a $b$) y traza la recta de la esquina inferior izquierda a la superior derecha. Ordenada al
origen = promedio $\frac{a+b}{2}$; pendiente $= \frac{b-a}{1-(-1)} = \frac{b-a}{2}$:

$$
x = \frac{a+b}{2} + \frac{b-a}{2}\,t \quad\Rightarrow\quad x = \frac{3}{2} + \frac{1}{2}\,t, \qquad t = 2x - 3
$$

**Paso 2:** trabajar con $f(t) = e^{\frac32 + \frac12 t}$ en $[-1,1]$, con
$\varphi_0(t) = 1$, $\varphi_1(t) = t$, $\varphi_2(t) = \frac12(3t^2-1)$:

$$
a_0 = \frac{1}{2}\int_{-1}^{1} e^{\frac32 + \frac12 t}\,dt \approx 4{,}6
\qquad
a_1 = \frac{3}{2}\int_{-1}^{1} e^{\frac32 + \frac12 t}\; t\,dt \approx 2{,}29
$$

**Paso 3:** volver a $x$ reemplazando $t = 2x - 3$ en $P_1(t) = a_0 + a_1 t$, distribuir y
agrupar:

$$
y = -2{,}22 + 4{,}5\ldots\,x
$$

que es **lo mismo** que por el sistema de ecuaciones.

**Paso 4 (parábola):** agregar

$$
a_2 = \frac{5}{2}\int_{-1}^{1} e^{\frac32 + \frac12 t}\cdot\tfrac12\big(3t^2-1\big)\,dt \approx 0{,}38
$$

sumar $a_2\varphi_2(t)$, distribuir y reemplazar $t = 2x-3$ de nuevo. Es largo y tedioso,
pero llega a lo mismo que por el sistema [coeficientes finales en el pizarrón, ver video].

</details>

</details>

## 12. Cierre — [1:47:05]

- **Legendre:** cada coeficiente es independiente → fácil agregar grados. **Contras:**
  integrales que se complican, recordar los polinomios, y el cambio de intervalo.
- En la práctica se repiten todos los modelos discretos con números (cómo llevar cada
  función a forma lineal, qué columnas agregar, qué sumatorias, cómo armar el sistema) y
  ejemplos de ajuste continuo.
