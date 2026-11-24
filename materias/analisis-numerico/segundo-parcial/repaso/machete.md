# MACHETE — Análisis Numérico · Segundo parcial

> Hoja de repaso del último día: recetas, fórmulas y las frases que hay que dejar escritas. Sin ejemplos.
> Basado en las 4 hojas de 2025 (`examenes/INDICE.md`), el repaso 2026 y las guías `01`–`05`.
> 📄 = está en el ayudamemoria oficial (pág. 4) · 🧠 = va de memoria.
> Ajuste por mínimos cuadrados no entra.

## 0 · Tabla de decisión: ¿qué me están pidiendo?

| El enunciado dice… | Qué hago | Dónde |
|---|---|---|
| "Indique un intervalo de longitud 1 para cada raíz" | Separar en dos funciones conocidas, graficar, Bolzano | §1.1 |
| "¿Cuántas iteraciones de bisección…? ¿Suficientes o necesarias?" | Cota $\frac{b-a}{2^i}<\varepsilon$, redondear para arriba, "suficientes" | §1.3 |
| "Analice si puede usarse $g(x)$" / elegir entre dos $g$ | Las dos condiciones de punto fijo en todo el intervalo | §1.4 |
| "Halle la raíz con error menor que…" / "método conveniente" | Newton-Raphson con tabla | §1.5 |
| "¿Qué extremo se fija en Regula Falsi?" | Signos de $f'$ y $f''$ | §1.6 |
| "¿Converge Jacobi / Gauss-Seidel?" (sin resolver) | Escalera: diagonal dominante → norma de $T$ → radio espectral | §2.2 |
| "Valores de $k$ para que converja" | Una inecuación con módulo por fila, intersección | §2.4 |
| "Reordene y haga una iteración" | Reordenar filas, despejar, iterar | §2.3 y §2.5 |
| "¿Está bien condicionado?" | $K(A)=\lVert A\rVert\cdot\lVert A^{-1}\rVert$ | §2.7 |
| "Halle $a$, $b$, $k$ para que el polinomio sea de grado… / de menor grado" | Tabla solo con los puntos conocidos, evaluar $P$ en la $x$ tapada | §3.3 |
| "¿Cuántos polinomios de grado $n$ pasan?" / "¿de qué grado es?" | Regla del conteo y salto al máximo | §3.4 |
| "Derivada (primera o segunda) en un punto de la tabla" | Central si se puede; primero ⇒ progresiva; último ⇒ regresiva | §4.5 |
| "Mayor $h$ conveniente / número de subintervalos para error menor que…" | Cota del error de Trapecios, máximo de $\lvert f''\rvert$ | §4.2 |
| "¿Puede usarse Simpson con ese $h$?" | $N=(b-a)/h$ entero y par | §4.1 |
| "Trapecios, ¿da de más o de menos?" / "¿da exacto?" | Signo de $f''$ / grado del polinomio | §4.4 |
| "Halle si es posible la constante de Lipschitz" | $L=\max\left\lvert\partial f/\partial y\right\rvert$ en el dominio | §5.1 |
| "Aproxime $y(0{,}3)$ con Euler / Heun / Runge-Kutta" | Tabla del método | §5.2–5.4 |
| "¿Explícita o implícita? ¿De cuántos pasos?" | Buscar $w_{i+1}$ a la derecha; contar hasta el índice más viejo | §5.5 |

**Antes de arrancar cualquier ejercicio:** calculadora en **radianes** ($\operatorname{sen}(3)=0{,}1411$). Arrastrar 6 o 7 decimales y redondear solo la respuesta.

---

## 1 · Raíces (Ej1) — todo 🧠, el ayudamemoria no trae nada

### 1.1 Separar raíces (ítem a, siempre)

1. $f(x)=0$ → pasar términos hasta tener **una función conocida de cada lado**.
2. Graficar las dos en los mismos ejes, a escala (raíces y vértice de la parábola, asíntotas, período del seno).
3. Contar cruces y leer entre qué enteros cae cada uno.
4. Preguntarse qué pasa **más a la derecha y más a la izquierda**: la exponencial siempre le termina ganando a la polinómica (otro cruce más adelante, buscarlo con una tablita de enteros) y el logaritmo se va a $-\infty$ en $0$ (cruza cualquier cosa finita).
5. **Confirmar cada intervalo con Bolzano:** $f$ continua en $[a;a+1]$ y $f(a)\cdot f(a+1)<0$. Una línea por intervalo.

