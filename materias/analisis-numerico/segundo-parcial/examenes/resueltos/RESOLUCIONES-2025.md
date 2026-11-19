# Resoluciones oficiales del 2do parcial — 1C 2025 (K3052)

> Fuente: `2025-1C_Parcial_respuestas.pdf` (hoja OneNote de la cátedra fechada 2025-06-30, Tema 1 y Tema 2), `2025-1C_Recuperatorio_respuestas.pdf` (fechada 2025-07-07) y `2025-1C_Recuperatorio-2_respuestas.pdf` (fechada 2025-07-11), curso K3052. Enunciados completos en `../INDICE.md`. Transcripción fiel de lo que está escrito en cada hoja: los pasos son los de la fuente, sin agregar ninguno. Las iteraciones y los ajustes están hechos en planilla de cálculo y la hoja solo muestra la tabla de valores; los gráficos se describen entre corchetes. Donde la hoja da únicamente el resultado se marca **(solo resultado en la fuente)**. Las hojas usan coma decimal en lo manuscrito y punto decimal en las tablas de planilla; acá se respeta cada uno.

---

## Parcial — Tema 1

### Ej1 — Raíces de $\ln(0{,}5x) - \operatorname{sen}(2x) = 0$

**Ítem a) — un intervalo $[a; a+1]$, $a \in \mathbb{Z}$, para cada raíz**

[Gráfico: $\operatorname{sen}(2x)$ y $\ln(0{,}5x)$ superpuestos; se cortan tres veces.]

- 1 raíz en $[1; 2]$
- 1 raíz en $[3; 4]$
- 1 raíz en $[4; 5]$

(solo resultado en la fuente, leído del gráfico)

**Ítem b) — raíz más cercana a 0 con $\varepsilon < 10^{-4}$**

"Más rápido es Newton-Raphson":

| $x_i$ | $f(x_i)$ | $f'(x_i)$ | $x_{i+1}$ |
|---|---|---|---|
| 1.50000 | -0.42880 | 2.64665 | 1.66202 |
| 1.66202 | -0.00368 | 2.56849 | 1.66345 |
| **1.66345** | 0.00000 | 2.56692 | 1.66345 |

**Resultado:** $x \approx 1{,}66345$ (resaltado en la tabla).

**Ítem c) — iteraciones de bisección en $[a-1, a+1]$ para $\varepsilon < 10^{-7}$**

$$
\frac{2}{2^{i}} < 10^{-7}
$$

$$
2^{1-i} < 10^{-7}
$$

$$
1 - i < \frac{-7}{\log_{10} 2}
$$

$$
i > 24{,}25\ldots
$$

**Resultado:** suficientes **25** iteraciones.

### Ej2 — ¿Converge Jacobi? Sistema $7x+5y+4z=10$, $3x+4y+2z=3$, $x+y+4z=-8$

**Paso 1:** despeja cada incógnita.

$$
\begin{cases}
x = -\dfrac{5}{7}\,y - \dfrac{4}{7}\,z + \dfrac{10}{7} \\[2mm]
y = -\dfrac{3}{4}\,x - \dfrac{1}{2}\,z + \dfrac{3}{4} \\[2mm]
z = -\dfrac{1}{4}\,x - \dfrac{1}{4}\,y - 2
\end{cases}
$$

**Paso 2:** matriz de iteración de Jacobi.

$$
T_J = \begin{pmatrix} 0 & -5/7 & -4/7 \\ -3/4 & 0 & -1/2 \\ -1/4 & -1/4 & 0 \end{pmatrix}
$$

**Paso 3:** radio espectral. Autovalores:

$$
\begin{vmatrix} -\lambda & -5/7 & -4/7 \\ -3/4 & -\lambda & -1/2 \\ -1/4 & -1/4 & -\lambda \end{vmatrix} = 0
$$

$$
-\lambda\left(\lambda^{2} - \frac{1}{8}\right) + \frac{5}{7}\left(\frac{3}{4}\lambda - \frac{1}{8}\right) - \frac{4}{7}\left(\frac{3}{16} - \frac{1}{4}\lambda\right) = 0
$$

$$
-\lambda^{3} + \frac{1}{8}\lambda + \frac{15}{28}\lambda - \frac{5}{56} - \frac{3}{28} + \frac{1}{7}\lambda = 0
$$

$$
-\lambda^{3} + \frac{45}{56}\lambda - \frac{11}{56} = 0
$$

**Paso 4:** $\lambda_1 = -1$ ("a ojo"). Nota de la hoja: *"Ya sabiendo que hay al menos un $|\lambda| \geq 1$ alcanza"*. Igual factoriza por Ruffini con $-1$ (coeficientes $-1,\ 0,\ 45/56,\ -11/56$ → $-1,\ 1,\ -11/56$, resto $0$):

$$
P(\lambda) = (\lambda + 1)\left(-\lambda^{2} + \lambda - \frac{11}{56}\right)
$$

