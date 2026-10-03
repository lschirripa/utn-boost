# Práctica de Sistemas Estables — polos y ceros, elección de K, corte de |G(s)| y respuesta temporal

> Fuente: fuentes/clases/Sistemas Estables/Sistemas Estables.pdf, págs. 1–13

---

## Índice

- [p. 1] — Constelación de polos y ceros: cómo se lee una $G(s)$
- [p. 1] — 📝 Ejercicio 1 a) y e): constelación de polos y ceros
- [p. 2] — Elección de $K$ con un dato de módulo (método gráfico / analítico)
- [p. 2] — 📝 Ejercicio 2: $K$ con $|G(j)| = \sqrt{13/5}$ + constelación
- [p. 2] — Corte de $|G(s)|$ por el eje real ($\mathrm{Im}(s) = 0$) y por el eje imaginario ($\mathrm{Re}(s) = 0$)
- [p. 2] — 📝 Ejercicio 3: constelación, $K$ con $|G(j)| = 1$ y corte por el eje real
- [p. 3] — 📝 Ejercicio 4: $K$ para que $3j$ sea polo + $|G(j\omega)|$
- [p. 4] — Construir una transferencia a partir de sus polos y ceros
- [p. 4] — 📝 Ejercicio 6 b): transferencia con $G(0) = -2$ y polos/ceros dados
- [p. 5] — 📝 Ejercicio 6 g): coeficientes reales, cero doble y $|G(j)| = \sqrt{5/2}$
- [p. 6] — Leer la constelación desde el gráfico del corte
- [p. 6] — 📝 Ejercicio 6 i): transferencia desde el corte por el eje real con $G(0) = 3$, $G(1) = 5$
- [p. 7] — 📝 Ejercicio 7: $G(s) = \mathcal{L}[e^{-3t}\,\mathrm{sen}(at)]$ con polo en $-3 + j$
- [p. 7] — Tipo de polo → tipo de respuesta y estabilidad
- [p. 7] — 📝 Ejercicio 8: tipo de respuesta y estabilidad desde la constelación
- [p. 8] — 📝 Ejercicio 10: estabilidad, $G(-1+j)$ por método gráfico y respuesta a $e^{-t}$
- [p. 9] — Transferencia a partir de la respuesta a una entrada conocida
- [p. 9] — 📝 Ejercicio 13: $G(s)$ desde la respuesta al escalón + corte por el eje real
- [p. 10] — Ecuación diferencial física → Laplace miembro a miembro; signo de $-b/2a$
- [p. 10] — 📝 Ejercicio 19: sistema mecánico de traslación (escalón unitario, movimiento no amortiguado)
- [p. 11] — Ejercicio integrador: teorema del valor final + análisis de polos
- [p. 11] — 📝 Ejercicio 20: ¿cuál transferencia da respuesta oscilatoria amortiguada con valor estable 2?

---

## Constelación de polos y ceros: cómo se lee una $G(s)$ — [p. 1]

Reglas que el profe aplica en todos los ejercicios de la guía:

- **Ceros** $z_i$: raíces del numerador. **Polos** $p_i$: raíces del denominador. En el diagrama los ceros se marcan con **○** y los polos con **×**, sobre el plano complejo (eje real horizontal, eje imaginario vertical).
- **Siempre hay una $K$:** si la transferencia no la muestra, es $K = 1$ (anotación del profe en el ej. 1: "$k = 1$, siempre hay una $k$").
- **Simplificar antes de graficar:** se factorizan numerador y denominador y se cancelan los factores comunes (en los ejs. 1 e), 2, 3, 8 y 10 aparece un factor repetido arriba y abajo que se tacha). El diagrama se arma con la $G(s)$ ya simplificada.
- **Factorizar el denominador cúbico:** se busca una raíz entera por **Ruffini** y el cociente de segundo grado se resuelve con la fórmula resolvente $s_{1,2} = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a}$.
- **Cero en el infinito:** cuando el numerador tiene un grado menos que el denominador, el profe anota siempre un cero en el infinito ($z_2 = \infty$).

<details>
<summary>📝 Ejercicio 1 a) y e) — [p. 1]: constelación de polos y ceros</summary>

Represente la constelación de polos y ceros de las siguientes funciones:

**a)**

$$
G(s) = \frac{s}{s^2 + 2s + 2}
$$

**e)**

$$
G(s) = \frac{s^2 - s}{(s^2 + 5s + 6)(s - 1)}
$$

*(en la fuente solo están resueltos los ítems a) y e) de este ejercicio)*

<details>
<summary>Ver resolución</summary>

**Ítem a)**

**Paso 1:** ceros y polos. El numerador se anula en $s = 0$; el denominador $s^2 + 2s + 2$ tiene raíces complejas conjugadas.

$$
z_1 = 0, \quad z_2 = \infty
$$

$$
p_1 = -1 + j, \quad p_2 = -1 - j
$$

El profe anota al costado: $K = 1$, "siempre hay una $K$".

**Paso 2:** constelación. Un **○** en el origen; dos **×** en $-1 + j$ y $-1 - j$ (líneas punteadas desde $-1$ en el eje real hasta $\pm j$ en el eje imaginario para ubicarlos).

**Ítem e)**

**Paso 1:** factorizar y simplificar.

$$
G(s) = \frac{s^2 - s}{(s^2 + 5s + 6)(s - 1)} = \frac{s(s-1)}{(s^2 + 5s + 6)(s - 1)} = \frac{s}{s^2 + 5s + 6} = \frac{s}{(s+2)(s+3)}
$$

**Paso 2:** ceros y polos de la $G(s)$ simplificada.

