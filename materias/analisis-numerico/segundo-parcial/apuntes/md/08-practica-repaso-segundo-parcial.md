# Práctica — repaso del 2do parcial

> Fuente: `fuentes/clases/repaso segundo parcial/OneNote - Repaso Segundo Parcial.pdf` (15 páginas: enunciados tipeados o fotografiados + resolución manuscrita del profesor). La clase grabada está en Drive con la descarga bloqueada, así que no hay transcripción: todo sale del OneNote.

---

> **Cómo usarla:** son los 15 ejercicios que el profesor resolvió en el repaso, en el orden del OneNote. Abrí el ejercicio, leé el enunciado y **hacelo en papel con reloj** (el tiempo sugerido está en cada título) antes de abrir la resolución. Solo ayudamemoria oficial (pág. 4) y calculadora, como en el parcial.
> **Qué es del profesor y qué no:** las resoluciones están transcriptas del manuscrito. Lo que agregué yo está marcado `(cuenta intermedia agregada)`; lo que no se lee, `[poco claro en el manuscrito]`. La línea **Qué mirar** al final de cada ejercicio es mía: el error típico o la frase que hay que escribir para que el ítem esté completo.
> **Verificación:** todos los números se rehicieron con Python (numpy/sympy). Hay **una discrepancia** (la planilla de punto fijo del ejercicio 2, marcada con ⚠) y dos redondeos menores; ninguno cambia una respuesta.
> **Gemelos:** la columna "se parece a" cruza cada ejercicio con las 4 hojas de 2025 de `examenes/INDICE.md` (T1/T2 = parcial Tema 1/2, R1/R2 = 1er/2do recuperatorio).

## Mapa de la práctica

| # | Tema | Tipo de ítem | Se parece a (2025) | Entra |
|---|---|---|---|---|
| 1 | Raíces | Cantidad de iteraciones de bisección, ¿suficientes o necesarias? `#Biseccion` `#CotaIteraciones` | **T1 Ej1c** (misma cuenta: $10^{-7}$ → 25) y **R2 Ej1c** ($10^{-5}$ → 18) | 🔴 |
| 2 | Raíces | Multiple choice: ubicar la raíz, unicidad, Regula Falsi, condiciones de punto fijo, Newton-Raphson `#SepararRaices` `#PuntoFijo` `#NewtonRaphson` | **T2 Ej1** (separar + condiciones de una $g$ + N-R), **R1 Ej1b** (elegir $g$) | 🔴 |
| 3 | Interpolación | Hallar $k$ para que el interpolante sea de grado 2 + cuántos valores de $k$ dan grado 3 / 4 `#GradoPolinomio` `#DiferenciasDivididas` `#CantidadPolinomios` | **R1 Ej3a** y **R2 Ej3a** (menor grado posible), **R2 Ej3b** | 🔴 |
| 4 | Interpolación | Hallar $h$ y $a$ para grado 3 + polinomio + cuántos polinomios de cada grado + 2da derivada numérica `#GradoPolinomio` `#DiferenciasDivididas` `#CantidadPolinomios` | **T2 Ej3a** (grado 3 + hallar el polinomio), **T1 Ej3b**, **R1 Ej3b/c** | 🔴 |
| 5 | Ajuste (continuo) | Mínimos cuadrados continuo: recta por Legendre, parábola por el método tradicional (sin tag en la leyenda) | — (ninguna hoja 2025 lo toma) | ⚪ no entra en el 2P 2026 |
| 6 | Sistemas lineales | Reordenar para diagonal dominante + $T$ de Jacobi + convergencia por $\lVert T\rVert_\infty$ `#DiagonalDominante` `#Jacobi` `#ConvergenciaIterativos` | **R2 Ej2b** (reordenar), **R1 Ej2** (diagonal dominante), **T1/T2 Ej2** (¿converge Jacobi?) | 🔴 |
| 7 | Interpolación + diferenciación | Grado y polinomio de Newton-Gregory + $f''(4)$ con la fórmula central `#GradoPolinomio` `#DiferenciasDivididas` | **T2 Ej3a**, **R2 Ej3b** (la derivada numérica no tiene gemelo 2025) | 🟠 |
| 8 | Interpolación / diferenciación | Multiple choice conceptual: interpolar o aproximar; qué fórmula de derivada usar | — (sin gemelo 2025) | 🟡 |
| 9 | Integración | Multiple choice: ¿cuándo Simpson da el valor exacto? `#Simpson` | **R2 Ej4b** (lejano: ¿se puede usar Simpson?) | 🟡 |
| 10 | Integración | V/F: Trapecios por defecto o por exceso; ¿Simpson con $h = 0{,}08$? `#Trapecios` `#Simpson` | **R2 Ej4b** (mismo criterio: $N$ par) | 🟠 |
| 11 | Integración | Mayor $h$ racional no periódico para Trapecios (+ variante Simpson) `#Trapecios` `#EleccionH` `#Simpson` | **T1 Ej4, T2 Ej4, R1 Ej4, R2 Ej4a** (4/4, misma consigna) | 🔴 |
| 12 | Ecuaciones diferenciales | Clasificar una fórmula: explícita/implícita, cantidad de pasos `#Multipaso` | **R2 Ej5b** | 🟠 |
| 13 | Ecuaciones diferenciales | Constante de Lipschitz en un rectángulo `#Lipschitz` | **T1 Ej5a**, **T2 Ej5a** | 🔴 |
| 14 | Ajuste (discreto) | Exponencial de mínimos cuadrados `#AjusteExponencial` | **T2 Ej3b**, **R2 Ej3c** | ⚪ no entra en el 2P 2026 |
| 15 | Sistemas lineales | Número de condición con norma infinito `#NumeroCondicion` | **R2 Ej2a** (es la **misma matriz** con las filas 1 y 2 intercambiadas) | 🟠 |

**Lectura rápida:** el repaso no tiene ningún ejercicio de Euler / Heun / RK4 (el Ej5 del parcial); de ecuaciones diferenciales solo hay Lipschitz y la fórmula multipaso. Eso se practica con la guía de EDO y con las hojas 2025.

---

## 1) Raíces — iteraciones de bisección · 8 min

<details>
<summary><strong>Ejercicio 1 — enunciado</strong></summary>

Sea $f(x) = x^4 - 8x^3 + 30x^2 - 25x + 2 - 12e^{-x}$ con una raíz en el intervalo $[a-1,\ a+1]$. Para asegurar un error menor que $10^{-7}$ por el método de bisección (sin aplicar el método):

- a) Son necesarias 23 iteraciones
- b) Son suficientes 24 iteraciones
- c) La cantidad de iteraciones suficientes depende de $f(x)$
- d) Son suficientes 23 iteraciones
- e) La cantidad de iteraciones suficientes depende del valor inicial
- f) n.a.

<details>
<summary><strong>Resolución 1</strong></summary>

**Paso 1 — la función no importa.** No importa la función (siempre y cuando cumpla con Bolzano en el intervalo). La cota de bisección solo usa la longitud del intervalo:

$$
\frac{b-a}{2^{i}} < \varepsilon
$$

**Paso 2 — reemplazar el intervalo** $[a-1,\ a+1]$:

$$
\frac{(a+1)-(a-1)}{2^{i}} < 10^{-7}
\quad\Longrightarrow\quad
\frac{2}{2^{i}} < 10^{-7}
\quad\Longrightarrow\quad
2^{\,1-i} < 10^{-7}
$$

**Paso 3 — despejar $i$ con logaritmo decimal:**

$$
(1-i)\cdot\log_{10}2 < -7
\quad\Longrightarrow\quad
1-i < \frac{-7}{\log_{10}2}
\quad\Longrightarrow\quad
1+\frac{7}{\log_{10}2} < i
$$

$$
i > 24{,}25349 \quad\Longrightarrow\quad i \geq 25
$$

**Paso 4 — redondeo.** No se puede partir iteraciones por la mitad: siempre tomar el primer $i$ entero que cumpla.

**Paso 5 — ¿suficientes o necesarias?** El método nos asegura la precisión para esa cantidad de iteraciones, pero no quiere decir que no podamos conseguirla antes. Son **suficientes**.

**Respuesta:** son suficientes 25 iteraciones ⇒ ninguna opción lo dice ⇒ **f) N.A.**

