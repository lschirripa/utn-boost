# Transformada Z desde cero — guía lineal (lunes mañana)

> Fuentes: `examenes/resueltos/RESOLUCIONES-2025.md` (Ej4 de Tema 1 y Tema 2) · `repaso/practica-repaso-2026.md` (H, I) · apuntes `06-practica-transformada-z.md`, `12-video-teorica-transformada-z.md`, `10-video-repaso-primer-parcial.md` (Z), `07-repaso-primer-parcial.md` (Z) · `examenes/INDICE.md` · `plan.md` · `fuentes/AYUDAMEMORIA-OFICIAL.pdf` · Generado 2026-10-03
>
> Cómo usarla: leé de arriba abajo. Los «Ejemplo guiado» están resueltos a la vista: leelos con lápiz, rehaciendo cada paso. Los «Tu turno» se hacen en papel, con reloj y sin mirar; la corrección está plegada. Los ejercicios del repaso 2026 (R-H, R-I) se hacen desde tu hoja `exports/practica-repaso-2026-enunciados.pdf`.
>
> Tiempo total ≈ 4 h: §1–§4 (1 h 20), §5–§6 (40 min), §7 (30 min), §8 (50 min), §9 (40 min), checkpoint (10 min).

---

## 0. Qué te toman (los 2 puntos del Ej4)

En el formato 2025 el Ej4 tiene dos ítems de 1 punto. Salen de esta lista (frecuencias sobre las 16 hojas de examen indexadas):

| Ítem | Qué es | De qué parcial sale | Sección |
|---|---|---|---|
| Transformada Z **y región de convergencia** de una $x(n)$ definida por paridad de $n$ (o V/F sobre la ROC) | Partir en dos series geométricas, sumarlas, ROC = intersección | 2025-1C T1 Ej4a, 2024-2C T1 y T2 Ej5a, sin-fecha K3521 T1 Ej5, 2025-02-13 Ej5 (7 de 16 hojas) | §4 |
| **Suma de una serie numérica** mediante Z | $\sum x(n)\,c^{-n}$ es $X(z)$ evaluada en $z=c$ | 2025-1C T1 Ej4b, 2025-1C T2 Ej4a, 2024-2C T1 y T2 Ej5b (4 de 16) | §5 |
| **Ecuación en diferencias** de 1er orden, con verificación de $x(2)$ | Transformar, despejar $X(z)$, fracciones simples "con una $z$ afuera", tabla | 2025-1C T2 Ej4b, 2015-05-29 T1 y T2 Ej4, sin-fecha K3521 T2 Ej5, 2024-2C rec Ej5 (8 de 16 contando las de 2º orden) | §8 |
| Ecuación en diferencias de **2º orden** (raíz doble) | Igual, con $x(n+2)$ y dos condiciones iniciales | Repaso 2026 de tu curso (R-I), 2022-10-11 Ej4, 2024-1C T1 y T2 | §9 |
| Z de una **secuencia finita** | Definición término a término | sin fecha (≈2015) T2 Ej4 (2 de 16) | §6 |
| Antitransformada suelta | Fracciones simples con una $z$ afuera | sin fecha (≈2015) T1 Ej4 (1 de 16) | §7 |

Lo más probable para el martes: **un ítem de "paridad + ROC"** y **otro de "ecuación en diferencias" o "suma de serie"**. El profe de la teórica sobre paridad: "se toma bastante, se toma mucho, tanto en finales como en parciales" (`12` [43:22]).

---

## 1. La idea en criollo

- En Laplace transformabas una función de tiempo continuo $f(t)$. Acá la "señal" es una **sucesión**: una lista de números $x(0), x(1), x(2), \dots$ (un valor por cada $n = 0, 1, 2, \dots$). En los ejercicios $x(n)$ y $a_n$ son lo mismo.
- La transformada Z mete esa lista en una **serie de potencias de $z^{-1}$**: el número $x(n)$ queda "colgado" de $z^{-n}$.

$$
\mathcal{Z}\left[x(n)\right] = \sum_{n=0}^{\infty} x(n)\, z^{-n} = x(0) + \frac{x(1)}{z} + \frac{x(2)}{z^2} + \frac{x(3)}{z^3} + \dots = X(z)
$$

- Es "la Laplace de lo discreto": la integral pasa a ser sumatoria, $f(t)$ pasa a ser $x(n)$ y $e^{-st}$ pasa a ser $z^{-n}$. La $z$ es complejo, como la $s$ (`12` [13:05]–[14:38]).
- Como es una suma infinita, **no converge para cualquier $z$**: converge si $|z|$ es suficientemente grande. Ese conjunto de $z$ es la **región de convergencia (ROC)**. Siempre te queda de la forma $|z| > R$: el exterior de una circunferencia de radio $R$ centrada en el origen.
- Para casi todo vas a usar **una sola herramienta: la serie geométrica**. "La idea es siempre llevarlos a una serie geométrica: algo elevado a la $n$, no importa el choclo que les quede adentro" (`12` [28:13]).
- Y como en Laplace: las **ecuaciones diferenciales** se resolvían transformando; acá las **ecuaciones en diferencias** (recurrencias como $x(n+1) = 3x(n) + 2$) se resuelven transformando. La derivada de Laplace la reemplaza el **desplazamiento a izquierda**.

---

## 2. Qué tenés en el ayudamemoria y qué tenés que saber de memoria

En el parcial solo podés tener el **ayudamemoria oficial** (+ tabla de integrales). La parte de Z está al final de la pág. 2 y en la pág. 3 del PDF.

**Está en el ayudamemoria (no lo memorices, aprendé a usarlo):**

- La definición $\mathcal{Z}[x(n)] = \sum_{n=0}^{\infty} x(n) z^{-n}$.
- Desplazamiento a derecha: $\mathcal{Z}[x(n-a)] = z^{-a} X(z)$.
- Desplazamiento a izquierda (el de las ecuaciones en diferencias), escrito así:

$$
\mathcal{Z}\left[x(n+1)\right] = z\left(X(z) - x(0)\right)
$$

$$
\mathcal{Z}\left[x(n+2)\right] = z^2\left(X(z) - x(0) - x(1)\,z^{-1}\right)
$$

  Distribuido es lo mismo que vas a usar: $zX - z\,x(0)$ y $z^2X - z^2x(0) - z\,x(1)$.
- Multiplicación por $n$: $\mathcal{Z}[n\,x(n)] = -z\,\dfrac{dX(z)}{dz}$; multiplicación por $a^n$; teoremas de valor inicial y final; convolución.
- **La tabla** (con la columna $R$ del radio, ROC $|z|>R$):

| $x(n)$ | $X(z)$ | $R$ |
|---|---|---|
| $\delta(n)$ | $1$ | $0$ |
| $u(n) = 1$ | $\dfrac{z}{z-1}$ | $1$ |
| $n$ | $\dfrac{z}{(z-1)^2}$ | $1$ |
| $n^2$ | $\dfrac{z(z+1)}{(z-1)^3}$ | $1$ |
| $a^n$ | $\dfrac{z}{z-a}$ | $\lvert a\rvert$ |
| $n\,a^n$ | $\dfrac{a\,z}{(z-a)^2}$ | $\lvert a\rvert$ |
| $\cos(an)$ | $\dfrac{z\,(z-\cos a)}{z^2 - 2z\cos a + 1}$ | $1$ |
| $\mathrm{sen}(an)$ | $\dfrac{z\,\mathrm{sen}\,a}{z^2 - 2z\cos a + 1}$ | $1$ |
| $e^{-an}$ | $\dfrac{z}{z-e^{-a}}$ | $e^{-a}$ |

