# Plan de estudio — 1er recuperatorio del primer parcial · Análisis Numérico

> Examen: **martes 2026-12-01** (1er recuperatorio) · Hoy: jueves 2026-11-26 ·
> **5 días restantes** (3 útiles para temas: jue 26, vie 27 y sáb 28; dom 29 y lun 30 son de
> simulacro; el martes es liviano).
> Restricciones declaradas: **ninguna**. Supuestos míos, a corregir si no son así: ≈ 5 h el jueves
> y el viernes, ≈ 8 h el sábado y el domingo, ≈ 4 h el lunes, y el examen a la tarde/noche del martes.
> Material: [`06` El parcial 2026 resuelto](../apuntes/html/06-parcial-2026-resuelto.html) ·
> [`01` Fourier](../apuntes/html/01-fourier-desde-cero.html) ·
> [`02` Laplace](../apuntes/html/02-laplace-desde-cero.html) ·
> [`03` Sistemas estables](../apuntes/html/03-sistemas-estables-desde-cero.html) ·
> [`04` Transformada Z](../apuntes/html/04-transformada-z-desde-cero.html) ·
> [`05` Práctica de repaso](../apuntes/html/05-practica-repaso-primer-parcial.html).
> Se lleva al examen: el ayudamemoria oficial (págs. 1–3) y la tabla de integrales.

---

## Lo que cambia con el parcial de este cuatrimestre

El 2026-11-26 se sumó al dataset el parcial que se tomó el 2026-10-06 (los dos temas, con la
resolución del profesor). Es la mejor pista de cómo va a ser el recuperatorio, y corrige el plan
del 2026-11-25 en tres puntos:

- **Recicló hojas de 2022 y 2024-1C**, no las de 2025: el Ej1 del Tema 1 es textual el del
  2022-10-11 y el del 2024-1C Tema 1; el Ej3 del Tema 2 es textual el del 2022-10-11. Los
  "tu turno" 🟠 de esas dos hojas suben a obligatorios.
- **Tomó dos cosas que el plan mandaba a saltear:** sumar una serie numérica con Fourier
  (guía `01` §11) y el método gráfico del módulo (guía `03` §10). Vuelven a entrar.
- **No tomó** media onda, espectro, convolución, sucesión por paridad ni $G(s)$ desde la ecuación
  diferencial. No se descartan (el recuperatorio suele cambiar los sub-ítems), pero pasan a
  segunda prioridad dentro de cada día.

## ⚠️ No entra todo

Son **4 ejercicios 🔴** y **3 días** para estudiarlos antes de los simulacros. Las cuatro guías
suman ≈ 8.600 líneas: enteras no entran. Entra la **ruta corta** de cada una (el recuadro 🧭 del
principio, con la nota 🆕 del parcial 2026) más los "tu turno" que figuran abajo. El triaje:

- **Sistemas y Z van primero y con día propio.** En octubre fueron los dos temas que quedaron para
  la mañana del examen; el registro está vacío, así que es la única evidencia de qué está flojo.
  Sistemas además es el que más vale (3 puntos) y sus ítems están encadenados.
- **Laplace y Fourier comparten el sábado.** Se llegaron a cerrar en octubre: es repaso.
- **Cae de cada guía** todo lo plegado como "⚪ Se toma poco" y además:
  - Fourier: §8 hallar $k$, §12 verdadero o falso, §13 fasores. §7 espectro y §9 media onda quedan
    en un "tu turno" cada uno.
  - Laplace: §8, §11 (ecuación integral), §12 (sistemas) y §13. §10 convolución queda en un solo
    "tu turno" (10.A).
  - Sistemas: §11 y el corte por el eje imaginario. §9 ($G$ desde la ecuación diferencial) queda
    en un solo "tu turno" (9.A).
  - Z: §7 más allá del recuadro de fórmulas, §10 (2º orden) y §11. §4 paridad y §6 secuencia finita
    quedan en un "tu turno" cada uno.
- **Complejos:** fuera. El anexo de la práctica `05` no se toca.

