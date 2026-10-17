# 📚 Historial de Versiones del Mapa Metabólico Celular Integrado

Este directorio preserva todas las etapas de desarrollo y evolución del atlas metabólico, desde su concepción central inicial hasta la versión ampliada y auditada para imprenta.

---

## 🗂️ Índice de Versiones

### 1. [Versión 1 — Hepatocito Central (17 Vías Troncales)](version_1/README.md)
* **Directorio:** [`version_1/`](version_1/) (o `version 1/`)
* **Alcance:** Mapa central del hepatocito que agrupa las 17 rutas del metabolismo intermediario estándar (glucólisis, Krebs, CTE, beta-oxidación, urea, purinas/pirimidinas, lanzaderas, etc.).
* **Archivos:**
  - `mapa_metabolico_v1.html`: Visor web interactivo original.
  - `mapa_metabolico_v1.pdf`: PDF vectorial para póster (1200 × 900 mm).
  - `mapa_metabolico_v1.svg`: Archivo vectorial fuente.

### 2. [Versión 2 — Ampliación a 25 Vías](version_2/README.md)
* **Directorio:** [`version_2/`](version_2/) (o `version 2/`)
* **Alcance:** Incorporación de las bandas laterales (vías 18 a 25: digestión lipídica, adipocito, sarcómero en músculo esquelético, cerebro y BHE, lipoproteínas plasmáticas, Kennedy y biosíntesis de aminoácidos no esenciales). Diseño preliminar previo a la auditoría técnica.
* **Archivos:**
  - `mapa_metabolico_v2.html`: Visor interactivo ampliado preliminar.
  - `mapa_metabolico_v2.pdf`: PDF vectorial (1200 × 900 mm y 1200 × 840 mm).
  - `mapa_metabolico_v2.svg`: Código SVG completo con las 25 rutas integradas.

### 3. [Versión Final — Oficial, Auditada y Corregida](version_final/README.md) ⭐
* **Directorio:** [`version_final/`](version_final/) (o `version final/`)
* **Alcance:** **Versión de producción oficial.** Incorpora todas las correcciones biológicas y de diseño validadas en la auditoría exhaustiva:
  - Corrección de transportador a **GLUT-2** en hepatocito.
  - Bifurcación real en 'Y' de la **Aldolasa** hacia DHAP y GAP.
  - Despeje total del canal colector lipolítico en adipocito.
  - Marcadores de inhibición `#inhibitionT` y contraste de H⁺ optimizado.
  - Incorporación de códigos oficiales de la Enzyme Commission (**EC**) en reacciones troncales.
  - Cero solapamientos verificados con el algoritmo detector ortogonal.
* **Archivos:**
  - `mapa_metabolico_final.html`: Visor oficial interactivo completo.
  - `mapa_metabolico_final.pdf`: PDF vectorial Ultra-HD 1:1 listo para imprenta profesional.
  - `mapa_metabolico_final.svg`: SVG vectorial depurado.
  - `mapa_metabolico_final_preview.png`: Vista previa renderizada en alta resolución (2400 × 1678 px).