**NO está y lo tenés que saber de memoria:**

1. **Serie geométrica:** $\displaystyle\sum_{k=0}^{\infty} r^k = \frac{1}{1-r}$ **solo si** $|r|<1$.
2. **ROC por geométricas:** cada serie pide $|\text{razón}|<1$; la ROC total es la **intersección** = el exterior de la circunferencia **más grande**.
3. Cómo separar pares e impares: $n = 2k$ y $n = 2k+1$ (o $3k, 3k+1, 3k+2$ si es "múltiplo de 3").
4. **$\mathcal{Z}[a^n/n!] = e^{a/z}$** (sale de la serie de $e^x$; no está en la tabla).
5. **$\sum x(n)\,c^{-n} = X(c)$**: sumar una serie numérica es evaluar una transformada.
6. **"Dejar una $z$ afuera"** antes de hacer fracciones simples.
7. Cómo hacer fracciones simples con raíz doble (lo traés de Laplace) y la **verificación** con la recurrencia.

> El ayudamemoria se lleva solo, sin anotaciones propias (`10` [02:40]). Practicá esta mañana con el PDF al lado, igual que el martes.

---

## 3. La serie geométrica y la primera transformada: $\mathcal{Z}[a^n]$

**Receta (la vas a repetir en todo el tema):**

1. Escribí la definición $\sum x(n) z^{-n}$.
2. Juntá todo lo que depende de $n$ como **"algo elevado a la $n$"** (o a la $k$). Ese "algo" es la **razón** $r$.
3. Sumá con $\dfrac{1}{1-r}$ y sacá denominador común.
4. ROC: imponé $|r|<1$ y despejá $|z|$.

Primero la geométrica, porque es la base de todo. Si $S = 1 + r + r^2 + \dots$, multiplicando por $r$ queda $rS = r + r^2 + \dots$; restando se cancela todo salvo el 1: $S - rS = 1$, o sea (`12` [19:24]–[22:02]):

$$
\sum_{k=0}^{\infty} r^k = \frac{1}{1-r} \qquad \text{si } |r|<1
$$

Si $|r| \ge 1$ la suma diverge (con $r=1$ sumás $1+1+1+\dots$ para siempre).

### Ejemplo guiado 3.1 — $\mathcal{Z}[a^n]$ por definición (`12` Ej. 3)

**Paso 1 — definición.** Reemplazo $x(n) = a^n$:

$$
\mathcal{Z}\left[a^n\right] = \sum_{n=0}^{\infty} a^n z^{-n}
$$

**Paso 2 — "algo a la $n$".** Por qué: la fórmula de la geométrica solo sirve si todo queda como una sola potencia. Como $z^{-n} = (1/z)^n$, junto las dos potencias de exponente $n$:

$$
\sum_{n=0}^{\infty} a^n z^{-n} = \sum_{n=0}^{\infty} \left(\frac{a}{z}\right)^n \qquad \Rightarrow \qquad r = \frac{a}{z}
$$

**Paso 3 — sumar.** Aplico $\frac{1}{1-r}$ y multiplico arriba y abajo por $z$ para que quede "lindo":

$$
\mathcal{Z}\left[a^n\right] = \frac{1}{1 - \frac{a}{z}} = \frac{z}{z-a}
$$

**Paso 4 — ROC.** Por qué: el paso 3 solo vale si la razón tiene módulo menor que 1.

$$
\left|\frac{a}{z}\right| < 1 \;\Leftrightarrow\; |a| < |z| \;\Leftrightarrow\; |z| > |a|
$$

**Resultado:** $\mathcal{Z}[a^n] = \dfrac{z}{z-a}$ con ROC $|z|>|a|$. Es exactamente la fila $a^n$ del ayudamemoria (y con $a=1$, el escalón $\frac{z}{z-1}$). Gráficamente: el exterior de la circunferencia de radio $|a|$, dibujada **punteada** porque el borde no entra (`12` [26:31]).

### Ejemplo guiado 3.2 — linealidad + tabla (`12` Ej. 7)

$x(n) = 3(-2)^n - 2\cdot 5^n$. Cuando $x(n)$ es suma de cosas de tabla, **no hace falta la definición**: linealidad ($\mathcal{Z}[\alpha x + \beta y] = \alpha X + \beta Y$) y tabla con $a=-2$ y $a=5$:

$$
X(z) = 3\,\frac{z}{z+2} - 2\,\frac{z}{z-5}
$$

ROC: cada término pide $|z|>|a|$, o sea $|z|>2$ y $|z|>5$. Las dos se tienen que cumplir a la vez (intersección): gana la más grande, **$|z|>5$**.

### ✍️ Tu turno 3.A (3 min) — guía, ej. 1a

Hallá por definición la transformada Z de $x(n) = \left(\frac{1}{3}\right)^n$ y su ROC.

<details>
<summary>Corrección</summary>

(resuelto para esta guía, verificado con sympy)

$$
X(z) = \sum_{n=0}^{\infty} \left(\frac{1}{3z}\right)^n = \frac{1}{1 - \frac{1}{3z}} = \frac{3z}{3z-1}, \qquad \left|\frac{1}{3z}\right|<1 \Rightarrow |z| > \frac{1}{3}
$$

Es la fila $a^n$ con $a = \frac13$: $\frac{z}{z-1/3}$, la misma expresión.

</details>

**Errores típicos de §3:**

- Olvidarse de la ROC. Si el enunciado dice "y la región de convergencia", es medio ítem.
- Despejar mal: $|a/z|<1$ da $|z|>|a|$ (afuera), **nunca** $|z|<|a|$.

---

## 4. Sucesión definida por paridad: dos geométricas y ROC = intersección

Es **el** ítem del Ej4. El profe: "es bastante mecánico todo, porque siempre es lo mismo" (`12` [43:22]).

**Receta (`06` p. 1):**

1. **Escribí los primeros términos** de $\sum x(n) z^{-n}$ ($n=0$ es par) para ver qué rama usa cada $n$.
2. **Separá en dos sumatorias**: pares con $n=2k$, impares con $n=2k+1$ (si es "múltiplo de 3": tres sumatorias $3k$, $3k+1$, $3k+2$; "múltiplo de 5": cinco).
3. En cada una, **llevá todo a "algo elevado a la $k$"**. En los impares sobra siempre un "$+1$" del exponente: sale **afuera** como constante (ej.: $z^{-(2k+1)} = z^{-1}\cdot (z^{-2})^k$).
4. **Sumá** cada geométrica con $\frac{1}{1-r}$ y simplificá (multiplicá arriba y abajo por $z^2$; en los impares se simplifica una $z$).
5. **ROC:** $|r|<1$ en cada sumatoria → $|z| > R_1$, $|z|>R_2$. La ROC de $X(z)$ es la **intersección**: $|z| > \max(R_1, R_2)$.

