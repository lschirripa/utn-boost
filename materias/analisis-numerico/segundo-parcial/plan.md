# Plan de estudio — Segundo parcial · Análisis Numérico

> Examen: **martes 2026-11-24, 17 h** · Hoy: viernes 2026-11-20 (noche) · **4 días restantes**
> (5 sesiones de estudio contando hoy y la mañana del examen) · **≈ 22 h útiles en total**.
> Restricciones declaradas (Lucho, 2026-11-20): **todavía no arrancaste**; vie 20 a la noche
> ≈ 1 h 45 · sáb 21 hasta las 15 h ≈ 5 h · dom 22 solo la mañana ≈ 3 h 30 · lun 23 todo el
> día ≈ 8 h · mar 24 hasta salir para el examen ≈ 4 h (nada nuevo). Punto de partida casi en
> cero; **ajuste por mínimos cuadrados no entra**; solo se permite el ayudamemoria oficial
> (pág. 4) y calculadora.
> Fuentes: [`estrategia.md`](estrategia.md) · [`examenes/INDICE.md`](examenes/INDICE.md) ·
> [`examenes/resueltos/RESOLUCIONES-2025.md`](examenes/resueltos/RESOLUCIONES-2025.md) ·
> guías `apuntes/md/01–06` (para leer, usá los HTML de `apuntes/html/`; cada guía `01–05`
> arranca con un recuadro **🧭 Ruta corta** que dice lo mismo que este plan).

---

## ⚠️ ¿Es factible? Sí para el 6; el 8 queda abierto pero sin red

**Respuesta corta:** con 22 h **alcanza para asegurar el 6 con margen y pelear el 8**, pero
solo en **núcleo estricto** y sin colchón para un día malo. La cuenta:

| | Horas |
|---|---|
| Las 5 guías completas (según sus encabezados) | ≈ 24 h |
| Núcleo estricto de las 5 guías (lo que arma este plan) | **≈ 17 h** |
| Repaso `06` a ciegas + corrección + resúmenes (martes) | ≈ 4 h |
| Hoja de memoria (lunes) | 0 h 30 |
| **Total planificado** | **≈ 21 h 30** |
| Disponible | ≈ 22 h 15 |

Entra, con **≈ 45 min de margen en cuatro días**. No es un plan cómodo: es un plan que cierra.

**Qué alcanza con 22 h**

- **Los tres ejercicios seguros, bien preparados (6 puntos):** Ej4 integración (4/4 la misma
  consigna en 2025), Ej5 ecuaciones diferenciales (Lipschitz + Euler 2/2 en el parcial;
  Euler, Heun y Runge-Kutta 4 están en el ayudamemoria) y Ej3 interpolación (valores tapados
  4/4 + conteo 3/4). Se estudian **primero** (viernes, sábado y domingo) y se repasan dos
  veces más (lunes en frío y martes con el repaso).
- **Ej1 raíces, una pasada completa (el colchón y la llave del 8):** tres ítems
  independientes; separar raíces, bisección y Newton-Raphson suman aunque falle uno.
- **Ej2 sistemas lineales, solo lo más tomado:** decidir si converge (3/4) y número de
  condición (1/4 + repaso). Es el menos predecible: se prepara, **no se cuenta con él**.

**Qué queda afuera (decidido, no es un descuido)**

- **Los 5 checkpoints** de las guías y **el simulacro de `/simulacro`**. El único examen a
  ciegas y con reloj es el repaso `06`, el martes a la mañana: **hace de simulacro**.
- **Tres ítems 🔴 de recuperatorio**, que quedan como "si sobra": `01` 3.D (separar raíces
  mostrando el gráfico, 2025-07-11 R2 Ej1a), `01` 7.C (iterar punto fijo, 2025-07-07 R1 Ej1c,
  1/4) y `02` 6.A (reordenar + una iteración de Gauss-Seidel, 2025-07-11 R2 Ej2b).
- **Todos los ⚪** (práctica extra de guía y teórico) y **todo lo plegado como "⚪ Se toma
  poco"**: `01` §9 · `03` §5, §9, §10 · `04` §7 · `05` §9. Además `02` §4 completa (de
  Jacobi solo §4.2–4.3, armar `T`), §5 y §6 (Gauss-Seidel), `03` §4 y §6.4, `05` §8.
