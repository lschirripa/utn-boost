# Plan de estudio — Segundo parcial · Análisis Numérico

> Examen: **martes 2026-11-24** · Hoy: jueves 2026-11-19 · **5 días restantes** (5 útiles:
> jue 19 → lun 23; el martes 24 solo repaso liviano).
> Restricciones declaradas: **punto de partida casi en cero** en los 5 temas; **ajuste por
> mínimos cuadrados no entra** (Lucho, 2026-11-18); solo se permite el ayudamemoria oficial
> (pág. 4). Objetivo: **asegurar el 6** (3 ejercicios de 5) y dejar abierto el 8.
> **Supuesto de disponibilidad (corregilo si no es así):** el mismo del primer parcial
> (`../primer-parcial/plan.md`): días enteros, **≈ 8 h útiles por día**, sin días bloqueados.
> Con otra disponibilidad, avisá y se recalcula con `/plan`.
> Fuentes: [`estrategia.md`](estrategia.md) · [`examenes/INDICE.md`](examenes/INDICE.md) ·
> [`examenes/resueltos/RESOLUCIONES-2025.md`](examenes/resueltos/RESOLUCIONES-2025.md) ·
> guías `apuntes/md/01–06` (para leer, usá los HTML de `apuntes/html/`).

---

## ⚠️ No entra todo: se hace solo el núcleo de cada guía

Son **5 temas 🔴 desde cero en 4 días** (el quinto es de simulacro). Las 5 guías completas
suman ≈ 24 h según sus encabezados; con ≈ 32 h en 4 días entrarían justas y sin margen para
corregir errores. Por eso cada guía se hace **en modo núcleo**:

- **Núcleo (obligatorio):** las secciones de lo que cayó en 2025 o en el repaso 2026, con sus
  ejemplos guiados y **solo los "tu turno" que son ítems de parcial 2025**, más el checkpoint.
- **Reservado para el lunes:** los "tu turno" marcados **"repaso 2026"** no se hacen en la
  guía: son los mismos ejercicios de `06`, que el lunes 23 se rinde **a ciegas y con reloj**.
  No abras `06` antes.
- **Opcional:** el resto de la práctica (ejercicios de la guía de la cátedra y del teórico).
  Solo si terminaste el núcleo del día antes de tiempo, o como refuerzo si un checkpoint salió
  mal.
- **Cae sin culpa:** ajuste (carpeta `ajuste/`; `06` ej. 5 y 14), Lagrange y Newton-Gregory
  equiespaciado (`03` §5, §9, §10), tablas largas de Jacobi/Gauss-Seidel (`02` 4.A–4.C,
  6.B–6.E), `h` para Simpson como ejercicio propio (`04` §7), RK2 y sistemas de EDO (`05` §9),
  órdenes y raíces múltiples (`01` §9, salvo el recuadro).

### Los ejercicios "seguros" para el 6

| Orden | Ejercicio | Por qué es seguro | Qué asegurar |
|---|---|---|---|
| 1 | **Ej4 Integración** (2 pts) | En las 4 hojas 2025 fue **la misma consigna** (elegir `h` para Trapecios) y el repaso 2026 la repitió. Un solo ítem, una sola receta; el error está en el ayudamemoria. | `04` §6: `f''`, `f''' = 0`, extremos contra puntos críticos, despejar `h`, elegir un `h` "lindo". Y "¿se puede Simpson?" = `N` par. |
| 2 | **Ej5 Ecuaciones diferenciales** (2 pts) | En el parcial cayó 2/2 Lipschitz + Euler de 3 filas. Euler, Heun y RK4 **están en el ayudamemoria**: es armar la tabla sin errar la calculadora. | `05` §3 (Lipschitz por derivada parcial) y §4; una tabla de Heun y una fila de RK4. |
| 3 | **Ej3 Interpolación** (2 pts) | El ítem (a) cayó 4/4 con la misma mecánica (tabla de diferencias divididas → polinomio → evaluar en las `x` tapadas) y el (b) sale de una regla de tres líneas. | `03` §6–§8. |
| Colchón | **Ej1 Raíces** | Tres ítems independientes (0,5 + 0,75 + 0,75): separar raíces (4/4), iteraciones de bisección (cuenta fija) y Newton-Raphson (3/4). Aunque falle uno, suma. Con este se llega al 8. | `01` §3, §5, §8. |
| El variable | **Ej2 Sistemas** | En 4 hojas hubo 3 consignas distintas (radio espectral, `k`, número de condición + Gauss-Seidel) y el repaso sumó una cuarta. Se prepara, pero **no se cuenta con él** para el 6. | `02` §7 completa. |

