# Práctica — ejercicios de la clase de repaso 2026

> **Fuente:** fotos de la clase de repaso del 1P de tu curso (2026), en `../fuentes/clases/repaso-clase-2026/pag-01…07.jpeg`. Los números entre paréntesis son los de la **guía de la cátedra** (los mismos que usan los OneNote).
> **Cómo usarla:** cada ejercicio en su página, con espacio para resolver en papel o en GoodNotes. Hacelo **sin mirar**, con reloj (el tiempo sugerido está en cada uno) y recién después abrí la corrección.
> **Verificación:** todas las cuentas de las fotos se rehicieron con cálculo simbólico (sympy). Los resultados finales de la hoja están bien; hay **dos errores de escritura intermedios** que no cambian el resultado, marcados con ⚠ en la corrección.
> **Día del plan:** cada ejercicio dice en qué bloque de `plan.md` va y qué ejercicio de parcial real es su "gemelo".

---

## A) Fourier: completar y desarrollar (guía 4e) · viernes · 30 min

Dada $f(t) = \pi - t$ si $0 < t < \pi$:

**a)** Completala en todo el eje real para que la serie trigonométrica de Fourier tenga **solo cosenos** (la SEF queda con coeficientes reales). Graficá y desarrollá la STF.

**b)** Completala para que la STF tenga **solo senos** (la SEF queda con coeficientes imaginarios puros). Graficá, desarrollá la STF y pasala a SEF.

*Gemelos en parciales reales:* **2025-1C T1 Ej1a** (es el mismo ítem a) y **2025-1C T2 Ej1a** (el b) da la misma función).

<div style="height: 3cm"></div>

<details>
<summary><strong>Corrección A</strong></summary>

**a) Paso 1 — completar como par.** Solo cosenos ⇔ $b_m = 0$ ⇔ $f$ par:

$$
f(t)=\begin{cases}\pi+t & -\pi<t<0\\ \pi-t & 0<t<\pi\end{cases},\qquad f(t)=f(t+2\pi)
$$

con $T=2\pi$, $L=\pi$, $\omega_0=1$.

Es un triángulo con pico $\pi$ en $t=0$.

**Paso 2 — valor medio.** Se lee del gráfico (área del triángulo sobre el período):

$$
\frac{a_0}{2}=\frac{\pi}{2}
$$

**Paso 3 — $a_m$.** Por paridad, $\frac{2}{L}\int_0^L$:

$$
a_m=\frac{2}{\pi}\int_0^{\pi}(\pi-t)\cos(mt)\,dt=\frac{2}{\pi}\cdot\frac{1-(-1)^m}{m^2}
=\begin{cases}\dfrac{4}{\pi m^2} & m\ \text{impar}\\[2mm] 0 & m\ \text{par}\end{cases}
$$

(la parte $\pi\int\cos(mt)$ da $0$ porque $\operatorname{sen}(m\pi)=0$; la parte $\int t\cos(mt)$ va por partes o por tabla).

**Paso 4 — serie con armónicas impares** ($m=2k+1$):

$$
S(t)=\frac{\pi}{2}+\frac{4}{\pi}\sum_{k=0}^{\infty}\frac{\cos\big((2k+1)t\big)}{(2k+1)^2}
$$

**b) Paso 1 — completar como impar.** Solo senos ⇔ $a_0=a_m=0$ ⇔ $f$ impar:

$$
f(t)=\begin{cases}-\pi-t & -\pi<t<0\\ \pi-t & 0<t<\pi\end{cases},\qquad f(t)=f(t+2\pi)
$$

Es un diente de sierra: en todo $(0,2\pi)$ vale $\pi-t$.

**Paso 2 — $b_m$:**

$$
b_m=\frac{2}{\pi}\int_0^{\pi}(\pi-t)\operatorname{sen}(mt)\,dt=\frac{2}{m}
\qquad\Longrightarrow\qquad
S(t)=2\sum_{m=1}^{\infty}\frac{\operatorname{sen}(mt)}{m}
$$

> ⚠ **En la hoja** el planteo dice $\frac{1}{\pi}\cdot 2\int_0^{2\pi}$. Con límites $0$ a $2\pi$ ese $2$ sobra: daría $4/m$. Lo correcto es $\frac{2}{\pi}\int_0^{\pi}$ o $\frac{1}{\pi}\int_0^{2\pi}$. El resultado $2/m$ que anotaron está bien.

