# Fourier desde cero — guía lineal (sábado mañana)

> Fuentes: apuntes `01` (OneNote práctica STF), `02` (OneNote práctica SEF), `10` (video repaso del 1P), `examenes/resueltos/RESOLUCIONES-2025.md`, `repaso/practica-repaso-2026.md`, `examenes/INDICE.md`, `fuentes/AYUDAMEMORIA-OFICIAL.pdf`. Coeficientes verificados con sympy. Generado 2026-10-03.
>
> **Cómo usarla:** leé de arriba abajo, sin saltear. Los **Ejemplos guiados** están resueltos a la vista: leelos con lápiz y rehacé cada paso en papel. Los **Tu turno** se hacen en papel, con reloj y **sin mirar**; la corrección está plegada. Tiempo total: ≈ 4 h.

---

## 0. Qué te toman: el Ej1 vale 3 puntos

En el parcial vigente (2025) el Ej1 siempre trae estos tres ítems, de 1 punto cada uno:

| Ítem | Qué te piden | Ejemplo real | Sección de esta guía |
|---|---|---|---|
| **a** | Te dan $f$ en **medio período**. La completás para que la serie tenga solo cosenos o solo senos (o, dicho de otra forma, que la SEF tenga coeficientes reales o imaginarios puros). Graficás y desarrollás la serie. | 2025-1C T1: $f(t)=\pi-t$ en $(0,\pi)$ | §3 a §6 |
| **b** | Una pregunta corta para justificar: "la STF de $2\operatorname{sen}x\cos x$ es…", o un verdadero o falso. | 2025-1C T1 y T2 | §7 y §9 |
| **c** | Completar para que tenga **simetría de media onda** y además una paridad. Solo gráfico y fórmula por tramos: **no hay que desarrollar la serie**. | 2025-1C T1: $f(t)=t$ en $(0,1)$ | §8 |

El ítem **a** salió en **15 de las 16 hojas** de parcial desde 2015. Es el punto más seguro de todo el examen.

## 1. La idea en criollo

Una función **periódica** se repite igual cada $T$ segundos. Fourier dice que **cualquier función periódica se puede escribir como una suma de cosenos y senos**: uno lento, que da una vuelta por período, y otros cada vez más rápidos, de 2, 3, 4… vueltas por período. Se les dice **armónicas**.

$$
f(t) = \underbrace{\frac{a_0}{2}}_{\text{altura promedio}} + a_1\cos(\omega_0 t) + b_1\operatorname{sen}(\omega_0 t) + a_2\cos(2\omega_0 t) + b_2\operatorname{sen}(2\omega_0 t) + \cdots
$$

**Desarrollar la serie** quiere decir encontrar esos números $a_0, a_m, b_m$, que dicen "cuánto" de cada armónica tiene la función. Se sacan con una integral cuya fórmula está en el ayudamemoria. Todo el trabajo del ejercicio es:

1. Dibujar la función.
2. Darte cuenta de qué coeficientes **dan cero sin calcular nada**, por simetría.
3. Calcular el único que queda. Es una integral por partes.

## 2. Qué tenés en el ayudamemoria y qué tenés que saber de memoria

**Está en el ayudamemoria (página 1).** No hace falta memorizarlo, pero tenés que saber usarlo:

$$
S(x) = \frac{a_0}{2} + \sum_{n=1}^{\infty} a_n\cos(n\omega x) + b_n\operatorname{sen}(n\omega x)
$$

$$
a_n = \frac{1}{L}\int_{-L}^{L} f(x)\cos(n\omega x)\,dx \qquad b_n = \frac{1}{L}\int_{-L}^{L} f(x)\operatorname{sen}(n\omega x)\,dx \qquad L = \frac{T}{2}
$$

- Simetría de media onda: $f(x) = -f(x + T/2)$.
- La forma de la serie exponencial (SEF).

La cátedra usa $n$ o $m$ como índice, da lo mismo. En esta guía va $m$, como en los OneNote. El $a_0$ es la fórmula de $a_n$ con $n=0$.

**No está en el ayudamemoria, así que va de memoria.** Es todo lo de esta guía marcado con 🧠:

- 🧠 $\omega_0 = \dfrac{\pi}{L} = \dfrac{2\pi}{T}$.
- 🧠 Par ⇒ $b_m = 0$. Impar ⇒ $a_0 = a_m = 0$. Y el atajo $\frac{2}{L}\int_0^L$.
- 🧠 $\cos(m\pi) = (-1)^m$ y $\operatorname{sen}(m\pi) = 0$.
- 🧠 $C_m = \frac12(a_m - j\,b_m)$ y $C_0 = \frac{a_0}{2}$.
- 🧠 Reales ⇒ par. Imaginarios puros ⇒ impar.
- 🧠 Media onda ⇒ solo armónicas impares. Con dos condiciones, el período es 4 veces el largo del dato.

Las integrales $\int t\cos(mt)\,dt$ y $\int t\operatorname{sen}(mt)\,dt$ están en la **tabla de integrales**, que también se puede llevar.

---

## 3. Herramientas: 20 minutos antes del primer ejemplo

### 3.1 Los tres datos: $T$, $L$ y $\omega_0$

El profe exige en **todos** los ejercicios: *graficar y anotar $T$, $L$, $\omega_0$* (apunte `01`, p. 1). Ya ese paso suma.

$$
T = \text{período}, \qquad L = \frac{T}{2}, \qquad \omega_0 = \frac{\pi}{L}
$$