> Si solo piden la ROC (o un V/F sobre la ROC), **cortás en el paso 3**: "el área de convergencia sale sin necesidad de resolver el resto de la transformada" (`06` p. 5). Las constantes que quedan afuera de la sumatoria no influyen (`10` [2:04:08]).

Dos identidades de potencias que vas a usar sin parar:

$$
b^{2k} = \left(b^2\right)^k, \qquad b^{2k+1} = b\cdot\left(b^2\right)^k
$$

$$
(-2)^{2k} = 4^k \;\text{(el signo desaparece en los pares)}, \qquad (-2)^{2k+1} = -2\cdot 4^k
$$

### Ejemplo guiado 4.1 — guía ej. 1c (`06` p. 1; es el 2025-02-13 Ej5)

$$
x(n) = \begin{cases} 4^n & n \text{ par} \\ 3^{-n} & n \text{ impar} \end{cases}
$$

**Paso 1 — primeros términos.** Por qué: para no equivocarte de rama. $n=0$ par usa $4^n$, $n=1$ impar usa $3^{-n}$, etc.:

$$
X(z) = 4^0 z^{0} + 3^{-1} z^{-1} + 4^2 z^{-2} + 3^{-3} z^{-3} + \dots
$$

**Paso 2 — dos sumatorias.** Reemplazo $n=2k$ en la de pares y $n=2k+1$ en la de impares:

$$
X(z) = \sum_{k=0}^{\infty} 4^{2k} z^{-2k} + \sum_{k=0}^{\infty} 3^{-(2k+1)} z^{-(2k+1)}
$$

**Paso 3 — "algo a la $k$".** Pares: $4^{2k} = 16^k$ y $z^{-2k} = (1/z^2)^k$, juntos dan $(16/z^2)^k$. Impares: separo el "+1" del exponente, $3^{-(2k+1)} z^{-(2k+1)} = \frac{1}{3z}\cdot\left(\frac{1}{9z^2}\right)^k$, y el $\frac{1}{3z}$ sale afuera porque no depende de $k$:

$$
X(z) = \sum_{k=0}^{\infty} \left(\frac{16}{z^2}\right)^k + \frac{1}{3z} \sum_{k=0}^{\infty} \left(\frac{1}{9z^2}\right)^k
$$

**Paso 4 — sumar.** Cada una con $\frac{1}{1-r}$, multiplicando arriba y abajo por $z^2$ (y por $9z^2$ en la segunda):

$$
X(z) = \frac{1}{1 - \frac{16}{z^2}} + \frac{1}{3z}\cdot\frac{1}{1 - \frac{1}{9z^2}} = \frac{z^2}{z^2-16} + \frac{1}{3z}\cdot\frac{9z^2}{9z^2-1} = \frac{z^2}{z^2-16} + \frac{3z}{9z^2-1}
$$

(en el impar se simplificó $\frac{9z^2}{3z} = 3z$: "en la parte impar siempre sobra algo con $z$ que se simplifica", `12` [42:50]).

**Paso 5 — ROC.** Una condición por sumatoria:

$$
\left|\frac{16}{z^2}\right|<1 \Rightarrow |z|^2>16 \Rightarrow |z|>4, \qquad \left|\frac{1}{9z^2}\right|<1 \Rightarrow |z|^2 > \frac19 \Rightarrow |z|>\frac13
$$

Intersección: dos circunferencias concéntricas (radios $\frac13$ y $4$); los $z$ que están afuera de las dos son los de afuera de la grande. **ROC: $|z|>4$.**

$$
\boxed{X(z) = \frac{z^2}{z^2-16} + \frac{3z}{9z^2-1}, \qquad |z|>4}
$$

### ✍️ Tu turno 4.A (12 min) — 2025-1C T1 Ej4a

Hallá la transformada Z y la región de convergencia de

$$
x(n) = \begin{cases} (-2)^n & n \text{ par} \\ 4^{-n} & n \text{ impar} \end{cases}
$$

<details>
<summary>Corrección</summary>

(resolución oficial de la cátedra, `RESOLUCIONES-2025.md` T1 Ej4a)

**Términos:** $X(z) = (-2)^0 z^0 + 4^{-1}z^{-1} + (-2)^2 z^{-2} + 4^{-3}z^{-3} + \dots$

**Separar:** pares $(-2)^{2k} z^{-2k} = \left(\frac{4}{z^2}\right)^k$ (el signo desaparece); impares $4^{-(2k+1)}z^{-(2k+1)} = \frac{1}{4z}\left(\frac{1}{16z^2}\right)^k$:

$$
X(z) = \sum_{k=0}^{\infty}\left(\frac{4}{z^2}\right)^k + \frac{1}{4z}\sum_{k=0}^{\infty}\left(\frac{1}{16z^2}\right)^k
$$

**Sumar:**

$$
X(z) = \frac{1}{1-\frac{4}{z^2}} + \frac{1}{4z}\cdot\frac{1}{1-\frac{1}{16z^2}} = \frac{z^2}{z^2-4} + \frac{4z}{16z^2-1}
$$

**ROC:** $\left|\frac{4}{z^2}\right|<1 \Rightarrow |z|>2$; $\left|\frac{1}{16z^2}\right|<1 \Rightarrow |16z^2|>1 \Rightarrow |z|>\frac14$. Intersección: **$|z|>2$**.

</details>

### ✍️ Tu turno 4.B (10 min) — 2024-2C T2 Ej5a

Transformada Z y región de convergencia de

$$
x(n) = \begin{cases} (-2)^n & n \text{ par} \\ 4^n & n \text{ impar} \end{cases}
$$

<details>
<summary>Corrección</summary>

(resuelto para esta guía, verificado con sympy)

Pares: $(-2)^{2k}z^{-2k} = \left(\frac{4}{z^2}\right)^k$. Impares: $4^{2k+1}z^{-(2k+1)} = \frac{4}{z}\left(\frac{16}{z^2}\right)^k$.

$$
X(z) = \frac{1}{1-\frac{4}{z^2}} + \frac{4}{z}\cdot\frac{1}{1-\frac{16}{z^2}} = \frac{z^2}{z^2-4} + \frac{4z}{z^2-16}
$$

ROC: $|z|>2$ y $|z|>4$ → **$|z|>4$**.

Ojo con la diferencia con 4.A: allá era $4^{-n}$ (razón $\frac{1}{16z^2}$, radio $\frac14$); acá es $4^{n}$ (razón $\frac{16}{z^2}$, radio $4$), y por eso cambia cuál manda.

</details>

### ✍️ Tu turno 4.C (10 min) — sin-fecha K3521 T1 Ej5

Transformada Z de $x(n) = (-3)^n$ si $n$ es par, $5\cdot 2^n$ si $n$ es impar, indicando la región de convergencia.

<details>
<summary>Corrección</summary>

(resuelto para esta guía, verificado con sympy)

