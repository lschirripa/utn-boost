# Plan de estudio — Primer parcial · Análisis Numérico

> Examen: **martes 2026-10-06** · Recalculado: lunes 2026-10-05, 15:00 · **3 días restantes + la
> mañana/tarde del martes** (sáb/dom/lun ≈ 8–9 h cada uno, mar liviano; el viernes no se usó).
> Restricciones declaradas: **punto de partida en cero**; objetivo **promocionar (≥ 8)**;
> no trabaja: tiene el fin de semana y el lunes enteros.
> Fuentes: [`estrategia.md`](estrategia.md) · [`examenes/INDICE.md`](examenes/INDICE.md) ·
> [`examenes/resueltos/RESOLUCIONES-2025.md`](examenes/resueltos/RESOLUCIONES-2025.md) ·
> `../fuentes/formulas-y-metodos-manuscrito.pdf`.

---

## ⚠️ No entra todo: triaje para llegar a 8

Hay ≈ **28 h útiles** para 4 bloques 🔴 que arrancan de cero. Alcanza para las **cuatro
recetas** si cada bloque se cierra en un día y no se abre nada lateral. Lo que **cae**:

- Ecuaciones integrales con convolución (`#EcuacionIntegral`, 0/3 en 2025): solo un ejemplo leído, no practicado.
- ~~Ecuaciones en diferencias de 2do orden~~ → **vuelven** (2026-10-02): el repaso 2026 resolvió una de 2º orden con raíz doble (guía 7e). Entra la de la hoja de práctica; las otras de 2º orden del dataset, solo si sobra tiempo.
- Corte de `|G|` por el eje real: 10 min de regla cualitativa, no ejercicios propios.
- Conjuntos de complejos, método gráfico del módulo, fasores, sistemas de EDO, sumas de series vía Fourier: **fuera**.
- El segundo simulacro a ciegas (`2024-2C T2`): fuera; queda solo `2025-1C_Recuperatorio.pdf`.

Lo que **no se negocia**, porque son los 8 puntos: Ej1a+b (2), Ej3 completo (3), Ej4 completo (2),
Ej2a o Ej2b (1). Ej1c (media onda, 1 punto de dibujo) y Ej2c (demostración de 2 líneas) son
el colchón para que un error en otro ítem no te baje de 8.

**Regla de trabajo:** cada ejercicio se hace **en papel, con reloj (25 min), sin mirar**, y se
corrige contra la hoja resuelta. Si un tipo de ítem sale bien dos veces seguidas, se cierra y
no se vuelve a tocar. Terminá cada bloque con `/registrar` (lo que falló manda el lunes).

### Qué apunte leer cada bloque (2026-10-02; **reemplazado el 2026-10-03 por las guías de `guia/`**: esto queda solo como referencia para cuando te trabás)

Leé **solo la teoría visible y la sección "Lo que el profe remarca"**; los ejercicios del
apunte son para consultar cuando te trabás, no para hacer todos.

| Bloque | Antes de practicar (≈30 min) | Si te trabás |
|---|---|---|
| Fourier I (vie) | `01` teoría + `10` "Lo que el profe dice del parcial" | `16` (teórica STF) |
| Fourier II (sáb mañana) | `02` teoría (impar desplazada, dos condiciones ⇒ cuadruplicar) | `17` (teórica SEF), `07` ej. de Fourier |
| Laplace (sáb tarde/noche) | `14` "Lo que el profe remarca" + `04` recetas `t·f`, `f/t`, convolución | `15` (teórica), `04` ejercicios |
| Sistemas (dom) | `11` "Lo que el profe remarca" + `13` tabla de los seis casos de polos | `05` (13 ejercicios resueltos), `07` ej. 8–9 |
| Z (lun mañana) | `12` "Lo que el profe remarca" + `06` recetas (paridad, ROC, "una z afuera") | `06` ejercicios |
| Lun noche, después del simulacro | `07` y `10` completos: es el repaso del profe | — |

**Descartado sin culpa:** `03` (transformada de Fourier, el profe dijo que no se toma) y los
fasores de `16`.

---