> **Clave del ítem a:** te dan la función en un intervalo como $(0,\pi)$ y te piden completarla. Ese intervalo es **medio período**. Entonces $L$ es el largo del intervalo y $T = 2L$.
> Ejemplo: dato en $(0,\pi)$ ⇒ $L=\pi$, $T=2\pi$, $\omega_0=1$. Dato en $(0,2)$ ⇒ $L=2$, $T=4$, $\omega_0=\pi/2$.

### 3.2 Par e impar, mirando el dibujo

- **Par**, $f(-t) = f(t)$: el dibujo es **espejo respecto del eje vertical**, como $\cos t$, $t^2$ o $|t|$.
- **Impar**, $f(-t) = -f(t)$: el dibujo es **espejo respecto del origen**, como $\operatorname{sen} t$, $t$ o $t^3$. Pasa por $0$ en el origen, salvo que haya un salto.

¿Por qué importa? Porque **la integral de una función impar en $(-L,L)$ da cero**: el área de la izquierda cancela la de la derecha. Y el coseno es par, el seno es impar:

| $f$ es… | $f\cdot\cos$ es… | $f\cdot\operatorname{sen}$ es… | Conclusión |
|---|---|---|---|
| **par** | par·par = par | par·impar = **impar ⇒ integral 0** | $b_m = 0$: **solo cosenos** (+ $a_0/2$) |
| **impar** | impar·par = **impar ⇒ integral 0** | impar·impar = par | $a_0 = a_m = 0$: **solo senos** |

Y cuando el integrando es par, la integral de $-L$ a $L$ es el doble de la de $0$ a $L$. Por eso, en la práctica:

$$
\text{par:}\quad a_m = \frac{2}{L}\int_0^L f(t)\cos(m\omega_0 t)\,dt \qquad\qquad \text{impar:}\quad b_m = \frac{2}{L}\int_0^L f(t)\operatorname{sen}(m\omega_0 t)\,dt
$$

**Ventaja enorme:** de $0$ a $L$ solo está el pedazo que te dieron como dato. No hace falta escribir la parte completada.

### 3.3 $\cos(m\pi)$ y $\operatorname{sen}(m\pi)$

Al evaluar en $\pi$ siempre aparece esto. En la circunferencia, $m\pi$ cae en $+1$ o en $-1$ del eje horizontal:

$$
\operatorname{sen}(m\pi) = 0, \qquad \cos(m\pi) = (-1)^m \quad (\text{vale } -1, 1, -1, 1, \dots \text{ para } m = 1, 2, 3, 4, \dots)
$$

El profe aclara que **no hace falta justificarlo**: "ponemos menos 1 a la n y listo" (video `10`, [54:34]).

### 3.4 Las dos integrales de la tabla

Casi todos los parciales tienen la función como una recta, $t$, $\pi - t$, $2x$, $x+1$…, así que siempre aparecen estas dos. Están en la tabla de integrales; si no, salen por partes con $u=t$:

$$
\int t\cos(mt)\,dt = \frac{\cos(mt)}{m^2} + \frac{t\operatorname{sen}(mt)}{m}
$$

$$
\int t\operatorname{sen}(mt)\,dt = \frac{\operatorname{sen}(mt)}{m^2} - \frac{t\cos(mt)}{m}
$$

Si en vez de $mt$ hay $m\omega_0 t$, por ejemplo $\frac{m\pi}{2}x$, se cambia $m$ por $m\omega_0$ en todos lados.

### 3.5 Cuando los pares dan cero: pasar a $2k+1$

Muchas veces el resultado tiene $(-1)^m - 1$. Eso da $0$ si $m$ es par y $-2$ si $m$ es impar. Entonces:

- Lo escribís separado: "si $m$ par, $a_m = 0$; si $m$ impar, $a_m = \dots$".
- En la serie reemplazás $m = 2k+1$, con $k$ desde $0$. Así quedan solo $1, 3, 5, \dots$

El profe lo pide así: dejarlo en $m$ "no es un error", pero queda mejor con $2k+1$ (video `10`, [38:25]).

---

## 4. La receta del ítem a (completar y desarrollar)

1. **Traducí el pedido a una paridad.**
   - "Solo cosenos" o "SEF con coeficientes **reales**" ⇒ **par**.
   - "Solo senos" o "SEF con coeficientes **imaginarios puros**" ⇒ **impar**.
   - ¿Por qué? Porque $C_m = \frac12(a_m - j\,b_m)$. Si es real, no hay $b_m$, o sea que es par. Si es imaginario puro, no hay $a_m$, o sea que es impar.
2. **Graficá** el dato y completalo:
   - **Par:** espejo vertical.
   - **Impar:** espejo por el origen.
   - Después repetilo con período $T$.
3. **Escribí $f$ por tramos** en $(-L, L)$, agregá "$f(t) = f(t+T)$" y anotá $T$, $L$ y $\omega_0$.
4. **Anulá lo que se anula, con una línea de justificación:**
   - Par: "$b_m = 0$ por ser par".
   - Impar: "$a_0 = a_m = 0$ por ser impar".
5. **Si es par, el valor medio $a_0/2$ se lee del gráfico.** Es la altura promedio. Por ejemplo, un triángulo que va de $0$ a $h$ tiene promedio $h/2$. Vale sacarlo "por gráfico" (video `10`, [33:13]).
6. **Calculá el coeficiente que queda** con $\frac{2}{L}\int_0^L$ sobre el dato. Integrás con la tabla y evaluás, usando $\cos(m\pi) = (-1)^m$ y $\operatorname{sen}(m\pi) = 0$.
7. **Separá $m$ par y $m$ impar** si hace falta y **escribí la serie**. Con $2k+1$ si los pares dan $0$.

---

## 5. Serie de cosenos

### Ejemplo guiado 1: $f(t) = t$ en $(0,\pi)$, completar para que la serie sea solo de cosenos