- **Ajuste:** carpeta `ajuste/` y `06` ej. 5 y 14.
- **Los 🟠 (repaso 2026) no se hacen en las guías:** son los mismos ejercicios de `06` y se
  rinden a ciegas el martes. Hasta entonces **no abras `06`**.

**¿Necesitás más tiempo algún día? No es imprescindible para el 6. Para el 8, sí conviene:
el domingo a la tarde, +3 h.** Es donde más rinde cada hora agregada, por tres motivos:

1. **El lunes carga dos temas nuevos el día previo** (raíces y sistemas, 6 h 10 de material
   nuevo sobre 8 h). Con +3 h el domingo, **raíces se hace el domingo a la tarde** (§3, §8,
   §5.3, §6.2 y §7 con 7.A; 7.B pasa al lunes) y el lunes queda con un solo tema nuevo.
2. **El repaso `06` pasa al lunes a la tarde** (2 h 35 + corrección). Así los errores
   aparecen con una noche y una mañana para corregirlos, y no tres horas antes del examen.
3. **El martes queda liviano de verdad:** rehacer lo que falló en `06` (≈ 1 h), `01` 3.D y
   7.C (25 min), los checkpoints de `04` y `03` con reloj (≈ 1 h 05) y los cinco resúmenes
   (40 min). Terminás a las 12 en vez de a las 13.

Con esas 3 h también entra `02` §6.1 + **6.A** (una iteración de Gauss-Seidel, 30 min) el
lunes. El resto de los días no mueve la aguja igual: el sábado no hay más horas (cortás a
las 15), y sumar el viernes a la noche solo adelanta 6.B. Si el domingo a la tarde no se
puede, la segunda mejor opción es **+1 h el lunes** para `02` §6.1 + 6.A y el checkpoint
de `04`.

### Los ejercicios, en orden de seguridad

| Orden | Ejercicio | Por qué | Núcleo | Cuándo |
|---|---|---|---|---|
| 1 | **Ej4 Integración** (2 pts) | 4/4 la misma consigna en 2025 + repaso ej. 11. Una sola receta; el error está en el ayudamemoria. | `04` ≈ 4 h | vie + sáb |
| 2 | **Ej5 Ecuaciones diferenciales** (2 pts) | Parcial 2025: Lipschitz + Euler 2/2. Las fórmulas están en el ayudamemoria. | `05` ≈ 3 h | sáb + lun |
| 3 | **Ej3 Interpolación** (2 pts) | Valores tapados 4/4 con la misma mecánica; el conteo es una regla de tres líneas. | `03` ≈ 3 h 40 | dom + lun |
| Colchón | **Ej1 Raíces** (2 pts) | Tres ítems independientes; nada en el ayudamemoria. Con este se llega al 8. | `01` ≈ 3 h 30 | lun |
| El variable | **Ej2 Sistemas** (2 pts) | 3 consignas distintas en 4 hojas + una cuarta en el repaso. Es **lo primero que se recorta**. | `02` ≈ 2 h 40 | lun |

**Regla de trabajo:** cada "tu turno" 🔴 se hace **en papel, con calculadora y sin mirar**, y
se corrige contra la resolución plegada. Los tiempos de cada bloque ya incluyen la
corrección. Si un bloque se pasa más de 15 min, cortá y seguí: lo pendiente se anota y va a
"Si te atrasás". Cerrá cada día con `/registrar`.

**Convención de las guías:** 🔴 parcial 2025 (obligatorio) · 🟠 repaso 2026 (reservado para
el martes) · ⚪ extra (opcional). Lo plegado como "⚪ Se toma poco" se saltea.

---

## Plan día por día