$$
\lambda_1 = -1 \qquad \lambda_2 \approx 0{,}26854 \qquad \lambda_3 \approx 0{,}73146
$$

**Resultado:** radio espectral $\rho = 1$ ⇒ "Puedo asegurar que **NO** converge".

### Ej3 — Tabla $x = 1, 2, 4, 5, 6, 8$; $y = 0{,}5,\ a,\ 41,\ 74{,}5,\ 123,\ b$

**Ítems a) y b)**

**Paso 1:** diferencias divididas con los puntos conocidos $x = 1, 4, 5, 6$ (deja afuera $x=2$ y $x=8$):

| $x$ | $y$ | O1 | O2 | O3 |
|---|---|---|---|---|
| 1 | 0,5 | | | |
| | | $27/2$ | | |
| 4 | 41 | | $5$ | |
| | | $67/2$ | | $1/2$ |
| 5 | 74,5 | | $15/2$ | |
| | | $97/2$ | | |
| 6 | 123 | | | |

**Paso 2:** polinomio de grado 3 por esos cuatro puntos.

$$
P(x) = \frac{1}{2} + \frac{27}{2}(x-1) + 5(x-1)(x-4) + \frac{1}{2}(x-1)(x-4)(x-5)
$$

**Paso 3:** evalúa en las abscisas de los valores desconocidos.

$$
P(2) = a = 7 \qquad P(8) = b = 277
$$

**Resultado a):** debe ser $a = 7$ y $b \neq 277$.

**Resultado b):** grado 4 ⇒ $\varnothing$ (ninguno); grado 5 ⇒ $\infty$ (uno para cada $b \neq 277$); grado 6 ⇒ $\infty$.

**Ítem c) — recta de mínimos cuadrados con $a = 15$, $b = 150$**

| $x$ | $y$ | $x^2$ | $xy$ |
|---|---|---|---|
| 1 | 0.5 | 1 | 0.5 |
| 2 | 15 | 4 | 30 |
| 4 | 41 | 16 | 164 |
| 5 | 74.5 | 25 | 372.5 |
| 6 | 123 | 36 | 738 |
| 8 | 150 | 64 | 1200 |
| **Suma: 26** | **404** | **146** | **2505** |

Sistema (matriz, términos independientes, inversa y solución tal como están en la planilla):

$$
\begin{pmatrix} 6 & 26 \\ 26 & 146 \end{pmatrix}\begin{pmatrix} a_0 \\ a_1 \end{pmatrix} = \begin{pmatrix} 404 \\ 2505 \end{pmatrix}
\qquad
\text{inversa} \approx \begin{pmatrix} 0.73 & -0.13 \\ -0.13 & 0.03 \end{pmatrix}
\qquad
\text{solución: } \begin{pmatrix} -30.73 \\ 22.63 \end{pmatrix}
$$

**Resultado:** $y = 22{,}63\,x - 30{,}73$ (ecuación de la línea de tendencia del gráfico de la planilla).

### Ej4 — Mayor $h$ para Trapecios, $\int_{-7}^{-5} e^{x}(x^{3}-6)\,dx$, $\varepsilon < 10^{-3}$

**Paso 1:** cota del error.

$$
\frac{2}{12}\cdot h^{2}\cdot \max_{-7 \le \alpha \le -5} |f''(\alpha)| < 10^{-3}
$$

**Paso 2:** derivadas.

$$
f(x) = e^{x}(x^{3}-6)
$$

$$
f'(x) = e^{x}(x^{3}-6) + e^{x}(3x^{2}) = e^{x}(x^{3}+3x^{2}-6)
$$

$$
f''(x) = e^{x}(x^{3}+3x^{2}-6) + e^{x}(3x^{2}+6x) = e^{x}(x^{3}+6x^{2}+6x-6)
$$

Nota de la hoja: *"No veo a ojo que sea creciente o decreciente en el intervalo"*.