$$
z_1 = 0, \quad z_2 = \infty, \quad p_1 = -2, \quad p_2 = -3
$$

**Paso 3:** constelación. **○** en el origen, **×** en $-2$ y **×** en $-3$, los tres sobre el eje real.

</details>

</details>

## Elección de $K$ con un dato de módulo (método gráfico / analítico) — [p. 2]

Cuando el enunciado da el valor de $|G(s_0)|$ en un punto $s_0$ (típicamente $s_0 = j$), el profe:

1. Simplifica $G(s)$ y factoriza en polos y ceros: $G(s) = K \dfrac{\prod (s - z_i)}{\prod (s - p_i)}$.
2. **Gráficamente:** marca el punto $s_0$ en la constelación (punto azul) y traza los vectores desde cada cero (verde) y desde cada polo (rojo) hasta $s_0$. El módulo de cada vector es $|s_0 - z_i|$ o $|s_0 - p_i|$.
3. **Analíticamente:** el módulo es el producto de los módulos de los vectores a los ceros sobre el producto de los módulos de los vectores a los polos, multiplicado por $K$:

$$
|G(s_0)| = K \cdot \frac{\prod |s_0 - z_i|}{\prod |s_0 - p_i|}
$$

4. Iguala al dato y despeja $K$. En los ejercicios de la guía se pide $K \in \mathbb{R}^+$, así que se toma la raíz positiva.

<details>
<summary>📝 Ejercicio 2 — [p. 2]: hallar K con |G(j)| = √(13/5) + constelación</summary>

Sea $G(s) = \dfrac{k\,(s^2 - 4s - 5)}{s^3 - 7s^2 + 17s + 25}$ la transferencia de un sistema.

a) Halle $k \in \mathbb{R}^+ \;/\; |G(j)| = \sqrt{\dfrac{13}{5}}$

b) Indique los polos y ceros de $G(s)$ y grafique la constelación.

<details>
<summary>Ver resolución</summary>

**Paso 1:** factorizar el numerador y el denominador. El numerador: $s^2 - 4s - 5 = (s+1)(s-5)$. El denominador, por Ruffini con la raíz $-1$:

$$
\begin{array}{c|cccc}
 & 1 & -7 & 17 & 25 \\
-1 & & -1 & 8 & -25 \\
\hline
 & 1 & -8 & 25 & 0
\end{array}
$$

$$
G(s) = \frac{k\,(s^2 - 4s - 5)}{s^3 - 7s^2 + 17s + 25} = \frac{k\,(s+1)(s-5)}{(s+1)(s^2 - 8s + 25)}
$$

El factor $(s+1)$ se cancela arriba y abajo.

**Paso 2:** raíces de $s^2 - 8s + 25$ con la resolvente.

$$
s_{1,2} = \frac{8 \pm \sqrt{64 - 4 \cdot 1 \cdot 25}}{2} \quad \Rightarrow \quad s_{1,2} = 4 \pm 3j
$$

**Paso 3:** constelación (ítem b). Cero **○** en $5$ (sobre el eje real); polos **×** en $4 + 3j$ y $4 - 3j$ (líneas punteadas desde $4$ hasta $\pm 3j$). El profe marca además el punto $j$ sobre el eje imaginario (punto azul) y traza los vectores desde el cero $5$ (verde) y desde los dos polos (rojos) hasta $j$: es el método gráfico del módulo.

**Paso 4:** módulo en $s = j$ e igualación al dato (ítem a). El vector desde el cero mide $|j - 5| = \sqrt{26}$; el producto de los vectores desde los polos es $|j^2 - 8j + 25| = \sqrt{32} \cdot \sqrt{20}$.

$$
\frac{k\,\sqrt{26}}{\sqrt{32} \cdot \sqrt{20}} = \sqrt{\frac{13}{5}}
$$

$$
k = \sqrt{64}
$$

$$
\boxed{k = 8}
$$

</details>

</details>

## Corte de $|G(s)|$ por el eje real ($\mathrm{Im}(s) = 0$) y por el eje imaginario ($\mathrm{Re}(s) = 0$) — [p. 2]

El "corte por el eje real" es el gráfico de $|G(s)|$ recorriendo únicamente los $s$ reales, es decir con $\mathrm{Im}(s) = 0$ (eje horizontal $\sigma = \mathrm{Re}(s)$, eje vertical $|G(s)|$). Cómo lo arma el profe en los ejercicios 3, 6 i) y 13:

- En cada **polo real** hay una **asíntota vertical** (línea punteada; la curva sube a infinito por los dos lados).
- En cada **cero real** la curva **toca el eje** ($|G| = 0$) y vuelve a subir.
- Entre dos puntos notables la curva forma **lomos** (máximos suaves). Un par de **polos complejos conjugados no da asíntota** sobre el eje real: aparece un lomo cerca de su parte real (ej. 13: lomo alrededor de $\sigma = -2$ para polos en $-2 \pm 3j$; ej. 6 i): lomo en $\sigma = 2$ para polos en $2 \pm bj$).
- Lejos de polos y ceros la curva **decae hacia el eje**.

El "corte por el eje imaginario" es lo mismo con $\mathrm{Re}(s) = 0$: se grafica $|G(j\omega)|$ contra $j\omega$; los polos imaginarios puros $\pm \omega_0 j$ dan asíntotas verticales en $\pm \omega_0$ (ej. 4). Para cada corte el profe deja un link de GeoGebra con el gráfico exacto (ver en cada ejercicio).

<details>
<summary>📝 Ejercicio 3 — [p. 2]: constelación, K con |G(j)| = 1 y corte por el eje real</summary>