Ojo: Bolzano no vale si $f$ no existe o no es continua en el intervalo ($\ln x$ en $0$, $\frac{x}{x-1}$ en $1$). Si piden "para cada raíz", van **todos** los intervalos.

### 1.2 Cuándo parar

Columna $f(x_i)$ en la tabla; parar en la **primera fila con $\lvert f(x_i)\rvert<\varepsilon$** y escribirlo: "paro porque $\lvert f(x_i)\rvert<\varepsilon$". Esa fila tiene que estar escrita. "$n$ decimales exactos" = $\varepsilon<10^{-n}$.

Teórico: ese criterio vale si $\lvert f'\rvert>1$; con $f$ muy acostada se usa $\lvert x_{i+1}-x_i\rvert<\varepsilon$.

### 1.3 Bisección: cantidad de iteraciones (nunca se itera)

$$
\frac{b-a}{2^{i}}<\varepsilon\ \Longrightarrow\ i>\frac{\log_{10}\left(\frac{b-a}{\varepsilon}\right)}{\log_{10}2}\ \Longrightarrow\ \text{primer entero mayor}
$$

- $b-a$ es la **longitud**: $[a;a+1]$ mide 1, $[a-1;a+1]$ mide **2** (da una iteración más).
- Siempre se redondea **para arriba**.
- Frase obligatoria: "son **suficientes**, no necesarias: la fórmula es una cota, la precisión se puede alcanzar antes".
- No depende de $f$ ni del valor inicial: solo de la longitud y de $\varepsilon$.

### 1.4 Punto fijo: $x_{i+1}=g(x_i)$

Condiciones (las dos, en **todo** $[a,b]$; suficientes, no necesarias):

$$
g(x)\in[a,b]\qquad\text{y}\qquad\lvert g'(x)\rvert<1
$$

1. Condición 1: si $g$ es monótona, alcanza con $g(a)$ y $g(b)$ dentro de $[a,b]$. Decir que es monótona.
2. Condición 2: calcular $g'$; si $g'$ es monótona, evaluar en $a$ y $b$ **en módulo**. Si es un cociente, acotar numerador y denominador por separado.
3. Para descartar alcanza **un** contraejemplo; si falla una condición no hace falta mirar la otra.
4. Conclusión con las palabras justas: "se cumplen las dos ⇒ converge" / "no se cumple la condición N ⇒ **no se puede asegurar** la convergencia" (nunca "diverge").

Si hay que iterar: $x_0$ = punto medio o un extremo.

### 1.5 Newton-Raphson (el "método conveniente")

$$
x_{i+1}=x_i-\frac{f(x_i)}{f'(x_i)}
$$

1. Escribir $f$, $f'$ y la fórmula.
2. $x_0$ = punto medio o extremo del intervalo de la raíz pedida. Chequear y **escribir**: $\lvert f'(x_0)\rvert$ lejos de $0$ y $\left\lvert\frac{f(x_0)}{f'(x_0)}\right\rvert<1$. Mirar el **cociente entero**, no solo la derivada. Si no pasa, probar otro punto.
3. Tabla: $x_i$ · $f(x_i)$ · $f'(x_i)$ · $x_{i+1}$. Son 2 a 4 filas.
4. Parar como en §1.2 y recuadrar.

Derivadas que traicionan: $\left(\ln(0{,}5x)\right)'=\frac1x$ · $\left(e^{2x}\right)'=2e^{2x}$ · $\left(e^{-2x}\right)'=-2e^{-2x}$ · $\left(\operatorname{sen}(2x)\right)'=2\cos(2x)$.

### 1.6 Regula Falsi: solo qué extremo se fija

| Signos de $f'$ y $f''$ en el intervalo | Extremo fijo | Arranca en |
|---|---|---|
| **Iguales** | $b$ | $x_0=a$ |
| **Distintos** | $a$ | $x_0=b$ |

Justificar: Bolzano + signo de $f'$ y de $f''$ + que **ninguna cambia de signo** en el intervalo (si cambian, no se puede).

### 1.7 Teoría suelta