> Verificado: $1 + 7/\log_{10}2 = 24{,}2535$.

**Qué mirar:** la longitud del intervalo es **2**, no 1 (es $[a-1, a+1]$): si usás 1 te da 24 y marcás la b). Y hay que escribir las dos cosas: el entero **siguiente** (25) y la palabra **"suficientes"** con su porqué (la cota garantiza el error, pero se puede alcanzar antes).

</details>

</details>

## 2) Raíces — multiple choice con $\operatorname{sen}(4x)+3x+3=0$ · 20 min

<details>
<summary><strong>Ejercicio 2 — enunciado</strong></summary>

Dada la ecuación $\operatorname{sen}(4x) + 3x + 3 = 0$:

- a) tiene por lo menos una raíz en el intervalo $[-1;\ 0]$
- b) se puede aplicar Regula Falsi en $[-2;\ -0{,}5]$ fijando el extremo $b = -0{,}5$
- c) tiene una sola raíz real
- d) el método de punto fijo converge con la función $g(x) = \operatorname{sen}(4x) + 4x + 3$
- e) ninguna es correcta

Decidí verdadero o falso para cada una, justificando.

<details>
<summary><strong>Resolución 2</strong></summary>

$$
f(x) = \operatorname{sen}(4x) + 3x + 3
$$

**Paso 1 — separar gráficamente (opción a).** Se parte la ecuación en dos funciones fáciles de dibujar:

$$
\operatorname{sen}(4x) = -3x - 3
$$

El profesor grafica en GeoGebra $\operatorname{sen}(4x)$ (verde) y la recta $-3x-3$ (roja): se cruzan **una sola vez**, y el cruce (la raíz) está en $[-2;\ -1]$.

- **a) Falsa:** la raíz no está en $[-1; 0]$.

> Verificado (cuenta intermedia agregada): $f(-2) = -3{,}9894$, $f(-1) = 0{,}7568$, $f(0) = 3$. Hay cambio de signo en $[-2;-1]$ y no en $[-1;0]$.

**Paso 2 — unicidad (opciones c y e).** Es única raíz real (no hay más cruces).

- **c) Verdadera.**
- **e) Falsa** (porque c es correcta).

**Paso 3 — Regula Falsi (opción b): ¿qué extremo fijar?** Hay que ver el crecimiento y la concavidad de $f(x)$ en el intervalo $[a,b]$:

$$
f'(x) = 4\cos(4x) + 3 \quad(\text{crecimiento}),\qquad f''(x) = -16\operatorname{sen}(4x)\quad(\text{concavidad})
$$

La regla del profesor: si $\operatorname{sg}(f') = \operatorname{sg}(f'')$ → se fija $b$. Tabla de planilla en $[-2;\ -0{,}5]$:

| $x$ | $f$ | $f'$ | $f''$ |
|---|---|---|---|
| $-2$ | $-3{,}9893582$ | $2{,}41799986$ | $15{,}8297319$ |
| $-0{,}9$ | $0{,}74252044$ | $-0{,}5870337$ | $-7{,}0803271$ |
| $-0{,}5$ | $0{,}59070257$ | $1{,}33541265$ | $14{,}5487588$ |

- **b) Falsa:** porque en $[-2;\ -0{,}5]$ hay cambio de crecimiento de $f'$ y $f''$ [la palabra "crecim." está abreviada en el manuscrito]: ni $f'$ ni $f''$ mantienen el signo en todo el intervalo, así que la regla del extremo fijo no se puede aplicar ahí.

> Verificado: los 9 valores de la tabla coinciden.

**Paso 4 — punto fijo (opción d).** La $g$ sale de sumar $x$ a los dos miembros:

$$
0 + x = \operatorname{sen}(4x) + 3x + 3 + x
\quad\Longrightarrow\quad
x = \operatorname{sen}(4x) + 4x + 3 = g(x)
$$

Trabajamos en $[-2;\ -1]$. Dos condiciones:

1. $\forall x_i \in [a,b]:\ \lvert g'(x_i)\rvert < 1$
2. $g(x_i) \in [a,b]\quad \forall x \in [a,b]$

Condición 1:

$$
g'(x) = 4\cos(4x) + 4
$$

Del gráfico de $g'$ (GeoGebra): $\nexists\, x_i \in [-2,-1]$ tal que $\lvert g'(x_i)\rvert < 1$. No se cumple la condición 1 ⇒ **no podemos asegurar que converge ni que no converge**.

> (cuenta intermedia agregada) En $[-2;-1]$ el mínimo de $g'$ está en $x=-1$: $g'(-1) = 4\cos(-4)+4 = 1{,}385 > 1$. O sea $\lvert g'\rvert > 1$ en **todo** el intervalo, y en la raíz $g'(-1{,}2966) = 5{,}83$.

**Paso 5 — probar iterando (planilla).** Como las condiciones no deciden, el profesor itera en Excel desde $x_0 = -2$:

| $x$ | $g(x)$ (planilla del profesor) |
|---|---|
| $-2$ | $-4{,}98936$ |
| $-4{,}98936$ | $-16{,}8522$ |
| $-16{,}8522$ | $-62{,}4179$ |
| $-62{,}4179$ | $-244{,}675$ |
| $-244{,}675$ | $-973{,}705$ |
| $-973{,}705$ | $-3890{,}14$ |
| $-3890{,}14$ | $-15556{,}3$ |
| $-15556{,}3$ | $-62221{,}5$ |
| $-62221{,}5$ | $-248882$ |
| $-248882$ | $-995526$ |
| $-995526$ | $-3982100$ |
| $-3982100$ | $-1{,}6\cdot10^{7}$ |
| $-1{,}6\cdot10^{7}$ | $-6{,}4\cdot10^{7}$ |
| $-6{,}4\cdot10^{7}$ | `#NUM!` |

No converge.

- **d) Falsa.**

> ⚠ **Discrepancia numérica.** Los valores de la planilla del profesor corresponden a $\operatorname{sen}(4x)+4x+\mathbf{4}$, no a la $g(x)=\operatorname{sen}(4x)+4x+3$ del enunciado (con $+4$ se reproducen exactos: $-4{,}9894;\ -16{,}8522;\ -62{,}4179;\ -244{,}675$). Con la $g$ del enunciado la sucesión es
>
> | $x$ | $g(x) = \operatorname{sen}(4x)+4x+3$ (Python) |
> |---|---|
> | $-2$ | $-5{,}9894$ |
> | $-5{,}9894$ | $-20{,}0346$ |
> | $-20{,}0346$ | $-76{,}1389$ |
> | $-76{,}1389$ | $-301{,}7335$ |
> | $-301{,}7335$ | $-1204{,}4675$ |
>
> La conclusión es la misma: diverge (se multiplica por ≈4 en cada paso). Quedan las dos tablas.

**Paso 6 — la raíz por Newton-Raphson** (recuadro del profesor):

$$
x_{i+1} = x_i - \frac{f(x_i)}{f'(x_i)} = x_i - \frac{\operatorname{sen}(4x_i) + 3x_i + 3}{4\cos(4x_i) + 3}
$$

| $x$ | $f$ | $f'$ |
|---|---|---|
| $-1{,}5$ | $-1{,}2205845$ | $6{,}84068115$ |
| $-1{,}3215697$ | $-0{,}1249138$ | $5{,}17161177$ |
| $-1{,}297416$ | $-0{,}003998$ | $4{,}83744168$ |
| $-1{,}2965895$ | $-4{,}857\cdot10^{-6}$ | $4{,}82568578$ |
| $-1{,}2965885$ | $-7{,}21\cdot10^{-12}$ | $4{,}82567145$ |
| $-1{,}2965885$ | $0$ | $4{,}82567145$ |
| $-1{,}2965885$ | $0$ | $4{,}82567145$ |

$$
\boxed{\,x \approx -1{,}2965885\,}
$$

> Verificado: las 7 filas coinciden.

**Respuestas:** a) F · b) F · **c) V** · d) F · e) F.