**Paso 1 — paridad.** Solo cosenos ⇒ completamos como **par**.

**Paso 2 — gráfico.** El dato es la recta de $0$ a $\pi$, en negro. Por ser par, la espejamos respecto del eje vertical: en $(-\pi, 0)$ queda $-t$. Después la repetimos cada $2\pi$. Queda una onda triangular.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 170" style="max-width:100%;height:auto;display:block;margin:8px auto;font-family:sans-serif;font-size:11px"><line x1="20" y1="127.0" x2="500" y2="127.0" stroke="#888"/><line x1="260.0" y1="150" x2="260.0" y2="15" stroke="#888"/><line x1="106.7" y1="124.0" x2="106.7" y2="130.0" stroke="#888"/><text x="106.7" y="142.0" text-anchor="middle" fill="#555">−2π</text><line x1="183.3" y1="124.0" x2="183.3" y2="130.0" stroke="#888"/><text x="183.3" y="142.0" text-anchor="middle" fill="#555">−π</text><line x1="336.7" y1="124.0" x2="336.7" y2="130.0" stroke="#888"/><text x="336.7" y="142.0" text-anchor="middle" fill="#555">π</text><line x1="413.3" y1="124.0" x2="413.3" y2="130.0" stroke="#888"/><text x="413.3" y="142.0" text-anchor="middle" fill="#555">2π</text><line x1="257.0" y1="45.6" x2="263.0" y2="45.6" stroke="#888"/><text x="254.0" y="49.6" text-anchor="end" fill="#555">π</text><polyline points="30.0,45.6 106.7,127.0 183.3,45.6" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="183.3,45.6 260.0,127.0 336.7,45.6" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="336.7,45.6 413.3,127.0 490.0,45.6" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="260.0,127.0 336.7,45.6" fill="none" stroke="#1a1a1a" stroke-width="3"/><text x="490" y="18" text-anchor="end" fill="#333">negro: el dato · naranja: lo que completás</text></svg>

**Paso 3 — por tramos y datos.**

$$
f(t) = \begin{cases} -t & -\pi < t < 0 \\ t & 0 < t < \pi \end{cases}, \qquad f(t) = f(t + 2\pi)
$$

$$
T = 2\pi, \qquad L = \pi, \qquad \omega_0 = \frac{\pi}{L} = 1
$$

**Paso 4 — lo que se anula.** $b_m = 0$ por ser $f$ par.

**Paso 5 — valor medio, del gráfico.** El triángulo va de $0$ a $\pi$, así que la altura promedio es la mitad:

$$
\frac{a_0}{2} = \frac{\pi}{2}
$$

**Paso 6 — calcular $a_m$** con $\frac{2}{L}\int_0^L$ sobre el dato, y la integral de §3.4:

$$
a_m = \frac{2}{\pi}\int_0^{\pi} t\cos(mt)\,dt = \frac{2}{\pi}\left[\frac{\cos(mt)}{m^2} + \frac{t\operatorname{sen}(mt)}{m}\right]_0^{\pi}
$$

El término con seno se anula en los dos extremos: en $\pi$ porque $\operatorname{sen}(m\pi) = 0$ y en $0$ porque $t = 0$. Queda:

$$
a_m = \frac{2}{\pi}\left[\frac{\cos(m\pi)}{m^2} - \frac{\cos 0}{m^2}\right] = \frac{2}{\pi}\cdot\frac{(-1)^m - 1}{m^2}
$$

**Paso 7 — separar par e impar.**

- $m$ par: $(-1)^m - 1 = 1 - 1 = 0$, así que $a_m = 0$.
- $m$ impar: $(-1)^m - 1 = -2$, así que $a_m = -\dfrac{4}{\pi m^2}$.

Con $m = 2k+1$:

$$
S(t) = \frac{\pi}{2} - \frac{4}{\pi}\sum_{k=0}^{\infty}\frac{\cos\big((2k+1)t\big)}{(2k+1)^2}
$$

**Chequeo rápido:** en $t = 0$ la función vale $0$. La serie da $\frac{\pi}{2} - \frac{4}{\pi}\left(1 + \frac19 + \frac1{25} + \dots\right)$. Como esa suma da $\frac{\pi^2}{8}$, queda $\frac{\pi}{2} - \frac{\pi}{2} = 0$. ✔

### ✍️ Tu turno 1 — R-A a), de la clase de repaso 2026 · 25 min

Hacé el **ejercicio A, inciso a)** de `exports/practica-repaso-2026-enunciados.pdf`: $f(t) = \pi - t$ en $(0,\pi)$, solo cosenos. Es **el mismo ítem que el 2025-1C T1 Ej1a** y es casi igual al ejemplo guiado: el triángulo ahora tiene el pico arriba, en $t = 0$.

<details>
<summary>Corrección (también en exports/practica-repaso-2026.pdf, corrección A)</summary>

1. **Par.** En $(-\pi, 0)$ va $\pi + t$. Es un triángulo con pico $\pi$ en $t = 0$. $T = 2\pi$, $L = \pi$, $\omega_0 = 1$.
2. $b_m = 0$ y, por gráfico, $\frac{a_0}{2} = \frac{\pi}{2}$.
3. Separás en dos integrales:

$$
a_m = \frac{2}{\pi}\int_0^{\pi}(\pi - t)\cos(mt)\,dt = \underbrace{2\int_0^{\pi}\cos(mt)\,dt}_{=\,0\ (\operatorname{sen}(m\pi)=0)} - \frac{2}{\pi}\int_0^{\pi} t\cos(mt)\,dt = -\frac{2}{\pi}\cdot\frac{(-1)^m - 1}{m^2}
$$

