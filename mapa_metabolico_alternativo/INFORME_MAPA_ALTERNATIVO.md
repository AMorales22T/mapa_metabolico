# INFORME DE EVALUACIÓN Y VALIDACIÓN — MAPA METABÓLICO INTEGRADO AMPLIADO (MAPA METABÓLICO ALTERNATIVO)

**Fecha:** 18 de Octubre de 2026  
**Ubicación de la alternativa:** `/home/dolfius/Escritorio/materias/mapa_metabolico/mapa_metabolico_alternativo/`  
**Mapa base original (inmutable):** `07_AMPLIACION_TEMARIO/mapa_cartulina_ampliado.svg` (completamente intacto, `git status` limpio)

---

## 1. Resumen Ejecutivo y Metodología de Trabajo

Se ha llevado a cabo una auditoría independiente y una revisión autónoma integral del mapa metabólico integrado ampliado (25 vías) y del trabajo de corrección realizado previamente.

Siguiendo la regla fundamental, el repositorio y mapa base original han sido protegidos en modo de solo lectura estricto, sin modificar, mover ni sobrescribir ningún archivo del árbol principal (`git status` limpio).

La versión alternativa ha sido construida dentro de la carpeta dedicada `mapa_metabolico_alternativo/`, seleccionando con criterio científico riguroso aquellas mejoras que aportaban valor real, eliminando la totalidad de colisiones geométricas y solapamientos de texto (**0 colisiones detectadas por `detectar_solapamientos.py`**), y dotando al visor HTML de interactividad avanzada (Motor de Flujo Vectorial Bioluminiscente a 60 FPS, Modo Lectura, Modo Aislar Vía, control por URL y buscador integral sin emojis).

---

## 2. Aportaciones y Correcciones Bioquímicas Integradas

### A. Diferenciación funcional en el Ciclo de la Urea (MMI)
- **SLC25A13 (Citrina):** Corregido su etiquetado y vectores de translocación para representar el antiporte electroneutro de aminoácidos dicarboxílicos ($\text{Asp}^- \rightleftharpoons \text{Glu}^-$), desmintiendo su antigua clasificación errónea como exportador de citrulina. Vectorizado lateralmente para evitar intersecciones con el recuadro del transportador.
- **SLC25A15 (ORNT1):** Asignado unívocamente como el transportador del intercambio catiónico $\text{Ornitina}^+ \rightleftharpoons \text{Citrulina}$. La conexión inter-ruta `cx_citrulina_translocacion` fue reubicada geométricamente para cruzar a través de ORNT1 ($X=4578$) en lugar de Citrina.

### B. Catabolismo secuencial de Cistationina (Vía 12B / CTH)
- La reacción de la Cistationina $\gamma$-Liasa (CTH, EC 4.4.1.1) dejaba de saltar directamente al propionil-CoA. Se agregaron los nodos explícitos de sus 3 productos reales:
  - **L-Cisteína** ($3\text{C}$, producto azufrado) en $X=2830, Y=1735$.
  - **$\alpha$-Cetobutirato** ($4\text{C}$, esqueleto carbonado) en $X=2830, Y=1775$.
  - **$+\ \text{NH}_4^+$** liberado en $X=2770, Y=1735$.
- Actualización del rótulo inter-ruta en `cx_rotulos` a: `"CTH: α-Cetobutirato ➔ Propionil-CoA"`.
- Calibración espacial exacta sin solapamientos con la tirosinemia ni con las conexiones vasculares.