**Qué mirar:** (1) para el intervalo, mostrá el cambio de signo de $f$ en los extremos o el gráfico de las dos curvas; (2) en punto fijo escribí **las dos** condiciones ($\lvert g'\rvert<1$ en todo el intervalo y $g([a,b])\subset[a,b]$) y decí cuál falla; (3) que no se cumplan **no prueba** que diverge: el profesor lo dice así ("no podemos asegurar…") y recién después lo muestra iterando.

</details>

</details>

## 3) Interpolación — hallar $k$ para grado 2 · 12 min

<details>
<summary><strong>Ejercicio 3 — enunciado</strong></summary>

Dada la siguiente tabla de datos, completá:

| $x$ | $-2$ | $1$ | $3$ | $4$ | $6$ |
|---|---|---|---|---|---|
| $y$ | $26$ | $5$ | $k$ | $20$ | $50$ |

- a) Para que por todos los puntos dados pase un polinomio de grado 2, debe ser $k = \dots$
- b.1) Existen … valores de $k \in \mathbb{R}$ tal que por todos los puntos dados pase un polinomio de grado 3.
- b.2) Existen … valores de $k \in \mathbb{R}$ tal que por todos los puntos dados pase un polinomio de grado 4.

<details>
<summary><strong>Resolución 3</strong></summary>

**Paso 1 — diferencias divididas sin el punto desconocido.** Se saca $(3, k)$ y se arma la tabla con los puntos conocidos. Con tres alcanza para un grado 2:

| $x$ | $y$ | O1 | O2 |
|---|---|---|---|
| $-2$ | $26$ | | |
| | | $-7$ | |
| $1$ | $5$ | | $2$ |
| | | $5$ | |
| $4$ | $20$ | | |

(cuenta intermedia agregada) $\dfrac{5-26}{1-(-2)} = -7$, $\dfrac{20-5}{4-1} = 5$, $\dfrac{5-(-7)}{4-(-2)} = 2$.

**Paso 2 — polinomio de Newton.** El profesor: "Recomiendo: Newton-Gregory general, siempre".

$$
P(x) = 26 - 7(x+2) + 2(x+2)(x-1)
$$

**Paso 3 — controlar el punto que quedó afuera.** Si $P(6) \neq 50 \Rightarrow \nexists\, k$.

$$
P(6) = 26 - 7\cdot 8 + 2\cdot 8\cdot 5 = 50\ \checkmark
$$

**Paso 4 — hallar $k$:**

$$
k = P(3) = 26 - 7\cdot 5 + 2\cdot 5\cdot 2 = 11
$$

$$
\boxed{\,k = 11\,}
$$

**Variante regresiva** (anotada en azul, arrancando desde $x=4$ hacia atrás):

$$
P(x) = 20 + 5(x-4) + 2(x-4)(x-1)
$$

$$
P(6) = 20 + 5\cdot 2 + 2\cdot 2\cdot 5 = 50\ \checkmark
\qquad
P(3) = 20 + 5(-1) + 2(-1)\cdot 2 = 11
$$

**Paso 5 — b.1 y b.2.** Si $k = 11$, entonces grado 2. Si $k \neq 11$, entonces salta al grado 4.

- **b.1)** $\emptyset$ (**ningún**) valor de $k$ para un polinomio de grado 3.
- **b.2)** $\infty$ (**infinitos**) valores de $k$ para un polinomio de grado 4 (todo $k \neq 11$).

> Verificado: $P(3)=11$, $P(4)=20$, $P(6)=50$.

**Qué mirar:** el paso que se olvida es el 3: antes de dar $k$ hay que **comprobar que los otros 4 puntos ya están en la parábola** (si $P(6)\neq 50$ no existe ningún $k$). Y para b) la justificación es que mover un solo dato hace saltar el grado directo a 4: la última diferencia dividida es proporcional a $(k-11)$, o es cero (grado 2) o no lo es (grado 4); nunca queda en 3.

</details>

</details>

## 4) Interpolación — hallar $h$ y $a$ para grado 3, contar polinomios y 2da derivada · 20 min

<details>
<summary><strong>Ejercicio 4 — enunciado</strong></summary>

Dada la siguiente tabla de valores:

| $x$ | $1$ | $1{,}5$ | $2$ | $3$ | $3{,}5$ | $4$ |
|---|---|---|---|---|---|---|
| $y$ | $-4$ | $-4{,}125$ | $h$ | $6$ | $15{,}375$ | $h+a$ |

- a) Hallar el valor de $h$ y $a$ reales para que el polinomio interpolante que pase por todos los puntos sea de grado 3. Hallar dicho polinomio.
- b) Con el $h$ obtenido en el ítem anterior y $a = 10$: indicar cuántos polinomios hay de grado 2, grado 3, grado 4, grado 5 y grado 6. Justifique.
- c) Con el valor de $h$ hallado en el ítem a), calcule la 2da diferencia [derivada segunda numérica] en $x = 1{,}5$.

<details>
<summary><strong>Resolución 4</strong></summary>

**a) Paso 1 — diferencias divididas con los 4 puntos conocidos** ($x = 1;\ 1{,}5;\ 3;\ 3{,}5$):

| $x$ | $y$ | O1 | O2 | O3 |
|---|---|---|---|---|
| $1$ | $-4$ | | | |
| | | $-0{,}25$ | | |
| $1{,}5$ | $-4{,}125$ | | $3{,}5$ | |
| | | $6{,}75$ | | $1$ |
| $3$ | $6$ | | $6$ | |
| | | $18{,}75$ | | |
| $3{,}5$ | $15{,}375$ | | | |

(cuenta intermedia agregada) O1: $\frac{-4{,}125+4}{0{,}5}=-0{,}25$; $\frac{6+4{,}125}{1{,}5}=6{,}75$; $\frac{15{,}375-6}{0{,}5}=18{,}75$. O2: $\frac{6{,}75+0{,}25}{3-1}=3{,}5$; $\frac{18{,}75-6{,}75}{3{,}5-1{,}5}=6$. O3: $\frac{6-3{,}5}{3{,}5-1}=1$.

**Paso 2 — polinomio de Newton** (primer elemento de cada columna):

$$
P(x) = -4 - 0{,}25\,(x-1) + 3{,}5\,(x-1)(x-1{,}5) + (x-1)(x-1{,}5)(x-3)
$$

**Paso 3 — los puntos desconocidos tienen que caer sobre $P$:**

$$
P(2) = -3 \quad\Longrightarrow\quad \boxed{\,h = -3\,}
$$

$$
P(4) = 29 \quad\Longrightarrow\quad h + a = 29 \quad\Longrightarrow\quad a = 29 - h = 29 + 3 \quad\Longrightarrow\quad \boxed{\,a = 32\,}
$$

(cuenta intermedia agregada) $P(2) = -4 - 0{,}25 + 3{,}5\cdot 1\cdot 0{,}5 + 1\cdot 0{,}5\cdot(-1) = -3$; $P(4) = -4 - 0{,}75 + 3{,}5\cdot 3\cdot 2{,}5 + 3\cdot 2{,}5\cdot 1 = 29$. Distribuido (no hace falta): $P(x) = x^3 - 2x^2 - 3$.

**b) Con $h = -3$ y $a = 10$** el último punto es $(4;\ 7)$, que **no** está sobre $P$ ($P(4)=29$). Lo que anota el profesor sobre el enunciado:

| Grado | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|
| Cantidad de polinomios | $0$ | $0$ | $0$ | $1$ | $\infty$ |

(justificación agregada, el manuscrito solo trae los números) Por 6 puntos con abscisas distintas pasa un **único** polinomio de grado $\le 5$. Los 5 primeros puntos están sobre una cúbica y el sexto no, así que ese único polinomio tiene grado exactamente 5: no hay ninguno de grado 2, 3 ni 4. De grado 6 (o mayor) hay infinitos, porque sobra un coeficiente libre.

**c) Derivada segunda en $x = 1{,}5$** con los tres puntos equiespaciados ($h_{\text{paso}} = 0{,}5$):

| $x$ | $y$ |
|---|---|
| $1$ | $-4$ |
| $1{,}5$ | $-4{,}125$ |
| $2$ | $-3$ (el $h$ hallado) |

$$
f''(1{,}5) \approx \frac{-3 - 2\cdot(-4{,}125) + (-4)}{0{,}5^{2}} = 5
$$

