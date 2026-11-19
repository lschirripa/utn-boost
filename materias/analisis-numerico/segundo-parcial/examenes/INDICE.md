# Índice de parciales — Segundo Parcial · Análisis Numérico (UTN.BA)

> **Para qué sirve:** los enunciados vienen como PDFs tipeados con fórmulas incrustadas
> como imagen (el sistema del Ej2, la integral del Ej4 y el PVI del Ej5 no salen en la capa
> de texto) y las respuestas oficiales son hojas OneNote manuscritas, sin capa de texto.
> Este archivo es la **única representación textual** de todos: transcripción curada
> (matemática intacta) de cada hoja de examen, con **tags por tema**. Para cualquier
> análisis (frecuencias, brechas, simulacros) se grepea **este archivo**, nunca se re-leen
> los PDFs.
>
> **Cómo buscar** (desde `examenes/`):
> ```bash
> grep -n "#EleccionH" INDICE.md            # elegir h por cota de error (Ej4)
> grep -n "#PuntoFijo" INDICE.md            # ítems de punto fijo
> grep -B2 "#AjusteExponencial" INDICE.md   # ajuste exponencial, con su hoja
> grep -n "^## 2025" INDICE.md              # listar las 4 hojas de examen
> grep -n "RECICLADO" INDICE.md             # ítems repetidos entre hojas
> ```
> **Mantenimiento:** al agregar un parcial nuevo, sumá su sección con los mismos tags y
> actualizá las tablas del final. Si viene con resolución en el mismo archivo, o es una
> hoja de respuestas, va a `resueltos/`; si es copia de uno ya indexado, a `duplicados/`.
> Las resoluciones oficiales se transcriben en `resueltos/RESOLUCIONES-2025.md`.

## Cómo está armado el dataset

- **Unidad de conteo = hoja de examen.** Hay **4 hojas** de **3 instancias**, todas del
  curso K3052, 1er cuatrimestre 2025: parcial **Tema 1** y **Tema 2** (2025-06-30), **1er
  recuperatorio** (2025-07-07) y **2do recuperatorio** (2025-07-11). Las fechas salen del
  encabezado de las hojas OneNote de respuestas (los enunciados no traen fecha).
- **Formato (único conocido):** 5 ejercicios de **2 puntos** en orden fijo — **Ej1 Raíces ·
  Ej2 Sistemas de ecuaciones lineales · Ej3 Interpolación y ajuste · Ej4 Integración · Ej5
  Ecuaciones diferenciales** —, se aprueba con 6. El 1er recuperatorio detalla el puntaje
  por ítem: Ej1 a 0,5 / b 0,75 / c 0,75; Ej3 a 0,5 / b 0,25 / c 0,25 / d 1.
- **El 2do recuperatorio no tiene enunciado suelto:** su enunciado está pegado dentro de la
  hoja de respuestas (`resueltos/2025-1C_Recuperatorio-2_respuestas.pdf`), con una línea
  cortada por el salto de página (marcada «≈»).
- **Nombres:** `2025-1C_…` como en el primer parcial (se conoce el cuatrimestre; la fecha
  exacta se infiere de la hoja de respuestas). Sufijo `_respuestas` = hoja de respuestas
  oficial; `Recuperatorio-2` = 2do recuperatorio.
- **Calculadora/planilla:** las respuestas oficiales hacen las iteraciones (Newton-Raphson,
  punto fijo, Euler, Heun, RK4) y los ajustes en una planilla de cálculo y solo muestran la
  tabla de valores.

## Leyenda de tags

**Raíces de ecuaciones:** `#SepararRaices` (hallar un intervalo `[a; a+1]` para cada raíz,
gráficamente) `#Biseccion` `#CotaIteraciones` (cuántas iteraciones garantizan un error dado;
¿suficientes o necesarias?) `#PuntoFijo` (verificar las condiciones de convergencia de una
`g(x)`, elegir entre dos `g`, iterar) `#NewtonRaphson`

**Sistemas de ecuaciones lineales:** `#Jacobi` `#GaussSeidel` `#ConvergenciaIterativos`
(decidir, sin resolver, si el método converge) `#RadioEspectral` `#DiagonalDominante`
`#NumeroCondicion` (bien / mal condicionado con `‖A‖·‖A⁻¹‖`)