**Paso 3 — pasar a SEF** con $C_m=\tfrac12(a_m-j\,b_m)$:

$$
C_0=0,\qquad C_m=-\frac{j}{m},\qquad C_{-m}=\frac{j}{m}
\qquad\Longrightarrow\qquad
S(t)=\sum_{\substack{m=-\infty\\ m\neq0}}^{\infty}\left(-\frac{j}{m}\right)e^{jmt}
$$

**Criterio:** decidir la paridad por lo que piden (1), gráfico con $T$, $L$, $\omega_0$ (1), coeficientes y serie (1 por ítem).

</details>

<div style="break-before: page"></div>

## B) Fourier: verdadero o falso conceptual (guía 14 a, b, g) · sábado mañana · 15 min

Justificá cada uno.

**a)** $f(t)=|t|-3$ si $t\in(-6,6)$, $f(t)=f(t+12)$. La STF de $f$ tiene solo cosenos de armónicas **pares**. «≈ la consigna exacta no se ve completa en la foto»

**b)** Para la misma $f$, los coeficientes $C_n$ de su SEF son reales.

**g)** Si $f(t)$ y $g(t)$ son dos funciones periódicas definidas en $\mathbb{R}$ y sus series de Fourier son iguales, entonces $f(t)=g(t)$ para todo $t\in\mathbb{R}$.

*Gemelos:* el ítem b) de **2025-1C Ej1** (justificar la STF de $2\operatorname{sen}x\cos x$) y los V/F de **2025-1C rec Ej4a**: la cátedra 2025–2026 mete ítems conceptuales cortos.

<div style="height: 10cm"></div>

<details>
<summary><strong>Corrección B</strong></summary>

**a) FALSO.** $f$ es par (solo cosenos y valor medio $0$), pero además tiene **simetría de media onda**: para $0<t<6$, $f(t)=t-3$ y $f(t-6)=|t-6|-3=3-t=-f(t)$. Con SMO sobreviven **solo las armónicas impares**. Tiene solo cosenos, pero de armónicas impares.

**b) VERDADERO.** $f$ es par ⇒ $b_n=0$ ⇒ $C_n=\tfrac12 a_n\in\mathbb{R}$.

**g) FALSO.** Dos funciones que difieren en los puntos de discontinuidad (o en un número finito de puntos de cada período) tienen los mismos coeficientes, porque las integrales no cambian. La serie converge al promedio de los límites laterales en cada salto, así que no puede coincidir con las dos.

</details>

<div style="break-before: page"></div>

## C) Laplace: transformada de $\cos^3 t$ (guía 3d) · sábado noche · 15 min

Hallá $\mathcal{L}\big[\cos^3(t)\big]$, $t>0$. *(En la foto el profe lo marcó "Practicar".)*

*Gemelos:* **2024-2C rec Ej3a** (el mismo) y **2025-1C T2 Ej2a** ($\operatorname{sen}^3 t$).

<div style="height: 10cm"></div>

<details>
<summary><strong>Corrección C</strong></summary>

**Paso 1 — Euler.** $\cos t=\dfrac{e^{jt}+e^{-jt}}{2}$, y se eleva al cubo con el binomio:

$$
\cos^3 t=\frac18\left(e^{3jt}+3e^{jt}+3e^{-jt}+e^{-3jt}\right)
=\frac14\cdot\frac{e^{3jt}+e^{-3jt}}{2}+\frac34\cdot\frac{e^{jt}+e^{-jt}}{2}
=\frac14\cos(3t)+\frac34\cos(t)
$$

> ⚠ **En la hoja** esa línea quedó escrita como $\frac14\operatorname{sen}(3t)+\frac34\cos(3t)$. Es un error de copia: lo correcto es $\frac14\cos(3t)+\frac34\cos(t)$, y la $F(s)$ final que escribieron corresponde a esto.

**Paso 2 — tabla** (está en el ayudamemoria):

$$
F(s)=\frac14\cdot\frac{s}{s^2+9}+\frac34\cdot\frac{s}{s^2+1}
$$

</details>

<div style="break-before: page"></div>

## D) Laplace: antitransformar por convolución (guía 1b) · sábado noche · 20 min

