# Sistemas estables desde cero — guía lineal (domingo)

> Fuentes: `examenes/resueltos/RESOLUCIONES-2025.md` (Ej3 de Tema 1, Tema 2 y recuperatorio), `repaso/practica-repaso-2026.md` (E, F, G), apuntes `05` (OneNote práctica de sistemas), `07` (OneNote del repaso), `10` (video repaso del 1P), `11` (video práctica de sistemas), `13` (video teórica de sistemas), `examenes/INDICE.md`, `plan.md` y `fuentes/AYUDAMEMORIA-OFICIAL.pdf`. Toda la matemática verificada con sympy. Generado 2026-10-03.
>
> **Cómo usarla:** leé de arriba abajo, sin saltear. Los **Ejemplos guiados** están resueltos a la vista: leelos con lápiz y rehacé cada paso en papel. Los **Tu turno** se hacen en papel, con reloj y **sin mirar**; la corrección está plegada. Los que dicen **R-x** son de tu hoja de práctica (`exports/practica-repaso-2026-enunciados.pdf`) y se corrigen con `exports/practica-repaso-2026.pdf`. Tiempo total: ≈ 8 h, con pausas.

---

## 0. Qué te toman: el Ej3 vale 3 puntos

El Ej3 es **el ejercicio más pesado del parcial**: 2 o 3 ítems de 1 punto cada uno. Siempre es la misma historia: te dan una función de transferencia $G(s)$ (o la ecuación diferencial de un sistema físico) y te piden algunos de estos ítems.

| Ítem | Qué te piden | De qué parcial sale | Sección |
|---|---|---|---|
| Polos, ceros, ¿es estable? | Factorizar, listar polos y ceros y decir si el sistema es estable. | 2025-1C rec Ej3a | §4 |
| **Hallar $K$** | $G(s)$ trae un $K$ adentro del numerador; elegirlo para que el sistema sea estable. | 2025-1C T2 Ej3a ($k=3$), 2022-10-11 Ej5a, 2024-2C T2 Ej4a | §5 |
| Corte por el eje real | Dibujar a mano $\lvert G(\sigma)\rvert$ (o $\lvert Y(\sigma)\rvert$). Solo cualitativo. | 2025-1C rec Ej3b, 2022-10-11 Ej5b, 2024-1C T1 Ej5c | §6 |
| **Respuesta temporal** | Hallar $y(t)$ para una entrada dada: impulso, escalón o exponencial. | 2025-1C T2 Ej3b (escalón), rec Ej3c ($e^{-3t}$), T1 Ej3b ($-e^{-t}$) | §7 |
| Tipo de respuesta y valor estable | "Oscilatoria amortiguada", "exponencial decreciente"… y a qué valor tiende $y(t)$. | 2025-1C T2 Ej3c | §8 |
| $G(s)$ desde la ecuación diferencial | Sistema físico (carrito con resorte, circuito RLC) que parte del reposo. | 2025-1C T1 Ej3a | §9 |

Datos del dataset (16 hojas de parcial, 2015 → 2025): **elegir $K$ / estabilidad aparece en 15 de 16**, la **respuesta temporal en 14 de 16**. Y un ejercicio salió **tres veces textual** (sin-fecha K3521 T2, 2024-2C T1 y 2025-1C T2):

$$
G(s)=\frac{10\,(s^2-4s+k)}{s^3+5s^2+4s-10}
$$

Ese es el ejemplo guiado principal de esta guía: lo vas a ver resuelto por partes en §5, §6, §7 y §8, y en el checkpoint final lo rehacés solo, de punta a punta.

## 1. La idea en criollo

Un **sistema** es una caja: le entra una señal $f(t)$ (una fuerza, una corriente) y sale otra $y(t)$ (una posición, una tensión). En el tiempo la relación es complicada, pero **en Laplace es una multiplicación**:

$$
Y(s)=G(s)\cdot F(s)\qquad\Longleftrightarrow\qquad G(s)=\frac{Y(s)}{F(s)}
$$

$G(s)$ es la **función de transferencia**: un cociente de polinomios en $s$. Las raíces del numerador son los **ceros**; las del denominador, los **polos**.

¿Por qué importan los polos? Porque cuando antitransformás $Y(s)$ por fracciones simples, **cada polo $p$ te deja un término $e^{pt}$ en $y(t)$**:

- Si el polo tiene **parte real negativa**, $e^{pt}$ se apaga con el tiempo. Todo bien.
- Si tiene **parte real positiva**, $e^{pt}$ explota. El sistema "se va al diablo": es **inestable**.
- Si el polo es complejo, $a\pm bj$, aparecen $e^{at}\cos(bt)$ y $e^{at}\operatorname{sen}(bt)$: oscila, y la parte real $a$ decide si la oscilación se apaga o crece.

**Estable = todos los polos a la izquierda del eje imaginario (o sobre él).** Todo el Ej3 es: **factorizar, mirar dónde están los polos y antitransformar $Y=G\cdot F$.**

## 2. Qué tenés en el ayudamemoria y qué tenés que saber de memoria

En el parcial solo podés tener el **ayudamemoria oficial** (págs. 1–2 para el 1P) y la tabla de integrales. Nada más.

**Está en el ayudamemoria.** No lo memorices, pero sabé encontrarlo y usarlo:

- Transformada de la derivada: $\mathcal L[f'(t)]=sF(s)-f(0)$. Solo la primera derivada: la segunda la armás vos (§9).
- Transformada de la integral: $\mathcal L\left[\int_0^t f(u)\,du\right]=\dfrac{F(s)}{s}$ (para el circuito RLC).
- **Primera propiedad de traslación:** $\mathcal L[e^{at}f(t)]=F(s-a)$. Es la que convierte $\dfrac{s+3}{(s+3)^2+1}$ en $e^{-3t}\cos t$.
- **Teorema del valor final:** $\lim_{t\to\infty}f(t)=\lim_{s\to0}s\,F(s)$. Y el del valor inicial: $\lim_{t\to0}f(t)=\lim_{s\to\infty}s\,F(s)$.
- Tabla: $1\to\frac1s$, $t\to\frac1{s^2}$, $t^n\to\frac{n!}{s^{n+1}}$, $e^{at}\to\frac1{s-a}$, $\operatorname{sen}(at)\to\frac{a}{s^2+a^2}$, $\cos(at)\to\frac{s}{s^2+a^2}$, $\delta(t)\to1$.
- Definición de cero y polo por límite: $z$ es cero si $\lim_{s\to z}G(s)=0$; $p$ es polo si $\lim_{s\to p}G(s)=\infty$.

**No está en el ayudamemoria, así que va de memoria.** Es todo lo marcado con 🧠 en esta guía:

- 🧠 $Y=G\cdot F$ y $G=Y/F$.
- 🧠 Las entradas: impulso $\to F=1$; escalón unitario $E(t)\to F=\frac1s$; $e^{-at}\to F=\frac1{s+a}$.
- 🧠 Simplificar siempre: una raíz común arriba y abajo **no es ni cero ni polo**.
- 🧠 La tabla **polo → tipo de respuesta → estable/inestable** (§4).
- 🧠 Para hallar $K$: el numerador se tiene que anular en el polo inestable.
- 🧠 Las reglas del corte por el eje real (§6).
- 🧠 Fracciones simples: tapado, igualar coeficientes, completar cuadrados, "prestar" (§3).
- 🧠 Las dos fórmulas armadas con la traslación:

$$
\frac{s+a}{(s+a)^2+b^2}\ \longrightarrow\ e^{-at}\cos(bt)\qquad\qquad \frac{b}{(s+a)^2+b^2}\ \longrightarrow\ e^{-at}\operatorname{sen}(bt)
$$

- 🧠 Reposo $\Rightarrow y(0)=0$, $y'(0)=0$, y $\mathcal L[y'']=s^2Y-s\,y(0)-y'(0)$.

**La calculadora sí vale** para sacar las raíces de una cuadrática con coeficientes reales en el medio de un ejercicio de sistemas: el profe dijo que "estos cálculos simples no me interesan" (apunte `10`, [14:19]). Lo que sí tenés que escribir es el planteo.

---

## 3. Repaso: fracciones simples con raíces complejas (≈ 30 min)

Venís de la guía de Laplace, así que ya sabés el caso fácil (raíces reales distintas, todo sale "tapando"). Lo que aparece en **todos** los Ej3 es el caso con un **cuadrático sin raíces reales** en el denominador. Es el corazón del ejercicio: si esto sale, el Ej3 sale.

### Ejemplo guiado 1: antitransformar $Y(s)=\dfrac{3}{s\,(s^2+4s+5)}$

(Es la parte b del ejercicio 9 del repaso grabado, apuntes `07` y `10`.)

**Paso 0 — ¿el cuadrático se puede factorizar?** Discriminante: $4^2-4\cdot5=-4<0$. No tiene raíces reales: sus raíces son complejas, $-2\pm j$. **No se parte más.** Su fracción lleva arriba un polinomio de **un grado menos**: $Bs+C$.

**Paso 1 — la forma:**

$$
\frac{3}{s\,(s^2+4s+5)}=\frac{A}{s}+\frac{Bs+C}{s^2+4s+5}
$$

**Paso 2 — $A$ por tapado.** Tapás el factor $s$ y evaluás todo lo demás en su raíz, $s=0$. ¿Por qué funciona? Porque si multiplicás todo por $s$ y ponés $s=0$, el término de $B,C$ se muere y queda solo $A$.

$$
A=\frac{3}{0+0+5}=\frac35
$$

**Paso 3 — $B$ y $C$ igualando coeficientes.** Sacás denominador común y los numeradores tienen que ser iguales para todo $s$:

$$
A\,(s^2+4s+5)+(Bs+C)\,s=3
$$

- Cuadráticos ($s^2$): $A+B=0\Rightarrow B=-\frac35$.
- Lineales ($s$): $4A+C=0\Rightarrow C=-\frac{12}5$.
- Control con los independientes: $5A=3$ ✓.

**Paso 4 — completar cuadrados.** La mitad del coeficiente lineal es $2$; $s^2+4s+5=(s+2)^2+5-4=(s+2)^2+1$. Ahora se lee: $e^{-2t}$ (por el $s+2$) y senos y cosenos de $1\cdot t$ (por el $+1=1^2$).

**Paso 5 — "prestar" para que aparezca $s+2$ arriba.** La fórmula del coseno necesita **exactamente** $s+2$ en el numerador. Entonces:

$$
-\frac35s-\frac{12}5=-\frac35\,(s+2)+\frac65-\frac{12}5=-\frac35\,(s+2)-\frac65
$$

$$
Y(s)=\frac{3/5}{s}-\frac35\cdot\frac{s+2}{(s+2)^2+1}-\frac65\cdot\frac{1}{(s+2)^2+1}
$$

**Paso 6 — antitransformar** con la tabla y la traslación:

$$
y(t)=\frac35-\frac35\cos(t)\,e^{-2t}-\frac65\operatorname{sen}(t)\,e^{-2t}
$$

**Ojo cuando el número de afuera no es 1.** Si te queda $\dfrac{1}{(s+2)^2+9}$, el seno necesita un $3$ arriba ($b=3$): lo agregás y lo compensás, $\dfrac13\cdot\dfrac{3}{(s+2)^2+9}\to\dfrac13\,e^{-2t}\operatorname{sen}(3t)$.

### ✍️ Tu turno 1 — fracciones simples (apunte `11`, ejercicio 20) · 10 min

Antitransformá:

$$
Y(s)=\frac{6s+20}{s\,(s^2+6s+10)}
$$

<details>
<summary>Corrección (apuntes 05 y 11, ejercicio 20)</summary>

Forma $\dfrac{A}{s}+\dfrac{Bs+C}{s^2+6s+10}$. Tapando: $A=\dfrac{20}{10}=2$.

Identidad $2(s^2+6s+10)+(Bs+C)\,s=6s+20$: cuadráticos $2+B=0\Rightarrow B=-2$; lineales $12+C=6\Rightarrow C=-6$.

$$
Y(s)=\frac2s+\frac{-2s-6}{(s+3)^2+1}=\frac2s-2\cdot\frac{s+3}{(s+3)^2+1}
$$

Acá no hace falta prestar: $-2s-6=-2(s+3)$ ya tiene la forma justa.

$$
y(t)=2-2\,e^{-3t}\cos t
$$

</details>

---

## 4. $G(s)$, polos, ceros y estabilidad (≈ 45 min)

### 4.1 Lo que tenés que saber

- **Ceros:** raíces del numerador. **Polos:** raíces del denominador. **Pero después de simplificar.**
- 🧠 **Simplificar primero.** "En el 95 % de los casos hay algo" que se cancela (apunte `11`, [04:17]). Una raíz común arriba y abajo **no es ni cero ni polo**: no cumple la definición del ayudamemoria (ni $G\to0$ ni $G\to\infty$). Error típico: decir que esa raíz es cero y polo a la vez.
- **Siempre hay una constante $K$** adelante; si no se ve, vale 1.
- **Cero en el infinito:** si el grado del denominador es mayor que el del numerador, $G(s)\to0$ cuando $s\to\infty$. Ponelo en la lista de ceros ($z=\infty$); olvidarlo "no es un error muy grave", pero suma.
- Los coeficientes son reales, así que **si un polo es complejo, su conjugado también es polo**.
- **Constelación:** el plano $s$ (parte real horizontal, parte imaginaria vertical) con **×** en los polos y **○** en los ceros.

### 4.2 La tabla de los seis casos 🧠

Esta tabla es de la teórica (apunte `13`) y del OneNote (apunte `05`). **Para la estabilidad solo importan los polos**; los ceros "no cortan ni pinchan".

| Dónde está el polo | Fracción simple | Qué aporta a $y(t)$ | Tipo de respuesta | ¿Estable? |
|---|---|---|---|---|
| Real negativo, $-a$ | $\dfrac{A}{s+a}$ | $A\,e^{-at}$ | exponencial decreciente | estable |
| Complejos con parte real negativa, $-a\pm bj$ | $\dfrac{Bs+C}{(s+a)^2+b^2}$ | $e^{-at}\cos(bt)$, $e^{-at}\operatorname{sen}(bt)$ | oscilatoria amortiguada | estable |
| En el origen (simple) | $\dfrac{A}{s}$ | la constante $A$ | constante: corre la respuesta y da el **valor estable** | marginalmente estable **= estable** |
| Imaginarios puros, $\pm bj$ (simples) | $\dfrac{Bs+C}{s^2+b^2}$ | $\cos(bt)$, $\operatorname{sen}(bt)$ | oscilatoria de amplitud constante | marginalmente estable **= estable** |
| Real positivo, $a>0$ | $\dfrac{A}{s-a}$ | $A\,e^{at}$ | exponencial creciente | **inestable** |
| Complejos con parte real positiva | $\dfrac{Bs+C}{(s-a)^2+b^2}$ | $e^{at}\cos(bt)$, $e^{at}\operatorname{sen}(bt)$ | oscilatoria de amplitud creciente | **inestable** |

Reglas que salen de la tabla:

- **Estable ⇔ todos los polos tienen parte real negativa o nula.** Gráficamente: todos a la izquierda del eje vertical, o sobre él.
- **Un solo polo a la derecha basta para que sea inestable**, "por más que tengan 52.000 polos del lado izquierdo" (apunte `13`, [1:38:14]).
- **Marginalmente estable se clasifica como estable** ("Marg. estable es estable", OneNote del repaso). Si querés, aclarás "marginalmente".
- Los polos **múltiples** sobre el eje ($1/s^2$, $(s^2+4)^2$) dan respuestas no acotadas ($t$, $t\operatorname{sen}t$): inestables. El profe dijo que los polos múltiples "no les damos bola"; casi nunca aparecen.
- Atajo para un cuadrático $as^2+bs+c$ con raíces complejas: su parte real es $-\frac{b}{2a}$. Con $a>0$ y $b>0$, están a la izquierda.

### 4.3 Receta: polos, ceros y estabilidad

1. Factorizá numerador y denominador **completos** (factor común $s$, resolvente, Ruffini).
2. Tachá los factores comunes.
3. Listá ceros (con el del infinito) y polos de la versión simplificada.
4. Mirá la parte real de cada polo y clasificá con la tabla.

### Ejemplo guiado 2: $G(s)=\dfrac{s^2+3s+2}{s^3-2s^2-3s}$ (apuntes `05` y `11`, ejercicio 8)

**Paso 1 — factorizar.** Numerador: raíces $-1$ y $-2$, o sea $(s+1)(s+2)$. Denominador: factor común $s$, y $s^2-2s-3$ tiene raíces $3$ y $-1$:

$$
G(s)=\frac{(s+1)(s+2)}{s\,(s-3)(s+1)}
$$

**Paso 2 — simplificar.** El $(s+1)$ está arriba y abajo: se tacha. El $-1$ **no es ni cero ni polo**.

$$
G(s)=\frac{s+2}{s\,(s-3)}
$$

**Paso 3 — listar.** Ceros: $-2$ y $\infty$. Polos: $0$ y $3$.

**Paso 4 — clasificar.** El polo en $3$ es real positivo: **sistema inestable**. Tipo de respuesta, sin resolver nada: $\frac{A}{s}+\frac{B}{s-3}\to A+B\,e^{3t}$, **exponencial creciente**.

### Ejemplo guiado 3: $G(s)=\dfrac{3s^2-6s-24}{s^3-3s^2-4s}$ (apunte `05`, ejercicio 10a)

$$
G(s)=\frac{3\,(s-4)(s+2)}{s\,(s-4)(s+1)}=\frac{3\,(s+2)}{s\,(s+1)}
$$

Ceros: $-2$, $\infty$. Polos: $0$ y $-1$. No hay nada a la derecha y el polo en $0$ es simple: **marginalmente estable, o sea estable**. Tipo: $A+B\,e^{-t}$, exponencial decreciente "desplazada $A$ unidades"; esa $A$ es el valor estable.

### ✍️ Tu turno 2 — 2025-1C rec Ej3a · 10 min

Indicá los polos y ceros de $G(s)$ y si representa un sistema estable.

$$
G(s)=\frac{2\,(s^2+2s-3)}{(s-1)(s+2)(s^2+8s+17)}
$$

(Es la misma $G$ de tu R-G; acá solo te pido polos y ceros.)

<details>
<summary>Corrección (RESOLUCIONES-2025, recuperatorio Ej3a)</summary>

$s^2+2s-3=(s+3)(s-1)$ y el $(s-1)$ se cancela con el del denominador:

$$
G(s)=\frac{2\,(s+3)}{(s+2)(s^2+8s+17)}
$$

$s^2+8s+17=(s+4)^2+1$, raíces $-4\pm j$.

- Ceros: $z_0=-3$, $z_1=\infty$.
- Polos: $p_1=-2$, $p_{2,3}=-4\pm j$.
- Todos los polos con parte real negativa: **sistema estable**.

Constelación: ○ en $-3$; × en $-2$, en $-4+j$ y en $-4-j$.

Ojo: el $1$ **no** es polo. Si no simplificabas, decías "polo en 1, inestable" y perdías el punto.

</details>

**Errores típicos de §4:** no simplificar; poner la raíz cancelada como cero y polo; olvidar el conjugado de un polo complejo; decir "inestable" por un polo en $0$ (es marginalmente estable = estable); mirar los ceros para decidir estabilidad.

---

## 5. Hallar $K$ para que sea estable (≈ 1 h 15)

El profe: elegir $K$ para cancelar el polo inestable es "una idea básica, pero que aparece en un montón de ejercicios de sistemas estables" (apunte `10`, [1:24:42]).

**La idea:** si el denominador tiene un polo malo $p$ (parte real positiva), la única forma de sacárselo de encima es que **el numerador también se anule en $p$**: así el factor $(s-p)$ queda arriba y abajo y se cancela.

### Receta 🧠

1. **Factorizá el denominador.** Si es cúbico, buscá una raíz probando los divisores del término independiente ($\pm1,\pm2,\pm5,\ldots$): reemplazás y, **si da 0, recién ahí** hacés Ruffini. Lo que queda es un cuadrático: resolvente (o completar cuadrados, o calculadora).
2. **Identificá el polo malo** $p$: el que tiene parte real positiva. (Un polo en $0$ **no** es malo: es marginalmente estable.)
3. **Pedí $N(p)=0$**: reemplazá $s=p$ en el numerador, igualá a cero y despejá $K$.
4. **Reemplazá $K$**, factorizá el numerador (Ruffini con la raíz $p$, que ya sabés que es raíz) y **cancelá**.
5. Escribí la $G$ simplificada y confirmá que los polos que quedan tienen parte real $\le0$.

### Ejemplo guiado 4: el reciclado ×3, ítem a (2025-1C T2 Ej3a)

> Hallar $K$ para que $G(s)=\dfrac{10\,(s^2-4s+k)}{s^3+5s^2+4s-10}$ sea estable.

**Paso 1 — buscar una raíz del denominador.** Divisores de $-10$: $\pm1,\pm2,\pm5,\pm10$. Pruebo $s=1$: $1+5+4-10=0$ ✓. Es raíz. Ruffini con $1$:

$$
\begin{array}{c|cccc} & 1 & 5 & 4 & -10\\ 1 & & 1 & 6 & 10\\ \hline & 1 & 6 & 10 & \boxed{0}\end{array}
$$

$$
s^3+5s^2+4s-10=(s-1)(s^2+6s+10)
$$

**Paso 2 — clasificar los polos.** $s^2+6s+10=(s+3)^2+1$, raíces $-3\pm j$: parte real negativa, no molestan. El polo $s=1$ es **real positivo**: es el malo. "Hay que eliminar el polo en $s=1$" (hoja oficial).

**Paso 3 — el numerador se tiene que anular en $s=1$:**

$$
1^2-4\cdot1+k=0\quad\Longrightarrow\quad \boxed{k=3}
$$

**Paso 4 — reemplazar y cancelar.** $s^2-4s+3$ con Ruffini en $1$: $1\ \ {-4}\ \ 3\to1\ \ {-3}\ |\ 0$, o sea $(s-1)(s-3)$.

$$
G(s)=\frac{10\,(s-1)(s-3)}{(s-1)(s^2+6s+10)}=\frac{10\,(s-3)}{s^2+6s+10}
$$

**Paso 5 — confirmar.** Polos: $-3\pm j$ (estable). Ceros: $3$ y $\infty$. ¿Y el cero en $3$, que está a la derecha? **No importa: los ceros no cuentan para la estabilidad.**

### Variantes que ya aparecieron (para que no te sorprendan)

- **Polo en el origen además del malo** (R-F): solo cancelás el malo; el de $0$ deja el sistema marginalmente estable, que es estable.
- **Denominador ya factorizado a medias** (2024-2C T2): $s^2+s-6$ esconde el polo malo; factorizalo: $(s+3)(s-2)$.
- **Dos parámetros** (2024-2C rec): uno se elige para cancelar, el otro se acota para que su polo quede a la izquierda.
- **$K$ por un dato de valor, no de estabilidad** (2024-1C T1 Ej5b, "hallar $k$ para que $G(0)=2$"): simplificás y evaluás en $s=0$. Lo hacés en §8.
- **Multiple choice "no existe $k$" / "solo $k\le0$"** (exámenes viejos): mismo razonamiento, Tu turno 7.

### ✍️ Tu turno 3 — R-F a) de tu hoja · 20 min

Hacé el **a)** de R-F: $K$, polos, ceros. **El corte por el eje real de R-F dejalo para §6** y el **b)** para §7. Corregí con `exports/practica-repaso-2026.pdf`.

### ✍️ Tu turno 4 — 2022-10-11 Ej5a · 10 min

Hallá $k$ para que sea estable.

$$
G(s)=\frac{17\,(s^2+s-k)}{(s-2)(s^2+8s+17)}
$$

<details>
<summary>Corrección (resuelto para esta guía, verificado con sympy)</summary>

$s^2+8s+17=(s+4)^2+1$, polos $-4\pm j$: bien. El polo malo es $s=2$.

$$
2^2+2-k=0\quad\Longrightarrow\quad \boxed{k=6}
$$

$s^2+s-6=(s-2)(s+3)$; se cancela $(s-2)$:

$$
G(s)=\frac{17\,(s+3)}{s^2+8s+17}
$$

Polos $-4\pm j$, ceros $-3$ e $\infty$: estable.

</details>

### ✍️ Tu turno 5 — 2024-2C T2 Ej4a (= 2024-1C T2 Ej4a) · 10 min

Hallá $k$, si existe, para que el sistema sea estable.

$$
G(s)=\frac{5\,(s^2-ks-2)}{(s^2+s-6)(s^2+2s+2)}
$$

<details>
<summary>Corrección (k = 1 según el INDICE; desarrollo resuelto para esta guía, verificado con sympy)</summary>

Denominador: $s^2+s-6=(s+3)(s-2)$ y $s^2+2s+2=(s+1)^2+1$, polos $-1\pm j$. El malo es $s=2$.

$$
4-2k-2=0\quad\Longrightarrow\quad \boxed{k=1}
$$

$s^2-s-2=(s-2)(s+1)$; se cancela $(s-2)$:

$$
G(s)=\frac{5\,(s+1)}{(s+3)(s^2+2s+2)}
$$

Polos: $-3$, $-1\pm j$. Ceros: $-1$, $\infty$. Estable. **Guardá esta $G$**: la usás en §7 (Tu turno 11 y 12).

</details>

### ✍️ Tu turno 6 — 2024-2C rec Ej4a · 15 min

Indicá **todos** los valores de $a,b\in\mathbb R$ para los que el sistema es estable. Justificá.

$$
G(s)=\frac{34\,(s^3-3s^2-as)}{(s-5)(s+b)(s^2+8s+17)}
$$

<details>
<summary>Corrección (resuelto para esta guía, verificado con sympy)</summary>

**El parámetro $a$.** El polo $s=5$ es malo. El numerador es $s\,(s^2-3s-a)$; tiene que anularse en $5$:

$$
5\,(25-15-a)=0\quad\Longrightarrow\quad \boxed{a=10}
$$

Con $a=10$: $s^2-3s-10=(s-5)(s+2)$, y se cancela $(s-5)$:

$$
G(s)=\frac{34\,s\,(s+2)}{(s+b)(s^2+8s+17)}
$$

**El parámetro $b$.** Queda el polo $-b$ (los otros, $-4\pm j$, están bien). Para que no esté a la derecha: $-b\le0$, o sea $\boxed{b\ge0}$.

- $b=0$: el polo en $0$ se cancela con el cero en $0$ (y aunque no se cancelara, sería marginalmente estable).
- $b<0$: el polo $-b$ es positivo y ningún cero del numerador ($0$, $-2$) puede cancelarlo: inestable.

Respuesta: $a=10$ y $b\ge0$.

</details>

### ✍️ Tu turno 7 — dos multiple choice viejos (sin-fecha ≈2015, T1 Ej1c y T2 Ej1b) · 10 min

