---
name: machete
description: Genera o actualiza el machete de una evaluación, el resumen final ultra-denso de fórmulas, recetas y decisiones (repaso/machete.md) para el repaso de último día. Trabaja SIEMPRE sobre el .md (barato de iterar) y exporta a PDF/HTML solo cuando el usuario da la versión por cerrada. Usala cuando el usuario pida el machete, una hoja de fórmulas, un resumen final de fórmulas, o cuando invoque /machete (con --pdf para exportar la versión final).
---

# machete

Produce el **machete** de una evaluación: una hoja de referencia ultra-densa — solo
fórmulas, recetas y criterios de decisión, **sin explicaciones** — para el repaso final.
Es el destilado de todo el sistema: prioridades de `estrategia.md`, fórmulas exactas de
los apuntes, patrón real de los exámenes y errores propios del `registro.md`.

**Ciclo de trabajo (importante):** el machete se itera sobre el `.md` (la verdad canónica)
y en cada corrida o retoque se regenera el **HTML** en `exports/` (es barato y el visor de
`.md` del usuario no renderiza LaTeX: lo que lee es el HTML). El **PDF** es un paso aparte,
solo cuando el usuario lo pide.

## Invocación

`/machete [materias/<materia>/<evaluacion>] [--pdf] [--html] [pedidos puntuales]`

| Argumento | Efecto |
|---|---|
| ruta `materias/<m>/<e>` | Evaluación objetivo explícita. |
| _(sin flags)_ | Genera o actualiza `repaso/machete.md` y regenera `exports/machete.html`. |
| `--pdf` | Exporta además el PDF del `.md` YA existente. Si se pasa solo el flag (sin pedidos de contenido), **no regenerar**: exportar tal cual está. |
| pedidos puntuales | "agregá X", "sacá la sección Y", "achicá Z" → edición dirigida del `.md`, sin regenerar el resto. |

Si no dan la ruta, aplicá la **Resolución de contexto** de `CLAUDE.md` (materia
`cursando`, evaluación próxima por fecha; ante ambigüedad, preguntar).

## Requisitos previos

- `estrategia.md` de la evaluación — de ahí salen prioridades y banco. Si falta,
  **pará** y pedí correr `/estrategia`.
- `apuntes/md/*.md` — de ahí salen las fórmulas. Sin apuntes no hay machete.
- Opcionales pero valiosos: `que-saltear.md` (✅ núcleo), `examenes/INDICE.md`
  (frecuencias, posiciones, problemas reciclados), `registro.md` (errores recurrentes).

## Pasos

1. **Resolver contexto** y leer: `MATERIA.md` (estructura del examen), `estrategia.md`
   (prioridades + banco), `que-saltear.md` si existe, y el tablero/errores de
   `registro.md` si existe. NUNCA leer PDFs/imágenes de `examenes/` (grep al INDICE).

2. **Seleccionar contenido por prioridad:** entra TODO lo 🔴 y 🟠; lo 🟡 solo si cabe
   en una línea; lo ⚪/🗑️ NO entra. El machete hereda la poda, no la contradice.

3. **Extraer las fórmulas de los apuntes** (`grep -n` para ubicar la sección, Read con
   offset para leerla). Las fórmulas van EXACTAS como figuran en el apunte — no
   inventar ni "mejorar" notación. Condensar es sacar palabras, no cambiar matemática.

4. **Escribir `repaso/machete.md`** con la estructura de abajo.

5. **Exportar el HTML**, comprobar el render (ver "Verificar un HTML" en `CLAUDE.md`) y
   pasarle al usuario el link al `.html`, no al `.md`.

6. **Confirmar** ruta y actualizar la columna **Machete** de la tabla "Estado del
   material" de `MATERIA.md`. Commitear md + html.

### Export

```bash
venv/bin/python tools/md_to_html.py <eval>/repaso/machete.md --out-dir <eval>/exports                   # siempre
venv/bin/python tools/md_to_html.py <eval>/repaso/machete.md --pdf --no-html --out-dir <eval>/exports   # solo con --pdf
```