**Interpolación y ajuste:** `#GradoPolinomio` (condiciones sobre los parámetros de la tabla
para que el interpolante tenga cierto grado; hallar los valores faltantes)
`#CantidadPolinomios` (¿cuántos polinomios de grado n pasan por los puntos?)
`#DiferenciasDivididas` (armar el polinomio de Newton) `#AjusteRecta` `#AjusteExponencial`
`#AjustePotencial` `#ErrorAjuste`

**Integración numérica:** `#Trapecios` `#EleccionH` (mayor `h` racional no periódico, o
número de subintervalos, que garantiza la cota de error) `#Simpson`

**Ecuaciones diferenciales:** `#Lipschitz` `#Euler` `#Heun` `#RungeKutta4` `#Multipaso`
(clasificar una fórmula: explícita/implícita, cantidad de pasos)

> Convención: cada ejercicio es una línea `- **EjN)** enunciado … → #Tag #Tag`; los ítems
> a/b/c van dentro de la misma línea. `«≈»` marca un detalle aproximado (texto cortado en la
> fuente). `[RECICLADO]` marca un ítem que ya apareció, casi textual, en otra hoja. `(sic)`
> = así está escrito en el enunciado.

---

## 2025-1C · Tema 1 · `2025-1C_Parcial.pdf` (tipeado, curso K3052, pág. 1; respuestas oficiales en `resueltos/2025-1C_Parcial_respuestas.pdf`, hoja OneNote fechada **2025-06-30**, probable fecha del examen) · el enunciado no trae fecha

- **Ej1)** (Raíces) Dada la ecuación `ln(0,5x) − sen(2x) = 0`. a) Encontrar un intervalo `[a; a+1]` con `a ∈ ℤ` para cada una de las raíces. b) Encontrar la raíz más cercana a 0 usando un método conveniente con un error `ε < 10⁻⁴`. c) Con un intervalo `[a−1, a+1]` con `a ∈ ℤ`, indicar con cuántas iteraciones se puede garantizar un error `ε < 10⁻⁷` para hallar alguna raíz usando el método de bisección. ¿Son suficientes o necesarias? → #SepararRaices #NewtonRaphson #Biseccion #CotaIteraciones **[RECICLADO]** (ítem c)
- **Ej2)** (Sistemas de ecuaciones lineales) Dado el sistema `7x + 5y + 4z = 10`, `3x + 4y + 2z = 3`, `x + y + 4z = −8`: defina, sin resolver el sistema, si el método de Jacobi *converge o no converge* a la solución. → #Jacobi #ConvergenciaIterativos #RadioEspectral **[RECICLADO]**
- **Ej3)** (Interpolación y ajuste) Tabla `x = 1, 2, 4, 5, 6, 8`; `y = 0,5, a, 41, 74,5, 123, b`. a) ¿Qué condiciones deben cumplir `a` y `b` para que el polinomio que interpola a todos los puntos sea de grado 5 pero que por los cinco primeros puntos pase un polinomio de grado 3? b) Con las condiciones del ítem a), ¿cuántos polinomios de grado 4 existen? ¿Cuántos de grado 5 y cuántos de grado 6? c) Con `a = 15` y `b = 150`, hallar la recta de mínimos cuadrados. → #GradoPolinomio #DiferenciasDivididas #CantidadPolinomios #AjusteRecta
- **Ej4)** (Integración) Encontrar el mayor `h` racional no periódico y conveniente para poder obtener una aproximación de `∫_{−7}^{−5} eˣ(x³ − 6) dx` con `ε < 10⁻³` usando el método de Trapecios. → #Trapecios #EleccionH
- **Ej5)** (Ecuaciones diferenciales) PVI: `y'(t) + 2y(t)² = 1/(1 + t²)`, `t ∈ [0; 1]`, `y(0) = 0`. a) Sabiendo que `y ∈ [0; 0.5]`, hallar si es posible la constante de Lipschitz. b) Hallar `y(0.3)` usando el método de Euler con `h = 0.1`. → #Lipschitz #Euler

## 2025-1C · Tema 2 · `2025-1C_Parcial.pdf` (tipeado, K3052, pág. 2; mismas respuestas oficiales)