$$
f'''(x) = e^{x}(x^{3}+6x^{2}+6x-6) + e^{x}(3x^{2}+12x+6) = e^{x}(x^{3}+9x^{2}+18x)
$$

**Paso 3:** puntos críticos de $f''$. El paréntesis se anula cuando $x = 0$ y en

$$
\frac{-9 \pm \sqrt{81 - 4\cdot 1\cdot 18}}{2} \;\Rightarrow\; x_2 = \frac{-9+3}{2} = -3 \qquad x_3 = \frac{-9-3}{2} = -6
$$

**Paso 4:** "Comparo extremos y puntos críticos en el intervalo":

$$
f''(-5) = -0{,}0741 \quad \text{vs.} \quad f''(-7) = -0{,}0885 \quad \text{vs.} \quad \boxed{f''(-6) = -0{,}1041}
$$

**Paso 5:**

$$
\frac{h^{2}}{6}\cdot 0{,}1041 < 10^{-3} \;\Rightarrow\; h < 0{,}24007
$$

**Resultado:** "Podemos tomar $h = 0{,}2$" ($N = 10$).

### Ej5 — PVI $y'(t) + 2y(t)^{2} = \dfrac{1}{1+t^{2}}$, $y(0)=0$, $t \in [0;1]$

$$
y'(t) = \frac{1}{1+t^{2}} - 2y^{2}
$$

**Ítem a) — constante de Lipschitz con $y \in [0; 0{,}5]$**

$$
\left|\frac{\partial f(t,y)}{\partial y}\right| = |4y| = L \quad \text{con } y \in [0; 0{,}5]
$$

**Resultado:** $L = 2$.

**Ítem b) — $y(0.3)$ por Euler con $h = 0.1$**

| $t_i$ | $w_i$ | $w_{i+1}$ |
|---|---|---|
| 0 | 0 | 0.1 |
| 0.1 | 0.1 | 0.1970099 |
| 0.2 | 0.1970099 | **0.28540117** |

**Resultado:** $y(0.3) \approx 0{,}28540117$ (resaltado en la tabla).

---

## Parcial — Tema 2

### Ej1 — Raíces de $e^{2x} - x^{2} - 3x - 2 = 0$

**Ítem a) — un intervalo $[a, a+1]$ para cada raíz**

Reescribe $e^{2x} = x^{2} + 3x + 2$ y estudia la parábola:

- Raíces de la parábola en $-1$ y $-2$: $\dfrac{-3 \pm \sqrt{9 - 4\cdot 1\cdot 2}}{2}$
- Vértice en $\left(-\dfrac{3}{2},\ -\dfrac{1}{4}\right)$

[Gráfico: la parábola y $e^{2x}$ superpuestas; se cortan tres veces.]

**Resultado:** 1 raíz en $[-3; -2]$, 1 raíz en $[-1; 0]$, 1 raíz en $[0; 1]$.

**Ítem b) — ¿sirve $g(x) = \tfrac12 \ln(x^{2}+3x+2)$ en $[0,1]$?**

**Paso 1:** función creciente: se mueve entre

$$
[g(0);\ g(1)] = [0{,}3466;\ 0{,}8959] \subset [0,1] \ \checkmark
$$

**Paso 2:**

$$
g'(x) = \frac{2x+3}{2x^{2}+6x+4}
$$

- El numerador, en $[0,1]$, se mueve entre $[3; 5]$.
- El denominador, en $[0,1]$, se mueve entre $[4; 12]$. (Ambas crecientes.)

"Siempre es más grande el denominador que el numerador" ⇒

$$
|g'(x_i)| < 1 \quad \forall x_i \in [0,1] \ \checkmark
$$

**Resultado:** "Se puede usar esa $g(x)$ para esa raíz".

**Ítem c) — raíz negativa más cercana a 0 por Newton-Raphson, $\varepsilon < 10^{-4}$**

| $x_i$ | $f(x_i)$ | $f'(x_i)$ | $x_{i+1}$ |
|---|---|---|---|
| -0.5 | -0.3821206 | -1.2642411 | -0.8022529 |
| -0.8022529 | -0.0358621 | -0.9935165 | -0.8383491 |
| -0.8383491 | -0.0007916 | -0.9493211 | **-0.8391829** |
| **-0.8391829** | -4.354E-07 | | |

**Resultado:** $x \approx -0{,}8391829$ (resaltado en la tabla).

### Ej2 — ¿Converge Jacobi? (mismo sistema que el Tema 1)

"Ídem Tema 1" (ver Parcial — Tema 1, Ej2: $\rho = 1$, no converge).

### Ej3 — Tabla $x = 1,\ 1{,}5,\ 2,\ 2{,}5,\ 3,\ 4$; $y = 7{,}8,\ 14{,}675,\ K,\ 50{,}625,\ 84{,}2,\ 193{,}8$

**Ítem a) — $k$ para que el interpolante sea de grado 3, y el polinomio**

**Paso 1:** diferencias divididas con $x = 1,\ 1{,}5,\ 2{,}5,\ 3$:

| $x$ | $y$ | O1 | O2 | O3 |
|---|---|---|---|---|
| 1 | 7,8 | | | |
| | | 13,75 | | |
| 1,5 | 14,675 | | 14,8 | |
| | | 35,95 | | 3 |
| 2,5 | 50,625 | | 20,8 | |
| | | 67,15 | | |
| 3 | 84,2 | | | |

**Paso 2:**

$$
P(x) = 7{,}8 + 13{,}75\,(x-1) + 14{,}8\,(x-1)(x-1{,}5) + 3\,(x-1)(x-1{,}5)(x-2{,}5)
$$

**Paso 3:** verifica el sexto punto y evalúa en $x = 2$.

$$
P(4) = 193{,}8 \ \checkmark \qquad P(2) = 28{,}2 = K
$$

**Resultado:** $k = 28{,}2$, con el polinomio $P(x)$ de arriba (la hoja lo deja en forma de Newton, sin desarrollar).

**Ítem b) — exponencial de mínimos cuadrados con los cuatro primeros datos y $k = 30$**

$$
y = a_0\, e^{a_1 x}
$$

$$
\ln y = \ln a_0 + a_1 x
$$

| $x$ | $y$ | $x^2$ | $\ln(y)$ | $x\cdot\ln(y)$ |
|---|---|---|---|---|
| 1 | 7.8 | 1 | 2.05412373 | 2.05412373 |
| 1.5 | 14.675 | 2.25 | 2.68614537 | 4.02921805 |
| 2 | 30 | 4 | 3.40119738 | 6.80239476 |
| 2.5 | 50.625 | 6.25 | 3.92444553 | 9.81111381 |
| **Suma: 7** | **103.1** | **13.5** | **12.065912** | **22.6968504** |

$$
\begin{pmatrix} 4 & 7 \\ 7 & 13.5 \end{pmatrix}\begin{pmatrix} A_0 \\ a_1 \end{pmatrix} = \begin{pmatrix} 12.065912 \\ 22.6968504 \end{pmatrix}
\qquad
\text{inversa} = \begin{pmatrix} 2.7 & -1.4 \\ -1.4 & 0.8 \end{pmatrix}
$$

$$
A_0 = 0.80237191 \;\Rightarrow\; a_0 = 2.23082599 \qquad a_1 = 1.26520348
$$

**Resultado:** $y \approx 2{,}2308\, e^{1{,}2652\,x}$ (los coeficientes son los de la planilla; la etiqueta de la línea de tendencia del gráfico es muy chica y se lee igual).

### Ej4 — Mayor $h$ para Trapecios, $\int_{0}^{2} e^{x}(x^{2}-9x+23)\,dx$, $\varepsilon < 10^{-2}$

**Paso 1:**

$$
\frac{2}{12}\cdot h^{2}\cdot \max_{0 \le \alpha \le 2} |f''(\alpha)| < 10^{-2}
$$

**Paso 2:**

$$
f(x) = e^{x}(x^{2}-9x+23)
$$

$$
f'(x) = e^{x}(x^{2}-9x+23) + e^{x}(2x-9) = e^{x}(x^{2}-7x+14)
$$

$$
f''(x) = e^{x}(x^{2}-7x+14) + e^{x}(2x-7) = e^{x}(x^{2}-5x+7)
$$

Nota de la hoja: *"No puedo decir a ojo que sea creciente o decreciente en el intervalo"*.

$$
f'''(x) = e^{x}(x^{2}-5x+7) + e^{x}(2x-5) = e^{x}(x^{2}-3x+2)
$$