4. $m$ par: $a_m = 0$. $m$ impar: $a_m = \dfrac{4}{\pi m^2}$.

$$
S(t) = \frac{\pi}{2} + \frac{4}{\pi}\sum_{k=0}^{\infty}\frac{\cos\big((2k+1)t\big)}{(2k+1)^2}
$$

Fijate que es el ejemplo guiado con el signo dado vuelta. Tiene sentido: $\pi - t$ es "$\pi$ menos el ejemplo".

</details>

### ✍️ Tu turno 2 — sin-fecha K3521 T2 Ej3a · 25 min

$f(x) = 3x$ en $(0,2)$. Completala para que la STF sea de cosenos y desarrollala. Después, usá el resultado para hallar los $C_m$ de la SEF **sin resolver ninguna integral**. ¿La función tiene simetría de media onda?

> Ojo: acá $L = 2$, así que $\omega_0 = \pi/2$. En la integral de la tabla, $m$ pasa a ser $\frac{m\pi}{2}$.

<details>
<summary>Corrección (resuelta para esta guía, verificada con sympy)</summary>

1. **Par:** $f(x) = 3|x|$ en $(-2,2)$, $f(x) = f(x+4)$. $T = 4$, $L = 2$, $\omega_0 = \frac{\pi}{2}$. Es un triángulo de $0$ a $6$.
2. $b_m = 0$ y $\frac{a_0}{2} = 3$, la mitad de $6$.
3. Calculás $a_m$:

$$
a_m = \frac{2}{2}\int_0^2 3x\cos\!\left(\tfrac{m\pi}{2}x\right)dx = 3\left[\frac{\cos(\frac{m\pi}{2}x)}{(m\pi/2)^2} + \frac{x\operatorname{sen}(\frac{m\pi}{2}x)}{m\pi/2}\right]_0^2 = \frac{12\big((-1)^m - 1\big)}{m^2\pi^2}
$$

4. $m$ par: $0$. $m$ impar: $a_m = -\dfrac{24}{m^2\pi^2}$.

$$
S(x) = 3 - \frac{24}{\pi^2}\sum_{k=0}^{\infty}\frac{\cos\!\big((2k+1)\frac{\pi}{2}x\big)}{(2k+1)^2}
$$

5. **$C_m$ sin integrar**, con $C_m = \frac12(a_m - j\,b_m)$ y $b_m = 0$:

$$
C_0 = 3, \qquad C_m = \frac{a_m}{2} = -\frac{12}{m^2\pi^2}\ (m \text{ impar}), \qquad C_m = 0\ (m \text{ par})
$$

Son reales, como tiene que ser por ser par.

6. **¿Media onda?** No. $3|x|$ nunca es negativa, así que no puede ser que $f(x + 2) = -f(x)$. Además, con media onda el valor medio tendría que ser $0$, y acá es $3$.

</details>

---

## 6. Serie de senos y paso a la SEF

### Ejemplo guiado 2: $f(t) = t$ en $(0,\pi)$, SEF con coeficientes imaginarios puros (2024-2C T1 Ej2)

**Paso 1 — paridad.** Imaginarios puros ⇒ $C_m = \frac12(\cancel{a_m} - j\,b_m)$ ⇒ hay que anular $a_m$ ⇒ **impar**.

**Paso 2 — gráfico.** Espejamos el dato por el origen: en $(-\pi, 0)$, $f(t) = t$ también. La recta sigue de largo. Repetida cada $2\pi$ queda un **diente de sierra**.

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 170" style="max-width:100%;height:auto;display:block;margin:8px auto;font-family:sans-serif;font-size:11px"><line x1="20" y1="85.0" x2="500" y2="85.0" stroke="#888"/><line x1="260.0" y1="150" x2="260.0" y2="15" stroke="#888"/><line x1="106.7" y1="82.0" x2="106.7" y2="88.0" stroke="#888"/><text x="106.7" y="100.0" text-anchor="middle" fill="#555">−2π</text><line x1="183.3" y1="82.0" x2="183.3" y2="88.0" stroke="#888"/><text x="183.3" y="100.0" text-anchor="middle" fill="#555">−π</text><line x1="336.7" y1="82.0" x2="336.7" y2="88.0" stroke="#888"/><text x="336.7" y="100.0" text-anchor="middle" fill="#555">π</text><line x1="413.3" y1="82.0" x2="413.3" y2="88.0" stroke="#888"/><text x="413.3" y="100.0" text-anchor="middle" fill="#555">2π</text><line x1="257.0" y1="38.8" x2="263.0" y2="38.8" stroke="#888"/><text x="254.0" y="42.8" text-anchor="end" fill="#555">π</text><line x1="257.0" y1="131.2" x2="263.0" y2="131.2" stroke="#888"/><text x="254.0" y="135.2" text-anchor="end" fill="#555">−π</text><polyline points="30.0,131.2 183.3,38.8" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="183.3,131.2 336.7,38.8" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="336.7,131.2 490.0,38.8" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="260.0,85.0 336.7,38.8" fill="none" stroke="#1a1a1a" stroke-width="3"/><text x="490" y="18" text-anchor="end" fill="#333">negro: el dato · naranja: lo que completás</text></svg>

**Paso 3 — por tramos y datos.**

$$
f(t) = t \quad \text{en } (-\pi, \pi), \qquad f(t) = f(t + 2\pi), \qquad T = 2\pi,\ L = \pi,\ \omega_0 = 1
$$

**Paso 4.** $a_0 = a_m = 0$ por ser $f$ impar.

**Paso 5 — calcular $b_m$:**

