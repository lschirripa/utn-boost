# Formulario complemento del ayudamemoria — 1P Análisis Numérico

> **Solo lo que NO está en el ayudamemoria oficial** y hace falta para resolver los ejercicios del parcial. Lo que sí está (fórmulas de la STF/SEF, propiedades y tablas de Laplace y Z, Euler, binomio) no se repite acá: aprendé a encontrarlo en el PDF. Fuentes: guías 01–04 (secciones 🧠), `RESOLUCIONES-2025.md`, `practica-repaso-2026.md`. Generado 2026-10-06.
>
> Esta hoja **no se lleva al examen**: es para memorizar esta tarde.

---

## 1 · Series de Fourier

**Datos de la función** (el intervalo dado es medio período):

$$
L = \text{largo del dato} \qquad T = 2L \qquad \omega_0 = \frac{\pi}{L} = \frac{2\pi}{T}
$$

**Paridad ⇒ qué se anula ⇒ qué pedido la impone:**

| Si $f$ es… | Se anula | Queda | Lo piden como… |
|---|---|---|---|
| **par** $f(-t)=f(t)$ (espejo vertical) | $b_m = 0$ | $\dfrac{a_0}{2},\ a_m$ | "solo cosenos", "SEF con coeficientes **reales**" |
| **impar** $f(-t)=-f(t)$ (espejo por el origen) | $a_0 = a_m = 0$ | $b_m$ | "solo senos", "SEF con coeficientes **imaginarios puros**" |
| impar **desplazada** (impar + constante) | $a_m = 0$ | $\dfrac{a_0}{2},\ b_m$ | "imaginarios puros salvo $C_0$" |

**Atajo de paridad** (se integra solo el dato, de $0$ a $L$):

$$
a_m = \frac{2}{L}\int_0^L f(t)\cos(m\omega_0 t)\,dt \qquad b_m = \frac{2}{L}\int_0^L f(t)\operatorname{sen}(m\omega_0 t)\,dt \qquad \frac{a_0}{2} = \text{altura promedio (por gráfico)}
$$

**Evaluar en $\pi$:**

$$
\cos(m\pi) = (-1)^m \qquad \operatorname{sen}(m\pi) = 0 \qquad \cos\!\left(\tfrac{m\pi}{2}\right) = 0 \text{ ($m$ impar)},\ (-1)^{m/2} \text{ ($m$ par)}
$$

$$
(-1)^m - 1 = \begin{cases}0 & m \text{ par}\\ -2 & m \text{ impar}\end{cases} \qquad\Longrightarrow\qquad \text{reindexar } m = 2k+1,\ k \ge 0
$$

**Las dos primitivas de siempre** (si $m\omega_0 \ne m$, reemplazar $m$ por $m\omega_0$):

$$
\int t\cos(mt)\,dt = \frac{\cos(mt)}{m^2} + \frac{t\operatorname{sen}(mt)}{m} \qquad\qquad \int t\operatorname{sen}(mt)\,dt = \frac{\operatorname{sen}(mt)}{m^2} - \frac{t\cos(mt)}{m}
$$

**De STF a SEF** (nunca integrar con la $j$ adentro):

$$
C_0 = \frac{a_0}{2} \qquad C_m = \frac12\left(a_m - j\,b_m\right) \qquad C_{-m} = \overline{C_m} \qquad |C_m| = \frac12\sqrt{a_m^2 + b_m^2}
$$

Espectro de amplitudes: bastones de $|C_m|$ en $m\omega_0$, simétrico, $|C_{-m}| = |C_m|$. Aclarar $m \ne 0$ bajo la sumatoria.

**Simetría de media onda:** $f(t + T/2) = -f(t)$ ⇒ **solo armónicas impares** y valor medio $0$. Para completar con **paridad + media onda**: $T = 4\ell$ ($\ell$ = largo del dato); primero espejar por paridad, después **correr medio período y dar vuelta**: en $(\ell, 2\ell)$, $f(t) = -f(t - 2\ell)$.

**Identidades para el ítem "ya es una serie":**

$$
2\operatorname{sen}x\cos x = \operatorname{sen}2x \qquad \cos^2 x = \tfrac12 + \tfrac12\cos 2x \qquad \operatorname{sen}^2 x = \tfrac12 - \tfrac12\cos 2x
$$

**Convergencia en un salto:** la serie da el promedio de los límites laterales.

---

## 2 · Transformada de Laplace

**Euler** (la de seno **no** está en el ayudamemoria):

$$
\cos x = \frac{e^{jx} + e^{-jx}}{2} \qquad \operatorname{sen}x = \frac{e^{jx} - e^{-jx}}{2j} \qquad (2j)^2 = -4,\quad (2j)^3 = -8j,\quad \frac{1}{j} = -j
$$