- **Ej1)** (Raíces) Dada la ecuación `e^{2x} − x² − 3x − 2 = 0`. a) Indique un intervalo `[a, a+1]` con `a ∈ ℤ` para cada una de las raíces. b) Analizar si es posible usar el método del punto fijo con `g(x) = ½ ln(x² + 3x + 2)` para hallar la raíz positiva usando el intervalo hallado en a), por medio de las condiciones de convergencia. c) Hallar la raíz negativa más cercana a 0 usando el método de Newton-Raphson con `ε < 10⁻⁴`. → #SepararRaices #PuntoFijo #NewtonRaphson
- **Ej2)** (Sistemas de ecuaciones lineales) Mismo sistema que el Tema 1: `7x + 5y + 4z = 10`, `3x + 4y + 2z = 3`, `x + y + 4z = −8`; definir, sin resolver, si Jacobi *converge o no converge*. → #Jacobi #ConvergenciaIterativos #RadioEspectral **[RECICLADO]**
- **Ej3)** (Interpolación y ajuste) Tabla `x = 1, 1,5, 2, 2,5, 3, 4`; `y = 7,8, 14,675, K, 50,625, 84,2, 193,8`. a) Hallar el valor de `k` real, si existe, para que el polinomio interpolante que pase por todos los puntos sea de grado 3. Hallar dicho polinomio. b) Usando los cuatro primeros datos de la tabla «del ejercicio 2» (sic; es esta tabla) y con `k = 30`, hallar la función exponencial de mínimos cuadrados que mejor ajusta a dichos datos. → #GradoPolinomio #DiferenciasDivididas #AjusteExponencial
- **Ej4)** (Integración) El mayor `h` racional no periódico y más conveniente para poder obtener una aproximación de `∫₀² eˣ(x² − 9x + 23) dx` usando el método de Trapecios con un error `ε < 10⁻²` es …… (completar). → #Trapecios #EleccionH
- **Ej5)** (Ecuaciones diferenciales) PVI: `y' = y · sen(t)`, `y(0) = 1`, `t ∈ [0; 2]`. a) Calcule si es posible la `L` de Lipschitz. b) Hallar `y(0,3)` usando el método de Euler con `h = 0.1`. → #Lipschitz #Euler

## 2025-1C · 1er recuperatorio · `2025-1C_Recuperatorio.pdf` (tipeado, K3052; respuestas en `resueltos/2025-1C_Recuperatorio_respuestas.pdf`, hoja OneNote fechada **2025-07-07**, probable fecha del examen)

- **Ej1)** (Raíces; a 0,5 · b 0,75 · c 0,75) Dada la ecuación `x/(x − 1) − eˣ = 0`. a) Indique un intervalo `[a, a+1]` / `a ∈ ℝ` (sic) para cada una de las raíces. b) Sean `g₁(x) = (x − 1)eˣ` y `g₂(x) = x/eˣ + 1` dos `g(x)` posibles para resolver la ecuación con el método del punto fijo. Indique cuál de las dos es la más adecuada para la mayor raíz. c) Halle una aproximación de dicha raíz usando la `g(x)` elegida en b) con `ε ≤ 10⁻²`. → #SepararRaices #PuntoFijo
- **Ej2)** (Sistemas de ecuaciones lineales; 2 puntos) Dada la matriz `A = (3k−3, 4, −1 ; 2, 5+k², −2 ; 7, 4, 10−k)` (filas separadas por `;`), indique los valores de `k ∈ ℝ` / el sistema `AX = B` converge a la solución utilizando el método de Jacobi o de Gauss-Seidel. → #DiagonalDominante #ConvergenciaIterativos #Jacobi #GaussSeidel
- **Ej3)** (Interpolación y ajuste; a 0,5 · b 0,25 · c 0,25 · d 1) Tabla `x = 1, 2, 4, 5, 6, 8`; `y = a, 4, 17, b, 32, c`. a) Encontrar los valores de `a`, `b` y `c` para que por los puntos pase el único polinomio de menor grado posible. b) Con `a = 1` y los valores de `b` y `c` hallados, ¿cuántos polinomios de grado 3 hay, cuántos de grado 4 y cuántos de grado 5? c) Con `b = 10` y los valores de `a` y `c` hallados, ¿cuántos polinomios de grado 10 hay? (la copia del enunciado en la hoja de respuestas agrega "Justifique correctamente") d) Con `a = 1`, `b = 24` y `c = 50`: hallar la función potencial de la forma `y = b·xᵃ` de mínimos cuadrados. → #GradoPolinomio #DiferenciasDivididas #CantidadPolinomios #AjustePotencial
- **Ej4)** (Integración; 2 puntos) Hallar un `h` racional no periódico para poder resolver la integral `∫₁³ (ln(x) + 1)/x dx` por Trapecios con `ε < 10⁻²`. → #Trapecios #EleccionH
- **Ej5)** (Ecuaciones diferenciales; 2 puntos) Sea el problema de valor inicial `y' = x/y`, siendo `y(0) = 1`. Calcule `y(0,2)` por el método de HEUN tomando `h = 0,1`. → #Heun

