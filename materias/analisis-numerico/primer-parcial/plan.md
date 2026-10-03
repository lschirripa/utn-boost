# Plan de estudio — Primer parcial · Análisis Numérico

> Examen: **martes 2026-10-06** · Recalculado: sábado 2026-10-03 · **3 días restantes + la
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

## Plan día por día (recalculado el sábado 2026-10-03: el viernes no se usó)

**Cambio de método:** cada bloque se estudia con **una sola guía lineal** de `guia/`, de arriba abajo:
idea → receta → ejemplo guiado → tu turno. Los apuntes largos de `apuntes/md/` quedan solo
para consultar si te trabás. Los ejercicios del repaso 2026 (R-A … R-I) ya están metidos en el
lugar justo de cada guía. Se estudia con el PDF `exports/NN-…-enunciados.pdf`, que no trae las
correcciones, y se corrige con `exports/NN-….pdf`.

| Día | Bloque | Guía | Entregable |
|---|---|---|---|
| **sáb 2026-10-03, mañana y mediodía (≈4 h)** | 🔴 **Fourier** (Ej1, 3 puntos) | `guia/01-fourier-desde-cero` | Tu turno 1–8, con **R-A** y **R-B**. Checkpoint. `/registrar`. |
| **sáb 2026-10-03, tarde y noche (≈4–5 h)** | 🔴 **Laplace** (Ej2, 3 puntos) | `guia/02-laplace-desde-cero` | §3–§6 y §9–§11, con **R-C** y **R-D**. La **§9 (fracciones simples) no se saltea**: es la base del domingo. Si falta energía, se corta la §7. `/registrar`. |
| **dom 2026-10-04 (≈8 h)** | 🔴 **Sistemas estables** (Ej3, 3 puntos) | `guia/03-sistemas-desde-cero` | §3–§9 con **R-F**, **R-G** y **R-E** en su lugar. El checkpoint es el reciclado 2025-1C T2 Ej3, a ciegas. `/registrar`. |
| **lun 2026-10-05, mañana (≈4 h)** | 🔴 **Transformada Z** (Ej4, 2 puntos) | `guia/04-z-desde-cero` | §3–§9 con **R-H** y **R-I**. Checkpoint. |
| **lun 2026-10-05, tarde (2 h + corrección)** | 🔴 **Simulacro a ciegas** | — | `examenes/2025-1C_Recuperatorio.pdf`, con reloj y solo el ayudamemoria. **Su Ej3 se reemplaza** por **sin-fecha K3521 T1 Ej4** (resuelto en `examenes/resueltos/sin-fecha_Parcial-K3521-T1_resuelto.pdf`). **Su Ej4a no es ciego**: es la misma sucesión del 2025-1C T1 Ej4a de la guía de Z, así que se hace igual pero no cuenta para la nota estimada. Se corrige con `RESOLUCIONES-2025.md` → "Recuperatorio". `/registrar` con la nota. |
| **lun 2026-10-05, noche** | Machete y errores | — | `/machete`: lo que el ayudamemoria no trae más lo que falló. Rehacer los ítems ❌ del simulacro. |
| **mar 2026-10-06 (liviano)** | 🟢 Repaso | — | Machete (30 min) y los checkpoints de las cuatro guías, **de memoria**. Rehacer **una vez** los dos ítems que peor salieron. **Nada nuevo.** |

**Si un día se atrasa:** no se arrastra. Se corta el final de la guía de ese día (las secciones
opcionales y los últimos "tu turno") y se arranca la siguiente a la hora prevista. Prioridad de
corte, de lo primero que se saca a lo último: Laplace §7 → Sistemas §9 → Z §6 → Fourier §9.

---

## Qué cambió respecto del plan anterior

- **2026-10-03:** el viernes no se usó y Lucho no podía arrancar desde los apuntes largos. Se armaron **cuatro guías lineales desde cero** (`guia/01`–`04`: idea, receta, ejemplos guiados y tu turno del dataset, verificados con sympy), con los R-A … R-I ya ubicados adentro. Fourier y Laplace pasan al sábado, Sistemas queda el domingo y Z el lunes a la mañana. En el simulacro, además del Ej3 ya reemplazado, el **Ej4a deja de ser ciego**, porque la guía de Z usa la misma sucesión.

- **2026-10-02 (noche):** entraron los 9 ejercicios de la clase de repaso 2026 (fotos). Van **primeros** en cada bloque (R-A … R-I); se sacaron los ítems del dataset que eran idénticos (2024-2C rec Ej3a/b, 2025-1C T1 Ej2b, 2015-05-29 T1 Ej4). Vuelven las ecuaciones en diferencias de 2º orden. El Ej3 del simulacro (2025-1C rec) dejó de ser ciego y se reemplaza por sin-fecha K3521 T1 Ej4.

- Se perdieron los días 23/9 → 1/10 (D1–D8 del plan previo): AM2 y Administración Gerencial ocuparon toda la ventana. Punto de partida: cero.
- De 13 días útiles a 4: cada bloque pasa a un solo día y cae lo lateral (triaje de arriba).
- Se saca el segundo simulacro (`2024-2C T2`); queda solo el recuperatorio 2025, que se hace el lunes a la tarde y no el domingo.
- El objetivo declarado pasa a ser **8 (promoción)**, no 6: por eso Ej3 y Ej4 (5 puntos de receta) tienen día completo y Ej2 queda en un ítem seguro + uno de colchón.

---

*Generado el 2026-10-02 con: MATERIA.md (examen 2026-10-06), estrategia.md (prioridades y banco, del 2026-09-10), registro.md (vacío, sin sesiones aún), que-saltear.md (no existe: no hay apuntes), input del usuario (arranca en cero; vie noche + sáb + dom + lun completos, martes liviano; busca ≥ 8), y desde la noche del 2026-10-02 las fotos del repaso 2026 (`repaso/practica-repaso-2026.md`).*