| Día | Horas | Foco | Entregable del día |
|---|---|---|---|
| **Vie 2026-11-20** (noche) | 1 h 45 | 🔴 **Integración**: idea, Trapecios y la receta de elegir `h` (`04` §0–§3, §6) | Ej4 del **2025-06-30 T1** (6.A) resuelto sin mirar |
| **Sáb 2026-11-21** (hasta las 15) | 4 h 45 | 🔴 Cierre de **integración** (`04` §6, §4, §5, §8) + 🔴 **ecuaciones diferenciales** (`05` §0–§5) | Ej4 del **2025-06-30 T2** (6.B), **2025-07-07 R1** (6.C) y **2025-07-11 R2** a, b, c (6.D, 4.A); Ej5 del **2025-06-30 T1 y T2** (Tu turno 3.1, 3.2, 4.1, 4.2) y del **2025-07-07 R1** (5.1) |
| **Dom 2026-11-22** (mañana) | 3 h 20 | 🔴 **Interpolación** núcleo (`03` §3, §6, §7, §8, §11.1) | Ej3a del **2025-06-30 T1** (7.A) y **T2** (ejemplo guiado 7) y del **2025-07-07 R1** (7.B); Ej3 b/c del **2025-07-07 R1** (8.A, 8.B) y del **2025-07-11 R2** (8.C) |
| **Lun 2026-11-23** (todo el día) | 7 h 40 | Cierre de los seguros (1 h) + 🔴 **raíces** (`01`, 3 h 30) + 🔴 **sistemas** (`02`, 2 h 40) + hoja de memoria | Ej3a y Ej5 a/b del **2025-07-11 R2** (`03` 7.C, `05` 6.1 y 7.1); Ej1 del **2025-06-30 T1 y T2**, **2025-07-07 R1** (a, b) y **2025-07-11 R2** (b, c); Ej2 del **2025-06-30** (T1 = T2), **2025-07-07 R1** y **2025-07-11 R2** a; hoja de memoria escrita |
| **Mar 2026-11-24** (9 a 13 h) | 3 h 55 | **Repaso `06` a ciegas y cronometrado** (13 ejercicios, 2 h 35) + corrección + los cinco "Resumen en una página". **Nada nuevo.** | 13 ejercicios corregidos con el tablero; hoja de memoria final. **Examen a las 17 h** |

**Total: 21 h 25** de ≈ 22 h 15 disponibles.

### Viernes 2026-11-20 (noche, 1 h 45) — la receta del Ej4 (`04-integracion-desde-cero`)

| Bloque | Secciones | "Tu turno" 🔴 |
|---|---|---|
| 1 · 15 min | `04` §0, §1, §2 (lectura rápida: qué te toman y qué está en el ayudamemoria) | — |
| 2 · 25 min | **§3 Trapecios con tabla** (§3.1, §3.2 y ejemplo guiado 1, rehaciendo la cuenta) | — (3.A es ⚪) |
| 3 · 45 min | **§6 elegir `h`**: §6.1, **§6.2 la receta**, §6.3, ejemplo guiado 3 (el caso fácil) y **ejemplo guiado 4** (el caso de parcial) rehecho en papel | — |
| 4 · 20 min | — | **6.A** (2025-06-30 T1, Ej4 completo) |

Si hoy solo llegás a 1 h 30, **6.A pasa a ser lo primero del sábado**. No cortes el bloque 3.

### Sábado 2026-11-21 (hasta las 15 h, 4 h 45) — cierre de `04` + `05-ecuaciones-diferenciales-desde-cero`

| Bloque | Secciones | "Tu turno" 🔴 | Reservado 🟠 (martes) |
|---|---|---|---|
| 1 · 60 min | `04` §6.2 de memoria: escribí la receta sin mirar antes de empezar | **6.B** (2025-06-30 T2), **6.C** (2025-07-07 R1, la variante con logaritmo), **6.D** (2025-07-11 R2 a, pide `N`) | 6.E |
| 2 · 35 min | `04` **§4 Simpson y "N par"** (§4.1, §4.2, ejemplo guiado 2) | **4.A** (2025-07-11 R2 b y c) | 4.E |
| 3 · 20 min | `04` **§5 conceptuales del error** (§5.1–§5.4): solo leer y subrayar las cuatro reglas | — | 5.A, 5.B |
| 4 · 15 min | `04` **§8 derivadas desde tabla**: §8.2, §8.3 y ejemplo guiado 6 (leído). §7 plegada: saltear | — | 7.B, 8.C |
| 5 · 10 min | `04` "Resumen en una página" + "Errores típicos" | — | — |
| 6 · 15 min | `05` §0, §1, §2 | — | — |
| 7 · 50 min | `05` **§3 Lipschitz** (§3.1, **§3.2 la receta por derivada parcial**, §3.3 leída, §3.4; ejemplos guiados 1–3) | **Tu turno 3.1** (2025-06-30 T1 a), **Tu turno 3.2** (T2 a) | Tu turno 3.5 |
| 8 · 50 min | `05` **§4 Euler** (§4.1–§4.3, ejemplo guiado 4), con el ayudamemoria al lado | **Tu turno 4.1** (2025-06-30 T1 b), **Tu turno 4.2** (T2 b) | — |
| 9 · 30 min | `05` **§5 Heun** (§5.1–§5.3, ejemplo guiado 5) | **Tu turno 5.1** (2025-07-07 R1, Ej5 completo) | — |