Sea $G(s) = \dfrac{k\,(s^2 - 4s - 5)}{s^3 - 3s^2 - 25s + 75}$ la transferencia de un sistema.

a) Grafique la constelación de polos y ceros de $G(s)$.

b) Halle $k \in \mathbb{R}^+$ sabiendo que $|G(j)| = 1$.

c) Grafique **aproximadamente** $|G(s)|$ a lo largo del eje $\sigma = \mathrm{Re}[s]$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** factorizar. Numerador: $s^2 - 4s - 5 = (s+1)(s-5)$. Denominador por Ruffini con la raíz $5$:

$$
\begin{array}{c|cccc}
 & 1 & -3 & -25 & 75 \\
5 & & 5 & 10 & -75 \\
\hline
 & 1 & 2 & -15 & 0
\end{array}
$$

$$
G(s) = \frac{k\,(s+1)(s-5)}{(s-5)(s^2 + 2s - 15)} = \frac{k\,(s+1)}{(s-3)(s+5)}
$$

El factor $(s-5)$ se cancela.

**Paso 2:** raíces de $s^2 + 2s - 15$.

$$
s_{1,2} = \frac{-2 \pm \sqrt{4 + 4 \cdot 1 \cdot 15}}{2} = -1 \pm 4 \quad \Rightarrow \quad s_1 = 3, \quad s_2 = -5
$$

$$
z_1 = -1, \quad z_2 = \infty, \quad p_1 = 3, \quad p_2 = -5
$$

**Paso 3:** constelación (ítem a). Todo sobre el eje real: **×** en $-5$, **○** en $-1$, **×** en $3$. El profe marca el punto $j$ y traza los tres vectores (azules) desde $-5$, $-1$ y $3$ hasta $j$.

**Paso 4:** módulo en $s = j$ (ítem b). Vector desde el cero: $|j + 1| = \sqrt{2}$; desde los polos: $|j + 5| = \sqrt{26}$ y $|j - 3| = \sqrt{10}$.

$$
\frac{k\,\sqrt{2}}{\sqrt{26}\,\sqrt{10}} = 1 \quad \Rightarrow \quad k = \sqrt{130}
$$

$$
\boxed{G(s) = \frac{\sqrt{130}\,(s+1)}{(s+5)(s-3)}}
$$

**Paso 5:** corte por el eje real, $\mathrm{Im}(s) = 0$ (ítem c). Gráfico de $|G(s)|$ contra $\mathrm{Re}(s)$:

- asíntota vertical (punteada) en $\sigma = -5$ y otra en $\sigma = 3$ (polos reales);
- la curva toca el eje en $\sigma = -1$ (cero real);
- a la izquierda de $-5$ la curva baja hacia el eje; entre $-5$ y $-1$ baja desde la asíntota hasta tocar el eje en $-1$; entre $-1$ y $3$ sube hasta la asíntota; a la derecha de $3$ decae hacia el eje.

Gráfico exacto: <https://www.geogebra.org/m/czrrzpcu>

</details>

</details>

<details>
<summary>📝 Ejercicio 4 — [p. 3]: K para que 3j sea polo + |G(jω)|</summary>

Sea $G(s) = \dfrac{s(s+2)}{s^3 + 2s^2 + 9s + k}$ la transferencia de un sistema.

a) Halle $k \in \mathbb{R}$ sabiendo que $3j$ es un polo.

b) Grafique aproximadamente $|G(j\omega)|$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** si $3j$ es polo, anula el denominador. Se reemplaza $s = 3j$ y se despeja $k$ (ítem a).

$$
(3j)^3 + 2(3j)^2 + 9 \cdot 3j + k = 0
$$

$$
-27j - 18 + 27j + k = 0 \quad \Rightarrow \quad k = 18
$$

(los términos $-27j$ y $+27j$ se tachan entre sí).

**Paso 2:** factorizar el denominador con $k = 18$ por Ruffini con la raíz $-2$:

$$
\begin{array}{c|cccc}
 & 1 & 2 & 9 & 18 \\
-2 & & -2 & 0 & -18 \\
\hline
 & 1 & 0 & 9 & 0
\end{array}
$$

$$
G(s) = \frac{s(s+2)}{s^3 + 2s^2 + 9s + 18} = \frac{s(s+2)}{(s+2)(s^2 + 9)}
$$

$$
\boxed{G(s) = \frac{s}{s^2 + 9}}
$$

**Paso 3:** polos y ceros, con $\mathrm{Re}(s) = 0$ (ítem b).

$$
z_1 = 0, \quad z_2 = \infty, \quad p_1 = 3j, \quad p_2 = -3j
$$

**Paso 4:** corte por el eje imaginario. Gráfico de $|G(s)|$ contra $j\omega$: asíntotas verticales (punteadas) en $-3$ y en $3$; la curva toca el eje en el origen (cero en $s = 0$); hacia afuera de las asíntotas decae hacia el eje.

Gráfico exacto: <https://www.geogebra.org/m/pgmyudtt>

</details>

</details>

## Construir una transferencia a partir de sus polos y ceros — [p. 4]

Cuando el enunciado da polos, ceros y un dato extra ($G(0)$, $|G(j)|$, …), el profe arma:

$$
G(s) = K \cdot \frac{\prod (s - z_i)}{\prod (s - p_i)}
$$

- Un **par complejo conjugado** $a \pm bj$ se arma directamente como un factor cuadrático con coeficientes reales (fórmula resaltada en la fuente):

$$
\big(s - (a + bj)\big)\big(s - (a - bj)\big) = s^2 - 2as + a^2 + b^2
$$

