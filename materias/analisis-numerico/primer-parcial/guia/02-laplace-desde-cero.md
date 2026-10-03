# Laplace desde cero — guía lineal (sábado tarde/noche)

> Fuentes: `examenes/resueltos/RESOLUCIONES-2025.md` (Ej2 de Tema 1 y Tema 2), `repaso/practica-repaso-2026.md` (C y D), `apuntes/md/04-practica-transformada-laplace.md`, `14-video-aplicaciones-laplace.md`, `15-video-teorica-transformada-laplace.md`, `10-video-repaso-primer-parcial.md`, `07-repaso-primer-parcial.md`, `examenes/INDICE.md`, `../fuentes/AYUDAMEMORIA-OFICIAL.pdf`, `../fuentes/metodo-fracciones-simples.pdf` · Generado 2026-10-03
>
> **Cómo usarla:** leé de arriba abajo. Los «Ejemplo guiado» están resueltos a la vista: leelos con lápiz, rehaciendo cada paso. Los «Tu turno» se hacen en papel, con reloj y sin mirar; la corrección está plegada.
>
> Tiempo total: unas 4 h (cada sección dice cuánto). Tené abierto el **ayudamemoria oficial** al lado, el mismo que vas a tener en el parcial: la idea es aprender a usarlo, no a recitarlo.

---

## 0. Qué te toman (los 3 puntos del Ej2)

En el formato vigente (curso K3052, 2025) el **Ej2 es siempre Laplace** y trae 2 o 3 ítems de **1 punto cada uno**. Estos son los tipos que salieron:

| Ítem | Qué es | De dónde sale |
|---|---|---|
| Integral impropia "con Laplace" | Una integral de 0 a infinito que en realidad es una transformada evaluada en un número. Viene con un factor `t` (se deriva) o dividida por `t` (se integra). | 2025-1C T1 Ej2a (hoja fechada 2025-05-02); 2025-1C recuperatorio Ej2a (2025-06-23) |
| Transformar algo | Una potencia de seno o coseno (se abre con Euler), o una integral de convolución (da un producto de transformadas). | 2025-1C T2 Ej2a (`sen³t`); 2024-2C recuperatorio Ej3a (`cos³t`, ≈ dic 2024); 2025-1C recuperatorio Ej2b |
| Antitransformar por convolución | `1/(s²+1)²` o `s²/(s²+1)²`: se parte en dos factores, se arma la integral y se resuelve con producto → suma. | 2025-1C T1 Ej2b y T2 Ej2b; 2024-2C recuperatorio Ej3b |
| Demostración corta | `L{2^t} = 1/(s − ln 2)` en dos renglones. | 2025-1C T1 Ej2c |

En los 16 exámenes del dataset: integral impropia por Laplace en 8, convolución en 9, antitransformada en 11. Además, **las fracciones simples** (sección 9) no aparecen como ítem suelto del Ej2 pero son la herramienta de todo el Ej3 (Sistemas, el domingo): "sí o sí va a haber alguna" en Laplace, sistemas estables o Z, dice el profe.

> ⚠ Los ítems del **recuperatorio 2025-1C** son tu simulacro a ciegas del lunes: no los busques. En esta guía no se usan (ni el idéntico de `sin-fecha K3521 T2 Ej2`).

---

## 1. La idea en criollo (5 min)

- Laplace es una **máquina de traducir**: le das una función del tiempo $f(t)$ y te devuelve una función de otra variable, $F(s)$. Se escribe $\mathcal{L}[f(t)] = F(s)$.
- La traducción está definida por una integral, $F(s)=\int_0^\infty f(t)\,e^{-st}\,dt$, pero **nunca la vas a calcular a mano**: usás la **tabla** del ayudamemoria (y al revés para volver).
- Las **propiedades** son atajos: "si en el tiempo multiplicás por $t$, en $s$ derivás", "si en el tiempo multiplicás por $e^{at}$, en $s$ corrés la $s$", etc. También están en el ayudamemoria.
- **Antitransformar** ($\mathcal{L}^{-1}$) es el viaje de vuelta: te dan $F(s)$ y buscás qué $f(t)$ la produjo. Es más "artesanal": se trata de acomodar $F(s)$ hasta que se parezca a algo de la tabla.
- El truco de las integrales impropias: como la definición **es** una integral de 0 a infinito, cualquier integral de la forma $\int_0^\infty f(t)\,e^{-5t}\,dt$ es directamente $F(5)$. Transformás con la tabla y reemplazás $s$ por 5. Listo.

---

## 2. Qué tenés en el ayudamemoria y qué tenés que saber de memoria (10 min)

En el parcial podés usar **solo el ayudamemoria oficial + la tabla de integrales**. Abrilo ahora y ubicá cada cosa.

**Está en el ayudamemoria (no memorizar: saber encontrarlo y aplicarlo):**