$$
b_m = \frac{2}{\pi}\int_0^{\pi} t\operatorname{sen}(mt)\,dt = \frac{2}{\pi}\left[\frac{\operatorname{sen}(mt)}{m^2} - \frac{t\cos(mt)}{m}\right]_0^{\pi} = \frac{2}{\pi}\left(-\frac{\pi(-1)^m}{m}\right) = -\frac{2(-1)^m}{m}
$$

Acá no hay que separar par e impar, porque no aparece $(-1)^m - 1$. Los valores son $b_1 = 2$, $b_2 = -1$, $b_3 = \frac23$…

$$
S(t) = \sum_{m=1}^{\infty}\frac{-2(-1)^m}{m}\operatorname{sen}(mt) = 2\left(\operatorname{sen}t - \frac{\operatorname{sen}2t}{2} + \frac{\operatorname{sen}3t}{3} - \cdots\right)
$$

**Paso 6 — pasar a SEF.** Es lo que pide el enunciado: los $C_m$. 🧠 $C_m = \frac12(a_m - j\,b_m)$ y $C_0 = \frac{a_0}{2}$.

$$
C_0 = 0, \qquad C_m = \frac12\left(0 - j\cdot\frac{-2(-1)^m}{m}\right) = \frac{(-1)^m}{m}\,j \qquad (m \neq 0)
$$

$$
S(t) = \sum_{\substack{m=-\infty\\ m\neq 0}}^{\infty}\frac{(-1)^m}{m}\,j\,e^{jmt}
$$

Son imaginarios puros, como pedían. ✔ El profe pide aclarar $m \neq 0$ debajo de la sumatoria (video `10`, [41:35]).

> **El espectro de amplitudes**, que a veces lo piden (2025-1C rec), es el gráfico de bastones de $|C_m|$ en función de $m\omega_0$. Acá $|C_m| = \frac{1}{|m|}$: bastones en $\pm1, \pm2, \pm3, \dots$ de altura $1, \frac12, \frac13, \dots$, simétrico respecto del $0$ y con $|C_0| = 0$.

### ✍️ Tu turno 3 — R-A b), de la clase de repaso 2026 · 25 min

**Ejercicio A, inciso b)** de la hoja de práctica: $\pi - t$, solo senos, y pasala a SEF. Es la **misma función que pide el 2025-1C T2 Ej1a**, así que con esto hacés los dos.

<details>
<summary>Corrección</summary>

1. **Impar:** en $(-\pi, 0)$ va $-\pi - t$. Es un diente de sierra que baja: en todo $(0, 2\pi)$ vale $\pi - t$. $T = 2\pi$, $L = \pi$, $\omega_0 = 1$.
2. $a_0 = a_m = 0$.
3. Calculás $b_m$:

$$
b_m = \frac{2}{\pi}\int_0^{\pi}(\pi - t)\operatorname{sen}(mt)\,dt = \frac{2}{m}
$$

Si lo hacés en dos integrales, los términos con $(-1)^m$ se cancelan. Así queda:

$$
S(t) = 2\sum_{m=1}^{\infty}\frac{\operatorname{sen}(mt)}{m}
$$

4. Pasás a SEF:

$$
C_0 = 0, \quad C_m = \frac12\left(0 - j\frac{2}{m}\right) = -\frac{j}{m}, \quad S(t) = \sum_{m\neq0}\left(-\frac{j}{m}\right)e^{jmt}
$$

⚠ En la foto del repaso, el planteo tiene un $2$ de más ($\frac1\pi\cdot 2\int_0^{2\pi}$). El resultado $2/m$ está bien.

</details>

### ✍️ Tu turno 4 — sin-fecha-2 T2 Ej3 · 20 min

$f(x) = x + 1$ en $(0,1)$. Completala con período $T = 2$ para que la STF sea solo de senos y desarrollala. ¿La función completada tiene simetría de media onda? Justificá.

<details>
<summary>Corrección (resuelta para esta guía, verificada con sympy)</summary>

1. **Impar:** en $(-1, 0)$, $f(x) = -f(-x) = -(-x + 1) = x - 1$. $T = 2$, $L = 1$, $\omega_0 = \pi$. Ojo: en $0$ la función **salta** de $-1$ a $1$. Una impar no tiene por qué pasar por $0$ si tiene un salto.
2. $a_0 = a_m = 0$.
3. Calculás $b_m$:

$$
b_m = \frac{2}{1}\int_0^1 (x+1)\operatorname{sen}(m\pi x)\,dx = \frac{2\big(1 - 2(-1)^m\big)}{m\pi}
$$

- $m$ impar: $b_m = \dfrac{6}{m\pi}$.
- $m$ par: $b_m = -\dfrac{2}{m\pi}$.

Como los dos casos son distintos de cero, dejás la serie en $m$:

$$
S(x) = \frac{2}{\pi}\sum_{m=1}^{\infty}\frac{1 - 2(-1)^m}{m}\operatorname{sen}(m\pi x)
$$

4. **¿Media onda? No.** Hay armónicas pares distintas de cero, por ejemplo $b_2 = -\frac1\pi$, y la media onda obliga a que todas las pares sean $0$. Por definición: para $x \in (-1, 0)$, $f(x+1) = (x+1) + 1 = x + 2$ y $-f(x) = 1 - x$. No coinciden.

</details>

---

## 7. Ítem b: cuando la función ya es una suma de senos y cosenos

Si te dan algo como $2\operatorname{sen}x\cos x$, $\cos^2 x$ o $\operatorname{sen}^3 x$, **no se integra nada**. Con una identidad trigonométrica lo escribís como suma de senos y cosenos, y eso **ya es** la serie de Fourier: la serie de una función es única.

**Identidades útiles.** Están en la tabla de integrales, que trae identidades:

$$
2\operatorname{sen}x\cos x = \operatorname{sen}2x, \qquad \cos^2 x = \frac12 + \frac12\cos 2x, \qquad \operatorname{sen}^2 x = \frac12 - \frac12\cos 2x
$$

Si no te acordás de ninguna, usá Euler: $\cos x = \frac{e^{jx} + e^{-jx}}{2}$ y $\operatorname{sen}x = \frac{e^{jx} - e^{-jx}}{2j}$. Multiplicás y reagrupás. Es el camino alternativo que muestra la hoja oficial 2025.

### Ejemplo guiado 3: ¿cuál es la STF de $f(x) = \cos^2 x$?

Usamos $\cos^2 x = \frac12 + \frac12\cos 2x$. Esa es la serie: $\frac{a_0}{2} = \frac12$, $a_2 = \frac12$ y todos los demás coeficientes valen $0$. **Tiene dos términos no nulos**: la constante y la segunda armónica.

### ✍️ Tu turno 5 — 2025-1C Ej1b (T1 y T2) · 10 min

Justificá cuál es la respuesta correcta. La STF de $f(x) = 2\operatorname{sen}(x)\cos(x)$ es:

- (a) la misma función
- (b) una serie con infinitos términos no nulos en senos
- (c) un solo término no nulo
- (d) infinitos términos en cosenos

<details>
<summary>Corrección (RESOLUCIONES-2025, Ej1b)</summary>

$2\operatorname{sen}x\cos x = \operatorname{sen}2x$. La función ya es una sola armónica, así que su STF es ella misma: $b_2 = 1$ y todo lo demás vale $0$. La respuesta es **un solo término no nulo** (c). La hoja oficial lo saca también con exponenciales:

$$
2\cdot\frac{e^{jx} - e^{-jx}}{2j}\cdot\frac{e^{jx} + e^{-jx}}{2} = \frac{e^{2jx} - e^{-2jx}}{2j} = \operatorname{sen}2x
$$

Para justificar, alcanza con escribir la identidad y decir "ya es una armónica, la serie es única".

</details>

---

## 8. Ítem c: simetría de media onda

**Qué es** (está en el ayudamemoria): $f(t + T/2) = -f(t)$. Si corrés la función **medio período** y la **dás vuelta** (espejo respecto del eje horizontal), te queda la misma.

**Consecuencia** 🧠: **una función con media onda solo tiene armónicas impares.** Todos los $a_m$ y $b_m$ con $m$ par valen $0$, y el valor medio también es $0$.

**Cómo completar con dos condiciones** (apunte `02`, p. 5) 🧠. Te dan un pedazo de largo $\ell$ y te piden **paridad y además media onda**. Cada condición duplica el intervalo, así que **el período queda $T = 4\ell$**.

1. **Primera condición, la paridad.** Espejás el dato:
   - **Impar:** espejo por el origen.
   - **Par:** espejo vertical.

   Ahora tenés un pedazo de largo $2\ell$, que es medio período.
2. **Segunda condición, la media onda.** Tomás ese pedazo, lo **corrés $2\ell$** (medio período) y lo **das vuelta**. Así llenás el otro medio.
3. Escribís $f$ por tramos en $(-2\ell, 2\ell)$ con $T = 4\ell$. Cada tramo nuevo sale de la definición: para $t$ en $(\ell, 2\ell)$, $f(t) = -f(t - 2\ell)$.

En este ítem **no se pide la serie**: solo el gráfico y las fórmulas por tramos. Hecho con cuidado, es un punto regalado.

### Ejemplo guiado 4: $f(t) = t^2$ en $[0,1)$, SEF con coeficientes imaginarios puros y media onda (apunte `02`, ejercicio 9a)

**Paso 1 — traducir.** Imaginarios puros ⇒ **impar**. Y además, media onda. Son dos condiciones, así que $T = 4\cdot 1 = 4$ y trabajamos en $(-2, 2)$.

**Paso 2 — impar.** En $(-1, 0)$: $f(t) = -f(-t) = -(-t)^2 = -t^2$.

**Paso 3 — media onda.**
- En $(1, 2)$: $f(t) = -f(t-2)$. Como $t - 2$ cae en $(-1, 0)$, ahí $f(t-2) = -(t-2)^2$. Entonces $f(t) = (t-2)^2$: baja de $1$ a $0$.
- En $(-2, -1)$: $f(t) = -f(t+2)$, con $t + 2 \in (0, 1)$. Entonces $f(t) = -(t+2)^2$.

**Paso 4 — por tramos y gráfico.**