Pares: $(-3)^{2k}z^{-2k} = \left(\frac{9}{z^2}\right)^k$. Impares: $5\cdot 2^{2k+1}z^{-(2k+1)} = \frac{10}{z}\left(\frac{4}{z^2}\right)^k$ (el 5 y el 2 que sobra salen juntos: $5\cdot 2 = 10$).

$$
X(z) = \frac{1}{1-\frac{9}{z^2}} + \frac{10}{z}\cdot\frac{1}{1-\frac{4}{z^2}} = \frac{z^2}{z^2-9} + \frac{10z}{z^2-4}
$$

ROC: $|z|>3$ y $|z|>2$ → **$|z|>3$**.

</details>

### Ejemplo guiado 4.2 — "múltiplo de 3", solo la ROC (`10` Ej. 11, repaso grabado)

$$
x(n) = \begin{cases} -3 & n \text{ no múltiplo de } 3 \\ (-2)^n & n \text{ múltiplo de } 3 \end{cases} \qquad \text{¿ROC?}
$$

**Paso 1 — términos.** $n=0$ y $n=3$ son múltiplos de 3; $n=1,2,4$ valen $-3$:

$$
X(z) = \frac{(-2)^0}{z^0} + \frac{-3}{z} + \frac{-3}{z^2} + \frac{(-2)^3}{z^3} + \frac{-3}{z^4} + \cdots
$$

**Paso 2 — tres sumatorias** según el resto de dividir $n$ por 3 ($n=3k$, $3k+1$, $3k+2$). El $-3$ no depende de $n$ y sale afuera:

$$
X(z) = \sum_{k=0}^{\infty}\left(\frac{-2}{z}\right)^{3k} - 3\sum_{k=0}^{\infty}\left(\frac{1}{z}\right)^{3k+1} - 3\sum_{k=0}^{\infty}\left(\frac{1}{z}\right)^{3k+2}
$$

**Paso 3 — "algo a la $k$".** $(-2/z)^{3k} = (-8/z^3)^k$; en las otras dos el "$+1$" y el "$+2$" salen afuera:

$$
X(z) = \sum_{k=0}^{\infty}\left(\frac{-8}{z^3}\right)^{k} - \frac{3}{z}\sum_{k=0}^{\infty}\left(\frac{1}{z^3}\right)^{k} - \frac{3}{z^2}\sum_{k=0}^{\infty}\left(\frac{1}{z^3}\right)^{k}
$$

**Paso 4 — ROC sin sumar nada.** Por qué alcanza: la convergencia solo depende de las razones. Hay dos razones distintas:

$$
\left|\frac{-8}{z^3}\right|<1 \Rightarrow |z|^3>8 \Rightarrow |z|>2, \qquad \left|\frac{1}{z^3}\right|<1 \Rightarrow |z|>1
$$

**Paso 5 — intersección:** **$|z|>2$**. (Si además pidieran $X(z)$: $\frac{z^3}{z^3+8} - \frac{3z^2}{z^3-1} - \frac{3z}{z^3-1}$.)

### Ahora hacé R-H (15 min)

Desde tu hoja: **R-H** (múltiplos de 5, V/F "la ROC es $|z|>2$"). Es la misma receta con cinco sumatorias, pero como es V/F solo necesitás el paso 4. Corregilo con la corrección H de la hoja.

**Errores típicos de §4:**

- **Unión en vez de intersección.** La ROC de la suma es donde convergen **todas**: $|z| > $ el radio **más grande**.
- Olvidar el factor que sobra en los impares ($\frac{1}{4z}$, $\frac{10}{z}$…) o dejarlo adentro de la sumatoria.
- Arrastrar el signo en los pares: $(-2)^{2k} = 4^k$, positivo.
- Confundir $4^{-n}$ con $4^n$: cambia la razón de $\frac{1}{16z^2}$ a $\frac{16}{z^2}$ y el radio de $\frac14$ a $4$.
- Despeje de $|1/(16z^2)|<1$: da vuelta la desigualdad al invertir, $|16z^2|>1$, $|z|^2>\frac{1}{16}$, $|z|>\frac14$.

---

## 5. Suma de una serie numérica mediante Z

**La idea:** la definición es $X(z) = \sum x(n)\,z^{-n}$. Si te piden sumar $\sum_{n=0}^{\infty} x(n)\,c^{-n}$ con un número $c$, eso **es** la definición con $z = c$:

$$
\sum_{n=0}^{\infty} x(n)\, c^{-n} = X(z)\Big|_{z=c}
$$

"Idem en Z: $\sum x(n)\,c^{-n} = X(z)|_{z=c}$" (`RESOLUCIONES-2025.md`, patrones transversales). Es el mismo truco que las integrales impropias de Laplace evaluadas en $s=a$.

**Receta:**

1. Identificá $c$: lo que está elevado a la $-n$ (si te dan $\left(\frac12\right)^n$, eso es $2^{-n}$, o sea $c=2$).
2. Lo que queda es $x(n)$. Buscá $X(z)$ en la tabla (o $e^{a/z}$ si es $\frac{a^n}{n!}$).
3. Reemplazá $z=c$. Control: $c$ tiene que estar en la ROC ($|c|>R$), si no la serie no converge.

**Lo que tenés que saber de memoria** (no está en la tabla): la serie de $e^x = \sum \frac{x^n}{n!}$ con $x = \frac{a}{z}$ da (`06` ej. 1g)

$$
\mathcal{Z}\left[\frac{a^n}{n!}\right] = \sum_{n=0}^{\infty} \frac{\left(\frac{a}{z}\right)^n}{n!} = e^{a/z} \qquad (z \neq 0)
$$

### Ejemplo guiado 5.1 — 2024-2C T1 Ej5b: $\sum_{n=0}^{\infty} n\cdot 2^{-n}$

**Paso 1 — $c$ y $x(n)$.** Lo elevado a la $-n$ es el 2: $c = 2$. Lo que multiplica es $x(n) = n$.

**Paso 2 — tabla.** Fila $n$: $X(z) = \dfrac{z}{(z-1)^2}$, con $R=1$.

**Paso 3 — evaluar.** $c=2$ está en la ROC ($2>1$), así que vale:

$$
\sum_{n=0}^{\infty} n\, 2^{-n} = \frac{z}{(z-1)^2}\bigg|_{z=2} = \frac{2}{1^2} = 2
$$

Coincide con la respuesta del examen (`INDICE.md`).

### ✍️ Tu turno 5.A (5 min) — 2025-1C T1 Ej4b

Resolvé mediante Z: $\displaystyle\sum_{n=0}^{\infty} \frac{3^n}{n!}\, 2^{-n}$.

<details>
<summary>Corrección</summary>

(resolución oficial, `RESOLUCIONES-2025.md` T1 Ej4b)

Es $\sum x(n) z^{-n}$ con $x(n) = \frac{3^n}{n!}$ y $z=2$. Como $\mathcal{Z}\left[\frac{a^n}{n!}\right] = e^{a/z}$, con $a=3$: $\mathcal{Z}\left[\frac{3^n}{n!}\right] = e^{3/z}$.

$$
\sum_{n=0}^{\infty} \frac{3^n}{n!}\, 2^{-n} = e^{3/z}\Big|_{z=2} = e^{3/2}
$$