## 🆕 Repaso 2026 de tu curso: va primero en cada bloque

La clase de repaso de tu cuatrimestre (fotos en `../fuentes/clases/repaso-clase-2026/`) es la
fuente **más cercana al parcial** de todas. Sus 9 ejercicios, verificados y con espacio para
resolver, están en [`repaso/practica-repaso-2026.md`](repaso/practica-repaso-2026.md):

- **Para resolver** (iPad/GoodNotes, una página por ejercicio): `exports/practica-repaso-2026-enunciados.pdf`.
- **Para corregir**: `exports/practica-repaso-2026.pdf` (con las correcciones abiertas).

Qué confirma: **los mismos moldes del dataset, casi textuales** (π−t de 2025-1C Ej1a; `K=7` del
2015-05-29 T2; `e^{−3t}` del 2025-1C rec; `1/(s²+1)²` y `cos³` de 2024-2C/2025-1C). Qué agrega:
**V/F conceptuales de Fourier** (guía 14), un **circuito RLC** como sistema físico (guía 18) y una
**ecuación en diferencias de 2º orden con raíz doble** (guía 7e). En la tabla, los ítems del
repaso van marcados **R-A … R-I** y siempre se hacen **antes** que los del dataset.

## Plan de emergencia (lunes 2026-10-05, 15:00 → examen)

**Situación real:** Fourier hecho. Laplace hasta la §5 (división por $t$). Sistemas y Z sin empezar.
Quedan ≈ 9 h hoy y la mañana del martes. **No entra todo: se estudia solo lo que cayó en 2025
(T1, T2 y recuperatorio) o en el repaso 2026.** El simulacro a ciegas **se cancela**; el machete
lo genera Claude esta noche para leer mañana.

### Qué se saltea de cada guía (y por qué)

| Guía | Se hace | Se saltea |
|---|---|---|
| `02-laplace` | §11 ($\mathcal{L}[a^t]$, 10 min, punto regalado) → §6 Euler + **R-C** → §9 fracciones simples (base de Sistemas) → §10 convolución + **R-D** | §7 (transformada de una integral: 1 ítem en 1 de 3 hojas 2025), §8 (lo repite §9) |
| `03-sistemas` | §4 polos/ceros/estabilidad → §5 hallar $K$ + **R-F** a/b → §7 respuesta temporal + **R-G** → §8 tipo de respuesta y valor estable → §6 solo la regla cualitativa del corte (10 min) | §3 (ya lo hiciste en Laplace §9), §9 EDO y **R-E** (solo si sobra: 1 punto en 2025-1C T1) |
| `04-z` | §3 geométrica → §4 paridad y ROC + **R-H** → §5 sumas vía Z (evaluar $X(c)$) → §7 + §8 ecuación en diferencias de 1er orden | §6 secuencia finita, §9 2º orden y **R-I** (solo si sobra) |

### Martes 2026-10-06, el día del examen (Laplace cerrado el lunes a la noche; Sistemas y Z sin empezar)

**Orden por puntos por hora:** primero Z (dos ítems baratos en 2 h), después el primer ítem de
Sistemas (1 h), después la respuesta temporal (lo único que se recorta si falta tiempo), y al
final un refresco fijo de Fourier + Laplace, que son los 5–6 puntos que ya tenés.

| Hora | Qué | Puntos |
|---|---|---|
| 08:00–10:00 | **Z:** §3 geométrica (20) → §4 paridad + ROC y **R-H** (60) → §5 sumas vía Z (40). Salteá §6–§9. | Ej4 (2) |
| 10:00–10:15 | Corte. | |
| 10:15–11:15 | **Sistemas §4 + §5** con **R-F a) y b)**: polos, ceros, estabilidad, hallar $K$. | Ej3a (1) |
| 11:15–12:45 | **Sistemas §7 + §8** con **R-G**: respuesta temporal (fracciones simples con $s+a$), tipo de respuesta y valor estable. **Se corta a las 12:45 pase lo que pase.** | Ej3b/c (0–2) |
| 12:45–13:30 | Almuerzo. | |
| 13:30–15:00 | **Refresco de lo seguro:** machete §Fourier y §Laplace (20) → **R-A** a) en limpio con reloj (25) → **R-C** o **R-D** de Laplace + un ítem de fracciones simples (30) → checkpoints de las guías 01 y 02 de memoria (15). | sostiene Ej1 + Ej2 (5–6) |
| 15:00–17:00 | Parar. Comer, ducha, viaje. Nada nuevo. | |