**Cubos** (coeficientes $1\ 3\ 3\ 1$):

$$
\operatorname{sen}^3 t = \tfrac34\operatorname{sen}t - \tfrac14\operatorname{sen}3t \qquad\qquad \cos^3 t = \tfrac34\cos t + \tfrac14\cos 3t
$$

**Producto → suma:**

$$
\operatorname{sen}A\operatorname{sen}B = \tfrac12[\cos(A-B) - \cos(A+B)] \qquad \cos A\cos B = \tfrac12[\cos(A-B) + \cos(A+B)] \qquad \operatorname{sen}A\cos B = \tfrac12[\operatorname{sen}(A+B) + \operatorname{sen}(A-B)]
$$

**Integral impropia = transformada evaluada:**

$$
\int_0^\infty f(t)\,e^{-at}\,dt = F(s)\Big|_{s=a} \qquad\qquad \int_0^\infty \frac{f(t)}{t}\,e^{-at}\,dt = \int_a^\infty F(u)\,du
$$

Para $\int_0^\infty \frac{e^{-at} - e^{-bt}}{t}dt$: sacar factor $e^{-at}$, queda $\mathcal{L}\!\left[\frac{1 - e^{-(b-a)t}}{t}\right]$ en $s = a$. Chequear que exista $\lim_{t\to0} f(t)/t$ (L'Hôpital).

**Derivadas que aparecen al multiplicar por $t$:**

$$
\left(\frac{N}{D}\right)' = \frac{N'D - ND'}{D^2} \qquad \left(\frac{s}{s^2+a^2}\right)' = \frac{a^2 - s^2}{(s^2+a^2)^2} \qquad \left(\frac{a}{s^2+a^2}\right)' = \frac{-2as}{(s^2+a^2)^2}
$$

$$
\mathcal{L}[t\cos at] = \frac{s^2 - a^2}{(s^2+a^2)^2} \qquad \mathcal{L}[t\operatorname{sen}at] = \frac{2as}{(s^2+a^2)^2} \qquad \mathcal{L}[t\,e^{at}] = \frac{1}{(s-a)^2}
$$

**Logaritmos y arcotangente** (salen en división por $t$):

$$
\int_s^\infty\left(\frac{1}{u-a} - \frac{1}{u-b}\right)du = \ln\frac{s-b}{s-a} \qquad \int_s^\infty \frac{a}{u^2+a^2}\,du = \frac{\pi}{2} - \operatorname{arctg}\frac{s}{a}
$$

$$
\ln a - \ln b = \ln\frac{a}{b} \qquad \ln 1 = 0 \qquad \operatorname{arctg}0 = 0,\quad \operatorname{arctg}1 = \tfrac{\pi}{4},\quad \operatorname{arctg}\sqrt3 = \tfrac{\pi}{3},\quad \operatorname{arctg}(\infty) = \tfrac{\pi}{2}
$$

**Convolución (ida y vuelta):**

$$
\mathcal{L}\!\left[\int_0^t f(u)\,g(t-u)\,du\right] = F(s)\,G(s) \qquad\qquad \mathcal{L}^{-1}[F\cdot G] = \int_0^t f(u)\,g(t-u)\,du
$$

$$
\mathcal{L}^{-1}\!\left[\frac{1}{(s^2+1)^2}\right] = \frac{\operatorname{sen}t - t\cos t}{2} \qquad \mathcal{L}^{-1}\!\left[\frac{s^2}{(s^2+1)^2}\right] = \frac{\operatorname{sen}t + t\cos t}{2} \qquad \mathcal{L}^{-1}\!\left[\frac{s}{(s^2+1)^2}\right] = \frac{t\operatorname{sen}t}{2}
$$

**Completar cuadrados y las dos antitransformadas con traslación:**

$$
s^2 + bs + c = \left(s + \tfrac{b}{2}\right)^2 + \left(c - \tfrac{b^2}{4}\right) \qquad\qquad \frac{s+a}{(s+a)^2+b^2} \to e^{-at}\cos bt \qquad \frac{b}{(s+a)^2+b^2} \to e^{-at}\operatorname{sen}bt
$$

Si arriba hay $s + c$ con $c \ne a$: escribir $s + c = (s + a) + (c - a)$ y repartir.

**Fracciones simples** (grado del numerador < grado del denominador; si no, dividir primero):

| Factor en el denominador | Términos | Cómo sacar las constantes |
|---|---|---|
| $(s - p)$ simple | $\dfrac{A}{s-p}$ | **tapado:** $A = \big[(s-p)\,Y(s)\big]_{s=p}$ |
| $(s - p)^2$ doble | $\dfrac{A}{s-p} + \dfrac{B}{(s-p)^2}$ | $B$ por tapado con $(s-p)^2$; $A$ igualando coeficientes o evaluando en otro $s$ |
| $s^2 + bs + c$ irreducible | $\dfrac{Bs + C}{s^2+bs+c}$ | igualar coeficientes (o evaluar en $s = 0$ y en otro valor) |

**Demostración $\mathcal{L}[a^t]$:** $a^t = e^{t\ln a}$ ⇒ $\mathcal{L}[a^t] = \dfrac{1}{s - \ln a}$, $s > \ln a$.

---

## 3 · Sistemas estables (por si entrás al Ej3a)

$$
Y(s) = G(s)\,F(s) \qquad \text{impulso: } F = 1 \qquad \text{escalón } E(t):\ F = \frac1s \qquad e^{-at}:\ F = \frac{1}{s+a}
$$

**Estable ⇔ todos los polos con parte real negativa** (después de simplificar factores comunes: una raíz común arriba y abajo no es ni polo ni cero). Para hallar $K$: factorizar el denominador (Ruffini: probar $\pm1, \pm2, \pm5, \pm10$, divisores del término independiente), encontrar el polo con $\operatorname{Re} > 0$ y elegir $K$ para que el **numerador se anule en ese polo**.

| Polo | Respuesta |
|---|---|
| real negativo $-a$ | $e^{-at}$, decae sin oscilar |
| real positivo | $e^{at}$, inestable |
| $-a \pm bj$ | $e^{-at}\cos bt$, $e^{-at}\operatorname{sen}bt$: **oscilatoria amortiguada** |
| $\pm bj$ | oscila sin amortiguar |
| en $0$ (viene de $F = 1/s$) | constante: el **valor estable** es su coeficiente $A$ (o $\lim_{s\to0} sY(s)$) |

$$
\mathcal{L}[y''] = s^2 Y - s\,y(0) - y'(0) \qquad \text{reposo} \Rightarrow y(0) = y'(0) = 0
$$

---

## 4 · Transformada Z

**Serie geométrica**, la base de todo:

$$
\sum_{k=0}^{\infty} r^k = \frac{1}{1 - r} \quad \text{solo si } |r| < 1 \qquad\qquad \sum_{k=0}^{\infty} \left(\frac{a}{z}\right)^k = \frac{z}{z-a},\quad |z| > |a|
$$

**Sucesión por paridad:** $n = 2k$ y $n = 2k+1$.

$$
\sum_{k} a^{2k} z^{-2k} = \sum_k \left(\frac{a^2}{z^2}\right)^k = \frac{z^2}{z^2 - a^2} \quad (|z| > |a|) \qquad\qquad \sum_k b^{2k+1} z^{-(2k+1)} = \frac{b}{z}\cdot\frac{z^2}{z^2 - b^2} = \frac{bz}{z^2 - b^2} \quad (|z| > |b|)
$$

Si $b^{-n}$: la razón es $\frac{1}{bz}$ y la ROC es $|z| > \frac{1}{|b|}$. **ROC total = intersección** = exterior de la circunferencia más grande (punteada si la desigualdad es estricta).

**Sumar series con Z:**

$$
\sum_{n=0}^{\infty} x(n)\,c^{-n} = X(z)\Big|_{z=c} \qquad\qquad \mathcal{Z}\!\left[\frac{a^n}{n!}\right] = e^{a/z} \qquad \cos(\pi n) = (-1)^n
$$

**Ecuaciones en diferencias** (desplazamiento, ya distribuido):

$$
\mathcal{Z}[x(n+1)] = zX - z\,x(0) \qquad \mathcal{Z}[x(n+2)] = z^2 X - z^2 x(0) - z\,x(1)
$$

Después de despejar $X(z)$: **dejar una $z$ afuera** (hacer fracciones simples de $X(z)/z$), volver a multiplicar por $z$ y leer la tabla: $\frac{z}{z-a} \to a^n$, $\frac{az}{(z-a)^2} \to n\,a^n$. **Verificar** con la recurrencia: calcular $x(1)$, $x(2)$ de la ecuación y comparar con la fórmula.

---

## 5 · Herramientas de cálculo

$$
\int u\,dv = uv - \int v\,du \qquad \text{(en } \int t\cdot\text{trig}: u = t\text{)}
$$

$$
s = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} \qquad \sqrt{-k} = j\sqrt{k} \qquad |a + bj| = \sqrt{a^2 + b^2}
$$

$$
\int_0^\infty e^{-at}\,dt = \frac1a \qquad e^{-\infty} = 0 \qquad \frac{1}{1 + 1/3} = \frac34
$$

*Generado el 2026-10-06 a partir de las guías `guia/01–04` (secciones "qué tenés que saber de memoria"), `RESOLUCIONES-2025.md` y `practica-repaso-2026.md`.*