(en la fuente el profe desarrolla el producto y tacha de a pares los términos con $j$, que se cancelan entre sí; lo que queda, resaltado, es $s^2 - 2as + a^2 + b^2$).

- Un **cero doble** va como factor al cuadrado: $(s - z_1)^2$.
- **"Coeficientes reales"** en el enunciado implica que los **polos complejos vienen de a pares conjugados**: si dan $p_1 = -4 + j$, hay un $p_3 = -4 - j$ aunque no lo digan.
- El dato extra sirve para despejar $K$: $G(0)$ se evalúa directamente; $|G(j)|$ se calcula con módulos como en la sección anterior.

<details>
<summary>📝 Ejercicio 6 b) — [p. 4]: transferencia con G(0) = −2 y polos/ceros dados</summary>

Construya funciones de transferencia que cumplan los siguientes requisitos:

**b)** $G(0) = -2$; ceros $z_1 = -3 - j$, $z_2 = -3 + j$; polos $p_1 = -2 + 3j$, $p_2 = -2 - 3j$, $p_3 = 1$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** armar los factores cuadráticos de cada par conjugado con $s^2 - 2as + a^2 + b^2$. Ceros $-3 \pm j$: $s^2 + 6s + 10$. Polos $-2 \pm 3j$: $s^2 + 4s + 13$. Polo real $1$: $(s - 1)$.

$$
G(s) = \frac{k\,(s^2 + 6s + 10)}{(s - 1)(s^2 + 4s + 13)}
$$

**Paso 2:** usar $G(0) = -2$ para despejar $k$.

$$
G(0) = -2 = \frac{10 \cdot k}{-13} \quad \Rightarrow \quad k = \frac{13}{5}
$$

**Paso 3:** transferencia final.

$$
\boxed{G(s) = \frac{\frac{13}{5}\,(s^2 + 6s + 10)}{(s - 1)(s^2 + 4s + 13)}}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 6 g) — [p. 5]: coeficientes reales, cero doble y |G(j)| = √(5/2)</summary>

Construya una función de transferencia que cumpla: coeficientes reales; $p_1 = -4 + j$; $p_2 = -1$; $z_1 = -2$ (doble); $|G(j)| = \sqrt{\dfrac{5}{2}}$.

<details>
<summary>Ver resolución</summary>

**Paso 1:** "coeficientes reales" ⇒ los polos complejos son conjugados ⇒ hay un tercer polo $p_3 = -4 - j$.

**Paso 2:** armar la transferencia. Cero doble: $(s+2)^2$. Polo real: $(s+1)$. Par $-4 \pm j$: $s^2 + 8s + 17$.

$$
G(s) = \frac{k\,(s+2)^2}{(s+1)(s^2 + 8s + 17)}
$$

**Paso 3:** módulo en $s = j$ e igualación al dato.

$$
|G(j)| = \sqrt{\frac{5}{2}} = \frac{k\,|2 + j|^2}{|1 + j| \cdot |8j + 16|} = \frac{5\,k}{\sqrt{2}\,\sqrt{320}}
$$

$$
\boxed{k = 8}
$$

**Paso 4:** transferencia final.

$$
\boxed{G(s) = \frac{8\,(s+2)^2}{(s+1)(s^2 + 8s + 17)}}
$$

Al costado, en la p. 6, el profe deja dos esquemas sueltos de cómo se ve $|G|$ cerca de un polo real: una asíntota vertical punteada con las dos ramas de la curva subiendo a infinito a cada lado [sin texto que los explique en la fuente].

</details>

</details>

## Leer la constelación desde el gráfico del corte — [p. 6]

Problema inverso: dan el gráfico de $|G(s)|$ sobre el eje real y hay que reconstruir $G(s)$. Lo que lee el profe en el ej. 6 i):

- **Asíntota vertical** en $\sigma = \sigma_0$ → polo real $p = \sigma_0$.
- La curva **toca el eje** en $\sigma_0$ → cero real $z = \sigma_0$.
- **Lomo sin asíntota** centrado en $\sigma_0$ → par de polos complejos conjugados $\sigma_0 \pm bj$, con **$b$ desconocido** (el gráfico del corte no lo muestra).
- Las incógnitas que quedan ($K$ y $b$) se despejan con los datos numéricos del enunciado ($G(0)$, $G(1)$, …), armando un sistema de ecuaciones.

<details>
<summary>📝 Ejercicio 6 i) — [p. 6]: transferencia desde el corte por el eje real con G(0) = 3, G(1) = 5</summary>

Construya una función de transferencia sabiendo que $G(0) = 3$, $G(1) = 5$ y el corte de la misma con el eje real es el siguiente gráfico de $|G(s)|$ contra $\sigma = \mathrm{Re}(s)$: un lomo chico a la izquierda que baja a tocar el eje en $\sigma = -3$, una asíntota vertical (punteada) en $\sigma = -1$, un lomo redondeado centrado en $\sigma = 2$ y, a la derecha, la curva decae hacia el eje.

<details>
<summary>Ver resolución</summary>

**Paso 1:** leer polos y ceros del gráfico. Asíntota en $-1$ → polo real; toca el eje en $-3$ → cero real; lomo en $2$ sin asíntota → par complejo conjugado con parte real $2$ y parte imaginaria $b$ desconocida.

$$
p_1 = -1, \quad p_2 = 2 + bj, \quad p_3 = 2 - bj, \qquad z_1 = -3, \quad z_2 = \infty
$$

**Paso 2:** armar la transferencia con el par conjugado como $s^2 - 2as + a^2 + b^2$ ($a = 2$).

