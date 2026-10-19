# 🧬 Atlas Metabólico Interactivo y Vectorial (1200 × 900 mm)

[![GitHub Pages](https://img.shields.io/badge/Demo-GitHub%20Pages-0284c7?style=flat&logo=github)](https://amorales22t.github.io/mapa_metabolico/)
[![Licencia](https://img.shields.io/badge/Licencia-CC%20BY--NC--ND%204.0-38bdf8?style=flat)](LICENSE)
[![Rutas Integradas](https://img.shields.io/badge/Vías%20Metabólicas-25%20Integradas-10b981?style=flat)](#vías-incluidas-25)
[![SVG Nativo](https://img.shields.io/badge/Motor-100%25%20SVG%20Nativo-f59e0b?style=flat)](#motor-vectorial)

> Plataforma didáctica y atlas visual interactivo de bioquímica con 25 vías integradas, navegación guiada paso a paso, simuladores de lanzaderas mitocondriales y cadena respiratoria.

---

## 🎬 Demostración en Vivo

[![Demostración del Mapa Metabólico](capturas_y_pruebas/mapa_metabolico_demo.gif)](https://amorales22t.github.io/mapa_metabolico/)

🌐 **Acceso directo en la web:** [https://amorales22t.github.io/mapa_metabolico/](https://amorales22t.github.io/mapa_metabolico/)

---

## ⚡ Guía Rápida de Uso

- **Índice lateral de vías:** pulsa en el botón **Índice** para desplegar las 25 rutas metabólicas. Al hacer clic en una ruta, la vista se centra suavemente y resalta sus metabolitos e interconexiones.
- **Navegación espacial:** arrastra libremente el lienzo (pan) y utiliza la rueda del ratón o gestos para zoom dinámico sin pérdida de resolución vectorial.
- **Modo didáctico Paso a Paso:** haz clic en **Paso a Paso** para inspeccionar secuencialmente cada reacción de la vía activa, visualizando enzimas (código EC), cofactores, $\Delta G^\circ$ y mecanismos de regulación.
- **Cadena Respiratoria y Lanzaderas:** al pulsar sobre la lupa de la *Cadena de Transporte de Electrones* o de las *Lanzaderas Mitocondriales*, se activa un monitor especializado por fases (Complejos I–IV, ATP sintasa, malato-aspartato, glicerol-3-fosfato y carnitina).
- **Flujo biológico:** las partículas bioluminiscentes se encuentran pausadas por defecto para optimizar el rendimiento. Puedes activarlas pulsando **Flujo Animado**.
- **Acceso directo por URL:** añade `?via=1` hasta `?via=25` a la URL para enlazar o compartir directamente una ruta específica.

---

## 📦 Contenido y Formatos Disponibles

| Recurso | Descripción | Ubicación |
| :--- | :--- | :--- |
| **Mapa Interactivo (Portal)** | Aplicación web completa y autónoma (SVG + motor JS) | [`index.html`](index.html) |
| **Mapa Alternativo (Entregables)** | Versión vectorial con flujo y visualización limpia | [`mapa_metabolico_alternativo/`](mapa_metabolico_alternativo/) |
| **Mapa Base (Cartulina)** | Diagrama maestro ampliado completo con las 25 vías | [`versiones_html/01_mapa_ampliado_completo_25_vias.html`](versiones_html/01_mapa_ampliado_completo_25_vias.html) |
| **Ampliación Rutas 18–25** | Vista aislada de vías intertisulares y de integración | [`versiones_html/02_ampliacion_rutas_18_25.html`](versiones_html/02_ampliacion_rutas_18_25.html) |
| **Póster de Impresión (PDF)** | Formato póster gigante listo para imprenta ($1200 \times 900\text{ mm}$) | [`versiones_impresion/`](versiones_impresion/) |
| **Vías Individuales (SVG)** | Diagramas vectoriales modulares clasificados por bloque | [`01_CARBOHIDRATOS/`](01_CARBOHIDRATOS/) a [`05_NUCLEOTIDOS_Y_OTRAS/`](05_NUCLEOTIDOS_Y_OTRAS/) |

---

## 🗺️ Vías Incluidas (25)

1. **Carbohidratos:** Glucólisis, Gluconeogénesis, Glucogenogénesis/Glucogenólisis, Vía de las Pentosas Fosfato y Ciclo de Cori.
2. **Respiración y Bioenergética:** Complejo Piruvato Deshidrogenasa (PDH), Ciclo de Krebs y Cadena de Transporte de Electrones con ATP sintasa.
3. **Lanzaderas Redox Mitocondriales:** Lanzadera de Malato-Aspartato, Glicerol-3-Fosfato y Lanzadera de Carnitina.
4. **Lípidos:** $\beta$-Oxidación de ácidos grasos, Lipogénesis *de novo*, Cetogénesis/Cetólisis y Síntesis de Colesterol.
5. **Nitrógeno y Aminoácidos:** Ciclo de la Urea, Transaminación/Desaminación oxidativa y Vía de Transulfuración (CTH).
6. **Nucleótidos:** Síntesis *de novo* de Purinas y Pirimidinas, Degradación de Purinas y transportador URAT1.
7. **Integración Tisular e Interorganos:** Ciclo glucosa-alanina (Cahill), regulación en adipocito y sarcómero, barrera hematoencefálica (BHE), metabolismo de lipoproteínas (VLDL/LDL/HDL) y vía de Kennedy.

---

## ⚙️ Motor y Arquitectura

- **100% SVG nativo:** renderizado vectorial escalable sin dependencias de frameworks externos pesados.
- **Micro-animaciones declarativas:** partículas SMIL (`<animateMotion>`) y flujos CSS de bajo impacto.
- **Integración continua:** despliegue automatizado a GitHub Pages mediante GitHub Actions ([`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)) con cada push a la rama `main`.

---

## 💻 Ejecución Local

Para visualizar el mapa localmente en cualquier navegador:

```bash
# Servir desde la raíz del repositorio
python3 -m http.server 8000
```
Luego abre tu navegador en `http://localhost:8000/`.

---

## ⚖️ Autoría y Licencia

**Autor:** [AMorales22T](https://github.com/AMorales22T) — Repositorio oficial: [AMorales22T/mapa_metabolico](https://github.com/AMorales22T/mapa_metabolico)

Este proyecto se distribuye bajo la licencia **[Creative Commons Atribución-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/)**.

- ✅ **Se permite:** compartir, visualizar y utilizar este material con fines académicos y de estudio personal, conservando siempre la atribución original al autor y el enlace al repositorio oficial.
- ❌ **No comercial:** no está permitido su uso comercial ni su venta en ninguna plataforma.
- ❌ **Sin obras derivadas:** no se autoriza la redistribución de versiones modificadas, adaptadas o desprovistas del crédito original de autoría.