</details>

### ✍️ Tu turno 5.B (6 min) — 2025-1C T2 Ej4a

Resolvé mediante Z: $\displaystyle\sum_{n=0}^{\infty} \cos(\pi n)\cdot 3^{-n}$.

<details>
<summary>Corrección</summary>

(resolución oficial, `RESOLUCIONES-2025.md` T2 Ej4a)

$c=3$, $x(n) = \cos(\pi n)$. Tabla $\cos(an)$ con $a=\pi$ ($\cos\pi = -1$):

$$
\mathcal{Z}\left[\cos(\pi n)\right] = \frac{z\,(z-\cos\pi)}{z^2 - 2z\cos\pi + 1} = \frac{z^2+z}{z^2+2z+1}
$$

Evaluando en $z=3$ ($3>1$, está en la ROC):

$$
\sum_{n=0}^{\infty} \cos(\pi n)\, 3^{-n} = \frac{9+3}{9+6+1} = \frac{12}{16} = \frac34
$$

Control (verificado con sympy): $\cos(\pi n) = (-1)^n$ y $\mathcal{Z}[(-1)^n] = \frac{z}{z+1}$, que en $z=3$ da $\frac34$. Es lo mismo: $\frac{z(z+1)}{(z+1)^2} = \frac{z}{z+1}$.

</details>

### ✍️ Tu turno 5.C (5 min) — 2024-2C T2 Ej5b

Resolvé mediante Z: $\displaystyle\sum_{n=0}^{\infty} n^2\cdot 4^{-n}$.

<details>
<summary>Corrección</summary>

(respuesta del examen según `INDICE.md`; desarrollo resuelto para esta guía, verificado con sympy)

$c = 4$, $x(n) = n^2$. Tabla: $\mathcal{Z}[n^2] = \dfrac{z(z+1)}{(z-1)^3}$, $R=1$, y $4>1$:

$$
\sum_{n=0}^{\infty} n^2\, 4^{-n} = \frac{4\cdot 5}{3^3} = \frac{20}{27}
$$

</details>

**Errores típicos de §5:**

- Evaluar en el número equivocado: si te dan $3^{-n}$, es $z=3$, no $z=\frac13$.
- Buscar $\frac{a^n}{n!}$ en el ayudamemoria: **no está**, es $e^{a/z}$ de memoria.
- En $\cos(an)$ meter $a = \pi n$: la $a$ de la tabla es solo el número que multiplica a $n$ ($a=\pi$).

---

## 6. Secuencia finita por definición

Si $x(n)$ tiene pocos valores no nulos, la definición es una **suma finita**: escribís término a término y listo. No hay geométrica ni ROC que discutir ("no en las secuencias de puntitos sueltos", `12` [44:57]). Si te la dan en un gráfico de bastones, primero leés cada $x(n)$, empezando por $n=0$.

### Ejemplo guiado 6.1 — `12` Ej. 4

$$
x(n) = \begin{cases} 2 & n=0 \\ n & 1\le n\le 3 \\ 1 & n=4 \\ 0 & \text{en otro caso} \end{cases}
$$

**Paso 1 — tabla de valores** (el "grafiquito" que recomienda el profe): $x(0)=2$, $x(1)=1$, $x(2)=2$, $x(3)=3$, $x(4)=1$, después todo 0.

**Paso 2 — definición término a término.** Cada $x(n)$ va con su $z^{-n}$:

$$
X(z) = 2 + \frac{1}{z} + \frac{2}{z^2} + \frac{3}{z^3} + \frac{1}{z^4}
$$

**Paso 3 — denominador común $z^4$** (las dos formas son respuestas válidas):

$$
X(z) = \frac{2z^4 + z^3 + 2z^2 + 3z + 1}{z^4}
$$

### ✍️ Tu turno 6.A (4 min) — guía, ej. 1e

Hallá la transformada Z de $x(n) = 2$ si $n=1$; $x(n)=n$ si $1<n<4$; $0$ en otro caso.

<details>
<summary>Corrección</summary>

(resuelto para esta guía, verificado con sympy)

Valores: $x(0)=0$ (cae en "otro caso"), $x(1)=2$, $x(2)=2$, $x(3)=3$; el resto 0.

$$
X(z) = \frac{2}{z} + \frac{2}{z^2} + \frac{3}{z^3} = \frac{2z^2+2z+3}{z^3}
$$

</details>

**Error típico de §6:** correr los valores un lugar (poner $x(1)$ con $z^0$). El de $n=0$ va con $z^0 = 1$.

---

## 7. Propiedades que usás y antitransformada con "una $z$ afuera"

Antes de las ecuaciones en diferencias necesitás dos cosas: las propiedades de desplazamiento y cómo volver de $X(z)$ a $x(n)$.

**Desplazamiento a izquierda** (ayudamemoria). Es el análogo de la derivada de Laplace, con una $z$ extra (`12` [57:35]):

$$
\mathcal{Z}\left[x(n+1)\right] = z\,X(z) - z\,x(0), \qquad \mathcal{Z}\left[x(n+2)\right] = z^2 X(z) - z^2 x(0) - z\,x(1)
$$

Por qué se restan esos términos: correr la sucesión a la izquierda deja $x(0)$ (y $x(1)$) en posiciones negativas, que no existen, y hay que descartarlos. **Nunca te van a pedir más de 2 desplazamientos** (`12` [58:38]).

**Multiplicación por $n$** (ayudamemoria): $\mathcal{Z}[n\,x(n)] = -z\,\frac{dX}{dz}$. De ahí sale la fila que vas a usar con raíces dobles (verificado con sympy):

$$
\mathcal{Z}\left[n\,a^n\right] = -z\,\frac{d}{dz}\left(\frac{z}{z-a}\right) = -z\cdot\frac{-a}{(z-a)^2} = \frac{a\,z}{(z-a)^2}
$$

No hace falta deducirla: está en la tabla. Lo importante es **leerla al revés**: $\frac{z}{(z-a)^2}$ **no** es $n a^n$, le falta la $a$ arriba. Si tenés $\frac{4z}{(z-2)^2}$, escribís $4 = 2\cdot 2$ y queda $2\cdot\frac{2z}{(z-2)^2} \to 2\,n\,2^n$.

**Antitransformar — receta "dejar una $z$ afuera"** (`12` [1:08:44], `07` p. 12: "DEJAR UNA Z AFUERA!!!!!!!"):

1. Sacá una $z$ de factor común: $X(z) = z\cdot\left[\dfrac{X(z)}{z}\right]$.
2. Hacé fracciones simples **de lo que quedó adentro** ($X(z)/z$), como en Laplace: polos simples por tapado; raíz doble con $\frac{A}{(z-a)^2} + \frac{B}{z-a}$ ($A$ por tapado, $B$ comparando coeficientes).
3. Distribuí la $z$: cada término queda $\frac{z}{z-a}$ o $\frac{z}{(z-a)^2}$, que son de tabla.
4. Antitransformá por tabla: $\frac{z}{z-a} \to a^n$, $\frac{z}{z-1} \to 1$, $\frac{az}{(z-a)^2} \to n\,a^n$.

