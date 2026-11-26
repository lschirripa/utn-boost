---
name: guia
description: Genera una guía "desde cero" de UN tema de una evaluación, una explicación lineal paso a paso (idea en criollo, receta, ejemplos guiados, "tu turno" con los ítems reales de parcial y checkpoint) que a la vez enseña el tema y entrena para el examen. Combina las fuentes que la materia declara en la tabla "Fuentes del aula por tema" de MATERIA.md (PDF de clase, teórico de cátedra, OneNote/práctica, transcripciones de video) con el INDICE.md de exámenes. Usala cuando el usuario pida un resumen explicativo y guiado de un tema, una guía desde cero, "explicame el tema X para el parcial", o cuando invoque /guia. Para varios temas, un subagente por tema.
---

# guia

Produce `materias/<materia>/<evaluacion>/apuntes/md/NN-<tema>-desde-cero.md` y su HTML.
A diferencia de `/apunte` y `/apunte-doc` (que siguen UNA fuente tal cual), la guía cuenta
el tema en el orden en que conviene aprenderlo y lo ata a lo que realmente se toma.

Modelos de referencia (leer uno antes de escribir):
`materias/analisis-numerico/segundo-parcial/apuntes/md/01-raices-desde-cero.md` y
`materias/analisis-numerico/primer-parcial/apuntes/md/03-sistemas-estables-desde-cero.md`.

## 1. Contexto

1. Resolver materia/evaluación (reglas de CLAUDE.md) y leer `MATERIA.md`.
2. Leer `<eval>/examenes/INDICE.md` (y `resueltos/RESOLUCIONES-*.md` si existe). Si no hay
   índice, avisar: la sección "Qué te toman" queda sin evidencia; ofrecer `/indexar-examenes` antes.
3. Ver qué se permite llevar al examen (ayudamemoria, tablas) según `MATERIA.md`.

## 2. Qué fuentes usar: la tabla de MATERIA.md

Cada materia es distinta: **no** se usan "todos los PDF del aula". Las fuentes de una guía son
exactamente las de la fila del tema en la tabla **"Fuentes del aula por tema"** de `MATERIA.md`
(columnas típicas: PDF de clase, teórico de cátedra, práctica/OneNote, videos → transcript,
más las fuentes transversales que la sección declare, p. ej. guía de ejercicios).

- **Si la tabla no existe o no tiene el tema:** armarla primero. Listar el aula con el MCP `utn`
  (`aula_list_courses` → `aula_open`), proponer por tema qué archivos sirven y cuáles se
  descartan (con el motivo), **mostrarle la propuesta al usuario y esperar su visto bueno**, y
  recién entonces escribirla en `MATERIA.md` y bajar los archivos a `fuentes/clases/<tema>/`.
- **Cómo se bajan** (detalle en "Material del aula virtual" de `CLAUDE.md`): PDF del aula con
  `aula_download_file` o `aula_study_pack` (une varios; separar por material con
  pymupdf usando `empiezaEn`/`paginas`); links de Drive públicos con `curl`; lo que pide sesión
  institucional (SharePoint/Stream, Drive) desde el Chrome del usuario con su cuenta; videos →
  `tools/transcribe_local.py` a `<eval>/apuntes/transcripts/NN-….json` (los mp4 no se versionan).
  Lo que tiene la descarga bloqueada se anota en la tabla como tal y el tema se cubre con el resto.
- Sin aula (materia que no la usa): la tabla se arma igual con lo que haya en `fuentes/`.

## 3. Estructura de la guía (obligatoria)

1. `# {Tema} desde cero` + `> Fuentes: …` (los archivos realmente usados) + bloque "Cómo usarla"
   que declare qué es de la cátedra y qué es agregado propio (intuición, cuentas intermedias,
   gráficos) + `---`.
2. `## 0. Qué te toman`: tabla de los ítems reales de ese tema en el `INDICE.md`, con frecuencia
   y la sección de la guía a la que manda cada uno.
3. Sección "qué está en el ayudamemoria y qué va de memoria", si el examen permite material.
4. Secciones `## N.` de a una idea por vez: idea en criollo → receta en pasos numerados → cuándo
   se usa y cuándo falla → **qué hay que dejar escrito** para que el ítem esté completo según el
   criterio de la cátedra (tomado de las resoluciones oficiales y de lo que dice el profesor).
5. **Ejemplos guiados** de la clase/práctica, con todas las cuentas y tablas completas.
6. **Tu turno** en cada sección: cada ejercicio en `<details>` con la resolución en un `<details>`
   anidado. Incluir **todos** los ítems de examen del tema, los del repaso y una selección de la
   guía de ejercicios. Indicar el origen de cada uno.
7. Notas `> **En clase:** … [mm:ss]` con lo que el profesor dice en los videos (qué se toma, cómo
   corrige, errores típicos). Solo timestamps reales del transcript.
8. `## Resumen en una página`, `## Errores típicos`, `## Checkpoint` (un ejercicio con formato de
   examen para hacer con reloj, resolución desplegable y puntaje; si es armado y no una hoja
   real, decirlo) y pie con fecha y fuentes.

## 4. Reglas

- Métodos, criterios y ejemplos salen de las fuentes; se usa la notación de la cátedra. Si el PDF
  de clase y el teórico difieren, manda lo que se usa en clase y en las resoluciones oficiales.
  Lo agregado propio se declara. Nada de métodos que la cátedra no da.
- **Verificar todos los números** con Python (`venv/bin/python`, numpy/sympy). Si una fuente
  tiene un error (errata de PDF, valor mal copiado en el manuscrito, respuesta de guía mal),
  poner el valor correcto y marcarlo con ⚠ indicando qué decía la fuente.
- Manuscritos y PDF sin capa de texto: leer con visión, todas las páginas. Lo ilegible:
  `[poco claro en el manuscrito]` / `[poco claro en la transcripción]`.
- LaTeX según CLAUDE.md. `md_to_html.py` **no renderiza LaTeX dentro de `<summary>`**: ahí va el
  enunciado en texto plano Unicode y, si tiene fracciones o matrices, se repite en LaTeX como
  primera línea del desplegable. En tablas, `\lvert … \rvert` en lugar de `|`.
- Gráficos con matplotlib en `<eval>/apuntes/img/NN-figK-<slug>.png` (referencia `../img/…`), con
  el script en `img/NN-figuras.py`.
- **Numeración:** si el examen tiene un ejercicio por tema, la guía lleva el número de ese
  ejercicio (`01` = Ej1…) y la práctica integradora va al final. Los temas que NO entran en la
  evaluación no se numeran en la serie: van a una subcarpeta propia (`<eval>/<tema>/`).
- Marcar cada ejercicio con su prioridad (🔴/🟠/⚪), dar una "ruta corta" al principio y dejar
  plegado lo que casi no se toma: el largo se resuelve con presentación, no recortando contenido.
- Extensión: priorizar los ítems de examen y del repaso; el resto de la práctica es selección,
  no exhaustividad (orientativo 900–1300 líneas).

## 5. Salida

- Exportar **solo a HTML** (`tools/md_to_html.py <md> --out-dir <eval>/apuntes/html`); PDF
  únicamente si el usuario lo pide. Comprobar que no queden fórmulas sin renderizar.
- Varios temas → un subagente por tema, cada uno con este procedimiento y su fila de la tabla.
- Informar: secciones, ejercicios incluidos con su origen, qué aportó el video que no estaba en
  los PDF, y erratas/discrepancias encontradas.
- Actualizar "Estado del material" en `MATERIA.md` y commitear solo los archivos de la tarea.