- Definición: $\mathcal{L}[f(t)] = F(s) = \int_0^\infty f(t)\,e^{-st}\,dt$.
- 1ª traslación: $\mathcal{L}[e^{at} f(t)] = F(s-a)$.
- 2ª traslación, cambio de escala, derivadas $\mathcal{L}[f'(t)] = sF(s) - f(0)$ (las usás en Sistemas).
- Transformada de una integral: $\mathcal{L}\left[\int_0^t f(u)\,du\right] = \dfrac{F(s)}{s}$.
- Multiplicación por $t$: $\mathcal{L}[t^n f(t)] = (-1)^n F^{(n)}(s)$.
- División por $t$: $\mathcal{L}\left[\dfrac{f(t)}{t}\right] = \int_s^\infty F(u)\,du$, **siempre que exista** $\lim_{t\to0} f(t)/t$.
- Teorema de convolución (de Borel): $\mathcal{L}^{-1}[F(s)\,G(s)] = \int_0^t f(u)\,g(t-u)\,du$.
- TVI y TVF (para Sistemas).
- Tabla: $1 \to \frac1s$, $t \to \frac1{s^2}$, $t^n \to \frac{n!}{s^{n+1}}$, $e^{at} \to \frac1{s-a}$, $\operatorname{sen}(at) \to \frac{a}{s^2+a^2}$, $\cos(at) \to \frac{s}{s^2+a^2}$, $\delta(t) \to 1$.
- En la **tabla de integrales**: primitivas como $\int\frac{du}{u^2+1} = \operatorname{arctg} u$, $\int e^{au}\operatorname{sen}(bu)\,du$, y las fórmulas de suma de ángulos que el profe cita.

**NO está (tenés que saberlo de memoria):**

- **Euler:** $\operatorname{sen}x = \dfrac{e^{jx}-e^{-jx}}{2j}$ y $\cos x = \dfrac{e^{jx}+e^{-jx}}{2}$.
- **Binomio al cubo:** coeficientes $1\ 3\ 3\ 1$ (con signos alternados si es una resta).
- **Producto → suma** (o saber deducirlas de $\cos(x\pm y)$): $\operatorname{sen}A\operatorname{sen}B = \tfrac12[\cos(A-B)-\cos(A+B)]$, $\cos A\cos B = \tfrac12[\cos(A-B)+\cos(A+B)]$, $\operatorname{sen}A\cos B = \tfrac12[\operatorname{sen}(A+B)+\operatorname{sen}(A-B)]$.
- **Derivada de un cociente:** $\left(\dfrac{N}{D}\right)' = \dfrac{N'D - ND'}{D^2}$.
- **L'Hôpital** (para chequear el límite de la división por $t$) y **logaritmos:** $\ln a - \ln b = \ln\frac ab$, $\ln 1 = 0$.
- **Valores de arcotangente:** $\operatorname{arctg}0=0$, $\operatorname{arctg}\sqrt3=\frac\pi3$, $\operatorname{arctg}u\to\frac\pi2$ si $u\to\infty$.
- **Completar cuadrados:** $s^2+bs+c = \left(s+\frac b2\right)^2 + \left(c-\frac{b^2}{4}\right)$.
- **El método de fracciones simples** (los casos y el "tapado").
- **La demostración** $a^t = e^{t\ln a}$ (sección 11).
- **La receta de cada tipo de ítem** (esta guía).

---

## 3. Transformar con la tabla, linealidad y 1ª traslación (20 min)

**Receta**

1. Si hay sumas o constantes multiplicando, separá: la transformada de una suma es la suma de las transformadas y las constantes salen afuera (linealidad).
2. Cada pedazo, buscalo en la tabla. Si en la tabla dice $\operatorname{sen}(at)$, leé quién es $a$ en tu función.
3. Si un pedazo viene multiplicado por $e^{at}$: transformá **sin** la exponencial y después cambiá cada $s$ por $s-a$ (1ª traslación).
4. Dejalo separado: no hace falta sacar denominador común ("es mejor dejarlo así, que es claro de dónde viene cada cosa", dice el profe).

**Ejemplo guiado 3.1** (clase teórica, `15` Ej. 2): $\mathcal{L}[4t^2 - 3\cos 2t + 5e^{-t}]$.

**Paso 1:** linealidad, porque son tres sumandos con constantes:

$$
4\,\mathcal{L}[t^2] - 3\,\mathcal{L}[\cos 2t] + 5\,\mathcal{L}[e^{-t}]
$$

**Paso 2:** tabla en cada uno ($t^2 \to \frac{2!}{s^3}$; coseno con $a=2$; exponencial con $a=-1$):

$$
F(s) = \frac{8}{s^3} - \frac{3s}{s^2+4} + \frac{5}{s+1}
$$

**Ejemplo guiado 3.2** (práctica, `04` Ej. 2b): $\mathcal{L}[5e^{-5t}\cos 3t]$.

**Paso 1:** sin la exponencial, por tabla, porque $e^{-5t}$ se trata aparte:

$$
\mathcal{L}[5\cos 3t] = \frac{5s}{s^2+9}
$$

**Paso 2:** 1ª traslación con $a=-5$: toda $s$ pasa a ser $s-(-5)=s+5$, **también la de arriba**:

$$
F(s) = \frac{5(s+5)}{(s+5)^2+9}
$$

**Tu turno 3** (4 min cada uno, práctica `04` Ej. 2a y 2e):

a) $\mathcal{L}[t^2 e^{4t}]$

b) $\mathcal{L}[e^{-2t}\operatorname{sen}(2t) + t^2e^{3t}]$

<details>
<summary>Corrección 3</summary>

**a)** Tabla: $t^2 \to \dfrac{2}{s^3}$. 1ª traslación con $a=4$ ($s \to s-4$):

$$
F(s) = \frac{2}{(s-4)^3}
$$

**b)** Primer sumando: $\operatorname{sen}2t \to \dfrac{2}{s^2+4}$, y con $a=-2$ queda $s\to s+2$. Segundo: como en a) pero con $a=3$:

$$
F(s) = \frac{2}{(s+2)^2+4} + \frac{2}{(s-3)^3}
$$

</details>

**Errores típicos:** trasladar solo el denominador y olvidarte de la $s$ del numerador; confundir seno con coseno (con denominador $s^2+a^2$: **si arriba hay $s$ es coseno, si hay una constante es seno**).

---

## 4. Multiplicación por $t$ e integral impropia = transformada evaluada (35 min)

**Dos ideas que se combinan:**

**(a) Multiplicar por $t$ en el tiempo = derivar en $s$ y cambiar el signo.** Del ayudamemoria, con $n=1$:

$$
\mathcal{L}[t\,f(t)] = -F'(s)
$$

Receta del profe: "**1°) derivo** $F(s)$, **2°) cambio el signo (una vez)**". Con $t^2$: derivás dos veces y cambiás el signo dos veces (o sea, no cambia).

**(b) Integral impropia = $F$ evaluada.** Comparando con la definición:

$$
\int_0^\infty f(t)\,e^{-kt}\,dt = F(k)
$$

$f(t)$ es **todo lo que no es la exponencial**; el número que acompaña al $-t$ en la exponencial es dónde evaluás. Si no hay exponencial, es $e^{-0t}$ y evaluás en $s=0$.

**Receta para "calcular $\int_0^\infty (\dots)\,dt$ con Laplace"**

1. Separá la exponencial $e^{-kt}$ (la que tiene exponente negativo con $t$): eso te da $s=k$.
2. Lo que queda es $f(t)$. Escribí: "la integral es $\mathcal{L}[f(t)]$ evaluada en $s=k$".
3. Calculá $F(s)$ **genérica** (tabla + propiedad que corresponda).
4. **Recién al final** reemplazá $s=k$.

**Ejemplo guiado 4.1** (clase grabada, `14` Ej. 9): $\int_0^\infty t^2e^{-2t}\,dt$.

**Paso 1:** la exponencial es $e^{-2t}$, entonces evaluamos en $s=2$; $f(t)=t^2$.

**Paso 2:** tabla: $\mathcal{L}[t^2] = \dfrac{2}{s^3}$.

**Paso 3:** evaluar:

$$
\int_0^\infty t^2e^{-2t}\,dt = F(2) = \frac{2}{8} = \frac14
$$

(Fijate: sin integrar por partes dos veces.)

**Ejemplo guiado 4.2** (repaso del profe, `07`/`10` Ej. 6, era multiple choice): $\int_0^\infty t\operatorname{sen}(at)\,e^{-2t}\,dt$.

**Paso 1:** $e^{-2t}$ ⇒ evaluar en $s=2$; $f(t) = t\operatorname{sen}(at)$, que tiene una $t$ multiplicando ⇒ multiplicación por $t$.

**Paso 2:** tabla para el seno solo:

$$
\mathcal{L}[\operatorname{sen}(at)] = \frac{a}{s^2+a^2}
$$

**Paso 3:** derivo respecto de $s$ (numerador constante: solo queda $-a\cdot 2s$ arriba):

$$
\frac{d}{ds}\left(\frac{a}{s^2+a^2}\right) = \frac{-2as}{(s^2+a^2)^2}
$$