**Nota esperada:** Fourier 3 + Laplace 2–3 + Z 1–2 + Sistemas 1–2 = **7–10**. Aprobar (6) está
prácticamente asegurado con Fourier + Laplace + un ítem más; el 8 lo deciden los dos ítems baratos de la
mañana (Z paridad+ROC y Sistemas K/polos).

**En el examen:** empezá por Ej1 y Ej2 (lo que sabés), después Ej4a, después Ej3a; la respuesta
temporal al final, con el tiempo que quede.

---

## Qué cambió respecto del plan anterior

- **2026-10-06 (00:30):** Laplace cerrado; Sistemas no se empezó el lunes. Plan del martes: Z primero (2 ítems baratos), Sistemas K/polos, respuesta temporal con corte fijo a las 12:45, refresco de Fourier + Laplace de 13:30 a 15:00.

- **2026-10-05 (21:00):** Laplace a falta de §11, práctica de fracciones simples y convolución; Sistemas y Z sin empezar. Decisión: no descartar ningún tema; hacer el primer ítem barato de Sistemas (K/polos) hoy y el de Z (paridad+ROC) mañana temprano, respuesta temporal mañana a media mañana, refresco de 2 h al final.

- **2026-10-05 (15:00):** Lucho va por Laplace §5; Sistemas y Z sin empezar. Plan de emergencia: se saltean las secciones que no cayeron en 2025 ni en el repaso 2026, se cancela el simulacro, Claude genera el machete.

- **2026-10-03:** el viernes no se usó y Lucho no podía arrancar desde los apuntes largos. Se armaron **cuatro guías lineales desde cero** (`guia/01`–`04`: idea, receta, ejemplos guiados y tu turno del dataset, verificados con sympy), con los R-A … R-I ya ubicados adentro. Fourier y Laplace pasan al sábado, Sistemas queda el domingo y Z el lunes a la mañana. En el simulacro, además del Ej3 ya reemplazado, el **Ej4a deja de ser ciego**, porque la guía de Z usa la misma sucesión.

- **2026-10-02 (noche):** entraron los 9 ejercicios de la clase de repaso 2026 (fotos). Van **primeros** en cada bloque (R-A … R-I); se sacaron los ítems del dataset que eran idénticos (2024-2C rec Ej3a/b, 2025-1C T1 Ej2b, 2015-05-29 T1 Ej4). Vuelven las ecuaciones en diferencias de 2º orden. El Ej3 del simulacro (2025-1C rec) dejó de ser ciego y se reemplaza por sin-fecha K3521 T1 Ej4.

- Se perdieron los días 23/9 → 1/10 (D1–D8 del plan previo): AM2 y Administración Gerencial ocuparon toda la ventana. Punto de partida: cero.
- De 13 días útiles a 4: cada bloque pasa a un solo día y cae lo lateral (triaje de arriba).
- Se saca el segundo simulacro (`2024-2C T2`); queda solo el recuperatorio 2025, que se hace el lunes a la tarde y no el domingo.
- El objetivo declarado pasa a ser **8 (promoción)**, no 6: por eso Ej3 y Ej4 (5 puntos de receta) tienen día completo y Ej2 queda en un ítem seguro + uno de colchón.

---

*Generado el 2026-10-02 con: MATERIA.md (examen 2026-10-06), estrategia.md (prioridades y banco, del 2026-09-10), registro.md (vacío, sin sesiones aún), que-saltear.md (no existe: no hay apuntes), input del usuario (arranca en cero; vie noche + sáb + dom + lun completos, martes liviano; busca ≥ 8), y desde la noche del 2026-10-02 las fotos del repaso 2026 (`repaso/practica-repaso-2026.md`).*