**Regla de trabajo:** los ejemplos guiados se leen con lápiz; los "tu turno" se hacen **en papel,
con reloj y sin mirar**, y recién después se abre la corrección. Al terminar cada día, `/registrar`
con lo que falló: eso decide qué se repite el domingo y el lunes.

**No abras el otro tema del parcial 2026.** En la guía `06` mirá solo el tema que rendiste: el otro
es el simulacro del domingo, el único examen real del formato vigente que todavía no viste.

## Plan día por día

| Día | Foco | Entregable del día |
|---|---|---|
| **Jue 2026-11-26** | **Diagnóstico (1 h):** rehacé en papel el Ej3 y el Ej4 del tema que rendiste el 2026-10-06 y comparalos con la guía `06`. Después 🔴 **Sistemas estables** (guía `03`, ruta corta): §5 hallar $K$ → §7 respuesta temporal → §3–§4 polos, ceros y los seis casos → §6.2 corte por el eje real → §10 método gráfico del módulo → §8 tipo de respuesta. | **5.B y 7.C** (parcial 2022-10-11: es textual el Ej3 del Tema 2 de 2026, $k=6$, $y(t)=3-3\cos(t)e^{-4t}+5\operatorname{sen}(t)e^{-4t}$). **El reciclado a ciegas** (ejemplos guiados 5 + 9 + 11: parcial 2025 Tema 2 = 2024-2C T1 = sin fecha K3521 T2). **3.A, 6.A y 7.A** (1er recuperatorio 2025, ítems a, b y c). **10.A** (parcial 2024-1C Tema 2) y **10.B** (parcial 2015-05-29 Tema 1): módulo gráfico. **8.A** (parcial 2024-1C Tema 1). Si sobra: 9.A (parcial 2025 Tema 1). |
| **Vie 2026-11-27** | 🔴 **Transformada Z** (guía `04`, ruta corta, en este orden): §3 geométrica → §8 "una $z$ afuera" → §9 ecuación en diferencias de 1er orden → §5 suma de una serie → §4 paridad y región de convergencia → §6 secuencia finita. Al final, 30 min de Sistemas: rehacer lo que falló el jueves. | **9.A** (parcial 2025 Tema 2 = sin fecha K3521 T2) y **9.B** (1er recuperatorio 2024-2C), con la verificación escrita. **5.A, 5.B** (parcial 2025, Temas 1 y 2) y **5.C** (parcial 2024-2C Tema 2). **4.A** (parcial 2025 Tema 1), **4.B y 6.A** (1er recuperatorio 2025). Del repaso de tu curso: **4.G**. De memoria al cerrar: la geométrica y $\mathcal{Z}[a^n/n!]=e^{a/z}$ (no está en el ayudamemoria). |
| **Sáb 2026-11-28** (mañana) | 🔴 **Laplace** (guía `02`, ruta corta): §4 integral impropia y multiplicación por $t^n$ → §5 división por $t$ → §3 tabla, linealidad y $a^t$ → §6 potencias de seno y coseno → §9 fracciones simples → §10 convolución (un ejemplo). | **4.A** (parcial 2025 Tema 1) y **5.A** (1er recuperatorio 2025, el $\ln 2$ reciclado), **5.B** (parcial 2024-2C). **3.A** (parcial 2025 Tema 1, ítem c). **6.A** (parcial 2025 Tema 2) y **6.B** (1er recuperatorio 2024-2C = repaso 2026 C). **9.A** (parcial 2024-2C Tema 1). **10.A** (parcial 2025 Tema 1 = 1er recuperatorio 2024-2C). Y de memoria, la regla del parcial 2026: con $t>0$ **no** va la 2ª traslación; se desarrolla y se usa la tabla. |
| **Sáb 2026-11-28** (tarde) | 🔴 **Fourier** (guía `01`, ruta corta): §3–§4 herramientas y paridad → §5 completar y desarrollar → §6 pase a $C_n$ → §11 sumar una serie numérica → §9 media onda → §7 espectro. | **11.A** (parcial 2022-10-11 = 2024-1C Tema 1: es textual el Ej1 del Tema 1 de 2026) y **11.B** (parcial 2024-1C Tema 2: la variante del Tema 2). **5.A, 5.B** (parcial 2025, ítem a de cada tema) y **5.C + 6.A** (1er recuperatorio 2025, ítems a y b). **9.A** (parcial 2025 Tema 1, ítem c) y **7.A** (1er recuperatorio 2025, ítem c). Si sobra: 10.A (parcial 2025, ítem b). |
| **Dom 2026-11-29** | **Simulacro 1, cronometrado: el otro tema del parcial del 2026-10-06** (el que no rendiste), 10 ítems, 2 h, solo con el ayudamemoria y la tabla de integrales. Enunciados en la guía `06` (cada ejercicio trae la resolución plegada: no la abras hasta terminar). Tarde: corregir contra el tablero de `06` y rehacer el tema que peor salió. | Los 10 ítems puntuados y anotados con `/registrar`. De cada ítem perdido, el "tu turno" gemelo de la guía hecho de nuevo en papel. Si queda resto: tanda 2 de la práctica `05` (3.3 → 1.1 → 2.3 → 4.4). |
| **Lun 2026-11-30** | **Simulacro 2, cronometrado (mañana):** tanda 1 de la práctica `05` (1.3 a y b + 1.4 → 2.2 + 2.5 + 2.4 → 3.1 a y b → 4.2 + 4.1), 2 h 15 min; o uno generado con `/simulacro` si preferís ejercicios que no viste. Tarde: solo los errores de los dos simulacros. Se corta a la tarde. | Simulacro corregido y registrado. Escritos **de memoria** en una hoja: regla par/impar y $C_n=\frac12(a_n-j\,b_n)$, dónde evaluar la serie para sumar, casos de fracciones simples (incluido el polo doble), tabla polo → tipo de respuesta, receta de $K$, módulo gráfico (distancias a ceros sobre distancias a polos, por la constante), "una $z$ afuera" y la verificación. |
| **Mar 2026-12-01** (día del examen) | Repaso liviano: "Resumen en una página" y "Errores típicos" de las cuatro guías, el tablero de `06` y los errores del registro. **Nada nuevo.** | Un ítem a) de cada tema en limpio para entrar en calor (5.A de Fourier, 4.A de Laplace, 5.B de Sistemas, 9.A de Z) y a rendir. |