Quedan 15 min de margen. Si a las 14:30 no llegaste a Heun, **dejalo para el lunes** junto
con Runge-Kutta 4: Lipschitz + Euler es lo que cayó en las dos hojas del parcial.

### Domingo 2026-11-22 (mañana, 3 h 20) — `03-interpolacion-desde-cero`

| Bloque | Secciones | "Tu turno" 🔴 | Reservado 🟠 (martes) |
|---|---|---|---|
| 1 · 10 min | `03` §0, §1, §2 | — | — |
| 2 · 25 min | **§3 teorema de existencia y unicidad** (§3.1–§3.4 y ejemplo guiado 1). §4 y §5 (plegada): saltear | — (3.A–3.C son ⚪) | — |
| 3 · 45 min | **§6 tabla de diferencias divididas**: §6.1, §6.2, **ejemplo guiado 4** armando la tabla a mano, §6.3 cómo se lee el grado. §6.4 (regresivo): saltear | — (6.A es ⚪) | 6.B |
| 4 · 75 min | **§7 valores tapados**: §7.1, §7.2, ejemplo guiado 6 (leído) y **ejemplo guiado 7** (2025-06-30 T2 a) rehecho sin mirar | **7.A** (2025-06-30 T1 a), **7.B** (2025-07-07 R1 a) | 7.D, 7.E |
| 5 · 30 min | **§8 contar polinomios y decir el grado**: §8.1, ejemplo guiado 8 y **ejemplo guiado 9** (2025-06-30 T1 b) | **8.A**, **8.B** (2025-07-07 R1 b y c), **8.C** (2025-07-11 R2 b) | 8.D, 8.E |
| 6 · 15 min | **§11.1 derivada segunda central** (§11.2 y §11.3 leídas) + "Resumen en una página". §9 y §10 (plegadas): saltear | — | — |

Quedan 10 min de margen. **7.C** (2025-07-11 R2 a) queda a propósito para el lunes: es el
repaso en frío del Ej3.

> **Si agregás la tarde del domingo (+3 h):** hacé raíces con los bloques 2a–2e del lunes y
> el 2f solo hasta 7.A (≈ 3 h). El lunes y el martes cambian como dice la sección de arriba.
> Avisá y se recalcula con `/plan`.

### Lunes 2026-11-23 (todo el día, 7 h 40) — cierre de seguros + `01-raices` + `02-sistemas-lineales`

Primero se cierran los seguros (1 h); después raíces con la cabeza fresca; sistemas a la
tarde. El orden interno de raíces va de lo más tomado a lo menos tomado, para que un corte
caiga sobre punto fijo y no sobre Newton-Raphson.

