# El parcial que se tomó este cuatrimestre (2026-10-06), resuelto

> Fuente: `examenes/resueltos/2026-10-06_Parcial_respuestas.pdf` (enunciados de los dos temas + resolución manuscrita del profesor, publicada en Avisos del aula el 2026-10-07). Índice en `examenes/INDICE.md`, transcripción del método en `examenes/resueltos/RESOLUCIONES-2026.md`.
>
> **Qué es de la cátedra y qué es mío:** los enunciados, el método y los resultados son los de la hoja del profesor. Las cuentas intermedias que la hoja saltea, las líneas "Qué te están tomando" y las referencias a las guías `01`–`04` son agregado propio. Todos los resultados están verificados con sympy; las dos erratas de la hoja van marcadas con ⚠.
>
> **Cómo usarlo:** el tema que rendiste, rehacelo en papel y comparalo con lo que entregaste: ahí está lo que tenés que arreglar. **El otro tema no lo abras todavía: es tu simulacro del domingo 2026-11-29**, el único examen real del formato vigente que todavía no viste.

---

## Qué dice este parcial sobre el recuperatorio

Es la evidencia más cercana que hay: mismo profesor, mismo cuatrimestre, mismo formato. Tres lecturas:

1. **Recicló hojas de 2022 y de 2024-1C, no las de 2025.** El Ej1 del Tema 1 ($t+2$ en $(0,2)$, cosenos, $C_n$ y $\sum 1/(2k+1)^2$) es textual el del 2022-10-11 y el del 2024-1C Tema 1. El Ej1 del Tema 2 ($t^2$) es el del 2024-1C Tema 2. El Ej3 del Tema 2 es textual el del 2022-10-11. Para el recuperatorio conviene practicar esas hojas con la misma prioridad que las de 2025.
2. **La estructura fue 3 + 2 + 3 + 2 = 10 ítems.** (En el Ej4 son 2 ítems; el a incluye la verificación.)
3. **Qué tipos de ítem salieron, comparado con 2025:**

| Ejercicio | Parcial 2026 (los dos temas) | Lo que había salido en 2025 y acá no |
|---|---|---|
| Ej1 Fourier | a) completar para cosenos y desarrollar · b) pasar a $C_n$ · c) **sumar una serie numérica** con la serie | media onda, espectro, la función que ya es un seno |
| Ej2 Laplace | a) integral impropia (división por $t$ en T1, multiplicación por $t^2$ en T2) · b) **transformada con un truco de álgebra** (binomio en T1, seno de una resta en T2) | convolución, demostración de $a^t$ |
| Ej3 Sistemas | a) hallar $k$ · b) **módulo por el método gráfico** (T1) o corte por el eje real de $Y(s)$ (T2) · c) respuesta al escalón (**polo doble** en T1, complejos en T2) | $G(s)$ desde la ecuación diferencial, tipo de respuesta |
| Ej4 Z | a) ecuación en diferencias de 1er orden con verificación · b) suma de una serie evaluando $X(z)$ | sucesión por paridad y región de convergencia, secuencia finita |

Lo marcado en negrita es lo que el análisis sobre 2025 daba por poco probable y se tomó igual: **sumar series con Fourier** (guía `01` §11) y el **método gráfico del módulo** (guía `03` §10). Entran al plan.

---

## Tema 1

<details>
<summary>🔴 <strong>T1 · Ej1 (Fourier, 3 ítems)</strong> — f(t) = t + 2 si t ∈ (0, 2), f(t) = f(t + 4). a) Completar para que la STF sea solo de cosenos y desarrollarla. b) Con ese desarrollo hallar los Cₙ de la SEF. c) Con el resultado hallar a qué converge Σ 1/(2k+1)², k desde 0. [RECICLADO: 2022-10-11 y 2024-1C T1]</summary>

**Qué te están tomando:** guía `01` §5 (completar y desarrollar), §6 (pase a $C_n$) y §11 (sumar una serie).

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** solo cosenos ⇒ se completa **par**. Gráfico: una "V" con vértice en $(0,2)$ que sube hasta 4 en $t=\pm2$.

$$
f(t)=\begin{cases}-t+2 & t\in(-2,0)\\ t+2 & t\in[0,2)\end{cases}\qquad T=4,\quad L=2,\quad \omega_0=\frac{\pi}{2}
$$

**Paso 2:** par ⇒ $b_m=0$. El valor medio sale del gráfico (trapecio entre 2 y 4): $\dfrac{a_0}{2}=3$.