> Verificado: tabla, $P(2)=-3$, $P(4)=29$ y la derivada ($\frac{1{,}25}{0{,}25}=5$). Como los datos son de la cúbica $x^3-2x^2-3$, el valor exacto es $P''(1{,}5)=6\cdot1{,}5-4=5$: la fórmula central no tiene error acá.

**Qué mirar:** (1) la tabla se arma **solo con los puntos conocidos** y la columna que tiene que quedar constante es la del grado pedido (O3); (2) ojo con la letra: en c) $h$ es el dato de la tabla y el paso es $0{,}5$, no los confundas; (3) en b) el conteo siempre es "0 por debajo del grado real, 1 en el grado del interpolante único (≤ n−1 con n puntos), ∞ de ahí para arriba", y hay que **escribir** la frase del polinomio único.

</details>

</details>

## 5) Ajuste continuo — mínimos cuadrados con Legendre · ⚪ no entra en el 2P 2026

<details>
<summary><strong>Ejercicio 5 — enunciado</strong> (guía, ejercicio 32 d — "C) Mínimos cuadrados - continuo")</summary>

Dadas las siguientes funciones continuas, aproxime por un polinomio de mínimos cuadrados en los intervalos indicados y grafique. Por lo menos resuelva 4 ítems utilizando los **polinomios de Legendre**:

d) $f(x) = e^{x}$ en $[0, 2]$ por una recta y por una parábola.

> ⚪ **No entra en el 2P 2026** (ajuste por mínimos cuadrados se evaluó con el TP). Queda transcripto porque está en el repaso; saltealo si vas justo de tiempo.

<details>
<summary><strong>Resolución 5</strong></summary>

El profesor hace la **recta por Legendre** y la **parábola por el método tradicional**.

### Recta por Legendre

**Paso 1 — llevar el intervalo a $[-1, 1]$.** Legendre necesita $[-1;1]$. Cambio de variable $x = \dfrac{a+b}{2} + \dfrac{b-a}{2}\,t$:

$$
[0;2] \to [-1;1]:\qquad x = t + 1,\qquad t = -1 + x,\qquad e^{x} = e^{t+1}
$$

**Paso 2 — base y coeficientes:**

$$
\varphi_0(t) = 1,\qquad \varphi_1(t) = t,\qquad y = a_0\,\varphi_0(t) + a_1\,\varphi_1(t)
$$

$$
a_i = \frac{1}{\lVert\varphi_i(t)\rVert}\int_{-1}^{1} f(t)\,\varphi_i(t)\,dt,
\qquad
\frac{1}{\lVert\varphi_m(t)\rVert} = \frac12,\ \frac32,\ \frac52,\ \frac72,\ \dots
$$

**Paso 3 — integrar:**

$$
a_0 = \frac12\int_{-1}^{1} 1\cdot e^{t+1}\,dt = 3{,}1945
\qquad
a_1 = \frac32\int_{-1}^{1} t\cdot e^{t+1}\,dt = 3
$$

**Paso 4 — volver a $x$:**

$$
y(t) = 3{,}1945 + 3t
\quad\Longrightarrow\quad
y(x) = 3{,}1945 + 3(-1 + x)
\quad\Longrightarrow\quad
\boxed{\,y(x) = 0{,}1945 + 3x\,}
$$

(Recuadro al margen: si se quisiera la parábola por Legendre haría falta $a_2 = \dfrac52\displaystyle\int_{-1}^{1} e^{t+1}\cdot\tfrac12\,(3t^2-1)\,dt$, con $\varphi_2(t) = \tfrac12(3t^2-1)$. El profesor no lo calcula.)

**Control por el método tradicional** (recuadro rojo), con $y = a_0 + a_1 x$:

$$
\begin{cases}
a_0\displaystyle\int_0^2 dx + a_1\int_0^2 x\,dx = \int_0^2 e^{x}\,dx\\[2mm]
a_0\displaystyle\int_0^2 x\,dx + a_1\int_0^2 x^2\,dx = \int_0^2 x\,e^{x}\,dx
\end{cases}
\quad\Longrightarrow\quad
\begin{cases}
2a_0 + 2a_1 = e^2 - 1 & (1)\\
2a_0 + \frac83\,a_1 = e^2 + 1 & (2)
\end{cases}
$$

Restando (1) y (2): $-\frac23\,a_1 = -2 \Rightarrow a_1 = 3$, y $a_0 = \dfrac{e^2 - 7}{2} = 0{,}19$. Da lo mismo: $y = 0{,}19 + 3x$.

### Parábola por el método tradicional

**Paso 1 — sistema de ecuaciones normales** para $y = a_0 + a_1 x + a_2 x^2$ en $[0,2]$:

$$
\begin{cases}
a_0\displaystyle\int_0^2 x^0\,dx + a_1\int_0^2 x^1\,dx + a_2\int_0^2 x^2\,dx = \int_0^2 x^0 f(x)\,dx\\[2mm]
a_0\displaystyle\int_0^2 x^1\,dx + a_1\int_0^2 x^2\,dx + a_2\int_0^2 x^3\,dx = \int_0^2 x^1 f(x)\,dx\\[2mm]
a_0\displaystyle\int_0^2 x^2\,dx + a_1\int_0^2 x^3\,dx + a_2\int_0^2 x^4\,dx = \int_0^2 x^2 f(x)\,dx
\end{cases}
$$

$$
\begin{cases}
2\,a_0 + 2\,a_1 + \frac83\,a_2 = e^2 - 1\\[1mm]
2\,a_0 + \frac83\,a_1 + 4\,a_2 = 1 + e^2\\[1mm]
\frac83\,a_0 + 4\,a_1 + \frac{32}{5}\,a_2 = 2\,(e^2 - 1)
\end{cases}
$$

**Paso 2 — resolver con la inversa** ($A\,X = B \Rightarrow X = A^{-1}B$), en planilla:

| Coeficientes | | | Independientes |
|---|---|---|---|
| $2$ | $2$ | $2{,}666666667$ | $6{,}38905609$ |
| $2$ | $2{,}666666667$ | $4$ | $8{,}38905609$ |
| $2{,}666666667$ | $4$ | $6{,}4$ | $12{,}7781122$ |

| Inversa de coeficientes | | |
|---|---|---|
| $4{,}5$ | $-9$ | $3{,}75$ |
| $-9$ | $24$ | $-11{,}25$ |
| $3{,}75$ | $-11{,}25$ | $5{,}625$ |

$$
a_0 = 1{,}16717,\qquad a_1 = 0{,}0821,\qquad a_2 = 1{,}45896
$$

$$
\boxed{\,y = 1{,}16717 + 0{,}0821\,x + 1{,}45896\,x^2\,}
$$

> Verificado: $a_0 = \frac{e^2-1}{2} = 3{,}19453$, $a_1 = 3$ exacto, $\frac{e^2-7}{2} = 0{,}19453$; la inversa coincide entera y la solución es $(1{,}167168;\ 0{,}082079;\ 1{,}458960)$. Los valores de la inversa se leen chicos en la captura, pero coinciden con el cálculo.

**Qué mirar:** el error típico es integrar $e^{x}$ en $[-1,1]$ sin hacer el cambio (hay que integrar $e^{t+1}$) y olvidarse de **volver a $x$** al final. El factor es $\frac{2m+1}{2}$: $\frac12$ para $\varphi_0$, $\frac32$ para $\varphi_1$.

</details>

</details>

## 6) Sistemas lineales — reordenar, $T$ de Jacobi y norma infinito · 15 min

<details>
<summary><strong>Ejercicio 6 — enunciado</strong> ("Ejercicio 3" de un parcial viejo, 1 punto por ítem)</summary>

Sea el sistema lineal:

$$
\begin{cases}
2x - 3y + 6z = 9\\
10x + y + z = 3\\
0{,}5x + y = 1
\end{cases}
$$

- a) Ordene las ecuaciones para que se pueda resolver por método iterativo. Justifique. (1 punto)
- b) Hallar la $T$ de Jacobi y verifique usando la norma infinito que el sistema converge a la solución. (1 punto)

<details>
<summary><strong>Resolución 6</strong></summary>

**a) Paso 1 — buscamos diagonal dominante.** Reordenamos las filas:

$$
\begin{cases}
10x + y + z = 3\\
\frac12 x + y = 1\\
2x - 3y + 6z = 9
\end{cases}
\qquad
A = \begin{pmatrix} 10 & 1 & 1\\ \frac12 & 1 & 0\\ 2 & -3 & 6\end{pmatrix}
$$