Hallá $y(t)$ si $Y(s)=\dfrac{1}{(s^2+1)^2}$, usando el teorema de convolución.

*Gemelos:* **2025-1C T1 Ej2b** y **2024-2C rec Ej3b** (los dos, el mismo); **2025-1C T2 Ej2b** ($s^2/(s^2+1)^2$).

<div style="height: 12cm"></div>

<details>
<summary><strong>Corrección D</strong></summary>

**Paso 1 — partir en producto.** $F(s)=G(s)=\dfrac{1}{s^2+1}$ ⇒ $f(t)=g(t)=\operatorname{sen}t$.

**Paso 2 — convolución:**

$$
y(t)=\int_0^t\operatorname{sen}(u)\,\operatorname{sen}(t-u)\,du
=\frac12\int_0^t\big[\cos(2u-t)-\cos t\big]\,du
$$

**Paso 3 — integrar** (con $\cos t$ constante respecto de $u$):

$$
y(t)=\frac12\left[\frac{\operatorname{sen}(2u-t)}{2}-u\cos t\right]_0^t
=\frac12\left(\frac{\operatorname{sen}t-\operatorname{sen}(-t)}{2}-t\cos t\right)
$$

$$
\boxed{\,y(t)=\frac{\operatorname{sen}t}{2}-\frac{t\cos t}{2}\,}
$$

</details>

<div style="break-before: page"></div>

## E) Sistemas: circuito RLC con entrada impulso (guía 18) · domingo noche · 25 min

En un circuito RLC en paralelo,

$$
i(t)=\frac{v(t)}{R}+\frac1L\int_0^t v(u)\,du+C\,\frac{dv(t)}{dt}
$$

con $R=6$, $L=5$, $C=\frac1{30}$ y $v(0)=0$.

Hallá $v(t)$ si la entrada es un impulso, $i(t)=\delta(t)$. Indicá si el sistema es estable y el tipo de respuesta.

*Gemelo:* **2025-1C T1 Ej3** (sistema mecánico masa-resorte-amortiguador: obtener $G(s)$ desde la ecuación y la respuesta). El profe de la grabación dijo que este tipo es "de parcial o de final".

<div style="height: 14cm"></div>

<details>
<summary><strong>Corrección E</strong></summary>

**Paso 1 — Laplace miembro a miembro.** $\mathcal L[\delta]=1$, $\mathcal L\!\left[\int_0^t v\right]=\dfrac{V(s)}{s}$ y $\mathcal L[v']=sV(s)-v(0)$, con $v(0)=0$:

$$
1=\frac{V(s)}{6}+\frac{V(s)}{5s}+\frac{s\,V(s)}{30}
=V(s)\cdot\frac{s^2+5s+6}{30s}
$$

**Paso 2 — despejar y factorizar:**

$$
V(s)=\frac{30s}{(s+2)(s+3)}=\frac{A}{s+2}+\frac{B}{s+3},
\qquad A=\frac{30(-2)}{1}=-60,\quad B=\frac{30(-3)}{-1}=90
$$

**Paso 3 — antitransformar:**

$$
\boxed{\,v(t)=-60\,e^{-2t}+90\,e^{-3t}\,}
$$

**Clasificación:** polos reales negativos ($-2$, $-3$) ⇒ **estable**, respuesta **exponencial decreciente** (tiende a $0$).

</details>

<div style="break-before: page"></div>

## F) Sistemas: hallar K, polos, ceros y corte (ejercicio de parcial) · domingo mañana · 25 min

$$
G(s)=\frac{25\,(s^2-Ks+12)}{(s^2+4s+5)(s^2-3s)}
$$

**a)** Hallá $K\in\mathbb R$ sabiendo que el sistema es estable. Indicá polos y ceros y graficá aproximadamente el corte de $|G(s)|$ por el eje real.

**b)** *(extra, del parcial original)* Hallá la respuesta del sistema a una entrada impulso unitario.

*Gemelo:* es **textual el 2015-05-29 T2 Ej3**: once años después lo volvieron a dar en el repaso. El b) está resuelto en `examenes/resueltos/2015-05-29_Parcial-T2_resuelto.pdf`.

<div style="height: 14cm"></div>

<details>
<summary><strong>Corrección F</strong></summary>

**a) Paso 1 — factorizar el denominador:**

$$
G(s)=\frac{25\,(s^2-Ks+12)}{\big((s+2)^2+1\big)\,s\,(s-3)}
$$