- Orden $p=1$ (lineal): bisección ($R=\frac12$), regula falsi, punto fijo ($R=\lvert g'(\alpha)\rvert$). Orden $p=2$: Newton-Raphson.
- Newton lento ⇒ raíz múltiple ($f(\alpha)=f'(\alpha)=0$).
- Fourier (suficientes, no necesarias): $f'$ sin ceros y $f''$ sin cambio de signo en $(a,b)$, y $x_0$ con $f(x_0)\cdot f''(x_0)>0$.

---

## 2 · Sistemas lineales (Ej2)

### 2.1 Tres herramientas 🧠

- **Diagonal dominante** (se mira en $A$): en cada fila $\lvert a_{ii}\rvert\ge\sum_{j\ne i}\lvert a_{ij}\rvert$. Contra la **suma** de los otros, todo en módulo. Estricta = con $>$ en todas las filas.
- **Normas de matriz:** infinito = mayor suma de módulos por **fila** (el ∞ está acostado); norma 1 = por **columna** (el 1 está parado). Norma infinito de un vector = mayor componente en módulo.
- **Radio espectral:** restar $\lambda$ en la diagonal, $\lvert T-\lambda I\rvert=0$ (📄), raíces, $\rho=\max\lvert\lambda_i\rvert$ (siempre positivo). Determinante $3\times3$: desarrollar por la fila o columna con más ceros. Con fracciones: multiplicar por el denominador común y probar $\lambda=\pm1$.

### 2.2 ¿Converge? Escalera de lo barato a lo caro

| Paso | Chequeo | Si se cumple | Si no se cumple |
|---|---|---|---|
| 1 | $A$ diagonal dominante | Convergen Jacobi **y** Gauss-Seidel | Nada: probar reordenar filas |
| 2 | $\lVert T\rVert_\infty<1$ o $\lVert T\rVert_1<1$ (alcanza una) | Ese método converge | Nada: seguir |
| 3 | $\rho(T)<1$ | Ese método converge | **No converge** |

- 1 y 2 son **suficientes**: no cumplirlas no dice nada. 3 es **necesaria y suficiente**: es la única que deja escribir "no converge".
- $T_J\ne T_{GS}$: puede converger uno y el otro no (el que suele converger es Gauss-Seidel).
- Cerrar con la frase: "condición suficiente ⇒ converge" / "condición necesaria y suficiente y $\rho\ge1$ ⇒ no converge". Es la mitad del ítem.
- $\ge$ o $>$: plantear con $\ge$ (como la resolución oficial) y agregar "en sentido estricto, que es lo que garantiza el teorema, los extremos se excluyen".

### 2.3 Reordenar filas

En cada ecuación, el coeficiente más grande en módulo dice a qué fila va (el de $x$ ⇒ primera, el de $y$ ⇒ segunda…). Se mueve la ecuación **entera, con su término independiente**. Después escribir las desigualdades de la matriz reordenada. Si dos ecuaciones piden la misma fila, no se puede.

### 2.4 Hallar $k$ para que converja

1. Una inecuación por fila: $\lvert\text{diagonal}\rvert\ge$ suma de los módulos de los otros.
2. Abrir el módulo: $\lvert u\rvert\ge c\ \Leftrightarrow\ u\ge c\ \vee\ u\le-c$.
3. Al pasar un $-k$ o multiplicar por $-1$, **se da vuelta** la desigualdad.
4. Respuesta = **intersección** de todas las filas (recta numérica). Puede quedar un punto suelto donde se tocan dos intervalos; en la versión estricta desaparece.

### 2.5 Iterar

- **Jacobi:** despejar la incógnita $i$ de la ecuación $i$; reemplazar **todo** con el vector anterior. Sin dato, $X^{(0)}$ = vector nulo.
- **Gauss-Seidel:** mismos despejes, pero cada valor nuevo se usa **enseguida** (escribir el vector e ir pisando). Es **el doble de rápido** (mitad de iteraciones). Autocontrol: la primera componente da igual que en Jacobi; desde la segunda, no.
- **Parar** (igual para los dos): restar componente a componente **con sus signos**, después módulo, quedarse con la mayor.

$$
\lVert X^{(k)}-X^{(k-1)}\rVert_\infty<\varepsilon\quad\text{(absoluto)}\qquad\frac{\lVert X^{(k)}-X^{(k-1)}\rVert_\infty}{\lVert X^{(k)}\rVert_\infty}<\varepsilon\quad\text{(relativo)}
$$

### 2.6 Matrices $T$ y $C$

- **A mano, $T_J$ sale de los despejes:** a cada fila de $A$ sacarle la diagonal, **cambiarle el signo** a los demás y **dividir por el elemento de la diagonal** (ojo si es negativo). Diagonal de $T_J$ = ceros. $C_J$ = términos independientes de los despejes. Desde el vector nulo, $X^{(1)}=C_J$.
- 📄 $T_J=D^{-1}(L+U)$, $C_J=D^{-1}B$; $T_{GS}=(D-L)^{-1}U$, $C_{GS}=(D-L)^{-1}B$. Esas fórmulas usan $A=D-L-U$: $L$ y $U$ ya traen **el signo cambiado**.
- $T_{GS}$ tiene ceros en la **primera columna** y no se pide a mano (a lo sumo la dan).

### 2.7 Número de condición

$$
K(A)=\lVert A\rVert_\infty\cdot\lVert A^{-1}\rVert_\infty\ \ge\ 1
$$

1. Norma infinito de $A$ y de $A^{-1}$ (la inversa la dan), **con módulos** y la **misma norma** en las dos.
2. Multiplicar y **concluir con una frase**: unidades (3; 10) ⇒ bien condicionado, los errores casi no se amplifican; miles ⇒ mal condicionado, no se puede confiar en la solución; zona gris (≈50) ⇒ decidir y justificar por escrito.
3. Si da menor que 1, sumaste con signos.

Inversa $2\times2$: $\begin{pmatrix}a&b\\c&d\end{pmatrix}^{-1}=\dfrac{1}{ad-bc}\begin{pmatrix}d&-b\\-c&a\end{pmatrix}$.

---

## 3 · Interpolación (Ej3) — casi todo 🧠

### 3.1 El teorema y sus dos consecuencias

- **Teorema:** por $n+1$ puntos pasa un **único** polinomio de grado **menor o igual** a $n$.
- **Agregar un punto:** evaluar $P$ en la $x$ nueva. Da la $y$ nueva ⇒ mismo polinomio, mismo grado. No da ⇒ el grado **salta al máximo** (cantidad de puntos menos 1), sin pasar por los intermedios.
- Con $m$ puntos hay **infinitos** polinomios de cada grado $\ge m$.

### 3.2 Tabla de diferencias divididas y polinomio de Newton

1. Columnas $x$, $y$.
2. **O1:** resta de $y$ sobre resta de sus $x$. **O2:** resta de dos O1 consecutivos sobre la resta de $x$ **salteando una**. **O3:** salteando dos. El denominador es siempre "última $x$ menos primera $x$" de los puntos que abarca.
3. Siempre **abajo menos arriba**, en numerador y denominador.
4. **Grado = última columna no nula** (columna constante ⇒ la siguiente se anula).

$$
P(x)=y_0+f[x_0,x_1](x-x_0)+f[x_0,x_1,x_2](x-x_0)(x-x_1)+f[x_0,\dots,x_3](x-x_0)(x-x_1)(x-x_2)+\dots
$$

- Coeficientes = **diagonal de arriba** (primer valor de cada columna). Los factores van en el orden de las filas y el último punto **no** aparece como factor.
- Regresivo: misma tabla, **diagonal de abajo** (último valor de cada columna) y factores con las $x$ de abajo hacia arriba. Se elige la diagonal con números más simples.
- Se deja **sin distribuir**.

### 3.3 Ítem a: hallar los valores tapados

Regla del profesor: **no meter la letra en la tabla**.

1. Sacar las filas con letras.
2. Si piden **grado $g$**: usar $g+1$ puntos conocidos. Si piden "**menor grado**": usar todos los conocidos.
3. Tabla + polinomio de Newton.
4. **Verificar los puntos conocidos que sobraron** evaluando $P$ en su $x$. Si alguno no da ⇒ no existe valor de la letra (por eso el "si es posible").
5. Letra $=P(\text{su }x)$. Cuidado con los signos al evaluar: a la izquierda de los datos todos los factores son negativos.

| La consigna dice… | Respuesta |
|---|---|
| "menor grado" / "grado $g$" | letra $=P(\text{su }x)$ |
| "grado máximo, pero por los primeros pase uno de grado $g$" | la de los primeros $=P(\text{su }x)$; la otra **≠** $P(\text{su }x)$ |
| "para los demás valores, ¿qué grado?" | cantidad de puntos menos 1 |

### 3.4 Ítems b y c: contar polinomios

$m$ puntos (en el parcial, 6), interpolante de grado $g$. ¿Cuántos de grado $d$ pasan por todos?

| $d<g$ | $d=g$ | $g<d\le m-1$ | $d\ge m$ |
|---|---|---|---|
| ninguno | uno | ninguno | infinitos |

Frase modelo: "Son 6 puntos: por el teorema de existencia y unicidad pasa un único polinomio de grado $\le5$, y ese es el de grado $g$. Entonces de grado [entre $g+1$ y 5] no hay ninguno. De grado 6 o más hay infinitos, porque con $m$ puntos hay infinitos polinomios de grado $\ge m$". El número sin la frase no alcanza.

### 3.5 Por si aparece

- **Lagrange** (solo si lo piden): $P(x)=\sum\dfrac{y_i}{L_i(x_i)}\,L_i(x)$ con $L_i(x)=\prod_{k\ne i}(x-x_k)$. No muestra el grado.
- **Equiespaciados** (📄 diferencias finitas, sin dividir): $a_i=\dfrac{\Delta^if_0}{i!\,h^i}$, $b_i=\dfrac{\nabla^if_n}{i!\,h^i}$.
- **Usar el polinomio:** dentro del rango sí; fuera no es recomendable.
- **¿Interpolar o aproximar?** Pocos datos exactos ⇒ interpolar. Mediciones, muchos puntos, tendencia o forma conocida ("siempre creciente") ⇒ aproximar.

---

## 4 · Integración y derivación numérica (Ej4)

### 4.1 Calcular

$N=\dfrac{b-a}{h}$: entero para Trapecios, **entero y par** para Simpson (esa es toda la respuesta a "¿se puede usar Simpson con este $h$?").

$$
A_T=\frac h2\,(E+2M)\qquad\qquad A_S=\frac h3\,(E+4I+2P)
$$

$E$ = primero + último · $M$ = todos los del medio · $I$ = subíndices **impares** (van con el 4) · $P$ = pares que no son extremos. Tabla $i$ · $x_i$ · $y_i$. 🧠

### 4.2 Elegir $h$ o $N$ para Trapecios (4/4 en 2025)

$$
\frac{b-a}{12}\,h^{2}\max_{[a,b]}\lvert f''\rvert<\varepsilon
$$

1. Plantear la cota (📄, con módulo y máximo). Intervalo de longitud 2 ⇒ $\frac{h^2}{6}K<\varepsilon$. El coeficiente es $\frac{b-a}{12}$, no $\frac1{12}$.
2. Derivar hasta $f''$ y factorizar. Atajo: $\left(e^{x}p\right)'=e^{x}(p+p')$ y $\left(e^{-x}p\right)'=e^{-x}(p'-p)$.
3. $K=\max\lvert f''\rvert$ en $[a,b]$:
   - Si $f''$ es monótona en el intervalo: evaluar en los dos extremos. **Decir** por qué es monótona.
   - Si no: escribir "no veo a ojo que sea creciente o decreciente en el intervalo", resolver $f'''=0$ (no $f''=0$), quedarse con los puntos críticos **dentro** de $[a,b]$ y evaluar $f''$ en **extremos y críticos**. $K$ = el mayor **en módulo**.
4. Despejar: $h<\sqrt{\dfrac{12\,\varepsilon}{(b-a)\,K}}$.
5. $N>\dfrac{b-a}{h_{\text{cota}}}$ ⇒ entero siguiente.
6. Subir $N$ de a uno hasta que $h=\frac{b-a}{N}$ sea un decimal finito y corto: es el **mayor** $h$ conveniente, así que no saltearse opciones lindas ni quedarse con un periódico. Con intervalo de longitud 2 sirven $N=4,5,8,10,16,20,25,32,40,50$ → $h=0{,}5;\ 0{,}4;\ 0{,}25;\ 0{,}2;\ 0{,}125;\ 0{,}1;\ 0{,}08;\ 0{,}0625;\ 0{,}05;\ 0{,}04$.
7. Responder con $h$ **y** $N$.

### 4.3 Lo mismo para Simpson

$$
\frac{b-a}{180}\,h^{4}\max_{[a,b]}\lvert f^{IV}\rvert<\varepsilon\qquad\Rightarrow\qquad h<\sqrt[4]{\frac{180\,\varepsilon}{(b-a)\,K}}
$$

Derivada **cuarta** (críticos con la quinta), raíz **cuarta**, y $N$ además **par**.

### 4.4 Conceptuales

| Pregunta | Respuesta |
|---|---|
| ¿Trapecios exacto? | Polinomio de grado $\le1$ ($f''=0$) |
| ¿Simpson exacto? | Polinomio de grado $\le3$ ($f^{IV}=0$) |
| Función impar en $[-a;a]$ | Exacto con los dos. El recíproco ("dio exacto ⇒ es polinomio") es **falso** |
| $f''>0$ en todo $[a,b]$ | Trapecios da **de más** (exceso) |
| $f''<0$ en todo $[a,b]$ | Trapecios da **de menos** (defecto) |
| $f''$ cambia de signo | No se puede concluir |
| ¿Simpson siempre gana? | No: $\lvert x\rvert$ en $[-1;1]$ con $h=1$ |

Concavidad: mostrar que $f''$ no cambia de signo en **todo** el intervalo, no en un punto. No depende de $h$. Si no me acuerdo, el dibujito: cóncava hacia arriba ⇒ la cuerda queda por encima.

### 4.5 Derivadas desde una tabla ($h$ fijo)

| | $f'(x_i)$ | $f''(x_i)$ |
|---|---|---|
| Progresiva 📄 | $\dfrac{f_{i+1}-f_i}{h}$ | $\dfrac{f_{i+2}-2f_{i+1}+f_i}{h^{2}}$ |
| Regresiva 📄 | $\dfrac{f_i-f_{i-1}}{h}$ | $\dfrac{f_i-2f_{i-1}+f_{i-2}}{h^{2}}$ |
| Central 🧠 | $\dfrac{f_{i+1}-f_{i-1}}{2h}$ | $\dfrac{f_{i+1}-2f_i+f_{i-1}}{h^{2}}$ |

(El ayudamemoria trae solo los numeradores $\Delta$ y $\nabla$; hay que dividir por $h$ o $h^2$.)

- "Fórmula conveniente" = **central** siempre que se pueda. Primer dato ⇒ solo progresiva. Último dato ⇒ solo regresiva.
- La central de la primera divide por $2h$ y **no usa $f_i$**.
- Los puntos usados tienen que estar a la **misma distancia**. En una tabla despareja, buscar tres consecutivos equiespaciados alrededor del punto.
- Punto que no está en la tabla pero cae en el medio de dos: central con esos dos y $h'$ = mitad del paso.
- No confundir el paso con una letra de la tabla que también se llame $h$.

---

## 5 · Ecuaciones diferenciales (Ej5)

Siempre primero: **despejar $y'$** para tener $f(t,y)$. $w_0$ = dato inicial. Cantidad de filas $=(t_{\text{final}}-t_0)/h$.

### 5.1 Lipschitz 🧠

$$
\lvert f(t,y_1)-f(t,y_2)\rvert\le L\,\lvert y_1-y_2\rvert\qquad\text{o}\qquad L=\max_{R}\left\lvert\frac{\partial f}{\partial y}\right\rvert
$$

1. Derivar respecto de **$y$** ($t$ constante; lo que no tiene $y$ desaparece).
2. Módulo.
3. Máximo en el dominio, factor por factor: creciente ⇒ extremo de **mayor módulo** ($y\in[-4;3]$ con $y^2$ ⇒ $y=-4$); variable en el **denominador** ⇒ el valor **más chico**; seno o coseno ⇒ ver si el $\pm1$ cae adentro.
4. Frase: "$\left\lvert\frac{\partial f}{\partial y}\right\rvert$ está acotada en $R$ ⇒ cumple Lipschitz con $L=\dots$; como además $f$ es continua en $R$, el problema está **bien planteado** (solución única)".

No se puede: derivada no acotada en el dominio, o depende de $y$ y no dan el intervalo de $y$. El intervalo de $t$ sí se deduce (del $t$ inicial al $t$ pedido). "De dos formas" = además por la definición: restar, sacar factor común $\lvert y_1-y_2\rvert$ y acotar lo que queda.

### 5.2 Euler 📄 — explícito, 1 paso, orden 1

$$
w_{i+1}=w_i+h\,f(t_i,w_i)
$$

Tabla: $t_i$ · $w_i$ · $f(t_i,w_i)$ · $w_{i+1}$. Todo con datos de la **misma fila**. $y(0{,}3)$ con $h=0{,}1$ es $w_3$: el $w_{i+1}$ de la fila $t_i=0{,}2$ (3 filas).

### 5.3 Heun = Euler modificado 📄 — implícito (corrector, con Euler de predictor), 1 paso, orden 2

$$
w^*_{i+1}=w_i+h\,f(t_i,w_i)\qquad w_{i+1}=w_i+\frac h2\Big(f(t_i,w_i)+f(t_{i+1},w^*_{i+1})\Big)
$$

Tabla: $t_i$ · $w_i$ · $f(t_i,w_i)$ · $w^*_{i+1}$ · $f(t_{i+1},w^*_{i+1})$ · $w_{i+1}$. El segundo $f$ va con $t_{i+1}$. A la fila siguiente pasa el $w_{i+1}$ **corregido**, no el $w^*$.

### 5.4 Runge-Kutta 4 📄 — explícito, 1 paso, orden 4

$$
\begin{gathered}
w_{i+1}=w_i+\tfrac16(k_1+2k_2+2k_3+k_4) \\[6pt]
k_1=h\,f(t_i,w_i)\quad k_2=h\,f\!\left(t_i+\tfrac h2,\,w_i+\tfrac{k_1}{2}\right)\quad k_3=h\,f\!\left(t_i+\tfrac h2,\,w_i+\tfrac{k_2}{2}\right)\quad k_4=h\,f(t_i+h,\,w_i+k_3)
\end{gathered}
$$

Copiar del ayudamemoria y controlar: cada $k$ lleva su $h$; $k_2$ y $k_3$ usan $t_i+\frac h2$ y **la mitad** del $k$ anterior; $k_4$ usa $t_i+h$ y $k_3$ **entero**. Tabla: $t_i$ · $w_i$ · $k_1$ · $k_2$ · $k_3$ · $k_4$ · $w_{i+1}$.

### 5.5 Clasificar una fórmula 🧠

- ¿Aparece $w_{i+1}$ **a la derecha** (suele estar dentro de un $f(t_{i+1},w_{i+1})$)? Sí ⇒ **implícita** (solo correctora). No ⇒ **explícita** (sola o predictora).
- **Pasos:** desde $w_i$ hasta el índice más viejo. Índice $i-k$ ⇒ $k+1$ pasos. $w_{i+1}$ **no cuenta**; los intermedios que faltan **sí**.
- Multipaso de la cátedra (solo para nombrar): Adams-Bashforth (explícitos), Adams-Moulton (implícitos), Milne-Simpson.

### 5.6 Teoría corta

| Método | Orden | Si $h$ baja a la mitad, el error global baja a | Exacto si $y(t)$ es |
|---|---|---|---|
| Euler | 1 | $\frac12$ | lineal |
| Heun | 2 | $\frac14$ | polinomio de grado $\le2$ |
| Runge-Kutta 4 | 4 | $\frac1{16}$ | polinomio de grado $\le4$ |

- Heun es de **orden 2** (el teórico dice 3: es errata).
- Runge-Kutta y Heun dan la precisión de Taylor de orden superior **sin calcular derivadas**.
- Euler, Heun y Runge-Kutta son de **paso simple**.
- Achicar $h$ mejora la precisión hasta que crecen los errores operativos.

Presentación: $f$ despejada, dato inicial, fórmula del método, tabla y el resultado señalado ("$y(0{,}3)\approx\dots$").

---

## 6 · Las frases que valen puntos

| Situación | Lo que hay que escribir |
|---|---|
| Iteraciones de bisección | "Son **suficientes**, no necesarias: es una cota" |
| Falla una condición de punto fijo | "**No se puede asegurar** la convergencia" |
| $A$ no es diagonal dominante o $\lVert T\rVert\ge1$ | "Es condición suficiente: no se puede concluir, voy al radio espectral" |
| $\rho(T)\ge1$ | "Condición necesaria y suficiente ⇒ **no converge**" |
| Calculé $K(A)$ | "…⇒ bien / mal condicionado" |
| Conteo de polinomios | Nombrar el teorema de existencia y unicidad |
| Máximo de $\lvert f''\rvert$ | "Es monótona en el intervalo" o "no veo a ojo que sea creciente o decreciente" |
| Elegí $x_0$ en Newton | Derivada lejos de 0 y cociente menor que 1 |
| Frené una iteración | "Paro porque $\lvert f(x_i)\rvert<\varepsilon$" |
| Lipschitz | "Derivada parcial acotada + $f$ continua ⇒ bien planteado" |

En esta materia casi todas las condiciones son **suficientes, no necesarias**, y los recíprocos no valen. La única necesaria y suficiente es $\rho(T)<1$.

## 7 · OJO — errores que cuestan puntos

- **Raíces:** longitud 1 cuando el intervalo es $[a-1;a+1]$; redondear las iteraciones para abajo; chequear $\lvert g'\rvert<1$ en un solo punto u olvidar el módulo; mirar solo la derivada al elegir $x_0$; parar una fila antes.
- **Sistemas:** hacer Jacobi cuando piden Gauss-Seidel; reordenar sin mover el término independiente; signos de $T_J$ (cambian y se dividen por la diagonal); mirar la diagonal dominante en $T$ o la norma en $A$; cruzar filas y columnas en las normas; unión donde va intersección; no dar vuelta la desigualdad con $-k$.
- **Interpolación:** dividir por la resta de $x$ equivocada en O2 y O3; restar al revés en una parte sola; tomar coeficientes de una fila en vez de la diagonal; no verificar los puntos que sobran; poner "=" cuando el grado tiene que saltar (va ≠); decir que el grado "sube uno"; contestar "uno" para un grado entre $g$ y $m-1$; distribuir sin que lo pidan.
- **Integración:** redondear la cota en vez de elegir un $h$ que dé $N$ entero; irse demasiado abajo con $h$; evaluar $f''$ solo en los extremos sin justificar; usar un punto crítico de afuera del intervalo; signos al derivar $e^{-x}$; Simpson con $N$ impar o con el 4 y el 2 cruzados; $h$ en vez de $\frac h2$ o $\frac h3$; central dividida por $h$ en vez de $2h$.
- **Ecuaciones diferenciales:** no despejar $y'$; una fila de más o de menos; en Heun pasar el $w^*$ a la fila siguiente; en Runge-Kutta $k_1$ entero dentro de $k_2$ o $\frac{k_3}{2}$ dentro de $k_4$; derivar respecto de $t$ en Lipschitz; contar $w_{i+1}$ como paso; decir que Heun es explícito.

## 8 · Datos de las hojas 2025 para comparar después de practicar

| Hoja | Ejercicio | Resultado oficial |
|---|---|---|
| T1 | Ej4: $\int_{-7}^{-5}e^{x}(x^{3}-6)\,dx$, $\varepsilon<10^{-3}$ | $h=0{,}2$ |
| T2 | Ej4: $\int_{0}^{2}e^{x}(x^{2}-9x+23)\,dx$, $\varepsilon<10^{-2}$ | $h=0{,}08$ |
| R1 | Ej4: $\int_{1}^{3}\frac{\ln(x)+1}{x}\,dx$, $\varepsilon<10^{-2}$ | $h=0{,}2$ (máximo en el extremo, $f''(1)=-1$) |
| R2 | Ej4: $\int_{4}^{6}e^{-x}(x^{2}-1)\,dx$, $\varepsilon\le10^{-3}$ | $N=8$ ($h=0{,}25$) |
| T1 / T2 | Ej2: ¿converge Jacobi? | $\rho(T_J)=1$ ⇒ no converge (Gauss-Seidel sí) |
| T1 / T2 | Ej5 a: Lipschitz | $L=2$ / $L=1$ |
| T1 / T2 / R2 | Ej1: $x_0$ de Newton | $1{,}5$ en $[1;2]$ / $-0{,}5$ en $[-1;0]$ / $3$ en $[3;4]$ |
| Repaso 2026 | Ej. 13: Lipschitz | $L=96$ |

---
*Generado el 2026-11-24 desde las guías `apuntes/md/01`–`05` (resúmenes, recetas y errores típicos), `estrategia.md` y `examenes/INDICE.md`. Iterar sobre este .md; exportar con `/machete --html` o `/machete --pdf`.*