**Paso 3:**

$$
f'''(x) = 0 \;\Rightarrow\; x^{2} - 3x + 2 = 0 \;\Rightarrow\; x_1 = 1 \qquad x_2 = 2
$$

**Paso 4:** "Extremos del intervalo vs. puntos críticos":

$$
|f''(0)| = 7 \quad \text{vs.} \quad |f''(1)| = 8{,}15 \quad \text{vs.} \quad |f''(2)| = 7{,}39
$$

**Paso 5:**

$$
\frac{h^{2}}{6}\cdot 8{,}15 < 10^{-2} \;\Rightarrow\; h < 0{,}086
$$

**Resultado:** "Podemos tomar $h = 0{,}08$" ($N = 25$).

### Ej5 — PVI $y' = y\cdot \operatorname{sen}(t)$, $y(0) = 1$, $t \in [0; 2]$

**Ítem a) — constante de Lipschitz**

$$
L = \max_{0 \le t \le 2} |\operatorname{sen} t| = 1
$$

**Ítem b) — $y(0{,}3)$ por Euler con $h = 0.1$**

| $t_i$ | $w_i$ | $w_{i+1}$ |
|---|---|---|
| 0 | 1 | 1 |
| 0.1 | 1 | 1.009983342 |
| 0.2 | 1.009983342 | **1.030048613** |
| 0.3 | **1.030048613** | |

**Resultado:** $y(0{,}3) \approx 1{,}030048613$ (resaltado en la tabla).

---

## 1er recuperatorio

### Ej1 — Raíces de $\dfrac{x}{x-1} - e^{x} = 0$

**Ítem a) — intervalos**

[Gráfico: $x/(x-1)$ y $e^{x}$ superpuestas.]

**Resultado:** 1 raíz en $[-1, 0]$ y 1 raíz en $[1, 2]$. (solo resultado en la fuente, leído del gráfico)

**Ítem b) — ¿$g_1(x) = (x-1)e^{x}$ o $g_2(x) = \dfrac{x}{e^{x}} + 1$ para la mayor raíz?**

**$g_1$:** si $x = 2 \Rightarrow g_1(x) = e^{2} \notin [1,2]$ ✗ (descartada).

**$g_2$:**

**Paso 1:** el término $\dfrac{x}{e^{x}}$ "siempre va a valer entre 0 y 1 si $x \in [1,2]$" ⇒

$$
g_2(x_i) \in [1,2] \quad \forall x_i \in [1,2] \ \checkmark
$$

**Paso 2:**

$$
g_2'(x) = \frac{e^{x} - x\,e^{x}}{e^{2x}} = \frac{1-x}{e^{x}}
$$

- El numerador varía entre $-1$ y $0$.
- El denominador varía entre $e$ y $e^{2}$.

$$
|g'(x_i)| < 1 \quad \forall x_i \in [1,2] \ \checkmark
$$

**Resultado:** la más adecuada es $g_2$.

**Ítem c) — aproximación de la raíz con $g_2$, $\varepsilon \le 10^{-2}$**

| $x_i$ | $g(x_i)$ | $f(x_i)$ |
|---|---|---|
| 2 | 1.27067057 | -5.3890561 |
| 1.27067057 | 1.35660527 | 1.1312869 |
| 1.35660527 | 1.34937137 | -0.0787681 |
| 1.34937137 | 1.35003136 | 0.00728232 |

**Resultado:** la tabla termina en $x \approx 1{,}35$ (última fila: $x_i = 1.34937137$, $g(x_i) = 1.35003136$; la hoja no recuadra un valor final).

### Ej2 — Valores de $k$ para que converja Jacobi o Gauss-Seidel, $A = \begin{pmatrix} 3k-3 & 4 & -1 \\ 2 & 5+k^{2} & -2 \\ 7 & 4 & 10-k \end{pmatrix}$

"Busco diagonal dominante":

$$
|3k-3| \ge 5 \quad \wedge \quad |5+k^{2}| \ge 4 \quad \wedge \quad |10-k| \ge 11
$$

**Primera condición:**

$$
3k-3 \ge 5 \ \vee\ 3k-3 \le -5 \;\Rightarrow\; k \ge \frac{8}{3} \ \vee\ k \le -\frac{2}{3}
$$

**Segunda condición:**

$$
5+k^{2} \ge 4 \ \vee\ 5+k^{2} \le -4 \;\Rightarrow\; k^{2} \ge -1 \ \vee\ k^{2} \le -9 \;\Rightarrow\; \forall k \in \mathbb{R} \ \vee\ \nexists k \in \mathbb{R}
$$

**Tercera condición:**

$$
10-k \ge 11 \ \vee\ 10-k \le -11 \;\Rightarrow\; k \le -1 \ \vee\ k \ge 21
$$

**Resultado:** $k \in S$, con

$$
S = (-\infty; -1] \cup [21; +\infty)
$$

### Ej3 — Tabla $x = 1, 2, 4, 5, 6, 8$; $y = a,\ 4,\ 17,\ b,\ 32,\ c$

**Ítem a) — $a$, $b$, $c$ para el único polinomio de menor grado**

**Paso 1:** diferencias divididas con los tres puntos conocidos:

| $x$ | $y$ | O1 | O2 |
|---|---|---|---|
| 2 | 4 | | |
| | | $13/2$ | |
| 4 | 17 | | $1/4$ |
| | | $15/2$ | |
| 6 | 32 | | |

**Paso 2:**

$$
P(x) = 4 + \frac{13}{2}(x-2) + \frac{1}{4}(x-2)(x-4)
$$

**Paso 3:**

$$
a = P(1) = -\frac{7}{4} \qquad b = P(5) = \frac{97}{4} \qquad c = P(8) = 49
$$

**Ítem b) — con $a = 1$ y los $b$, $c$ hallados**

**Resultado:** grado 3: $\varnothing$; grado 4: $\varnothing$; grado 5: **1**. (solo resultado en la fuente)

**Ítem c) — con $b = 10$ y los $a$, $c$ hallados, polinomios de grado 10**

**Resultado:** infinitos. (solo resultado en la fuente)

**Ítem d) — potencial $y = b\cdot x^{a}$ de mínimos cuadrados con $a=1$, $b=24$, $c=50$**

$$
\ln y = \underbrace{\ln b}_{B} + a\cdot \ln x
$$

$$
\begin{cases}
B\cdot n + a\sum \ln x = \sum \ln y \\[1mm]
B\cdot \sum \ln x + a\cdot \sum (\ln x)^{2} = \sum \ln x\cdot \ln y
\end{cases}
$$

| $x$ | $y$ | $\ln x$ | $\ln y$ | $(\ln x)^2$ | $\ln x\cdot\ln y$ |
|---|---|---|---|---|---|
| 1 | 1 | 0 | 0 | 0 | 0 |
| 2 | 4 | 0.69314718 | 1.38629436 | 0.48045301 | 0.96090603 |
| 4 | 17 | 1.38629436 | 2.83321334 | 1.92181206 | 3.92766768 |
| 5 | 24 | 1.60943791 | 3.17805383 | 2.59029039 | 5.11488032 |
| 6 | 32 | 1.79175947 | 3.4657359 | 3.210402 | 6.20976512 |
| 8 | 50 | 2.07944154 | 3.91202301 | 4.32407713 | 8.13482315 |
| **Suma: 26** | **128** | **7.56008047** | **14.7753204** | **12.5270346** | **24.3480423** |

$$
\begin{pmatrix} 6 & 7.56008047 \\ 7.56008047 & 12.5270346 \end{pmatrix}\begin{pmatrix} B \\ a \end{pmatrix} = \begin{pmatrix} 14.7753204 \\ 24.3480423 \end{pmatrix}
\qquad
\text{inversa} = \begin{pmatrix} 0.69566072 & -0.4198321 \\ -0.4198321 & 0.33319952 \end{pmatrix}
$$

$$
B = 0.05652075 \;\Rightarrow\; b = 1.05814857 \qquad a = 1.90952941
$$

**Resultado:** $y = 1{,}0581\, x^{1{,}9095}$ (ecuación de la línea de tendencia del gráfico).

### Ej4 — $h$ para Trapecios, $\int_{1}^{3} \dfrac{\ln(x)+1}{x}\,dx$, $\varepsilon < 10^{-2}$

**Paso 1:**

$$
\varepsilon_T = \left|\frac{b-a}{12}\right|\cdot h^{2}\cdot \max_{a \le \alpha \le b} |f''(\alpha)| < 10^{-2}
$$

$$
\varepsilon_T = \frac{1}{6}\cdot h^{2}\cdot \max_{a \le \alpha \le b} |f''(\alpha)| < 10^{-2}
$$

**Paso 2:**

$$
f(x) = \frac{\ln x + 1}{x}
$$

$$
f'(x) = \frac{1 - 1\,(\ln x + 1)}{x^{2}} = \frac{-\ln x}{x^{2}}
$$

$$
f''(x) = \frac{-x + 2x\ln x}{x^{4}} = \frac{-1 + 2\ln x}{x^{3}}
$$

Nota de la hoja: *"No es creciente/decreciente en el intervalo"*.

**Paso 3:** "Para calcular el máximo hay que comparar extremos del intervalo vs. máximos y mínimos relativos".

Extremos:

$$
f''(1) = -1 \qquad f''(3) = 0{,}0443\ldots
$$

Máximos y mínimos relativos:

$$
f'''(x) = \frac{2x^{2} - 3x^{2}(-1 + 2\ln x)}{x^{6}} = \frac{5 - 6\ln x}{x^{4}}
$$