**Paso 4:** cambio el signo una vez, porque $n=1$:

$$
\mathcal{L}[t\operatorname{sen}(at)] = \frac{2as}{(s^2+a^2)^2}
$$

**Paso 5:** evalúo en $s=2$:

$$
\int_0^\infty t\operatorname{sen}(at)\,e^{-2t}\,dt = \frac{4a}{(4+a^2)^2}
$$

**Tu turno 4** (8 min cada uno)

a) **(parcial 2025-1C T1 Ej2a)** Resolver con Laplace: $\int_0^\infty t\,e^{-5t}\cos(t)\,dt$.

b) **(sin-fecha K3521 T1 Ej2, multiple choice)** $\int_0^\infty t\cos(3t)\,e^{-5t}\,dt$ es: $\frac{4}{289}$ / $\frac{5}{34}$ / $\frac{5}{1156}$ / $\infty$ / n.a. Justificar con Laplace.

c) **(práctica `04` Ej. 2c)** $\mathcal{L}[e^{-t}\,t\operatorname{sen}(2t)]$. Pista del profe: si hay exponencial y $t$, **primero** la multiplicación por $t$ y **después** la traslación.

d) (opcional, práctica `04` Ej. 13e) $\int_0^\infty t\,e^{-2t}\cos(4t)\,dt$.

<details>
<summary>Corrección 4</summary>

**a)** $s=5$, $f(t)=t\cos t$. Tabla: $\mathcal{L}[\cos t] = \dfrac{s}{s^2+1}$. Derivo con la regla del cociente:

$$
\frac{d}{ds}\left(\frac{s}{s^2+1}\right) = \frac{(s^2+1) - s\cdot 2s}{(s^2+1)^2} = \frac{1-s^2}{(s^2+1)^2}
$$

Cambio el signo:

$$
\mathcal{L}[t\cos t] = \frac{s^2-1}{(s^2+1)^2}
$$

Evalúo en $s=5$:

$$
\int_0^\infty t\,e^{-5t}\cos t\,dt = \frac{24}{26^2} = \frac{24}{676} = \frac{6}{169}
$$

(La hoja oficial lo deja como $24/676$.)

**b)** Igual que a) con $\cos 3t$: $\mathcal{L}[t\cos 3t] = \dfrac{s^2-9}{(s^2+9)^2}$. En $s=5$:

$$
\frac{25-9}{34^2} = \frac{16}{1156} = \frac{4}{289}
$$

Opción **a**.

**c)** Paso 1, multiplicación por $t$ sobre $\operatorname{sen}2t$: $\dfrac{2}{s^2+4}$ → derivo $\dfrac{-4s}{(s^2+4)^2}$ → cambio signo $\dfrac{4s}{(s^2+4)^2}$. Paso 2, 1ª traslación con $a=-1$ ($s\to s+1$ en todos lados):

$$
\mathcal{L}[e^{-t}\,t\operatorname{sen}2t] = \frac{4(s+1)}{\left[(s+1)^2+4\right]^2}
$$

**d)** $\mathcal{L}[t\cos 4t] = \dfrac{s^2-16}{(s^2+16)^2}$; en $s=2$: $\dfrac{4-16}{20^2} = -\dfrac{12}{400} = -\dfrac{3}{100}$.

</details>

**Errores típicos:** reemplazar $s$ por el número **antes** de derivar (derivás una constante y te da 0); olvidarte el cambio de signo; tratar el $e^{-5t}$ de la integral como 1ª traslación (en una integral de 0 a ∞ esa exponencial es el $e^{-st}$ de la definición: te dice dónde evaluar).

> **Guardate este resultado:** $\mathcal{L}[t\cos t] = \dfrac{s^2-1}{(s^2+1)^2}$ salió en **dos** exámenes de 2025.

---

## 5. División por $t$: integrales con $/t$ (30 min)

Del ayudamemoria:

$$
\mathcal{L}\left[\frac{f(t)}{t}\right] = \int_s^\infty F(u)\,du \qquad \text{siempre que exista } \lim_{t\to0}\frac{f(t)}{t}
$$

$F$ es la transformada del **numerador**, escrita con la letra $u$ en lugar de $s$. El profe: es una propiedad que "se toma bastante" y el ejercicio de las dos exponenciales sobre $t$ "es un ejercicio tomable" (a veces da $\ln 2$, a veces $\ln 3$; los pasos son los mismos).

**Receta**

1. Si hay **dos exponenciales** sobre $t$, sacá factor común la de **menor** exponente: así queda $e^{-kt}\cdot\dfrac{1-e^{-mt}}{t}$. La $e^{-kt}$ te dice que evaluás en $s=k$. Si no hay exponencial, evaluás en $s=0$.
2. **Chequeá el límite** $\lim_{t\to0}\dfrac{f(t)}{t}$ (suele ser $0/0$: L'Hôpital). Escribilo: si existe, podés aplicar la propiedad. Es parte del puntaje.
3. Transformá el numerador $f(t)$ con la tabla, cambiale $s$ por $u$, e integrá de $s$ a $\infty$ (las primitivas dan logaritmos o arcotangentes).
4. Si al evaluar en $\infty$ aparece $\infty-\infty$ con logaritmos, **juntalos en uno solo** ($\ln a - \ln b = \ln\frac ab$): el cociente tiende a 1 y $\ln 1 = 0$.
5. Al final, evaluá en $s=k$.

**Ejemplo guiado 5.1** (práctica `04` Ej. 13d, resuelto también en `14` y `10`): $\int_0^\infty \dfrac{e^{-3t}-e^{-6t}}{t}\,dt$.

**Paso 1 — el camino que NO va:** separar en $\int\frac{e^{-3t}}{t} - \int\frac{e^{-6t}}{t}$ y tomar cada una como "transformada de $1/t$". No se puede: $\lim_{t\to0}\frac1t$ no existe. "No vayan por ahí porque no van a llegar a nada".

**Paso 2 — factor común $e^{-3t}$**, para que quede una sola exponencial que marque dónde evaluar:

$$
\int_0^\infty e^{-3t}\,\frac{1-e^{-3t}}{t}\,dt = \mathcal{L}\left[\frac{1-e^{-3t}}{t}\right]\Bigg|_{s=3}
$$

**Paso 3 — chequear la condición** ($0/0$, L'Hôpital: derivo arriba y abajo):

$$
\lim_{t\to0}\frac{1-e^{-3t}}{t} = \lim_{t\to0}\frac{3e^{-3t}}{1} = 3 \quad\text{(existe)}
$$

**Paso 4 — división por $t$:** $\mathcal{L}[1] = \frac1s$ y $\mathcal{L}[e^{-3t}] = \frac{1}{s+3}$, pasados a $u$:

$$
\mathcal{L}\left[\frac{1-e^{-3t}}{t}\right] = \int_s^\infty\left(\frac1u - \frac{1}{u+3}\right)du = \Big[\ln|u| - \ln|u+3|\Big]_s^\infty
$$

**Paso 5 — salvar el $\infty-\infty$:** junto en un solo logaritmo; $\frac{u}{u+3}\to1$ cuando $u\to\infty$, y $\ln 1 = 0$:

$$
\left[\ln\left|\frac{u}{u+3}\right|\right]_s^\infty = 0 - \ln\left|\frac{s}{s+3}\right| = \ln\left|\frac{s+3}{s}\right|
$$

**Paso 6 — evaluar en $s=3$:**

$$
\int_0^\infty\frac{e^{-3t}-e^{-6t}}{t}\,dt = \ln\frac{6}{3} = \ln 2
$$

**Tu turno 5** (8 min cada uno)

a) **(parcial 2024-2C T1 Ej3b)** Resolver $\int_0^\infty \dfrac{\operatorname{sen}t}{t}\,dt$.

b) **(parcial 2015-05-29 T2 Ej2 iii, multiple choice)** $\int_0^\infty \dfrac{\operatorname{sen}t}{t}\,e^{-\sqrt3\,t}\,dt$ es: $0$ / $\frac\pi2$ / $\frac\pi4$ / $\frac\pi6$.