## 2025-1C · 2do recuperatorio · `resueltos/2025-1C_Recuperatorio-2_respuestas.pdf` (enunciado tipeado + respuestas manuscritas en la misma hoja OneNote, fechada **2025-07-11**; no hay enunciado suelto)

- **Ej1)** (Raíces) Dada la ecuación `e^{−2x} − sen(x) = 0`. a) Mostrar gráficamente dónde se encuentran las raíces. ¿Cuántas raíces tiene la ecuación? b) Hallar la segunda raíz positiva en orden ascendente usando el método de Newton-Raphson con un error menor a `10⁻⁵`, eligiendo un punto conveniente para iniciar los cálculos. c) Dada una ecuación `f(x) = 0`, indicar la cantidad de iteraciones que hay que hacer para asegurar un error de `10⁻⁵` usando el método de bisección en el intervalo `[a−1; a+1]` con `a ∈ ℤ`. ¿Son necesarias o suficientes dichas iteraciones? Justifique. → #SepararRaices #NewtonRaphson #Biseccion #CotaIteraciones **[RECICLADO]** (ítem c)
- **Ej2)** (Sistemas de ecuaciones lineales) Dado el sistema `AX = B` con `A = (4, 7, 1 ; −5, −1, 2 ; −1, 2, 9)` y `B = (6 ; 4 ; −3)`, sabiendo que `A⁻¹ = (−13/238, −61/238, 15/238 ; 43/238, 37/238, −13/238 ; −11/238, −15/238, 31/238)`. a) Indicar si el sistema está bien condicionado o no. b) Reordenando si es necesario, realizar una iteración usando el método de Gauss-Seidel comenzando con el vector `x₀ = (1, 0, 1)`. → #NumeroCondicion #GaussSeidel #DiagonalDominante
- **Ej3)** (Interpolación y ajuste) Tabla `x = 2, 3, 4, 6, 8, 9`; `y = a, 4,35, 3,2, b, 13,6, 21,45`. a) Hallar el valor de `a` y `b` para que todos los puntos pasen por el único polinomio de menor grado. b) Con el valor de `a` hallado en el punto anterior, y `b = 10`, ¿de qué grado es el polinomio que interpola a todos los puntos? Justifique. c) «≈» Con `a = 1`, `b = 8`, hallar la función exponencial de mínimos cuadrados que mejor ajusta a los puntos. Hallar el error del ajuste. (línea cortada por el salto de página; `a = 1` y `b = 8` se confirman con la tabla de la resolución) → #GradoPolinomio #DiferenciasDivididas #AjusteExponencial #ErrorAjuste
- **Ej4)** (Integración) a) Hallar un número conveniente de subintervalos para poder resolver la integral `∫₄⁶ e^{−x}(x² − 1) dx` con un error `ε ≤ 10⁻³` usando el método de Trapecios. b) Con el `h` hallado en el punto a), ¿se podría usar el método de Simpson? c) Resolver la integral con un `h = 0,5` usando el método más conveniente. → #Trapecios #EleccionH #Simpson
- **Ej5)** (Ecuaciones diferenciales) a) PVI: `y' = y · cos(t)`, `y(0) = 2`, `t ∈ [0; 1]`. Hallar `y(0,3)` usando el método de RK de orden 4 con `h = 0.3`. b) Indicar si la siguiente fórmula es implícita o no y de cuántos pasos es: `w_{i+1} = (h/2)[3f(tᵢ; wᵢ) − f(t_{i−1}; w_{i−1})]` (sic, así está impresa). → #RungeKutta4 #Multipaso

---

## Índice inverso: tema → hojas (para búsqueda rápida)