| Bloque | Secciones | "Tu turno" 🔴 | Reservado 🟠 (martes) |
|---|---|---|---|
| 1a · 20 min | En frío, sin releer nada | `03` **7.C** (2025-07-11 R2 a) | — |
| 1b · 40 min | `05` **§6 Runge-Kutta 4** (§6.1–§6.3, ejemplo guiado 6) y **§7 clasificar una fórmula** (§7.1–§7.3). §8 y §9: saltear | `05` **Tu turno 6.1** (2025-07-11 R2 a), **Tu turno 7.1** (R2 b) | Tu turno 7.2 |
| 2a · 15 min | `01` §0, §1, §2 y §4 (cuándo parar) | — | — |
| 2b · 50 min | `01` **§3 separar raíces** (§3.1–§3.3, ejemplos guiados 1 y 2) | **3.A** (2025-06-30 T1 a), **3.B** (T2 a), **3.C** (2025-07-07 R1 a) | — |
| 2c · 50 min | `01` **§8 Newton-Raphson** (§8.1, §8.2, **§8.3 cómo elegir `x₀`**) y **ejemplo guiado 10** (2025-06-30 T1 b) rehecho | **8.A** (2025-06-30 T2 c), **8.B** (2025-07-11 R2 b) | — |
| 2d · 30 min | `01` **§5.3 la cuenta de iteraciones de bisección** + ejemplo guiado 5 (§5.1–§5.2 leídas) | **5.A** (2025-06-30 T1 c), **5.B** (2025-07-11 R2 c) | 5.E |
| 2e · 10 min | `01` **§6.2 la regla del extremo fijo** de Regula Falsi + ejemplo guiado 6. Nada más de §6 | — | 6.D |
| 2f · 50 min | `01` **§7 punto fijo**: §7.1, **§7.2 las dos condiciones**, §7.3 y ejemplo guiado 7 | **7.A** (2025-06-30 T2 b), **7.B** (2025-07-07 R1 b) | 7.G |
| 2g · 5 min | `01` "Resumen en una página". §9 (plegada) y Checkpoint: saltear | — | — |
| 3a · 10 min | `02` §0, §1, §2 | — | — |
| 3b · 25 min | `02` **§3 herramientas**: §3.1 diagonal dominante, §3.2 autovalores y radio espectral, §3.3 normas | — (3.A–3.C son ⚪) | — |
| 3c · 15 min | `02` **§4.2 y §4.3**: cómo salen `T` y `C` de Jacobi y la fórmula del ayudamemoria. El resto de §4, §5 y §6: saltear | — | — |
| 3d · 40 min | `02` **§7 ¿converge o no?** completa: §7.1 tres teoremas, §7.2 receta, §7.3 reordenar, §7.4 hallar `k`, §7.5 radio espectral | — | 7.C |
| 3e · 45 min | — | **7.A** (2025-06-30 T1 = T2, Ej2 completo), **7.B** (2025-07-07 R1, Ej2 completo) | — |
| 3f · 20 min | `02` **§8 número de condición**: §8.2 la fórmula y el criterio + ejemplo guiado 6 | **8.A** (2025-07-11 R2 a) | 8.B |
| 3g · 5 min | `02` "Resumen en una página" | — | — |
| 4 · 30 min | **Hoja de memoria** (lo que NO está en el ayudamemoria), escrita sin mirar y corregida contra los resúmenes: Bolzano, cota de bisección y "suficientes, no necesarias", las dos condiciones de punto fijo, Newton-Raphson, regla de Regula Falsi · los tres teoremas de convergencia y `K(A)` · teorema de unicidad y regla del conteo · Trapecios, Simpson y derivada segunda central · `L = máx│∂f/∂y│` | — | — |

Quedan 20 min de margen. **Si sobran**, en este orden: `02` §6.1 + **6.A** (2025-07-11 R2 b,
una iteración de Gauss-Seidel), `01` **3.D** (2025-07-11 R2 a) y `01` **7.C** (2025-07-07 R1 c).

### Martes 2026-11-24 (9 a 13 h, 3 h 55) — el repaso `06` hace de simulacro

Nada nuevo: todo lo de hoy es práctica de lo ya estudiado. Cortá a las **13 h** pase lo que
pase, comé y salí con tiempo.

| Hora | Qué | Entregable |
|---|---|---|
| 9:00 · 2 h 35 | **`06` a ciegas y cronometrado**, solo con el ayudamemoria (pág. 4) y calculadora, respetando el tiempo de cada título y **en el orden del examen que vas a usar**: integración **11, 10, 9** (35 min) → ecuaciones diferenciales **13, 12** (17 min) → interpolación **3, 4, 7, 8** (52 min) → raíces **1, 2** (28 min) → sistemas **6, 15** (23 min). Salteá el **5** y el **14** (ajuste). | 13 ejercicios en papel |
| 11:35 · 40 min | Corrección contra el "Tablero de resultados" de `06`. Marcá ✅ / 🟡 / ❌. Lo ❌ de un ejercicio seguro (Ej3, Ej4, Ej5): releé **solo** la receta de esa sección. | Lista corta de errores |
| 12:15 · 40 min | Los cinco **"Resumen en una página"** + "Errores típicos" de `01–05`, y la hoja de memoria escrita una última vez. | Hoja de memoria final |

**No entra un simulacro además del repaso.** `/simulacro` y los 5 checkpoints quedan afuera
con 22 h; el repaso cronometrado cumple esa función (13 ejercicios nuevos, con reloj y sin
apuntes). **En el examen:** primero **Ej4 y Ej5**, después **Ej3**, después **Ej1**; el **Ej2**
al final.

---