<details>
<summary>Corrección 5</summary>

**a)** No hay exponencial ⇒ es $e^{-0t}$ ⇒ evaluar en $s=0$. Condición: $\lim_{t\to0}\frac{\operatorname{sen}t}{t} = 1$, existe. $\mathcal{L}[\operatorname{sen}t] = \frac{1}{s^2+1}$, en $u$:

$$
F(s) = \int_s^\infty\frac{du}{u^2+1} = \operatorname{arctg}u\,\Big|_s^\infty = \frac\pi2 - \operatorname{arctg}s
$$

$$
\int_0^\infty\frac{\operatorname{sen}t}{t}\,dt = F(0) = \frac\pi2
$$

(Variante del 2024-2C T2: de $-\infty$ a $\infty$. Como $\frac{\operatorname{sen}t}{t}$ es par, es el doble: $\pi$.)

**b)** Misma $F(s)$ que en a), evaluada en $s=\sqrt3$:

$$
\frac\pi2 - \operatorname{arctg}\sqrt3 = \frac\pi2 - \frac\pi3 = \frac\pi6
$$

Opción **$\frac\pi6$**.

</details>

**Errores típicos:** separar la fracción en dos integrales con $1/t$; no escribir el chequeo del límite; dejar $\infty-\infty$ sin juntar los logaritmos; olvidarte de evaluar en el número del final.

---

## 6. Potencias y productos de seno y coseno: Euler (25 min)

La tabla no tiene $\cos^3t$ ni $\operatorname{sen}5t\cos2t$. El truco es **convertir el producto en una suma** de senos/cosenos simples, que sí están en la tabla.

**Receta**

1. Reemplazá cada seno/coseno por Euler: $\operatorname{sen}x = \frac{e^{jx}-e^{-jx}}{2j}$, $\cos x = \frac{e^{jx}+e^{-jx}}{2}$.
2. Desarrollá (binomio $1\,3\,3\,1$ para el cubo; distributiva para un producto) y juntá exponentes: $e^{2jt}e^{-jt} = e^{jt}$.
3. Reagrupá en parejas $e^{jkt}$ con $e^{-jkt}$ y armá de nuevo $\frac{e^{jkt}+e^{-jkt}}{2} = \cos kt$ o $\frac{e^{jkt}-e^{-jkt}}{2j} = \operatorname{sen}kt$ (multiplicando y dividiendo por lo que haga falta).
4. Transformá por tabla y linealidad.

(Alternativa válida: identidades trigonométricas producto → suma. Euler tiene la ventaja de que no hay que acordarse de nada más.)

**Ejemplo guiado 6.1** (práctica `04` Ej. 3f): $\mathcal{L}[\operatorname{sen}(5t)\cos(2t)]$.

**Paso 1 — Euler:**

$$
\operatorname{sen}5t\cos2t = \frac{e^{5jt}-e^{-5jt}}{2j}\cdot\frac{e^{2jt}+e^{-2jt}}{2}
$$

**Paso 2 — distributiva** ($2j\cdot 2 = 4j$; se suman exponentes: $5+2=7$, $5-2=3$, $-5+2=-3$, $-5-2=-7$):

$$
= \frac{1}{4j}\left(e^{7jt} + e^{3jt} - e^{-3jt} - e^{-7jt}\right)
$$

**Paso 3 — reagrupar** las parejas $\pm7$ y $\pm3$; como $\frac1{4j} = \frac12\cdot\frac1{2j}$, cada pareja arma un seno:

$$
= \frac12\cdot\frac{e^{7jt}-e^{-7jt}}{2j} + \frac12\cdot\frac{e^{3jt}-e^{-3jt}}{2j} = \frac12\operatorname{sen}7t + \frac12\operatorname{sen}3t
$$

**Paso 4 — tabla:**

$$
F(s) = \frac12\cdot\frac{7}{s^2+49} + \frac12\cdot\frac{3}{s^2+9}
$$

**Ahora hacé el C) de `exports/practica-repaso-2026-enunciados.pdf`** ($\cos^3t$, 15 min, el profe lo marcó "Practicar"). La corrección está en `repaso/practica-repaso-2026.md`.

**Tu turno 6** (15 min) **(parcial 2025-1C T2 Ej2a)** Transformada de Laplace de $\operatorname{sen}^3(t)$, $t>0$.

<details>
<summary>Corrección 6</summary>

**Paso 1 — Euler y cubo.** Ojo con el denominador: $(2j)^3 = 8j^3 = -8j$.

$$
\operatorname{sen}^3t = \left(\frac{e^{jt}-e^{-jt}}{2j}\right)^3 = -\frac{1}{8j}\left(e^{3jt} - 3e^{jt} + 3e^{-jt} - e^{-3jt}\right)
$$

(los del medio: $3e^{2jt}e^{-jt} = 3e^{jt}$ y $3e^{jt}e^{-2jt} = 3e^{-jt}$; signos alternados por ser una resta).

**Paso 2 — reagrupar en senos** ($-\frac1{8j} = -\frac14\cdot\frac1{2j}$):

$$
= -\frac14\cdot\frac{e^{3jt}-e^{-3jt}}{2j} + \frac34\cdot\frac{e^{jt}-e^{-jt}}{2j} = -\frac14\operatorname{sen}3t + \frac34\operatorname{sen}t
$$

**Paso 3 — tabla:**

$$
\mathcal{L}[\operatorname{sen}^3t] = -\frac14\cdot\frac{3}{s^2+9} + \frac34\cdot\frac{1}{s^2+1}
$$

Es la respuesta oficial (que la escribe como $-\frac34\cdot\frac1{s^2+9} + \frac34\cdot\frac1{s^2+1}$).

</details>