**Regla de trabajo:** cada "tu turno" se hace **en papel, con calculadora y sin mirar**, y se
corrige contra la resolución plegada. El checkpoint de cada guía va **con reloj (25 min)** y
solo con la pág. 4 del ayudamemoria. Si un checkpoint sale mal, antes de seguir rehacé el
ítem de parcial gemelo. Terminá cada día con `/registrar`: lo que falló manda el domingo a la
tarde y el lunes.

---

## Plan día por día

| Día | Foco | Entregable del día |
|---|---|---|
| **Jue 2026-11-19** | 🔴 **Raíces** — guía `01` (núcleo ≈ 6 h) + herramientas de matrices (`02` §3, ≈ 1 h) | Ej1 completo de 2025-06-30 T1 y T2, 2025-07-07 R1 y 2025-07-11 R2 hechos como "tu turno"; **checkpoint de `01`** con reloj |
| **Vie 2026-11-20** | 🔴 **Sistemas lineales** — guía `02` (≈ 4,5 h) + 🔴 **integración, la receta estrella** (`04` §1–§3 y §6, ≈ 3 h) | Ej2 de 2025-06-30 (T1 = T2), 2025-07-07 R1 y 2025-07-11 R2; **checkpoint de `02`**; Ej4 de 2025-06-30 T1 y T2 |
| **Sáb 2026-11-21** | 🔴 **Integración** — cierre de `04` (≈ 3,5 h) + 🔴 **ecuaciones diferenciales** — guía `05` (≈ 4 h) | Ej4 de 2025-07-07 R1 y 2025-07-11 R2 (a, b, c); **checkpoint de `04`**; Ej5 de las 4 hojas; **checkpoint de `05`** |
| **Dom 2026-11-22** | 🔴 **Interpolación** — guía `03` (≈ 5,5 h) + hoja de memoria y errores de la semana (≈ 2 h) | Ej3 a/b de 2025-06-30 T1 y T2, 2025-07-07 R1 y 2025-07-11 R2; **checkpoint de `03`**; checklist teórico de raíces, sistemas e interpolación **escrito de memoria** |
| **Lun 2026-11-23** | 🔴 **Repaso 2026 (`06`) a ciegas y cronometrado** + **simulacro** (`/simulacro`) | 13 ejercicios de `06` en ≈ 2 h 35 corregidos con el tablero; simulacro completo en 2 h corregido; errores en `/registrar` |
| **Mar 2026-11-24** | Liviano: los 5 "Resumen en una página" + hoja de memoria. **Nada nuevo.** | Examen |

### Jueves 2026-11-19 — Raíces (`01-raices-desde-cero`)

De raíces **no hay nada en el ayudamemoria**: todo lo de hoy va de memoria.