$$
f(t) = \begin{cases} -(t+2)^2 & -2 < t < -1 \\ -t^2 & -1 < t < 0 \\ t^2 & 0 < t < 1 \\ (t-2)^2 & 1 < t < 2 \end{cases}, \qquad f(t) = f(t+4)
$$

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 520 170" style="max-width:100%;height:auto;display:block;margin:8px auto;font-family:sans-serif;font-size:11px"><line x1="20" y1="85.0" x2="500" y2="85.0" stroke="#888"/><line x1="260.0" y1="150" x2="260.0" y2="15" stroke="#888"/><line x1="106.7" y1="82.0" x2="106.7" y2="88.0" stroke="#888"/><text x="106.7" y="100.0" text-anchor="middle" fill="#555">−4</text><line x1="183.3" y1="82.0" x2="183.3" y2="88.0" stroke="#888"/><text x="183.3" y="100.0" text-anchor="middle" fill="#555">−2</text><line x1="221.7" y1="82.0" x2="221.7" y2="88.0" stroke="#888"/><text x="221.7" y="100.0" text-anchor="middle" fill="#555">−1</text><line x1="298.3" y1="82.0" x2="298.3" y2="88.0" stroke="#888"/><text x="298.3" y="100.0" text-anchor="middle" fill="#555">1</text><line x1="336.7" y1="82.0" x2="336.7" y2="88.0" stroke="#888"/><text x="336.7" y="100.0" text-anchor="middle" fill="#555">2</text><line x1="413.3" y1="82.0" x2="413.3" y2="88.0" stroke="#888"/><text x="413.3" y="100.0" text-anchor="middle" fill="#555">4</text><line x1="257.0" y1="48.3" x2="263.0" y2="48.3" stroke="#888"/><text x="254.0" y="52.3" text-anchor="end" fill="#555">1</text><line x1="257.0" y1="121.7" x2="263.0" y2="121.7" stroke="#888"/><text x="254.0" y="125.7" text-anchor="end" fill="#555">−1</text><polyline points="30.0,85.0 31.9,85.1 33.8,85.4 35.8,85.8 37.7,86.5 39.6,87.3 41.5,88.3 43.4,89.5 45.3,90.9 47.3,92.4 49.2,94.2 51.1,96.1 53.0,98.2 54.9,100.5 56.8,103.0 58.7,105.6 60.7,108.5 62.6,111.5 64.5,114.7 66.4,118.1 68.3,121.7" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="68.3,121.7 70.3,118.1 72.2,114.7 74.1,111.5 76.0,108.5 77.9,105.6 79.8,103.0 81.8,100.5 83.7,98.2 85.6,96.1 87.5,94.2 89.4,92.4 91.3,90.9 93.2,89.5 95.2,88.3 97.1,87.3 99.0,86.5 100.9,85.8 102.8,85.4 104.7,85.1 106.7,85.0" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="106.7,85.0 108.6,84.9 110.5,84.6 112.4,84.2 114.3,83.5 116.3,82.7 118.2,81.7 120.1,80.5 122.0,79.1 123.9,77.6 125.8,75.8 127.7,73.9 129.7,71.8 131.6,69.5 133.5,67.0 135.4,64.4 137.3,61.5 139.2,58.5 141.2,55.3 143.1,51.9 145.0,48.3" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="145.0,48.3 146.9,51.9 148.8,55.3 150.8,58.5 152.7,61.5 154.6,64.4 156.5,67.0 158.4,69.5 160.3,71.8 162.3,73.9 164.2,75.8 166.1,77.6 168.0,79.1 169.9,80.5 171.8,81.7 173.7,82.7 175.7,83.5 177.6,84.2 179.5,84.6 181.4,84.9 183.3,85.0" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="183.3,85.0 185.3,85.1 187.2,85.4 189.1,85.8 191.0,86.5 192.9,87.3 194.8,88.3 196.8,89.5 198.7,90.9 200.6,92.4 202.5,94.2 204.4,96.1 206.3,98.2 208.2,100.5 210.2,103.0 212.1,105.6 214.0,108.5 215.9,111.5 217.8,114.7 219.7,118.1 221.7,121.7" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="221.7,121.7 223.6,118.1 225.5,114.7 227.4,111.5 229.3,108.5 231.3,105.6 233.2,103.0 235.1,100.5 237.0,98.2 238.9,96.1 240.8,94.2 242.7,92.4 244.7,90.9 246.6,89.5 248.5,88.3 250.4,87.3 252.3,86.5 254.2,85.8 256.2,85.4 258.1,85.1 260.0,85.0" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="260.0,85.0 261.9,84.9 263.8,84.6 265.8,84.2 267.7,83.5 269.6,82.7 271.5,81.7 273.4,80.5 275.3,79.1 277.3,77.6 279.2,75.8 281.1,73.9 283.0,71.8 284.9,69.5 286.8,67.0 288.7,64.4 290.7,61.5 292.6,58.5 294.5,55.3 296.4,51.9 298.3,48.3" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="298.3,48.3 300.3,51.9 302.2,55.3 304.1,58.5 306.0,61.5 307.9,64.4 309.8,67.0 311.8,69.5 313.7,71.8 315.6,73.9 317.5,75.8 319.4,77.6 321.3,79.1 323.2,80.5 325.2,81.7 327.1,82.7 329.0,83.5 330.9,84.2 332.8,84.6 334.7,84.9 336.7,85.0" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="336.7,85.0 338.6,85.1 340.5,85.4 342.4,85.8 344.3,86.5 346.3,87.3 348.2,88.3 350.1,89.5 352.0,90.9 353.9,92.4 355.8,94.2 357.7,96.1 359.7,98.2 361.6,100.5 363.5,103.0 365.4,105.6 367.3,108.5 369.2,111.5 371.2,114.7 373.1,118.1 375.0,121.7" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="375.0,121.7 376.9,118.1 378.8,114.7 380.8,111.5 382.7,108.5 384.6,105.6 386.5,103.0 388.4,100.5 390.3,98.2 392.3,96.1 394.2,94.2 396.1,92.4 398.0,90.9 399.9,89.5 401.8,88.3 403.7,87.3 405.7,86.5 407.6,85.8 409.5,85.4 411.4,85.1 413.3,85.0" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="413.3,85.0 415.3,84.9 417.2,84.6 419.1,84.2 421.0,83.5 422.9,82.7 424.8,81.7 426.8,80.5 428.7,79.1 430.6,77.6 432.5,75.8 434.4,73.9 436.3,71.8 438.2,69.5 440.2,67.0 442.1,64.4 444.0,61.5 445.9,58.5 447.8,55.3 449.7,51.9 451.7,48.3" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="451.7,48.3 453.6,51.9 455.5,55.3 457.4,58.5 459.3,61.5 461.3,64.4 463.2,67.0 465.1,69.5 467.0,71.8 468.9,73.9 470.8,75.8 472.7,77.6 474.7,79.1 476.6,80.5 478.5,81.7 480.4,82.7 482.3,83.5 484.2,84.2 486.2,84.6 488.1,84.9 490.0,85.0" fill="none" stroke="#d9480f" stroke-width="2"/><polyline points="260.0,85.0 261.9,84.9 263.8,84.6 265.8,84.2 267.7,83.5 269.6,82.7 271.5,81.7 273.4,80.5 275.3,79.1 277.2,77.6 279.2,75.8 281.1,73.9 283.0,71.8 284.9,69.5 286.8,67.0 288.8,64.4 290.7,61.5 292.6,58.5 294.5,55.3 296.4,51.9 298.3,48.3" fill="none" stroke="#1a1a1a" stroke-width="3"/><text x="490" y="18" text-anchor="end" fill="#333">impar + media onda: T = 4·(largo del dato)</text></svg>

