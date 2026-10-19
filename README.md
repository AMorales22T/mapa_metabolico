```
 __  __                         __  __      _        _           _ _           
|  \/  | __ _ _ __   __ _      |  \/  | ___| |_ __ _| |__   ___ | (_) ___ ___  
| |\/| |/ _` | '_ \ / _` |_____| |\/| |/ _ \ __/ _` | '_ \ / _ \| | |/ __/ _ \ 
| |  | | (_| | |_) | (_| |_____| |  | |  __/ || (_| | |_) | (_) | | | (_| (_) |
|_|  |_|\__,_| .__/ \__,_|     |_|  |_|\___|\__\__,_|_.__/ \___/|_|_|\___\___/ 
             |_|                                                               
```

```
+------------------------------------------------------------------------------+
|                                                                              |
|   Mapa de Metabolismo y su Regulacion  (1200 x 900 mm)                       |
|   Asignatura de Biologia  -  Universidad de Navarra                         |
|   25 vias metabolicas integradas  -  100% SVG nativo  -  GitHub Pages       |
|                                                                              |
+------------------------------------------------------------------------------+
```

[![GitHub Pages](https://img.shields.io/badge/Demo-GitHub%20Pages-0284c7?style=flat&logo=github)](https://amorales22t.github.io/mapa_metabolico/)
[![Licencia](https://img.shields.io/badge/Licencia-CC%20BY--NC--ND%204.0-38bdf8?style=flat)](LICENSE)
[![Vias Integradas](https://img.shields.io/badge/Vias%20Metabolicas-25%20Integradas-10b981?style=flat)](#vias-incluidas-25)
[![SVG Nativo](https://img.shields.io/badge/Motor-100%25%20SVG%20Nativo-f59e0b?style=flat)](#arquitectura-y-motor-tecnico)

> Material didactico para la asignatura *Metabolismo y su regulacion* del Grado en Biologia (Universidad de Navarra). Mapa visual interactivo con veinticinco vias metabolicas integradas, navegacion guiada paso a paso y simuladores de lanzaderas mitocondriales y cadena respiratoria, todo renderizado en SVG nativo sin dependencias externas.

---

## Tabla de Contenidos

- [Introduccion](#introduccion)
- [Demostracion en Vivo](#demostracion-en-vivo)
- [Caracteristicas Principales](#caracteristicas-principales)
- [Guia Rapida de Uso](#guia-rapida-de-uso)
- [Vias Incluidas (25)](#vias-incluidas-25)
- [Contenido y Formatos Disponibles](#contenido-y-formatos-disponibles)
- [Arquitectura y Motor Tecnico](#arquitectura-y-motor-tecnico)
- [Ejecucion Local](#ejecucion-local)
- [Autoria y Licencia](#autoria-y-licencia)

---

## Introduccion

Este proyecto es un trabajo desarrollado para la asignatura de *Metabolismo y su regulacion* dentro del Grado en Biologia de la Universidad de Navarra. Se trata de una aplicacion web autonoma, construida integramente sobre SVG nativo y JavaScript vanilla, que recoge veinticinco vias metabolicas en un unico lienzo vectorial de formato cartel (1200 x 900 mm, pensado tambien para impresion en plotter). El objetivo es ofrecer a los companeros de segundo curso una herramienta de estudio que permita situar cada via en su contexto celular, seguir paso a paso sus reacciones enzimaticas y explorar la regulacion alosterica y hormonal que controla el metabolismo intermediario.

La herramienta se organiza en torno a tres niveles de uso. El primero es una vista panoramica del mapa completo, que permite localizar cada via dentro de su compartimento celular y de su tejido de referencia. El segundo es una navegacion guiada paso a paso que descompone cada reaccion en sus elementos basicos: enzima, numero EC, cofactores, balance termodinamico y mecanismos de regulacion. El tercero agrupa una serie de simuladores que permiten explorar sistemas que en un libro de texto aparecen estaticos, como las lanzaderas mitocondriales de malato-aspartato y glicerol-3-fosfato o la cadena de transporte de electrones con su gradiente quimiosmotico y la rotacion del rotor F0F1 de la ATP sintasa.

| Metrica | Valor |
| :--- | :--- |
| Vias metabolicas integradas | 25 |
| Resolucion del lienzo | 1200 x 900 mm |
| Formato de renderizado | 100% SVG nativo |
| Dependencias externas | 0 (sin frameworks pesados) |
| Frecuencia de animacion | 60 FPS optimizados |
| Despliegue continuo | GitHub Actions a GitHub Pages |
| Licencia | CC BY-NC-ND 4.0 Internacional |

---

## Demostracion en Vivo

[![Demostracion del Mapa Metabolico](capturas_y_pruebas/mapa_metabolico_demo.gif)](https://amorales22t.github.io/mapa_metabolico/)

**Acceso directo en la web:** https://amorales22t.github.io/mapa_metabolico/

La version en linea permite explorar el mapa completo sin necesidad de descarga local. La interfaz funciona en cualquier navegador moderno (Chrome, Firefox, Edge o Safari en sus versiones recientes) y aprovecha la aceleracion hardware del renderizado SVG del navegador, lo que mantiene una frecuencia de actualizacion fluida incluso en dispositivos modestos. El lienzo vectorial no pierde calidad al hacer zoom, lo que resulta especialmente util para inspeccionar estructuras moleculares detalladas o para proyectar el mapa en clase o en el laboratorio sin perdida de nitidez.

---

## Caracteristicas Principales

| Modulo | Descripcion |
| :--- | :--- |
| **Indice lateral de vias** | Panel plegable con las veinticinco rutas metabolicas. Al pulsar sobre una via, la vista se centra suavemente, se atenuan las rutas no seleccionadas y se resaltan sus metabolitos e interconexiones con otras vias. |
| **Navegacion espacial pan-zoom** | Arrastre libre del lienzo y zoom dinamico mediante rueda de raton o gestos tactiles, conservando en todo momento la nitidez vectorial caracteristica del formato SVG. |
| **Modo didactico Paso a Paso** | Inspeccion secuencial de cada reaccion de la via activa, mostrando enzima, codigo EC, cofactores, variacion de energia libre y mecanismos de regulacion alosterica y hormonal. |
| **Simulador de Lanzaderas Mitocondriales** | Al pulsar sobre las lupas de la Cadena de Transporte de Electrones o de las lanzaderas, se activa un monitor especializado por fases (Complejos I-IV, ATP sintasa, malato-aspartato, glicerol-3-fosfato y carnitina). |
| **Estados metabolicos fisiologicos** | Conmutacion instantanea entre estado normal, posprandial (insulina alta, glucagon bajo) y ayuno (glucagon alto, insulina baja), con resaltado dinamico de las vias activas en cada contexto. |
| **Flujo biologico animado** | Particulas bioluminiscentes con motor de animacion SMIL (`<animateMotion>`) y flujos CSS de bajo impacto, pausadas por defecto para optimizar el rendimiento y activables a voluntad. |

---

## Guia Rapida de Uso

Para sacar provecho del mapa, conviene familiarizarse con los controles principales descritos a continuacion. Cada uno de ellos esta accesible desde la barra superior o desde los botones flotantes del lienzo.

1. **Indice lateral de vias.** Pulsa el boton **Vias (25)** situado en la barra superior para desplegar el panel con la lista completa de rutas metabolicas. Al hacer clic en una ruta, la vista se centra suavemente sobre ella y se atenuan el resto. Un buscador interno permite filtrar por nombre (por ejemplo, Krebs, Lipolisis o Kennedy).
2. **Navegacion espacial.** Arrastra el lienzo con el puntero para desplazarte libremente por el mapa. Utiliza la rueda del raton o los gestos tactiles para hacer zoom in o zoom out sin perdida de resolucion vectorial. Los botones de la barra superior permiten ajustar el zoom a un valor concreto, restablecer la vista o ajustar a pantalla.
3. **Modo Paso a Paso.** Activa el boton **Paso a Paso** para iniciar la navegacion guiada. El panel inferior mostrara secuencialmente cada reaccion de la via activa con su ecuacion quimica, enzima, cofactores y regulacion. Las flechas del panel permiten avanzar o retroceder en la secuencia.
4. **Cadena Respiratoria y Lanzaderas.** Situate sobre las lupas marcadas como CTE o Lanzaderas y pulsa para abrir el simulador especializado. En el caso de la cadena respiratoria se accede a un monitor por fases con los Complejos I-IV y la ATP sintasa. En las lanzaderas, un monitor especifico muestra malato-aspartato, glicerol-3-fosfato o carnitina segun el caso.
5. **Estados metabolicos.** Utiliza los botones Normal / Posprandial / Ayuno para visualizar como cambia el patron de actividad metabolica en funcion del contexto hormonal. El rastreo visual de los flujos activos facilita la comprension integrada del metabolismo intertisular.
6. **Flujo biologico.** Las particulas bioluminiscentes estan pausadas por defecto para optimizar el rendimiento en sesiones largas. Activalas con el boton **Flujo Animado** cuando desees visualizar dinamicamente el sentido de las reacciones y el transporte de equivalentes reducidos.
7. **Acceso directo por URL.** Puedes enlazar a una ruta concreta añadiendo el parametro `?via=N` a la URL, donde N va de 1 a 25. Esto resulta especialmente util para compartir una via concreta en foros academicos, aulas virtuales o presentaciones.

---

## Vias Incluidas (25)

Las veinticinco vias metabolicas se organizan en siete bloques tematicos, siguiendo la estructura pedagogica clasica del metabolismo intermediario. Cada via conserva su numeracion original y es accesible de forma individual tanto desde el indice lateral como desde el selector rapido de la barra superior o por parametro URL.

### Bloque I. Carbohidratos

| # | Via | Compartimento | Puntos clave |
| :---: | :--- | :--- | :--- |
| 1 | Glucolisis | Citosol | Hexocinasa, PFK-1, Piruvato quinasa, regulacion alosterica y hormonal |
| 2 | Gluconeogenesis | Matriz / Citosol / RE | Tres rodeos enzimaticos (PC, PEPCK, FBPasa-1, G6Pasa) |
| 3 | Glucogenogenesis / Glucogenolisis | Citosol | Glucogeno sintasa y glucogeno fosforilasa, fosforilacion reversible |
| 4 | Via de las Pentosas Fosfato | Citosol | Fase oxidativa (G6PDH), fase no oxidativa (TK, TA), NADPH y ribosa-5-P |

### Bloque II. Respiracion y Bioenergetica

| # | Via | Compartimento | Puntos clave |
| :---: | :--- | :--- | :--- |
| 5 | Complejo Piruvato Deshidrogenasa (PDH) | Matriz mitocondrial | Descarboxilacion oxidativa, cinco cofactores (TPP, lipoamida, CoA, FAD, NAD+), regulacion por PDK/PDP |
| 6 | Ciclo de Krebs | Matriz mitocondrial | Ocho pasos, tres NADH, un FADH2, un GTP, dos CO2 por vuelta |
| 7 | Cadena Respiratoria y ATP Sintasa | Membrana mitocondrial interna | Complejos I-IV, CoQ, citocromo c, F0F1, gradiente quimiosmotico de Mitchell |

### Bloque III. Lanzaderas Redox Mitocondriales

| # | Via | Compartimento | Puntos clave |
| :---: | :--- | :--- | :--- |
| 8 | Lanzadera Malato-Aspartato | Membrana mitocondrial interna | Transportadores OGC y AGC (Aralar), transferencia citosol-matriz de equivalentes |
| 8B | Lanzadera Glicerol-3-Fosfato | MME / MMI | g3pDH citosolica y mitocondrial, transferencia de electrones a CoQ via FAD |
| 9 | Lanzadera de Carnitina | MME y MMI | CPT-1 (limitante, inhibida por malonil-CoA), CACT (antipuerto), CPT-2 |

### Bloque IV. Lipidos

| # | Via | Compartimento | Puntos clave |
| :---: | :--- | :--- | :--- |
| 9 | Beta-Oxidacion de acidos grasos | Matriz mitocondrial | Cuatro pasos (deshidrogenacion, hidratacion, deshidrogenacion, tiolisis), rendimientos energeticamente relevantes |
| 10 | Lipogenesis de novo | Citosol | ATP citrato liasa, ACC, FAS (siete ciclos condensacion-reduccion), palmitato final |
| 11 | Cetogenesis / Cetolisis | Matriz hepatica / Citosol extrahepatico | HMG-CoA sintasa mitocondrial, HMG-CoA liasa, acetoacetato y beta-hidroxibutirato |
| 12 | Biosintesis de Colesterol | Reticulo endoplasmico | Via del mevalonato, HMG-CoA reductasa (limitante, diana de estatinas), Bloch y Kandutsch |

### Bloque V. Nitrogeno y Aminoacidos

| # | Via | Compartimento | Puntos clave |
| :---: | :--- | :--- | :--- |
| 12B | Via de Transulfuracion (CTH) | Citosol | Cistationina beta-sintasa y cistationina gamma-liasa, destino del carbon esqueletico |
| 13 | Transaminacion y Ciclo Glucosa-Alanina | Citosol / Sangre | ALT, AST, ciclo glucosa-alanina (Cahill), transportador de nitrogeno muscular |
| 14 | Ciclo de la Urea | Mitochondria / Citosol hepatico | Biciclo Krebs-Henseleit, cinco enzimas, dos compartimentos, excrecion nitrogenada |

### Bloque VI. Nucleotidos

| # | Via | Compartimento | Puntos clave |
| :---: | :--- | :--- | :--- |
| 15 | Biosintesis de Purinas y Pirimidinas | Citosol | Sintesis de novo y de salvamento, PRPP como donador, regulacion alosterica |
| 16 | Catabolismo de Nucleotidos | Citosol / Renal | Degradacion de purinas a acido urico, transportador URAT1, diana farmacologica en gota |

### Bloque VII. Integracion Tisular e Interorganos

| # | Via | Compartimento | Puntos clave |
| :---: | :--- | :--- | :--- |
| 17 | Ciclo de Cori y Ciclo de Cahill | Vascular | Acoplamiento musculo-higado y adipocito-higado durante el ayuno |
| 18 | Digestion y Absorcion de Lipidos | Enterocito | Quilomicrones, enterocito, transporte linfatico |
| 19 | Lipolisis Adipocitaria | Adipocito | ATGL, HSL y MGL, regulacion hormonal por insulina y catecolaminas |
| 20 | Musculo Esqueletico y Sarcomero | Sarcomero | GLUT-4 insulina-dependiente, fosfagenos, tipos de fibra |
| 21 | Cerebro y Barrera Hematoencefalica | Endotelio capilar / Neurona | BHE, cetolisis neuronal, dependencia glucosada fisiologica |
| 22 | Metabolismo de Lipoproteinas | Plasma | VLDL, LDL, HDL, LPL, LCAT, receptores hepaticos |
| 23 | Via de Kennedy | Reticulo endoplasmico | Sintesis de fosfolipidos de membrana, CDP-colina y CDP-etanolamina |
| 24 | Biosintesis de Aminoacidos No Esenciales | Citosol | Transaminacion, reacciones de un carbon (folato, B12) |
| 25 | Conmutador Hormonal Pancreatico | Celulas beta y alfa | Insulina, glucagon, amilina, regulacion integrada |

---

## Contenido y Formatos Disponibles

El repositorio ofrece el mapa en varios formatos complementarios, cada uno pensado para un caso de uso distinto (estudio personal, sesion en clase, impresion o modificacion del codigo). La siguiente tabla resume los recursos disponibles y su ubicacion dentro del repositorio.

| Recurso | Descripcion | Ubicacion |
| :--- | :--- | :--- |
| **Mapa Interactivo (Portal)** | Aplicacion web completa y autonoma con motor SVG y JavaScript vanilla | [`index.html`](index.html) |
| **Mapa Alternativo (Entregables)** | Version vectorial con flujo animado continuo y visualizacion limpia | [`mapa_metabolico_alternativo/`](mapa_metabolico_alternativo/) |
| **Mapa Base (Cartulina)** | Diagrama maestro ampliado completo con las 25 vias | [`versiones_html/01_mapa_ampliado_completo_25_vias.html`](versiones_html/01_mapa_ampliado_completo_25_vias.html) |
| **Ampliacion Rutas 18-25** | Vista aislada de vias intertisulares y de integracion | [`versiones_html/02_ampliacion_rutas_18_25.html`](versiones_html/02_ampliacion_rutas_18_25.html) |
| **Poster de Impresion (PDF)** | Formato poster gigante listo para imprenta (1200 x 900 mm) | [`versiones_impresion/`](versiones_impresion/) |
| **Vias Individuales (SVG)** | Diagramas vectoriales modulares clasificados por bloque | [`01_CARBOHIDRATOS/`](01_CARBOHIDRATOS/) a [`05_NUCLEOTIDOS_Y_OTRAS/`](05_NUCLEOTIDOS_Y_OTRAS/) |

---

## Arquitectura y Motor Tecnico

El proyecto se ha concebido como una aplicacion ligera y autosuficiente, sin dependencias de frameworks externos. Toda la interactividad se implementa en JavaScript vanilla y todo el renderizado se apoya en el formato SVG nativo del navegador, lo que garantiza escalabilidad vectorial sin perdida de calidad, independencia de plugins y un consumo minimo de recursos. Esta decision permite que el codigo fuente sea legible y modificable tambien por companeros sin experiencia previa en frameworks web.

```
+--------------------------------------------------------------------------+
|                        ARQUITECTURA DEL MAPA                            |
+--------------------------------------------------------------------------+
|                                                                          |
|   [ NAVEGADOR ]                                                          |
|        |                                                                 |
|        v                                                                 |
|   +-------------------+        +-------------------+                     |
|   |   index.html      |  <-->  |  SVG Nativo       |                    |
|   |   (estructura)    |        |  (lienzo 7320 px) |                    |
|   +-------------------+        +-------------------+                     |
|        |                          ^                                     |
|        v                          |                                     |
|   +-------------------+        +-------------------+                    |
|   |  Motor JS Vanilla |  --->  |  SMIL + CSS       |                    |
|   |  (pan, zoom,        |       |  (animaciones      |                   |
|   |   step, sidebar)   |       |   bioluminiscentes)|                   |
|   +-------------------+        +-------------------+                    |
|        |                                                                 |
|        v                                                                 |
|   +-------------------+                                                  |
|   |  GitHub Actions   |  -->  push a rama main  -->  GitHub Pages       |
|   |  deploy.yml       |                        despliegue automatico     |
|   +-------------------+                                                  |
|                                                                          |
+--------------------------------------------------------------------------+
```

Los principios arquitectonicos clave son tres. En primer lugar, el uso exclusivo de SVG nativo permite que el lienzo se renderice como un arbol DOM manipulable directamente desde JavaScript, evitando el coste de un canvas raster o de un motor WebGL. En segundo lugar, las micro-animaciones se declaran mediante `<animateMotion>` de SMIL y transiciones CSS de bajo impacto, lo que permite mantener una frecuencia estable de 60 FPS sin sacrificar la legibilidad del codigo fuente. En tercer lugar, el despliegue continuo se automatiza mediante GitHub Actions: cada push a la rama `main` dispara el flujo de trabajo definido en `.github/workflows/deploy.yml` y publica la nueva version en GitHub Pages en cuestion de segundos.

---

## Ejecucion Local

Para visualizar el mapa localmente en cualquier navegador, basta con servir el contenido del repositorio mediante un servidor HTTP estatico. La siguiente instruccion utiliza el modulo integrado de Python 3, que no requiere instalacion adicional:

```bash
# Servir desde la raiz del repositorio
python3 -m http.server 8000
```

Una vez ejecutado, abre tu navegador en `http://localhost:8000/`. El mapa se cargara integramente desde tu maquina, sin dependencia de conexion externa. Esta opcion resulta util para sesiones en clase sin acceso a internet o para revisar y modificar el codigo fuente en tiempo real durante el desarrollo.

Alternativamente, puede emplearse cualquier otro servidor HTTP estatico equivalente, como `npx serve`, `php -S localhost:8000` o una extension de servidor local del propio navegador. La unica condicion tecnica es que los archivos se sirvan bajo el mismo origen, dado que el navegador impone restricciones a la carga de SVG como archivo (`file://`) por razones de seguridad del modelo CORS.

---

## Autoria y Licencia

**Autor:** [AMorales22T](https://github.com/AMorales22T) - Estudiante de Grado en Biologia, Universidad de Navarra. Repositorio: [AMorales22T/mapa_metabolico](https://github.com/AMorales22T/mapa_metabolico)

**Asignatura:** Metabolismo y su regulacion (segundo curso del Grado en Biologia).

**Agradecimientos:** Al profesorado de la asignatura por la orientacion bibliografica y por la sugerencia de integrar en un unico mapa las vias vistas de forma aislada a lo largo del curso.

Este proyecto se distribuye bajo la licencia **Creative Commons Atribucion-NoComercial-SinDerivadas 4.0 Internacional (CC BY-NC-ND 4.0)**. La licencia completa puede consultarse en https://creativecommons.org/licenses/by-nc-nd/4.0/.

**Se permite** compartir, visualizar y utilizar este material con fines academicos y de estudio personal, conservando siempre la atribucion original al autor y el enlace al repositorio oficial. Esto incluye su proyeccion en aulas, su inclusion en plataformas educativas no comerciales y su uso como material de referencia en trabajos de investigacion.

**No comercial.** No esta permitido el uso comercial del material ni su venta en ninguna plataforma, ni siquiera de forma modificada o integrada en productos de pago. Cualquier uso que genere ingresos directos o indirectos requiere autorizacion expresa y previa del autor.

**Sin obras derivadas.** No se autoriza la redistribucion de versiones modificadas, adaptadas o desprovistas del credito original de autoria. Las traducciones, adaptaciones a otros idiomas o reorganizaciones sustanciales del contenido requieren permiso explicito del autor.

---

```
+--------------------------------------------------------------------------+
|                                                                          |
|   © AMorales22T  -  Mapa de Metabolismo y su Regulacion                  |
|   Grado en Biologia  -  Universidad de Navarra                           |
|   Licencia: CC BY-NC-ND 4.0  -  https://github.com/AMorales22T           |
|                                                                          |
+--------------------------------------------------------------------------+
```