| Bloque | Secciones | "Tu turno" núcleo (parcial 2025) | Opcional | Reservado (lunes) |
|---|---|---|---|---|
| 1 · ≈ 1 h 30 | §0, §1, §2, **§3 separar raíces** (ejemplos guiados 1–3) | **3.A** (T1 a), **3.B** (T2 a), **3.C** (R1 a), **3.D** (R2 a) | 3.E | — |
| 2 · ≈ 50 min | §4 cuándo parar, **§5 bisección y la cuenta de iteraciones** (5.3 es lo que se toma) | **5.A** (T1 c), **5.B** (R2 c) | 5.C, 5.D | 5.E |
| 3 · ≈ 20 min | §6 Regula Falsi: solo **§6.2 la regla del extremo fijo** + ejemplo guiado 6 | — | 6.A | 6.D |
| 4 · ≈ 1 h 30 | **§7 punto fijo**: las dos condiciones y cómo justificarlas (ejemplos guiados 7–8) | **7.A** (T2 b), **7.B** (R1 b), **7.C** (R1 c) | 7.D, 7.E, 7.F, 7.H | 7.G |
| 5 · ≈ 1 h 15 | **§8 Newton-Raphson** (8.3: cómo elegir `x₀`); rehacé el **ejemplo guiado 10** (T1 b) sin mirar | **8.A** (T2 c), **8.B** (R2 b) | 8.C, 8.D, 8.E, 8.F | — |
| 6 · ≈ 40 min | §9 solo el recuadro de órdenes · "Resumen en una página" · "Errores típicos" · **Checkpoint (25 min, con reloj)** | — | 9.A, 9.B | — |
| 7 · ≈ 1 h | Adelanto de mañana: `02` §1, §2 y **§3** (diagonal dominante, autovalores y radio espectral, normas) | `02` **3.B**, **3.C** | `02` 3.A | — |

Cierre: escribí en una hoja, de memoria, Bolzano, la cota de bisección con su frase
("suficientes, no necesarias"), las dos condiciones de punto fijo y la fórmula de
Newton-Raphson. Esa hoja se va completando cada día.

### Viernes 2026-11-20 — Sistemas lineales (`02`) + la receta del Ej4 (`04` §6)

| Bloque | Secciones | "Tu turno" núcleo (parcial 2025) | Opcional | Reservado (lunes) |
|---|---|---|---|---|
| 1 · ≈ 1 h | `02` **§4 Jacobi** (ejemplo guiado 1 y §4.3: la trampa de signos de `T_J = D⁻¹(L+U)`), §5 cuándo parar | — | 4.A (solo dos iteraciones) | — |
| 2 · ≈ 45 min | `02` **§6 Gauss-Seidel** (ejemplo guiado 2; §6.2 "el doble de rápido") | **6.A** (R2 b: reordenar + una iteración) | 6.B, 6.D | — |
| 3 · ≈ 1 h 45 | `02` **§7 ¿converge o no?** completa: 7.1 tres teoremas, 7.2 receta, 7.3 reordenar, 7.4 hallar `k`, 7.5 radio espectral | **7.A** (T1 = T2, Ej2 completo), **7.B** (R1, Ej2 completo) | 7.D, 7.E | 7.C |
| 4 · ≈ 45 min | `02` **§8 número de condición** (ejemplos guiados 6–7) | **8.A** (R2 a) | 8.C, 8.D | 8.B |
| 5 · ≈ 35 min | `02` "Resumen en una página" · "Errores típicos" · **Checkpoint (25 min, con reloj)** | — | — | — |
| 6 · ≈ 1 h | `04` §0, §1, §2, **§3 Trapecios con tabla** (ejemplo guiado 1) | `04` 3.A (rápido) | — | — |
| 7 · ≈ 2 h | `04` **§6 elegir `h` para Trapecios**: 6.1–6.3, ejemplo guiado 3 (caso fácil) y **ejemplo guiado 4** (caso de parcial) rehechos | **6.A** (T1 Ej4), **6.B** (T2 Ej4) | 6.F | 6.E |

Si los bloques 1–5 se alargan, **no recortes el bloque 7**: el Ej4 es el seguro número 1.
Recortá el 4 (número de condición: leé solo §8.2 y el ejemplo guiado 6) y pasá 8.A al sábado.

### Sábado 2026-11-21 — cierre de integración (`04`) + ecuaciones diferenciales (`05`)