**a)** Para que $G(s)=\dfrac{s^2-ks+12}{(s^2+8s+25)(s-2)}$ sea estable: $k=0$ / $k=8$ / cualquier $k$ / no existe $k$.

**b)** Los valores de $k\in\mathbb R$ para que $G(s)=\dfrac{s^3-3s^2-4s}{(s-4)(s-k)(s^2+8s+17)}$ sea estable son: $\forall k$ / solo $k\ge0$ / solo $k\le0$ / no existen / n.a.

<details>
<summary>Corrección (respuestas del INDICE; justificación verificada con sympy)</summary>

**a) $k=8$.** $s^2+8s+25$ tiene raíces $-4\pm3j$ (bien). El malo es $s=2$: $4-2k+12=0\Rightarrow k=8$.

**b) Solo $k\le0$.** El numerador es $s\,(s-4)(s+1)$: cancela el polo malo $4$. Queda el polo $k$: tiene que ser $\le0$. Con $k=0$ se cancela con el cero en $0$; con $k<0$ está a la izquierda. Con $k>0$ hay un polo a la derecha (incluso con $k=4$: el denominador tendría $(s-4)^2$ y el numerador cancela uno solo).

</details>

**Errores típicos de §5:** hacer Ruffini con un número que no verificaste que sea raíz; querer cancelar también el polo en $0$; cancelar un polo que no era el malo; error de signo al evaluar $N(p)$; olvidarte de **reescribir $G$ simplificada**, que es lo que usás en todos los ítems siguientes.

---

## 6. Corte de $|G(s)|$ por el eje real (≈ 45 min)

$|G(s)|$ es una superficie sobre el plano $s$ (los polos son "volcanes" que suben a infinito, los ceros son "pozos" que tocan el piso). El **corte por el eje real** es lo que ves si cortás esa superficie con el plano $\mathrm{Im}(s)=0$: el gráfico de $|G(\sigma)|$ con $\sigma$ real.

**Es cualitativo.** "No importa el ancho de las asíntotas ni la altura"; hay que marcar los **hitos** (apunte `13`, [27:12]). Y con el gráfico alcanza, no hace falta justificar con palabras (apunte `10`, [1:33:03]).

### Receta 🧠

1. Partí de la $G$ **simplificada**. Marcá en el eje $\sigma$:
   - cada **polo real** → **asíntota vertical** (la curva sube a $\infty$);
   - cada **cero real** → la curva **toca el eje y rebota** (nunca lo cruza: es un módulo, siempre $\ge0$);
   - cada **par de polos complejos** $a\pm bj$ → una **montañita (lomo)** centrada en su **parte real** $a$ (el plano pasa entre los dos volcanes sin embocarle a ninguno). Ojo: en $a$, no en $0$;
   - los **ceros complejos no se ven**: no se marcan.
2. **Extremos:** si el grado de abajo es mayor (cero en el infinito), la curva se pega al eje a la izquierda y a la derecha.
3. Uní los hitos con una curva siempre positiva.
4. Si te piden el corte de $|Y(s)|$, primero armá $Y=G\cdot F$. Con escalón, $F=\frac1s$ **agrega un polo en $0$**: una asíntota vertical más.

El origen es un "comodín": un polo o cero en $0$ aparece tanto en el corte por el eje real como en el del eje imaginario. El corte por el eje imaginario casi no se toma en el formato actual; si lo piden, mismo criterio sobre el eje $j\omega$.

### Ejemplo guiado 5: todo real (apuntes `05` y `11`, ejercicio 3)

$$
G(s)=\frac{K\,(s+1)}{(s-3)(s+5)}
$$

Hitos: asíntotas verticales en $-5$ y en $3$; toca el eje en $-1$; cero en el infinito. El recorrido que describe el profe: viene pegada al eje desde la izquierda, sube a infinito en $-5$, baja, toca en $-1$, sube a la asíntota de $3$ y a la derecha vuelve a pegarse al eje.

<div class="fig" style="margin:0.6rem 0; page-break-inside: avoid;">
<svg viewBox="0 0 560 230" width="100%" style="max-width:560px" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<defs><clipPath id="clip-ej3apunte"><rect x="30" y="22" width="515" height="168"/></clipPath></defs>
<text x="30" y="14" fill="currentColor" font-size="12">|G(σ)| de G(s) = K(s+1)/((s−3)(s+5))</text>
<line x1="30" y1="190.0" x2="545" y2="190.0" stroke="currentColor" stroke-width="1"/>
<text x="537" y="218.0" fill="currentColor">σ</text>
<line x1="319.7" y1="22" x2="319.7" y2="190.0" stroke="currentColor" stroke-width="0.6" stroke-dasharray="1 3"/>
<line x1="158.8" y1="22" x2="158.8" y2="190.0" stroke="#c0392b" stroke-width="1" stroke-dasharray="5 4"/>
<line x1="416.2" y1="22" x2="416.2" y2="190.0" stroke="#c0392b" stroke-width="1" stroke-dasharray="5 4"/>
<line x1="158.8" y1="187.0" x2="158.8" y2="193.0" stroke="currentColor"/>
<text x="158.8" y="206.0" fill="currentColor" text-anchor="middle">−5</text>
<line x1="287.5" y1="187.0" x2="287.5" y2="193.0" stroke="currentColor"/>
<text x="287.5" y="206.0" fill="currentColor" text-anchor="middle">−1</text>
<line x1="319.7" y1="187.0" x2="319.7" y2="193.0" stroke="currentColor"/>
<text x="319.7" y="206.0" fill="currentColor" text-anchor="middle">0</text>
<line x1="416.2" y1="187.0" x2="416.2" y2="193.0" stroke="currentColor"/>
<text x="416.2" y="206.0" fill="currentColor" text-anchor="middle">3</text>
<circle cx="287.5" cy="190.0" r="4" fill="none" stroke="#2471a3" stroke-width="1.5"/>
<text x="158.8" y="220.0" fill="#c0392b" text-anchor="middle" font-size="11">polo</text>
<text x="416.2" y="220.0" fill="#c0392b" text-anchor="middle" font-size="11">polo</text>
<text x="287.5" y="220.0" fill="#2471a3" text-anchor="middle" font-size="11">cero</text>
<polyline points="30.0,152.3 31.4,152.0 32.9,151.7 34.3,151.3 35.7,150.9 37.2,150.6 38.6,150.2 40.0,149.8 41.4,149.4 42.9,149.1 44.3,148.7 45.7,148.2 47.2,147.8 48.6,147.4 50.0,146.9 51.5,146.5 52.9,146.0 54.3,145.6 55.8,145.1 57.2,144.6 58.6,144.1 60.0,143.6 61.5,143.0 62.9,142.5 64.3,141.9 65.8,141.3 67.2,140.8 68.6,140.1 70.1,139.5 71.5,138.9 72.9,138.2 74.3,137.5 75.8,136.8 77.2,136.1 78.6,135.4 80.1,134.6 81.5,133.8 82.9,133.0 84.4,132.2 85.8,131.3 87.2,130.5 88.7,129.5 90.1,128.6 91.5,127.6 92.9,126.6 94.4,125.5 95.8,124.4 97.2,123.3 98.7,122.1 100.1,120.9 101.5,119.7 103.0,118.3 104.4,117.0 105.8,115.6 107.3,114.1 108.7,112.5 110.1,110.9 111.5,109.3 113.0,107.5 114.4,105.7 115.8,103.8 117.3,101.8 118.7,99.7 120.1,97.5 121.6,95.2 123.0,92.7 124.4,90.2 125.8,87.5 127.3,84.7 128.7,81.8 130.1,78.7 131.6,75.4 133.0,71.9 134.4,68.3 135.9,64.5 137.3,60.4 138.7,56.2 140.2,51.7 141.6,47.0 143.0,42.0 144.4,36.8 145.9,31.3 147.3,25.6 148.7,19.6 150.2,13.4 151.6,6.9 153.0,0.2 154.5,-6.7 155.9,-13.8 157.3,-21.0 157.8,-23.4 158.1,-25.1 158.4,-26.7 158.6,-27.6 158.7,-28.1 158.7,-28.2 158.7,-28.3 158.7,-28.4 158.7,-28.4" fill="none" stroke="#1e8449" stroke-width="2" clip-path="url(#clip-ej3apunte)"/>
<polyline points="158.8,-28.4 158.8,-28.4 158.8,-28.3 158.8,-28.2 158.8,-28.1 158.9,-27.6 159.1,-26.7 159.4,-25.1 159.7,-23.4 160.2,-21.0 161.6,-13.5 163.0,-6.0 164.5,1.5 165.9,8.8 167.3,16.1 168.8,23.2 170.2,30.1 171.6,36.8 173.1,43.3 174.5,49.5 175.9,55.5 177.3,61.2 178.8,66.7 180.2,71.9 181.6,76.9 183.1,81.6 184.5,86.1 185.9,90.4 187.4,94.5 188.8,98.3 190.2,102.0 191.7,105.5 193.1,108.8 194.5,111.9 195.9,114.9 197.4,117.8 198.8,120.5 200.2,123.1 201.7,125.5 203.1,127.9 204.5,130.1 206.0,132.3 207.4,134.4 208.8,136.3 210.2,138.2 211.7,140.0 213.1,141.8 214.5,143.5 216.0,145.1 217.4,146.6 218.8,148.1 220.3,149.6 221.7,151.0 223.1,152.3 224.6,153.6 226.0,154.9 227.4,156.1 228.8,157.3 230.3,158.5 231.7,159.6 233.1,160.7 234.6,161.7 236.0,162.8 237.4,163.8 238.9,164.8 240.3,165.7 241.7,166.6 243.2,167.6 244.6,168.4 246.0,169.3 247.4,170.2 248.9,171.0 250.3,171.8 251.7,172.7 253.2,173.4 254.6,174.2 256.0,175.0 257.5,175.8 258.9,176.5 260.3,177.2 261.8,178.0 263.2,178.7 264.6,179.4 266.0,180.1 267.5,180.8 268.9,181.5 270.3,182.1 271.8,182.8 273.2,183.5 274.6,184.2 276.1,184.8 277.5,185.5 278.9,186.1 280.3,186.8 281.8,187.4 283.2,188.1 284.6,188.7 286.1,189.4 287.5,190.0 288.9,189.4 290.4,188.7 291.8,188.1 293.2,187.4 294.7,186.8 296.1,186.1 297.5,185.5 298.9,184.8 300.4,184.2 301.8,183.5 303.2,182.8 304.7,182.1 306.1,181.5 307.5,180.8 309.0,180.1 310.4,179.4 311.8,178.7 313.2,178.0 314.7,177.2 316.1,176.5 317.5,175.8 319.0,175.0 320.4,174.2 321.8,173.4 323.3,172.7 324.7,171.8 326.1,171.0 327.6,170.2 329.0,169.3 330.4,168.4 331.8,167.6 333.3,166.6 334.7,165.7 336.1,164.8 337.6,163.8 339.0,162.8 340.4,161.7 341.9,160.7 343.3,159.6 344.7,158.5 346.2,157.3 347.6,156.1 349.0,154.9 350.4,153.6 351.9,152.3 353.3,151.0 354.7,149.6 356.2,148.1 357.6,146.6 359.0,145.1 360.5,143.5 361.9,141.8 363.3,140.0 364.8,138.2 366.2,136.3 367.6,134.4 369.0,132.3 370.5,130.1 371.9,127.9 373.3,125.5 374.8,123.1 376.2,120.5 377.6,117.8 379.1,114.9 380.5,111.9 381.9,108.8 383.3,105.5 384.8,102.0 386.2,98.3 387.6,94.5 389.1,90.4 390.5,86.1 391.9,81.6 393.4,76.9 394.8,71.9 396.2,66.7 397.7,61.2 399.1,55.5 400.5,49.5 401.9,43.3 403.4,36.8 404.8,30.1 406.2,23.2 407.7,16.1 409.1,8.8 410.5,1.5 412.0,-6.0 413.4,-13.5 414.8,-21.0 415.3,-23.4 415.6,-25.1 415.9,-26.7 416.1,-27.6 416.2,-28.1 416.2,-28.2 416.2,-28.3 416.2,-28.4 416.2,-28.4" fill="none" stroke="#1e8449" stroke-width="2" clip-path="url(#clip-ej3apunte)"/>
<polyline points="416.3,-28.4 416.3,-28.4 416.3,-28.3 416.3,-28.2 416.3,-28.1 416.4,-27.6 416.6,-26.7 416.9,-25.1 417.2,-23.4 417.7,-21.0 419.1,-13.8 420.5,-6.7 422.0,0.2 423.4,6.9 424.8,13.4 426.3,19.6 427.7,25.6 429.1,31.3 430.6,36.8 432.0,42.0 433.4,47.0 434.8,51.7 436.3,56.2 437.7,60.4 439.1,64.5 440.6,68.3 442.0,71.9 443.4,75.4 444.9,78.7 446.3,81.8 447.7,84.7 449.2,87.5 450.6,90.2 452.0,92.7 453.4,95.2 454.9,97.5 456.3,99.7 457.7,101.8 459.2,103.8 460.6,105.7 462.0,107.5 463.5,109.3 464.9,110.9 466.3,112.5 467.8,114.1 469.2,115.6 470.6,117.0 472.0,118.3 473.5,119.7 474.9,120.9 476.3,122.1 477.8,123.3 479.2,124.4 480.6,125.5 482.1,126.6 483.5,127.6 484.9,128.6 486.3,129.5 487.8,130.5 489.2,131.3 490.6,132.2 492.1,133.0 493.5,133.8 494.9,134.6 496.4,135.4 497.8,136.1 499.2,136.8 500.7,137.5 502.1,138.2 503.5,138.9 504.9,139.5 506.4,140.1 507.8,140.8 509.2,141.3 510.7,141.9 512.1,142.5 513.5,143.0 515.0,143.6 516.4,144.1 517.8,144.6 519.2,145.1 520.7,145.6 522.1,146.0 523.5,146.5 525.0,146.9 526.4,147.4 527.8,147.8 529.3,148.2 530.7,148.7 532.1,149.1 533.6,149.4 535.0,149.8 536.4,150.2 537.8,150.6 539.3,150.9 540.7,151.3 542.1,151.7 543.6,152.0 545.0,152.3" fill="none" stroke="#1e8449" stroke-width="2" clip-path="url(#clip-ej3apunte)"/>
</svg>
</div>

