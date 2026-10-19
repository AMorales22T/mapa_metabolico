```
 __  __                         __  __      _        _           _ _           
|  \/  | __ _ _ __   __ _      |  \/  | ___| |_ __ _| |__   ___ | (_) ___ ___  
| |\/| |/ _` | '_ \ / _` |_____| |\/| |/ _ \ __/ _` | '_ \ / _ \| | |/ __/ _ \ 
| |  | | (_| | |_) | (_| |_____| |  | |  __/ || (_| | |_) | (_) | | | (_| (_) |
|_|  |_|\__,_| .__/ \__,_|     |_|  |_|\___|\__\__,_|_.__/ \___/|_|_|\___\___/ 
             |_|                                                               
```

> Atlas metabolico interactivo y vectorial (1200 x 900 mm). 25 vias integradas.

**Demo en linea:** https://amorales22t.github.io/mapa_metabolico/

(c) 2026 AMorales22T. Licencia **CC BY-NC-ND 4.0** (ver [Autoria y licencia](#autoria-y-licencia)).

================================================================================
USO RAPIDO
================================================================================

* **Indice de vias** (panel lateral): lista las 25 vias; pulsa una para resaltarla
  y centrar la camara. Tambien hay un selector desplegable en la barra superior.
* **Navegacion:** arrastra para mover, rueda del raton para zoom.
* **Flujo animado:** las "bolitas" que recorren las flechas arrancan **pausadas**
  (mejora el rendimiento). Pulsa el boton "Flujo: Pausado" para activarlas.
* **Paso a paso:** recorre las reacciones de la via seleccionada con panel de
  detalle (enzima, cofactores, deltaG, regulacion). Boton "Camara" para
  activar/desactivar el centrado automatico.
* **Cadena respiratoria y lanzaderas:** al pulsar su lupa se abre un monitor de
  fases (Complejos I-IV, ATP sintasa; lanzaderas malato-aspartato,
  glicerol-3-fosfato y carnitina).
* **Enlace directo a una via:** `?via=1` ... `?via=25` en la URL.

================================================================================
CONTENIDO Y FORMATOS
================================================================================

+----------------------------+-------------------------------------------------+
| Recurso                    | Enlace / Ubicacion                              |
+----------------------------+-------------------------------------------------+
| Mapa interactivo (portal)  | index.html (SVG + JS en un unico archivo)       |
| Mapa Alternativo (entregab)| mapa_metabolico_alternativo/ (SVG, HTML, PDF)   |
| Mapa Original (Base)       | versiones_html/01_mapa_ampliado_completo_25_vias|
| Standalone Vias 18-25      | versiones_html/02_ampliacion_rutas_18_25.html   |
| Cuadro Temario Bloques A-E | versiones_html/04_cuadro_temario_bloques_A_E.htm|
| PDF Poster                 | versiones_impresion/ (120 x 90 cm)              |
| SVG individual por via     | 01_ ... 05_ (carpetas tematicas)                |
+----------------------------+-------------------------------------------------+

================================================================================
VIAS INCLUIDAS (25)
================================================================================

* Carbohidratos: Glucolisis, Gluconeogenesis, Glucogeno, Pentosas Fosfato.
* Respiracion: Complejo PDH, Ciclo de Krebs, Cadena de Transporte de Electrones.
* Lanzaderas Redox: Malato-Aspartato, Glicerol-3-Fosfato, Carnitina.
* Lipidos: Beta-Oxidacion, Lipogenesis de Novo, Cetogenesis, Colesterol.
* Nitrogeno y AA: Ciclo de la Urea, Transaminacion, Transulfuracion (CTH).
* Nucleotidos: Sintesis Purinas/Pirimidinas, Degradacion y URAT1.
* Intertisular: Ciclo de Cori/Cahill, Digestion, Adipocito, Sarcomero, BHE,
  Lipoproteinas (VLDL/LDL/HDL), Via de Kennedy, AA no esenciales, Hormonas.

================================================================================
MOTOR VECTORIAL
================================================================================

* 100% SVG nativo, sin dependencias externas pesadas.
* Particulas de flujo con animaciones SMIL (`<animateMotion>`) y CSS.
* Despliegue automatico a GitHub Pages con GitHub Actions
  (`.github/workflows/deploy.yml`) en cada push a `main`.

================================================================================
ESTRUCTURA DEL REPOSITORIO
================================================================================

.
|-- index.html                              # Portal GitHub Pages (mapa interactivo)
|-- mapa_metabolico_alternativo/            # Entregables alternativos (SVG, HTML, PDF, PNG)
|-- versiones_html/                         # Visores HTML interactivos
|-- versiones_impresion/                    # Archivos PDF para impresion (1200 x 900 mm)
|-- scripts_generacion/                     # Generadores y detector de solapamientos
|-- 00 a 07/                                # Modulos bioquimicos y mapa base original
|-- LICENSE                                 # CC BY-NC-ND 4.0
`-- AUDITORIA_INTEGRAL_MAPA_METABOLICO.txt  # Reporte de trazabilidad

================================================================================
EJECUCION LOCAL
================================================================================

Ver el mapa interactivo:
  python3 -m http.server 8000     # y abrir http://localhost:8000/

Generar mapa alternativo (SVG, HTML, PDF, PNG):
  python3 mapa_metabolico_alternativo/generar_mapa_alternativo.py

Verificar colisiones geometricas:
  python3 scripts_generacion/detectar_solapamientos.py mapa_metabolico_alternativo/mapa_metabolico_alternativo.svg

================================================================================
AUTORIA Y LICENCIA
================================================================================

Autor: **AMorales22T** - https://github.com/AMorales22T/mapa_metabolico

Este trabajo se publica bajo
[Creative Commons Atribucion-NoComercial-SinDerivadas 4.0 Internacional
(CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/).

* **Puedes** compartirlo y usarlo para estudiar, siempre dando credito al autor
  y enlazando a este repositorio.
* **No puedes** usarlo con fines comerciales.
* **No puedes** publicar versiones modificadas o derivadas (incluidas copias
  con otro nombre o con la autoria eliminada) sin permiso escrito del autor.

Si encuentras una copia sin atribucion, abre un issue en este repositorio.