**Paso 3:** el coeficiente, integrando solo en la mitad donde está definida:

$$
a_m=\frac{2}{2}\int_0^2 (t+2)\cos\left(\frac{m\pi}{2}t\right)dt=\left[\frac{\cos\left(\frac{m\pi}{2}t\right)}{\left(\frac{m\pi}{2}\right)^2}+\frac{t\operatorname{sen}\left(\frac{m\pi}{2}t\right)}{\frac{m\pi}{2}}+\frac{2\operatorname{sen}\left(\frac{m\pi}{2}t\right)}{\frac{m\pi}{2}}\right]_0^2
$$

Los dos términos con seno se anulan en $t=0$ y en $t=2$ ($\operatorname{sen}(m\pi)=0$). Queda:

$$
a_m=\frac{(-1)^m-1}{\left(\frac{m\pi}{2}\right)^2}\quad\Rightarrow\quad m\text{ par: }a_m=0\qquad m\text{ impar: }a_m=\frac{-8}{m^2\pi^2}
$$

**Paso 4:** se reindexa con $m=2k+1$:

$$
S(t)=3-\frac{8}{\pi^2}\sum_{k=0}^{\infty}\frac{\cos\left[(2k+1)\frac{\pi}{2}t\right]}{(2k+1)^2}
$$

**Paso 5 (b):** $C_m=\frac12(a_m-j\,b_m)$ con $b_m=0$:

$$
C_m=\frac{-4}{m^2\pi^2}\ \ (m\text{ impar}),\qquad C_m=0\ \ (m\text{ par},\ m\neq0),\qquad C_0=3
$$

La hoja del profesor recuadra solo $C_m=-4/(m^2\pi^2)$; aclarar para qué $m$ vale y cuánto da $C_0$ es lo prolijo.

**Paso 6 (c):** se evalúa la serie en un punto donde la función es continua y los cosenos valen 1: $t=0$, con $f(0)=2$.

$$
S(0)=3-\frac{8}{\pi^2}\sum_{k=0}^{\infty}\frac{1}{(2k+1)^2}=2\quad\Rightarrow\quad\sum_{k=0}^{\infty}\frac{1}{(2k+1)^2}=\frac{\pi^2}{8}
$$

</details>
</details>

<details>
<summary>🔴 <strong>T1 · Ej2 (Laplace, 2 ítems)</strong> — a) Calcular la integral de 0 a ∞ de e^(−t)·sen(t)/t dt. b) Calcular la transformada de Laplace de (t − 1)³, t > 0.</summary>

**Qué te están tomando:** guía `02` §5 (división por $t$) y §3 (tabla y linealidad).

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** por la definición de la transformada, la integral es una transformada evaluada en $s=1$:

$$
\int_0^{\infty}e^{-t}\,\frac{\operatorname{sen}t}{t}\,dt=\mathcal{L}\left[\frac{\operatorname{sen}t}{t}\right]_{s=1}
$$

**Paso 2:** división por $t$. Antes hay que dejar escrito que existe el límite: $\exists\lim_{t\to0}\dfrac{\operatorname{sen}t}{t}=1$.

$$
\mathcal{L}\left[\frac{\operatorname{sen}t}{t}\right]=\int_s^{\infty}\frac{1}{u^2+1}\,du=\Big[\operatorname{arctg}u\Big]_s^{\infty}=\frac{\pi}{2}-\operatorname{arctg}(s)
$$

**Paso 3:** se evalúa en $s=1$:

$$
\int_0^{\infty}e^{-t}\,\frac{\operatorname{sen}t}{t}\,dt=\frac{\pi}{2}-\operatorname{arctg}(1)=\frac{\pi}{4}
$$

**Paso 4 (b):** la trampa. **No** se usa la segunda propiedad de traslación: esa necesita la función corrida y nula hasta $t=1$ (o sea $t>1$), y acá es $t>0$. Se desarrolla el binomio y se transforma término a término:

$$
\mathcal{L}\left[(t-1)^3\right]=\mathcal{L}\left[t^3-3t^2+3t-1\right]=\frac{6}{s^4}-\frac{6}{s^3}+\frac{3}{s^2}-\frac{1}{s}=\frac{6-6s+3s^2-s^3}{s^4}
$$

</details>
</details>

<details>
<summary>🔴 <strong>T1 · Ej3 (Sistemas estables, 3 ítems)</strong> — G(s) = (3s² + 3s − 6) / (s³ + 5s² + 3s − k). a) Hallar k para que s = 1 no sea un cero. b) Calcular |G(1 + j)| en forma gráfica. c) Hallar la respuesta temporal y(t) si la entrada es un escalón unitario E(t).</summary>