Diagonal dominante: converge con los métodos numéricos [iterativos].

(cuenta intermedia agregada, es la justificación que pide el ítem) $\lvert 10\rvert > 1 + 1$; $\lvert 1\rvert > \frac12 + 0$; $\lvert 6\rvert > 2 + 3$. Es **estrictamente** diagonal dominante por filas.

**b) Paso 2 — despejar cada incógnita de su ecuación:**

$$
\begin{cases}
x = -\dfrac{y}{10} - \dfrac{z}{10} + \dfrac{3}{10}\\[2mm]
y = -\dfrac12\,x + 1\\[2mm]
z = -\dfrac13\,x + \dfrac12\,y + \dfrac32
\end{cases}
$$

**Paso 3 — forma matricial** $\vec X = T\,\vec X + \vec C$, con $T_J = -D^{-1}(L+U)$:

$$
\begin{pmatrix}x\\y\\z\end{pmatrix}
=
\underbrace{\begin{pmatrix} 0 & -\frac1{10} & -\frac1{10}\\[1mm] -\frac12 & 0 & 0\\[1mm] -\frac13 & \frac12 & 0\end{pmatrix}}_{T_J}
\begin{pmatrix}x\\y\\z\end{pmatrix}
+
\begin{pmatrix}\frac3{10}\\[1mm] 1\\[1mm] \frac32\end{pmatrix}
$$

(En el manuscrito aparece "$D^{-1}(L+U)$" sin el signo menos; los signos de la matriz están bien.)

**Paso 4 — criterios de convergencia** (los tres que anota el profesor):

1. $A$ diagonal dominante
2. $\lVert T\rVert < 1$
3. $\rho(T) < 1$, con los autovalores de $\lvert T - \lambda I\rvert = 0$

**Paso 5 — norma infinito** (máxima suma de módulos por fila):

$$
\text{fila 1: } \tfrac1{10}+\tfrac1{10} = \tfrac{2}{10}
\qquad
\text{fila 2: } \tfrac12
\qquad
\text{fila 3: } \tfrac13+\tfrac12 = \tfrac56
$$

$$
\boxed{\,\lVert T\rVert_\infty = \frac56 < 1\ \Rightarrow\ \text{Jacobi converge}\,}
$$

> Verificado: sumas por fila $0{,}2;\ 0{,}5;\ 0{,}8333$. Dato extra (agregado): $\rho(T_J) = 0{,}385$ y la solución exacta del sistema es $(0;\ 1;\ 2)$.

**Qué mirar:** (1) "Justifique" = escribir las tres desigualdades de la diagonal dominante, no solo la palabra; (2) $T$ tiene **ceros en la diagonal** y los signos cambiados respecto de $A$ (cada fila dividida por su pivote); (3) la norma infinito es por **filas** (la norma 1 es por columnas) y la condición es $<1$ estricta. En el parcial 2025 (T1/T2 Ej2) la norma no alcanzó y hubo que ir al radio espectral: si $\lVert T\rVert \ge 1$ no se puede concluir nada, se sigue con $\rho(T)$.

</details>

</details>

## 7) Interpolación + diferenciación — Newton-Gregory y $f''(4)$ · 15 min

<details>
<summary><strong>Ejercicio 7 — enunciado</strong> ("Ejercicio 4" de un parcial viejo, 1 punto por ítem)</summary>

Dado el conjunto de puntos:

| $x$ | $1$ | $3$ | $4$ | $5$ | $7$ |
|---|---|---|---|---|---|
| $y$ | $-1{,}5$ | $-4{,}5$ | $0$ | $12{,}5$ | $73{,}5$ |

- a) Indicar el grado del polinomio interpolante que pasa por todos los puntos. Hallar dicho polinomio usando Newton-Gregory (no es necesario distribuir). (1 punto)
- b) Halle $f''(4)$ usando la fórmula central. (1 punto)

<details>
<summary><strong>Resolución 7</strong></summary>

**a)** El manuscrito **no resuelve este ítem** (en el repaso solo se hizo el b). Lo que sigue es todo `(cuenta intermedia agregada)`, con el mismo método de los ejercicios 3 y 4.

**Paso 1 — diferencias divididas:**

| $x$ | $y$ | O1 | O2 | O3 | O4 |
|---|---|---|---|---|---|
| $1$ | $-1{,}5$ | | | | |
| | | $-1{,}5$ | | | |
| $3$ | $-4{,}5$ | | $2$ | | |
| | | $4{,}5$ | | $0{,}5$ | |
| $4$ | $0$ | | $4$ | | $0$ |
| | | $12{,}5$ | | $0{,}5$ | |
| $5$ | $12{,}5$ | | $6$ | | |
| | | $30{,}5$ | | | |
| $7$ | $73{,}5$ | | | | |

**Paso 2 — grado.** La columna O3 es constante ($0{,}5$) y O4 se anula ⇒ el interpolante es de **grado 3**.

**Paso 3 — polinomio:**

$$
P(x) = -1{,}5 - 1{,}5\,(x-1) + 2\,(x-1)(x-3) + 0{,}5\,(x-1)(x-3)(x-4)
$$

**b) Paso 4 — fórmula central de la derivada segunda** (del profesor). Alrededor de $x=4$ los puntos $3,\ 4,\ 5$ están equiespaciados con $h = 1$:

$$
f''_c(4) = \frac{f(3) - 2f(4) + f(5)}{1^{2}} = \frac{-4{,}5 - 2\cdot 0 + 12{,}5}{1} = 8
$$

$$
\boxed{\,f''(4) \approx 8\,}
$$

Debajo del recuadro quedó un "$= 6$" (o "$= 0$") suelto, tapado por la foto del ejercicio siguiente: `[poco claro en el manuscrito]`, no pertenece a esta cuenta.

> Verificado: tabla de diferencias y $f''_c(4) = 8$. Con el polinomio del ítem a), $P''(4) = 4 + 0{,}5\,(6\cdot 4 - 16) = 8$: coincide.

**Qué mirar:** la fórmula central necesita **paso constante a los dos lados** del punto. La tabla no es equiespaciada ($1, 3, 4, 5, 7$), pero justo $3, 4, 5$ sí: hay que elegir esos tres y decir $h=1$. Con $1$ y $7$ no se puede.

</details>

</details>

## 8) Interpolación / diferenciación — conceptual (consumo acumulado) · 5 min

<details>
<summary><strong>Ejercicio 8 — enunciado</strong></summary>

La siguiente tabla muestra el consumo acumulado de energía eléctrica de una casa a lo largo del tiempo:

| $t$ (tiempo en días) | $0$ | $1$ | $2$ | $3$ | $6$ | $8$ |
|---|---|---|---|---|---|---|
| $E(t)$ (consumo acumulado de energía en kW) | $0$ | $10$ | $18$ | $30$ | $80$ | $95$ |

**i)** Para hacer estimaciones sobre el consumo de energía dentro del intervalo dado, ¿qué es conveniente utilizar? a) Interpolación · b) Aproximación · c) ambas · d) n.a.

**ii)** Si tuviese que estimar el consumo puntual de energía que hubo en el octavo día, ¿cuál de las siguientes fórmulas de diferenciación numérica podría utilizar de forma conveniente? a) Progresiva · b) Regresiva · c) Central · d) No es posible ninguna fórmula numérica.

<details>
<summary><strong>Resolución 8</strong></summary>

**i) Consumo acumulado:** siempre creciente. No puede tener saltos como tendría si interpolamos.

**Respuesta: b) Aproximación (ajuste).**

**ii)** Solo cuento con los datos para calcular la fórmula regresiva.

**Respuesta: b) Regresiva.**

(aclaración agregada) $t = 8$ es el **último** dato: no hay ningún punto a la derecha, así que ni la progresiva ni la central se pueden armar; la regresiva usa el dato anterior ($t=6$).

**Qué mirar:** la justificación de i) es física (un acumulado no puede bajar y el interpolante de grado 5 oscila); la de ii) es de datos disponibles: **extremo derecho → regresiva, extremo izquierdo → progresiva, punto interior con paso parejo → central**.

</details>

</details>

## 9) Integración — ¿cuándo Simpson da el valor exacto? · 5 min