Por qué la $z$ afuera: en la tabla **todas** las transformadas tienen una $z$ en el numerador. Si descomponés sin sacarla, te quedan $\frac{A}{z-1}$ que no están en la tabla (`12` [1:10:46]).

### Ejemplo guiado 7.1 — guía ej. 5a (`06` p. 3)

$X(z) = \dfrac{3z(z-3)}{z^2-5z+4}$.

**Paso 1 — factorizar y sacar la $z$.** $z^2-5z+4 = (z-1)(z-4)$:

$$
X(z) = z\cdot\frac{3(z-3)}{(z-1)(z-4)} = z\left(\frac{A}{z-1} + \frac{B}{z-4}\right)
$$

**Paso 2 — tapado.** Por qué funciona: tapás el factor del polo y evaluás el resto en ese polo. $A$: tapo $(z-1)$, evalúo en $z=1$: $\frac{3(1-3)}{1-4} = \frac{-6}{-3} = 2$. $B$: tapo $(z-4)$, evalúo en $z=4$: $\frac{3(4-3)}{4-1} = \frac33 = 1$.

**Paso 3 — distribuir la $z$:**

$$
X(z) = 2\,\frac{z}{z-1} + \frac{z}{z-4}
$$

**Paso 4 — tabla:** $\frac{z}{z-1}\to 1$, $\frac{z}{z-4}\to 4^n$:

$$
\boxed{x(n) = 2 + 4^n}
$$

Control rápido: $x(0) = 3$, y el teorema del valor inicial (ayudamemoria) dice $x(0) = \lim_{z\to\infty} X(z) = 3$. ✓

### ✍️ Tu turno 7.A (8 min) — sin fecha (≈2015) T1 Ej4

Hallá la antitransformada Z de $X(z) = \dfrac{z(2z+3)}{z^2-7z+6}$.

<details>
<summary>Corrección</summary>

(resuelto para esta guía, verificado con sympy)

$z^2-7z+6 = (z-1)(z-6)$. Con la $z$ afuera:

$$
X(z) = z\left(\frac{A}{z-1} + \frac{B}{z-6}\right), \qquad A = \frac{2+3}{1-6} = -1, \quad B = \frac{12+3}{6-1} = 3
$$

$$
X(z) = -\frac{z}{z-1} + 3\,\frac{z}{z-6} \quad\Rightarrow\quad x(n) = -1 + 3\cdot 6^n
$$

Control: $x(0) = 2 = \lim_{z\to\infty}X(z)$. ✓

</details>

**Errores típicos de §7:**

- Hacer fracciones simples de $X(z)$ entero (sin sacar la $z$): quedan términos sin tabla.
- En $\mathcal{Z}[x(n+1)]$ escribir $zX - x(0)$: falta la $z$ que multiplica a $x(0)$. Es un V/F clásico (`06` p. 5, ítem d: falso).
- Creer que $\mathcal{Z}$ es multiplicativa: $\mathcal{Z}[a_n b_n] \neq \mathcal{Z}[a_n]\,\mathcal{Z}[b_n]$ (otro V/F de la guía). Solo vale la linealidad.

---

## 8. Ecuación en diferencias de 1er orden (con verificación)

**Receta** (`12` [1:15:31], `06` p. 3):

1. **Ordená** la ecuación como $x(n+1) + c\,x(n) = g(n)$ y **distribuí** $g(n)$ en términos de tabla (ej.: $4(1-n)2^n = 4\cdot 2^n - 4\,n\,2^n$; una constante $k$ es $k\cdot u(n)$).
2. **Transformá miembro a miembro:** $x(n+1) \to zX - z\,x(0)$, $x(n) \to X$, y $g(n)$ por tabla.
3. **Reemplazá $x(0)$** y agrupá: $X(z)\,(z+c) = \dots$; pasá $(z+c)$ dividiendo.
4. **Dejá una $z$ afuera**, fracciones simples de $X(z)/z$, distribuí la $z$.
5. **Antitransformá** por tabla.
6. **Verificá** (te lo piden y "lleva 40 segundos", `12` [1:29:44]): calculá $x(1)$ y $x(2)$ con la ecuación (despejando $x(n+1)$) y con tu fórmula. Si coinciden, está bien.

### Ejemplo guiado 8.1 — 2015-05-29 T2 Ej4 (`10` Ej. 10 / `07` Ej. 9, repaso grabado)

Usando Z, resolvé $x(n+1) = 3x(n) + 2$ con $x(0) = 2$ y verificá con $x(2)$.

**Paso 1 — transformar miembro a miembro.** El 2 es $2\,u(n)$, que va a $\frac{2z}{z-1}$:

$$
z\,X(z) - z\,\underbrace{x(0)}_{2} = 3X(z) + \frac{2z}{z-1}
$$

**Paso 2 — agrupar $X(z)$.** Paso $3X$ a la izquierda y $-2z$ a la derecha; después divido por $(z-3)$ y junto en una fracción:

$$
X(z)\,(z-3) = \frac{2z}{z-1} + 2z \quad\Rightarrow\quad X(z) = \frac{2z + 2z(z-1)}{(z-1)(z-3)} = \frac{2z^2}{(z-1)(z-3)}
$$

**Paso 3 — una $z$ afuera.** Saco una $z$ de $2z^2$ (no las dos): adentro queda $\frac{2z}{(z-1)(z-3)}$, y descompongo eso:

$$
\frac{2z}{(z-1)(z-3)} = \frac{A}{z-1} + \frac{B}{z-3}, \qquad A = \frac{2}{1-3} = -1, \quad B = \frac{6}{3-1} = 3
$$

**Paso 4 — distribuir la $z$ y tabla:**

$$
X(z) = -\frac{z}{z-1} + 3\,\frac{z}{z-3} \quad\Rightarrow\quad \boxed{x(n) = -1 + 3\cdot 3^n = 3^{n+1} - 1}
$$

**Paso 5 — verificar con la ecuación** ("el siguiente es 3 veces el anterior más 2"):

$$
x(1) = 3\cdot 2 + 2 = 8, \qquad x(2) = 3\cdot 8 + 2 = 26
$$

**Paso 6 — verificar con la solución:** $x(2) = 3^3 - 1 = 26$. ✓ (Y $x(0) = 3 - 1 = 2$ ✓.)

> En el plan este ejercicio figura como práctica del mediodía: como ya lo leíste resuelto, tapalo y rehacelo solo en 8 minutos antes de seguir.

### ✍️ Tu turno 8.A (12 min) — 2015-05-29 T1 Ej4

Resolvé por transformada Z: $x(n+1) + 3x(n) = 5\cdot 2^n$, $x(0) = 2$. Verificá hallando $x(3)$ con la ecuación en diferencias y con la solución.

<details>
<summary>Corrección</summary>

(resuelto para esta guía, verificado con sympy e iterando la recurrencia)

**Transformar:** $zX - 2z + 3X = \dfrac{5z}{z-2}$, o sea $X(z)(z+3) = \dfrac{5z}{z-2} + 2z$.

**Una $z$ afuera:**

$$
X(z) = z\left[\frac{5}{(z-2)(z+3)} + \frac{2}{z+3}\right] = z\cdot\frac{2z+1}{(z-2)(z+3)}
$$

