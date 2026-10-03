# Repaso del primer parcial: ejercicios tipo parcial resueltos (complejos, Fourier, Laplace, sistemas estables, Z)

> Fuente: fuentes/clases/repaso primer parcial/Repaso Primer Parcial.pdf, págs. 1–17

---

## Índice

- [p. 1] — Sobre esta clase de repaso (qué es, cómo leerla, avisos del profe)
- [p. 1] — Números complejos
- [p. 1] — 📝 Ejercicio 1: raíces de $z^2+2z+3+j(2z+6)=0$, cuál afirmación es correcta
- [p. 2] — 📝 Ejercicio 2: raíces cuartas de $j$, producto y suma
- [p. 3] — Series de Fourier: cómo completar una función (paridad, coeficientes)
- [p. 3] — 📝 Ejercicio 3: completar $k(t)$ para que la STF tenga cosenos + Serie Exponencial
- [p. 4] — 📝 Ejercicio 4: completar para que no haya cosenos con valor medio 1 + suma de $\sum (-1)^k/(2k+1)$
- [p. 6] — Transformada de Laplace: resolución "miembro a miembro" e integrales impropias
- [p. 6] — 📝 Ejercicio 5: $y'-y=2t-t^2$, $y(0)=1$ por Laplace
- [p. 7] — 📝 Ejercicio 6: valor de $\int_0^\infty t\,\mathrm{sen}(at)\,e^{-2t}\,dt$
- [p. 7] — Sistemas estables: estabilidad, corte por el eje real, respuesta temporal
- [p. 7] — 📝 Ejercicio 7: hallar $K$ para que el sistema sea estable, corte de $|G(s)|$ con el eje real, respuesta al impulso
- [p. 9] — 📝 Ejercicio 8: reconstruir $G(s)$ desde el gráfico del corte y $|G(1+j)|=2$, respuesta a $x(t)=\frac{1}{\sqrt{26}}(1-t)$
- [p. 12] — Transformada Z: ecuaciones en diferencia y región de convergencia
- [p. 12] — 📝 Ejercicio 9: $x(n+1)=3x(n)+2$, $x(0)=2$ por Z, con verificación
- [p. 13] — 📝 Ejercicio 10: región de convergencia de una sucesión definida por múltiplos de 3 (+ la transformada)
- [p. 15] — "Si sobra tiempo": complejos
- [p. 15] — 📝 Ejercicio 11: $n$ tal que $(1-2j)^n=117-44j$; resolver $z^4+16=0 \wedge |z+1-j|\le 1$

---

## Sobre esta clase de repaso — [p. 1]

- Es el OneNote de la clase "Repaso Parcial" (fechado el lunes 18 de mayo de 2020). Son
  **enunciados de parciales reales** (fotos de hojas de examen pegadas en el OneNote) que el
  profesor resuelve a mano, en el orden en que los va tomando: complejos → Fourier →
  Laplace → sistemas estables → Z → complejos otra vez "si sobra tiempo".
- Varios enunciados son de **multiple choice** (los parciales viejos, 2015–2022, traían un
  ítem de opción múltiple justificado; ver `MATERIA.md`). Igual, el profe los resuelve
  completos como si fueran a desarrollar: lo que vale es el procedimiento.
- La clase es de 2020, cuando la materia todavía se llamaba Matemática Superior y había
  ejercicio de complejos. Según `MATERIA.md`, en el formato vigente (2025) **no hay
  ejercicio de complejos** como tal; el cronograma 2026 solo tiene un "repaso rápido de
  complejos". Los otros cuatro temas (Fourier, Laplace, sistemas, Z) son exactamente los
  4 ejercicios del parcial.

### Avisos y énfasis del profe durante la clase (resumen)

- **Sistemas:** "**Marginalmente estable es estable**" (un polo en $s=0$ no rompe la
  estabilidad). La forma de hacer estable un sistema con un polo real positivo es elegir
  $K$ para que **un cero lo cancele**.
- **Z:** al hacer fracciones simples de $X(z)$, "**DEJAR UNA Z AFUERA!!!!!!!**" (lo escribe en
  mayúsculas, con un meme del Gato con Botas pidiendo "please"): se descompone $X(z)/z$ y
  después se vuelve a multiplicar por $z$ para antitransformar con la tabla.
- **Z, región de convergencia:** "**Sólo importa la región de convergencia**": en un ítem de
  ROC no hace falta hallar la transformada cerrada; alcanza con escribir la serie como
  suma de geométricas y pedir $|a|<1$ en cada una. La transformada la calcula "**para
  practicar**".
- **Fourier:** la regla de decisión para completar una función es
  "**Cosenos = Par = Coef. reales**" (términos con cosenos en la STF ⇔ función par ⇔
  $C_n$ reales en la SEF). Si piden que **no** haya cosenos y valor medio distinto de 0, "**me
  piden impar desplazada**". Para sumar la serie numérica, evaluar la serie en el punto
  que deja "**sólo armónicas impares**".
- **Laplace:** las ecuaciones diferenciales se transforman "**miembro a miembro**"; la
  integral impropia $\int_0^\infty f(t)e^{-2t}\,dt$ es "la definición de la transformada
  evaluada en $s=2$". Para multiplicar por $t^n$: "**1°) derivo, 2°) cambio signo (una vez)**".
- **Complejos (potencias):** después de igualar módulos hay que "**chequear los
  argumentos: llevar todo al primer giro positivo**".
- Los complejos quedan para el final: "**Si sobra tiempo**".

---

## Números complejos — [p. 1]

Herramientas que usa el profe en estos ejercicios:

- Para una ecuación de segundo grado con coeficientes complejos se usa la **resolvente**
  directamente:

$$
z_{1,2}=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

- La **raíz cuadrada de un complejo** $w=a+bj$ en binómica: $\sqrt{w}=x+yj$ con

$$
x=\sqrt{\frac{|w|+a}{2}},\qquad y=\sqrt{\frac{|w|-a}{2}}
$$

  y los signos se eligen según el signo de $b$: si $b<0$ los signos de $x$ e $y$ son
  **opuestos** ($+\,-$ o $-\,+$); si $b>0$ son **iguales** ($+\,+$ o $-\,-$).