### Ejemplo guiado 6: con polos complejos (el reciclado, después de $k=3$)

$$
G(s)=\frac{10\,(s-3)}{s^2+6s+10}=\frac{10\,(s-3)}{(s+3)^2+1}
$$

Hitos: **ningún polo real** (no hay asíntotas verticales); **lomo en $\sigma=-3$** (parte real de $-3\pm j$); **toca el eje en $\sigma=3$** (el cero); cero en el infinito: pegada al eje en los extremos. (Dibujo hecho para esta guía aplicando la receta.)

<div class="fig" style="margin:0.6rem 0; page-break-inside: avoid;">
<svg viewBox="0 0 560 230" width="100%" style="max-width:560px" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<defs><clipPath id="clip-reciclado"><rect x="30" y="22" width="515" height="168"/></clipPath></defs>
<text x="30" y="14" fill="currentColor" font-size="12">|G(σ)| de G(s) = 10(s−3)/(s²+6s+10)</text>
<line x1="30" y1="190.0" x2="545" y2="190.0" stroke="currentColor" stroke-width="1"/>
<text x="537" y="218.0" fill="currentColor">σ</text>
<line x1="319.7" y1="22" x2="319.7" y2="190.0" stroke="currentColor" stroke-width="0.6" stroke-dasharray="1 3"/>
<line x1="223.1" y1="187.0" x2="223.1" y2="193.0" stroke="currentColor"/>
<text x="223.1" y="206.0" fill="currentColor" text-anchor="middle">−3</text>
<line x1="319.7" y1="187.0" x2="319.7" y2="193.0" stroke="currentColor"/>
<text x="319.7" y="206.0" fill="currentColor" text-anchor="middle">0</text>
<line x1="416.2" y1="187.0" x2="416.2" y2="193.0" stroke="currentColor"/>
<text x="416.2" y="206.0" fill="currentColor" text-anchor="middle">3</text>
<circle cx="416.2" cy="190.0" r="4" fill="none" stroke="#2471a3" stroke-width="1.5"/>
<text x="416.2" y="220.0" fill="#2471a3" text-anchor="middle" font-size="11">cero</text>
<text x="223.1" y="220.0" fill="#7d3c98" text-anchor="middle" font-size="11">lomo</text>
<polyline points="30.0,147.2 31.4,147.0 32.9,146.9 34.3,146.7 35.7,146.6 37.2,146.4 38.6,146.3 40.0,146.1 41.4,145.9 42.9,145.8 44.3,145.6 45.7,145.4 47.2,145.3 48.6,145.1 50.0,144.9 51.5,144.7 52.9,144.5 54.3,144.4 55.8,144.2 57.2,144.0 58.6,143.8 60.0,143.6 61.5,143.4 62.9,143.2 64.3,143.0 65.8,142.8 67.2,142.6 68.6,142.4 70.1,142.2 71.5,142.0 72.9,141.8 74.3,141.5 75.8,141.3 77.2,141.1 78.6,140.9 80.1,140.6 81.5,140.4 82.9,140.2 84.4,139.9 85.8,139.7 87.2,139.4 88.7,139.2 90.1,138.9 91.5,138.6 92.9,138.4 94.4,138.1 95.8,137.8 97.2,137.5 98.7,137.3 100.1,137.0 101.5,136.7 103.0,136.4 104.4,136.1 105.8,135.8 107.3,135.5 108.7,135.2 110.1,134.8 111.5,134.5 113.0,134.2 114.4,133.8 115.8,133.5 117.3,133.1 118.7,132.8 120.1,132.4 121.6,132.0 123.0,131.7 124.4,131.3 125.8,130.9 127.3,130.5 128.7,130.1 130.1,129.7 131.6,129.2 133.0,128.8 134.4,128.4 135.9,127.9 137.3,127.5 138.7,127.0 140.2,126.5 141.6,126.1 143.0,125.6 144.4,125.1 145.9,124.6 147.3,124.0 148.7,123.5 150.2,123.0 151.6,122.4 153.0,121.8 154.5,121.3 155.9,120.7 157.3,120.1 158.8,119.5 160.2,118.8 161.6,118.2 163.0,117.5 164.5,116.9 165.9,116.2 167.3,115.5 168.8,114.8 170.2,114.1 171.6,113.3 173.1,112.6 174.5,111.8 175.9,111.1 177.3,110.3 178.8,109.5 180.2,108.7 181.6,107.8 183.1,107.0 184.5,106.1 185.9,105.3 187.4,104.4 188.8,103.5 190.2,102.7 191.7,101.8 193.1,100.9 194.5,100.0 195.9,99.1 197.4,98.3 198.8,97.4 200.2,96.6 201.7,95.7 203.1,94.9 204.5,94.1 206.0,93.4 207.4,92.7 208.8,92.1 210.2,91.5 211.7,90.9 213.1,90.4 214.5,90.0 216.0,89.7 217.4,89.5 218.8,89.3 220.3,89.3 221.7,89.3 223.1,89.4 224.6,89.7 226.0,90.0 227.4,90.4 228.8,90.9 230.3,91.5 231.7,92.2 233.1,92.9 234.6,93.8 236.0,94.7 237.4,95.6 238.9,96.6 240.3,97.6 241.7,98.7 243.2,99.8 244.6,101.0 246.0,102.1 247.4,103.3 248.9,104.5 250.3,105.7 251.7,106.9 253.2,108.1 254.6,109.3 256.0,110.5 257.5,111.6 258.9,112.8 260.3,114.0 261.8,115.1 263.2,116.2 264.6,117.3 266.0,118.4 267.5,119.5 268.9,120.6 270.3,121.6 271.8,122.7 273.2,123.7 274.6,124.7 276.1,125.6 277.5,126.6 278.9,127.5 280.3,128.5 281.8,129.4 283.2,130.3 284.6,131.1 286.1,132.0 287.5,132.8 288.9,133.6 290.4,134.5 291.8,135.2 293.2,136.0 294.7,136.8 296.1,137.5 297.5,138.3 298.9,139.0 300.4,139.7 301.8,140.4 303.2,141.1 304.7,141.8 306.1,142.5 307.5,143.1 309.0,143.8 310.4,144.4 311.8,145.0 313.2,145.6 314.7,146.2 316.1,146.8 317.5,147.4 319.0,148.0 320.4,148.6 321.8,149.1 323.3,149.7 324.7,150.2 326.1,150.8 327.6,151.3 329.0,151.8 330.4,152.3 331.8,152.9 333.3,153.4 334.7,153.9 336.1,154.4 337.6,154.8 339.0,155.3 340.4,155.8 341.9,156.3 343.3,156.8 344.7,157.2 346.2,157.7 347.6,158.1 349.0,158.6 350.4,159.0 351.9,159.5 353.3,159.9 354.7,160.4 356.2,160.8 357.6,161.3 359.0,161.7 360.5,162.1 361.9,162.6 363.3,163.0 364.8,163.4 366.2,163.8 367.6,164.3 369.0,164.7 370.5,165.1 371.9,165.5 373.3,166.0 374.8,166.4 376.2,166.8 377.6,167.2 379.1,167.7 380.5,168.1 381.9,168.5 383.3,169.0 384.8,169.4 386.2,169.9 387.6,170.3 389.1,170.8 390.5,171.2 391.9,171.7 393.4,172.2 394.8,172.7 396.2,173.2 397.7,173.7 399.1,174.2 400.5,174.8 401.9,175.4 403.4,176.0 404.8,176.6 406.2,177.3 407.7,178.0 409.1,178.8 410.5,179.7 412.0,180.7 413.4,182.0 414.8,183.7 416.2,190.0 417.7,183.8 419.1,182.1 420.5,181.0 422.0,180.1 423.4,179.3 424.8,178.7 426.3,178.1 427.7,177.6 429.1,177.2 430.6,176.8 432.0,176.4 433.4,176.0 434.8,175.7 436.3,175.4 437.7,175.1 439.1,174.8 440.6,174.6 442.0,174.3 443.4,174.1 444.9,173.9 446.3,173.7 447.7,173.5 449.2,173.3 450.6,173.1 452.0,173.0 453.4,172.8 454.9,172.7 456.3,172.5 457.7,172.4 459.2,172.2 460.6,172.1 462.0,172.0 463.5,171.9 464.9,171.7 466.3,171.6 467.8,171.5 469.2,171.4 470.6,171.3 472.0,171.2 473.5,171.1 474.9,171.1 476.3,171.0 477.8,170.9 479.2,170.8 480.6,170.7 482.1,170.7 483.5,170.6 484.9,170.5 486.3,170.5 487.8,170.4 489.2,170.3 490.6,170.3 492.1,170.2 493.5,170.2 494.9,170.1 496.4,170.0 497.8,170.0 499.2,169.9 500.7,169.9 502.1,169.9 503.5,169.8 504.9,169.8 506.4,169.7 507.8,169.7 509.2,169.6 510.7,169.6 512.1,169.6 513.5,169.5 515.0,169.5 516.4,169.5 517.8,169.4 519.2,169.4 520.7,169.4 522.1,169.3 523.5,169.3 525.0,169.3 526.4,169.3 527.8,169.2 529.3,169.2 530.7,169.2 532.1,169.2 533.6,169.1 535.0,169.1 536.4,169.1 537.8,169.1 539.3,169.1 540.7,169.0 542.1,169.0 543.6,169.0 545.0,169.0" fill="none" stroke="#1e8449" stroke-width="2" clip-path="url(#clip-reciclado)"/>
</svg>
</div>

### ✍️ Tu turno 8 — 2025-1C rec Ej3b · 10 min

Graficá el corte por el eje real de $|G(s)|$ para la $G$ del Tu turno 2:

$$
G(s)=\frac{2\,(s+3)}{(s+2)(s^2+8s+17)}
$$

<details>
<summary>Corrección (RESOLUCIONES-2025, recuperatorio Ej3b)</summary>

Gráfico de la hoja oficial: tiende a $\infty$ en $\sigma=-2$ (polo real), se anula en $\sigma=-3$ (cero), tiene un lomo finito centrado en $\sigma=-4$ (rotulado "polos complejos conjugados") y decae hacia los dos extremos.