$$
G(s)=\frac{3s^2+3s-6}{s^3+5s^2+3s-k}
$$

**Qué te están tomando:** guía `03` §5 (hallar $k$), §10 (método gráfico del módulo) y §7 (respuesta temporal, acá con polo doble).

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** se factoriza el numerador: $3s^2+3s-6=3(s-1)(s+2)$. Hoy $s=1$ **es** un cero. Para que deje de serlo, tiene que anular también el denominador, así se simplifica:

$$
1^3+5\cdot1^2+3\cdot1-k=0\quad\Rightarrow\quad k=9
$$

**Paso 2:** Ruffini con la raíz 1 sobre $s^3+5s^2+3s-9$ da cociente $s^2+6s+9=(s+3)^2$:

$$
G(s)=\frac{3(s-1)(s+2)}{(s-1)(s+3)^2}=\frac{3(s+2)}{(s+3)^2}
$$

Es la misma receta de "hallar $k$ para que sea estable": el $k$ hace que el numerador y el denominador compartan la raíz mala. Cambia solo cómo lo preguntan.

**Paso 3 (b):** se marcan el cero ($-2$) y el polo doble ($-3$) en el plano, y el punto $1+j$. Se mide la distancia desde cada uno hasta el punto:

- desde el cero $-2$: el vector es $3+j$, de módulo $\sqrt{3^2+1^2}=\sqrt{10}$;
- desde el polo $-3$: el vector es $4+j$, de módulo $\sqrt{17}$, y como el polo es doble va al cuadrado: $17$.

$$
\lvert G(1+j)\rvert=3\cdot\frac{\sqrt{10}}{17}
$$

No te olvides la constante 3 adelante: es el error que el profesor marca en clase.

**Paso 4 (c):** $Y(s)=G(s)\cdot F(s)$ con $F(s)=\dfrac1s$:

$$
Y(s)=\frac{3(s+2)}{s\,(s+3)^2}=\frac{A}{s}+\frac{B}{(s+3)^2}+\frac{C}{s+3}
$$

**Paso 5:** $A$ y $B$ salen tapando: $A=\dfrac{3\cdot2}{3^2}=\dfrac23$ y $B=\dfrac{3(-3+2)}{-3}=1$. Para $C$ se iguala el coeficiente de $s^2$ en $\frac23(s+3)^2+1\cdot s+C\,s(s+3)=3(s+2)$:

$$
\frac23+C=0\quad\Rightarrow\quad C=-\frac23
$$

**Paso 6:** se antitransforma:

$$
y(t)=\frac23+t\,e^{-3t}-\frac23\,e^{-3t}
$$

</details>
</details>

<details>
<summary>🔴 <strong>T1 · Ej4 (Transformada Z, 2 ítems)</strong> — a) Resolver con Z: x(n+1) + 3x(n) = 5·2ⁿ, x(0) = 2; verificar hallando x(3) con la ecuación y con la solución. b) Resolver mediante Z: Σ (2n + 3)(−1/4)ⁿ, n desde 0.</summary>

**Qué te están tomando:** guía `04` §9 (ecuación en diferencias de 1er orden) y §5 (suma de una serie).

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** se transforma. El desplazamiento trae la condición inicial:

$$
z\,X(z)-z\,x(0)+3X(z)=\frac{5z}{z-2}\quad\Rightarrow\quad X(z)\,(z+3)=\frac{5z}{z-2}+2z
$$

**Paso 2:** se junta todo en un cociente:

$$
X(z)=\frac{2z^2+z}{(z-2)(z+3)}
$$

**Paso 3:** fracciones simples **dejando una $z$ afuera**:

$$
\frac{X(z)}{z}=\frac{2z+1}{(z-2)(z+3)}=\frac{A}{z-2}+\frac{B}{z+3},\qquad A=\frac{5}{5}=1,\quad B=\frac{-5}{-5}=1
$$

$$
X(z)=\frac{z}{z-2}+\frac{z}{z+3}\quad\Rightarrow\quad x(n)=2^n+(-3)^n
$$

**Paso 4 (verificación):** con la solución, $x(3)=8-27=-19$. Con la ecuación: $x(0)=2$; $x(1)+3\cdot2=5\Rightarrow x(1)=-1$; $x(2)+3(-1)=10\Rightarrow x(2)=13$; $x(3)+3\cdot13=20\Rightarrow x(3)=-19$ ✓.