$$
f'''(x) = 0 \;\Rightarrow\; \ln x = \frac{5}{6} \;\Rightarrow\; x = 2{,}30097
$$

$$
f''(2{,}30097) = 0{,}0547233
$$

"El máximo se encuentra en el extremo izquierdo" → "Ese es el número que tenemos que usar".

**Paso 4:**

$$
\varepsilon_T = \frac{1}{6}\cdot h^{2}\cdot 1 < 10^{-2} \;\Rightarrow\; h < \sqrt{0{,}06} \;\Rightarrow\; h < 0{,}2449
$$

**Resultado:** "Se puede usar $h = 0{,}2$ y ya tendremos un $\varepsilon < 10^{-2}$".

### Ej5 — PVI $y' = x/y$, $y(0) = 1$; $y(0{,}2)$ por Heun con $h = 0{,}1$

Fórmula de Heun tal como figura en la hoja:

$$
w_{i+1} = w_i + \frac{h}{2}\left[\, f(t_i, w_i) + f\big(t_i + h,\ w_i + h\, f(t_i, w_i)\big) \right]
$$

Tabla de la planilla ($w_0 = y(0) = 1$, $h = 0.1$; $w^{*}_{i+1}$ es el paso de Euler y $w_{i+1}$ el de Heun, "Euler modificado"):

| $x_i$ | $w_i$ | $w^{*}_{i+1}$ (Euler) | $w_{i+1}$ (Heun) |
|---|---|---|---|
| 0 | 1 | 1 | 1.005 |
| 0.1 | 1.005 | 1.01495025 | 1.01982782 |
| 0.2 | **1.01982782** | | |

**Resultado:** $y(0{,}2) \approx 1{,}01982782$ (resaltado en la tabla).

---

## 2do recuperatorio

### Ej1 — Raíces de $e^{-2x} - \operatorname{sen}(x) = 0$

**Ítem a) — ubicación gráfica y cantidad de raíces**

[Gráfico: $e^{-2x}$ y $\operatorname{sen}(x)$ superpuestas.]

**Resultado:** "Infinitas raíces. Las primeras 2 en $[0,1]$ y $[3,4]$".

**Ítem b) — segunda raíz positiva por Newton-Raphson, error menor a $10^{-5}$**

$$
f(x) = e^{-2x} - \operatorname{sen} x
$$

$$
f'(x) = -2e^{-2x} - \cos x
$$

| $x_i$ | $f(x_i)$ | $f'(x_i)$ | $x_{i+1}$ |
|---|---|---|---|
| 3 | -0.1386413 | 0.985035 | 3.1407475 |
| 3.1407475 | 0.0010255 | 0.9962584 | **3.1397182** |
| **3.1397182** | 4.596E-09 | | |

**Resultado:** $x \approx 3{,}1397182$ (resaltado en la tabla).

**Ítem c) — iteraciones de bisección en $[a-1; a+1]$ para un error de $10^{-5}$**

$$
\frac{2}{2^{i}} \le 10^{-5}
$$

$$
2^{1-i} \le 10^{-5}
$$

$$
1 - i \le \frac{-5}{\log_{10} 2}
$$

$$
i \ge 17{,}60964
$$

**Resultado:** **18** iteraciones, suficientes. (La hoja no escribe la justificación de "suficientes".)

### Ej2 — $A = \begin{pmatrix} 4 & 7 & 1 \\ -5 & -1 & 2 \\ -1 & 2 & 9 \end{pmatrix}$, $B = \begin{pmatrix} 6 \\ 4 \\ -3 \end{pmatrix}$, con $A^{-1}$ dada

**Ítem a) — ¿bien condicionado?**

$$
\|A\|_{\infty} = 12 \qquad \|A^{-1}\|_{\infty} = \frac{93}{238}
$$

(Nota de la hoja: "Puede usarse Norma-1 también".)

$$
K(A) = 12\cdot \frac{93}{238} = 4{,}6891
$$

**Resultado:** bien condicionado ✓.

**Ítem b) — una iteración de Gauss-Seidel desde $x_0 = (1, 0, 1)$**

**Paso 1:** "Reordeno para diagonal dominante" (intercambia las dos primeras filas):

$$
\begin{pmatrix} -5 & -1 & 2 \\ 4 & 7 & 1 \\ -1 & 2 & 9 \end{pmatrix}
\;\Rightarrow\;
\begin{cases}
-5x - y + 2z = 4 \\
4x + 7y + z = 6 \\
-x + 2y + 9z = -3
\end{cases}
$$

**Paso 2:**

$$
\begin{cases}
x = -\dfrac{1}{5}\,y + \dfrac{2}{5}\,z - \dfrac{4}{5} \\[2mm]
y = -\dfrac{4}{7}\,x - \dfrac{1}{7}\,z + \dfrac{6}{7} \\[2mm]
z = \dfrac{1}{9}\,x - \dfrac{2}{9}\,y - \dfrac{1}{3}
\end{cases}
$$

**Paso 3:** con $X_0 = (1,\ 0,\ 1)$ (componentes $x$, $y$, $z$):

**Resultado:**

$$
X_1 = (-0{,}4;\ 0{,}94286;\ -0{,}5873)
$$

(La hoja pasa de $X_0$ a $X_1$ sin mostrar las cuentas intermedias.)

### Ej3 — Tabla $x = 2, 3, 4, 6, 8, 9$; $y = a,\ 4{,}35,\ 3{,}2,\ b,\ 13{,}6,\ 21{,}45$

**Ítem a) — $a$ y $b$ para el único polinomio de menor grado**

**Paso 1:** diferencias divididas con $x = 3, 4, 8, 9$:

| $x$ | $y$ | O1 | O2 | O3 |
|---|---|---|---|---|
| 3 | 4,35 | | | |
| | | $-1{,}15$ | | |
| 4 | 3,2 | | 0,75 | |
| | | 2,6 | | 0,05 |
| 8 | 13,6 | | 1,05 | |
| | | 7,85 | | |
| 9 | 21,45 | | | |

**Paso 2:**

$$
P(x) = 4{,}35 - 1{,}15\,(x-3) + 0{,}75\,(x-3)(x-4) + 0{,}05\,(x-3)(x-4)(x-8)
$$

**Paso 3:**

$$
P(2) = a = 6{,}4 \qquad P(6) = b = 4{,}8
$$

**Ítem b) — con el $a$ hallado y $b = 10$, grado del interpolante**

**Resultado:** grado 5. (solo resultado en la fuente; no está escrita la justificación)

**Ítem c) — exponencial de mínimos cuadrados con $a = 1$, $b = 8$, y error del ajuste**

$$
y = a_0\, e^{a_1 x}
$$

$$
\ln y = \underbrace{\ln a_0}_{A_0} + a_1 x
$$

| $x$ | $y$ | $x^2$ | $\ln(y)$ | $x\cdot\ln(y)$ |
|---|---|---|---|---|
| 3 | 4.35 | 9 | 1.47017585 | 4.41052754 |
| 4 | 3.2 | 16 | 1.16315081 | 4.65260324 |
| 8 | 13.6 | 64 | 2.61006979 | 20.8805583 |
| 9 | 21.45 | 81 | 3.06572465 | 27.5915218 |
| 2 | 1 | 4 | 0 | 0 |
| 6 | 8 | 36 | 2.07944154 | 12.4766493 |
| **Suma: 32** | **51.6** | **210** | **10.3885626** | **70.0118602** |

$$
\begin{cases}
6\cdot A_0 + 32\cdot a_1 = 10{,}38856 \\
32\cdot A_0 + 210\cdot a_1 = 70{,}01186
\end{cases}
$$

$$
A_0 = -0{,}24907 \;\Rightarrow\; a_0 = e^{-0{,}24907} = 0{,}77952 \qquad a_1 = 0{,}37134
$$

**Resultado:** $y = 0{,}7795\, e^{0{,}3713\,x}$ (línea de tendencia del gráfico) y **Error $= 7{,}8828$** (la hoja da el valor del error sin mostrar la cuenta ni la fórmula usada).

### Ej4 — $\int_{4}^{6} e^{-x}(x^{2}-1)\,dx$

**Ítem a) — número conveniente de subintervalos para Trapecios con $\varepsilon \le 10^{-3}$**

**Paso 1:**

$$
\frac{2}{12}\cdot h^{2}\cdot \max_{4 \le \alpha \le 6} |f''(\alpha)| \le 10^{-3}
$$

**Paso 2:**

$$
f(x) = e^{-x}(x^{2}-1)
$$

$$
f'(x) = -e^{-x}(x^{2}-1) + e^{-x}\cdot 2x = e^{-x}(-x^{2}+2x+1)
$$

$$
f''(x) = -e^{-x}(-x^{2}+2x+1) + e^{-x}(-2x+2) = e^{-x}(x^{2}-4x+1)
$$

Nota de la hoja: *"No es creciente/decreciente en el intervalo"*.

**Paso 3:** "Analizo máx/mín locales":

$$
f'''(x) = -e^{-x}(x^{2}-4x+1) + e^{-x}(2x-4) = e^{-x}(-x^{2}+6x-5)
$$