<div class="fig" style="margin:0.6rem 0; page-break-inside: avoid;">
<svg viewBox="0 0 560 230" width="100%" style="max-width:560px" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<defs><clipPath id="clip-recEj3b"><rect x="30" y="22" width="515" height="168"/></clipPath></defs>
<text x="30" y="14" fill="currentColor" font-size="12">|G(σ)| de G(s) = 2(s+3)/((s+2)(s²+8s+17))</text>
<line x1="30" y1="190.0" x2="545" y2="190.0" stroke="currentColor" stroke-width="1"/>
<text x="537" y="218.0" fill="currentColor">σ</text>
<line x1="404.5" y1="22" x2="404.5" y2="190.0" stroke="currentColor" stroke-width="0.6" stroke-dasharray="1 3"/>
<line x1="310.9" y1="22" x2="310.9" y2="190.0" stroke="#c0392b" stroke-width="1" stroke-dasharray="5 4"/>
<line x1="217.3" y1="187.0" x2="217.3" y2="193.0" stroke="currentColor"/>
<text x="217.3" y="206.0" fill="currentColor" text-anchor="middle">−4</text>
<line x1="264.1" y1="187.0" x2="264.1" y2="193.0" stroke="currentColor"/>
<text x="264.1" y="206.0" fill="currentColor" text-anchor="middle">−3</text>
<line x1="310.9" y1="187.0" x2="310.9" y2="193.0" stroke="currentColor"/>
<text x="310.9" y="206.0" fill="currentColor" text-anchor="middle">−2</text>
<line x1="404.5" y1="187.0" x2="404.5" y2="193.0" stroke="currentColor"/>
<text x="404.5" y="206.0" fill="currentColor" text-anchor="middle">0</text>
<circle cx="264.1" cy="190.0" r="4" fill="none" stroke="#2471a3" stroke-width="1.5"/>
<text x="310.9" y="220.0" fill="#c0392b" text-anchor="middle" font-size="11">polo</text>
<text x="264.1" y="220.0" fill="#2471a3" text-anchor="middle" font-size="11">cero</text>
<text x="217.3" y="220.0" fill="#7d3c98" text-anchor="middle" font-size="11">lomo</text>
<polyline points="30.0,178.5 31.4,178.4 32.9,178.2 34.3,178.1 35.7,177.9 37.2,177.7 38.6,177.6 40.0,177.4 41.4,177.2 42.9,177.0 44.3,176.8 45.7,176.6 47.2,176.5 48.6,176.3 50.0,176.1 51.5,175.9 52.9,175.6 54.3,175.4 55.7,175.2 57.2,175.0 58.6,174.8 60.0,174.5 61.5,174.3 62.9,174.0 64.3,173.8 65.8,173.5 67.2,173.3 68.6,173.0 70.1,172.7 71.5,172.4 72.9,172.2 74.3,171.9 75.8,171.6 77.2,171.3 78.6,170.9 80.1,170.6 81.5,170.3 82.9,169.9 84.4,169.6 85.8,169.2 87.2,168.9 88.7,168.5 90.1,168.1 91.5,167.7 92.9,167.3 94.4,166.9 95.8,166.5 97.2,166.0 98.7,165.6 100.1,165.1 101.5,164.7 103.0,164.2 104.4,163.7 105.8,163.2 107.3,162.7 108.7,162.1 110.1,161.6 111.5,161.0 113.0,160.4 114.4,159.8 115.8,159.2 117.3,158.6 118.7,157.9 120.1,157.3 121.6,156.6 123.0,155.9 124.4,155.1 125.8,154.4 127.3,153.6 128.7,152.8 130.1,152.0 131.6,151.2 133.0,150.3 134.4,149.5 135.9,148.6 137.3,147.6 138.7,146.7 140.2,145.7 141.6,144.7 143.0,143.7 144.4,142.6 145.9,141.5 147.3,140.4 148.7,139.3 150.2,138.1 151.6,136.9 153.0,135.7 154.5,134.4 155.9,133.2 157.3,131.9 158.8,130.5 160.2,129.2 161.6,127.8 163.0,126.4 164.5,125.0 165.9,123.5 167.3,122.0 168.8,120.5 170.2,119.0 171.6,117.5 173.1,116.0 174.5,114.5 175.9,112.9 177.3,111.4 178.8,109.9 180.2,108.3 181.6,106.8 183.1,105.3 184.5,103.9 185.9,102.4 187.4,101.0 188.8,99.7 190.2,98.4 191.7,97.1 193.1,96.0 194.5,94.9 195.9,93.8 197.4,92.9 198.8,92.0 200.2,91.3 201.7,90.6 203.1,90.1 204.5,89.7 206.0,89.4 207.4,89.3 208.8,89.3 210.2,89.5 211.7,89.8 213.1,90.2 214.5,90.9 216.0,91.7 217.4,92.7 218.8,93.8 220.3,95.1 221.7,96.6 223.1,98.3 224.6,100.1 226.0,102.2 227.4,104.3 228.8,106.7 230.3,109.2 231.7,111.8 233.1,114.6 234.6,117.5 236.0,120.6 237.4,123.7 238.9,127.0 240.3,130.3 241.7,133.7 243.2,137.2 244.6,140.7 246.0,144.3 247.4,147.9 248.9,151.5 250.3,155.1 251.7,158.8 253.2,162.4 254.6,166.1 256.0,169.7 257.5,173.3 258.9,176.9 260.3,180.5 261.8,184.1 263.2,187.7 264.6,188.7 266.0,185.1 267.5,181.5 268.9,177.9 270.3,174.3 271.8,170.6 273.2,166.9 274.6,163.1 276.1,159.3 277.5,155.3 278.9,151.3 280.3,147.1 281.8,142.8 283.2,138.3 284.6,133.6 286.1,128.6 287.5,123.4 288.9,117.9 290.4,112.1 291.8,105.8 293.2,99.2 294.7,92.0 296.1,84.4 297.5,76.1 298.9,67.3 300.4,57.8 301.8,47.7 303.2,36.9 304.7,25.6 306.1,13.7 307.5,1.4 309.0,-11.2 309.5,-16.0 310.0,-20.1 310.4,-23.8 310.4,-24.3 310.7,-26.3 310.8,-27.6 310.9,-28.0 310.9,-28.3 310.9,-28.4 310.9,-28.4" fill="none" stroke="#1e8449" stroke-width="2" clip-path="url(#clip-recEj3b)"/>
<polyline points="310.9,-28.4 310.9,-28.4 310.9,-28.3 311.0,-28.0 311.0,-27.6 311.1,-26.3 311.4,-24.3 311.8,-20.4 311.8,-20.2 312.3,-16.1 313.2,-8.1 314.7,3.7 316.1,15.1 317.5,25.8 319.0,35.8 320.4,45.2 321.8,53.8 323.3,61.8 324.7,69.1 326.1,75.8 327.6,82.0 329.0,87.7 330.4,93.0 331.8,97.8 333.3,102.2 334.7,106.3 336.1,110.1 337.6,113.7 339.0,116.9 340.4,120.0 341.9,122.8 343.3,125.5 344.7,128.0 346.2,130.3 347.6,132.5 349.0,134.5 350.4,136.4 351.9,138.3 353.3,140.0 354.7,141.6 356.2,143.2 357.6,144.6 359.0,146.0 360.5,147.3 361.9,148.6 363.3,149.8 364.8,150.9 366.2,152.0 367.6,153.0 369.0,154.0 370.5,155.0 371.9,155.9 373.3,156.7 374.8,157.6 376.2,158.4 377.6,159.2 379.1,159.9 380.5,160.6 381.9,161.3 383.3,162.0 384.8,162.6 386.2,163.2 387.6,163.8 389.1,164.4 390.5,164.9 391.9,165.4 393.4,166.0 394.8,166.5 396.2,166.9 397.7,167.4 399.1,167.9 400.5,168.3 401.9,168.7 403.4,169.1 404.8,169.5 406.2,169.9 407.7,170.3 409.1,170.6 410.5,171.0 412.0,171.3 413.4,171.7 414.8,172.0 416.2,172.3 417.7,172.6 419.1,172.9 420.5,173.2 422.0,173.5 423.4,173.8 424.8,174.0 426.3,174.3 427.7,174.6 429.1,174.8 430.6,175.1 432.0,175.3 433.4,175.5 434.8,175.7 436.3,176.0 437.7,176.2 439.1,176.4 440.6,176.6 442.0,176.8 443.4,177.0 444.9,177.2 446.3,177.4 447.7,177.6 449.2,177.7 450.6,177.9 452.0,178.1 453.4,178.2 454.9,178.4 456.3,178.6 457.7,178.7 459.2,178.9 460.6,179.0 462.0,179.2 463.5,179.3 464.9,179.5 466.3,179.6 467.8,179.7 469.2,179.9 470.6,180.0 472.0,180.1 473.5,180.3 474.9,180.4 476.3,180.5 477.8,180.6 479.2,180.7 480.6,180.8 482.1,181.0 483.5,181.1 484.9,181.2 486.3,181.3 487.8,181.4 489.2,181.5 490.6,181.6 492.1,181.7 493.5,181.8 494.9,181.9 496.4,182.0 497.8,182.1 499.2,182.1 500.7,182.2 502.1,182.3 503.5,182.4 504.9,182.5 506.4,182.6 507.8,182.7 509.2,182.7 510.7,182.8 512.1,182.9 513.5,183.0 515.0,183.0 516.4,183.1 517.8,183.2 519.2,183.3 520.7,183.3 522.1,183.4 523.5,183.5 525.0,183.5 526.4,183.6 527.8,183.7 529.3,183.7 530.7,183.8 532.1,183.9 533.6,183.9 535.0,184.0 536.4,184.0 537.8,184.1 539.3,184.2 540.7,184.2 542.1,184.3 543.6,184.3 545.0,184.4" fill="none" stroke="#1e8449" stroke-width="2" clip-path="url(#clip-recEj3b)"/>
</svg>
</div>

</details>

### ✍️ Tu turno 9 — R-F, el corte · 10 min

Volvé a R-F y hacé el corte por el eje real que dejaste pendiente. Corregí con la hoja de práctica.

### ✍️ Tu turno 10 — 2022-10-11 Ej5b · 10 min

Con la $G$ del Tu turno 4 ($k=6$) y entrada **escalón unitario**, dibujá el corte por el eje real de $|Y(s)|$.

<details>
<summary>Corrección (resuelto para esta guía, verificado con sympy)</summary>

$$
Y(s)=G(s)\cdot\frac1s=\frac{17\,(s+3)}{s\,(s^2+8s+17)}
$$

Hitos: **asíntota vertical en $0$** (el polo que agregó el escalón), toca el eje en $-3$ (cero), lomo en $-4$ (parte real de $-4\pm j$), pegada al eje en los extremos.

<div class="fig" style="margin:0.6rem 0; page-break-inside: avoid;">
<svg viewBox="0 0 560 230" width="100%" style="max-width:560px" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<defs><clipPath id="clip-ej5_2022"><rect x="30" y="22" width="515" height="168"/></clipPath></defs>
<text x="30" y="14" fill="currentColor" font-size="12">|Y(σ)| de Y(s) = 17(s+3)/(s(s²+8s+17))</text>
<line x1="30" y1="190.0" x2="545" y2="190.0" stroke="currentColor" stroke-width="1"/>
<text x="537" y="218.0" fill="currentColor">σ</text>
<line x1="404.5" y1="22" x2="404.5" y2="190.0" stroke="currentColor" stroke-width="0.6" stroke-dasharray="1 3"/>
<line x1="404.5" y1="22" x2="404.5" y2="190.0" stroke="#c0392b" stroke-width="1" stroke-dasharray="5 4"/>
<line x1="217.3" y1="187.0" x2="217.3" y2="193.0" stroke="currentColor"/>
<text x="217.3" y="206.0" fill="currentColor" text-anchor="middle">−4</text>
<line x1="264.1" y1="187.0" x2="264.1" y2="193.0" stroke="currentColor"/>
<text x="264.1" y="206.0" fill="currentColor" text-anchor="middle">−3</text>
<line x1="404.5" y1="187.0" x2="404.5" y2="193.0" stroke="currentColor"/>
<text x="404.5" y="206.0" fill="currentColor" text-anchor="middle">0</text>
<circle cx="264.1" cy="190.0" r="4" fill="none" stroke="#2471a3" stroke-width="1.5"/>
<text x="404.5" y="220.0" fill="#c0392b" text-anchor="middle" font-size="11">polo</text>
<text x="264.1" y="220.0" fill="#2471a3" text-anchor="middle" font-size="11">cero</text>
<text x="217.3" y="220.0" fill="#7d3c98" text-anchor="middle" font-size="11">lomo</text>
<polyline points="30.0,173.8 31.4,173.6 32.9,173.4 34.3,173.2 35.7,173.0 37.2,172.7 38.6,172.5 40.0,172.3 41.4,172.1 42.9,171.9 44.3,171.6 45.7,171.4 47.2,171.2 48.6,170.9 50.0,170.7 51.5,170.4 52.9,170.1 54.3,169.9 55.7,169.6 57.2,169.3 58.6,169.1 60.0,168.8 61.5,168.5 62.9,168.2 64.3,167.9 65.8,167.6 67.2,167.2 68.6,166.9 70.1,166.6 71.5,166.2 72.9,165.9 74.3,165.6 75.8,165.2 77.2,164.8 78.6,164.4 80.1,164.1 81.5,163.7 82.9,163.3 84.4,162.9 85.8,162.4 87.2,162.0 88.7,161.6 90.1,161.1 91.5,160.7 92.9,160.2 94.4,159.7 95.8,159.2 97.2,158.7 98.7,158.2 100.1,157.7 101.5,157.2 103.0,156.6 104.4,156.0 105.8,155.5 107.3,154.9 108.7,154.3 110.1,153.7 111.5,153.0 113.0,152.4 114.4,151.7 115.8,151.0 117.3,150.4 118.7,149.6 120.1,148.9 121.6,148.2 123.0,147.4 124.4,146.6 125.8,145.8 127.3,145.0 128.7,144.2 130.1,143.3 131.6,142.4 133.0,141.6 134.4,140.6 135.9,139.7 137.3,138.7 138.7,137.8 140.2,136.8 141.6,135.7 143.0,134.7 144.4,133.6 145.9,132.5 147.3,131.4 148.7,130.3 150.2,129.2 151.6,128.0 153.0,126.8 154.5,125.6 155.9,124.4 157.3,123.1 158.8,121.8 160.2,120.6 161.6,119.3 163.0,118.0 164.5,116.6 165.9,115.3 167.3,114.0 168.8,112.6 170.2,111.3 171.6,109.9 173.1,108.6 174.5,107.2 175.9,105.9 177.3,104.6 178.8,103.3 180.2,102.0 181.6,100.8 183.1,99.6 184.5,98.4 185.9,97.2 187.4,96.1 188.8,95.1 190.2,94.1 191.7,93.2 193.1,92.4 194.5,91.7 195.9,91.0 197.4,90.4 198.8,90.0 200.2,89.6 201.7,89.4 203.1,89.3 204.5,89.3 206.0,89.5 207.4,89.8 208.8,90.2 210.2,90.9 211.7,91.7 213.1,92.6 214.5,93.7 216.0,95.0 217.4,96.5 218.8,98.2 220.3,100.0 221.7,102.0 223.1,104.2 224.6,106.6 226.0,109.1 227.4,111.7 228.8,114.5 230.3,117.5 231.7,120.5 233.1,123.7 234.6,126.9 236.0,130.2 237.4,133.6 238.9,137.0 240.3,140.4 241.7,143.9 243.2,147.3 244.6,150.7 246.0,154.1 247.4,157.4 248.9,160.7 250.3,163.8 251.7,167.0 253.2,170.0 254.6,172.9 256.0,175.8 257.5,178.5 258.9,181.2 260.3,183.7 261.8,186.2 263.2,188.5 264.6,189.2 266.0,187.0 267.5,184.9 268.9,182.9 270.3,181.0 271.8,179.1 273.2,177.4 274.6,175.7 276.1,174.0 277.5,172.5 278.9,171.0 280.3,169.5 281.8,168.1 283.2,166.8 284.6,165.5 286.1,164.2 287.5,163.0 288.9,161.9 290.4,160.7 291.8,159.6 293.2,158.6 294.7,157.5 296.1,156.5 297.5,155.5 298.9,154.6 300.4,153.6 301.8,152.7 303.2,151.8 304.7,150.9 306.1,150.0 307.5,149.1 309.0,148.2 310.4,147.4 311.8,146.5 313.2,145.7 314.7,144.8 316.1,143.9 317.5,143.1 319.0,142.2 320.4,141.4 321.8,140.5 323.3,139.6 324.7,138.7 326.1,137.8 327.6,136.9 329.0,136.0 330.4,135.0 331.8,134.1 333.3,133.1 334.7,132.1 336.1,131.1 337.6,130.0 339.0,128.9 340.4,127.8 341.9,126.7 343.3,125.5 344.7,124.3 346.2,123.0 347.6,121.7 349.0,120.4 350.4,119.0 351.9,117.6 353.3,116.1 354.7,114.5 356.2,112.9 357.6,111.2 359.0,109.4 360.5,107.6 361.9,105.7 363.3,103.6 364.8,101.5 366.2,99.3 367.6,97.0 369.0,94.5 370.5,92.0 371.9,89.3 373.3,86.4 374.8,83.4 376.2,80.3 377.6,76.9 379.1,73.4 380.5,69.7 381.9,65.8 383.3,61.7 384.8,57.3 386.2,52.7 387.6,47.8 389.1,42.7 390.5,37.3 391.9,31.7 393.4,25.8 394.8,19.6 396.2,13.2 397.7,6.5 399.1,-0.4 400.5,-7.5 401.9,-14.8 403.1,-21.0 403.4,-22.3 403.6,-23.5 404.1,-25.9 404.3,-27.2 404.5,-27.9 404.5,-28.2 404.5,-28.3 404.5,-28.4 404.5,-28.4" fill="none" stroke="#1e8449" stroke-width="2" clip-path="url(#clip-ej5_2022)"/>
<polyline points="404.5,-28.4 404.6,-28.4 404.6,-28.3 404.6,-28.2 404.6,-27.9 404.8,-27.2 404.8,-27.0 405.0,-25.9 405.5,-23.4 405.9,-21.0 406.2,-19.5 407.7,-11.9 409.1,-4.3 410.5,3.2 412.0,10.5 413.4,17.7 414.8,24.7 416.2,31.5 417.7,38.0 419.1,44.3 420.5,50.4 422.0,56.1 423.4,61.6 424.8,66.8 426.3,71.8 427.7,76.5 429.1,81.0 430.6,85.2 432.0,89.2 433.4,93.0 434.8,96.6 436.3,99.9 437.7,103.1 439.1,106.2 440.6,109.1 442.0,111.8 443.4,114.4 444.9,116.8 446.3,119.2 447.7,121.4 449.2,123.5 450.6,125.5 452.0,127.4 453.4,129.2 454.9,131.0 456.3,132.6 457.7,134.2 459.2,135.7 460.6,137.2 462.0,138.6 463.5,139.9 464.9,141.2 466.3,142.4 467.8,143.6 469.2,144.7 470.6,145.8 472.0,146.8 473.5,147.8 474.9,148.8 476.3,149.7 477.8,150.6 479.2,151.4 480.6,152.3 482.1,153.1 483.5,153.8 484.9,154.6 486.3,155.3 487.8,156.0 489.2,156.7 490.6,157.3 492.1,158.0 493.5,158.6 494.9,159.2 496.4,159.8 497.8,160.3 499.2,160.9 500.7,161.4 502.1,161.9 503.5,162.4 504.9,162.9 506.4,163.4 507.8,163.8 509.2,164.3 510.7,164.7 512.1,165.1 513.5,165.5 515.0,165.9 516.4,166.3 517.8,166.7 519.2,167.0 520.7,167.4 522.1,167.8 523.5,168.1 525.0,168.4 526.4,168.8 527.8,169.1 529.3,169.4 530.7,169.7 532.1,170.0 533.6,170.3 535.0,170.5 536.4,170.8 537.8,171.1 539.3,171.4 540.7,171.6 542.1,171.9 543.6,172.1 545.0,172.4" fill="none" stroke="#1e8449" stroke-width="2" clip-path="url(#clip-ej5_2022)"/>
</svg>
</div>