**Paso 5 (b):** $\left(-\frac14\right)^n=(-4)^{-n}$, así que la suma es una transformada evaluada en $z=-4$:

$$
\sum_{n=0}^{\infty}(2n+3)\left(-\frac14\right)^n=\mathcal{Z}\left[2n+3\right]_{z=-4},\qquad \mathcal{Z}[2n+3]=\frac{2z}{(z-1)^2}+\frac{3z}{z-1}
$$

**Paso 6:** en $z=-4$: $\dfrac{-8}{25}+\dfrac{-12}{-5}=-\dfrac{8}{25}+\dfrac{60}{25}$.

$$
\sum_{n=0}^{\infty}(2n+3)\left(-\frac14\right)^n=\frac{52}{25}
$$

</details>
</details>

---

## Tema 2

<details>
<summary>🔴 <strong>T2 · Ej1 (Fourier, 3 ítems)</strong> — f(t) = t² si t ∈ (0; 2), a completar en (−2; 0). a) Completar para que la STF sea solo de cosenos y desarrollarla. b) Con ese desarrollo hallar los Cₙ de la SEF. c) Con el resultado hallar a qué converge Σ (−1)ⁿ/n², n desde 1. [RECICLADO: variante del 2024-1C T2]</summary>

**Qué te están tomando:** guía `01` §5, §6 y §11.

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** solo cosenos ⇒ par. Como $t^2$ ya es par, la función completada es $f(t)=t^2$ en $(-2,2)$: una parábola que vale 4 en los extremos.

$$
T=4,\quad L=2,\quad \omega_0=\frac{\pi}{2},\qquad b_m=0
$$

**Paso 2:** valor medio:

$$
a_0=\frac22\int_0^2t^2\,dt=\frac83\quad\Rightarrow\quad\frac{a_0}{2}=\frac43
$$

**Paso 3:** coeficientes, por partes dos veces:

$$
a_m=\frac22\int_0^2t^2\cos\left(\frac{m\pi}{2}t\right)dt=\left[\frac{t^2\operatorname{sen}\left(\frac{m\pi}{2}t\right)}{\frac{m\pi}{2}}+\frac{2t\cos\left(\frac{m\pi}{2}t\right)}{\frac{m^2\pi^2}{4}}-\frac{2\operatorname{sen}\left(\frac{m\pi}{2}t\right)}{\frac{m^3\pi^3}{8}}\right]_0^2
$$

Los senos se anulan; queda solo el término del medio en $t=2$:

$$
a_m=\frac{4(-1)^m}{\frac{m^2\pi^2}{4}}=\frac{16(-1)^m}{m^2\pi^2}
$$

**Paso 4:**

$$
S(t)=\frac43+\frac{16}{\pi^2}\sum_{m=1}^{\infty}\frac{(-1)^m}{m^2}\cos\left(\frac{m\pi}{2}t\right)
$$

**Paso 5 (b):** $C_m=\frac12a_m$:

$$
C_m=\frac{8(-1)^m}{m^2\pi^2}\ \ (m\neq0),\qquad C_0=\frac43
$$

⚠ La hoja del profesor recuadra $C_m=\dfrac{8(-1)^m}{m^2}$: le falta el $\pi^2$ del denominador (se ve que es un descuido porque sale de dividir por 2 su propio $a_m$).

**Paso 6 (c):** se evalúa en $t=0$, donde $f(0)=0$ y los cosenos valen 1:

$$
\frac43+\frac{16}{\pi^2}\sum_{m=1}^{\infty}\frac{(-1)^m}{m^2}=0\quad\Rightarrow\quad\sum_{m=1}^{\infty}\frac{(-1)^m}{m^2}=-\frac{\pi^2}{12}
$$

</details>
</details>

<details>
<summary>🔴 <strong>T2 · Ej2 (Laplace, 2 ítems)</strong> — a) Calcular la integral de 0 a ∞ de sen(2t)·t²·e^(−3t) dt. b) Calcular la transformada de Laplace de sen(2t − π/3), t > 0.</summary>

**Qué te están tomando:** guía `02` §4 (integral impropia y multiplicación por $t^n$) y §3 (tabla y linealidad).

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** la integral es una transformada evaluada en $s=3$:

$$
\int_0^{\infty}\operatorname{sen}(2t)\,t^2\,e^{-3t}\,dt=\mathcal{L}\left[t^2\operatorname{sen}(2t)\right]_{s=3}
$$