## Si te atrasás

Los recortes van **en este orden**; no se pasa al siguiente sin haber aplicado el anterior.

1. **Sistemas (`02`) se achica primero.** Bloque 3f (número de condición) pasa a "leer §8.2
   y el ejemplo guiado 6" sin hacer 8.A (−15 min). Después se cae 7.B y queda solo 7.A, que
   es el sistema textual del parcial (−20 min).
2. **Punto fijo (`01` §7) se reduce** a §7.2 + 7.A (las dos condiciones); 7.B se cae
   (−20 min).
3. **Heun y Runge-Kutta 4 (`05` §5, §6) pasan a "ejemplo guiado leído"** sin hacer 5.1 ni
   6.1 (−35 min): las fórmulas están en el ayudamemoria y en el parcial 2025 cayó Euler.
4. **El martes se acorta `06`:** se caen los ejercicios 6 y 15 de sistemas y el 8 conceptual
   (−28 min).
5. **Sistemas entero se reduce a `02` "Resumen en una página" + 7.A** (≈ 40 min en vez de
   2 h 40). Es resignar el Ej2 y jugar a los otros cuatro.
6. **Raíces se queda en §3 + §8 + §5.3** (separar, Newton-Raphson y bisección: ≈ 2 h 15),
   sin punto fijo ni Regula Falsi.

**Lo que no se recorta nunca:** `04` §6 con 6.A–6.D, `05` §3–§4 con Tu turno 3.1, 3.2, 4.1 y
4.2, y `03` §6–§8 con 7.A, 7.B y 8.A–8.C. Esos son los 6 puntos.

- **Se pierde el viernes entero:** el sábado arranca por `04` §3 y §6 (1 h 45) y Heun pasa
  al lunes; aplicá el recorte 1.
- **Se pierde el domingo:** interpolación pasa al lunes a la mañana y sistemas se reduce
  como en el recorte 5. Recalculá con `/plan`.

---

## Qué cambió respecto del plan anterior

- **Horas totales: de ≈ 40 h (5 días de 8 h desde el jueves 19) a ≈ 22 h** — el jueves no
  se estudió y la disponibilidad real es la declarada el 2026-11-20.
- **Orden invertido: primero los seguros** (integración → ecuaciones diferenciales →
  interpolación) y recién después raíces y sistemas. Antes iba raíces → sistemas →
  integración → ecuaciones diferenciales → interpolación. Motivo: con menos horas, lo que
  queda para el final es lo que se recorta, y tiene que ser el Ej2, no el Ej4.
- **Núcleo estricto:** cada guía baja de 4–6 h a 2 h 40–4 h. Se caen los "tu turno" ⚪ que
  el plan anterior traía como núcleo (`02` 3.B, 3.C; `03` 3.C, 6.A; `04` 3.A, 5.C, 8.A) y pasan a "si sobra" `01` 3.D y 7.C y `02` 6.A.
- **Se caen los 5 checkpoints y el simulacro de `/simulacro`** — no entran en 22 h.
- **El repaso `06` pasa del lunes al martes a la mañana** y hace de simulacro; el lunes es
  día de material nuevo (raíces y sistemas), cosa que el plan anterior evitaba.
- **Sistemas se reduce a convergencia + número de condición** (sin Jacobi iterado ni
  Gauss-Seidel) — es el ejercicio menos predecible y el primero en recortarse.
- **Nueva convención de las guías:** 🔴 / 🟠 / ⚪ en cada "tu turno" y secciones plegadas
  "⚪ Se toma poco"; el plan cita los mismos ids de sección y de ejercicio que antes.

---

*Generado el 2026-11-20 con: MATERIA.md (fecha del examen: 2026-11-24), estrategia.md
(prioridades, banco y reserva a ciegas de `06`), registro.md (vacío, sin sesiones aún),
que-saltear.md (no existe), plan.md anterior (2026-11-19, para el diff), input del usuario
(disponibilidad: vie ≈ 1,5–2 h a la noche, sáb ≈ 5 h hasta las 15, dom ≈ 3,5 h a la mañana,
lun ≈ 8 h, mar ≈ 4 h antes de rendir a las 17 h; todavía no arrancó; primero los ejercicios
seguros). Después de cada sesión: `/registrar`; si cambia el panorama (por ejemplo, si
sumás la tarde del domingo): `/plan`.*