**Errores típicos:** $(2j)^3 = -8j$ (no $8j$); al reagrupar, quedarte con $\frac{1}{4j}$ en vez de convertirlo en $\frac12\cdot\frac1{2j}$; copiar mal la línea intermedia (en la hoja del profe del C) quedó $\frac14\operatorname{sen}3t$ en vez de $\frac14\cos3t$; la $F(s)$ final estaba bien).

---

## 7. Transformada de una integral de convolución (20 min)

Del ayudamemoria, leído "de derecha a izquierda":

$$
\mathcal{L}\left[\int_0^t f(u)\,g(t-u)\,du\right] = F(s)\cdot G(s)
$$

**Receta**

1. Mirá adentro de la integral e identificá: lo que depende **solo de $u$** es $f(u)$; lo que depende de **$t-u$** es $g(t-u)$. "Ahí no hay demasiado para elegir".
2. Transformá cada una por separado, **pensando $u$ y $t-u$ como si fueran $t$** (el corrimiento no importa al transformar). Si $f(u)$ trae una $u$ multiplicando, es multiplicación por $t$ (sección 4).
3. Multiplicá y simplificá lo que se pueda (diferencia de cuadrados, por ejemplo).

**Ejemplo guiado 7.1** (clase grabada, `14` Ej. 5): $\mathcal{L}\left[\int_0^t e^{u}\,e^{2(t-u)}\,du\right]$.

**Paso 1:** $f(u) = e^u$ (solo $u$) y $g(t-u) = e^{2(t-u)}$ (tiene $t-u$).

**Paso 2:** se piensan como $e^t$ y $e^{2t}$: tabla con $a=1$ y $a=2$.

**Paso 3:** producto:

$$
\mathcal{L}\left[\int_0^t e^{u}\,e^{2(t-u)}\,du\right] = \frac{1}{s-1}\cdot\frac{1}{s-2}
$$

**Ejemplo guiado 7.2 — solo leer** (parciales 2022-10-11 Ej2 y 2024-1C T1 Ej2, formato viejo: ecuación integral). Resolver $y(t) - \int_0^t y(u)\operatorname{sen}(t-u)\,du = t^4$.

**Paso 1:** transformar miembro a miembro; la integral es una convolución de $y$ con $\operatorname{sen}$, así que da $Y(s)\cdot\frac{1}{s^2+1}$:

$$
Y(s) - \frac{Y(s)}{s^2+1} = \frac{24}{s^5}
$$

**Paso 2:** despejar ($1 - \frac{1}{s^2+1} = \frac{s^2}{s^2+1}$):

$$
Y(s) = \frac{24(s^2+1)}{s^7} = \frac{24}{s^5} + \frac{24}{s^7}
$$

**Paso 3:** antitransformar por tabla ($t^4\to\frac{24}{s^5}$, $t^6\to\frac{720}{s^7}$):

$$
y(t) = t^4 + \frac{t^6}{30}
$$

(En el formato vigente no salió, pero es "donde más vamos a usar convolución", según el profe.)

**Tu turno 7** (5 min) **(la integral de `14` Ej. 7, leída al revés)** Hallá $\mathcal{L}\left[3\int_0^t e^{-(t-u)}\operatorname{sen}(2u)\,du\right]$.

<details>
<summary>Corrección 7</summary>

$f(u) = \operatorname{sen}2u \to \dfrac{2}{s^2+4}$; $g(t-u) = e^{-(t-u)}$, pensada como $e^{-t}$ $\to \dfrac{1}{s+1}$. Con el 3 afuera:

$$
3\cdot\frac{1}{s+1}\cdot\frac{2}{s^2+4} = \frac{6}{(s+1)(s^2+4)}
$$

Esta $Y(s)$ la vas a antitransformar dos veces más adelante (secciones 9 y 10): tiene que volver a dar la integral.

</details>

**Errores típicos:** transformar $g(t-u)$ con el corrimiento (no va); no detectar que $f(u)$ tiene una $u$ multiplicando (entonces es derivar y cambiar signo); no simplificar al final. En el parcial el ítem puede combinar esto con la sección 4: no te asustes, es una propiedad por factor.

---

## 8. Antitransformar I: tabla, ajustar constantes, completar cuadrados (20 min)

**Receta**

1. Buscá a qué fila de la tabla se parece. Si falta una constante, **multiplicá y dividí** por ella (el truco "se usa mucho").
2. Si el denominador es $s^2+bs+c$ y no tiene raíces reales, **completá el cuadrado**: $(s-\alpha)^2 + \beta^2$.
3. Si el numerador tiene $s$, **partilo** para que aparezca el mismo $(s-\alpha)$ de abajo: $s = (s-\alpha) + \alpha$.
4. 1ª traslación al revés: todo lo que está en función de $(s-\alpha)$ sale multiplicado por $e^{\alpha t}$. Con $(s-\alpha)$ arriba es coseno; con una constante arriba, seno:

$$
\mathcal{L}^{-1}\left[\frac{s-\alpha}{(s-\alpha)^2+\beta^2}\right] = e^{\alpha t}\cos\beta t
\qquad
\mathcal{L}^{-1}\left[\frac{\beta}{(s-\alpha)^2+\beta^2}\right] = e^{\alpha t}\operatorname{sen}\beta t
$$

Esto es exactamente lo que vas a hacer el domingo con los polos complejos de Sistemas.

**Ejemplo guiado 8.1** (clase teórica, `15` Ej. 17): $\mathcal{L}^{-1}\left[\dfrac{1}{s^2-2s+5}\right]$.

**Paso 1 — completar el cuadrado** (la mitad de $-2$ es $-1$; $5 - 1 = 4$):

$$
\frac{1}{s^2-2s+5} = \frac{1}{(s-1)^2+4}
$$

**Paso 2 — ajustar la constante:** se parece a $\operatorname{sen}2t \to \frac{2}{s^2+4}$; falta un 2 arriba: multiplico y divido por 2.

**Paso 3 — traslación al revés:** $(s-1)$ ⇒ $e^{t}$:

$$
\mathcal{L}^{-1}\left[\frac12\cdot\frac{2}{(s-1)^2+4}\right] = \frac12\,e^{t}\operatorname{sen}2t
$$

**Ejemplo guiado 8.2** (práctica `04` Ej. 5g): $\mathcal{L}^{-1}\left[\dfrac{s-1}{s^2+2s+2}\right]$.

**Paso 1 — completar el cuadrado:** $s^2+2s+2 = (s+1)^2+1$.

**Paso 2 — partir el numerador** para que aparezca $(s+1)$: $s-1 = (s+1) - 2$:

$$
\frac{s-1}{(s+1)^2+1} = \frac{s+1}{(s+1)^2+1} - \frac{2}{(s+1)^2+1}
$$

**Paso 3 — tabla + traslación** ($\beta=1$, $e^{-t}$ por el $s+1$):

$$
y(t) = e^{-t}\cos t - 2e^{-t}\operatorname{sen}t
$$

**Tu turno 8** (4 min cada uno, práctica `04` Ej. 5b, 5f, 5h)

a) $\mathcal{L}^{-1}\left[\dfrac{8}{s^2+3} + \dfrac1s\right]$