**Chequeo visual:** la joroba positiva de $(0,2)$, corrida $2$ y dada vuelta, es la joroba negativa de $(2,4)$. ✔ Y es impar: espejo por el origen. ✔

### ✍️ Tu turno 6 — 2025-1C T1 Ej1c · 15 min

$f(t) = t$ si $0 < t < 1$. Completala en forma gráfica y analítica para que la SEF tenga coeficientes **imaginarios puros** y además $f$ tenga **simetría de media onda**.

<details>
<summary>Corrección (RESOLUCIONES-2025, T1 Ej1c)</summary>

Impar + media onda ⇒ $T = 4$. Impar: en $(-1, 0)$ va $t$. Media onda: en $(1, 2)$ va $-(t-2) = -t + 2$, que baja de $1$ a $0$. En $(-2, -1)$ va $-(t+2) = -t - 2$.

$$
f(t) = \begin{cases} -t-2 & -2 < t < -1 \\ t & -1 < t < 1 \\ -t+2 & 1 < t < 2 \end{cases}, \qquad f(t) = f(t+4)
$$

Es una **onda triangular** que pasa por el origen. En la hoja anotaron "impar" y "S.M.O.".

</details>

### ✍️ Tu turno 7 — 2025-1C T2 Ej1c · 15 min

Mismo dato, $f(t) = t$ en $(0,1)$, pero ahora la SEF tiene que tener coeficientes **reales** y simetría de media onda.

<details>
<summary>Corrección (RESOLUCIONES-2025, T2 Ej1c)</summary>

Reales ⇒ **par**. En $(-1, 0)$ va $-t$. Media onda con $T = 4$: en $(1, 2)$ va $-f(t-2)$, y como $t - 2 \in (-1, 0)$ ahí $f = -(t-2)$, así que queda $t - 2$, que va de $-1$ a $0$. En $(-2, -1)$ va $-t - 2$.

$$
f(t) = \begin{cases} -t-2 & -2 < t < -1 \\ -t & -1 < t < 0 \\ t & 0 < t < 1 \\ t-2 & 1 < t < 2 \end{cases}, \qquad f(t) = f(t+4)
$$

En la hoja anotaron "par" y "S.M.O.". El dibujo es una "V" en el origen y una "Λ" dada vuelta alrededor de $t = \pm 2$.

</details>

---

## 9. Verdadero o falso conceptual: la teoría que tenés que tener clara

La cátedra 2025–2026 mete ítems cortos para justificar. Todos salen de estas siete ideas:

1. **Par** ⇒ solo cosenos, más $a_0/2$, y $C_m$ **reales**.
2. **Impar** ⇒ solo senos, $a_0 = 0$, y $C_m$ **imaginarios puros**.
3. **Impar desplazada** (impar más una constante) ⇒ solo senos, pero con $a_0/2 \neq 0$. Pasa cuando piden "imaginarios puros salvo $C_0 = 3$" (apunte `02`).
4. **Media onda** ⇒ solo armónicas **impares** y valor medio $0$.
5. **$a_0/2 = C_0 =$ valor medio** = la altura promedio de la función en un período.
6. En un **salto**, la serie converge al **promedio** de los dos valores. Por eso dos funciones que difieren solo en esos puntos tienen la misma serie.
7. La serie de una función es **única**. Si ya la escribiste como suma de senos y cosenos, esa es la serie (§7).

### ✍️ Tu turno 8 — R-B, de la clase de repaso 2026 · 15 min

Hacé el **ejercicio B** de la hoja de práctica: tres verdadero o falso, cada uno con su justificación. Corregí con la corrección B de `exports/practica-repaso-2026.pdf`.

---

## Checkpoint: ¿pasás a Laplace?

Pasás si podés hacer esto **sin mirar**:

- [ ] Dado un dato en $(0, a)$, decir $T$, $L$ y $\omega_0$ en 10 segundos.
- [ ] "Reales / cosenos" ⇒ par. "Imaginarios / senos" ⇒ impar. Y por qué, con $C_m = \frac12(a_m - j\,b_m)$.
- [ ] Dibujar la extensión par o impar y escribirla por tramos.
- [ ] Calcular $a_m$ o $b_m$ de una recta con la tabla y evaluar con $(-1)^m$.
- [ ] Pasar a $2k+1$ cuando los pares dan $0$.
- [ ] Pasar de STF a SEF: $C_0 = a_0/2$, $C_m = \frac12(a_m - j\,b_m)$.
- [ ] Completar con paridad y media onda ($T = 4\ell$) y escribir los cuatro tramos.

Si te falla uno, rehacé **solo** el "tu turno" de esa sección. Después, `/registrar` con lo que salió y lo que no, y seguí con `02-laplace-desde-cero`.