</details>

**Errores típicos de §6:** poner el lomo en $0$ en vez de en la parte real de los polos; dibujar la curva cruzando el eje en un cero; poner asíntotas en los polos complejos; marcar ceros complejos; graficar $|G|$ cuando pedían $|Y|$ (te falta el polo del escalón).

---

## 7. Respuesta temporal: $Y=G\cdot F$ (≈ 2 h 30)

Es el ítem que más se repite (14 de 16 hojas) y el que más tiempo lleva. Es mecánico: siempre los mismos pasos.

### Las entradas 🧠

| Entrada $f(t)$ | $F(s)$ | Qué queda |
|---|---|---|
| Impulso $\delta(t)$ | $1$ | $Y=G$ ("respuesta natural") |
| Escalón unitario $E(t)$ | $\dfrac1s$ | $Y=\dfrac{G}{s}$: aparece un $\dfrac{A}{s}$ |
| $e^{-at}$ | $\dfrac1{s+a}$ | suele **cancelar** un cero de $G$ |
| $-e^{-t}$ | $-\dfrac1{s+1}$ | ídem, con el signo |

"La entrada suele estar pensada para simplificar algo con la transferencia" (apunte `13`, [1:12:28]).

### Receta 🧠

1. Partí de la $G$ **simplificada** (con el $K$ ya hallado).
2. Transformá la entrada: $F(s)$.
3. $Y(s)=G(s)\cdot F(s)$. **Cancelá** lo que se cancele.
4. Planteá fracciones simples: $\frac{A}{s-p}$ por cada polo real, $\frac{Bs+C}{\text{cuadrático}}$ por cada par complejo.
5. Constantes de polos reales **por tapado**; $B$ y $C$ **igualando coeficientes** (cuadráticos, lineales; los independientes de control).
6. Completá cuadrados: $(s+a)^2+b^2$.
7. **Prestá:** $Bs+C=B\,(s+a)+(C-Ba)$.
8. Antitransformá con la tabla y la traslación.
9. **Control (con el teorema del valor inicial, que está en el ayudamemoria):** $y(0)=\lim_{s\to\infty}s\,Y(s)$. Cuando el grado de abajo de $Y$ supera en 2 o más al de arriba, da **$y(0)=0$**: reemplazá $t=0$ en tu respuesta ($e^0=1$, $\cos0=1$, $\operatorname{sen}0=0$) y fijate que dé $0$. Si no da, hay un error de cuentas. (Control agregado en esta guía; vale para todos los ejercicios de esta guía salvo R-E.)

### Ejemplo guiado 7: el reciclado, ítem b (2025-1C T2 Ej3b) — respuesta al escalón

> Con $k=3$, hallar la respuesta temporal a una entrada escalón unitario $E(t)$.

**Paso 1 — $G$ simplificada** (de §5):

$$
G(s)=\frac{10\,(s-3)}{s^2+6s+10}
$$

**Paso 2 — entrada.** Escalón: $F(s)=\dfrac1s$.

**Paso 3 — salida.** No se cancela nada:

$$
Y(s)=\frac{10\,(s-3)}{s\,(s^2+6s+10)}
$$

**Paso 4 — forma.** El $s$ es un polo real; $s^2+6s+10$ no tiene raíces reales:

$$
Y(s)=\frac{A}{s}+\frac{Bs+C}{s^2+6s+10}
$$

**Paso 5 — constantes.** $A$ tapando la $s$ y evaluando en $0$:

$$
A=\frac{10\,(0-3)}{0+0+10}=-3
$$

Identidad de numeradores:

$$
-3\,(s^2+6s+10)+(Bs+C)\,s=10s-30
$$

- Cuadráticos: $-3+B=0\Rightarrow B=3$.
- Lineales: $-18+C=10\Rightarrow C=28$.
- Control, independientes: $-30=-30$ ✓.

**Paso 6 — completar cuadrados:** $s^2+6s+10=(s+3)^2+1$.

**Paso 7 — prestar.** Necesito $s+3$ arriba: $3s+28=3\,(s+3)+19$ (el $28$ le presta $9$ al $3s$ y se queda con $19$).

$$
Y(s)=-\frac3s+3\cdot\frac{s+3}{(s+3)^2+1}+19\cdot\frac{1}{(s+3)^2+1}
$$

**Paso 8 — antitransformar:**

$$
\boxed{\,y(t)=-3+3\cos(t)\,e^{-3t}+19\operatorname{sen}(t)\,e^{-3t}\,}
$$

Es exactamente la respuesta oficial.

**Paso 9 — control:** $y(0)=-3+3\cdot1+19\cdot0=0$ ✓.

### Ejemplo guiado 8: entrada exponencial (apunte `13`, ejercicio 7)

> $G(s)=\dfrac{s^2+2s}{s^3-2s^2-3s}$. Hallar $y(t)$ para $f(t)=e^{-2t}$.

**Paso 1 — simplificar.** Factor común $s$ arriba y abajo, se cancela:

$$
G(s)=\frac{s+2}{(s+1)(s-3)}
$$

**Paso 2 y 3 — entrada y salida.** $F(s)=\dfrac1{s+2}$, que **cancela el cero** en $-2$:

$$
Y(s)=\frac{1}{(s+1)(s-3)}=\frac{A}{s+1}+\frac{B}{s-3}
$$

**Paso 5 — tapado:** $A=\dfrac{1}{-1-3}=-\dfrac14$, $B=\dfrac{1}{3+1}=\dfrac14$.

$$
y(t)=-\frac14\,e^{-t}+\frac14\,e^{3t}
$$

Como hay $e^{3t}$, $y(t)\to\infty$: el sistema es **inestable** (en el video el profe dice "estable" y se corrige enseguida). Este ejemplo muestra el patrón "la entrada cancela algo" con cuentas cortas; en el parcial el $G$ ya viene estable o lo hiciste estable con $K$.

### ✍️ Tu turno 11 — 2024-1C T2 Ej4b · 25 min (impulso)

Con la $G$ del Tu turno 5 ($k=1$), hallá la respuesta temporal a $f(t)=\delta(t)$.

<details>
<summary>Corrección (resuelto para esta guía, verificado con sympy)</summary>

Impulso: $F=1$, $Y=G$:

$$
Y(s)=\frac{5\,(s+1)}{(s+3)(s^2+2s+2)}=\frac{A}{s+3}+\frac{Bs+C}{s^2+2s+2}
$$

Tapando en $s=-3$: $A=\dfrac{5\,(-2)}{9-6+2}=-2$.

Identidad $-2\,(s^2+2s+2)+(Bs+C)(s+3)=5s+5$: cuadráticos $-2+B=0\Rightarrow B=2$; independientes $-4+3C=5\Rightarrow C=3$ (control, lineales: $-4+3B+C=-4+6+3=5$ ✓).

$s^2+2s+2=(s+1)^2+1$; prestar: $2s+3=2\,(s+1)+1$.

$$
Y(s)=-\frac{2}{s+3}+2\cdot\frac{s+1}{(s+1)^2+1}+\frac{1}{(s+1)^2+1}
$$

$$
\boxed{\,y(t)=-2\,e^{-3t}+2\cos(t)\,e^{-t}+\operatorname{sen}(t)\,e^{-t}\,}
$$

Control: $y(0)=-2+2=0$ ✓.

</details>

### ✍️ Tu turno 12 — 2024-2C T2 Ej4b · 25 min (exponencial)

Misma $G$ ($k=1$). Hallá la respuesta a la entrada $f(t)=e^{-t}$.

<details>
<summary>Corrección (resuelto para esta guía, verificado con sympy)</summary>

$F(s)=\dfrac1{s+1}$: **cancela el cero** en $-1$.

$$
Y(s)=\frac{5}{(s+3)(s^2+2s+2)}=\frac{A}{s+3}+\frac{Bs+C}{s^2+2s+2}
$$

(Es la $Y$ de la hoja de respuestas oficial.) Tapando: $A=\dfrac{5}{9-6+2}=1$.

Identidad $(s^2+2s+2)+(Bs+C)(s+3)=5$: cuadráticos $1+B=0\Rightarrow B=-1$; independientes $2+3C=5\Rightarrow C=1$.

Prestar: $-s+1=-(s+1)+2$.

$$
Y(s)=\frac1{s+3}-\frac{s+1}{(s+1)^2+1}+\frac{2}{(s+1)^2+1}
$$

$$
\boxed{\,y(t)=e^{-3t}-\cos(t)\,e^{-t}+2\operatorname{sen}(t)\,e^{-t}\,}
$$

Control: $y(0)=1-1=0$ ✓.

</details>

### ✍️ Tu turno 13 — R-F b) y R-G de tu hoja · 50 min

Primero **R-F b)** (impulso, 25 min) y después **R-G** (entrada $e^{-3t}$, 25 min). Los dos son ejercicios de parcial textuales. Corregí con la hoja de práctica.

### ✍️ Tu turno 14 (si vas bien de tiempo) — 2022-10-11 Ej5c · 20 min

Con $k=6$ y entrada escalón unitario, hallá $y(t)$. Ya tenés $Y(s)$ del Tu turno 10.

<details>
<summary>Corrección (resuelto para esta guía, verificado con sympy)</summary>

$$
Y(s)=\frac{17\,(s+3)}{s\,(s^2+8s+17)}=\frac{A}{s}+\frac{Bs+C}{s^2+8s+17},\qquad A=\frac{17\cdot3}{17}=3
$$