$$
f'''(x) = 0 \;\Rightarrow\; x^{2} - 6x + 5 = 0 \;\Rightarrow\; x_0 = 1 \qquad x_1 = 5 \ \leftarrow \text{dentro de mi intervalo}
$$

**Paso 4:**

$$
f''(4) = 0{,}0183 \quad \text{vs.} \quad f''(5) = 0{,}0404 \ (\text{el mayor}) \quad \text{vs.} \quad f''(6) = 0{,}0322
$$

**Paso 5:**

$$
\frac{1}{6}\cdot h^{2}\cdot 0{,}0404 \le 10^{-3} \;\Rightarrow\; h \le 0{,}3854
$$

$$
N \ge \frac{2}{0{,}3854} = 5{,}1894
$$

**Paso 6:** elige $N$:

- $N = 6 \to h = \dfrac{1}{3}$ ✗ periódico
- $N = 7 \to h = \dfrac{2}{7}$ ✗ muchos decimales
- $N = 8 \to h = 0{,}25$ ✓

**Resultado:** $N = 8$ subintervalos ($h = 0{,}25$).

**Ítem b) — ¿se podría usar Simpson con ese $h$?**

**Resultado:** "Sí, porque $N$ es par".

**Ítem c) — resolver la integral con $h = 0{,}5$ por el método más conveniente**

| $x$ | $y$ |
|---|---|
| 4 | 0.27473458 |
| 4.5 | 0.21384818 |
| 5 | 0.16171073 |
| 5.5 | 0.11953806 |
| 6 | 0.08675633 |

**Resultado:** $AS = 0.33640956$ (la hoja da la tabla de valores y el resultado rotulado "AS", sin escribir la fórmula).

### Ej5 — Ecuaciones diferenciales

**Ítem a) — PVI $y' = y\cdot\cos(t)$, $y(0) = 2$; $y(0{,}3)$ por RK de orden 4 con $h = 0.3$**

| $t_i$ | $w_i$ | $k_1$ | $k_2$ | $k_3$ | $k_4$ | $w_{i+1}$ |
|---|---|---|---|---|---|---|
| 0 | 2 | 0.6 | 0.68225204 | 0.69445131 | 0.7722323 | **2.6876065** |

**Resultado:** $y(0{,}3) \approx 2{,}6876065$ (la hoja da solo la fila de la planilla, sin escribir las fórmulas de $k_1 \ldots k_4$).

**Ítem b) — clasificar $w_{i+1} = \dfrac{h}{2}\left[3f(t_i; w_i) - f(t_{i-1}; w_{i-1})\right]$**

**Resultado:** explícita, 2 pasos. (solo resultado en la fuente)

---

*Transcripto el 2026-11-18 desde las tres hojas OneNote de respuestas oficiales (K3052, 1C 2025) que están en esta carpeta. No se agregó ningún paso que no figure en la fuente.*