<details>
<summary><strong>Ejercicio 9 — enunciado</strong></summary>

Al resolver $\displaystyle\int_{-3}^{3} \left(x^{3}\cos x + x\right)dx$ por el método de Simpson tomando $n$ subintervalos se obtiene el valor exacto si:

- a) $n$ es par
- b) $n$ es mayor que 3
- c) $n$ es par y mayor que 6
- d) nunca es posible
- e) $n$ es impar
- f) n.a.

<details>
<summary><strong>Resolución 9</strong></summary>

**Paso 1 — paridad del integrando:**

$$
\underbrace{\underbrace{x^{3}}_{\text{impar}}\cdot\underbrace{\cos x}_{\text{par}}}_{\text{impar}} + \underbrace{x}_{\text{impar}}
\quad\Longrightarrow\quad \text{impar}
$$

**Paso 2 — intervalo simétrico.** Función impar + intervalo simétrico ⇒ resultado exacto con Trapecios o Simpson.

**Paso 3 — condición de Simpson.** Para Simpson necesito cantidad de subintervalos **par**.

**Respuesta: a)** y también **c)** (si $n$ es par y mayor que 6, también es par): el profesor marca las dos.

(aclaración agregada) La integral exacta vale $0$, y la suma de Simpson (o de Trapecios) también da $0$ porque los nodos y los pesos son simétricos respecto del origen: cada $f(x_i)$ se cancela con $f(-x_i)$.

**Qué mirar:** no hay que calcular nada: se justifica con **paridad + simetría** y con el requisito de $N$ par. Si te sale acotar $f^{(4)}$ estás yendo por el camino largo.

</details>

</details>

## 10) Integración — V/F: Trapecios por defecto y Simpson con $h=0{,}08$ · 10 min

<details>
<summary><strong>Ejercicio 10 — enunciado</strong> ("Ejercicio 5")</summary>

Dada la integral $\displaystyle\int_{1}^{3} \big(\operatorname{sen}(x) + \ln(x)\big)\,dx$, indique verdadero o falso justificando:

- a) Trapecios devuelve un valor menor al exacto.
- b) Se puede resolver por Simpson con $h = 0{,}08$.

<details>
<summary><strong>Resolución 10</strong></summary>

**a) Paso 1 — la regla (dibujo del profesor).**

- Cóncava hacia abajo, $f''(x) < 0$: los trapecios quedan **debajo** de la curva ⇒ $A_T < \int$.
- Cóncava hacia arriba, $f''(x) > 0$: los trapecios quedan **encima** ⇒ $A_T > \int$.

**Paso 2 — derivar:**

$$
f(x) = \operatorname{sen}(x) + \ln(x)
\qquad
f'(x) = \cos x + \frac1x
\qquad
f''(x) = -\operatorname{sen}x - \frac{1}{x^{2}}
$$

**Paso 3 — signo.** Ambos términos ($\operatorname{sen}x$ y $\frac1{x^2}$) son siempre positivos entre 1 y 3 (el profesor lo muestra con la circunferencia: $1$ y $3$ rad están entre $0$ y $\pi$). Con el signo menos adelante, $f''$ es **siempre negativa** en $[1,3]$.

Cóncava hacia abajo ⇒ $A_T < \int$ ⇒ **a) Verdadero.**

**b) Paso 4 — cantidad de subintervalos:**

$$
N = \frac{b-a}{h} = \frac{3-1}{0{,}08} = 25
$$

$N$ impar ⇒ no sirve ⇒ **b) Falso.**

> Verificado: $f''(1) = -1{,}841$, $f''(3) = -0{,}252$ (negativa en los dos extremos y en el medio); $2/0{,}08 = 25$.

**Qué mirar:** en a) la justificación completa es el **signo de $f''$ en todo el intervalo** (no alcanza con evaluar en un punto: hay que decir por qué no cambia). En b) lo único que se mira es si $N=(b-a)/h$ es **entero y par**.

</details>

</details>

## 11) Integración — mayor $h$ racional no periódico para Trapecios · 20 min

<details>
<summary><strong>Ejercicio 11 — enunciado</strong></summary>

Dada la siguiente integral, hallar el mayor $h$ racional no periódico para asegurar un error menor a $10^{-2}$ con el método de Trapecios:

$$
\int_{1}^{3} \ln(3x)\,x^{3}\,dx
$$

*(Extra del profesor: ¿y si fuera con Simpson?)*

<details>
<summary><strong>Resolución 11</strong></summary>

**Paso 1 — fórmula del error de Trapecios** (está en el ayudamemoria):

$$
e_T = \left\lvert \frac{b-a}{12}\right\rvert\, h^{2}\, \max\lvert f''\rvert
$$

**Paso 2 — derivar dos veces:**

$$
f(x) = \ln(3x)\cdot x^{3}
$$

$$
f'(x) = \frac1x\,x^{3} + 3x^{2}\ln(3x) = x^{2} + 3x^{2}\ln(3x)
$$

$$
f''(x) = 2x + \frac{3x^{2}}{x} + 6x\ln(3x) = 5x + 6x\ln(3x)
$$

**Paso 3 — máximo de $\lvert f''\rvert$ en $[1,3]$.** $f''(x)$ crece ∴ $f''(3)$ es el $\max\lvert f''\rvert$:

$$
f''(3) = 15 + 18\ln 9 = 54{,}55
$$

(cuenta intermedia agregada) Crece porque $f'''(x) = 11 + 6\ln(3x) > 0$ en $[1,3]$.

**Paso 4 — despejar $h$:**

$$
\frac{3-1}{12}\,h^{2}\cdot 54{,}55 < 10^{-2}
\quad\therefore\quad
\frac16\,h^{2}\cdot 54{,}55 < 10^{-2}
\quad\Longrightarrow\quad
h < \sqrt{\frac{6}{5455}} = 0{,}0332
$$

**Paso 5 — pasar a cantidad de subintervalos:**

$$
N = \frac{2}{0{,}0332} = 60{,}24 \quad\Longrightarrow\quad N > 60{,}24
$$

**Paso 6 — tabla de candidatos** ($h = 2/N$, planilla del profesor):

| $N$ | $h$ | | $N$ | $h$ |
|---|---|---|---|---|
| 61 | 0,03278689 | | 71 | 0,02816901 |
| 62 | 0,03225806 | | 72 | 0,02777778 |
| 63 | 0,03174603 | | 73 | 0,02739726 |
| **64** | **0,03125** | | 74 | 0,02702703 |
| 65 | 0,03076923 | | 75 | 0,02666667 |
| 66 | 0,03030303 | | 76 | 0,02631579 |
| 67 | 0,02985075 | | 77 | 0,02597403 |
| 68 | 0,02941176 | | 78 | 0,02564103 |
| 69 | 0,02898551 | | 79 | 0,02531646 |
| 70 | 0,02857143 | | **80** | **0,025** |

El primer $N$ que da un $h$ con desarrollo decimal finito es $N = 64$ (el manuscrito deja la tabla y no escribe la conclusión; es la lectura de la tabla):

$$
\boxed{\,h = \frac{2}{64} = 0{,}03125 \quad (N = 64)\,}
$$

> Verificado: $f''(3) = 54{,}5500$; $\sqrt{6/5455} = 0{,}033165$ (el profesor escribe $0{,}0332$, redondeado **hacia arriba**); $2/0{,}033165 = 60{,}30$ (el profesor: $60{,}24$, porque divide por el $0{,}0332$ redondeado). **No cambia nada:** $N \ge 61$ en los dos casos y el primer $h$ no periódico sigue siendo $0{,}03125$. Entre 61 y 80 solo $N=64$ y $N=80$ dan decimal finito.

### Si fuera con Simpson

**Paso 7 — error de Simpson** (también en el ayudamemoria):

$$
e_S = \left\lvert \frac{b-a}{180}\right\rvert\, h^{4}\, \max_{[a,b]}\lvert f^{IV}\rvert
$$

**Paso 8 — derivar hasta la cuarta:**

$$
f'' = 5x + 6x\ln(3x)
\qquad
f'''(x) = 5 + 6\ln(3x) + \frac{6x}{x} = 11 + 6\ln(3x)
\qquad
f^{IV}(x) = \frac6x
$$