(fallback `python tools/…` si no está el venv). El PDF renderiza la matemática sin
internet — es la versión para imprimir/iPad. Confirmar la ruta escrita en `exports/`.

## Estructura de `machete.md`

```markdown
# MACHETE — <Materia> · <Evaluación>

> Solo fórmulas y recetas, sin explicaciones. Orden: identificar → plantear → integrar.
> Basado en el patrón real de <N> exámenes (`examenes/INDICE.md`).

## 0 · Tabla de decisión: ¿qué me están pidiendo?

| El enunciado dice… | Herramienta |
|---|---|
| <señal del enunciado> | <fórmula/método, con referencia §N si el detalle está abajo> |

## 1..N · <Un tema por sección, en el orden del examen (P1→Tn) o de prioridad>

- Una subsección por tipo de ítem (`### N.M`), con la **receta en pasos numerados** y una
  frase de *por qué* en el paso que suele trabar. Tiene que alcanzar para hacer el ejercicio
  sin abrir la guía: si un punto queda en una sola línea críptica, ampliarlo.
- Fórmulas en bloque `$$…$$`; atajos y casos especiales en una línea.
- **Recordatorio de tabla** en todo ejercicio que se resuelve con tabla (iteraciones,
  diferencias divididas, métodos paso a paso…): un esqueleto chico con los encabezados y una
  o dos filas con símbolos, y una línea de qué valor baja a la fila siguiente y cuándo parar.
- Si el examen permite ayudamemoria: marcar 📄 (está en la hoja oficial) / 🧠 (va de memoria).
- **Sin ejemplos resueltos ni resultados numéricos dentro de las secciones.**

## N+1 · Las frases que valen puntos        ← si la cátedra corrige justificaciones

| Situación | Lo que hay que escribir |

## N+1 · Reciclados con resultado verificado (autocorrección)

| Problema (examen de origen) | Resultado |    ← solo si el INDICE registra reciclados

## N+2 · OJO — errores que cuestan puntos

- Lista corta: primero los errores recurrentes de `registro.md`, después las trampas
  clásicas que los apuntes/estrategia marcan (orientación, módulo del jacobiano, etc.).

---
*Generado el AAAA-MM-DD desde estrategia.md, que-saltear.md, apuntes/md/ y
examenes/INDICE.md. Iterar sobre este .md; exportar con `/machete --pdf`.*
```

La **tabla de decisión** inicial es obligatoria: es el índice mental del examen
(enunciado → herramienta). Las secciones siguen el patrón por posición del examen si
`MATERIA.md` lo documenta; si no, el orden de prioridad de la estrategia.

## Reglas

- **Denso pero entendible:** recetas explicadas en palabras, sin demostraciones completas
  ni ejercicios resueltos — para eso están apuntes y flashcards. Las secciones finales de
  resultados verificados y de errores son **opcionales**: van todas juntas al final (nunca
  mezcladas en las recetas) y se sacan si el usuario no las quiere. Título y subtítulo
  también son prescindibles: el documento puede arrancar en la tabla de decisión. Si una
  demostración es checklist del examen, va solo el esqueleto (pasos clave en una línea).
- **No inventar:** cada fórmula sale de `apuntes/md/` (o del INDICE para resultados de
  reciclados). Ante duda, se omite — un machete con una fórmula errada es peor que
  ninguno.
- **Iteración barata:** con el `.md` ya creado, los pedidos del usuario se aplican como
  ediciones puntuales (Edit), no regenerando todo. Regeneración completa solo si cambió
  la estrategia/poda o el usuario la pide.
- Los retoques manuales del usuario sobre `machete.md` son válidos (es SU machete):
  antes de regenerar, avisá que se pisan.
- Español rioplatense, fechas absolutas (AAAA-MM-DD), pie con fecha y fuentes.
- Fórmulas en `$$…$$` en líneas propias sin sangría (convención del repo); en tablas,
  matemática inline `$…$`.
- Nunca leer PDFs/imágenes de `examenes/`; la evidencia sale de `INDICE.md` (grep).