### C. Biosíntesis de Pirimidinas y Timidilato (Vía 15)
- Se incorporó la secuencia explícita $\text{UMP} \to \text{UDP} \to \text{dUDP/dUTP} \to \text{dUMP} \to \text{dTMP}$, explicitando la Ribonucleótido Reductasa (RNR, reducción del $2'\text{-OH}$) y la Timidilato Sintasa ($\text{TS} + N^5,N^{10}\text{-CH}_2\text{-THF}$), clave para entender dianas farmacológicas como el 5-fluorouracilo y el metotrexato.

### D. Fisiología Renal de URAT1 (Vía 16)
- Se corrigió el error conceptual donde URAT1 aparecía secretando urato a la sangre. Se representó adecuadamente como un transportador apical de **reabsorción** desde el lumen tubular proximal hacia la célula epitelial tubular, agregando el nodo de filtrado glomerular/lumen tubular (`renal_lumen_urato`) y reconduciendo la conexión vascular `cx_urato_sangre`.

### E. Vía de las Pentosas Fosfato (Vía 4)
- Conexión explícita del nodo libre de Gliceraldehído-3-Fosfato (`m_gap_pnt`) recibiendo el flujo de la Transcetolasa 2 / Transaldolasa y reingresando formalmente a la glucólisis citosólica.

### F. Puertos de Entrada a Cadena Respiratoria (Vía 7)
- Inclusión de 5 puertos de atraque vectorial (*docking ports*) en el perímetro exterior de la cresta mitocondrial para guiar la lectura de los donantes de equivalentes de reducción:
  - Complejo I (NADH de Krebs y Lanzadera Malato)
  - Complejo II (FADH$_2$ de Succinato DH)
  - CoQ ETF (FADH$_2$ de $\beta$-oxidación)
  - CoQ DHODH (FADH$_2$ de biosíntesis de pirimidinas)
  - CoQ mGPDH (FADH$_2$ de lanzadera de glicerol-3-P)

### G. Rótulos de Conexiones Inter-Ruta Completados
- Corrección de rótulos que se encontraban truncados:
  - `"Lactato (Ciclo de Cori) ➔ Piruvato"`
  - `"Glicerol (Lipólisis TAG) ➔ Glicerol-3-P"`

---

## 3. Verificación Automática y Métricas de Calidad

1. **Detección de Solapamientos (`detectar_solapamientos.py`):**
   ```
   RESUMEN: sin solapamientos
   TOTAL: 0
   ```
   Todas las 11 colisiones previamente reportadas quedaron 100% resueltas.

2. **Auditoría Integral de Vías (`verificar_y_capturar.py`):**
   - 2623 textos, 439 flechas y 50 conexiones inter-ruta verificadas.
   - 0 errores críticos encontrados.

3. **Motor de Flujo Vectorial Bioluminiscente (60 FPS):**
   - Animación acelerada por GPU mediante reglas CSS sobre `stroke-dashoffset` y filtros de resplandor.
   - Activación dinámica al seleccionar una vía en el índice o cambiar el estado metabólico (Posprandial / Ayuno).
   - Botón interruptor "Flujo Animado" en la cabecera para encender o pausar la animación en cualquier instante.

4. **Interactividad HTML:**
   - Soporte para parámetros URL: `?via=6`, `?search=Glucosa`, `?state=ayuno`.
   - Botón interactivo de **Modo Lectura** (resalta y engrosa todas las conexiones y rótulos).
   - Botón interactivo de **Aislar Vía** (oculta por completo las vías atenuadas no seleccionadas).
   - Indexación automática de los nuevos nodos en el buscador en vivo.
   - Depuración tipográfica total sin pictogramas ni emojis en la interfaz ni en el SVG.

---

## 4. Inventario de Archivos en `mapa_metabolico_alternativo/`

- `generar_mapa_alternativo.py`: Script generador autónomo y reproducible.
- `mapa_metabolico_alternativo.svg`: Archivo vectorial maestro con 0 solapamientos y correcciones bioquímicas.
- `mapa_metabolico_alternativo.html`: Visor interactivo autónomo con pan/zoom CTM, motor de flujo animado, índice de 25 vías, búsqueda en vivo, modo lectura, aislamiento y deep linking.
- `mapa_metabolico_alternativo_120x90cm.pdf`: Versión vectorial lista para impresión profesional en gran formato ($120 \times 90\text{ cm}$).
- `mapa_metabolico_alternativo_preview.png`: Vista previa de alta resolución ($2400 \times 1678\text{ px}$).
- `INFORME_MAPA_ALTERNATIVO.md`: Presente documento de balance científico y auditoría.