Identidad $3\,(s^2+8s+17)+(Bs+C)\,s=17s+51$: cuadráticos $B=-3$; lineales $24+C=17\Rightarrow C=-7$.

$(s+4)^2+1$; prestar: $-3s-7=-3\,(s+4)+5$.

$$
\boxed{\,y(t)=3-3\cos(t)\,e^{-4t}+5\operatorname{sen}(t)\,e^{-4t}\,}
$$

Control: $y(0)=3-3=0$ ✓. Oscilatoria amortiguada, valor estable $3$.

</details>

**Errores típicos de §7:** usar $G$ sin simplificar; olvidarte de multiplicar por $F$; no prestar y antitransformar $\frac{3s+28}{(s+3)^2+1}$ "a ojo"; confundir el signo de la traslación ($s+3\leftrightarrow e^{-3t}$, no $e^{3t}$); olvidar el factor $\frac1b$ cuando $b\ne1$; no hacer el control $y(0)=0$.

---

## 8. Tipo de respuesta y valor estable (≈ 45 min)

"Decir el tipo de respuesta es algo muy típico que se pida" (apunte `13`, [1:50:15]).

### Tipo de respuesta 🧠

Se lee de los términos de $y(t)$ (o directamente de los polos de $Y$, con la tabla de §4):

- Hay $\cos/\operatorname{sen}$ por una exponencial decreciente → **oscilatoria amortiguada**. "Lo importante que me diga es oscilatoria amortiguada" (apunte `10`, [1:47:54]).
- Solo exponenciales decrecientes → **exponencial decreciente**.
- $\cos/\operatorname{sen}$ sin exponencial → **oscilatoria de amplitud constante**.
- Algo con exponente positivo → **creciente** (exponencial u oscilatoria): inestable.
- Si además hay una constante, la respuesta está **desplazada** esa cantidad.

**Tipo ≠ estabilidad.** Si el enunciado dice "indicar el tipo de respuesta (no si es estable, sino el tipo)", contestá con el **nombre**, no con "estable".

Por si aparece, el **factor de amortiguamiento** $\alpha$ es el número que multiplica a $-t$ en la exponencial, dado **en positivo**: en $4\operatorname{sen}(3t)\,e^{-2t}$, $\alpha=2$. El profe lo considera "muy por arriba".

### Valor estable 🧠

Es el valor al que tiende $y(t)$ cuando $t\to\infty$. Tres formas, que dan lo mismo:

1. Mirando $y(t)$: todo lo que tiene $e^{-at}$ se va a $0$; queda la constante.
2. **Teorema del valor final** (está en el ayudamemoria):

$$
\text{V.E.}=\lim_{t\to\infty}y(t)=\lim_{s\to0}s\,Y(s)
$$

3. Con entrada escalón: es la $A$ de $\frac{A}{s}$, que es igual a $G(0)$.

Si no hay término $\frac{A}{s}$ (por ejemplo, impulso con una $G$ sin polo en $0$), el valor estable es $0$. Si el sistema es inestable, **no hay** valor estable.

### Ejemplo guiado 9: el reciclado, ítem c (2025-1C T2 Ej3c)

> Indicar el tipo de respuesta (no confundir con estabilidad) y el valor estable.

$$
y(t)=-3+3\cos(t)\,e^{-3t}+19\operatorname{sen}(t)\,e^{-3t}
$$

- **Tipo:** polos complejos conjugados con parte real negativa ($-3\pm j$): **oscilatoria amortiguada** (respuesta oficial).
- **Valor estable:** los términos con $e^{-3t}$ se van a $0$; queda **$-3$**. Por TVF: $\lim_{s\to0}s\cdot\dfrac{10(s-3)}{s(s^2+6s+10)}=\dfrac{-30}{10}=-3$ ✓.

### Ejemplo guiado 10: elegir la transferencia por el tipo y el valor estable (apuntes `05` y `11`, ejercicio 20)

> ¿Cuál corresponde a un sistema cuya respuesta al impulso es **oscilatoria amortiguada con valor estable 2**?

$$
G_1(s)=\frac{6}{s^2+9},\qquad G_2(s)=\frac{2}{s^2+6s+10},\qquad G_3(s)=\frac{6s+20}{s^3+6s^2+10s}
$$

Impulso, así que $Y_i=G_i$. Análisis de polos + TVF, sin antitransformar:

- **$G_1$:** polos $\pm3j$, imaginarios puros: $2\operatorname{sen}(3t)$, **amplitud constante**. No es amortiguada. Afuera.
- **$G_2$:** $(s+3)^2+1$: oscilatoria amortiguada ✓, pero nada la corre: valor estable $0$. Afuera.
- **$G_3$:** $s\,(s^2+6s+10)$: un $\frac{A}{s}$ (corre la respuesta) más un $\frac{Bs+C}{(s+3)^2+1}$ (oscila y se amortigua). TVF: $\lim_{s\to0}s\cdot G_3=\dfrac{20}{10}=2$ ✓. **Respuesta: $G_3$.** (Es la $Y$ de tu Tu turno 1: $y=2-2e^{-3t}\cos t$.)

### ✍️ Tu turno 15 — 2024-1C T1 Ej5 completo · 40 min (el integrador)

$$
G(s)=\frac{k\,(s^2-s-2)}{(s-2)(s^2+10s+26)}
$$

**a)** Hallá la constelación de polos y ceros de $G(s)$. **b)** Hallá $k$ para que $G(0)=2$. **c)** Con entrada escalón unitario $E(t)$, dibujá el corte por el eje real de $|Y(s)|$. **d)** Hallá $y(t)$ y clasificala (oscilatoria o exponencial, amortiguada o creciente); hallá, si existe, el valor estable.

<details>
<summary>Corrección (resuelto para esta guía, verificado con sympy)</summary>

**a)** $s^2-s-2=(s-2)(s+1)$: el $(s-2)$ se cancela (no es ni cero ni polo). $s^2+10s+26=(s+5)^2+1$.

$$
G(s)=\frac{k\,(s+1)}{s^2+10s+26}
$$

Ceros: $-1$, $\infty$. Polos: $-5\pm j$. (Estable.)

**b)** $G(0)=\dfrac{k}{26}=2\Rightarrow\boxed{k=52}$.

**c)** $Y(s)=\dfrac{52\,(s+1)}{s\,(s^2+10s+26)}$: asíntota vertical en $0$ (polo del escalón), toca el eje en $-1$, lomo en $-5$, pegada al eje en los extremos.

<div class="fig" style="margin:0.6rem 0; page-break-inside: avoid;">
<svg viewBox="0 0 560 230" width="100%" style="max-width:560px" xmlns="http://www.w3.org/2000/svg" font-family="sans-serif" font-size="12">
<defs><clipPath id="clip-ej5_2024"><rect x="30" y="22" width="515" height="168"/></clipPath></defs>
<text x="30" y="14" fill="currentColor" font-size="12">|Y(σ)| de Y(s) = 52(s+1)/(s(s²+10s+26))</text>
<line x1="30" y1="190.0" x2="545" y2="190.0" stroke="currentColor" stroke-width="1"/>
<text x="537" y="218.0" fill="currentColor">σ</text>
<line x1="416.2" y1="22" x2="416.2" y2="190.0" stroke="currentColor" stroke-width="0.6" stroke-dasharray="1 3"/>
<line x1="416.2" y1="22" x2="416.2" y2="190.0" stroke="#c0392b" stroke-width="1" stroke-dasharray="5 4"/>
<line x1="201.7" y1="187.0" x2="201.7" y2="193.0" stroke="currentColor"/>
<text x="201.7" y="206.0" fill="currentColor" text-anchor="middle">−5</text>
<line x1="373.3" y1="187.0" x2="373.3" y2="193.0" stroke="currentColor"/>
<text x="373.3" y="206.0" fill="currentColor" text-anchor="middle">−1</text>
<line x1="416.2" y1="187.0" x2="416.2" y2="193.0" stroke="currentColor"/>
<text x="416.2" y="206.0" fill="currentColor" text-anchor="middle">0</text>
<circle cx="373.3" cy="190.0" r="4" fill="none" stroke="#2471a3" stroke-width="1.5"/>
<text x="416.2" y="220.0" fill="#c0392b" text-anchor="middle" font-size="11">polo</text>
<text x="373.3" y="220.0" fill="#2471a3" text-anchor="middle" font-size="11">cero</text>
<text x="201.7" y="220.0" fill="#7d3c98" text-anchor="middle" font-size="11">lomo</text>
<polyline points="30.0,149.8 31.4,149.6 32.9,149.4 34.3,149.1 35.7,148.9 37.2,148.6 38.6,148.4 40.0,148.2 41.4,147.9 42.9,147.6 44.3,147.4 45.7,147.1 47.2,146.8 48.6,146.6 50.0,146.3 51.5,146.0 52.9,145.7 54.3,145.4 55.7,145.2 57.2,144.9 58.6,144.6 60.0,144.3 61.5,144.0 62.9,143.6 64.3,143.3 65.8,143.0 67.2,142.7 68.6,142.3 70.1,142.0 71.5,141.7 72.9,141.3 74.3,141.0 75.8,140.6 77.2,140.3 78.6,139.9 80.1,139.5 81.5,139.1 82.9,138.8 84.4,138.4 85.8,138.0 87.2,137.6 88.7,137.2 90.1,136.8 91.5,136.3 92.9,135.9 94.4,135.5 95.8,135.0 97.2,134.6 98.7,134.1 100.1,133.7 101.5,133.2 103.0,132.7 104.4,132.2 105.8,131.7 107.2,131.2 108.7,130.7 110.1,130.2 111.5,129.7 113.0,129.1 114.4,128.6 115.8,128.0 117.3,127.5 118.7,126.9 120.1,126.3 121.6,125.7 123.0,125.1 124.4,124.5 125.8,123.9 127.3,123.2 128.7,122.6 130.1,121.9 131.6,121.3 133.0,120.6 134.4,119.9 135.9,119.2 137.3,118.5 138.7,117.8 140.2,117.1 141.6,116.3 143.0,115.6 144.4,114.8 145.9,114.1 147.3,113.3 148.7,112.5 150.2,111.7 151.6,110.9 153.0,110.1 154.5,109.3 155.9,108.5 157.3,107.7 158.8,106.8 160.2,106.0 161.6,105.1 163.0,104.3 164.5,103.5 165.9,102.6 167.3,101.8 168.8,101.0 170.2,100.1 171.6,99.3 173.1,98.5 174.5,97.7 175.9,97.0 177.3,96.2 178.8,95.5 180.2,94.8 181.6,94.1 183.1,93.5 184.5,92.9 185.9,92.3 187.4,91.8 188.8,91.3 190.2,90.8 191.7,90.4 193.1,90.1 194.5,89.8 195.9,89.6 197.4,89.4 198.8,89.3 200.2,89.3 201.7,89.3 203.1,89.4 204.5,89.5 206.0,89.7 207.4,90.0 208.8,90.3 210.3,90.7 211.7,91.1 213.1,91.6 214.5,92.1 216.0,92.7 217.4,93.3 218.8,94.0 220.3,94.7 221.7,95.4 223.1,96.2 224.6,97.0 226.0,97.8 227.4,98.6 228.8,99.5 230.3,100.4 231.7,101.3 233.1,102.2 234.6,103.1 236.0,104.0 237.4,104.9 238.9,105.8 240.3,106.8 241.7,107.7 243.2,108.6 244.6,109.5 246.0,110.4 247.4,111.4 248.9,112.3 250.3,113.2 251.7,114.1 253.2,114.9 254.6,115.8 256.0,116.7 257.5,117.5 258.9,118.4 260.3,119.2 261.8,120.1 263.2,120.9 264.6,121.7 266.0,122.5 267.5,123.3 268.9,124.1 270.3,124.8 271.8,125.6 273.2,126.3 274.6,127.1 276.1,127.8 277.5,128.5 278.9,129.2 280.3,129.9 281.8,130.6 283.2,131.3 284.6,132.0 286.1,132.6 287.5,133.3 288.9,133.9 290.4,134.6 291.8,135.2 293.2,135.8 294.7,136.5 296.1,137.1 297.5,137.7 298.9,138.3 300.4,138.9 301.8,139.5 303.2,140.0 304.7,140.6 306.1,141.2 307.5,141.8 309.0,142.3 310.4,142.9 311.8,143.4 313.2,144.0 314.7,144.5 316.1,145.1 317.5,145.6 319.0,146.2 320.4,146.7 321.8,147.3 323.3,147.8 324.7,148.3 326.1,148.9 327.6,149.4 329.0,150.0 330.4,150.5 331.8,151.1 333.3,151.6 334.7,152.2 336.1,152.7 337.6,153.3 339.0,153.9 340.4,154.5 341.9,155.1 343.3,155.7 344.7,156.3 346.2,156.9 347.6,157.6 349.0,158.3 350.4,158.9 351.9,159.7 353.3,160.4 354.7,161.2 356.2,162.0 357.6,162.9 359.0,163.8 360.5,164.7 361.9,165.8 363.3,166.9 364.8,168.2 366.2,169.6 367.6,171.2 369.0,173.2 370.5,175.6 371.9,179.0 373.3,190.0 374.8,178.8 376.2,175.2 377.6,172.4 379.1,170.2 380.5,168.1 381.9,166.3 383.3,164.5 384.8,162.8 386.2,161.2 387.6,159.6 389.1,158.0 390.5,156.4 391.9,154.8 393.4,153.1 394.8,151.4 396.2,149.6 397.7,147.7 399.1,145.7 400.5,143.6 401.9,141.3 403.4,138.7 404.8,135.8 406.2,132.5 407.7,128.7 409.1,124.0 410.5,118.3 412.0,110.6 413.4,99.4 414.8,79.7 415.0,76.7 415.4,65.4 415.8,47.2 416.0,31.3 416.2,14.3 416.2,4.4 416.2,-7.9 416.2,-15.2 416.2,-20.2" fill="none" stroke="#1e8449" stroke-width="2" clip-path="url(#clip-ej5_2024)"/>
<polyline points="416.3,-20.2 416.3,-15.2 416.3,-7.9 416.3,4.4 416.3,14.2 416.5,31.1 416.7,46.9 417.1,64.7 417.5,75.7 417.7,78.6 419.1,97.2 420.5,107.4 422.0,114.2 423.4,119.2 424.8,123.1 426.3,126.2 427.7,128.8 429.1,131.0 430.6,132.9 432.0,134.6 433.4,136.1 434.8,137.4 436.3,138.6 437.7,139.6 439.1,140.6 440.6,141.5 442.0,142.4 443.4,143.2 444.9,143.9 446.3,144.6 447.7,145.2 449.2,145.9 450.6,146.4 452.0,147.0 453.4,147.5 454.9,148.0 456.3,148.5 457.7,148.9 459.2,149.3 460.6,149.7 462.0,150.1 463.5,150.5 464.9,150.9 466.3,151.3 467.8,151.6 469.2,151.9 470.6,152.2 472.0,152.6 473.5,152.9 474.9,153.2 476.3,153.4 477.8,153.7 479.2,154.0 480.6,154.2 482.1,154.5 483.5,154.7 484.9,155.0 486.3,155.2 487.8,155.5 489.2,155.7 490.6,155.9 492.1,156.1 493.5,156.3 494.9,156.5 496.4,156.7 497.8,156.9 499.2,157.1 500.7,157.3 502.1,157.5 503.5,157.7 504.9,157.9 506.4,158.1 507.8,158.2 509.2,158.4 510.7,158.6 512.1,158.7 513.5,158.9 515.0,159.1 516.4,159.2 517.8,159.4 519.2,159.5 520.7,159.7 522.1,159.8 523.5,160.0 525.0,160.1 526.4,160.3 527.8,160.4 529.3,160.6 530.7,160.7 532.1,160.8 533.6,161.0 535.0,161.1 536.4,161.2 537.8,161.4 539.3,161.5 540.7,161.6 542.1,161.7 543.6,161.9 545.0,162.0" fill="none" stroke="#1e8449" stroke-width="2" clip-path="url(#clip-ej5_2024)"/>
</svg>
</div>