Máximo en $x = 1$: $f^{IV}(1) = 6$.

**Paso 9 — despejar:**

$$
\frac{2}{180}\,h^{4}\cdot 6 < 10^{-2}
\quad\Longrightarrow\quad
\frac{h^{4}}{15} < 10^{-2}
\quad\Longrightarrow\quad
h < \sqrt[4]{\frac{15}{100}} = 0{,}6223
$$

$$
N > \frac{2}{0{,}6223} = 3{,}21 \quad\Longrightarrow\quad N = 4 \quad\Longrightarrow\quad \boxed{\,h = \frac24 = 0{,}5\,}
$$

> Verificado: $0{,}15^{1/4} = 0{,}62233$, $N > 3{,}214$; $N=4$ es par, así que sirve para Simpson.

**Qué mirar:** (1) hay que **justificar dónde está el máximo** de $\lvert f''\rvert$: acá "es creciente porque $f'''>0$, entonces el máximo está en $x=3$" (en las hojas 2025 hubo que comparar extremos contra puntos críticos); (2) "racional no periódico" = elegir $N$ entero $\ge$ la cota tal que $h=(b-a)/N$ **termine** ($N$ con solo factores 2 y 5 cuando $b-a=2$): no es redondear $0{,}0332$ a $0{,}03$, porque $2/0{,}03$ no es entero; (3) al redondear $h$ siempre **hacia abajo** ($N$ hacia arriba); (4) en Simpson, además, $N$ **par**.

</details>

</details>

## 12) Ecuaciones diferenciales — clasificar una fórmula multipaso · 5 min

<details>
<summary><strong>Ejercicio 12 — enunciado</strong></summary>

La fórmula

$$
w_{i+1} = w_i + \frac{h}{24}\Big[\,9f(t_{i+1};w_{i+1}) + 19f(t_i;w_i) - 5f(t_{i-1};w_{i-1}) + f(t_{i-3};w_{i-3})\Big]
$$

corresponde a una fórmula ……………… (explícita / implícita) de …… pasos.

*(Así está impresa: el último término tiene subíndice $i-3$. La $h$ del factor $\frac{h}{24}$ la agrega el profesor a mano sobre la foto.)*

<details>
<summary><strong>Resolución 12</strong></summary>

**Paso 1 — ¿explícita o implícita?** **Implícita**, porque incluye a $w_{i+1}$ (del lado derecho, adentro de $f$). Solo puede utilizarse como **etapa correctora**.

**Paso 2 — ¿cuántos pasos?** **4 pasos**: $(w_i,\ w_{i-1},\ w_{i-2},\ w_{i-3})$. Aunque $w_{i-2}$ no aparezca en la fórmula, lo necesitamos para llegar a $w_{i-3}$.

**Respuesta: implícita, de 4 pasos.**

**Qué mirar:** implícita ⇔ $w_{i+1}$ aparece **también a la derecha**. Los pasos se cuentan desde $w_i$ hasta el índice **más viejo** que aparece ($i-3$ ⇒ 4 valores anteriores), no contando cuántos términos hay escritos. En el R2 2025 la fórmula era $\frac h2[3f(t_i;w_i) - f(t_{i-1};w_{i-1})]$: explícita, 2 pasos.

</details>

</details>

## 13) Ecuaciones diferenciales — constante de Lipschitz · 12 min

<details>
<summary><strong>Ejercicio 13 — enunciado</strong></summary>

Hallar la constante de Lipschitz para $f(t,y) = 2\,t^{-1/2}\,y^{3}$ en

$$
R = \{(t,y) \in \mathbb{R}^{2}\ /\ 1 \le t \le 4\ \wedge\ -4 \le y \le 3\}
$$

(contexto que anota el profesor: el PVI $y' = f(t,y)$, $y(a) = \alpha$).

<details>
<summary><strong>Resolución 13</strong></summary>

Hay **dos formas**.

### Forma 1 — por la definición

$$
\lvert f(t,y_1) - f(t,y_2)\rvert \le L\cdot\lvert y_1 - y_2\rvert
$$

**Paso 1 — armar la diferencia:**

$$
\left\lvert \frac{2}{\sqrt t}\,y_1^{3} - \frac{2}{\sqrt t}\,y_2^{3}\right\rvert = \left\lvert\frac{2}{\sqrt t}\right\rvert\,\lvert y_1^{3} - y_2^{3}\rvert
$$

**Paso 2 — sacar el factor $(y_1 - y_2)$** (el profesor hace la división de polinomios $(y_1^3 - y_2^3) : (y_1 - y_2)$, cociente $y_1^2 + y_1y_2 + y_2^2$, resto 0):

$$
\frac{2}{\sqrt t}\,\lvert y_1^{3} - y_2^{3}\rvert = \frac{2}{\sqrt t}\,\lvert y_1^{2} + y_1 y_2 + y_2^{2}\rvert\cdot\lvert y_1 - y_2\rvert
$$

**Paso 3 — acotar lo que multiplica a $\lvert y_1-y_2\rvert$.** Es máximo para $t = 1$ (da $2$) y para $y_1 = y_2$ en el extremo de mayor módulo, $y=-4$, o sea $\lvert y\rvert = 4$ (da $48$):

$$
\frac{2}{\sqrt 1}\cdot\lvert 4^{2} + 4\cdot 4 + 4^{2}\rvert = 2\cdot 48
\quad\Longrightarrow\quad
\boxed{\,L = 96\,}
$$

(Nota en azul: como $y_1$ e $y_2$ son lo mismo, se puede pensar como $3y^2$.)

### Forma 2 — por la derivada parcial

**Paso 1 — criterio** (tal como lo escribe el profesor): si $\displaystyle\lim_{y\to 0}\left\lvert\frac{\partial f(t,y)}{\partial y}\right\rvert = k \wedge k \in \mathbb{R} \Rightarrow L = \max\left\lvert\frac{\partial f(t,y)}{\partial y}\right\rvert$. La derivada parcial tiene que ser continua en el rectángulo.

**Paso 2 — derivar respecto de $y$:**

$$
f(t,y) = \frac{2}{\sqrt t}\,y^{3}
\qquad
\left\lvert\frac{\partial f(t,y)}{\partial y}\right\rvert = \left\lvert\frac{6}{\sqrt t}\,y^{2}\right\rvert
$$

**Paso 3 — control de continuidad:**

$$
\lim_{y\to 0}\frac{6}{\sqrt t}\,y^{2} = 0\ \checkmark
$$

**Paso 4 — maximizar en $R$.** Máximo cuando $t = 1$ (el factor $\frac{6}{\sqrt t}$ vale $6$) y $\lvert y\rvert = 4$ ($y^2 = 16$):

$$
L = \left\lvert\frac61\cdot 4^{2}\right\rvert
\quad\Longrightarrow\quad
\boxed{\,L = 96\,}
$$

> Verificado: $6\cdot 16 = 96$ por las dos formas.

**Qué mirar:** (1) el máximo de $y^2$ se toma en el extremo de **mayor módulo** ($y=-4$, no $y=3$): con 3 da $54$ y está mal; (2) $t$ va en el denominador, así que el máximo es en el $t$ **más chico**; (3) hay que decir que $\partial f/\partial y$ es **continua y acotada** en el rectángulo (por eso existe $L$). Si $t$ pudiera valer 0 no existiría.

</details>

</details>

## 14) Ajuste discreto — exponencial de mínimos cuadrados · ⚪ no entra en el 2P 2026

<details>
<summary><strong>Ejercicio 14 — enunciado</strong> ("3)" de un parcial viejo)</summary>

Dada la siguiente tabla de valores:

| $x$ | $1$ | $1{,}2$ | $1{,}6$ | $2$ | $2{,}1$ |
|---|---|---|---|---|---|
| $y$ | $5$ | $5{,}5$ | $7$ | $7{,}8$ | $9$ |

- a) Hallar la función exponencial $y = b\,e^{ax}$ que mejor ajuste a los datos. (2 puntos)
- b) ~~Halle el valor en $x = 1{,}4$ usando un polinomio de grado 2. Tome una cantidad de puntos consecutivos convenientes. (1 punto)~~ *(tachado por el profesor: no se hizo)*