**Paso 2:** multiplicar por $t^2$ es derivar dos veces la transformada (con signo $(-1)^2=+$):

$$
\frac{2}{s^2+4}\ \xrightarrow{\ \text{derivo}\ }\ \frac{-4s}{(s^2+4)^2}\ \xrightarrow{\ \text{derivo}\ }\ \frac{-4(s^2+4)+16s^2}{(s^2+4)^3}=\frac{12s^2-16}{(s^2+4)^3}
$$

**Paso 3:** en $s=3$: numerador $108-16=92$, denominador $13^3=2197$.

$$
\int_0^{\infty}\operatorname{sen}(2t)\,t^2\,e^{-3t}\,dt=\frac{92}{2197}
$$

**Paso 4 (b):** la misma trampa que en el Tema 1: es $t>0$, así que **no** va la segunda traslación. Se abre el seno de la resta:

$$
\operatorname{sen}\left(2t-\frac{\pi}{3}\right)=\operatorname{sen}(2t)\cos\frac{\pi}{3}-\cos(2t)\operatorname{sen}\frac{\pi}{3}=\frac12\operatorname{sen}(2t)-\frac{\sqrt3}{2}\cos(2t)
$$

**Paso 5:**

$$
\mathcal{L}\left[\operatorname{sen}\left(2t-\frac{\pi}{3}\right)\right]=\frac{1}{s^2+4}-\frac{\sqrt3}{2}\cdot\frac{s}{s^2+4}
$$

</details>
</details>

<details>
<summary>🔴 <strong>T2 · Ej3 (Sistemas estables, 3 ítems)</strong> — G(s) = 17(s² + s − k) / [(s − 2)(s² + 8s + 17)]. a) Hallar k para que G(s) sea estable. Con entrada escalón unitario E(t): b) dibujar un corte por el eje real de Y(s); c) hallar la respuesta temporal y(t). [RECICLADO: textual del 2022-10-11]</summary>

$$
G(s)=\frac{17(s^2+s-k)}{(s-2)(s^2+8s+17)}
$$

**Qué te están tomando:** guía `03` §5 (hallar $k$), §6 (corte por el eje real) y §7 (respuesta temporal con polos complejos).

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** el polo $s=2$ es positivo: inestable. Se pide que el numerador se anule ahí para cancelarlo:

$$
2^2+2-k=0\quad\Rightarrow\quad k=6,\qquad s^2+s-6=(s-2)(s+3)
$$

$$
G(s)=\frac{17(s-2)(s+3)}{(s-2)(s^2+8s+17)}=\frac{17(s+3)}{s^2+8s+17}
$$

Los polos que quedan son $-4\pm j$ (parte real negativa): estable.

**Paso 2 (b):** ojo, el corte es de $Y(s)$, no de $G(s)$: hay que multiplicar por la entrada primero.

$$
Y(s)=\frac{17(s+3)}{s\,(s^2+8s+17)}
$$

Hitos: ceros en $z_0=-3$ y $z_1=\infty$; polos en $p_0=-4+j$, $p_1=-4-j$ y $p_2=0$. En el dibujo: sube a infinito en $s=0$ (polo real), toca el eje en $s=-3$ (cero), hace un **lomo** en $s=-4$ (parte real del par complejo) y se acuesta sobre el eje hacia los dos costados (cero en el infinito).

**Paso 3 (c):** fracciones simples con un cuadrático irreducible:

$$
Y(s)=\frac{A}{s}+\frac{Bs+C}{s^2+8s+17},\qquad A=\frac{17\cdot3}{17}=3
$$

**Paso 4:** se iguala $3(s^2+8s+17)+Bs^2+Cs=17s+51$:

$$
3+B=0\Rightarrow B=-3,\qquad 24+C=17\Rightarrow C=-7
$$

⚠ En la hoja del profesor el miembro derecho quedó escrito "$=s+3$" y la segunda ecuación "$24+C=1$" (le faltó el 17). Los valores $B=-3$ y $C=-7$ que anota son los correctos.

**Paso 5:** se completa el cuadrado, $s^2+8s+17=(s+4)^2+1$, y se arma el numerador en función de $(s+4)$:

$$
Y(s)=\frac{3}{s}-\frac{3s+7}{(s+4)^2+1}=\frac{3}{s}-\frac{3(s+4)-5}{(s+4)^2+1}
$$

**Paso 6:**

$$
y(t)=3-3\cos(t)\,e^{-4t}+5\operatorname{sen}(t)\,e^{-4t}
$$