**Fracciones simples:** $A$ (polo 2) $= \frac{2\cdot 2+1}{2+3} = 1$; $B$ (polo $-3$) $= \frac{-6+1}{-3-2} = 1$.

$$
X(z) = \frac{z}{z-2} + \frac{z}{z+3} \quad\Rightarrow\quad \boxed{x(n) = 2^n + (-3)^n}
$$

**Verificación:** con la ecuación, $x(n+1) = 5\cdot 2^n - 3x(n)$:

$$
x(1) = 5 - 6 = -1, \qquad x(2) = 10 + 3 = 13, \qquad x(3) = 20 - 39 = -19
$$

Con la solución: $x(3) = 8 + (-27) = -19$. ✓

</details>

### ✍️ Tu turno 8.B (15 min) — 2025-1C T2 Ej4b (raíz doble)

Resolvé $x(n+1) - 4x(n) = 4(1-n)\,2^n$, $x(0) = 3$. Verificá con $x(2)$.

<details>
<summary>Corrección</summary>

(resolución oficial, `RESOLUCIONES-2025.md` T2 Ej4b; la verificación no está en la hoja, calculada aparte y verificada con sympy)

**1. Distribuir:** $4(1-n)2^n = 4\cdot 2^n - 4\,n\,2^n$.

**2. Transformar** con $\mathcal{Z}[2^n] = \frac{z}{z-2}$ y $\mathcal{Z}[n2^n] = \frac{2z}{(z-2)^2}$:

$$
zX - 3z - 4X = \frac{4z}{z-2} - \frac{8z}{(z-2)^2}
$$

**3. Despejar:**

$$
X(z) = \frac{4z(z-2) - 8z + 3z(z-2)^2}{(z-2)^2(z-4)} = z\cdot\frac{4(z-2) - 8 + 3(z-2)^2}{(z-2)^2(z-4)}
$$

**4. Fracciones simples** de lo de adentro: $\frac{A}{(z-2)^2} + \frac{B}{z-2} + \frac{C}{z-4}$. Tapado: $A = \frac{-8}{2-4} = 4$ (numerador en $z=2$ vale $-8$), $C = \frac{4\cdot 2 - 8 + 3\cdot 4}{4} = 3$. Coeficiente de $z^2$: $B + C = 3 \Rightarrow B = 0$.

**5. Antitransformar:** $X(z) = \frac{4z}{(z-2)^2} + \frac{3z}{z-4}$, y $\frac{4z}{(z-2)^2} = 2\cdot\frac{2z}{(z-2)^2}$:

$$
\boxed{x(n) = 2\,n\,2^n + 3\cdot 4^n}
$$

**Verificación:** ecuación: $x(1) = 4\cdot 3 + 4\cdot 1\cdot 1 = 16$, $x(2) = 4\cdot 16 + 4\cdot 0\cdot 2 = 64$. Solución: $x(2) = 2\cdot 2\cdot 4 + 3\cdot 16 = 64$. ✓

</details>

### ✍️ Tu turno 8.C (12 min) — 2024-2C rec Ej5

Resolvé por transformada Z $x(n+1) = 2x(n) + 3n - 1$, $x(0) = 0$. Comprobá hallando $x(2)$ con la solución y con la ecuación en diferencias.

<details>
<summary>Corrección</summary>

(resuelto para esta guía, verificado con sympy e iterando la recurrencia)

**Transformar** ($3n \to \frac{3z}{(z-1)^2}$, $-1 \to -\frac{z}{z-1}$, $x(0)=0$):

$$
zX - 0 = 2X + \frac{3z}{(z-1)^2} - \frac{z}{z-1} \quad\Rightarrow\quad X(z)(z-2) = \frac{3z - z(z-1)}{(z-1)^2}
$$

**Una $z$ afuera:**

$$
X(z) = z\cdot\frac{4-z}{(z-1)^2(z-2)} = z\left(\frac{A}{(z-1)^2} + \frac{B}{z-1} + \frac{C}{z-2}\right)
$$

Tapado: $A = \frac{4-1}{1-2} = -3$, $C = \frac{4-2}{(2-1)^2} = 2$. Coeficiente de $z^2$: $B + C = 0 \Rightarrow B = -2$.

**Antitransformar:** $X(z) = -3\frac{z}{(z-1)^2} - 2\frac{z}{z-1} + 2\frac{z}{z-2}$:

$$
\boxed{x(n) = -3n - 2 + 2\cdot 2^n = 2^{n+1} - 3n - 2}
$$

**Verificación:** ecuación: $x(1) = 0 + 0 - 1 = -1$, $x(2) = -2 + 3 - 1 = 0$. Solución: $x(2) = 8 - 6 - 2 = 0$. ✓

</details>

**Errores típicos de §8:**

- No distribuir el segundo miembro antes de transformar ($4(1-n)2^n$ no está en la tabla; $4\cdot 2^n$ y $n\,2^n$ sí).
- Olvidarse del $-z\,x(0)$, o poner $-x(0)$ sin la $z$.
- Leer $\frac{4z}{(z-2)^2}$ como $4\,n\,2^n$: la tabla es $\frac{2z}{(z-2)^2} \to n\,2^n$, así que es $2\,n\,2^n$.
- No verificar: si $x(2)$ no te da igual por los dos caminos, hay un error. Buscalo antes de entregar.

---

## 9. Ecuación en diferencias de 2º orden (raíz doble)

Lo mismo que §8, con dos cambios (`12` [1:23:25], `06` p. 3):

- Aparece $x(n+2)$: $\mathcal{Z}[x(n+2)] = z^2X - z^2x(0) - z\,x(1)$. Necesitás **dos datos**, $x(0)$ y $x(1)$.
- $X(z)$ queda multiplicada por un **polinomio de grado 2** (el "característico"). Factorizalo; si es un cuadrado perfecto, tenés **raíz doble** y aparece $n\,a^n$. Acá sí conviene juntar todo el segundo miembro en **un solo cociente** antes de dividir (`12` [1:24:58]).

### Ejemplo guiado 9.1 — guía ej. 8b (`06` p. 5)

$x(n+2) - 4x(n+1) + 4x(n) = 4^{n+1}$, con $x(0) = 1$, $x(1) = 10$.

**Paso 1 — segundo miembro a forma de tabla.** $4^{n+1} = 4\cdot 4^n \to \dfrac{4z}{z-4}$.

**Paso 2 — transformar miembro a miembro** con $x(0)=1$, $x(1)=10$:

$$
z^2X - z^2 - 10z - 4\left(zX - z\right) + 4X = \frac{4z}{z-4}
$$

**Paso 3 — agrupar.** Todo lo que tiene $X$ a la izquierda, el resto a la derecha ($-z^2 - 10z + 4z$ pasa como $z^2 + 6z$):

$$
X(z)\left(z^2 - 4z + 4\right) = \frac{4z}{z-4} + z^2 + 6z
$$

**Paso 4 — factorizar y despejar.** $z^2 - 4z + 4 = (z-2)^2$: raíz doble en 2. Junto en un solo cociente y saco la $z$:

$$
X(z) = \frac{4z + z^2(z-4) + 6z(z-4)}{(z-4)(z-2)^2} = z\cdot\frac{4 + z(z-4) + 6(z-4)}{(z-4)(z-2)^2}
$$

**Paso 5 — fracciones simples con raíz doble.** Por qué tres términos: el polo doble aporta $\frac{B}{(z-2)^2}$ y $\frac{C}{z-2}$.

$$
\frac{4 + z(z-4) + 6(z-4)}{(z-4)(z-2)^2} = \frac{A}{z-4} + \frac{B}{(z-2)^2} + \frac{C}{z-2}
$$

$A$: tapo $(z-4)$, $z=4$: $\frac{4}{4} = 1$. $B$: tapo $(z-2)^2$, $z=2$: $\frac{4 - 4 - 12}{2-4} = \frac{-12}{-2} = 6$. $C$: coeficiente de $z^2$ de los numeradores, $1 + C = 1 \Rightarrow C = 0$.

**Paso 6 — distribuir la $z$ y tabla.** $6 = 3\cdot 2$ para tener $\frac{2z}{(z-2)^2} \to n\,2^n$:

$$
X(z) = \frac{z}{z-4} + 3\cdot\frac{2z}{(z-2)^2} \quad\Rightarrow\quad \boxed{x(n) = 4^n + 3\,n\,2^n}
$$

**Paso 7 — verificar** (no está en la fuente; verificado con sympy). Datos: $x(0) = 1 + 0 = 1$ ✓, $x(1) = 4 + 6 = 10$ ✓. Ecuación: $x(2) = 4x(1) - 4x(0) + 4^1 = 40 - 4 + 4 = 40$; solución: $x(2) = 16 + 24 = 40$. ✓

### Ahora hacé R-I (30 min)

Desde tu hoja: **R-I** ($x(n+2) - 6x(n+1) + 9x(n) = 5\cdot 2^n$, raíz doble en 3, del repaso 2026 de tu curso). Es la receta del 9.1 al pie de la letra. Corregila con la corrección I de la hoja.

### ✍️ Tu turno 9.A (opcional, si sobra tiempo, 15 min) — `12` Ej. 12 (= guía ej. 7c)

Resolvé $x(n+2) - 4x(n+1) + 3x(n) = -2$, con $x(0)=7$, $x(1)=12$.

<details>
<summary>Corrección</summary>

(resolución de la clase teórica grabada, `12` [1:23:58]; el numerador de $X(z)$ lo completa el apunte; todo verificado con sympy)

**Transformar** ($-2 \to -\frac{2z}{z-1}$):

$$
\left[z^2X - 7z^2 - 12z\right] - 4\left[zX - 7z\right] + 3X = -\frac{2z}{z-1}
$$

$z^2-4z+3 = (z-1)(z-3)$, y como el segundo miembro trae otro $(z-1)$, queda raíz doble en 1:

$$
X(z) = \frac{z\,(7z^2 - 23z + 14)}{(z-1)^2(z-3)} = z\left[\frac{A}{(z-1)^2} + \frac{B}{z-1} + \frac{C}{z-3}\right]
$$

con $A=1$, $B=5$, $C=2$ ($A$ y $C$ por tapado, $B$ comparando coeficientes).

**Antitransformar:** $\frac{z}{(z-1)^2} \to n$, $\frac{z}{z-1}\to 1$, $\frac{z}{z-3}\to 3^n$:

$$
\boxed{x(n) = n + 5 + 2\cdot 3^n}
$$

**Verificación:** $x(0) = 5 + 2 = 7$ ✓, $x(1) = 1 + 5 + 6 = 12$ ✓; ecuación: $x(2) = 4\cdot 12 - 3\cdot 7 - 2 = 25$, solución: $2 + 5 + 18 = 25$ ✓.

</details>

**Errores típicos de §9:**

- En $\mathcal{Z}[x(n+2)]$: es $-z^2x(0) - z\,x(1)$ (el $x(0)$ va con $z^2$, el $x(1)$ con $z$).
- Olvidarse del término $\frac{C}{z-a}$ de la raíz doble (aunque después dé 0, hay que plantearlo).
- Signos al pasar $-4(zX - z\,x(0))$: el $-4\cdot(-z\,x(0))$ da $+4z\,x(0)$.

---

## Checkpoint final (10 min, sin mirar nada salvo el ayudamemoria)

1. ¿Cuánto vale $\sum_{k=0}^{\infty} r^k$ y cuándo?
2. ROC de una $X(z)$ que es suma de dos geométricas con condiciones $|z|>\frac12$ y $|z|>3$.
3. Pares e impares de $x(n) = 2^n$ (par) / $5^{-n}$ (impar): escribí solo las dos razones y la ROC.
4. ¿Cuánto da $\sum_{n=0}^{\infty} \frac{2^n}{n!}\,4^{-n}$?
5. Escribí $\mathcal{Z}[x(n+1)]$ y $\mathcal{Z}[x(n+2)]$.
6. ¿Por qué se deja una $z$ afuera antes de las fracciones simples?
7. ¿Qué es $\frac{6z}{(z-3)^2}$ en el dominio $n$?
8. ¿Cómo verificás una ecuación en diferencias?

<details>
<summary>Respuestas</summary>

(resueltas para esta guía, verificadas con sympy)

1. $\frac{1}{1-r}$, solo si $|r|<1$.
2. Intersección: $|z|>3$.
3. Pares: $2^{2k}z^{-2k} = \left(\frac{4}{z^2}\right)^k$ → $|z|>2$. Impares: $5^{-(2k+1)}z^{-(2k+1)} = \frac{1}{5z}\left(\frac{1}{25z^2}\right)^k$ → $|z|>\frac15$. ROC: $|z|>2$.
4. $e^{2/z}$ en $z=4$: $e^{1/2}$.
5. $zX - z\,x(0)$ y $z^2X - z^2x(0) - z\,x(1)$.
6. Porque todas las entradas de la tabla tienen una $z$ en el numerador; sin ella quedan términos $\frac{A}{z-a}$ que no están en la tabla.
7. $6 = 2\cdot 3$: $2\cdot\frac{3z}{(z-3)^2} \to 2\,n\,3^n$.
8. Calculás $x(1)$, $x(2)$ con la recurrencia desde los datos iniciales y los comparás con tu fórmula cerrada.

</details>

Si fallaste 2, 3 o 5: volvé a §4 o §7 antes del mediodía. Anotá lo que falló con `/registrar`.

---

*Generado el 2026-10-03. Fuentes: `examenes/resueltos/RESOLUCIONES-2025.md` (Ej4 T1 y T2), `repaso/practica-repaso-2026.md` (H, I, solo referenciados), apuntes `06`, `07`, `10`, `12`, `examenes/INDICE.md`, `plan.md` y `fuentes/AYUDAMEMORIA-OFICIAL.pdf` (págs. 2–3). Las correcciones marcadas «resuelto para esta guía» no están resueltas en las fuentes: se resolvieron y se verificaron con sympy (y, en las ecuaciones en diferencias, iterando la recurrencia). Toda la matemática de la guía se verificó con sympy 1.14.*
