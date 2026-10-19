```
 __  __                         __  __      _        _           _ _           
|  \/  | __ _ _ __   __ _      |  \/  | ___| |_ __ _| |__   ___ | (_) ___ ___  
| |\/| |/ _` | '_ \ / _` |_____| |\/| |/ _ \ __/ _` | '_ \ / _ \| | |/ __/ _ \ 
| |  | | (_| | |_) | (_| |_____| |  | |  __/ || (_| | |_) | (_) | | | (_| (_) |
|_|  |_|\__,_| .__/ \__,_|     |_|  |_|\___|\__\__,_|_.__/ \___/|_|_|\___\___/ 
             |_|                                                               
```

# Atlas Metabolico Interactivo y Vectorial (1200 x 900 mm)

[![GitHub Pages](https://img.shields.io/badge/Demo-GitHub%20Pages-0284c7?style=flat&logo=github)](https://amorales22t.github.io/mapa_metabolico/)
[![Licencia](https://img.shields.io/badge/Licencia-CC%20BY--NC--ND%204.0-38bdf8?style=flat)](LICENSE)
[![Rutas Integradas](https://img.shields.io/badge/Vias%20Metabolicas-25%20Integradas-10b981?style=flat)](#vias-incluidas-25)
[![SVG Nativo](https://img.shields.io/badge/Motor-100%25%20SVG%20Nativo-f59e0b?style=flat)](#motor-y-arquitectura)

> Plataforma didactica y atlas visual interactivo de bioquimica con 25 vias integradas, navegacion guiada paso a paso, simuladores de lanzaderas mitocondriales y cadena respiratoria.

---

## Demostracion en Vivo

[![Demostracion del Mapa Metabolico](capturas_y_pruebas/mapa_metabolico_demo.gif)](https://amorales22t.github.io/mapa_metabolico/)

**Acceso directo en la web:** [https://amorales22t.github.io/mapa_metabolico/](https://amorales22t.github.io/mapa_metabolico/)

---

## Guia Rapida de Uso

- **Indice lateral de vias:** pulsa en el boton **Indice** para desplegar las 25 rutas metabolicas. Al hacer clic en una ruta, la vista se centra suavemente y resalta sus metabolitos e interconexiones.
- **Navegacion espacial:** arrastra libremente el lienzo (pan) y utiliza la rueda del raton o gestos para zoom dinamico sin perdida de resolucion vectorial.
- **Modo didactico Paso a Paso:** haz clic en **Paso a Paso** para inspeccionar secuencialmente cada reaccion de la via activa, visualizando enzimas (codigo EC), cofactores, Delta G y mecanismos de regulacion.
- **Cadena Respiratoria y Lanzaderas:** al pulsar sobre la lupa de la *Cadena de Transporte de Electrones* o de las *Lanzaderas Mitocondriales*, se activa un monitor especializado por fases (Complejos I-IV, ATP sintasa, malato-aspartato, glicerol-3-fosfato y carnitina).
- **Flujo biologico:** las particulas bioluminiscentes se encuentran pausadas por defecto para optimizar el rendimiento. Puedes activarlas pulsando **Flujo Animado**.
- **Acceso directo por URL:** anade `?via=1` hasta `?via=25` a la URL para enlazar o compartir directamente una ruta especifica.

---

## Contenido y Formatos Disponibles

| Recurso | Descripcion | Ubicacion |
| :--- | :--- | :--- |
| **Mapa Interactivo (Portal)** | Aplicacion web completa y autonoma (SVG + motor JS) | [`index.html`](index.html) |
| **Mapa Alternativo (Entregables)** | Version vectorial con flujo y visualizacion limpia | [`mapa_metabolico_alternativo/`](mapa_metabolico_alternativo/) |
| **Mapa Base (Cartulina)** | Diagrama maestro ampliado completo con las 25 vias | [`versiones_html/01_mapa_ampliado_completo_25_vias.html`](versiones_html/01_mapa_ampliado_completo_25_vias.html) |
| **Ampliacion Rutas 18-25** | Vista aislada de vias intertisulares y de integracion | [`versiones_html/02_ampliacion_rutas_18_25.html`](versiones_html/02_ampliacion_rutas_18_25.html) |
| **Poster de Impresion (PDF)** | Formato poster gigante listo para imprenta (1200 x 900 mm) | [`versiones_impresion/`](versiones_impresion/) |
| **Vias Individuales (SVG)** | Diagramas vectoriales modulares clasificados por bloque | [`01_CARBOHIDRATOS/`](01_CARBOHIDRATOS/) a [`05_NUCLEOTIDOS_Y_OTRAS/`](05_NUCLEOTIDOS_Y_OTRAS/) |

---

## Vias Incluidas (25)

1. **Carbohidratos:** Glucolisis, Gluconeogenesis, Glucogenogenesis/Glucogenolisis, Via de las Pentosas Fosfato y Ciclo de Cori.
2. **Respiracion y Bioenergetica:** Complejo Piruvato Deshidrogenasa (PDH), Ciclo de Krebs y Cadena de Transporte de Electrones con ATP sintasa.
3. **Lanzaderas Redox Mitocondriales:** Lanzadera de Malato-Aspartato, Glicerol-3-Fosfato y Lanzadera de Carnitina.
4. **Lipidos:** Beta-Oxidacion de acidos grasos, Lipogenesis *de novo*, Cetogenesis/Cetolisis y Sintesis de Colesterol.
5. **Nitrogeno y Aminoacidos:** Ciclo de la Urea, Transaminacion/Desaminacion oxidativa y Via de Transulfuracion (CTH).
6. **Nucleotidos:** Sintesis *de novo* de Purinas y Pirimidinas, Degradacion de Purinas y transportador URAT1.
7. **Integracion Tisular e Interorganos:** Ciclo glucosa-alanina (Cahill), regulacion en adipocito y sarcomero, barrera hematoencefalica (BHE), metabolismo de lipoproteinas (VLDL/LDL/HDL) y via de Kennedy.

---

## Motor y Arquitectura

- **100% SVG nativo:** renderizado vectorial escalable sin dependencias de frameworks externos pesados.
- **Micro-animaciones declarativas:** particulas SMIL (`<animateMotion>`) y flujos CSS de bajo impacto.
- **Integracion continua:** despliegue automatizado a GitHub Pages mediante GitHub Actions ([`.github/workflows/deploy.yml`](.github/workflows/deploy.yml)) con cada push a la rama `main`.

---

## Ejecucion Local

Para visualizar el mapa localmente en cualquier navegador:

```bash
# Servir desde la raiz del repositorio
python3 -m http.server 8000
```
Luego abre tu navegador en `http://localhost:8000/`.

---

## Autoria y Licencia

**Autor:** [AMorales22T](https://github.com/AMorales22T) - Repositorio oficial: [AMorales22T/mapa_metabolico](https://github.com/AMorales22T/mapa_metabolico)

Este proyecto se distribuye bajo la licencia **[Creative Commons Atribucion-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0)](https://creativecommons.org/licenses/by-nc-nd/4.0/)**.

- **Se permite:** compartir, visualizar y utilizar este material con fines academicos y de estudio personal, conservando siempre la atribucion original al autor y el enlace al repositorio oficial.
- **No comercial:** no esta permitido su uso comercial ni su venta en ninguna plataforma.
- **Sin obras derivadas:** no se autoriza la redistribucion de versiones modificadas, adaptadas o desprovistas del credito original de autoria.