$$
G(s) = \frac{k\,(s+3)}{(s^2 - 4s + 4 + b^2)(s+1)}
$$

**Paso 3:** plantear las dos condiciones.

$$
G(0) = \frac{3k}{4 + b^2} = 3 \quad \Rightarrow \quad k = 4 + b^2
$$

$$
G(1) = \frac{4k}{(1 + b^2) \cdot 2} = 5
$$

**Paso 4:** reemplazar $k$ en la segunda y despejar $b$.

$$
\frac{4\,(4 + b^2)}{1 + b^2} = 10
$$

$$
16 + 4b^2 = 10 + 10b^2
$$

$$
6\,b^2 = 6
$$

$$
\boxed{b = \pm 1} \qquad \boxed{k = 5}
$$

**Paso 5:** transferencia final.

$$
\boxed{G(s) = \frac{5\,(s+3)}{(s+1)(s^2 - 4s + 5)}}
$$

Gráfico exacto: <https://www.geogebra.org/m/hncqz6fy>

</details>

</details>

<details>
<summary>📝 Ejercicio 7 — [p. 7]: G(s) = L[e^(−3t)·sen(at)] con polo en −3 + j</summary>

Dada $G(s) = \mathcal{L}[\,g(t)\,]$ siendo $g(t) = e^{-3t} \cdot \mathrm{sen}(at)$.

a) Halle el valor de $a \in \mathbb{R}^+$ tal que uno de los polos de $G(s)$ sea $p_1 = -3 + j$.

b) Halle el otro polo.

<details>
<summary>Ver resolución</summary>

**Paso 1:** transformar $g(t)$ (seno con traslación en $s$).

$$
G(s) = \frac{a}{(s+3)^2 + a^2}, \qquad a \in \mathbb{R}^+
$$

**Paso 2:** los polos son el par conjugado (ítem b).

$$
p_1 = -3 + j, \qquad p_2 = -3 - j
$$

**Paso 3:** si $p_1$ es polo, anula el denominador (ítem a).

$$
(-3 + j + 3)^2 + a^2 = 0
$$

$$
a^2 - 1 = 0
$$

$$
\boxed{a = 1}
$$

</details>

</details>

## Tipo de polo → tipo de respuesta y estabilidad — [p. 7]

El profe decide el tipo de respuesta mirando qué fracciones simples genera cada polo de $G(s)$ (o de $Y(s)$) y qué antitransformada le corresponde. Lo que anota en los ejercicios 8, 10, 19 y 20:

| Polo | Fracción simple | Aporte a $y(t)$ | Qué dice el profe |
|---|---|---|---|
| Real positivo ($s = 3$) | $\dfrac{B}{s - 3}$ | $B\,e^{3t}$ | **S.I.** (sistema inestable): respuesta exponencial **creciente** |
| Real negativo ($s = -1$) | $\dfrac{b}{s + 1}$ | $b\,e^{-t}$ | exponencial **decreciente** (tiende a $0$) |
| En el origen ($s = 0$) | $\dfrac{A}{s}$ | $A$ (constante) | aporta el **valor estable (V.E.)**; con un polo real negativo: **sistema marginalmente estable**, "respuesta exponencial decreciente desplazada" |
| Imaginarios puros ($s^2 + 4$, $s^2 + 9$) | $\dfrac{Bs + C}{s^2 + 4}$ | senos / cosenos | polos complejos conjugados con **parte real $= 0$** ⇒ respuesta **oscilatoria de amplitud constante**, **NO** amortiguada |
| Complejos con parte real negativa ($(s+3)^2 + 1$) | $\dfrac{Bs + C}{s^2 + 6s + 10}$ | $2\,\mathrm{sen}(t)\,e^{-3t}$ | $-\dfrac{b}{2a} < 0$ ⇒ respuesta **oscilatoria amortiguada** |

Para un denominador cuadrático $as^2 + bs + c$ con raíces complejas, **el signo de $b$ determina de qué lado del eje imaginario caen los polos**, porque su parte real es $-\dfrac{b}{2a}$: si $-\dfrac{b}{2a} < 0$ están en el semiplano izquierdo (amortiguado); si $b = 0$ quedan sobre el eje imaginario (amplitud constante).

<details>
<summary>📝 Ejercicio 8 — [p. 7]: tipo de respuesta y estabilidad desde la constelación</summary>

Sea $G(s) = \dfrac{s^2 + 3s + 2}{s^3 - 2s^2 - 3s}$ la transferencia de un sistema. De acuerdo a la configuración de polos y ceros, indique el tipo de respuesta del mismo y si es un sistema estable.

<details>
<summary>Ver resolución</summary>

**Paso 1:** factorizar. Numerador: $s^2 + 3s + 2 = (s+1)(s+2)$. Denominador por Ruffini con la raíz $-1$:

$$
\begin{array}{c|cccc}
 & 1 & -2 & -3 & 0 \\
-1 & & -1 & 3 & 0 \\
\hline
 & 1 & -3 & 0 & 0
\end{array}
$$

$$
G(s) = \frac{s^2 + 3s + 2}{s^3 - 2s^2 - 3s} = \frac{(s+1)(s+2)}{(s+1)(s^2 - 3s)} = \frac{s + 2}{s(s - 3)}
$$

**Paso 2:** descomponer en fracciones simples para ver qué aporta cada polo.

$$
\frac{s + 2}{s(s - 3)} = \frac{A}{s} + \frac{B}{s - 3}
$$

El término $\dfrac{B}{s-3}$ antitransforma a $B\,e^{3t}$.

**Paso 3:** constelación: **○** en $-2$, **×** en $0$ y **×** en $3$ (todos sobre el eje real).