Abreviaturas: **T1** / **T2** = parcial Tema 1 / Tema 2 · **R1** = 1er recuperatorio ·
**R2** = 2do recuperatorio.

| Tag | Hojas | Frecuencia |
|---|---|---|
| `#SepararRaices` | T1, T2, R1, R2 (siempre el ítem a del Ej1) | 4/4 |
| `#NewtonRaphson` | T1 (como "método conveniente"), T2, R2 | 3/4 |
| `#PuntoFijo` | T2 (condiciones de convergencia de una `g`), R1 (elegir entre dos `g` + iterar) | 2/4 |
| `#Biseccion` `#CotaIteraciones` | T1, R2 (nunca se itera: solo se cuenta cuántas iteraciones) | 2/4 |
| `#ConvergenciaIterativos` | T1, T2, R1 | 3/4 |
| `#Jacobi` | T1, T2, R1 | 3/4 |
| `#RadioEspectral` | T1, T2 (así lo resuelve la cátedra) | 2/4 |
| `#DiagonalDominante` | R1 (hallar `k`), R2 (reordenar filas antes de Gauss-Seidel) | 2/4 |
| `#GaussSeidel` | R1 (convergencia), R2 (una iteración) | 2/4 |
| `#NumeroCondicion` | R2 | 1/4 |
| `#GradoPolinomio` | T1, T2, R1, R2 (siempre el ítem a del Ej3) | 4/4 |
| `#DiferenciasDivididas` | T1, T2, R1, R2 (es el método de la cátedra para el ítem a; solo T2 pide el polinomio explícitamente) | 4/4 |
| `#CantidadPolinomios` | T1, R1 (dos ítems) — R2 pregunta el grado, no la cantidad | 2/4 |
| `#AjusteRecta` | T1 | 1/4 |
| `#AjusteExponencial` | T2, R2 | 2/4 |
| `#AjustePotencial` | R1 | 1/4 |
| `#ErrorAjuste` | R2 | 1/4 |
| `#Trapecios` `#EleccionH` | T1, T2, R1, R2 (todo el Ej4, salvo R2 que suma Simpson) | 4/4 |
| `#Simpson` | R2 (¿se puede usar? + calcular con `h = 0,5`) | 1/4 |
| `#Lipschitz` | T1, T2 | 2/4 |
| `#Euler` | T1, T2 | 2/4 |
| `#Heun` | R1 | 1/4 |
| `#RungeKutta4` | R2 | 1/4 |
| `#Multipaso` | R2 | 1/4 |

**Lectura rápida por posición:**

- **Ej1:** separar raíces (4/4) + un ítem de iterar (Newton-Raphson 3/4, punto fijo 1/4) +
  un ítem "teórico-práctico" (cota de iteraciones de bisección 2/4, condiciones de
  convergencia de punto fijo 2/4).
- **Ej2:** convergencia de Jacobi/Gauss-Seidel sin resolver (3/4: por radio espectral en el
  parcial, por diagonal dominante con parámetro en el 1er recuperatorio); el 2do
  recuperatorio cambia a número de condición + una iteración de Gauss-Seidel.
- **Ej3:** valores/condiciones de los parámetros de la tabla por diferencias divididas (4/4)
  + conteo de polinomios o grado (3/4) + un ajuste por mínimos cuadrados (4/4: recta,
  exponencial ×2, potencial).
- **Ej4:** elegir `h` para Trapecios acotando `|f''|` (4/4); Simpson solo en el 2do
  recuperatorio.
- **Ej5:** parcial = Lipschitz + Euler (`h = 0.1`, 3 pasos); recuperatorios = métodos de
  orden mayor (Heun, RK4) + clasificación de una fórmula multipaso.

## Problemas reciclados (idénticos o casi entre hojas)

- **Sistema `7x + 5y + 4z = 10`, `3x + 4y + 2z = 3`, `x + y + 4z = −8` → ¿converge Jacobi?**
  → **T1 Ej2, T2 Ej2** (textual; la respuesta oficial del Tema 2 dice "Ídem Tema 1").
  Respuesta oficial: radio espectral `ρ = 1` (autovalor `λ = −1`) ⇒ no converge.
- **Cantidad de iteraciones de bisección en un intervalo `[a−1; a+1]` (longitud 2) para
  garantizar un error dado, y si son suficientes o necesarias** → **T1 Ej1c** (`ε < 10⁻⁷` →
  25), **R2 Ej1c** (`10⁻⁵` → 18). Misma cuenta `2/2ⁱ < ε`; respuesta "suficientes".