b) $\mathcal{L}^{-1}\left[\dfrac{s+3}{s^2+6s+13}\right]$

c) $\mathcal{L}^{-1}\left[\dfrac{4s}{(s^2+4)^2}\right]$. Pista: "hace pensar en $t\cos 2t$ o $t\operatorname{sen}2t$"; probá con la sección 4.

<details>
<summary>Corrección 8</summary>

**a)** $3 = a^2$ ⇒ $a = \sqrt3$. Multiplico y divido por $\sqrt3$:

$$
y(t) = \frac{8}{\sqrt3}\operatorname{sen}(\sqrt3\,t) + 1
$$

**b)** $s^2+6s+13 = (s+3)^2+4$, y el numerador ya es $s+3$:

$$
y(t) = e^{-3t}\cos 2t
$$

**c)** Probar con $t\operatorname{sen}2t$: $\frac{2}{s^2+4}$ → derivo $\frac{-4s}{(s^2+4)^2}$ → cambio signo $\frac{4s}{(s^2+4)^2}$ ✓. Entonces:

$$
y(t) = t\operatorname{sen}2t
$$

</details>

**Errores típicos:** completar mal el cuadrado (la mitad del coeficiente de $s$, al cuadrado, se resta); trasladar el denominador y no partir el numerador; olvidarte la constante que multiplicaste y dividiste.

---

## 9. Antitransformar II: fracciones simples (45 min — clave para el domingo)

Cuando $F(s)$ es un cociente de polinomios que "ya no se parece a nada", se rompe en **fracciones simples**, cada una antitransformable por tabla.

**Receta**

0. **Grados:** si grado(numerador) ≥ grado(denominador), primero dividí: $\frac PQ = C + \frac RQ$ (caso raro, "no es muy importante").
1. **Factorizá el denominador** (resolvente, Ruffini). **Sacá afuera el coeficiente principal:** $2s^2+7s+3 = 2(s+3)(s+\frac12)$; si no, "el resultado de fracciones simples no les va a dar bien".
2. **Planteá** según las raíces (casos del PDF de la cátedra):
   - raíz real simple $p$: $\dfrac{A}{s-p}$;
   - raíz real doble $p$: $\dfrac{A}{(s-p)^2} + \dfrac{B}{s-p}$;
   - par complejo conjugado (cuadrático con $b^2-4ac<0$): $\dfrac{Bs+C}{s^2+bs+c}$ (**dos incógnitas arriba**);
   - complejas múltiples: "no las toma" (por eso $1/(s^2+1)^2$ va por convolución).
3. **Truco del tapado (cover-up):** para cada raíz real simple, y para la potencia más alta de una raíz repetida: **tapá ese factor** en la $F(s)$ original y evaluá lo que queda en la raíz. Eso es el coeficiente. "Sáquense de encima todas las incógnitas que puedan con el truquito".
4. **Lo que falte** (la $B$ de la raíz doble, la $Bs+C$ del cuadrático): sumá las fracciones con denominador común, igualá el numerador al original y **compará coeficientes**, eligiendo los que despejan fácil (el de $s^2$ y el término independiente suelen alcanzar).
5. **Antitransformá** cada pedazo: $\frac{A}{s-p}\to Ae^{pt}$, $\frac{A}{(s-p)^2}\to Ate^{pt}$, el cuadrático con la sección 8 (completar cuadrado, partir numerador).

**Ejemplo guiado 9.1 — raíces reales simples** (práctica `04` Ej. 6a): $F(s) = \dfrac{s+7}{s^2-6s+5}$.

**Paso 1 — factorizar:** raíces 5 y 1 ⇒ $s^2-6s+5 = (s-5)(s-1)$.

**Paso 2 — plantear:**

$$
\frac{s+7}{(s-5)(s-1)} = \frac{A}{s-5} + \frac{B}{s-1}
$$

**Paso 3 — tapado:** para $A$ tapo $(s-5)$ y evalúo el resto en $s=5$; para $B$ tapo $(s-1)$ y evalúo en $s=1$:

$$
A = \frac{5+7}{5-1} = \frac{12}{4} = 3 \qquad B = \frac{1+7}{1-5} = \frac{8}{-4} = -2
$$

**Paso 4 — antitransformar:**

$$
f(t) = 3e^{5t} - 2e^{t}
$$

**Ejemplo guiado 9.2 — raíz doble** (práctica `04` Ej. 6c): $F(s) = \dfrac{1}{(s+2)^2(s+1)}$.

**Paso 1 — plantear** (la doble baja de potencia 2 a 1):

$$
F(s) = \frac{A}{(s+2)^2} + \frac{B}{s+2} + \frac{C}{s+1}
$$

**Paso 2 — tapado** para $A$ (tapo $(s+2)^2$, evalúo en $-2$) y $C$ (tapo $(s+1)$, evalúo en $-1$):

$$
A = \frac{1}{-2+1} = -1 \qquad C = \frac{1}{(-1+2)^2} = 1
$$

**Paso 3 — $B$ igualando coeficientes:** el numerador común es $A(s+1) + B(s+2)(s+1) + C(s+2)^2 = 1$. Mirando solo los $s^2$: $B + C = 0$ ⇒ $B = -1$.

**Paso 4 — antitransformar** ($\frac{1}{(s+2)^2}$ es $t$ trasladada: $te^{-2t}$):

$$
f(t) = -t\,e^{-2t} - e^{-2t} + e^{-t}
$$

**Ejemplo guiado 9.3 — raíces complejas** (práctica `04` Ej. 6h): $F(s) = \dfrac{7s^2-41s+84}{(s-1)(s^2-4s+13)}$.

**Paso 1 — chequear el cuadrático:** $b^2-4ac = 16-52 < 0$ ⇒ complejas, lleva $Bs+C$:

$$
F(s) = \frac{A}{s-1} + \frac{Bs+C}{s^2-4s+13}
$$

**Paso 2 — tapado para $A$** (tapo $s-1$, evalúo en $s=1$):

$$
A = \frac{7-41+84}{1-4+13} = \frac{50}{10} = 5
$$

**Paso 3 — igualar coeficientes:**

$$
5(s^2-4s+13) + (Bs+C)(s-1) = 7s^2-41s+84
$$

$s^2$: $5+B = 7$ ⇒ $B=2$. Independiente: $65 - C = 84$ ⇒ $C = -19$.

**Paso 4 — completar el cuadrado y partir el numerador** ($s^2-4s+13 = (s-2)^2+9$; $2s = 2(s-2)+4$, y $4-19 = -15$):

$$
F(s) = \frac{5}{s-1} + \frac{2(s-2)}{(s-2)^2+9} - \frac{15}{(s-2)^2+9}
$$

**Paso 5 — antitransformar** ($\beta = 3$, así que $15 = 5\cdot 3$; $e^{2t}$ por el $s-2$):

$$
f(t) = 5e^{t} + 2e^{2t}\cos3t - 5e^{2t}\operatorname{sen}3t
$$

