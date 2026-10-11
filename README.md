# Mapa Metabólico Integrado

Mapa metabólico celular hepático integral y continuo en formato vectorial SVG y HTML, con 16 rutas metabólicas interconectadas algorítmicamente (A*), regulación alostérica/covalente, clasificación enzimática EC e interactividad web.

---

## 📂 Estructura del Proyecto

```text
├── 01_fuente_python/             # Scripts generadores en Python 3
│   ├── generar_prueba_visual_integrada.py  # Generador principal del mapa base
│   ├── conectar_rutas.py                   # Trazador algorítmico A* de las 46 conexiones
│   ├── detectar_solapamientos.py           # Geometría SVG y detección de colisiones
│   ├── crear_version_interactiva.py        # Compilador de la app interactiva de estudio
│   ├── generar_imprimible.py               # Generador del póster imprimible V1
│   ├── generar_imprimible_v2.py            # Generador del póster imprimible V2 (1200×900 mm)
│   ├── generador_reacciones.py             # Generador modular de micro-reacciones
│   ├── generar_blueprint_excalidraw.py     # Generador de bocetos Excalidraw
│   └── verificar_y_capturar.py             # Suite de verificación headless y capturas
│
├── 02_versiones_html/            # Entregables finales (abrir en navegador)
│   ├── prueba_visual_integrada_conectada.html  # Mapa principal con las 46 rutas conectadas
│   ├── prueba_visual_integrada_conectada.svg   # SVG vectorial puro canónico
│   ├── prueba_visual_interactiva.html          # Herramienta interactiva de estudio (resaltado, buscador, modos)
│   ├── prueba_visual_imprimible_v2.html        # Versión póster 1200×900 mm (V2 definitiva sin franjas)
│   ├── prueba_visual_imprimible.html           # Versión póster V1 con fuentes incrustadas base64
│   ├── prueba_visual_integrada.html            # Mapa base (sin conexiones entre rutas)
│   └── prueba_visual_integrada.svg             # SVG base sin conexiones
│
├── 03_impresion/                 # Archivos para imprenta / preimpresión
│   ├── prueba_visual_imprimible_v2.pdf         # PDF vectorial Ultra HD 1200 × 900 mm (V2)
│   ├── prueba_visual_imprimible.pdf            # PDF vectorial V1
│   └── mapa_metabolico_integrado_prueba.pdf    # Prueba de impresión histórica
│
├── 04_capturas_y_pruebas/        # Renders de comprobación y vistas previas
│   ├── prueba_visual_imprimible_v2_preview.png # Vista previa del póster V2 completo
│   ├── prueba_visual_integrada_conectada_preview.png # Vista previa del mapa conectado
│   ├── prueba_visual_imprimible_v2_seam_*.png  # Comprobación de uniones X=0 y X=5800
│   └── captura_*.png                           # Capturas automáticas de los modos interactivos
│
├── _para_borrar/                 # Archivos obsoletos o temporales (pendientes de confirmación)
│   ├── .aider.chat.history.md
│   ├── .aider.input.history
│   ├── .directory
│   ├── blueprint_cartulina_visual.html
│   ├── blueprint_cartulina_metabolica.excalidraw
│   ├── editor_arrastrable.html
│   └── ejemplo_estilo_visual.html
│
├── 00_GUIA_DISENO_Y_LEYENDA/     # Guías de diseño, convenciones y paleta
├── 01_CARBOHIDRATOS/             # Módulos: Glucólisis, Gluconeogénesis, Glucógeno, Pentosas
├── 02_RESPIRACION_Y_ENERGIA/     # Módulos: PDH, Krebs, Cadena Respiratoria, Lanzaderas
├── 03_LIPIDOS/                   # Módulos: β-Oxidación, Lipogénesis, Cetogénesis, Colesterol
├── 04_NITROGENO_Y_AMINOACIDOS/   # Módulos: Transaminación, Ciclo de la Urea
├── 05_NUCLEOTIDOS_Y_OTRAS/       # Módulos: Síntesis y degradación de nucleótidos
├── 06_REGULACION_Y_LEYENDA/      # Módulos de regulación enzimática y tablas de vías
├── Base_entorno_celular/         # Arte y topología citosólica/mitocondrial
├── IMPRIMIBLES_CARTULINA/        # Recursos cartulina
├── PRUEBA_CITOSOL/               # Pruebas de citosol
├── MANUAL_ESTILO_Y_COMANDOS.txt  # Manual de estilo
└── README.md                     # Documentación principal
```

---

## 🚀 Compilación y Regeneración del Mapa

Todos los scripts pueden ejecutarse directamente desde la raíz del proyecto o desde `01_fuente_python/`:

```bash
# 1. Regenerar el mapa base orgánico celular
python3 01_fuente_python/generar_prueba_visual_integrada.py

# 2. Trazar las 46 conexiones inter-rutas (A* sin cruces destructivos)
python3 01_fuente_python/conectar_rutas.py

# 3. Compilar la versión interactiva de estudio (buscador, modos y resaltado)
python3 01_fuente_python/crear_version_interactiva.py

# 4. Compilar los pósteres listos para imprenta (1200 × 900 mm con fuentes base64 y PDF vectorial)
python3 01_fuente_python/generar_imprimible.py
python3 01_fuente_python/generar_imprimible_v2.py
```

---

## 🔬 Vías Metabólicas Integradas (16 Rutas)

1. **Glucólisis** (Glucosa ➔ Piruvato)
2. **Gluconeogénesis** (Piruvato / Oxalacetato ➔ Glucosa)
3. **Glucogenogénesis y Glucogenólisis** (Glucógeno hepático)
4. **Vía de las Pentosas Fosfato** (Fase oxidativa NADPH y no oxidativa R5P)
5. **Complejo Piruvato Deshidrogenasa (PDH)**
6. **Ciclo de Krebs** (Ciclo del Ácido Cítrico)
7. **Cadena Respiratoria y ATP Sintasa** (Fosforilación oxidativa)
8. **Lanzadera Malato-Aspartato**
9. **Lanzadera Glicerol-3-Fosfato** (8B)
10. **β-Oxidación y Lanzadera de Carnitina**
11. **Lipogénesis** (Síntesis de novo de ácidos grasos)
12. **Cetogénesis** (Cuerpos cetónicos)
13. **Síntesis de Colesterol** (Vía del Mevalonato)
14. **Destinos de los Esqueletos Carbonados de los Aminoácidos** (12B)
15. **Transaminación y Desaminación Oxidativa**
16. **Ciclo de la Urea**
17. **Biosíntesis de Nucleótidos** (Purinas y Pirimidinas)
18. **Catabolismo de Nucleótidos y Ácido Úrico**