**Paso 4:** conclusión. Hay un polo real positivo ($s = 3$) ⇒ **S.I.** (sistema inestable): **respuesta exponencial creciente**.

</details>

</details>

<details>
<summary>📝 Ejercicio 10 — [p. 8]: estabilidad, G(−1+j) por método gráfico y respuesta a e^(−t)</summary>

Sea $G(s) = \dfrac{3s^2 - 6s - 24}{s^3 - 3s^2 - 4s}$ la transferencia de un sistema.

a) Grafique la constelación de polos y ceros de $G(s)$ e indique si el sistema es estable.

b) Halle módulo y fase de $G(-1 + j)$ por el método gráfico y por método analítico.

c) ¿Cuál será la respuesta del sistema si se lo excita con una señal $v_1(t) = e^{-t}$?

<details>
<summary>Ver resolución</summary>

**Paso 1:** factorizar y simplificar.

$$
G(s) = \frac{3s^2 - 6s - 24}{s^3 - 3s^2 - 4s} = \frac{3\,(s - 4)(s + 2)}{s\,(s - 4)(s + 1)} = \frac{3\,(s + 2)}{s\,(s + 1)}
$$

El factor $(s - 4)$ se cancela. El profe anota debajo de cada polo lo que aporta: $\dfrac{1}{s} \to A$, $\dfrac{1}{s+1} \to b\,e^{-t}$.

**Paso 2:** constelación y estabilidad (ítem a). **○** en $-2$, **×** en $-1$, **×** en $0$, sobre el eje real. Conclusión del profe: **sistema marginalmente estable** (respuesta exponencial decreciente desplazada; la constante $A$ es el **V.E.**).

**Paso 3:** método gráfico para $G(-1 + j)$ (ítem b). Se marca el punto $-1 + j$ (azul) y se trazan los vectores desde el cero $-2$ (verde) y desde los polos $-1$ y $0$ (azules) hasta ese punto. El vector desde $-2$ forma ángulo $\dfrac{\pi}{4}$ con el eje real; el vector desde $-1$ es vertical, ángulo $\dfrac{\pi}{2}$; el vector desde $0$ forma ángulo $\dfrac{3\pi}{4}$.

**Paso 4:** módulo y argumento (ítem b).

$$
|G(-1 + j)| = \frac{3\,\sqrt{2}}{1 \cdot \sqrt{2}} = 3
$$

$$
\mathrm{Arg}\big(G(-1 + j)\big) = \frac{\pi}{4} - \left(\frac{\pi}{2} + \frac{3\pi}{4}\right) = -\pi
$$

(módulo: $3$ por el módulo del vector al cero, dividido el producto de los módulos de los vectores a los polos; argumento: ángulo del vector al cero menos la suma de los ángulos de los vectores a los polos).

**Paso 5:** respuesta a $f(t) = e^{-t}$ (ítem c). La salida es $Y(s) = G(s)\,F(s)$ con $F(s) = \dfrac{1}{s+1}$.

$$
Y(s) = \frac{3\,(s + 2)}{s\,(s + 1)^2}
$$

$$
\mathcal{L}^{-1}\big(Y(s)\big) = y(t)
$$

**Paso 6:** fracciones simples (polo doble en $-1$).

$$
Y(s) = \frac{A}{s} + \frac{B}{(s+1)^2} + \frac{C}{s+1}, \qquad A = 6, \quad B = -3, \quad C = -6
$$

$$
Y(s) = \frac{6}{s} - \frac{3}{(s+1)^2} - \frac{6}{s+1}
$$

**Paso 7:** antitransformar.

$$
\boxed{y(t) = 6 - 3\,t\,e^{-t} - 6\,e^{-t}}
$$

Debajo de cada término el profe marca a qué tiende: $6 \to 6$, $-3te^{-t} \to 0$, $-6e^{-t} \to 0$ (el valor estable es $6$).

</details>

</details>

## Transferencia a partir de la respuesta a una entrada conocida — [p. 9]

Si el enunciado da la **salida** $y(t)$ a una entrada conocida, la transferencia sale del cociente de transformadas:

$$
G(s) = \frac{Y(s)}{F(s)}
$$

- Entrada **escalón** $E(t)$: $F(s) = \dfrac{1}{s}$ ⇒ $G(s) = s \cdot Y(s)$.
- Entrada **impulso** $\delta(t)$: $F(s) = \mathcal{L}(\delta(t)) = 1$ ⇒ $Y(s) = G(s)$ (ej. 20).

Receta: transformar $y(t)$ término a término, llevar $Y(s)$ a una sola fracción, dividir por $F(s)$ (con el escalón, el $s$ del numerador cancela el $s$ del denominador) y recién después sacar polos, ceros y el corte.

<details>
<summary>📝 Ejercicio 13 — [p. 9]: G(s) desde la respuesta al escalón + corte por el eje real</summary>

Sea $y(t) = 5 - 5\,e^{-2t}\cos(3t)$ la salida o respuesta de un sistema a una entrada escalón $E(t)$.

a) Indique la función transferencia $G(s)$ correspondiente.

b) Haga el diagrama o constelación de polos y ceros y grafique **aproximadamente** el corte de $|G(s)|$ por el eje real.

<details>
<summary>Ver resolución</summary>

**Paso 1:** planteo. $y(t)$ es la respuesta a $E(t)$, cuya transformada es $F(s) = \dfrac{1}{s}$.

$$
G(s) = \frac{Y(s)}{F(s)}
$$

**Paso 2:** transformar la salida (coseno con traslación en $s$).

