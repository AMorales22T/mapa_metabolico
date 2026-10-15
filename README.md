# Mapa Metabólico Celular Integrado y Temario Ampliado

> **Atlas Bioquímico Vectorial Ultra-HD (1200 × 900 mm) & Suite Interactiva de Estudio**  
> **Autor:** Adolfo Morales Tena ([@AMorales22T](https://github.com/AMorales22T))  
> **Repositorio Oficial:** [https://github.com/AMorales22T/mapa_metabolico](https://github.com/AMorales22T/mapa_metabolico)  
> **Licencia:** MIT Open Source

---

## 🌟 Resumen del Proyecto

El **Mapa Metabólico Celular Integrado** es un mapa continuo, anatómico y algorítmico diseñado para estudiantes, docentes e investigadores de **Medicina, Bioquímica, Farmacia y Ciencias Biomédicas**. Representa de forma panorámica y continua el metabolismo celular eucariota (con foco en el hepatocito central y su integración con músculo, tejido adiposo, encéfalo y torrente vascular) a través de **25 vías metabólicas interconectadas** mediante el **algoritmo de pathfinding A\*** sin cruces destructivos.

El proyecto se presenta en dos formatos fundamentales:
1. **Pósteres Vectoriales Imprimibles (1200 × 900 mm):** Compilados en SVG y PDF de alta definición listos para imprenta o cartulina académica, con tipografías vectoriales incrustadas en base64 y código QR escaneable hacia el repositorio.
2. **Suite Interactiva Web (HTML5/CSS3/ES6):** Visores de estudio con navegación suave por arrastre y zoom vectorial afín (CTM), buscador diacrítico instantáneo, fichas técnicas flotantes para enzimas y metabolitos, índice lateral con 25 vías e indicador de estados nutricionales (**Normal**, **Posprandial** y **Ayuno**).

---

## 🧭 Guía Rápida de Entregables (Nombres Claros y Numerados)

Para evitar confusiones con versiones y archivos preliminares, todos los entregables oficiales finales están organizados con una **nomenclatura numérica unificada (01 a 04)**:

### 🌐 Visores HTML Interactivos (`versiones_html/`)
| Archivo Numerado | Descripción del Entregable | Vías |
| :--- | :--- | :---: |
| **`01_mapa_ampliado_completo_25_vias.html`** | **Póster Completo Integrado:** Hepatocito central (17 vías) + 8 vías de integración periférica en lienzo continuo de 1200 × 900 mm. Resaltado por clic, buscador y zoom CTM. | **1 a 25** |
| **`02_ampliacion_rutas_18_25.html`** | **Ampliación Especializada Standalone:** Visor enfocado exclusivamente en las vías 18 a 25 (sin el mapa central integrado), ideal para estudiar digestión, lipólisis adiposa, sarcómero, cerebro y lipoproteínas. | **18 a 25** |
| **`03_mapa_central_interactivo_17_vias.html`** | **Mapa Central Hepatocitario Original:** La herramienta interactiva de referencia del hepatocito troncal (Glucólisis, Gluconeogénesis, Glucógeno, Krebs, Cadena Respiratoria, Urea, etc.). | **1 a 17** |
| **`04_cuadro_temario_bloques_A_E.html`** | **Cuadro Temático de Metabolismo Intermediario:** Clasificación por bloques temáticos complementarios (A a E) con tablas de cofactores, balances de ATP y regulación. | **Bloques A–E** |
| **`index.html`** | **Centro de Visores / Hub Principal:** Portal de bienvenida que enlaza a las cuatro modalidades interactivas y descargas directas en PDF. | **Portal** |

*(Nota: Los archivos con nomenclatura previa como `prueba_visual_interactiva.html`, `mapa_cartulina_ampliado.html` o `ampliacion_rutas_18_25_interactiva.html` se mantienen como enlaces directos para preservar la compatibilidad con scripts existentes).*

### 🖨️ Documentos Vectoriales para Impresión (`versiones_impresion/`)
| Archivo PDF | Dimensiones | Resolución / Formato |
| :--- | :---: | :--- |
| **`01_mapa_ampliado_completo_120x90cm.pdf`** | **1200 × 900 mm** | PDF Vectorial Ultra-HD (25 vías completas con torrente continuo) |
| **`02_ampliacion_rutas_18_25.pdf`** | **1200 × 900 mm** | PDF Vectorial Standalone (Vías 18 a 25 con estructuras químicas) |
| **`03_mapa_central_original_120x90cm.pdf`** | **1200 × 900 mm** | PDF Vectorial Ultra-HD (Mapa central original sin costuras) |

---

## 📂 Estructura General del Proyecto

```text
├── scripts_generacion/                 # Scripts generadores en Python 3
│   ├── generar_prueba_visual_integrada.py  # Generador principal del mapa base celular
│   ├── conectar_rutas.py                   # Trazador algorítmico A* de las 45 conexiones inter-ruta
│   ├── detectar_solapamientos.py           # Geometría SVG y detección de colisiones de texto/cajas
│   ├── crear_version_interactiva.py        # Compilador de la app interactiva de estudio central
│   ├── generar_imprimible_v2.py            # Generador del póster central imprimible (1200×900 mm)
│   ├── generador_reacciones.py             # Generador modular de micro-reacciones
│   └── verificar_y_capturar.py             # Suite de verificación headless y comprobación de fuentes
│
├── versiones_html/                # Entregables interactivos (abrir en cualquier navegador moderno)
│   ├── index.html                          # Centro de visores interactivos (portal principal)
│   ├── 01_mapa_ampliado_completo_25_vias.html # Mapa ampliado interactivo completo (25 vías)
│   ├── 02_ampliacion_rutas_18_25.html         # Ampliación interactiva standalone (vías 18 a 25)
│   ├── 03_mapa_central_interactivo_17_vias.html # Mapa central interactivo (17 vías troncales)
│   ├── 04_cuadro_temario_bloques_A_E.html     # Cuadro temático interactivo (bloques A–E)
│   ├── prueba_visual_integrada_conectada.svg # SVG vectorial canónico con las 45 conexiones
│   └── prueba_visual_imprimible_v2.html     # Versión póster con fuentes incrustadas base64
│
├── versiones_impresion/                     # Archivos de imprenta profesional
│   ├── 01_mapa_ampliado_completo_120x90cm.pdf # PDF vectorial Ultra-HD del mapa ampliado (25 vías)
│   ├── 02_ampliacion_rutas_18_25.pdf          # PDF vectorial de la ampliación standalone
│   └── 03_mapa_central_original_120x90cm.pdf  # PDF vectorial Ultra-HD del mapa central
│
├── capturas_y_pruebas/            # Renders de comprobación visual y análisis de cobertura
│   ├── prueba_visual_imprimible_v2_preview.png # Vista previa del póster V2 completo (95.37% de cobertura)
│   ├── prueba_visual_imprimible_v2_seam_*.png  # Validación microscópica de uniones X=0 y X=5800
│   └── capturas_modos_*.png                    # Capturas automáticas de los modos ayuno y posprandial
│
├── 06_REGULACION_Y_LEYENDA/          # Base de datos bioquímica unificada
│   ├── regulacion.py                       # Catálogo de efectores ⊕/⊖, fosforilaciones y números EC
│   ├── LEYENDA_VIAS.md                     # Documento de especificación de vías
│   └── REGULACION_ENZIMATICA.md            # Fichas técnicas de enzimas reguladas
│
├── 07_AMPLIACION_TEMARIO/            # Generadores de la ampliación periférica y temario universitario
│   ├── generar_ampliacion.py               # Ensamblador del mapa ampliado completo (7320 × 5490 px)
│   ├── generar_ampliacion_standalone.py    # Ensamblador de la ampliación standalone (vías 18 a 25)
│   ├── interactividad_html.py              # Motor de interactividad para los visores de 25 vías
│   ├── actualizar_interactividad_temario.py# Motor interactivo para el temario de bloques A–E
│   ├── estructuras_ampliacion.py           # Fórmulas moleculares SVG (TAG, DAG, MAG, sarcómero, etc.)
│   └── index.html                          # Landing page local de la suite ampliada
│
├── 00_GUIA_DISENO_Y_LEYENDA/         # Guías de paleta de colores y convenciones visuales
├── 01_CARBOHIDRATOS/                 # Módulos: Glucólisis, Gluconeogénesis, Glucógeno, Pentosas, Cori
├── 02_RESPIRACION_Y_ENERGIA/         # Módulos: PDH, Krebs, Cadena Respiratoria, Lanzaderas Redox
├── 03_LIPIDOS/                       # Módulos: β-Oxidación, Lipogénesis, Cetogénesis, Colesterol
├── 04_NITROGENO_Y_AMINOACIDOS/       # Módulos: Transaminación, Ciclo de la Urea, Esqueletos AA
├── 05_NUCLEOTIDOS_Y_OTRAS/           # Módulos: Síntesis de Novo, Salvamento y Degradación a Ácido Úrico
├── .github/workflows/deploy.yml      # Despliegue automatizado en GitHub Pages (CI/CD)
└── README.md                         # Este documento
```

---

## 🔬 Las 25 Vías Metabólicas Integradas

### Bloque Central: Hepatocito Troncal (Vías 1 a 17)
1. **Glucólisis** (Glucosa ➔ 2 Piruvato; +2 ATP neto, +2 NADH; puntos de control HK, PFK-1, PK).
2. **Gluconeogénesis** (Piruvato/OAA/Lactato ➔ Glucosa; 3 rodeos metabólicos sorteando las reacciones irreversibles; PC, PEPCK, FBPasa-1, G6Pasa en el retículo endoplásmico).
3. **Glucogenogénesis y Glucogenólisis** (Almacenamiento y liberación de glucosa hepática; Glucógeno Sintasa y Glucógeno Fosforilasa con control recíproco covalente).
4. **Vía de las Pentosas Fosfato** (G6P ➔ NADPH para defensas antioxidantes GSH y lipogénesis; fase no oxidativa de reciclaje con Transaldolasa y Transcetolasa).
5. **Complejo Piruvato Deshidrogenasa (PDH)** (Decarboxilación oxidativa de Piruvato a Acetil-CoA en matriz mitocondrial; regulación por PDH Quinasa y Fosfatasa).
6. **Ciclo de Krebs (Ciclo del Ácido Cítrico)** (Oxidación total del grupo acetilo; 2 CO₂, 3 NADH, 1 FADH₂, 1 GTP; enzimas anfibólicas y anaplerosis).
7. **Cadena de Transporte de Electrones y ATP Sintasa** (Fosforilación oxidativa; Complejos I a IV, gradiente electroquímico de protones $\Delta\mu_{H^+}$ y rotor molecular $F_oF_1$).
8. **Lanzadera Malato-Aspartato** (Transporte de equivalentes redox de NADH citosólico a matriz; 2.5 ATP por par de electrones; antiportadores MDH, GOT/AST y AGC).
9. **Lanzadera de Glicerol-3-Fosfato (Vía 8B)** (Reoxidación rápida de NADH hacia FAD de la membrana mitocondrial interna; 1.5 ATP; esencial en músculo y cerebro).
10. **β-Oxidación de Ácidos Grasos** (Activación citosólica a Acil-CoA, lanzadera de carnitina CPT-I / CACT / CPT-II y espiral oxidativa mitocondrial).
11. **Lipogénesis (Síntesis de Novo de Ácidos Grasos)** (Lanzadera de citrato, Acetil-CoA Carboxilasa [ACC], Complejo Sintasa de Ácidos Grasos [FAS] ➔ Palmitato).
12. **Cetogénesis Hepática** (Exceso de Acetil-CoA mitocondrial ➔ Acetoacetato y D-β-Hidroxibutirato; HMG-CoA Sintasa mitocondrial; exportación a tejidos extrahepáticos).
13. **Síntesis de Colesterol** (Vía citosólica del mevalonato; HMG-CoA Reductasa [HMGCR], farnesil pirofosfato, escualeno y ciclación a colesterol).
14. **Destinos de los Esqueletos Carbonados de los Aminoácidos (Vía 12B)** (Convergencia de los 20 aminoácidos en Piruvato, Acetil-CoA, Acetoacetato, $\alpha$-Cetoglutarato, Succinil-CoA, Fumarato y Oxalacetato).
15. **Transaminación y Desaminación Oxidativa** (Recogida del nitrógeno amino por transaminasas GPT/ALT y GOT/AST hacia Glutamato; Glutamato Deshidrogenasa mitocondrial libera $NH_4^+$).
16. **Ciclo de la Urea** (Desintoxicación de amonio en matriz y citosol hepático; Carbamoil Fosfato Sintetasa I [CPS-I], Ornitina Transcarbamilasa, Argininosuccinato y Arginasa; acoplamiento al biciclo de Krebs).
17. **Biosíntesis de Nucleótidos (Purinas y Pirimidinas)** (Convergencia sobre PRPP; síntesis de novo de IMP y UMP; enzimas de salvamento HGPRT y APRT).
18. **Catabolismo de Nucleótidos y Ácido Úrico** (Degradación de purinas a través de Xantina Oxidasa [XOD] hacia Ácido Úrico; degradación de pirimidinas a $\beta$-Alanina soluble).
19. **Ciclo de Cori (Acoplamiento Músculo-Hígado)** (Lactato producido anaeróbicamente en músculo esquelético o eritrocitos transportado por sangre al hígado para reconversión en glucosa mediante gluconeogénesis con coste neto de -4 ATP).

### Bloque Periférico e Integración Tisular (Vías 18 a 25)
18. **Digestión y Absorción de Lípidos:** Luz del intestino delgado, emulsificación biliar en micelas mixtas, acción de Lipasa Pancreática y Colipasa, absorción enterocitaria, reesterificación en REL y empaquetamiento en quilomicrones hacia la linfa quilífera.
19. **Tejido Adiposo y Cascada Lipolítica:** Movilización hormonal de reservas energéticas en la gota lipídica; cascada secuencial enzimática con estructuras químicas completas: $\text{TAG} \xrightarrow{\text{ATGL}} \text{DAG} \xrightarrow{\text{HSL}} \text{2-MAG} \xrightarrow{\text{MGL}} \text{Glicerol} + 3\,\text{AG libres}$.
20. **Músculo Esquelético y Ultraestructura del Sarcómero:** Detalle anatómico del sarcómero estriado en contracción (líneas Z, filamentos delgados de actina, filamentos gruesos de miosina, cabezas globulares y túbulo T con cisterna terminal de $Ca^{2+}$); acoplamiento metabólico al ciclo de Cori (Lactato) y ciclo glucosa-alanina de Cahill (Alanina).
21. **Cerebro y Combustibles Neuronales:** Paso a través de la barrera hematoencefálica (BHE) por transportadores de alta afinidad GLUT1 (endotelio) y GLUT3 (neuronas); adaptación metabólica en ayuno prolongado al consumo de cuerpos cetónicos mediante transportadores monocarboxilato (MCT1/MCT2).
22. **Metabolismo de Lipoproteínas Plasmáticas:** Vía endógena hepática con secreción de VLDL, hidrólisis endotelial por LPL formando IDL y LDL, captación tisular por el receptor LDLR (con apoproteínas ApoB-100 y ApoE), y transporte reverso de colesterol mediante HDL nacientes, LCAT y receptor scavenger SR-B1.
23. **Biosíntesis de Triacilgliceroles y Fosfolípidos (Vía de Kennedy):** Síntesis microsomal de novo a partir de Glicerol-3-P ➔ Ácido Lisofosfatídico (LPA) ➔ Ácido Fosfatídico (PA) ➔ 1,2-Diacilglicerol (DAG) ➔ Triacilglicerol (TAG) o Fosfatidilcolina (PC) para ensamblaje de membranas y VLDL.
24. **Biosíntesis de Aminoácidos No Esenciales:** Rutas anabólicas de síntesis de los 10 aminoácidos que el ser humano produce a partir de intermediarios de la glucólisis y del ciclo de Krebs (Ala, Ser, Gly, Cys, Asp, Asn, Glu, Gln, Pro, Tyr).
25. **Conmutador Nutricional e Integración Metabólica:** Comparativa gráfica y hormonal de flujos entre el estado **Posprandial** (dominado por Insulina; anabolismo, almacenamiento de glucógeno y lipogénesis), el estado de **Ayuno** (dominado por Glucagón y Adrenalina; glucogenólisis, gluconeogénesis, lipólisis y cetogénesis) y **Ejercicio Vigoroso** (acoplamiento anaeróbico de Cori y consumo fosfágeno).

---

## 🎨 Código de Colores y Convenciones Visuales

La identidad cromática del mapa respeta estándares editoriales de bioquímica para facilitar la retención visual:

* 🔵 **Carbohidratos y Glucólisis:** Azul cian (`#0284c7`) y azul profundo (`#0f172a`).
* 🟣 **Gluconeogénesis:** Púrpura / Violeta real (`#7c3aed`), diferenciando claramente las enzimas de rodeo de los pasos glicolíticos reversibles.
* 🟠 **Metabolismo del Glucógeno:** Naranja energético (`#ea580c`).
* 🟢 **Vía de las Pentosas Fosfato:** Verde esmeralda (`#059669`).
* 🟤 **Ciclo de Krebs y PDH:** Ámbar dorado (`#d97706`) y terracota (`#c2410c`).
* 🟢 **Cadena Respiratoria y ATP Sintasa:** Verde clorofila (`#16a34a`).
* 🟤 **Lípidos y β-Oxidación:** Marrón cálido (`#b45309`) y cerceta (`#0d9488`).
* 🔴 **Cetogénesis y Ciclo de Cori:** Carmín / Borgoña (`#be123c` / `#9f1239`).
* 🔵 **Metabolismo del Nitrógeno, Aminoácidos y Ciclo de la Urea:** Azul real (`#2563eb`) y cian marino (`#0891b2`).
* 🟣 **Biosíntesis de Nucleótidos y Colesterol:** Índigo (`#4f46e5`) y azul acero (`#475569`).

### Convenciones de Regulación y Nomenclatura
* **`(+)` en verde (`#16a34a`):** Activador alostérico (efector positivo).
* **`(-)` en rojo (`#dc2626`):** Inhibidor alostérico (retroinhibición por producto o carga energética).
* **`(P)` en dorado (`#ca8a04`):** Regulación covalente por fosforilación (especificando si la forma fosforilada es activa o inactiva según tejido).
* **`▭` Caja rectangular redondeada:** Transportador o carrier de membrana (GLUT1-4, MPC, CACT, AGC, MCT, ABC...).
* **`[nC]`:** Número de átomos de carbono del metabolito para seguimiento estequiométrico.
* **Código `EC x.x.x.x`:** Código oficial de 4 cifras de la *Enzyme Commission* (Oxidorreductasas, Transferasas, Hidrolasas, Liasas, Isomerasas, Ligasas, Translocasas).

---

## 🛠️ Herramientas y Tecnologías Utilizadas

El desarrollo del mapa ha requerido una arquitectura multidisciplinar que combina ciencias biológicas, matemáticas discretas, ingeniería gráfica vectorial y desarrollo web nativo:

1. **Python 3 (Lenguaje Núcleo):**
   * Motor procedural que calcula coordenadas espaciales, ángulos trigonométricos de flechas y estequiometrías.
   * Generación programática de estructuras químicas moleculares en SVG puro (enlaces de Fischer, proyecciones de Haworth, grupos fosfato y esqueletos carbonados).
2. **Algoritmo de Pathfinding A\* (A-Star):**
   * Implementado en `scripts_generacion/conectar_rutas.py`.
   * Opera sobre una rejilla ortogonal discreta de **484 × 427 celdas** (paso de 12 px) que detecta dinámicamente más de 3900 obstáculos biológicos (metabolitos, etiquetas enzimáticas, membranas).
   * Traza las **45 conexiones metabólicas** minimizando la longitud, con penalización de esquinas (giros suaves) y evitando cruces con vías incompatibles.
3. **SVG 1.1 / SVG 2.0 (Scalable Vector Graphics):**
   * Estándar vectorial abierto W3C.
   * Permite resolución infinita tanto en un visor web 4K como en una cartulina de 1.20 metros impresa a 300 ppp sin pixelación.
4. **librsvg (`rsvg-convert`):**
   * Motor nativo de renderizado utilizado para compilar el SVG a PDF vectorial Ultra-HD respetando medidas físicas exactas (`1200mm × 900mm`) y para generar vistas previas PNG de comprobación analítica.
5. **HTML5 / CSS3 / ES6 (JavaScript Nativo Moderno):**
   * Interfaz de estudio interactiva de alto rendimiento sin sobrecarga de frameworks externos (0 dependencias de npm en runtime).
   * Manipulación fluida de matriz afín mediante `matrixTransform` y `getCTM()` de SVG para zoom centrado exacto y pan con inercia.
   * Buscador universal insensible a acentos ni mayúsculas implementado mediante `String.normalize('NFD')` y animación de pulso con filtros SVG (`feDropShadow`).
   * Soporte táctil completo para tabletas y pantallas táctiles (arrastre con 1 dedo y zoom por pellizco con 2 dedos).
6. **libqrencode (`qrencode`):**
   * Generador algorítmico utilizado para sintetizar la matriz bidimensional de 29×29 módulos del código QR que enlaza vectorialmente al repositorio oficial de GitHub.
7. **Chromium / Brave Headless:**
   * Utilizado para comprobaciones automatizadas de fidelidad tipográfica, pruebas de exportación a PDF y verificación de texto vectorial con `pdftotext`.
8. **GitHub Actions (`.github/workflows/deploy.yml`):**
   * Flujo de integración y despliegue continuo (CI/CD) que compila y publica automáticamente la suite completa de visores en **GitHub Pages** con cada actualización en la rama principal `main`.

---

## 📚 Bibliografía Científica de Referencia

La precisión bioquímica de todas las rutas, enzimas, cofactores, transportadores y balances de energía se ha contrastado rigurosamente con la literatura de referencia internacional:

1. **Nelson, D. L., & Cox, M. M.** (2018/2021). *Lehninger Principios de Bioquímica* (7.ª y 8.ª ed.). Editorial Médica Panamericana / Ediciones Omega.
2. **Rodwell, V. W., Bender, D. A., Botham, K. M., Kennelly, P. J., & Weil, P. A.** (2018/2022). *Harper: Bioquímica Ilustrada* (31.ª y 32.ª ed.). McGraw-Hill Education.
3. **Devlin, T. M.** (2015). *Bioquímica: Libro de Texto con Aplicaciones Clínicas* (4.ª y 5.ª ed.). Editorial Reverté.
4. **Berg, J. M., Tymoczko, J. L., Gatto, G. J., & Stryer, L.** (2019/2020). *Bioquímica* (8.ª y 9.ª ed.). Editorial Reverté.
5. **Michal, G., & Schomburg, D.** (2012). *Biochemical Pathways: An Atlas of Biochemistry and Molecular Biology* (2.ª ed.). John Wiley & Sons / Roche Applied Science.
6. **Kanehisa Laboratories.** *KEGG: Kyoto Encyclopedia of Genes and Genomes* (Pathway Maps for Homo sapiens). [https://www.kegg.jp/](https://www.kegg.jp/)
7. **IUPAC-IUBMB Joint Commission on Biochemical Nomenclature.** *Enzyme Nomenclature Recommendations* (EC classification). [https://www.qmul.ac.uk/sbcs/iubmb/enzyme/](https://www.qmul.ac.uk/sbcs/iubmb/enzyme/)

---

## 🚀 Regeneración y Compilación del Proyecto

Para regenerar todo el conjunto de mapas desde el código fuente Python:

```bash
# 1. Regenerar el mapa base orgánico celular
python3 scripts_generacion/generar_prueba_visual_integrada.py

# 2. Trazar las 45 conexiones inter-ruta con el algoritmo A*
python3 scripts_generacion/conectar_rutas.py

# 3. Compilar la herramienta de estudio interactiva del mapa central (17 vías)
python3 scripts_generacion/crear_version_interactiva.py

# 4. Generar el póster central imprimible V2 (1200 × 900 mm)
python3 scripts_generacion/generar_imprimible_v2.py

# 5. Generar el mapa ampliado completo de 25 vías (HTML interactivo y PDF)
python3 07_AMPLIACION_TEMARIO/generar_ampliacion.py

# 6. Generar la ampliación especializada standalone (Vías 18 a 25)
python3 07_AMPLIACION_TEMARIO/generar_ampliacion_standalone.py

# 7. Actualizar el cuadro temático interactivo de bloques A a E
python3 07_AMPLIACION_TEMARIO/actualizar_interactividad_temario.py
```

---

## 👤 Autoría y Contacto

* **Autor:** **Adolfo Morales Tena**
* **Usuario GitHub:** [@AMorales22T](https://github.com/AMorales22T)
* **Repositorio del Proyecto:** [https://github.com/AMorales22T/mapa_metabolico](https://github.com/AMorales22T/mapa_metabolico)

---

## 📄 Licencia

Este proyecto se distribuye bajo la **Licencia MIT**. Eres libre de usarlo, estudiarlo, modificarlo y compartirlo tanto para fines educativos como de investigación citando la autoría original.