**Tu turno 9** (8–10 min cada uno, práctica `04` Ej. 6d y 6i, y `14` Ej. 7 por otro camino)

a) $\mathcal{L}^{-1}\left[\dfrac{s^2+9s+19}{(s+1)(s+2)(s+4)}\right]$ (solo tapado).

b) $\mathcal{L}^{-1}\left[\dfrac{-2s^2+8s-14}{(s+1)(s^2-2s+5)}\right]$

c) $\mathcal{L}^{-1}\left[\dfrac{6}{(s+1)(s^2+4)}\right]$ por fracciones simples. (El profe: por los dos caminos "tiene que dar lo mismo"; lo comprobás en la sección 10, por convolución.)

d) (opcional, integrador; parcial 2024-1C T2 Ej2) Resolver por Laplace $y(t) - 2\int_0^t y(u)\cos(t-u)\,du = 1$.

<details>
<summary>Corrección 9</summary>

**a)** Tres raíces reales simples, todo por tapado:

$$
A = \frac{1-9+19}{(1)(3)} = \frac{11}{3}\ (s=-1) \qquad B = \frac{4-18+19}{(-1)(2)} = -\frac52\ (s=-2) \qquad C = \frac{16-36+19}{(-3)(-2)} = -\frac16\ (s=-4)
$$

$$
f(t) = \frac{11}{3}e^{-t} - \frac52 e^{-2t} - \frac16 e^{-4t}
$$

**b)** $s^2-2s+5$: $4-20<0$, complejas. Planteo $\frac{A}{s+1} + \frac{Bs+C}{s^2-2s+5}$.

Tapado en $s=-1$: $A = \dfrac{-2-8-14}{1+2+5} = \dfrac{-24}{8} = -3$.

Igualo $A(s^2-2s+5) + (Bs+C)(s+1) = -2s^2+8s-14$. $s^2$: $-3+B = -2$ ⇒ $B = 1$. Independiente: $-15 + C = -14$ ⇒ $C = 1$.

Completo cuadrado ($s^2-2s+5 = (s-1)^2+4$) y parto ($s+1 = (s-1)+2$):

$$
F(s) = -\frac{3}{s+1} + \frac{s-1}{(s-1)^2+4} + \frac{2}{(s-1)^2+4}
$$

$$
f(t) = -3e^{-t} + e^{t}\cos2t + e^{t}\operatorname{sen}2t
$$

**c)** Planteo $\frac{A}{s+1} + \frac{Bs+C}{s^2+4}$. Tapado en $s=-1$: $A = \frac{6}{1+4} = \frac65$. Igualo $A(s^2+4) + (Bs+C)(s+1) = 6$: $s^2$: $A + B = 0$ ⇒ $B = -\frac65$; independiente: $4A + C = 6$ ⇒ $C = \frac65$.

$$
F(s) = \frac{6/5}{s+1} - \frac65\cdot\frac{s}{s^2+4} + \frac35\cdot\frac{2}{s^2+4}
$$

$$
y(t) = \frac65e^{-t} - \frac65\cos2t + \frac35\operatorname{sen}2t
$$

**d)** Miembro a miembro (la integral es $Y(s)\cdot\frac{s}{s^2+1}$):

$$
Y(s) - \frac{2s\,Y(s)}{s^2+1} = \frac1s \quad\Rightarrow\quad Y(s)\,\frac{(s-1)^2}{s^2+1} = \frac1s \quad\Rightarrow\quad Y(s) = \frac{s^2+1}{s(s-1)^2}
$$

Planteo $\frac{A}{s} + \frac{B}{(s-1)^2} + \frac{C}{s-1}$. Tapado: $A = \frac{1}{1} = 1$ ($s=0$), $B = \frac{2}{1} = 2$ ($s=1$). $s^2$: $A + C = 1$ ⇒ $C = 0$.

$$
y(t) = 1 + 2t\,e^{t}
$$

</details>

**Errores típicos:** no sacar el coeficiente principal al factorizar; poner una sola constante arriba de un cuadrático (van dos: $Bs+C$); armar el sistema completo sin usar antes el tapado ("lo que parecía un 3×3 queda en dos ecuaciones"); al completar cuadrados, no partir el numerador y dejar una $s$ suelta.

---

## 10. Antitransformar III: por convolución (30 min)

Cuando la consigna dice "antitransformar utilizando convolución" (o cuando hay complejas dobles como $(s^2+1)^2$, que en fracciones simples "no toma"):

$$
\mathcal{L}^{-1}[F(s)\,G(s)] = \int_0^t f(u)\,g(t-u)\,du
$$

**Receta**

1. **Partí** $Y(s)$ en dos factores que estén en la tabla, siguiendo los factores del denominador. Las constantes repartilas como quieras.
2. **Antitransformá** cada uno: $f(t)$ y $g(t)$.
3. **Armá la integral:** a una le ponés $u$ y a la otra $t-u$. Si hay una exponencial, **dale el $t-u$ a la exponencial**: $e^{-(t-u)} = e^{-t}e^{u}$ y el $e^{-t}$ sale afuera de la integral.
4. **Resolvé la integral en $u$** ($t$ es una constante ahí adentro). Con productos de senos/cosenos, primero producto → suma; con exponencial por seno, primitiva de la tabla de integrales.
5. **Barrow:** reemplazá $u=t$ y $u=0$, y simplificá ($\operatorname{sen}(-t) = -\operatorname{sen}t$, $\cos(-t) = \cos t$).

**Ejemplo guiado 10.1** (clase grabada `14` Ej. 7 = práctica `04` Ej. 11a): $\mathcal{L}^{-1}\left[\dfrac{6}{(s+1)(s^2+4)}\right]$ por convolución.

**Paso 1 — partir** según los dos factores del denominador:

$$
F(s) = \frac{6}{s+1} \qquad G(s) = \frac{1}{s^2+4}
$$

**Paso 2 — antitransformar cada uno** (al seno le falta un 2 arriba: multiplico y divido):

$$
f(t) = 6e^{-t} \qquad g(t) = \frac12\operatorname{sen}2t
$$

**Paso 3 — armar la integral** dándole el $t-u$ a la exponencial ($6\cdot\frac12 = 3$):

$$
y(t) = 3\int_0^t e^{-(t-u)}\operatorname{sen}(2u)\,du = 3e^{-t}\int_0^t e^{u}\operatorname{sen}(2u)\,du
$$

**Paso 4 — primitiva de la tabla de integrales** ($\int e^{au}\operatorname{sen}(bu)\,du$ con $a=1$, $b=2$) y Barrow (en $u=0$: $e^0=1$, $\operatorname{sen}0=0$, $-2\cos0 = -2$):

$$
y(t) = 3e^{-t}\left[\frac15e^{u}\big(\operatorname{sen}2u - 2\cos2u\big)\right]_0^t = 3e^{-t}\left[\frac15e^{t}\big(\operatorname{sen}2t - 2\cos2t\big) + \frac25\right]
$$

**Paso 5 — distributiva** ($e^{-t}e^{t} = 1$):