**d)** $A=\dfrac{52}{26}=2$. Identidad $2\,(s^2+10s+26)+(Bs+C)\,s=52s+52$: cuadráticos $B=-2$; lineales $20+C=52\Rightarrow C=32$. Prestar: $-2s+32=-2\,(s+5)+42$.

$$
Y(s)=\frac2s-2\cdot\frac{s+5}{(s+5)^2+1}+42\cdot\frac{1}{(s+5)^2+1}
$$

$$
\boxed{\,y(t)=2-2\cos(t)\,e^{-5t}+42\operatorname{sen}(t)\,e^{-5t}\,}
$$

Control: $y(0)=2-2=0$ ✓. **Oscilatoria amortiguada**, **valor estable $2$** (coincide con $G(0)=2$, como tenía que ser con escalón).

</details>

**Errores típicos de §8:** contestar "estable" cuando piden el tipo; decir "oscilatoria" sin "amortiguada"; dar un valor estable para un sistema inestable; con impulso, inventar un $\frac{A}{s}$ que no existe.

---

## 9. $G(s)$ desde la ecuación diferencial: sistemas físicos (≈ 1 h)

El profe: "esto sí es un ejercicio de parcial o de final" (apunte `11`, [1:07:52]). Y "no es necesario saber física": la ecuación viene dada; alcanza con saber que **en reposo no te estás moviendo**.

### Receta 🧠

1. **Identificá** entrada (la fuerza $f$, la corriente $i$) y salida (la posición $y$, la tensión $v$).
2. **Reposo** ⇒ posición inicial $y(0)=0$ y velocidad inicial $y'(0)=0$.
3. **Laplace miembro a miembro.** La segunda derivada sale de aplicar dos veces la fórmula del ayudamemoria:

$$
\mathcal L[y'']=s\,\mathcal L[y']-y'(0)=s\big(sY-y(0)\big)-y'(0)=s^2Y-s\,y(0)-y'(0)
$$

Con reposo, todo lo que tiene $y(0)$ o $y'(0)$ se tacha: $\mathcal L[y']=sY$, $\mathcal L[y'']=s^2Y$. Si hay una integral, $\mathcal L\left[\int_0^t y\right]=\frac{Y}{s}$.

4. **Factor común $Y$** y despejá $G=\dfrac{Y}{F}$.
5. Si piden la respuesta, seguís con la receta de §7.

### Ejemplo guiado 11: el carrito (apuntes `05` y `11`, ejercicio 19a)

> $f(t)-K\,y(t)-B\,y'(t)=M\,y''(t)$ con $M=1$, $B=5$, $K=4$. Hallar la respuesta a un escalón unitario sabiendo que parte del reposo.

**Paso 1 y 2.** Entrada $f$ (escalón, $F=\frac1s$); salida $y$. Reposo: $y(0)=y'(0)=0$.

**Paso 3 — miembro a miembro:**

$$
F(s)-4Y-5\big(sY-y(0)\big)=s^2Y-s\,y(0)-y'(0)\quad\Longrightarrow\quad F(s)=Y\,(s^2+5s+4)
$$

**Paso 4 — transferencia:**

$$
G(s)=\frac{Y(s)}{F(s)}=\frac{1}{s^2+5s+4}=\frac{1}{(s+1)(s+4)}
$$

**Paso 5 — respuesta al escalón.** Raíces reales y distintas: "el caso más fácil", todo por tapado.

$$
Y(s)=\frac{1}{s\,(s+1)(s+4)}=\frac{A}{s}+\frac{B}{s+1}+\frac{C}{s+4},\qquad A=\frac14,\quad B=\frac{1}{(-1)(3)}=-\frac13,\quad C=\frac{1}{(-4)(-3)}=\frac1{12}
$$

$$
y(t)=\frac14-\frac13\,e^{-t}+\frac1{12}\,e^{-4t}
$$

Control: $\frac14-\frac13+\frac1{12}=0$ ✓. Tipo: exponencial decreciente (desplazada), valor estable $\frac14$.

**El ítem b del mismo ejercicio** (concepto que puede caer): ¿qué $B$ hace que el movimiento **no** sea amortiguado? $B$ es el rozamiento, lo que frena al carrito. Con $B=0$ el denominador queda $s^2+4$, polos $\pm2j$ sobre el eje: **oscilatoria de amplitud constante** (marginalmente estable). La justificación física ("sin rozamiento nada lo frena") "está bien justificado".

### ✍️ Tu turno 16 — 2025-1C T1 Ej3a/b · 25 min

Ecuación del sistema mecánico de traslación: $f(t)-K\,y(t)-B\,y'(t)=M\,y''(t)$, con $M=1$, $B=2$, $K=2$.

**a)** Hallá la función de transferencia $G(s)$ sabiendo que $y(0)=0$ y parte del reposo. **b)** Hallá la respuesta del sistema si la entrada es $f(t)=-e^{-t}$.

<details>
<summary>Corrección (RESOLUCIONES-2025, Tema 1 Ej3a/b)</summary>

**a)** $F-2Y-2\big(sY-y(0)\big)=s^2Y-s\,y(0)-y'(0)$; se tachan las condiciones iniciales:

$$
F=Y\,(s^2+2s+2)\quad\Longrightarrow\quad G(s)=\frac{1}{s^2+2s+2}
$$

**b)** $F(s)=-\dfrac1{s+1}$:

$$
Y(s)=\frac{-1}{(s^2+2s+2)(s+1)}=\frac{As+B}{s^2+2s+2}+\frac{C}{s+1}
$$

(La hoja usa $A,B$ para el cuadrático y $C$ para el polo real.) Tapando: $C=\dfrac{-1}{1-2+2}=-1$. Identidad $(As+B)(s+1)-(s^2+2s+2)=-1$: cuadráticos $A-1=0\Rightarrow A=1$; independientes $B-2=-1\Rightarrow B=1$.

$$
Y(s)=\frac{s+1}{(s+1)^2+1}-\frac1{s+1}
$$

$$
\boxed{\,y(t)=\cos(t)\,e^{-t}-e^{-t}\,}
$$

Control: $y(0)=1-1=0$ ✓.

</details>

### ✍️ Tu turno 17 — R-E de tu hoja (circuito RLC con impulso) · 25 min

Mismo molde con otra física: la integral pasa a $\frac{V(s)}{s}$ y la derivada a $sV(s)$ (con $v(0)=0$). Corregí con la hoja de práctica. Ojo: acá el control $y(0)=0$ **no** aplica (la $V$ tiene un solo grado de diferencia; por el teorema del valor inicial, $v(0)=\lim_{s\to\infty}s\,V(s)$, que no da $0$).

**Errores típicos de §9:** no tachar las condiciones iniciales (o tacharlas sin escribir que es por el reposo); errores de signo al pasar de miembro ($F-KY-BsY=Ms^2Y\Rightarrow F=Y(Ms^2+Bs+K)$); dar $Y$ cuando piden $G$ (o al revés).

---

## Checkpoint final: ¿cerraste sistemas? (≈ 45 min)

### ✍️ Tu turno 18 — el reciclado ×3, completo y a ciegas · 25 min

Tapá todo lo anterior y resolvé, en limpio, como en el parcial:

$$
G(s)=\frac{10\,(s^2-4s+k)}{s^3+5s^2+4s-10}
$$

**a)** Hallá $K$ para que $G(s)$ sea estable. **b)** Con ese $k$, hallá la respuesta temporal a una entrada escalón unitario $E(t)$. **c)** Indicá el tipo de respuesta (no confundir con estabilidad) y el valor estable.

<details>
<summary>Corrección (RESOLUCIONES-2025, Tema 2 Ej3a/b/c)</summary>

**a)** $s^3+5s^2+4s-10=(s-1)(s^2+6s+10)$ (Ruffini con $1$). Polo malo $s=1$: $1-4+k=0\Rightarrow k=3$. $G(s)=\dfrac{10\,(s-3)}{s^2+6s+10}$.

**b)** $Y=\dfrac{10(s-3)}{s(s^2+6s+10)}$, $A=-3$, $B=3$, $C=28$; $3s+28=3(s+3)+19$.

$$
y(t)=-3+3\cos(t)\,e^{-3t}+19\operatorname{sen}(t)\,e^{-3t}
$$

**c)** Oscilatoria amortiguada (polos $-3\pm j$); valor estable $-3$.

Si algo no salió, volvé a la sección que corresponde (§5, §7 u §8) y rehacé ese paso.

</details>

### Checklist de memoria (escribilo en una hoja sin mirar; 10 min)

- [ ] $Y=G\cdot F$; impulso $F=1$, escalón $F=\frac1s$, $e^{-at}\to\frac1{s+a}$.
- [ ] Simplificar primero; la raíz común no es ni cero ni polo; cero en el infinito.
- [ ] Estable ⇔ todos los polos con parte real $\le0$; uno solo a la derecha ⇒ inestable; marginalmente estable = estable.
- [ ] La tabla de los seis casos: polo → término de $y(t)$ → nombre del tipo de respuesta.
- [ ] $K$: Ruffini en el denominador, polo malo $p$, $N(p)=0$, cancelar, reescribir $G$.
- [ ] Corte: asíntota vertical en polos reales, toca y rebota en ceros reales, lomo en la parte real de los complejos, pegada al eje en los extremos; $|Y|$ con escalón suma un polo en $0$.
- [ ] Fracciones simples: tapado, cuadráticos/lineales, completar cuadrados, prestar; $\frac{s+a}{(s+a)^2+b^2}\to e^{-at}\cos bt$, $\frac{b}{(s+a)^2+b^2}\to e^{-at}\operatorname{sen}bt$.
- [ ] Control $y(0)=0$.
- [ ] V.E. $=\lim_{s\to0}sY(s)$ = la $A$ de $\frac{A}{s}$ = $G(0)$ con escalón.
- [ ] Reposo ⇒ $y(0)=y'(0)=0$; $\mathcal L[y'']=s^2Y-s\,y(0)-y'(0)$.

### Antes de cerrar el día

- Anotá con `/registrar` qué Tu turno salieron y cuáles no. Lo que falló se rehace el lunes a la noche.
- **No abras** `examenes/2025-1C_Recuperatorio.pdf`: es el simulacro a ciegas del lunes (su Ej3 se reemplaza por otro ejercicio, según `plan.md`).

---

*Generado el 2026-10-03 con: `examenes/resueltos/RESOLUCIONES-2025.md` (Ej3 T1, T2 y recuperatorio), `repaso/practica-repaso-2026.md` (E, F, G, solo referenciados), apuntes `05`, `07`, `10`, `11` y `13`, `examenes/INDICE.md` (enunciados y respuestas de los multiple choice), `plan.md` (ejercicios del domingo) y `fuentes/AYUDAMEMORIA-OFICIAL.pdf` (págs. 1–2). Correcciones marcadas «resuelto para esta guía» (2022-10-11 Ej5, 2024-2C rec Ej4a, 2024-1C T1 Ej5, 2024-1C T2 Ej4b, 2024-2C T2 Ej4b) y todas las demás cuentas verificadas con sympy 1.14. Gráficos de los cortes: dibujos cualitativos generados para esta guía con escala comprimida.*
