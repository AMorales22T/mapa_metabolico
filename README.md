```
 __  __                         __  __      _        _           _ _           
|  \/  | __ _ _ __   __ _      |  \/  | ___| |_ __ _| |__   ___ | (_) ___ ___  
| |\/| |/ _` | '_ \ / _` |_____| |\/| |/ _ \ __/ _` | '_ \ / _ \| | |/ __/ _ \ 
| |  | | (_| | |_) | (_| |_____| |  | |  __/ || (_| | |_) | (_) | | | (_| (_) |
|_|  |_|\__,_| .__/ \__,_|     |_|  |_|\___|\__\__,_|_.__/ \___/|_|_|\___\___/ 
             |_|                                                               
```

> Atlas metabolico interactivo y vectorial (1200 x 900 mm). 25 vias integradas.

Demo en linea: https://amorales22t.github.io/mapa_metabolico/

================================================================================
CONTENIDO Y FORMATOS
================================================================================

+----------------------------+-------------------------------------------------+
| Recurso                    | Enlace / Ubicacion                              |
+----------------------------+-------------------------------------------------+
| Mapa Alternativo (Vivo)    | index.html (flujo 60 FPS, lanzaderas, CTE)      |
| Mapa Original (Base)       | versiones_html/01_mapa_ampliado_completo_25_vias|
| Standalone Vias 18-25      | versiones_html/02_ampliacion_rutas_18_25.html   |
| Cuadro Temario Bloques A-E | versiones_html/04_cuadro_temario_bloques_A_E.htm|
| PDF Alternativo (Poster)   | mapa_metabolico_alternativo/..._120x90cm.pdf    |
| PDF Original (Poster)      | versiones_impresion/01_mapa_..._120x90cm.pdf    |
| SVG Alternativo            | mapa_metabolico_alternativo/...alternativo.svg  |
| SVG Original               | 07_AMPLIACION_TEMARIO/mapa_cartulina_ampliado   |
+----------------------------+-------------------------------------------------+

================================================================================
CARACTERISTICAS
================================================================================

* 25 Vias Integradas:
  - Carbohidratos: Glucolisis, Gluconeogenesis, Glucogeno, Pentosas Fosfato.
  - Respiracion: Complejo PDH, Ciclo de Krebs, Cadena de Transporte de Electrones.
  - Lanzaderas Redox: Malato-Aspartato, Glicerol-3-Fosfato, Carnitina.
  - Lipidos: Beta-Oxidacion, Lipogenesis de Novo, Cetogenesis, Colesterol.
  - Nitrogeno y AA: Ciclo de la Urea, Transaminacion, Transulfuracion (CTH).
  - Nucleotidos: Sintesis Purinas/Pirimidinas, Degradacion y URAT1.
  - Intertisular: Ciclo de Cori/Cahill, Digestion, Adipocito, Sarcomero, BHE,
    Lipoproteinas (VLDL/LDL/HDL), Via de Kennedy, AA no esenciales, Hormonas.

* Selector en Linea (GitHub Pages):
  - Conmutador directo entre Mapa Alternativo y Mapa Base en la barra superior.
  - Selector desplegable de rutas individuales con modo de aislamiento visual.
  - Sincronizacion directa con URL (?via=1 a ?via=25).

* Motor Vectorial:
  - 100% SVG nativo, sin dependencias externas pesadas.
  - Flujo animado a 60 FPS con aceleracion CSS y particulas SMIL.
  - 0 colisiones en detector de solapamientos geometricos.

================================================================================
ESTRUCTURA DEL REPOSITORIO
================================================================================

.
|-- index.html                              # Portal GitHub Pages (Mapa Alternativo)
|-- mapa_metabolico_alternativo/            # Entregables alternativos (SVG, HTML, PDF, PNG)
|-- versiones_html/                         # Visores HTML interactivos
|-- versiones_impresion/                    # Archivos PDF para impresion (1200 x 900 mm)
|-- scripts_generacion/                     # Generadores y detector de solapamientos
|-- 00 a 07/                               # Modulos bioquimicos y mapa base original
`-- AUDITORIA_INTEGRAL_MAPA_METABOLICO.txt  # Reporte completo de trazabilidad

================================================================================
EJECUCION LOCAL
================================================================================

Generar mapa alternativo (SVG, HTML, PDF, PNG):
  python3 mapa_metabolico_alternativo/generar_mapa_alternativo.py

Verificar colisiones geometricas (debe dar 0):
  python3 scripts_generacion/detectar_solapamientos.py mapa_metabolico_alternativo/mapa_metabolico_alternativo.svg