| Bloque | Secciones | "Tu turno" núcleo (parcial 2025) | Opcional | Reservado (lunes) |
|---|---|---|---|---|
| 1 · ≈ 1 h 15 | `04` §6 otra vez, en frío | **6.C** (R1 Ej4, la variante con logaritmo), **6.D** (R2 Ej4 a, pide `N`) | — | — |
| 2 · ≈ 50 min | `04` **§4 Simpson y "N par"** (ejemplo guiado 2) | **4.A** (R2 b y c) | 4.B, 4.E | — |
| 3 · ≈ 40 min | `04` **§5 conceptuales del error**: exactitud, impares en intervalo simétrico, concavidad | **5.C** (V/F de la guía; los de parcial son del repaso) | 5.D, 5.E | 5.A, 5.B |
| 4 · ≈ 30 min | `04` §7 solo el ejemplo guiado 5 (leído) · **§8 derivadas desde tabla**: 8.2, 8.3 y ejemplo guiado 6 | **8.A** | 7.A, 8.B, 8.D | 7.B, 8.C |
| 5 · ≈ 35 min | `04` "Resumen en una página" · **Checkpoint (25 min, 2 puntos)** | — | — | — |
| 6 · ≈ 1 h 15 | `05` §0, §1, §2, **§3 Lipschitz** (receta por la derivada parcial; ejemplos guiados 1–3; 3.4 cuándo no se puede) | **3.1** (T1 a), **3.2** (T2 a) | 3.3, 3.4, 3.6 | 3.5 |
| 7 · ≈ 1 h | `05` **§4 Euler** (ejemplo guiado 4) | **4.1** (T1 b), **4.2** (T2 b) | 4.3, 4.4, 4.6 | — |
| 8 · ≈ 1 h 15 | `05` **§5 Heun** (ejemplo guiado 5) y **§6 Runge-Kutta 4** (ejemplo guiado 6), con el ayudamemoria al lado | **5.1** (R1, Ej5 completo), **6.1** (R2 a) | 5.4, 6.2 | — |
| 9 · ≈ 45 min | `05` **§7 clasificar una fórmula** · §8 teoría corta (leer) · "Resumen en una página" · **Checkpoint (25 min, con reloj)** | **7.1** (R2 b) | 7.3, 7.4, 8.1, 8.2 | 7.2 |

`05` §9 se saltea. Agregá a la hoja de memoria: `A_T = h/2·(E + 2M)`, `A_S = h/3·(E + 4I + 2P)`,
las derivadas centrales y `L = máx│∂f/∂y│` (ninguna está en el ayudamemoria).

### Domingo 2026-11-22 — Interpolación (`03`) + memoria y errores

| Bloque | Secciones | "Tu turno" núcleo (parcial 2025) | Opcional | Reservado (lunes) |
|---|---|---|---|---|
| 1 · ≈ 50 min | `03` §0, §1, §2, **§3 teorema de existencia y unicidad** (3.3 y 3.4: agregar un punto; ejemplo guiado 1) | **3.C** (3.A y 3.B son de 2 minutos: hacelos) | — | — |
| 2 · ≈ 15 min | `03` §4 y §5.1 (qué es Lagrange y que da el mismo polinomio): **solo leer** | — | 5.C | — |
| 3 · ≈ 1 h 15 | `03` **§6 tabla de diferencias divididas** (6.2 receta, ejemplo guiado 4, 6.3 cómo se lee el grado). §6.4 regresivo: saltear | **6.A** | 6.C, 6.D | 6.B |
| 4 · ≈ 2 h | `03` **§7 valores tapados** (ejemplo guiado 6 y **ejemplo guiado 7 = T2 a**, rehecho sin mirar) | **7.A** (T1 a), **7.B** (R1 a), **7.C** (R2 a) | 7.F, 7.G, 7.J | 7.D, 7.E |
| 5 · ≈ 45 min | `03` **§8 contar polinomios y decir el grado** (ejemplo guiado 8 y **9 = T1 b**) | **8.A** (R1 b), **8.B** (R1 c), **8.C** (R2 b) | 8.F, 8.G | 8.D, 8.E |
| 6 · ≈ 50 min | `03` **§11** (derivada segunda central, qué fórmula usar, interpolar o aproximar) · "Resumen en una página" · **Checkpoint (25 min, con reloj)**. §9 y §10: saltear | — | — | — |
| 7 · ≈ 2 h | **Memoria y errores:** (1) escribí de memoria, sin mirar, el checklist teórico de `estrategia.md` §6 de raíces, sistemas e interpolación y corregilo contra los resúmenes; (2) rehacé lo que falló en los 5 checkpoints (según `registro.md`); (3) un Ej4 en frío: **2025-06-30 T2 Ej4** otra vez | — | — | — |