El polo $s=3$ es inestable (parte real positiva).

**Paso 2 — K que lo cancela.** El numerador tiene que anularse en $s=3$:

$$
9-3K+12=0\quad\Longrightarrow\quad \boxed{K=7}
$$

**Paso 3 — simplificar.** $s^2-7s+12=(s-3)(s-4)$:

$$
G(s)=\frac{25\,(s-4)}{s\,\big((s+2)^2+1\big)}
$$

- **Ceros:** $4$ (y $\infty$).
- **Polos:** $0$, $-2+j$, $-2-j$.
- Polo nulo simple ⇒ **marginalmente estable**, que la cátedra cuenta como estable.

**Paso 4 — corte por el eje real** ($s=\sigma$): asíntota vertical en $\sigma=0$ (polo real), un lomo centrado en $\sigma=-2$ (parte real de los polos complejos), la curva toca el eje en $\sigma=4$ (cero) y decae hacia $0$ en los dos extremos.

**b) Respuesta al impulso.** $F(s)=1$ ⇒ $Y(s)=G(s)$:

$$
Y(s)=\frac{25s-100}{s(s^2+4s+5)}=\frac{A}{s}+\frac{Bs+C}{s^2+4s+5},
\qquad A=\frac{-100}{5}=-20,\quad B=20,\quad C=105
$$

$$
\frac{20s+105}{(s+2)^2+1}=\frac{20(s+2)}{(s+2)^2+1}+\frac{65}{(s+2)^2+1}
$$

$$
\boxed{\,y(t)=-20+20\,e^{-2t}\cos t+65\,e^{-2t}\operatorname{sen}t\,}
$$

</details>

<div style="break-before: page"></div>

## G) Sistemas: respuesta a una entrada exponencial (ejercicio de parcial) · domingo tarde · 25 min

$$
G(s)=\frac{2\,(s^2+2s-3)}{(s-1)(s+2)(s^2+8s+17)}
$$

Dada la entrada $f(t)=e^{-3t}$, calculá la respuesta $y(t)$ del sistema.

*Gemelo:* es **textual el 2025-1C rec Ej3c**. ⚠ Por eso ese ítem **ya no sirve a ciegas** en el simulacro del lunes; `plan.md` lo reemplaza.

<div style="height: 14cm"></div>

<details>
<summary><strong>Corrección G</strong></summary>

**Paso 1 — simplificar.** $s^2+2s-3=(s-1)(s+3)$ y se cancela $(s-1)$:

$$
G(s)=\frac{2\,(s+3)}{(s+2)\big((s+4)^2+1\big)}
$$

**Paso 2 — salida.** $F(s)=\dfrac1{s+3}$; el cero en $-3$ se cancela con la entrada:

$$
Y(s)=F(s)\,G(s)=\frac{2}{(s+2)\big((s+4)^2+1\big)}=\frac{A}{s+2}+\frac{Bs+C}{(s+4)^2+1}
$$

**Paso 3 — coeficientes.** Por tapado, $A=\dfrac{2}{(-2+4)^2+1}=\dfrac25$. Con la identidad $A\big((s+4)^2+1\big)+(Bs+C)(s+2)=2$:

$$
s^2:\ A+B=0\Rightarrow B=-\frac25,\qquad
s^0:\ 17A+2C=2\Rightarrow C=-\frac{12}{5}
$$

**Paso 4 — partir el numerador en $(s+4)$ + constante:**

$$
\frac{-\frac25 s-\frac{12}5}{(s+4)^2+1}
=-\frac25\cdot\frac{s+4}{(s+4)^2+1}-\frac45\cdot\frac{1}{(s+4)^2+1}
$$

$$
\boxed{\,y(t)=\frac25e^{-2t}-\frac25\cos(t)\,e^{-4t}-\frac45\operatorname{sen}(t)\,e^{-4t}\,}
$$

Coincide con la hoja de respuestas oficial del 2025-1C.

</details>

<div style="break-before: page"></div>

## H) Transformada Z: región de convergencia (guía 4c) · lunes mañana · 15 min

$$
x(n)=\begin{cases}3 & \text{si } n \text{ es múltiplo de } 5\\ (-2)^n & \text{si } n \text{ no es múltiplo de } 5\end{cases}
$$