- **Raíces $n$-ésimas** en polar: si $z=[\rho,\varphi]$,

$$
w_k=\left[\sqrt[n]{\rho},\ \frac{\varphi+2k\pi}{n}\right],\qquad k=0,\dots,n-1
$$

<details>
<summary>📝 Ejercicio 1 — [p. 1]: raíces de z²+2z+3+j(2z+6)=0, cuál afirmación es correcta</summary>

Sea $z_1$ la raíz de menor módulo de la ecuación $z^2+2z+3+j(2z+6)=0$ y $z_2$ la de mayor
módulo:

a) $z_1$ es imaginaria pura  b) $z_2\in$ III cuadrante  c) $\bar z_1=z_2$  d) $z_2^2$ es
real  e) ninguna es correcta

<details>
<summary>Ver resolución</summary>

**Paso 1:** se distribuye la $j$ y se agrupa como polinomio en $z$ con coeficientes complejos.

$$
z^2+2z+3+j(2z+6)=0
$$

$$
z^2+2z+3+2jz+6j=0
$$

$$
z^2+(2+2j)z+3+6j=0
$$

**Paso 2:** resolvente con $a=1$, $b=2+2j$, $c=3+6j$.

$$
z_{1,2}=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

$$
z_{1,2}=\frac{-2-2j\pm\sqrt{(2+2j)^2-4\cdot 1\cdot(3+6j)}}{2\cdot 1}
$$

$$
z_{1,2}=\frac{-2-2j\pm\sqrt{4+8j-4-12-24j}}{2}
$$

$$
z_{1,2}=\frac{-2-2j\pm\sqrt{-12-16j}}{2}
$$

**Paso 3:** raíz cuadrada de $-12-16j$ (módulo $|{-12-16j}|=20$) en binómica:

$$
x=\sqrt{\frac{20+(-12)}{2}}=2,\qquad y=\sqrt{\frac{20-(-12)}{2}}=4
$$

Como $b=-16<0$, los signos son opuestos: $\sqrt{-12-16j}=\pm(2-4j)$.

**Paso 4:** las dos raíces.

$$
z=\frac{-2-2j+2-4j}{2}=-3j\qquad (|z|=3)\ \Rightarrow\ z_2
$$

$$
z=\frac{-2-2j-2+4j}{2}=-2+j\qquad (|z|=\sqrt5)\ \Rightarrow\ z_1
$$

**Paso 5:** se revisa cada opción.

- A) $z_1$ es imaginaria pura: **FALSO** ($z_1=-2+j$).
- B) $z_2$ pertenece al tercer cuadrante: **FALSO** ($z_2=-3j$ está sobre el eje imaginario).
- C) Conjugado de $z_1$ $=z_2$: **FALSO**.
- D) $z_2^2$ es real: **VERDADERO** ($(-3j)^2=-9$).
- E) Ninguna es correcta: **FALSO**.

</details>

</details>

<details>
<summary>📝 Ejercicio 2 — [p. 2]: raíces cuartas de j, producto y suma</summary>

Sean $w_0,w_1,w_2$ y $w_3$ las raíces cuartas de la unidad imaginaria $z=j$; se puede
asegurar que:

a) sólo una de ellas es imaginaria pura  b) sólo una de ellas es real  c) $w_0\cdot w_1\cdot
w_2\cdot w_3=-j$  d) $w_0+w_1+w_2+w_3=1$  e) n.a.

<details>
<summary>Ver resolución</summary>

**Paso 1:** $w_n=\sqrt[4]{j}$. Se pasa $j$ a polar: $j=[1,\pi/2]=[\rho,\varphi]$.

**Paso 2:** fórmula de las raíces $n$-ésimas.

$$
w_k=\left[\sqrt[n]{\rho},\ \frac{\varphi+2k\pi}{n}\right],\quad k=0,\dots,n-1
$$

$$
w_k=\left[\sqrt[4]{1},\ \frac{\pi/2+2k\pi}{4}\right],\quad k=0,\dots,3
$$

**Paso 3:** las cuatro raíces, separadas entre sí por $\pi/2$:

$$
w_0=[1,\pi/8],\quad w_1=[1,5\pi/8],\quad w_2=[1,9\pi/8],\quad w_3=[1,13\pi/8]
$$

**Paso 4:** opciones A y B. Ninguna raíz cae sobre los ejes (los argumentos son
$\pi/8$, $5\pi/8$, $9\pi/8$, $13\pi/8$): A) **FALSO**, B) **FALSO**.

**Paso 5:** opción C, producto en forma exponencial (se suman los argumentos).

$$
w_0\,w_1\,w_2\,w_3=e^{j\pi/8}\,e^{j5\pi/8}\,e^{j9\pi/8}\,e^{j13\pi/8}=e^{\frac{28\pi}{8}j}=1\cdot e^{\frac{7\pi}{2}j}
$$

En el dibujo del profe: una espiral que da vueltas desde el origen y termina apuntando
hacia abajo, en $-j$ (un argumento de $7\pi/2$ equivale a $3\pi/2$). Opción C:
**VERDADERA**. Opción E: **FALSA**.

**Paso 6:** opción D, suma en binómica.

$$
w_0+w_1+w_2+w_3=\cos(\pi/8)+j\,\mathrm{sen}(\pi/8)+\cos(5\pi/8)+j\,\mathrm{sen}(5\pi/8)+\cos(9\pi/8)+j\,\mathrm{sen}(9\pi/8)+\cos(13\pi/8)+j\,\mathrm{sen}(13\pi/8)=0
$$

Opción D: **FALSA**.

</details>

</details>

---

## Series de Fourier: cómo completar una función — [p. 3]

Lo que el profe deja escrito como regla, antes de hacer las cuentas:

- **"Cosenos = Par = Coef. reales"**: que la STF tenga términos con cosenos equivale a que
  la función (completada) sea **par**, y eso equivale a que los coeficientes $C_n$ de la
  SEF sean **reales**. Al revés: "que no tenga cosenos" ⇒ completar como función
  **impar**; si además piden un valor medio $\neq 0$, es una "**impar desplazada**" (impar
  más una constante igual al valor medio).
- Relación entre coeficientes de la SEF y de la STF:

$$
C_n=\frac{1}{2}\left(a_n-b_n\,j\right)
$$

  (si la función es par, $b_n=0$ y $C_n=\tfrac12 a_n$; en la resolución el profe tacha el
  término $b_n j$).

- Coeficientes de la STF, con $L$ el semiperíodo y $\omega_0=\pi/L$:

$$
a_0=\frac{2}{L}\int_0^L f(t)\,dt,\qquad a_n=\frac{2}{L}\int_0^L f(t)\cos(n\omega_0 t)\,dt
$$

  El profe marca con un círculo el $2$ de $\frac{2}{L}$: para una función par alcanza con
  integrar sobre medio período y duplicar. El término constante es $\frac{a_0}{2}=C_0$ (el
  valor medio).

- Para sumar una **serie numérica** con la serie hallada: evaluar $S(t)$ en un $t$ donde la
  función sea continua y los senos/cosenos tomen valores $0,\pm1$, de modo que queden
  "sólo armónicas impares" con signo alternado $(-1)^k$.

<details>
<summary>📝 Ejercicio 3 — [p. 3]: completar k(t) para que la STF tenga cosenos + Serie Exponencial</summary>

Dada la función

$$
f(t)=\begin{cases}2t & \text{si } 0<t<2\\ k(t) & \text{si } -2<t<0\end{cases}\qquad\text{y } f(t)=f(t+4)
$$

a) Halle la función $k(t)$ para que la Serie Trigonométrica de Fourier tenga términos con
cosenos.
b) Desarrolle $f(t)$ en Serie Exponencial de Fourier.

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** gráfico de lo dado: en $(0,2)$ la recta $2t$ sube desde $0$ hasta $4$ (en
rojo); el tramo $(-2,0)$ está punteado porque hay que elegirlo. Regla:

$$
\text{Cosenos} = \text{Par} = \text{Coef. reales (S.T.F.) (S.E.F.)}
$$

Se completa de forma **par**: en $(-2,0)$ se dibuja (en verde) el espejo de la recta, que
baja desde $4$ en $t=-2$ hasta $0$ en $t=0$.

$$
f(t)=\begin{cases}2t & \text{si } 0<t<2\\ -2t & \text{si } -2<t<0\end{cases}\qquad\Rightarrow\ k(t)=-2t
$$

Datos del período: $T=4$, $L=2$, $\omega_0=\pi/2$, $f(t)=f(t+4)$.

**Paso 2 (b):** S.E.F. Como la función es par, $b_n=0$ y

$$
C_n=\frac{1}{2}\left(a_n-\cancel{b_n\,j}\right)=\frac12 a_n
$$

**Paso 3:** término constante.

$$
a_0=\frac{2}{L}\int_0^L f(t)\,dt=\frac{2}{2}\int_0^2 2t\,dt=4\ \Rightarrow\ \frac{a_0}{2}=C_0=2
$$

**Paso 4:** $a_n$ (integrando por partes; el corchete se evalúa entre $0$ y $2$).

$$
a_n=\frac{2}{L}\int_0^L f(t)\cos(n\omega_0 t)\,dt=\frac{2}{2}\int_0^2 2t\cos\!\left(\frac{n\pi}{2}t\right)dt
$$

$$
=2\left[\frac{\cos\!\left(\frac{n\pi}{2}t\right)}{\left(\frac{n\pi}{2}\right)^2}+\frac{t\,\mathrm{sen}\!\left(\frac{n\pi}{2}t\right)}{\frac{n\pi}{2}}\right]_0^2
=2\left(\frac{4(-1)^n}{n^2\pi^2}+0-\frac{4}{n^2\pi^2}-0\right)
$$

(los dos términos con seno, marcados en rojo, valen $0$ en ambos extremos; los del coseno,
en verde, dan $4(-1)^n/(n^2\pi^2)$ en $t=2$ y $4/(n^2\pi^2)$ en $t=0$).

$$
a_n=\begin{cases}0 & n \text{ par}\\[2pt] \dfrac{-16}{n^2\pi^2} & n \text{ impar}\end{cases}
$$

**Paso 5:** coeficientes exponenciales y serie.

$$
C_n=\frac12 a_n=\frac{-8}{n^2\pi^2}\quad (n \text{ impar})
$$

$$
\text{S.E.F.}=S(t)=2-\frac{8}{\pi^2}\sum_{k=-\infty}^{+\infty}\frac{1}{(2k+1)^2}\,e^{j(2k+1)\frac{\pi}{2}t}
$$

$$
=2-\frac{8}{\pi^2}\sum_{k=0}^{\infty}\frac{1}{(2k+1)^2}\left(e^{j(2k+1)\frac{\pi}{2}t}+e^{-j(2k+1)\frac{\pi}{2}t}\right)
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 4 — [p. 4]: completar para que no haya cosenos con valor medio 1 + suma de ∑(−1)^k/(2k+1)</summary>

a) Dada $f(t)=t$ en $(1,2)$, complete en $(0,1)$ con $T=2$ para que la STF no tenga
cosenos, y su valor medio sea $1$. Desarrolle la serie.
b) A partir de la serie hallada, calcule el valor de

$$
\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}
$$

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** gráfico de lo dado: el segmento de recta $f(t)=t$ entre $(1,1)$ y $(2,2)$,
con líneas punteadas en $t=1$ y $t=2$.

"**Me piden impar desplazada (V.M. $=1$)**": sin cosenos ⇒ impar; con valor medio $1$ ⇒
impar corrida hacia arriba en $1$. Se completa en $(0,1)$ con la misma recta $t$, y queda
el diente de sierra: en el segundo gráfico la recta sube de $(0,0)$ a $(2,2)$ y su
extensión periódica (en verde) repite el mismo diente a la izquierda, entre $t=-2$ y $t=0$.