$$
y(t) = \frac35\operatorname{sen}2t - \frac65\cos2t + \frac65e^{-t}
$$

Igual que en el Tu turno 9c (por fracciones simples) ✓.

**Ahora hacé el D) de `exports/practica-repaso-2026-enunciados.pdf`** ($1/(s^2+1)^2$, 20 min). Es el mismo ítem que el 2025-1C T1 Ej2b. Pista: $\operatorname{sen}u\operatorname{sen}(t-u) = \frac12[\cos(2u-t) - \cos t]$, y $\cos t$ es constante respecto de $u$.

**Tu turno 10** (15 min) **(parcial 2025-1C T2 Ej2b)** Antitransformar utilizando convolución: $Y(s) = \dfrac{s^2}{(s^2+1)^2}$.

<details>
<summary>Corrección 10</summary>

**Paso 1:** $F(s) = G(s) = \dfrac{s}{s^2+1}$ ⇒ $f(t) = g(t) = \cos t$.

**Paso 2:** convolución y producto → suma ($A = u$, $B = t-u$: $A-B = 2u-t$, $A+B = t$):

$$
y(t) = \int_0^t\cos u\cos(t-u)\,du = \frac12\int_0^t\big[\cos t + \cos(2u-t)\big]\,du
$$

**Paso 3:** integrar en $u$ ($\cos t$ es constante: da $u\cos t$; la primitiva de $\cos(2u-t)$ es $\frac{\operatorname{sen}(2u-t)}{2}$):

$$
y(t) = \frac12\Big[u\cos t\Big]_0^t + \frac12\left[\frac{\operatorname{sen}(2u-t)}{2}\right]_0^t = \frac12t\cos t + \frac14\big(\operatorname{sen}t - \operatorname{sen}(-t)\big)
$$

**Paso 4:** $\operatorname{sen}t - \operatorname{sen}(-t) = 2\operatorname{sen}t$:

$$
y(t) = \frac12t\cos t + \frac12\operatorname{sen}t
$$

(Y la del D) da $y(t) = \frac12\operatorname{sen}t - \frac12t\cos t$: mismo esqueleto, cambia un signo.)

</details>

**Errores típicos:** integrar $\cos t$ como si dependiera de $u$ (es constante: da $u\cos t$); olvidarte el $\frac12$ de la primitiva de $\cos(2u-t)$; equivocarte con $\operatorname{sen}(-t)$; darle el $t-u$ al seno cuando había una exponencial (la integral se complica).

---

## 11. Demostración: $\mathcal{L}[a^t] = \dfrac{1}{s-\ln a}$ (10 min)

Te piden "demostrar", pero son dos renglones (2025-1C T1 Ej2c, con $a=2$). La tabla solo tiene exponenciales en base $e$, así que pasás $a^t$ a base $e$.

**Ejemplo guiado 11.1** (práctica `04` Ej. 3d, con $a>0$):

**Paso 1 — reescribir en base $e$** (aplico logaritmo y vuelvo a exponenciar; $\ln a^t = t\ln a$):

$$
a^t = e^{\ln a^t} = e^{t\ln a}
$$

**Paso 2 — tabla** $\mathcal{L}[e^{ct}] = \frac{1}{s-c}$ con $c = \ln a$ (es un número):

$$
\mathcal{L}[a^t] = \mathcal{L}[e^{t\ln a}] = \frac{1}{s-\ln a}
$$

**Tu turno 11** (3 min cada uno)

a) **(parcial 2025-1C T1 Ej2c)** Demostrar que $\mathcal{L}(2^t) = \dfrac{1}{s-\ln2}$. Escribilo de memoria.

b) **(parcial sin-fecha-2 T1 Ej1a, multiple choice)** Si $f(t) = 2^te^{-4t}$, $\mathcal{L}[f(t)]$ es: $\frac{1}{\ln(2s+4)}$ / $\frac{1}{s-\ln2+4}$ / $\frac{1}{s-\ln2}\cdot\frac{1}{s+4}$ / otra.

<details>
<summary>Corrección 11</summary>

**a)** $2^t = e^{\ln 2^t} = e^{t\ln2}$; por tabla con $c = \ln2$: $\mathcal{L}[2^t] = \dfrac{1}{s-\ln2}$.

**b)** $\mathcal{L}[2^t] = \frac{1}{s-\ln2}$ y la $e^{-4t}$ es 1ª traslación ($s\to s+4$):

$$
\mathcal{L}[2^te^{-4t}] = \frac{1}{s+4-\ln2}
$$

Opción **b**. (La tercera es la trampa: una exponencial multiplicando **no** es un producto de transformadas.)

</details>

---

## Checkpoint final: si podés hacer esto sin mirar, pasás a Sistemas

Hacé cada uno en papel, sin la guía, solo con el ayudamemoria al lado:

- [ ] Escribir **qué no está en el ayudamemoria**: Euler, binomio $1\,3\,3\,1$, producto → suma, derivada del cociente, completar cuadrados.
- [ ] Dada $\int_0^\infty f(t)\,e^{-kt}\,dt$: decir sin dudar "es $F(k)$" y quién es $f$.
- [ ] $\mathcal{L}[t\cos t] = \dfrac{s^2-1}{(s^2+1)^2}$ derivando (y evaluar al final, no antes).
- [ ] La integral con $\dfrac{e^{-at}-e^{-bt}}{t}$: factor común, **chequeo del límite** escrito, logaritmos juntos, evaluar. Da $\ln\frac ba$.
- [ ] $\cos^3t$ y $\operatorname{sen}^3t$ por Euler en menos de 10 minutos cada una (con $(2j)^3 = -8j$).
- [ ] Transformar $\int_0^t f(u)\,g(t-u)\,du$ como $F\cdot G$, identificando quién es quién.
- [ ] Fracciones simples con tapado: reales simples, una doble y un cuadrático complejo (completar cuadrado → $e^{\alpha t}\cos\beta t$, $e^{\alpha t}\operatorname{sen}\beta t$).
- [ ] $\dfrac{1}{(s^2+1)^2}$ y $\dfrac{s^2}{(s^2+1)^2}$ por convolución, con producto → suma.
- [ ] $\mathcal{L}[2^t]$ demostrado en dos renglones.

Si algo no salió, volvé a esa sección y rehacé su Tu turno. Después anotá la sesión con `/registrar` (qué salió, qué no, en qué paso te trabaste).

---

*Generado el 2026-10-03 a partir de `examenes/resueltos/RESOLUCIONES-2025.md`, `repaso/practica-repaso-2026.md`, `apuntes/md/04`, `07`, `10`, `14` y `15`, `examenes/INDICE.md`, el ayudamemoria oficial y el PDF de fracciones simples de la cátedra. Todos los resultados (incluidos los ítems sin resolución en la fuente: `04` Ej. 6d, 6i, 13e; 2015-05-29 T2 Ej2 iii; 2024-1C T2 Ej2) se verificaron con cálculo simbólico (sympy 1.14).*