> ⚪ **No entra en el 2P 2026** (ajuste se evaluó con el TP). En 2025 este ítem cayó en las 4 hojas, por eso está en el repaso.

<details>
<summary><strong>Resolución 14</strong></summary>

**Paso 1 — linealizar:**

$$
y = b\,e^{ax}\quad\longrightarrow\quad \underbrace{\ln y}_{Y} = \underbrace{\ln b}_{B} + a\,x
$$

**Paso 2 — ecuaciones normales.** Las de la recta $y = ax + b$ son $a\sum x_i^2 + b\sum x_i = \sum x_i y_i$ y $a\sum x_i + b\,n = \sum y_i$; con $Y = \ln y$ y $B = \ln b$:

$$
\begin{cases}
a\sum x_i^{2} + B\sum x_i = \sum x_i\ln(y_i)\\[1mm]
a\sum x_i + B\cdot 5 = \sum \ln(y_i)
\end{cases}
$$

**Paso 3 — tabla de sumatorias** (planilla):

| $x$ | $y$ | $x^2$ | $\ln y$ | $x\ln y$ |
|---|---|---|---|---|
| $1$ | $5$ | $1$ | $1{,}60943791$ | $1{,}60943791$ |
| $1{,}2$ | $5{,}5$ | $1{,}44$ | $1{,}70474809$ | $2{,}04569771$ |
| $1{,}6$ | $7$ | $2{,}56$ | $1{,}94591015$ | $3{,}11345624$ |
| $2$ | $7{,}8$ | $4$ | $2{,}05412373$ | $4{,}10824747$ |
| $2{,}1$ | $9$ | $4{,}41$ | $2{,}19722458$ | $4{,}61417161$ |
| $\Sigma = 7{,}9$ | $34{,}3$ | $13{,}41$ | $9{,}51144446$ | $15{,}4910109$ |

**Paso 4 — sistema y solución:**

$$
\begin{cases}
13{,}41\,a + 7{,}9\,B = 15{,}4910\\
7{,}9\,a + 5\,B = 9{,}5114
\end{cases}
\quad\Longrightarrow\quad
a = 0{,}4988,\qquad B = 1{,}1141
$$

**Paso 5 — deshacer el cambio:** $b = e^{B} = 3{,}0468$ (planilla: $a = 0{,}49884557$; $B = 1{,}1141129$; $b = 3{,}04686409$).

$$
\boxed{\,y = 3{,}0468\,e^{0{,}4988\,x}\,}
$$

Al margen el profesor anota también el error del ajuste, $E = \sum (y - \bar y)^2$ (con $\bar y$ el valor del modelo); no lo calcula.

> Verificado: sumatorias, $a = 0{,}498846$, $B = 1{,}114113$, $b = 3{,}046864$.

**Qué mirar:** el parámetro que sale del sistema es $B=\ln b$, no $b$: hay que hacer $b=e^{B}$. Y en la segunda ecuación va $n = 5$ (cantidad de puntos), no $\sum$ de nada.

</details>

</details>

## 15) Sistemas lineales — número de condición · 8 min

<details>
<summary><strong>Ejercicio 15 — enunciado</strong></summary>

Hallar el número de condición de la matriz $A$:

$$
A = \begin{pmatrix} -5 & -1 & 2\\ 4 & 7 & 1\\ -1 & 2 & 9\end{pmatrix}
\qquad
A^{-1} = \begin{pmatrix}
-\frac{61}{238} & -\frac{13}{238} & \frac{15}{238}\\[1mm]
\frac{37}{238} & \frac{43}{238} & -\frac{13}{238}\\[1mm]
-\frac{15}{238} & -\frac{11}{238} & \frac{31}{238}
\end{pmatrix}
$$

*(Las dos matrices están impresas muy chicas en el OneNote: los módulos se leen, los signos de $A^{-1}$ no. Los signos de arriba salen de invertir $A$ con Python y son consistentes con las sumas por fila que escribe el profesor.)*

<details>
<summary><strong>Resolución 15</strong></summary>

**Paso 1 — norma infinito de $A$** (suma de módulos por fila):

$$
\text{fila 1: } 5+1+2 = 8
\qquad
\text{fila 2: } 4+7+1 = 12
\qquad
\text{fila 3: } 1+2+9 = 12
\qquad\Longrightarrow\qquad
\lVert A\rVert_\infty = 12
$$

**Paso 2 — norma infinito de $A^{-1}$:**

$$
\text{fila 1: } \tfrac{89}{238} = 0{,}3739
\qquad
\text{fila 2: } \tfrac{93}{238} = 0{,}3907
\qquad
\text{fila 3: } \tfrac{57}{238} = 0{,}2394
\qquad\Longrightarrow\qquad
\lVert A^{-1}\rVert_\infty = 0{,}3907
$$

**Paso 3 — número de condición:**

$$
K(A) = \lVert A\rVert\,\lVert A^{-1}\rVert = 12\cdot 0{,}3907 = 4{,}69
$$

$$
\boxed{\,K(A) \approx 4{,}69 \ \Rightarrow\ \text{está bien condicionada}\,}
$$

> Verificado: $A^{-1}\cdot 238$ coincide, sumas $89,\ 93,\ 57$ y $K = 12\cdot\frac{93}{238} = 4{,}689$.

**Qué mirar:** es el **R2 2025 Ej2a** con las filas 1 y 2 de $A$ intercambiadas (por eso en $A^{-1}$ aparecen las columnas 1 y 2 intercambiadas); el resultado es el mismo. Las dos normas tienen que ser **la misma** (infinito con infinito) y con **módulos**. Conclusión que hay que escribir: $K$ chico (cercano a 1, del orden de las unidades) ⇒ bien condicionada; $K$ grande ⇒ mal condicionada. $K\ge 1$ siempre: si te da menos de 1, hay un error.

</details>

</details>

---

## Tablero de resultados (para corregirte rápido)

| # | Resultado |
|---|---|
| 1 | $i > 24{,}25 \Rightarrow$ suficientes 25 iteraciones ⇒ **f) N.A.** |
| 2 | a) F · b) F · **c) V** · d) F · e) F; raíz $x \approx -1{,}2965885$ en $[-2;-1]$ |
| 3 | $k = 11$; b.1) ninguno; b.2) infinitos |
| 4 | $h = -3$, $a = 32$, $P(x) = -4 - 0{,}25(x-1) + 3{,}5(x-1)(x-1{,}5) + (x-1)(x-1{,}5)(x-3)$; b) $0, 0, 0, 1, \infty$; c) $5$ |
| 5 ⚪ | recta $y = 0{,}1945 + 3x$; parábola $y = 1{,}16717 + 0{,}0821x + 1{,}45896x^2$ |
| 6 | filas en orden 2ª, 3ª, 1ª; $\lVert T_J\rVert_\infty = \frac56 < 1$ ⇒ converge |
| 7 | grado 3 (agregado); $f''(4) \approx 8$ |
| 8 | i) b) Aproximación · ii) b) Regresiva |
| 9 | a) (y c): integrando impar en intervalo simétrico, $n$ par |
| 10 | a) V ($f''<0$) · b) F ($N = 25$ impar) |
| 11 | Trapecios: $h < 0{,}0332$, $N \ge 61$ ⇒ $h = 0{,}03125$ ($N=64$). Simpson: $h = 0{,}5$ ($N=4$) |
| 12 | implícita, 4 pasos |
| 13 | $L = 96$ |
| 14 ⚪ | $y = 3{,}0468\,e^{0{,}4988x}$ |
| 15 | $K(A) = 4{,}69$, bien condicionada |

---

*Generado el 2026-11-18 desde `fuentes/clases/repaso segundo parcial/OneNote - Repaso Segundo Parcial.pdf` (15 páginas, leídas con visión). Enunciados transcriptos de las fotos/recortes del OneNote; resoluciones transcriptas del manuscrito del profesor y verificadas con Python (numpy/sympy). Gemelos de parcial tomados de `segundo-parcial/examenes/INDICE.md` (4 hojas 2025-1C), sin releer los PDFs de exámenes. Tags según la leyenda del 2P en `MATERIA.md`. Agregados propios marcados en el texto: ítem 7a (no resuelto en el manuscrito), justificaciones de 4b, 6a y 8, conclusión de la tabla de $h$ en 11, y todas las líneas "Qué mirar".*