$$
Y(s) = \frac{5}{s} - \frac{5\,(s + 2)}{(s + 2)^2 + 9}
$$

**Paso 3:** llevar a una sola fracción.

$$
Y(s) = \frac{5\,\big[(s+2)^2 + 9\big] - 5s^2 - 10s}{s\,\big[(s+2)^2 + 9\big]}
$$

$$
Y(s) = \frac{10s + 65}{s\,(s^2 + 4s + 13)}
$$

**Paso 4:** dividir por $F(s)$: el $s$ que multiplica cancela el $s$ del denominador (ítem a).

$$
\frac{Y(s)}{F(s)} = \frac{(10s + 65) \cdot s}{s\,(s^2 + 4s + 13)} = G(s)
$$

$$
\boxed{G(s) = \frac{10s + 65}{s^2 + 4s + 13}}
$$

**Paso 5:** polos y ceros (ítem b).

$$
z_1 = -6{,}5, \qquad p_1 = -2 + 3j, \qquad p_2 = -2 - 3j
$$

Constelación: **○** en $-6{,}5$ sobre el eje real; **×** en $-2 + 3j$ y $-2 - 3j$ (líneas punteadas desde $-2$ hasta $\pm 3j$).

**Paso 6:** corte de $|G(s)|$ por el eje real (ítem b). Gráfico de $|G(s)|$ contra $\sigma$: la curva viene baja desde la izquierda, **toca el eje en $\sigma = -6{,}5$** (cero real), sube formando un **lomo redondeado centrado alrededor de $\sigma = -2$** (parte real de los polos complejos; **no hay asíntota** porque los polos no son reales) y después decae hacia el eje hacia la derecha.

Gráfico exacto: <https://www.geogebra.org/m/qb7ahfvr>

</details>

</details>

## Ecuación diferencial física → Laplace miembro a miembro; signo de $-b/2a$ — [p. 10]

Para un sistema dado por su ecuación diferencial (ej. 19, sistema mecánico):

- **"Parte del reposo"** significa posición y velocidad iniciales nulas: $y(0) = 0$ (pos.) y $y'(0) = 0$ (vel.). Con eso, los términos de condiciones iniciales de las transformadas de las derivadas se tachan.
- Se aplica **Laplace miembro a miembro** ("Laplace m.a.m."), se saca $Y(s)$ factor común y se despeja. Después, fracciones simples y antitransformada.
- La relación con la transferencia es $Y(s) = F(s)\,G(s)$, o sea $G(s) = \dfrac{Y(s)}{F(s)}$.
- Para analizar **cómo cambia la respuesta con un parámetro** (el rozamiento $B$), se mira el denominador cuadrático $s^2 + Bs + K$: **el signo de $b$ determina de qué lado del eje imaginario se ubican los polos**, porque su parte real es $-\dfrac{b}{2a}$. Con $b < 0$ no habría polos en el semiplano izquierdo (pero un coeficiente de rozamiento no puede ser negativo); con $b = 0$ el denominador queda $s^2 + c$, que **da lugar a senos o cosenos**: respuesta **oscilatoria de amplitud constante** (no amortiguada).

<details>
<summary>📝 Ejercicio 19 — [p. 10]: sistema mecánico de traslación (escalón unitario, movimiento no amortiguado)</summary>

Sea el sistema mecánico de traslación de la figura (un carro de masa $M$ sobre rodillos, con la fuerza $F(t)$ aplicada por la izquierda, un resorte $K$ que lo une a la pared de la derecha y un amortiguador $B$ por debajo), cuya E.D. de movimiento es (aplicando la 2.ª Ley de Newton):

$$
F(t) - K\,y(t) - B\,y'(t) = M\,y''(t)
$$

a) Considerar $M = 1$ [Kg], $B = 5$ [Kg/s], $K = 4$ [N/m] y hallar la respuesta del sistema a un escalón unitario sabiendo que parte del reposo. (Resolver por Transf. de Laplace.)

b) ¿Qué valor debería tener $B$ para que el movimiento no sea amortiguado? Justifique.

<details>
<summary>Ver resolución</summary>

**Paso 1:** condiciones iniciales. Reposo: $y(0) = 0$ (posición $= 0$) e $y'(0) = 0$ (velocidad $= 0$).

**Paso 2:** Laplace miembro a miembro con $M = 1$, $B = 5$, $K = 4$ y $F(t)$ = escalón unitario ($F(s) = 1/s$). Los términos con $y(0)$ e $y'(0)$ se tachan.