A la noche pedí el simulacro (`/simulacro`) para tenerlo listo el lunes.

### Lunes 2026-11-23 — examen a ciegas ×2

| Hora | Qué | Entregable |
|---|---|---|
| Mañana · ≈ 2 h 35 | **`06` cronometrado**, solo con el ayudamemoria (pág. 4) y calculadora, respetando el tiempo de cada título: ej. **1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13, 15**. Salteá el **5** y el **14** (ajuste). | 13 ejercicios hechos en papel |
| ≈ 1 h | Corrección contra el "Tablero de resultados" de `06` y las resoluciones del profesor. Marcá cada uno ✅ / 🟡 / ❌. | Lista de errores por tema |
| Tarde · 2 h | **Simulacro** generado con `/simulacro`: 5 ejercicios, 2 h con reloj. Empezá por los seguros: **Ej4 → Ej5 → Ej3 → Ej1 → Ej2**. | Examen completo |
| ≈ 1 h | Corrección con el criterio de puntuación del simulacro. `/registrar`. | Nota estimada y errores |
| Noche · ≈ 1 h | Solo lo que salió ❌: rehacé el ítem de parcial gemelo (está en la columna "se parece a" de `06`). | Hoja de memoria final |

### Martes 2026-11-24 — día del examen

Nada nuevo. Releé los cinco **"Resumen en una página"** y los **"Errores típicos"** de `01–05`,
y escribí una última vez la hoja de memoria (raíces, convergencia de sistemas, teorema y regla
del conteo, Trapecios/Simpson, Lipschitz). En el examen: **primero Ej4 y Ej5**, después Ej3,
después Ej1; el Ej2 al final.

---

## Si te atrasás

- **Los seguros no se tocan.** Lo que se recorta siempre sale del Ej2 (sistemas) y de los
  opcionales, nunca de `04` §6, `05` §3–§4 ni `03` §6–§8.
- **Raíces se pasa de las 6 h:** cortá §7 en 7.A (dejá 7.B y 7.C) y seguí; se retoma el domingo
  en el bloque 7.
- **Sistemas no cierra el viernes:** quedate con §7.2–§7.5 + 7.A y 7.B; §6 y §8 pasan a
  "receta + un ejemplo leído".
- **Se pierde un día entero:** el lunes pasa a ser solo `06` cronometrado (sin simulacro) y el
  tema que faltó se hace en modo "Resumen en una página + ítems de parcial". Recalculá con
  `/plan`.

---

*Generado el 2026-11-19 con: MATERIA.md (fecha del examen: 2026-11-24), estrategia.md
(prioridades, banco y reserva a ciegas de `06`), registro.md (vacío, sin sesiones aún),
que-saltear.md (no existe), input del usuario (alcance 2026 sin ajuste; arranca casi de cero;
orden raíces → sistemas → integración → ecuaciones diferenciales → interpolación; último día
repaso `06` cronometrado + simulacro; disponibilidad **supuesta** de ≈ 8 h por día, igual que
en el primer parcial). Después de cada sesión: `/registrar`; si cambia el panorama: `/plan`.*
