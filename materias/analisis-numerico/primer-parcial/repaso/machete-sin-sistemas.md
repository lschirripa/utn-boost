<style>
/* Estilo compacto propio del machete: dos columnas, letra chica, tablas a todo el ancho. */
@page { margin: .8cm .8cm; }
body { font-size: 8pt; line-height: 1.25; }
#content { column-count: 2; column-gap: 6mm; column-fill: auto; }
#content > h1 { font-size: 13pt; margin: 0 0 .3rem; padding-bottom: .15rem; column-span: all; }
#content > blockquote { column-span: all; margin: .3rem 0 .5rem; padding: .1rem .6rem; font-size: 8pt; }
h2 { font-size: 10.5pt; margin: .5rem 0 .25rem; padding-bottom: .1rem; break-after: avoid; column-span: all; }
h3 { font-size: 9pt; margin: .45rem 0 .15rem; break-after: avoid; }
p, ul, ol { margin: .2rem 0; }
li { margin: .06rem 0; }
ul, ol { padding-left: 1.1rem; }
table { column-span: all; font-size: 7.5pt; margin: .3rem 0; }
th, td { padding: .1rem .3rem; }
.katex-display { margin: .3rem 0; }
.katex { font-size: 1em; }
hr { margin: .45rem 0; border: 0; border-top: 1px solid #bbb; column-span: all; }
</style>

## 0 · Tabla de decisión: ¿qué me están pidiendo?

| El enunciado dice… | Receta | Dónde |
|---|---|---|
| "Completá para que la STF sea **solo cosenos**" / "SEF con coeficientes **reales**" | extensión **par**, $b_m = 0$, $\frac{2}{L}\int_0^L$ | §1.2 |
| "…**solo senos**" / "coeficientes **imaginarios puros**" | extensión **impar**, $a_0 = a_m = 0$ | §1.2 |
| "Hallá los $C_m$ de la SEF" (después de la STF) | $C_m = \tfrac12(a_m - j\,b_m)$, sin integrar | §1.1 |
| "¿Cuál es la STF de $2\operatorname{sen}x\cos x$ / $\cos^2 x$?" | identidad trigonométrica: ya es la serie | §1.3 |
| "Completá con **simetría de media onda** y paridad" | $T = 4\ell$, cuatro tramos, **sin serie** | §1.4 |
| "Espectro de amplitudes" | bastones $\lvert C_m\rvert$ en $m\omega_0$ | §1.1 |
| V/F conceptual de Fourier | las siete ideas | §1.5 |
| "$\int_0^\infty (\dots)\,e^{-kt}\,dt$ con Laplace" | es $F(k)$: transformar y evaluar al final | §2.2 |
| …con una $t$ multiplicando | derivar $F$ y cambiar el signo | §2.2 |
| …dividido por $t$ (dos exponenciales, $\operatorname{sen}t/t$) | $\int_s^\infty F(u)\,du$ + chequeo del límite | §2.3 |
| "$\mathcal{L}[\operatorname{sen}^3 t]$, $\cos^3 t$, $\operatorname{sen}5t\cos2t$" | Euler → suma de senos/cosenos → tabla | §2.4 |
| "$\mathcal{L}\left[\int_0^t f(u)\,g(t-u)\,du\right]$" | $F(s)\cdot G(s)$ | §2.5 |
| "Antitransformá" un cociente de polinomios | fracciones simples + tapado | §2.6 |
| "Antitransformá **por convolución**" / $(s^2+1)^2$ | partir en dos factores, integral en $u$ | §2.7 |
| "Demostrá $\mathcal{L}[2^t] = \frac{1}{s-\ln 2}$" | $a^t = e^{t\ln a}$ | §2.8 |
| "$\mathcal{Z}$ y ROC de $x(n)$ definida por paridad" | dos geométricas, ROC = intersección | §4.2 |
| "V/F: la ROC es $\lvert z\rvert > \dots$" | solo las razones, sin sumar | §4.2 |
| "Resolvé mediante Z: $\sum x(n)\,c^{-n}$" | $X(z)$ evaluada en $z = c$ | §4.3 |
| Secuencia finita / gráfico de bastones | definición término a término | §4.4 |
| "Antitransformá $X(z)$" | **una $z$ afuera** → fracciones simples → tabla | §4.5 |
| "Ecuación en diferencias $x(n+1)\dots$, verificá con $x(2)$" | transformar, despejar, $z$ afuera, verificar | §4.6 |
| "…$x(n+2)\dots$, $x(0)$ y $x(1)$" | ídem con $z^2X - z^2x(0) - z\,x(1)$; raíz doble → $n\,a^n$ | §4.7 |

---

## 1 · Fourier (Ej1)

### 1.1 Lo que no está en el ayudamemoria

- $\omega_0 = \dfrac{\pi}{L} = \dfrac{2\pi}{T}$. El dato en $(0, a)$ es **medio período**: $L = a$, $T = 2a$. (Dato en $(0,\pi)$ ⇒ $\omega_0 = 1$; en $(0,2)$ ⇒ $\omega_0 = \pi/2$; en $(0,1)$ ⇒ $\omega_0 = \pi$.)
- **Par** ⇒ $b_m = 0$ (solo cosenos + $a_0/2$). **Impar** ⇒ $a_0 = a_m = 0$ (solo senos). Y el atajo, integrando **solo sobre el dato**:

$$
\text{par:}\quad a_m = \frac{2}{L}\int_0^L f(t)\cos(m\omega_0 t)\,dt
$$

$$
\text{impar:}\quad b_m = \frac{2}{L}\int_0^L f(t)\operatorname{sen}(m\omega_0 t)\,dt
$$

- $\cos(m\pi) = (-1)^m$ y $\operatorname{sen}(m\pi) = 0$. No hace falta justificarlo.
- STF → SEF: $C_0 = \dfrac{a_0}{2}$ y $C_m = \dfrac12\,(a_m - j\,b_m)$. Por eso **reales ⇒ par** (no hay $b_m$) e **imaginarios puros ⇒ impar** (no hay $a_m$). Bajo la sumatoria de la SEF, aclarar $m \neq 0$.
- $(-1)^m - 1$ vale $0$ si $m$ par y $-2$ si $m$ impar ⇒ separar casos y escribir la serie con $m = 2k+1$, $k$ desde $0$.
- Media onda $f(t + T/2) = -f(t)$ (la definición sí está) ⇒ **solo armónicas impares** y valor medio $0$. Paridad **y** media onda ⇒ $T = 4\ell$ ($\ell$ = largo del dato).
- Valor medio $= a_0/2 = C_0$ = altura promedio en un período: con $f$ par se lee del gráfico (triángulo de $0$ a $h$ ⇒ $h/2$).
- Las dos integrales de siempre (están en la tabla de integrales; si hay $m\omega_0 t$, cambiar $m$ por $m\omega_0$):

$$
\int t\cos(mt)\,dt = \frac{\cos(mt)}{m^2} + \frac{t\operatorname{sen}(mt)}{m}
$$

$$
\int t\operatorname{sen}(mt)\,dt = \frac{\operatorname{sen}(mt)}{m^2} - \frac{t\cos(mt)}{m}
$$

- Espectro de amplitudes: bastones de altura $\lvert C_m\rvert$ en $m\omega_0$, simétrico respecto de $0$ (incluido $\lvert C_0\rvert$).

### 1.2 Receta del ítem a: completar y desarrollar

1. **Traducí el pedido a una paridad** (cosenos/reales ⇒ par; senos/imaginarios ⇒ impar) y escribí por qué: $C_m = \frac12(a_m - j\,b_m)$.
2. **Graficá** el dato y completalo: par = espejo vertical; impar = espejo por el origen. Repetí con período $T$. Una impar con salto en $0$ no tiene por qué pasar por el origen.
3. **Escribí $f$ por tramos** en $(-L, L)$, más "$f(t) = f(t+T)$", y anotá $T$, $L$, $\omega_0$. El profe lo exige siempre: ya suma.
4. **Anulá con una línea de justificación:** "$b_m = 0$ por ser par" o "$a_0 = a_m = 0$ por ser impar".
5. Si es par, **$a_0/2$ del gráfico** (altura promedio).
6. **Calculá el coeficiente que queda** con $\frac{2}{L}\int_0^L$ sobre el dato: si $f$ es $\pi - t$ o $x+1$, separá en dos integrales (la de la constante da $0$ por $\operatorname{sen}(m\pi) = 0$); la otra, por tabla. Evaluá con $(-1)^m$.
7. **Separá $m$ par / impar** si aparece $(-1)^m - 1$ y escribí la serie con $2k+1$. Si los dos casos son distintos de cero (ej. $1 - 2(-1)^m$), dejala en $m$.
8. Si piden la SEF: $C_0$ y $C_m$ con la fórmula de §1.1, sin integrar nada.

### 1.3 Ítem b: la función ya es suma de senos y cosenos

No se integra: con una identidad la escribís como suma de armónicas y **esa es la serie** (la serie es única). $2\operatorname{sen}x\cos x = \operatorname{sen}2x$ (un solo término, $b_2 = 1$); $\cos^2 x = \frac12 + \frac12\cos 2x$ (dos términos); $\operatorname{sen}^2 x = \frac12 - \frac12\cos 2x$. Si no te acordás de la identidad: Euler, multiplicar y reagrupar.

### 1.4 Ítem c: paridad + simetría de media onda (solo gráfico y tramos)

1. **Primera condición, la paridad:** espejá el dato ($\ell$ de largo). Ahora tenés $2\ell$: eso es medio período, $T = 4\ell$.
2. **Segunda condición, la media onda:** ese pedazo de $(-\ell, \ell)$ lo corrés $2\ell$ y lo das vuelta. Por tramos, para $t \in (\ell, 2\ell)$: $f(t) = -f(t - 2\ell)$; para $t \in (-2\ell, -\ell)$: $f(t) = -f(t + 2\ell)$. El $t - 2\ell$ cae en $(-\ell, 0)$: usá la fórmula de **ese** tramo, no la del dato.
3. Escribí los **cuatro tramos** en $(-2\ell, 2\ell)$ con $f(t) = f(t + 4\ell)$ y anotá "par/impar" y "S.M.O.". Chequeo visual: la joroba corrida medio período tiene que ser la misma dada vuelta.

Cuándo una función **no** tiene media onda: si nunca cambia de signo, si el valor medio no es $0$ o si tiene alguna armónica par distinta de cero.

### 1.5 V/F: las siete ideas

1. Par ⇒ solo cosenos (+ $a_0/2$) y $C_m$ reales. 2. Impar ⇒ solo senos, $a_0 = 0$, $C_m$ imaginarios puros. 3. Impar + constante ⇒ solo senos pero $a_0/2 \neq 0$. 4. Media onda ⇒ solo armónicas impares y valor medio $0$ (una función par puede tener media onda: $\lvert t\rvert - 3$ en $(-6,6)$). 5. $a_0/2 = C_0$ = valor medio. 6. En un salto la serie converge al **promedio** de los dos valores ⇒ dos funciones que difieren en puntos aislados tienen la **misma serie** ("misma serie ⇒ misma función" es **falso**). 7. La serie es única.

---

## 2 · Laplace (Ej2)

### 2.1 Lo que no está en el ayudamemoria

- **Euler:** $\operatorname{sen}x = \dfrac{e^{jx} - e^{-jx}}{2j}$, $\cos x = \dfrac{e^{jx} + e^{-jx}}{2}$. Binomio al cubo $1\ 3\ 3\ 1$ (signos alternados si es resta); $(2j)^3 = -8j$.
- **Producto → suma:** $\operatorname{sen}A\operatorname{sen}B = \tfrac12[\cos(A-B) - \cos(A+B)]$, $\cos A\cos B = \tfrac12[\cos(A-B) + \cos(A+B)]$, $\operatorname{sen}A\cos B = \tfrac12[\operatorname{sen}(A+B) + \operatorname{sen}(A-B)]$.
- Derivada del cociente $\left(\frac ND\right)' = \frac{N'D - ND'}{D^2}$; L'Hôpital; $\ln a - \ln b = \ln\frac ab$, $\ln 1 = 0$; $\operatorname{arctg}0 = 0$, $\operatorname{arctg}\sqrt3 = \frac\pi3$, $\operatorname{arctg}u \to \frac\pi2$.
- **Completar cuadrados:** $s^2 + bs + c = \left(s + \frac b2\right)^2 + \left(c - \frac{b^2}{4}\right)$.
- **Las dos fórmulas armadas** con la 1ª traslación (toda $s$ pasa a $s - \alpha$, también la del numerador):

$$
\mathcal{L}^{-1}\left[\frac{s-\alpha}{(s-\alpha)^2+\beta^2}\right] = e^{\alpha t}\cos\beta t
$$

$$
\mathcal{L}^{-1}\left[\frac{\beta}{(s-\alpha)^2+\beta^2}\right] = e^{\alpha t}\operatorname{sen}\beta t
$$

- Con denominador $s^2 + a^2$: **$s$ arriba es coseno, constante arriba es seno.** Si falta la constante, multiplicá y dividí por ella.
- Resultado que salió dos veces en 2025: $\mathcal{L}[t\cos t] = \dfrac{s^2 - 1}{(s^2+1)^2}$; y $\mathcal{L}[t\operatorname{sen}(at)] = \dfrac{2as}{(s^2+a^2)^2}$.

### 2.2 Integral impropia = transformada evaluada (y multiplicación por $t$)

1. Separá la exponencial $e^{-kt}$: es el $e^{-st}$ de la definición, así que **evaluás en $s = k$**. Sin exponencial, $s = 0$. Lo que queda es $f(t)$. Escribí: "la integral es $\mathcal{L}[f(t)]$ en $s = k$".
2. Calculá $F(s)$ **genérica**. Si $f$ trae una $t$ multiplicando: tabla del resto, **derivá respecto de $s$ y cambiá el signo una vez** ($t^2$: dos veces, el signo no cambia). Si además hay $e^{at}$ multiplicando dentro de $f$: primero la $t$, después la traslación.
3. **Recién al final** reemplazá $s = k$. Si reemplazás antes de derivar, derivás una constante y da $0$.

### 2.3 División por $t$

1. Con dos exponenciales sobre $t$, sacá factor común la de **menor** exponente: $e^{-kt}\cdot\dfrac{1 - e^{-mt}}{t}$. Evaluás en $s = k$. No separes en dos integrales con $1/t$: $\lim 1/t$ no existe y no llegás a nada.
2. **Escribí el chequeo** $\lim_{t\to0} f(t)/t$ (L'Hôpital; para $\frac{\operatorname{sen}t}{t}$ da $1$). Es parte del puntaje.
3. Transformá el numerador, cambiá $s$ por $u$ e integrá de $s$ a $\infty$ (salen logaritmos o arcotangente).
4. Si queda $\infty - \infty$ con logaritmos, **juntalos en uno**: $\ln\frac{u}{u+m} \to \ln 1 = 0$.
5. Evaluá en $s = k$. Con $\frac{e^{-at} - e^{-bt}}{t}$ el resultado es $\ln\frac ba$. Si la integral va de $-\infty$ a $\infty$ y $f/t$ es par, es el doble.

### 2.4 Potencias y productos de seno/coseno: Euler

1. Reemplazá cada seno/coseno por Euler. 2. Desarrollá (binomio para el cubo, distributiva para el producto) y sumá exponentes. 3. Reagrupá las parejas $e^{jkt}$ con $e^{-jkt}$ en $\cos kt$ o $\operatorname{sen}kt$, convirtiendo la constante: $\frac{1}{4j} = \frac12\cdot\frac{1}{2j}$, $-\frac{1}{8j} = -\frac14\cdot\frac{1}{2j}$, $\frac18 = \frac14\cdot\frac12$. 4. Tabla y linealidad. Dejalo como suma de fracciones, sin denominador común.

### 2.5 Transformar una integral de convolución

Lo que depende solo de $u$ es $f(u)$; lo que tiene $t - u$ es $g(t-u)$. Transformá cada una **como si fueran de $t$** (el corrimiento no importa); si $f(u)$ trae una $u$ multiplicando, es §2.2. El resultado es $F(s)\cdot G(s)$, simplificado. En una ecuación integral ($y - \int_0^t y(u)\operatorname{sen}(t-u)\,du = t^4$): transformar miembro a miembro, la integral es $Y\cdot\frac{1}{s^2+1}$, despejar $Y$, antitransformar.

### 2.6 Fracciones simples (la herramienta de todo el Ej3)

0. Si grado del numerador $\ge$ grado del denominador, dividí primero.
1. **Factorizá el denominador** (factor común $s$, resolvente, Ruffini) y **sacá afuera el coeficiente principal**: $2s^2 + 7s + 3 = 2(s+3)(s+\frac12)$; si no, los coeficientes no dan.
2. **Planteá** según las raíces: real simple $p$ → $\dfrac{A}{s-p}$; real doble → $\dfrac{A}{(s-p)^2} + \dfrac{B}{s-p}$; cuadrático con $b^2 - 4ac < 0$ → $\dfrac{Bs + C}{s^2 + bs + c}$ (**dos incógnitas arriba**). Complejas múltiples no se toman: van por convolución.
3. **Tapado:** para cada raíz real simple, y para la potencia más alta de la doble, tapá ese factor en la $F(s)$ original y evaluá el resto en la raíz. Funciona porque al multiplicar por el factor y evaluar en la raíz, los otros términos mueren.
4. **Lo que falte** ($B$ de la doble, $Bs + C$ del cuadrático): denominador común, igualá numeradores y **compará coeficientes** (los de $s^2$ y el independiente suelen alcanzar; usá otro de control).
5. **Antitransformá:** $\frac{A}{s-p} \to Ae^{pt}$; $\frac{A}{(s-p)^2} \to Ate^{pt}$; el cuadrático: completar cuadrado y **prestar** para que arriba aparezca exactamente $(s + a)$: $Bs + C = B(s+a) + (C - Ba)$; después las dos fórmulas de §2.1. Si $b \neq 1$, el seno necesita $b$ arriba: $\frac{1}{(s+a)^2 + 9} = \frac13\cdot\frac{3}{(s+a)^2+9}$.

### 2.7 Antitransformar por convolución ($\frac{1}{(s^2+1)^2}$, $\frac{s^2}{(s^2+1)^2}$)

1. **Partí** $Y(s)$ en dos factores de tabla, siguiendo el denominador; $f(t)$ y $g(t)$.
2. Armá $\int_0^t f(u)\,g(t-u)\,du$. Si hay una exponencial, **dale el $t - u$ a la exponencial**: $e^{-(t-u)} = e^{-t}e^{u}$ y el $e^{-t}$ sale de la integral.
3. Producto de senos/cosenos → suma (§2.1) con $A = u$, $B = t - u$: queda $\cos(2u - t)$ y $\cos t$. **$\cos t$ es constante respecto de $u$**: su primitiva es $u\cos t$. La de $\cos(2u-t)$ es $\frac{\operatorname{sen}(2u-t)}{2}$.
4. Barrow en $u = t$ y $u = 0$; $\operatorname{sen}(-t) = -\operatorname{sen}t$, $\cos(-t) = \cos t$. Con exponencial por seno, primitiva de la tabla de integrales.

### 2.8 Demostración de $\mathcal{L}[a^t]$ (dos renglones)

$a^t = e^{\ln a^t} = e^{t\ln a}$; por tabla con $c = \ln a$: $\mathcal{L}[a^t] = \dfrac{1}{s - \ln a}$. Si además hay $e^{-4t}$: 1ª traslación, $\frac{1}{s + 4 - \ln a}$ (**no** es un producto de transformadas).

---

## 4 · Transformada Z (Ej4)

### 4.1 Lo que no está en el ayudamemoria

- **Serie geométrica:** $\displaystyle\sum_{k=0}^{\infty} r^k = \frac{1}{1-r}$ **solo si** $\lvert r\rvert < 1$. Receta universal: escribir la definición, juntar todo lo que depende de $n$ como "algo elevado a la $n$" (esa es la razón), sumar, imponer $\lvert r\rvert < 1$.
- **ROC:** cada geométrica exige $\lvert r\rvert < 1$ ⇒ $\lvert z\rvert > R_i$; la ROC de la suma es la **intersección** = $\lvert z\rvert > \max R_i$ (exterior de la circunferencia más grande, borde punteado). $\lvert a/z\rvert < 1 \Leftrightarrow \lvert z\rvert > \lvert a\rvert$, nunca al revés. Al invertir se da vuelta la desigualdad: $\left|\frac{1}{16z^2}\right| < 1 \Rightarrow \lvert z\rvert^2 > \frac1{16} \Rightarrow \lvert z\rvert > \frac14$.
- Pares e impares: $n = 2k$ y $n = 2k+1$ (múltiplo de 3: $3k, 3k+1, 3k+2$; de 5: cinco sumatorias). Potencias: $b^{2k} = (b^2)^k$, $b^{2k+1} = b\cdot(b^2)^k$, $(-2)^{2k} = 4^k$ (el signo desaparece en los pares), $(-2)^{2k+1} = -2\cdot 4^k$.
- $\mathcal{Z}\left[\dfrac{a^n}{n!}\right] = e^{a/z}$ (serie de $e^x$). No está en la tabla.
- $\displaystyle\sum_{n=0}^{\infty} x(n)\,c^{-n} = X(z)\Big|_{z=c}$.
- **Dejar una $z$ afuera** antes de fracciones simples; fracciones simples con raíz doble; **verificación** con la recurrencia.
- Leer la tabla al revés: $\dfrac{z}{(z-a)^2}$ **no** es $n\,a^n$, le falta la $a$ arriba: $\dfrac{4z}{(z-2)^2} = 2\cdot\dfrac{2z}{(z-2)^2} \to 2\,n\,2^n$; $\dfrac{6z}{(z-3)^2} \to 2\,n\,3^n$.
- Control: $x(0) = \lim_{z\to\infty} X(z)$ (TVI, está en el ayudamemoria).

### 4.2 Sucesión por paridad + ROC

1. **Escribí los primeros términos** de $\sum x(n)z^{-n}$ ($n = 0$ es par) para no equivocarte de rama.
2. **Separá** en pares ($n = 2k$) e impares ($n = 2k+1$).
3. En cada una, **todo a "algo elevado a la $k$"**. En los impares sobra el "+1" del exponente: sale **afuera** como constante, ej. $4^{-(2k+1)}z^{-(2k+1)} = \frac{1}{4z}\left(\frac{1}{16z^2}\right)^k$, $5\cdot2^{2k+1}z^{-(2k+1)} = \frac{10}{z}\left(\frac{4}{z^2}\right)^k$.
4. **Sumá** cada una con $\frac{1}{1-r}$ y multiplicá arriba y abajo por $z^2$; en los impares siempre se simplifica una $z$.
5. **ROC:** $\lvert r\rvert < 1$ en cada sumatoria; intersección. **Si solo piden la ROC o es V/F, cortás en el paso 3**: las constantes de afuera no influyen.

Ojo con $4^{-n}$ vs $4^n$: razón $\frac{1}{16z^2}$ (radio $\frac14$) contra $\frac{16}{z^2}$ (radio $4$); cambia quién manda.

### 4.3 Suma de una serie numérica mediante Z

1. $c$ = lo elevado a la $-n$ ($(\tfrac12)^n$ es $2^{-n}$, $c = 2$; $3^{-n}$ es $z = 3$, no $\frac13$). 2. Lo que queda es $x(n)$: buscá $X(z)$ en la tabla ($n \to \frac{z}{(z-1)^2}$, $n^2 \to \frac{z(z+1)}{(z-1)^3}$, $\cos(an)$ con $a$ = solo el número que multiplica a $n$, $\cos(\pi n) = (-1)^n$) o $e^{a/z}$ si es $\frac{a^n}{n!}$. 3. Reemplazá $z = c$; control: $c$ tiene que estar en la ROC ($\lvert c\rvert > R$).

### 4.4 Secuencia finita

Tabla de valores empezando por $n = 0$ (en un gráfico de bastones, leer cada $x(n)$); definición término a término: $X(z) = x(0) + \frac{x(1)}{z} + \frac{x(2)}{z^2} + \dots$; denominador común optativo. Sin geométrica ni ROC. El de $n = 0$ va con $z^0 = 1$: no corras los valores.

### 4.5 Antitransformar: "dejar una $z$ afuera"

1. $X(z) = z\cdot\left[\dfrac{X(z)}{z}\right]$ (de $2z^2$ sacás **una** $z$). Por qué: todas las filas de la tabla tienen una $z$ en el numerador; sin sacarla quedan $\frac{A}{z-a}$ que no están en la tabla.
2. Fracciones simples de lo de adentro: polos simples por tapado; raíz doble $\frac{A}{(z-a)^2} + \frac{B}{z-a}$ ($A$ tapado, $B$ comparando el coeficiente de $z^2$; plantealo aunque después dé $0$).
3. Distribuí la $z$: $\frac{z}{z-a} \to a^n$, $\frac{z}{z-1} \to 1$, $\frac{z}{(z-1)^2} \to n$, $\frac{az}{(z-a)^2} \to n\,a^n$ (ajustando la constante, §4.1).

### 4.6 Ecuación en diferencias de 1er orden (con verificación)

1. Ordená $x(n+1) + c\,x(n) = g(n)$ y **distribuí** $g(n)$ en cosas de tabla: $4(1-n)2^n = 4\cdot2^n - 4\,n\,2^n$; una constante $k$ es $k\cdot u(n) \to \frac{kz}{z-1}$; $3n \to \frac{3z}{(z-1)^2}$.
2. Transformá miembro a miembro: $x(n+1) \to zX - z\,x(0)$ (**con la $z$** multiplicando a $x(0)$), $x(n) \to X$.
3. Reemplazá $x(0)$, agrupá $X(z)(z + c) = \dots$ y pasá $(z+c)$ dividiendo. Juntá el segundo miembro en un solo cociente.
4. Una $z$ afuera, fracciones simples, distribuir, tabla (§4.5).
5. **Verificá:** $x(1)$, $x(2)$ con la recurrencia desde $x(0)$ (despejando $x(n+1)$) y con tu fórmula. Si no coinciden, hay un error: buscalo antes de entregar.

### 4.7 Ecuación en diferencias de 2º orden (raíz doble)

Igual que §4.6 con $\mathcal{Z}[x(n+2)] = z^2X - z^2x(0) - z\,x(1)$ ($x(0)$ va con $z^2$, $x(1)$ con $z$) y dos datos. Signos al pasar $-4(zX - z\,x(0))$: queda $+4z\,x(0)$. $X(z)$ queda multiplicada por el polinomio característico de grado 2: factorizalo; si es un cuadrado perfecto hay **raíz doble** y aparece $n\,a^n$. Juntá todo el segundo miembro en un solo cociente antes de dividir, sacá la $z$, planteá $\frac{A}{z-b} + \frac{B}{(z-a)^2} + \frac{C}{z-a}$ ($A$ y $B$ por tapado, $C$ por el coeficiente de $z^2$). Verificá con $x(0)$, $x(1)$ y $x(2)$.

---

## 5 · Resultados de referencia (mirar solo después de hacer el ejercicio)

| Ejercicio | Resultado |
|---|---|
| **R-A a)** $\pi - t$ en $(0,\pi)$, solo cosenos (= 2025-1C T1 Ej1a) | $\frac{a_0}{2} = \frac\pi2$, $a_m = \frac{4}{\pi m^2}$ ($m$ impar), $S = \frac\pi2 + \frac4\pi\sum_{k\ge0}\frac{\cos((2k+1)t)}{(2k+1)^2}$ |
| **R-A b)** ídem solo senos + SEF (= 2025-1C T2 Ej1a) | $b_m = \frac2m$, $S = 2\sum\frac{\operatorname{sen}(mt)}{m}$; $C_0 = 0$, $C_m = -\frac jm$ |
| $f(t) = t$ en $(0,\pi)$, SEF imaginarios puros (2024-2C T1 Ej2) | $b_m = -\frac{2(-1)^m}{m}$; $C_m = \frac{(-1)^m}{m}\,j$, $m \neq 0$ |
| 2025-1C T1 Ej1c: $t$ en $(0,1)$, imaginarios + SMO | $T=4$: $-t-2$ en $(-2,-1)$, $t$ en $(-1,1)$, $-t+2$ en $(1,2)$ |
| 2025-1C T2 Ej1c: $t$ en $(0,1)$, reales + SMO | $T=4$: $-t-2$, $-t$, $t$, $t-2$ en $(-2,-1)$, $(-1,0)$, $(0,1)$, $(1,2)$ |
| **R-B** V/F | a) **F** (par con SMO: solo armónicas **impares**); b) **V**; g) **F** |
| **R-C** $\mathcal{L}[\cos^3 t]$ (= 2024-2C rec Ej3a) | $\frac14\cos3t + \frac34\cos t \to \frac14\frac{s}{s^2+9} + \frac34\frac{s}{s^2+1}$ |
| $\mathcal{L}[\operatorname{sen}^3 t]$ (2025-1C T2 Ej2a) | $-\frac14\operatorname{sen}3t + \frac34\operatorname{sen}t \to -\frac14\frac{3}{s^2+9} + \frac34\frac{1}{s^2+1}$ |
| **R-D** $\mathcal{L}^{-1}\left[\frac{1}{(s^2+1)^2}\right]$ (= 2025-1C T1 Ej2b) | $y = \frac{\operatorname{sen}t}{2} - \frac{t\cos t}{2}$ |
| $\mathcal{L}^{-1}\left[\frac{s^2}{(s^2+1)^2}\right]$ (2025-1C T2 Ej2b) | $y = \frac12 t\cos t + \frac12\operatorname{sen}t$ |
| $\int_0^\infty t\,e^{-5t}\cos t\,dt$ (2025-1C T1 Ej2a) | $\frac{24}{676} = \frac{6}{169}$ |
| $\int_0^\infty \frac{e^{-5t} - e^{-10t}}{t}\,dt$ (2025-1C rec Ej2a) | $\ln 2$ (y $\frac{e^{-3t} - e^{-6t}}{t}$: también $\ln 2$) |
| $\int_0^\infty \frac{\operatorname{sen}t}{t}\,dt$ (2024-2C T1 Ej3b) | $\frac\pi2$ (de $-\infty$ a $\infty$: $\pi$); con $e^{-\sqrt3 t}$: $\frac\pi6$ |
| $y - \int_0^t y(u)\operatorname{sen}(t-u)\,du = t^4$ (2022-10-11 Ej2) | $y = t^4 + \frac{t^6}{30}$ |
| 2022-10-11 Ej5: $\frac{17(s^2+s-k)}{(s-2)(s^2+8s+17)}$ | $k = 6$; escalón: $y = 3 - 3\cos(t)e^{-4t} + 5\operatorname{sen}(t)e^{-4t}$, V.E. $3$ |
| 2024-2C T2 Ej4 (= 2024-1C T2): $\frac{5(s^2-ks-2)}{(s^2+s-6)(s^2+2s+2)}$ | $k = 1$, $G = \frac{5(s+1)}{(s+3)(s^2+2s+2)}$; impulso: $-2e^{-3t} + 2\cos(t)e^{-t} + \operatorname{sen}(t)e^{-t}$; $e^{-t}$: $e^{-3t} - \cos(t)e^{-t} + 2\operatorname{sen}(t)e^{-t}$ |
| 2024-2C rec Ej4a: $\frac{34(s^3-3s^2-as)}{(s-5)(s+b)(s^2+8s+17)}$ | $a = 10$, $b \ge 0$ |
| 2025-1C T1 Ej4a: $(-2)^n$ par / $4^{-n}$ impar | $X = \frac{z^2}{z^2-4} + \frac{4z}{16z^2-1}$, ROC $\lvert z\rvert > 2$ (rec Ej4a V/F: **V**) |
| **R-H** múltiplos de 5 ($3$) / $(-2)^n$: ROC $\lvert z\rvert > 2$ | **V** (razones $\frac{1}{z^5}$ y $\frac{-32}{z^5}$) |
| Sumas por Z | $\sum n\,2^{-n} = 2$; $\sum n^2 4^{-n} = \frac{20}{27}$; $\sum\frac{3^n}{n!}2^{-n} = e^{3/2}$; $\sum\cos(\pi n)3^{-n} = \frac34$ |
| Secuencia $(0,1,3,2,1)$ (2025-1C rec Ej4b) | $\frac1z + \frac{3}{z^2} + \frac{2}{z^3} + \frac{1}{z^4}$ |
| $x(n+1) - 4x(n) = 4(1-n)2^n$, $x(0) = 3$ (2025-1C T2 Ej4b) | $x(n) = 2\,n\,2^n + 3\cdot4^n$; $x(2) = 64$ |
| **R-I** $x(n+2) - 6x(n+1) + 9x(n) = 5\cdot2^n$, $x(0)=5$, $x(1)=13$ | $X = 5\frac{z}{z-2} + 3\frac{z}{(z-3)^2}$; $x(n) = 5\cdot2^n + n\,3^n$; $x(2) = 38$ |

*Generado el 2026-10-05 desde `guia/01-fourier-desde-cero.md`, `guia/02-laplace-desde-cero.md`, `guia/03-sistemas-desde-cero.md`, `guia/04-z-desde-cero.md` (secciones "qué tenés que saber de memoria", recetas y checkpoints), `estrategia.md` §6 (checklist teórico), `repaso/practica-repaso-2026.md` (R-A…R-I) y `examenes/INDICE.md` (reciclados). Complemento de `fuentes/AYUDAMEMORIA-OFICIAL.pdf` págs. 1–3, que es lo único permitido en el parcial junto con la tabla de integrales. Iterar sobre este .md; exportar con `/machete --pdf`.*