Verdadero o falso, justificando: la región de convergencia de su transformada Z es $|z|>2$.

*Gemelos:* la familia "sucesión por casos + ROC": **2025-1C T1 Ej4a**, **2025-1C rec Ej4a** (también como V/F), **2024-2C T1/T2 Ej5a**. El profe de la grabación: "el área de convergencia sale sin resolver el resto de la transformada".

<div style="height: 10cm"></div>

<details>
<summary><strong>Corrección H</strong></summary>

**Paso 1 — una serie por cada clase de $n$** ($n=5k$, $5k+1$, …, $5k+4$):

$$
X(z)=3\sum_{k=0}^{\infty}\left(\frac{1}{z^5}\right)^{k}+\sum_{r=1}^{4}(-2)^r z^{-r}\sum_{k=0}^{\infty}\left(\frac{(-2)^5}{z^5}\right)^{k}
$$

**Paso 2 — cada geométrica exige razón con módulo menor que 1:**

$$
\left|\frac{1}{z^5}\right|<1\Rightarrow |z|>1,
\qquad
\left|\frac{(-2)^5}{z^5}\right|<1\Rightarrow |z|^5>32\Rightarrow |z|>2
$$

Las cuatro series de los no múltiplos tienen la misma razón, así que dan la misma condición.

**Paso 3 — intersección:** gana la más restrictiva, $|z|>2$. **VERDADERO.**

</details>

<div style="break-before: page"></div>

## I) Transformada Z: ecuación en diferencias de 2º orden (guía 7e) · lunes mediodía · 30 min

$$
x(n+2)-6\,x(n+1)+9\,x(n)=5\cdot2^n,\qquad x(0)=5,\quad x(1)=13
$$

Resolvé con transformada Z y verificá con $x(2)$.

*Gemelos:* **2024-1C T2 Ej5** y **2022-10-11 Ej4** (= **2024-1C T1 Ej4**), también de 2º orden. Este tiene **raíz doble** ($z=3$), el caso que usa $\mathcal Z[n\,a^n]$.

<div style="height: 15cm"></div>

<details>
<summary><strong>Corrección I</strong></summary>

**Paso 1 — transformar** con $\mathcal Z[x(n+2)]=z^2X-z^2x(0)-z\,x(1)$ y $\mathcal Z[x(n+1)]=zX-z\,x(0)$:

$$
z^2X-5z^2-13z-6\,(zX-5z)+9X=\frac{5z}{z-2}
$$

$$
X(z)\,(z^2-6z+9)=\frac{5z}{z-2}+5z^2-17z
$$

**Paso 2 — despejar** (común denominador):

$$
X(z)=\frac{5z^3-27z^2+39z}{(z-2)(z-3)^2}=z\cdot\frac{5z^2-27z+39}{(z-2)(z-3)^2}
$$

**Paso 3 — fracciones simples con "una $z$ afuera":**

$$
\frac{5z^2-27z+39}{(z-2)(z-3)^2}=\frac{A}{z-2}+\frac{B}{z-3}+\frac{C}{(z-3)^2}
$$

Por tapado, $A=\dfrac{20-54+39}{1}=5$ y $C=\dfrac{45-81+39}{1}=3$. Comparando $z^2$: $A+B=5\Rightarrow B=0$.

$$
X(z)=5\,\frac{z}{z-2}+3\,\frac{z}{(z-3)^2}
$$

**Paso 4 — antitransformar.** Con la tabla $\mathcal Z[n\,a^n]=\dfrac{az}{(z-a)^2}$ y $a=3$, el término $3\dfrac{z}{(z-3)^2}$ es $\mathcal Z[n\,3^n]$:

$$
\boxed{\,x(n)=5\cdot2^n+n\cdot3^n\,}
$$

**Verificación:** con la solución, $x(2)=20+18=38$. Con la ecuación, $x(2)=6\,x(1)-9\,x(0)+5\cdot2^0=78-45+5=38$. ✓

</details>

---

*Generado el 2026-10-02 desde las 7 fotos de la clase de repaso 2026 (`fuentes/clases/repaso-clase-2026/`). Enunciados reconstruidos de las notas de clase y de la guía (el de B a está marcado «≈»); resoluciones transcriptas de las fotos y verificadas con sympy; F b) agregado desde la resolución del 2015-05-29 T2.*