$$
\frac{1}{s} - 4\,Y(s) - 5\,\big[s\,Y(s) - y(0)\big] = 1 \cdot \big[s^2\,Y(s) - s\,y(0) - y'(0)\big]
$$

$$
Y(s)\,(s^2 + 5s + 4) = \frac{1}{s}
$$

**Paso 3:** despejar $Y(s)$ y factorizar (ítem a). Al costado el profe recuerda $Y(s) = F(s)\,G(s)$ y $G(s) = \dfrac{Y(s)}{F(s)}$.

$$
Y(s) = \frac{1}{s\,(s + 1)(s + 4)}
$$

**Paso 4:** fracciones simples.

$$
Y(s) = \frac{A}{s} + \frac{B}{s + 1} + \frac{C}{s + 4}, \qquad A = \frac{1}{4}, \quad B = -\frac{1}{3}, \quad C = \frac{1}{12}
$$

$$
Y(s) = \frac{1/4}{s} - \frac{1/3}{s + 1} + \frac{1/12}{s + 4}
$$

**Paso 5:** antitransformar.

$$
\boxed{y(t) = \frac{1}{4} - \frac{1}{3}\,e^{-t} + \frac{1}{12}\,e^{-4t}}
$$

**Paso 6:** $B \in \mathbb{R}$ para que el movimiento no sea amortiguado (ítem b). Se mira el denominador $s^2 + 5s + 4$: el signo de $b$ (el coeficiente de $s$, que es $B$) determina de qué lado del eje imaginario se ubican los polos, porque su parte real es $-\dfrac{b}{2a}$.

- Si $b < 0$ ⇒ no tendré polos en el semiplano izquierdo. Pero $b$ no puede ser $< 0$ porque es un coeficiente de rozamiento.
- Entonces:

$$
\boxed{B = 0}
$$

Con $B = 0$ el denominador queda $s^2 + 4$, que va a dar lugar a senos o cosenos: **respuesta oscilatoria de amplitud constante**. En azul el profe lo verifica:

$$
Y(s) = \frac{1}{s\,(s^2 + 4)} = \frac{A}{s} + \frac{Bs + C}{s^2 + 4} \quad \to \quad A + \mathrm{sen}(2t)
$$

(el primer término aporta la constante $A$ y el segundo un seno de pulsación $2$ sin amortiguar).

</details>

</details>

## Ejercicio integrador: teorema del valor final + análisis de polos — [p. 11]

Para decidir **cuál de varias transferencias** cumple una condición sobre la respuesta (tipo de respuesta + valor estable), el profe plantea dos caminos:

- **Alternativa 1:** hacer todas las antitransformadas y ver cuál cumple.
- **Alternativa 2:** **teorema del valor final** + **análisis de polos**. Es la que usa.

Con entrada impulso, $F(s) = \mathcal{L}(\delta(t)) = 1$ ⇒ $Y(s) = G(s)$, así que se analizan directamente los polos de $G(s)$.

**Teorema del valor final (T.V.F.):**

$$
\lim_{s \to 0} s \cdot Y(s) = \lim_{t \to \infty} y(t) = \text{V.E.}
$$

Receta: (1) descartar por polos las que no dan el tipo de respuesta pedido (parte real $= 0$ ⇒ no es amortiguada; $-b/2a < 0$ ⇒ oscilatoria amortiguada); (2) entre las que quedan, aplicar el T.V.F. y quedarse con la que da el valor estable pedido.

<details>
<summary>📝 Ejercicio 20 — [p. 11]: ¿cuál transferencia da respuesta oscilatoria amortiguada con valor estable 2?</summary>

**Parte 4: ejercicio integrador.** Dadas las transferencias:

$$
G_1(s) = \frac{6}{s^2 + 9}, \qquad G_2(s) = \frac{2}{s^2 + 6s + 10}, \qquad G_3(s) = \frac{6s + 20}{s^3 + 6s^2 + 10s}
$$

a) Indique cuál de ellas corresponde a un sistema cuya respuesta a la entrada impulso $f(t) = \delta(t)$ es oscilatoria amortiguada con valor estable 2. Justifique correctamente.

<details>
<summary>Ver resolución</summary>

**Paso 1:** qué hay que cumplir con entrada $f(t) = \delta(t)$: (✓) salida oscilatoria amortiguada y (✓) V.E. $= 2$. Como $Y(s) = G(s)\,F(s)$ y $F(s) = \mathcal{L}(\delta(t)) = 1$:

$$
Y(s) = G(s)
$$

El profe enumera dos alternativas (hacer todas las antitransformadas, o T.V.F. + análisis de polos) y sigue por la segunda.

**Paso 2:** análisis de polos de $G_1$.

$$
G_1(s) = \frac{6}{s^2 + 9} \quad \to \quad 2\,\mathrm{sen}(3t)
$$

Polos complejos conjugados con **parte real $= 0$** ⇒ **NO** es oscilatoria amortiguada. Se descarta.

**Paso 3:** análisis de polos de $G_2$.

$$
G_2(s) = \frac{2}{s^2 + 6s + 10} = \frac{2}{(s+3)^2 + 1} \quad \to \quad 2\,\mathrm{sen}(t)\,e^{-3t}
$$

**Paso 4:** análisis de polos de $G_3$.

$$
G_3(s) = \frac{6s + 20}{s^3 + 6s^2 + 10s} = \frac{6s + 20}{s\,\big[(s+3)^2 + 1\big]} \quad \to \quad \frac{A}{s} + \frac{Bs + C}{s^2 + 6s + 10}
$$

Tanto $G_2$ como $G_3$ cumplen $-\dfrac{b}{2a} < 0$ ⇒ ambas dan respuesta oscilatoria amortiguada.

**Paso 5:** teorema del valor final para decidir entre $G_2$ y $G_3$.

$$
\text{T.V.F.:} \quad \lim_{s \to 0} s \cdot Y(s) = \lim_{t \to \infty} y(t) = \text{V.E.}
$$

$$
G_2: \quad \lim_{s \to 0} \frac{2\,s}{s^2 + 6s + 10} = 0 \neq 2 \quad ✗
$$

$$
G_3: \quad \lim_{s \to 0} \frac{s\,(6s + 20)}{s\,(s^2 + 6s + 10)} = 2 \quad ✓
$$

**Paso 6:** respuesta.

$$
\boxed{\text{Rta.} = G_3}
$$

</details>

</details>

---

*Generado el 2026-10-02 a partir de `fuentes/clases/Sistemas Estables/Sistemas Estables.pdf` (OneNote de la práctica de Sistemas Estables, guía tipeada + resolución manuscrita del profesor, 13 páginas). Transcripción fiel del manuscrito; los gráficos de GeoGebra linkeados son los que dejó el profesor en la fuente.*