- **Mayor `h` racional no periódico para Trapecios con integrando `e^{±x}·polinomio`** →
  **T1 Ej4** (`eˣ(x³ − 6)` en `[−7; −5]`, `h = 0,2`), **T2 Ej4** (`eˣ(x² − 9x + 23)` en
  `[0; 2]`, `h = 0,08`), **R2 Ej4** (`e^{−x}(x² − 1)` en `[4; 6]`, `N = 8`, `h = 0,25`).
  Variante con logaritmo: **R1 Ej4** (`(ln x + 1)/x` en `[1; 3]`, `h = 0,2`). **(4 hojas,
  misma receta: `f''`, `f''' = 0`, comparar extremos vs. puntos críticos, despejar `h`;
  los cuatro intervalos tienen longitud 2, así que la cota queda `h²/6 · máx|f''|`.)**
- **Tabla de 6 puntos con 1–3 valores desconocidos → hallarlos para que el interpolante
  tenga el menor grado (o un grado dado), por diferencias divididas con los puntos
  conocidos** → **T1 Ej3a, T2 Ej3a, R1 Ej3a, R2 Ej3a**. **(4 hojas)** T1 y R1 usan las
  mismas abscisas `x = 1, 2, 4, 5, 6, 8`.
- **¿Cuántos polinomios de grado n pasan por los puntos?** → **T1 Ej3b, R1 Ej3b y 3c**;
  variante "¿de qué grado es el interpolante?" en **R2 Ej3b**.
- **Ajuste exponencial `y = a₀·e^{a₁x}` linealizando con `ln y`** → **T2 Ej3b** (4 puntos),
  **R2 Ej3c** (6 puntos + error del ajuste).
- **Lipschitz + Euler con `h = 0.1` hasta `y(0.3)`** → **T1 Ej5, T2 Ej5** (misma consigna,
  distinto PVI). Los PVI `y' = y·sen(t)` (T2) e `y' = y·cos(t)` (R2) son de la misma familia.
- **Newton-Raphson para una raíz de una ecuación trascendente con error dado** → **T1 Ej1b,
  T2 Ej1c, R2 Ej1b**; las ecuaciones `ln(0,5x) − sen(2x) = 0` (T1) y `e^{−2x} − sen(x) = 0`
  (R2) mezclan una función monótona con un seno (infinitas o varias raíces a separar
  gráficamente).

## Equivalencias (mismo archivo o mismo examen, no practicar dos veces)

- `duplicados/2025-1C_Recuperatorio_respuestas_copia.pdf` (llegó como `Respuestas 1er Rec 2do Parcial 1er Cuat 2025.pdf`) ≡ `resueltos/2025-1C_Recuperatorio_respuestas.pdf` (idénticos byte a byte, mismo MD5).
- `2025-1C_Parcial.pdf` contiene Tema 1 y Tema 2 en el mismo archivo (una página cada uno); cada tema se cuenta como hoja aparte, pero su **Ej2 es el mismo problema**.
- No hay dos hojas idénticas en el dataset; el reciclaje es a nivel de ejercicio (ver arriba).

## Fuera de dataset

- `resueltos/RESOLUCIONES-2025.md` — transcripción fiel (LaTeX) de las respuestas oficiales de las 4 hojas, para usar como ejercicios resueltos sin abrir los PDFs. No es un examen.
- `resueltos/2025-1C_Parcial_respuestas.pdf` y `resueltos/2025-1C_Recuperatorio_respuestas.pdf` — hojas de respuestas oficiales (OneNote manuscrito + tablas de planilla) del parcial y del 1er recuperatorio; sus enunciados ya están indexados arriba.

---

*Índice generado el 2026-11-18 a partir de la lectura (con visión) de 5 archivos originales, todos de 2025-1C (K3052): 2 PDFs tipeados de enunciados (parcial con Tema 1 y Tema 2, 1er recuperatorio) y 3 hojas OneNote de respuestas oficiales (parcial, 1er recuperatorio y 2do recuperatorio; esta última es la única fuente del enunciado del 2do recuperatorio). Un sexto archivo era copia byte a byte de las respuestas del 1er recuperatorio y fue a `duplicados/`.*