$$
f(t)=t\ \text{ si } 0\le t\le 2,\qquad f(t)=f(t+2)
$$

Datos: $T=2$, $L=1$, $\omega_0=\pi$.

**Paso 2:** coeficientes. Valor medio y cosenos directamente:

$$
\frac{a_0}{2}=1,\qquad a_n=0
$$

**Paso 3:** $b_n$ integrando sobre el período completo (por partes).

$$
b_n=\frac{1}{L}\int_0^2 t\,\mathrm{sen}(n\pi t)\,dt=\left[\frac{\mathrm{sen}(n\pi t)}{n^2\pi^2}-\frac{t\cos(n\pi t)}{n\pi}\right]_0^2=\frac{-2}{n\pi}
$$

**Paso 4:** la serie.

$$
S(t)=1-\frac{2}{\pi}\sum_{n=1}^{\infty}\frac{1}{n}\,\mathrm{sen}(n\pi t)
$$

**Paso 5 (b):** se evalúa en $t=\tfrac12$. Tabla de $\mathrm{sen}(n\pi/2)$:

| $n$ | $\mathrm{sen}(n\pi/2)$ |
|---|---|
| 1 | 1 |
| 2 | 0 |
| 3 | $-1$ |
| 4 | 0 |
| 5 | 1 |
| 6 | 0 |
| ⋮ | ⋮ |

Los valores no nulos siguen el patrón $(-1)^k$: "**Sólo armónicas impares**" ($n=2k+1$).

**Paso 6:** como $f(\tfrac12)=\tfrac12$,

$$
f\!\left(\tfrac12\right)=\frac12=1-\frac{2}{\pi}\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}
$$

$$
\frac{2}{\pi}\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}=\frac12\quad\Rightarrow\quad \boxed{\sum_{k=0}^{\infty}\frac{(-1)^k}{2k+1}=\frac{\pi}{4}}
$$

</details>

</details>

---

## Transformada de Laplace: resolución "miembro a miembro" e integrales impropias — [p. 6]

- **Ecuaciones diferenciales:** se transforma "**Laplace m.a.m.**" (miembro a miembro),
  usando $\mathcal{L}\{y'\}=sY(s)-y(0)$, se despeja $Y(s)$, se descompone en **fracciones
  simples** y se antitransforma. Para hallar los coeficientes de las fracciones simples el
  profe combina el método de **tapar** (evaluar en el polo para obtener los coeficientes
  de los términos de mayor orden) con **igualar coeficientes** por grado (cúbico,
  cuadrático, lineal).
- **Integrales impropias:** por definición,

$$
\mathcal{L}\{f(t)\}=F(s)=\int_0^{\infty}f(t)\,e^{-st}\,dt
$$

  así que una integral del tipo $\int_0^\infty f(t)\,e^{-2t}\,dt$ es **la transformada de
  $f$ evaluada en $s=2$**.

- **Multiplicación por $t^n$** (acá con $n=1$): "**1°) derivo** $F(s)$ respecto de $s$,
  **2°) cambio signo (una vez)**" — es decir, $\mathcal{L}\{t\,f(t)\}=-F'(s)$.

<details>
<summary>📝 Ejercicio 5 — [p. 6]: y' − y = 2t − t², y(0) = 1, por Laplace</summary>

Ej. 2: Dada la siguiente ecuación diferencial: $y'-y=2t-t^2$ con $y(0)=1$.
a) Resuelva analíticamente por Transformada de Laplace.

<details>
<summary>Ver resolución</summary>

**Paso 1:** se escribe la ecuación y se transforma "Laplace m.a.m." ($y(0)=1$, marcado en
rojo).

$$
y'(t)-y(t)=2t-t^2,\qquad y(0)=1
$$

$$
s\,Y(s)-\underbrace{y(0)}_{1}-Y(s)=\frac{2}{s^2}-\frac{2}{s^3}
$$

**Paso 2:** se despeja $Y(s)$.

$$
Y(s)\,(s-1)=\frac{2}{s^2}-\frac{2}{s^3}+1
$$

$$
Y(s)=\frac{2s-2+s^3}{s^3(s-1)}
$$

**Paso 3:** fracciones simples (polo triple en $0$ y simple en $1$).

$$
\frac{s^3+2s-2}{s^3(s-1)}=\frac{A}{s^3}+\frac{B}{s^2}+\frac{C}{s}+\frac{D}{s-1}
$$

Tapando: $A=\dfrac{-2}{-1}=2$ (numerador y el factor $(s-1)$ evaluados en $s=0$) y
$D=\dfrac{1}{1}=1$ (numerador y $s^3$ evaluados en $s=1$).

**Paso 4:** para $B$ y $C$ se iguala el numerador:

$$
2(s-1)+B\,s(s-1)+C\,s^2(s-1)+1\cdot s^3=s^3+2s-2
$$

- Cúbico: $C+1=1\Rightarrow C=0$.
- Cuadrático: $B=0$.

**Paso 5:** antitransformada.

$$
Y(s)=\frac{2}{s^3}+\frac{1}{s-1}
$$

$$
\mathcal{L}^{-1}\{Y(s)\}=y(t)=t^2+e^{t}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 6 — [p. 7]: valor de ∫₀^∞ t·sen(at)·e^(−2t) dt</summary>

3) El valor de la siguiente integral es: $\displaystyle\int_0^{\infty}t\,\mathrm{sen}(at)\,e^{-2t}\,dt$

a) $\dfrac{4}{(4+a^2)}$  b) $\dfrac{-4a}{(4-a^2)^2}$  c) $\dfrac{4a}{(4+a^2)^2}$  d) $\dfrac{-4}{(a^2+4)^2}$  e) n.a.

<details>
<summary>Ver resolución</summary>

**Paso 1:** definición de la transformada de Laplace.

$$
\mathcal{L}\{f(t)\}=F(s)=\int_0^{\infty}f(t)\,e^{-st}\,dt
$$