</details>
</details>

<details>
<summary>🔴 <strong>T2 · Ej4 (Transformada Z, 2 ítems)</strong> — a) Resolver con Z: x(n+1) = 3x(n) + 2, x(0) = 2; verificar hallando x(2) con la ecuación y con la solución. b) Resolver mediante Z: Σ (n + 1)(1/3)ⁿ, n desde 0.</summary>

**Qué te están tomando:** guía `04` §9 y §5.

<details>
<summary>Ver resolución</summary>

**Paso 1 (a):** el 2 suelto es $2\cdot u(n)$, cuya transformada es $\dfrac{2z}{z-1}$:

$$
z\,X(z)-z\,x(0)=3X(z)+\frac{2z}{z-1}\quad\Rightarrow\quad X(z)\,(z-3)=\frac{2z}{z-1}+2z
$$

**Paso 2:**

$$
X(z)=\frac{2z^2}{(z-1)(z-3)}
$$

**Paso 3:** una $z$ afuera:

$$
\frac{X(z)}{z}=\frac{2z}{(z-1)(z-3)}=\frac{A}{z-1}+\frac{B}{z-3},\qquad A=\frac{2}{-2}=-1,\quad B=\frac{6}{2}=3
$$

$$
X(z)=\frac{-z}{z-1}+\frac{3z}{z-3}\quad\Rightarrow\quad x(n)=-1+3^{n+1}
$$

**Paso 4 (verificación):** con la solución, $x(2)=-1+27=26$. Con la ecuación: $x(1)=3\cdot2+2=8$, $x(2)=3\cdot8+2=26$ ✓.

**Paso 5 (b):** $\left(\frac13\right)^n=3^{-n}$, la suma es una transformada evaluada en $z=3$:

$$
\sum_{n=0}^{\infty}(n+1)\left(\frac13\right)^n=\mathcal{Z}[n+1]_{z=3},\qquad\mathcal{Z}[n+1]=\frac{z}{(z-1)^2}+\frac{z}{z-1}
$$

**Paso 6:** en $z=3$: $\dfrac34+\dfrac32$.

$$
\sum_{n=0}^{\infty}(n+1)\left(\frac13\right)^n=\frac94
$$

</details>
</details>

---

## Tablero de resultados

| Ítem | Tema 1 | Tema 2 |
|---|---|---|
| Ej1 a | $S(t)=3-\frac{8}{\pi^2}\sum_{k\ge0}\frac{\cos[(2k+1)\frac{\pi}{2}t]}{(2k+1)^2}$ | $S(t)=\frac43+\frac{16}{\pi^2}\sum_{m\ge1}\frac{(-1)^m}{m^2}\cos(\frac{m\pi}{2}t)$ |
| Ej1 b | $C_m=\frac{-4}{m^2\pi^2}$ ($m$ impar), $C_0=3$ | $C_m=\frac{8(-1)^m}{m^2\pi^2}$, $C_0=\frac43$ |
| Ej1 c | $\frac{\pi^2}{8}$ | $-\frac{\pi^2}{12}$ |
| Ej2 a | $\frac{\pi}{4}$ | $\frac{92}{2197}$ |
| Ej2 b | $\frac{6-6s+3s^2-s^3}{s^4}$ | $\frac{1}{s^2+4}-\frac{\sqrt3}{2}\frac{s}{s^2+4}$ |
| Ej3 a | $k=9$ | $k=6$ |
| Ej3 b | $\lvert G(1+j)\rvert=\frac{3\sqrt{10}}{17}$ | corte de $Y(s)$: polo en 0, cero en $-3$, lomo en $-4$ |
| Ej3 c | $y(t)=\frac23+t\,e^{-3t}-\frac23e^{-3t}$ | $y(t)=3-3\cos(t)e^{-4t}+5\operatorname{sen}(t)e^{-4t}$ |
| Ej4 a | $x(n)=2^n+(-3)^n$, $x(3)=-19$ | $x(n)=-1+3^{n+1}$, $x(2)=26$ |
| Ej4 b | $\frac{52}{25}$ | $\frac94$ |

---

*Generado el 2026-11-26 desde `examenes/resueltos/2026-10-06_Parcial_respuestas.pdf` (leído con visión, 11 páginas). Resultados verificados con sympy. Erratas de la fuente: el $C_m$ del Tema 2 sin $\pi^2$ y un renglón intermedio de las fracciones simples del Ej3 del Tema 2.*