**En el examen:** arrancá por el ítem a) de cada ejercicio, que son los cuatro puntos de receta,
y dejá la respuesta temporal de Sistemas para cuando tengas el resto asegurado. Controlá dos veces
el ítem a) de Sistemas antes de seguir: el $k$ mal arrastra los otros dos puntos.

## Qué cambió respecto del plan anterior

- **2026-11-26: entró el parcial del 2026-10-06** (bajado del aula, indexado en `examenes/INDICE.md`
  y resuelto en la guía `06`). Vuelven Fourier §11 y Sistemas §10, que el plan del 2026-11-25
  descartaba por "0 de 3 en 2025". Suben a obligatorios los "tu turno" de 2022-10-11 y 2024-1C
  que el parcial recicló (Sistemas 5.B y 7.C; Fourier 11.A y 11.B). En Z la ecuación en diferencias
  y la suma de series pasan delante de paridad. Bajan a un solo "tu turno" la convolución, la media
  onda, el espectro y $G$ desde la ecuación diferencial.
- **Simulacro 1 nuevo:** el domingo se rinde el tema del parcial 2026 que no te tocó, en lugar de la
  práctica `05`, que pasa al lunes.
- **Jueves con diagnóstico:** se arranca rehaciendo el Ej3 y el Ej4 del tema que rendiste.
- Del plan del 2026-11-25 se mantiene el orden (Sistemas → Z → Laplace + Fourier) y los dos simulacros.

---

*Generado el 2026-11-26 con: MATERIA.md (1er recuperatorio el 2026-12-01), estrategia.md (prioridades
y banco, del 2026-09-10, anterior al parcial 2026), examenes/INDICE.md (18 hojas, con las dos del
2026-10-06), las rutas cortas y los "tu turno" de las guías `apuntes/md/01–06`, registro.md (vacío,
sin sesiones), plan.md anterior (2026-11-25), que-saltear.md (no existe), input del usuario
(recuperatorio del 1/12, los 4 temas; sin disponibilidad declarada).*