Comparando (el profe subraya $f(t)=t\,\mathrm{sen}(at)$ en azul y $e^{-2t}$ en verde):

$$
\int_0^{\infty}t\,\mathrm{sen}(at)\,e^{-2t}\,dt=\mathcal{L}\left[t\,\mathrm{sen}(at)\right]\Big|_{s=2}
$$

**Paso 2:** multiplicación por $t^n$ con $n=1$.

1°) Derivo:

$$
\frac{d}{ds}\left(\frac{a}{s^2+a^2}\right)=\frac{-2as}{(s^2+a^2)^2}
$$

2°) Cambio signo (una vez):

$$
\mathcal{L}\left[t\,\mathrm{sen}(at)\right]=\frac{2as}{(s^2+a^2)^2}
$$

**Paso 3:** se evalúa en $s=2$.

$$
\mathcal{L}\left[t\,\mathrm{sen}(at)\right]\Big|_{s=2}=\frac{4a}{(4+a^2)^2}\qquad\text{(opción C)}
$$

</details>

</details>

---

## Sistemas estables: estabilidad, corte por el eje real, respuesta temporal — [p. 7]

Lo que el profe aplica en los dos ejercicios de sistemas:

- **Estabilidad:** se factoriza el denominador y se clasifica cada factor. Un factor
  cuadrático con raíces **complejas conjugadas con parte real $<0$** está bien; un polo
  **real positivo** hace inestable al sistema, salvo que se lo **cancele con un cero** del
  numerador (eso fija $K$). Un polo en $s=0$ deja el sistema **marginalmente estable**, y
  "**Marg. estable es estable**".
- **Corte de $|G(s)|$ por el eje real:** se grafica $|G(\sigma)|$ para $\sigma$ real: va a
  infinito en los polos reales, vale $0$ en los ceros reales y hace una "joroba" a la
  altura de la parte real de los polos complejos.
- **Lectura inversa del gráfico:** un pico vertical ⇒ polo real; un cero del gráfico en el
  origen ⇒ cero en $s=0$; una joroba en $\sigma=-2$ ⇒ par de polos $-2\pm bj$. La constante
  $K$ se obtiene con el dato $|G(s_0)|$ por el **método gráfico de la constelación**: módulo
  $=K\cdot$ (producto de distancias de los ceros a $s_0$) / (producto de distancias de los
  polos a $s_0$).
- **Respuesta temporal:** $Y(s)=G(s)\,X(s)$. Para el impulso, $X(s)=1$ y $Y(s)=G(s)$. Se
  descompone $Y(s)$ en fracciones simples (igualando coeficientes cuadráticos y lineales),
  se completa el cuadrado del factor $s^2+4s+5=(s+2)^2+1$ y se parte el numerador lineal
  para que aparezcan las formas $\dfrac{s+2}{(s+2)^2+1}$ (coseno amortiguado) y
  $\dfrac{1}{(s+2)^2+1}$ (seno amortiguado).

<details>
<summary>📝 Ejercicio 7 — [p. 7]: hallar K para que el sistema sea estable, corte de |G(s)| con el eje real, respuesta al impulso</summary>

Ejercicio n° 3: Sea

$$
G(s)=\frac{25\,(s^2-Ks+12)}{(s^2+4s+5)(s^2-3s)}
$$

la transferencia de un sistema.
a) Halle el valor de $K\in\mathbb{R}$ sabiendo que el sistema es estable, y grafique
aproximadamente el corte de $|G(s)|$ con el eje real.
b) Halle la respuesta del sistema a una entrada impulso unitario.

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** se factoriza el denominador.

$$
G(s)=\frac{25\,(s^2-Ks+12)}{(s^2+4s+5)(s^2-3s)}=\frac{25\,(s^2-Ks+12)}{(s^2+4s+5)\cdot s\cdot(s-3)}
$$

- $(s^2+4s+5)$: raíces complejas conjugadas con parte real $<0$ (en verde): OK.
- $(s-3)$: raíz **real positiva** (en rojo): hay que cancelarla con un cero.
- $s$: polo en el origen. Nota del profe en un recuadro: "**Marg. estable, es estable**".

**Paso 2:** se pide que el numerador se anule en $s=3$.

$$
\left[s^2-Ks+12\right]_{s=3}=0\ \Rightarrow\ 9-3K+12=0\ \Rightarrow\ \boxed{K=7}
$$

**Paso 3:** Ruffini de $s^2-7s+12$ dividido por $(s-3)$:

$$
\begin{array}{c|ccc} & 1 & -7 & 12\\ 3 & & 3 & -12\\ \hline & 1 & -4 & \boxed{0}\end{array}
$$

$$
G(s)=\frac{25\,(s-4)}{(s^2+4s+5)\cdot s}
$$

Ceros y polos: $Z_1=4$, $Z_2=\infty$, $P_1=-2+j$, $P_2=-2-j$, $P_3=0$.

**Paso 4:** corte por el eje real. Gráfico (en rojo) de $|G(\sigma)|$: viene desde la
izquierda cerca de cero, hace una **joroba en $\sigma=-2$** (parte real de los polos
complejos), baja un poco y sube a **infinito en $\sigma=0$** (asíntota vertical, el polo en
el origen), del lado derecho baja hasta **tocar cero en $\sigma=4$** (el cero) y vuelve a
levantarse apenas. El profe deja también un link a GeoGebra con el gráfico
(`https://www.geogebra.org/classic/pgtuvdtj` [la URL se lee así en el OneNote; puede tener
algún caracter mal transcripto]).

**Paso 5 (b):** respuesta a $\delta(t)$.

$$
G(s)\,F(s)=Y(s),\qquad F(s)=1\ \Rightarrow\ G(s)=Y(s)
$$

$$
Y(s)=\frac{25\,(s-4)}{s\,(s^2+4s+5)}=\frac{A}{s}+\frac{Bs+C}{s^2+4s+5}
$$

Tapando en $s=0$: $A=\dfrac{-100}{5}=-20$.

**Paso 6:** igualando el numerador:

$$
-20\,(s^2+4s+5)+Bs^2+Cs=25s-100
$$

- Cuadráticos: $-20+B=0\Rightarrow B=20$.
- Lineales: $-80+C=25\Rightarrow C=105$.

**Paso 7:** se completa el cuadrado y se parte el numerador ($105=40+65$).

$$
Y(s)=\frac{-20}{s}+\frac{20s+105}{s^2+4s+5}=\frac{-20}{s}+\frac{20s+105}{(s+2)^2+1}
$$

$$
Y(s)=\frac{-20}{s}+\frac{20\,(s+2)}{(s+2)^2+1}+\frac{65}{(s+2)^2+1}
$$

**Paso 8:** antitransformada.

$$
y(t)=-20+20\cos(t)\,e^{-2t}+65\,\mathrm{sen}(t)\,e^{-2t}
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 8 — [p. 9]: reconstruir G(s) desde el gráfico del corte y |G(1+j)| = 2, respuesta a x(t) = (1/√26)(1 − t)</summary>

Ejercicio 2: El siguiente gráfico muestra el corte de $|G(s)|$ por el eje real:

*(Gráfico de $|G(\sigma)|$ vs. $\sigma=\mathrm{Re}(s)$: la curva arranca en cero a la
izquierda, forma una joroba redondeada centrada en $\sigma=-2$, baja y **toca cero en el
origen**, y tiene un **pico vertical (asíntota) en $\sigma=1$** marcado con línea
punteada, después del cual vuelve a bajar.)*

a) Escriba la expresión de $G(s)$ sabiendo que tiene únicamente 3 polos (cuya distancia al
eje real es entera y no mayor a 1) y un cero finito y simple, y además $|G(1+j)|=2$.
b) Halle la respuesta del sistema a una entrada $x(t)=\dfrac{1}{\sqrt{26}}(1-t)$ (con $t>0$).

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** lectura del gráfico.

- $Z_1=0$ (el gráfico toca cero en el origen).
- $P_1=1$ (asíntota vertical).
- $P_2=-2+bj$, $P_3=-2-bj$ (la joroba en $\sigma=-2$: par de polos complejos conjugados;
  en el croquis se marcan con cruces en $-2\pm b$).
- Dato: $|G(1+j)|=2$.

**Paso 2:** "$b$ es entero, no mayor que 1 y las raíces son conjugadas" $\Rightarrow$

$$
\boxed{b=1}
$$

**Paso 3:** el polinomio de los polos complejos:

$$
\left[s-(-2+j)\right]\left[s-(-2-j)\right]=s^2+2s+sj+2s+4-2j-js+2j+1=s^2+4s+5
$$

$$
G(s)=\frac{K\,s}{(s-1)(s^2+4s+5)}
$$

**Paso 4:** constelación para $|G(1+j)|=2$. Croquis: cruces en $1$, $-2+j$ y $-2-j$, un
círculo en el origen (cero) y el punto $1+j$ marcado en verde; se trazan los vectores
desde cada cero y polo hasta $1+j$ y se miden sus módulos: del cero $0$ a $1+j$, $\sqrt2$;
del polo $-2+j$, $3$; del polo $-2-j$, $\sqrt{13}$; del polo $1$, $1$.

$$
|G(1+j)|=\frac{K\cdot\sqrt2}{3\cdot\sqrt{13}\cdot 1}=2\ \Rightarrow\ K=3\sqrt{26}
$$

$$
G(s)=\frac{3\sqrt{26}\,s}{(s-1)(s^2+4s+5)}
$$

**Paso 5 (b):** respuesta a la entrada $x(t)=\dfrac{1}{\sqrt{26}}(1-t)$, $t>0$.

$$
Y(s)=G(s)\,X(s),\qquad X(s)=\frac{1}{\sqrt{26}}\left(\frac1s-\frac1{s^2}\right)=\frac{1}{\sqrt{26}}\left(\frac{s-1}{s^2}\right)
$$

$$
Y(s)=\frac{3\sqrt{26}\,s}{(s-1)(s^2+4s+5)}\cdot\frac{s-1}{s^2}\cdot\frac{1}{\sqrt{26}}
$$

Se cancelan $(s-1)$, una $s$ y $\sqrt{26}$ (tachados en rojo):

$$
Y(s)=\frac{3}{s\,(s^2+4s+5)}
$$

**Paso 6:** fracciones simples.

$$
Y(s)=\frac{A}{s}+\frac{Bs+C}{s^2+4s+5},\qquad A=\frac{3}{5}
$$

$$
\frac35\,(s^2+4s+5)+Bs^2+Cs=3
$$

- Cuadráticos: $\frac35+B=0\Rightarrow B=-\frac35$.
- Lineales: $\frac{12}{5}+C=0\Rightarrow C=-\frac{12}{5}$.

**Paso 7:** se completa el cuadrado y se parte el numerador ($\frac{12}{5}=\frac65+\frac65$).

$$
Y(s)=\frac{3/5}{s}-\frac{\frac35 s+\frac{12}{5}}{(s+2)^2+1}
$$

$$
Y(s)=\frac{3/5}{s}-\frac35\cdot\frac{s+2}{(s+2)^2+1}-\frac{6/5}{(s+2)^2+1}
$$

**Paso 8:** antitransformada.

$$
y(t)=\frac35-\frac35\cos(t)\,e^{-2t}-\frac65\,\mathrm{sen}(t)\,e^{-2t}
$$

</details>

</details>

---

## Transformada Z: ecuaciones en diferencia y región de convergencia — [p. 12]

- **Ecuaciones en diferencia:** se transforma "**Transf. Z m.a.m.**" usando
  $\mathcal{Z}\{x(n+1)\}=z\,X(z)-z\,x(0)$ y $\mathcal{Z}\{1\}=\dfrac{z}{z-1}$, se despeja $X(z)$ y se
  antitransforma por fracciones simples.
- **"DEJAR UNA Z AFUERA!!!!!!!"**: la descomposición en fracciones simples se hace sobre
  $\dfrac{X(z)}{z}$, dejando una $z$ factorizada afuera; así cada término queda de la forma
  $\dfrac{z}{z-a}$, que antitransforma a $a^n$.
- **Verificación** (la piden en el enunciado): calcular algunos valores con la ecuación en
  diferencia y compararlos con la solución cerrada.
- **Región de convergencia:** se escribe $X(z)=\sum_{n=0}^{\infty}x(n)\,z^{-n}$, se separan
  los términos según el patrón de $n$ y se reescribe cada grupo como **serie geométrica**.
  "**Sólo importa la región de convergencia**":

$$
\sum_{k=0}^{\infty}a^k\ \text{converge si y sólo si } |a|<1\qquad\left(\text{converge a } \frac{1}{1-a}\right)
$$

  La ROC es la **intersección** de las condiciones de todas las geométricas.

<details>
<summary>📝 Ejercicio 9 — [p. 12]: x(n+1) = 3x(n) + 2, x(0) = 2, por Z, con verificación</summary>

Ejercicio n° 4: Usando Transformada Z hallar la solución de la siguiente ecuación en
diferencia:

$$
x(n+1)=3x(n)+2,\qquad x(0)=2
$$

Verifique el resultado obtenido hallando el valor $x(2)$ usando la ecuación en diferencia y
su solución.

<details>
<summary>Ver resolución</summary>

**Paso 1:** se transforma "Transf. Z m.a.m." ($x(0)=2$, subrayado en rojo).

$$
z\,X(z)-z\,\underbrace{x(0)}_{2}=3X(z)+\frac{2z}{z-1}
$$

**Paso 2:** se despeja $X(z)$.

$$
X(z)\,(z-3)=\frac{2z}{z-1}+2z
$$

$$
X(z)=\frac{2z^2}{(z-1)(z-3)}
$$

**Paso 3:** fracciones simples. "**DEJAR UNA Z AFUERA!!!!!!!**"

$$
\frac{2z}{(z-1)(z-3)}=\frac{A}{z-1}+\frac{B}{z-3}
$$

Tapando: $A=\dfrac{2}{-2}=-1$, $B=\dfrac{6}{2}=3$.

$$
X(z)=-\frac{z}{z-1}+\frac{3z}{z-3}
$$

**Paso 4:** antitransformada.

$$
x(n)=-1+3\,(3)^n=-1+3^{\,n+1}
$$

**Paso 5:** verificación con la ecuación en diferencia:

$$
x(0)=2,\qquad x(1)=3\cdot x(0)+2=8,\qquad x(2)=3\cdot x(1)+2=26\ \checkmark
$$

Con la $x(n)$ hallada:

$$
x(2)=-1+3\cdot 3^2=26\ \checkmark
$$

</details>

</details>

<details>
<summary>📝 Ejercicio 10 — [p. 13]: región de convergencia de una sucesión definida por múltiplos de 3 (+ la transformada)</summary>

5) La región de convergencia de la transformada Z de

$$
x(n)=\begin{cases}-3 & \text{si } n \text{ no es múltiplo de } 3\\ (-2)^n & \text{si } n \text{ es múltiplo de } 3\end{cases}
$$

a) $|z|>2$  b) $|z|\ge 3$  c) $|z|\ge 2$  d) $|z|<3$  e) $2<|z|<3$  f) n.a.

<details>
<summary>Ver resolución</summary>

**Paso 1:** se escribe la transformada por definición, término a término.

$$
X(z)=\sum_{n=0}^{\infty}x(n)\,z^{-n}=\frac{(-2)^0}{z^0}+\frac{-3}{z^1}+\frac{-3}{z^2}+\frac{(-2)^3}{z^3}+\frac{-3}{z^4}+\dots
$$

**Paso 2:** se agrupa según $n=3k$, $n=3k+1$, $n=3k+2$.

$$
X(z)=\sum_{k=0}^{\infty}\left(\frac{-2}{z}\right)^{3k}-3\sum_{k=0}^{\infty}\left(\frac1z\right)^{3k+1}-3\sum_{k=0}^{\infty}\left(\frac1z\right)^{3k+2}
$$

$$
X(z)=\sum_{k=0}^{\infty}\left(\frac{-8}{z^3}\right)^{k}-\frac{3}{z}\sum_{k=0}^{\infty}\left(\frac{1}{z^3}\right)^{k}-\frac{3}{z^2}\sum_{k=0}^{\infty}\left(\frac{1}{z^3}\right)^{k}
$$

**Paso 3:** "**Sólo importa la región de convergencia**":

$$
\sum_{k=0}^{\infty}a^k\ \text{converge si y sólo si } |a|<1\quad\left(\text{converge a }\frac{1}{1-a}\right)
$$

Primera geométrica (en verde):

$$
\left|\frac{-8}{z^3}\right|<1\ \Rightarrow\ |z^3|>8\ \Rightarrow\ |z|>2
$$

Segunda y tercera (en rojo, la misma razón):

$$
\left|\frac{1}{z^3}\right|<1\ \Rightarrow\ |z^3|>1\ \Rightarrow\ |z|>1
$$

**Paso 4:** croquis: dos circunferencias concéntricas de radios $1$ y $2$; la zona exterior
a $|z|=1$ rayada en rojo y la exterior a $|z|=2$ rayada en verde. La ROC es la
**intersección**:

$$
|z|>2\qquad\text{(opción a)}
$$

**Paso 5:** "**Para practicar, vamos a hallar la transformada**" (sumando cada geométrica):

$$
X(z)=\frac{1}{1-\left(\frac{-8}{z^3}\right)}-\frac{3}{z}\cdot\frac{1}{1-\frac{1}{z^3}}-\frac{3}{z^2}\cdot\frac{1}{1-\frac{1}{z^3}}
$$

$$
=\frac{z^3}{z^3+8}-\frac{3}{z}\cdot\frac{z^3}{z^3-1}-\frac{3}{z^2}\cdot\frac{z^3}{z^3-1}
$$

(se simplifican $z$ y $z^2$ con el $z^3$ del numerador):

$$
\boxed{X(z)=\frac{z^3}{z^3+8}-\frac{3z^2}{z^3-1}-\frac{3z}{z^3-1}}
$$

</details>

</details>

---

## "Si sobra tiempo": complejos — [p. 15]

El profe titula así el último bloque: el ejercicio de complejos queda para el final de la
clase y solo si alcanza el tiempo. Dos técnicas que aparecen:

- **Potencia con exponente desconocido:** pasar base y resultado a polar, igualar
  **módulos** para despejar $n$ y después "**chequear los argumentos, llevando todo al
  primer giro positivo**" (sumar $2\pi$ a los argumentos negativos y restar vueltas
  completas $2k\pi$ al argumento multiplicado por $n$).
- **Raíces + condición de módulo:** resolver $z^n=w$ en polar (y, como control, en
  binómica por raíces cuadradas sucesivas), después probar cada raíz en la condición
  $|z-z_0|\le r$ (un disco; conviene dibujarlo y ubicar las raíces).

<details>
<summary>📝 Ejercicio 11 — [p. 15]: n tal que (1−2j)^n = 117−44j; resolver z⁴+16=0 ∧ |z+1−j| ≤ 1</summary>

Ejercicio n° 1:
a) Halle el valor de $n\in\mathbb{N}$ / $(1-2j)^n=117-44j$ (Justifique su forma de hallarlo).
b) Resuelva en $\mathbb{C}$: $z^4+16=0\ \wedge\ |z+1-j|\le 1$.

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** base y resultado en polar.

$$
(1-2j)^n=\left[\sqrt5,\ \mathrm{arctg}(-2)\right]^n=\left[(\sqrt5)^n,\ n\cdot\mathrm{arctg}(-2)\right]
$$

$$
117-44j=\left[125,\ \mathrm{arctg}\!\left(\frac{-44}{117}\right)\right]
$$

**Paso 2:** igualando módulos:

$$
(\sqrt5)^n=125\ \Rightarrow\ n=6\ \checkmark
$$

**Paso 3:** "**Chequear los argumentos (llevar todo a 1er giro positivo)**":

$$
\mathrm{arctg}\!\left(\frac{-44}{117}\right)=-0{,}3597+2\pi=5{,}9235
$$

$$
6\cdot\mathrm{arctg}(-2)=6\cdot(-1{,}1072+2\pi)=31{,}0562
$$

A $31{,}0562$ se le restan $8\pi$ (4 giros) y queda $5{,}9235$ ✓. Coinciden: $n=6$.

**Paso 4 (b):** se separan las dos condiciones: ① $z^4+16=0$ y ② $|z+1-j|\le 1$.

**Paso 5:** ① en polar: $z^4=-16$, es decir $z=\sqrt[4]{[16,\pi]}$. El profe escribe las
cuatro raíces así:

$$
w_0=[2,\pi/4]=\sqrt2+\sqrt2\,j,\qquad w_1=[2,5\pi/4]=-\sqrt2+\sqrt2\,j
$$

$$
w_2=[2,9\pi/4]=-\sqrt2-\sqrt2\,j,\qquad w_3=[2,13\pi/4]=\sqrt2-\sqrt2\,j
$$

*[Los argumentos $5\pi/4$, $9\pi/4$, $13\pi/4$ están así en el manuscrito; las formas
binómicas que el profe escribe al lado corresponden a los argumentos $3\pi/4$, $5\pi/4$ y
$7\pi/4$, que son los que salen de $(\pi+2k\pi)/4$. Se transcribe sin corregir.]*

**Paso 6:** ① en binómica, como control: $z^4=-16\Rightarrow z=\sqrt[4]{-16}=\sqrt{\sqrt{-16}}$.
Se abre en árbol: $\sqrt{-16}=\pm 4j$, y de cada rama se sacan dos raíces cuadradas:

$$
\sqrt{4j}:\quad x=\sqrt{\frac{|4j|+0}{2}},\ y=\sqrt{\frac{|4j|-0}{2}}\quad\text{signos } (+,+)\ /\ (-,-)
$$

$$
\sqrt{-4j}:\quad x=\sqrt{\frac{|-4j|+0}{2}},\ y=\sqrt{\frac{|-4j|-0}{2}}\quad\text{signos } (+,-)\ /\ (-,+)
$$

$$
w_0=\sqrt2+\sqrt2\,j,\quad w_1=-\sqrt2-\sqrt2\,j,\qquad w_2=\sqrt2-\sqrt2\,j,\quad w_3=-\sqrt2+\sqrt2\,j
$$

**Paso 7:** ② $|z+1-j|\le 1$ es el disco de centro $-1+j$ y radio $1$. Captura de GeoGebra:
circunferencia $(x+1)^2+(y-1)^2=1$ y los puntos $A=(\sqrt2,\sqrt2)=(1{,}41;\,1{,}41)$,
$B=(-\sqrt2,-\sqrt2)$, $C=(\sqrt2,-\sqrt2)$, $D=(-\sqrt2,\sqrt2)$; solo $D$ cae adentro del
círculo.

"**Sólo cumple** $z=-\sqrt2+\sqrt2\,j$."

**Paso 8:** si no se tiene el gráfico, se prueba cada raíz en la condición:

$$
\left|\sqrt2+\sqrt2\,j+1-j\right|=\sqrt6\approx 2{,}4495\quad\times
$$

$$
\left|-\sqrt2-\sqrt2\,j+1-j\right|=\sqrt6\quad\times
$$

$$
\left|\sqrt2-\sqrt2\,j+1-j\right|=2+\sqrt2\approx 3{,}4142\quad\times
$$

$$
\left|-\sqrt2+\sqrt2\,j+1-j\right|=2-\sqrt2\approx 0{,}5858\quad\checkmark
$$

</details>

</details>

---

*Generado el 2026-10-02 a partir de `fuentes/clases/repaso primer parcial/Repaso Primer Parcial.pdf` (OneNote de la clase de repaso del primer parcial, 17 págs., resolución manuscrita del profesor).*
