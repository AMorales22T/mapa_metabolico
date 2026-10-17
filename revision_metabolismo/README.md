# 🧭 Guía de Revisión Modular del Código (`revision_metabolismo`)

Esta carpeta contiene **todo el código del proyecto desglosado en archivos pequeños, temáticos y numerados**, sin tocar absolutamente nada del proyecto original.

Los archivos gigantescos del proyecto original (como `generar_prueba_visual_integrada.py` de **4.188 líneas** o `interactividad_html.py` de **1.638 líneas**) se han dividido aquí bloque por bloque (entre 40 y 300 líneas cada uno). Cada archivo incluye en su cabecera de qué archivo y rango de líneas original proviene.

---

## 📂 Mapa de las 7 Subcarpetas Principales

| # | Subcarpeta | ¿Qué contiene? | ¿Cómo estaba antes? |
| :-: | :--- | :--- | :--- |
| **01** | [`01_rutas_individuales/`](01_rutas_individuales/) | Las **17 vías originales** separadas por familia bioquímica (`entorno`, `estructuras` y `generador`). Las rutas densas como Gluconeogénesis, Pentosas y Carbohidratos Integrados están divididas en partes. | Repartido en múltiples carpetas con generadores de hasta 1.260 líneas. |
| **02** | [`02_mapa_central_integrado/`](02_mapa_central_integrado/) | El **hepatocito central de 17 vías** dividido en **25 archivos numerados** (`00` a `24`): uno por cada vía metabólica, organelo, lupa y leyenda. | Un único archivo monolítico de **4.188 líneas** (`generar_prueba_visual_integrada.py`). |
| **03** | [`03_ampliacion_vias_18_a_25/`](03_ampliacion_vias_18_a_25/) | Las **bandas laterales de ampliación (vías 18 a 25)** divididas en 4 subcarpetas: estructuras visuales, banda izquierda (órganos), banda derecha (biosíntesis) y calibración/auditoría. | Mezclado en `generar_ampliacion.py` (925 líneas) y `estructuras_ampliacion.py` (611 líneas). |
| **04** | [`04_algoritmos_trazado_y_validacion/`](04_algoritmos_trazado_y_validacion/) | Los **2 motores algorítmicos** divididos paso a paso: el enrutador **A\*** de 45 conexiones (`01_conector_rutas_astar/`) y el **detector de solapamientos** (`02_detector_solapamientos/`). | 2 scripts densos de 851 y 553 líneas. |
| **05** | [`05_datos_bioquimicos_y_regulacion/`](05_datos_bioquimicos_y_regulacion/) | **Estequiometría, $\Delta G^{\circ\prime}$, números EC y regulación alostérica/hormonal** divididos en 5 bloques temáticos (A–E). | Un diccionario gigante de casi 1.000 líneas (`reacciones_estequiometria.py`). |
| **06** | [`06_motor_interactividad_web/`](06_motor_interactividad_web/) | El **visor interactivo web** separado limpiamente en sus lenguajes reales: `.css` (estilos), `.html` (controles DOM) y 5 módulos `.js` (cámara CTM, buscador, tooltips, estados). | Todo incrustado como texto dentro de un string de Python de **1.638 líneas** (`interactividad_html.py`). |
| **07** | [`07_exportacion_imprenta_y_utilidades/`](07_exportacion_imprenta_y_utilidades/) | Herramientas de exportación a **PDF de gran formato (120 × 90 cm)**, blueprints de Excalidraw y capturas. | Mezclado en `scripts_generacion/`. |

---

## 🔍 Índice Detallado por Subcarpeta

### 1️⃣ [`01_rutas_individuales/`](01_rutas_individuales/) — Vías por Familia Bioquímica
* **[`01_carbohidratos/`](01_rutas_individuales/01_carbohidratos/)**
  * [`via_01_glucolisis/`](01_rutas_individuales/01_carbohidratos/via_01_glucolisis/) — Entorno, estructuras 2D y los 10 pasos glucolíticos.
  * [`via_02_gluconeogenesis/`](01_rutas_individuales/01_carbohidratos/via_02_gluconeogenesis/) — Dividida en 4 archivos: estructuras, entorno, tramo citosólico (Rodeos 2 y 3) y matriz mitocondrial (Rodeo 1: PC y PEPCK).
  * [`via_03_glucogeno/`](01_rutas_individuales/01_carbohidratos/via_03_glucogeno/) — Glucogenina, glucógeno sintasa y fosforilasa.
  * [`via_04_pentosas_fosfato/`](01_rutas_individuales/01_carbohidratos/via_04_pentosas_fosfato/) — Dividida en estructuras, fase oxidativa (NADPH) y fase no oxidativa (transcetolasa/transaldolasa).
  * [`via_17_ciclo_de_cori/`](01_rutas_individuales/01_carbohidratos/via_17_ciclo_de_cori/) — Ciclo lactato-glucosa entre músculo e hígado.
  * [`carbohidratos_integrados/`](01_rutas_individuales/01_carbohidratos/carbohidratos_integrados/) — Unión de carbohidratos dividida en 5 archivos.
* **[`02_respiracion_y_energia/`](01_rutas_individuales/02_respiracion_y_energia/)**
  * [`via_05_complejo_pdh/`](01_rutas_individuales/02_respiracion_y_energia/via_05_complejo_pdh/) — E1, E2, E3 y los 5 cofactores (TPP, lipoamida, CoA, FAD, NAD⁺).
  * [`via_06_ciclo_de_krebs/`](01_rutas_individuales/02_respiracion_y_energia/via_06_ciclo_de_krebs/) — Matriz mitocondrial, estructuras y anillo de 8 pasos.
  * [`via_07_cadena_respiratoria/`](01_rutas_individuales/02_respiracion_y_energia/via_07_cadena_respiratoria/) — Complejos I–IV, gradiente de H⁺ y ATP sintasa.
  * [`via_08_lanzaderas_redox/`](01_rutas_individuales/02_respiracion_y_energia/via_08_lanzaderas_redox/) — Lanzadera Malato-Aspartato y Lanzadera Glicerol-3-Fosfato.
* **[`03_lipidos/`](01_rutas_individuales/03_lipidos/)**
  * [`via_09_beta_oxidacion/`](01_rutas_individuales/03_lipidos/via_09_beta_oxidacion/), [`via_10_lipogenesis/`](01_rutas_individuales/03_lipidos/via_10_lipogenesis/), [`via_11_cetogenesis_y_cetolisis/`](01_rutas_individuales/03_lipidos/via_11_cetogenesis_y_cetolisis/), [`via_12_colesterol/`](01_rutas_individuales/03_lipidos/via_12_colesterol/).
* **[`04_nitrogeno_y_aminoacidos/`](01_rutas_individuales/04_nitrogeno_y_aminoacidos/)**
  * [`via_12b_esqueletos_carbonados/`](01_rutas_individuales/04_nitrogeno_y_aminoacidos/via_12b_esqueletos_carbonados/), [`via_13_transaminacion_y_desaminacion/`](01_rutas_individuales/04_nitrogeno_y_aminoacidos/via_13_transaminacion_y_desaminacion/), [`via_14_ciclo_de_la_urea/`](01_rutas_individuales/04_nitrogeno_y_aminoacidos/via_14_ciclo_de_la_urea/).
* **[`05_nucleotidos/`](01_rutas_individuales/05_nucleotidos/)**
  * [`via_15_sintesis_purinas_pirimidinas/`](01_rutas_individuales/05_nucleotidos/via_15_sintesis_purinas_pirimidinas/) y [`via_16_degradacion_y_acido_urico/`](01_rutas_individuales/05_nucleotidos/via_16_degradacion_y_acido_urico/).

---

### 2️⃣ [`02_mapa_central_integrado/`](02_mapa_central_integrado/) — El Lienzo Central en 25 Partes
Desglose secuencial de `generar_prueba_visual_integrada.py`:
* **Base y Helpers:** [`00_imports_y_configuracion.py`](02_mapa_central_integrado/00_imports_y_configuracion.py), [`01_helpers_nodos_y_reacciones.py`](02_mapa_central_integrado/01_helpers_nodos_y_reacciones.py), [`02_leyenda_y_autoria_funciones.py`](02_mapa_central_integrado/02_leyenda_y_autoria_funciones.py).
* ** Ultraestructura Celular:** [`03_ciclo_de_cori_y_musculo_funcion.py`](02_mapa_central_integrado/03_ciclo_de_cori_y_musculo_funcion.py), [`04_entorno_celular_y_vascular.py`](02_mapa_central_integrado/04_entorno_celular_y_vascular.py), [`05_gran_mitocondria_biologica.py`](02_mapa_central_integrado/05_gran_mitocondria_biologica.py).
* **Carbohidratos en el Lienzo:** [`06_eje_central_glucolisis.py`](02_mapa_central_integrado/06_eje_central_glucolisis.py), [`07_via_gluconeogenesis_rodeos.py`](02_mapa_central_integrado/07_via_gluconeogenesis_rodeos.py), [`08_metabolismo_del_glucogeno.py`](02_mapa_central_integrado/08_metabolismo_del_glucogeno.py), [`09_via_pentosas_fosfato.py`](02_mapa_central_integrado/09_via_pentosas_fosfato.py).
* **Mitocondria y Respiración:** [`10_lupa_lanzadera_malato_aspartato.py`](02_mapa_central_integrado/10_lupa_lanzadera_malato_aspartato.py), [`11_matriz_ciclo_de_krebs.py`](02_mapa_central_integrado/11_matriz_ciclo_de_krebs.py), [`12_lupa_complejo_pdh.py`](02_mapa_central_integrado/12_lupa_complejo_pdh.py), [`13_lupa_cadena_respiratoria_cte.py`](02_mapa_central_integrado/13_lupa_cadena_respiratoria_cte.py), [`23_lupa_lanzadera_glicerol_3p.py`](02_mapa_central_integrado/23_lupa_lanzadera_glicerol_3p.py).
* **Lípidos en el Lienzo:** [`14_citosol_lipogenesis.py`](02_mapa_central_integrado/14_citosol_lipogenesis.py), [`15_sintesis_de_colesterol.py`](02_mapa_central_integrado/15_sintesis_de_colesterol.py), [`16_matriz_beta_oxidacion.py`](02_mapa_central_integrado/16_matriz_beta_oxidacion.py), [`17_matriz_cetogenesis.py`](02_mapa_central_integrado/17_matriz_cetogenesis.py).
* **Nitrógeno y Nucleótidos:** [`18_transaminacion_y_desaminacion.py`](02_mapa_central_integrado/18_transaminacion_y_desaminacion.py), [`19_destinos_esqueletos_carbonados_aa.py`](02_mapa_central_integrado/19_destinos_esqueletos_carbonados_aa.py), [`20_ciclo_de_la_urea_y_biciclo.py`](02_mapa_central_integrado/20_ciclo_de_la_urea_y_biciclo.py), [`21_biosintesis_de_nucleotidos.py`](02_mapa_central_integrado/21_biosintesis_de_nucleotidos.py), [`22_catabolismo_nucleotidos_acido_urico.py`](02_mapa_central_integrado/22_catabolismo_nucleotidos_acido_urico.py).
* **Cierre:** [`24_defs_marcadores_y_ensamblaje.py`](02_mapa_central_integrado/24_defs_marcadores_y_ensamblaje.py).

---

### 3️⃣ [`03_ampliacion_vias_18_a_25/`](03_ampliacion_vias_18_a_25/) — Bandas Periféricas y Calibración
* **[`01_estructuras_visuales/`](03_ampliacion_vias_18_a_25/01_estructuras_visuales/)**: Dibujos vectoriales de lípidos, micela, lipoproteínas, enterocito, sarcómero, cerebro/neurona y aminoácidos.
* **[`02_banda_izquierda_organos/`](03_ampliacion_vias_18_a_25/02_banda_izquierda_organos/)**: Vía 18 (Digestión intestinal), Vía 19 (Adipocito: ATGL/HSL/MGL), Vía 20 (Músculo y sarcómero), Vía 21 (Cerebro y BHE).
* **[`03_banda_derecha_biosintesis/`](03_ampliacion_vias_18_a_25/03_banda_derecha_biosintesis/)**: Vía 22 (Lipoproteínas VLDL/LDL/HDL), Vía 23 (Vía de Kennedy TAG/PL), Vía 24 (Biosíntesis de AA no esenciales), Vía 25 (Conmutador de estados metabólicos).
* **[`04_calibracion_y_ensamblaje/`](03_ampliacion_vias_18_a_25/04_calibracion_y_ensamblaje/)**: Leyenda de 25 vías, [`02_correcciones_auditoria.py`](03_ampliacion_vias_18_a_25/04_calibracion_y_ensamblaje/02_correcciones_auditoria.py) y ensamblador final.

---

### 4️⃣ [`04_algoritmos_trazado_y_validacion/`](04_algoritmos_trazado_y_validacion/) — Motores Algorítmicos
* **[`01_conector_rutas_astar/`](04_algoritmos_trazado_y_validacion/01_conector_rutas_astar/)** (El algoritmo que conecta las rutas):
  1. [`01_catalogo_45_conexiones_y_carriers.py`](04_algoritmos_trazado_y_validacion/01_conector_rutas_astar/01_catalogo_45_conexiones_y_carriers.py)
  2. [`02_lector_geometria_svg.py`](04_algoritmos_trazado_y_validacion/01_conector_rutas_astar/02_lector_geometria_svg.py)
  3. [`03_rejilla_costes_y_obstaculos.py`](04_algoritmos_trazado_y_validacion/01_conector_rutas_astar/03_rejilla_costes_y_obstaculos.py)
  4. [`04_algoritmo_astar_8_direcciones.py`](04_algoritmos_trazado_y_validacion/01_conector_rutas_astar/04_algoritmo_astar_8_direcciones.py)
  5. [`05_curvas_bezier_y_colocacion_rotulos.py`](04_algoritmos_trazado_y_validacion/01_conector_rutas_astar/05_curvas_bezier_y_colocacion_rotulos.py)
  6. [`06_orquestador_capa_conexiones.py`](04_algoritmos_trazado_y_validacion/01_conector_rutas_astar/06_orquestador_capa_conexiones.py)
* **[`02_detector_solapamientos/`](04_algoritmos_trazado_y_validacion/02_detector_solapamientos/)** (El verificador de colisiones):
  1. [`01_algebra_afin_y_muestreo_paths.py`](04_algoritmos_trazado_y_validacion/02_detector_solapamientos/01_algebra_afin_y_muestreo_paths.py)
  2. [`02_recorrido_arbol_svg.py`](04_algoritmos_trazado_y_validacion/02_detector_solapamientos/02_recorrido_arbol_svg.py)
  3. [`03_motor_colisiones_liang_barsky.py`](04_algoritmos_trazado_y_validacion/02_detector_solapamientos/03_motor_colisiones_liang_barsky.py)
  4. [`04_reporte_y_debug_svg.py`](04_algoritmos_trazado_y_validacion/02_detector_solapamientos/04_reporte_y_debug_svg.py)

---

### 5️⃣ [`05_datos_bioquimicos_y_regulacion/`](05_datos_bioquimicos_y_regulacion/) — Base de Datos Bioquímica
* [`01_regulacion_alosterica_y_hormonal.py`](05_datos_bioquimicos_y_regulacion/01_regulacion_alosterica_y_hormonal.py) — Efectores $\oplus/\ominus$ e insulina/glucagón.
* [`02_estequiometria_bloque_A_carbohidratos.py`](05_datos_bioquimicos_y_regulacion/02_estequiometria_bloque_A_carbohidratos.py) — Vías 1 a 4.
* [`03_estequiometria_bloque_B_energia_y_redox.py`](05_datos_bioquimicos_y_regulacion/03_estequiometria_bloque_B_energia_y_redox.py) — Vías 5 a 8.
* [`04_estequiometria_bloque_C_lipidos.py`](05_datos_bioquimicos_y_regulacion/04_estequiometria_bloque_C_lipidos.py) — Vías 9 a 12.
* [`05_estequiometria_bloque_D_nitrogeno_y_nucleotidos.py`](05_datos_bioquimicos_y_regulacion/05_estequiometria_bloque_D_nitrogeno_y_nucleotidos.py) — Vías 13 a 16.
* [`06_estequiometria_bloque_E_ampliacion_18_25.py`](05_datos_bioquimicos_y_regulacion/06_estequiometria_bloque_E_ampliacion_18_25.py) — Vías 18 a 24.
* [`07_generador_documentos_y_tablas.py`](05_datos_bioquimicos_y_regulacion/07_generador_documentos_y_tablas.py).

---

### 6️⃣ [`06_motor_interactividad_web/`](06_motor_interactividad_web/) — Frontend del Visor Interactivo
Con sintaxis nativa `.css`, `.html` y `.js` para que tu editor los coloree adecuadamente:
* [`01_estilos_interfaz_visor.css`](06_motor_interactividad_web/01_estilos_interfaz_visor.css)
* [`02_plantilla_dom_controles.html`](06_motor_interactividad_web/02_plantilla_dom_controles.html)
* [`03_catalogo_25_vias_y_colores.js`](06_motor_interactividad_web/03_catalogo_25_vias_y_colores.js)
* [`04_resaltado_y_zoom_vectorial_ctm.js`](06_motor_interactividad_web/04_resaltado_y_zoom_vectorial_ctm.js)
* [`05_indice_lateral_y_buscador_global.js`](06_motor_interactividad_web/05_indice_lateral_y_buscador_global.js)
* [`06_fichas_flotantes_tooltips.js`](06_motor_interactividad_web/06_fichas_flotantes_tooltips.js)
* [`07_estados_nutricionales_y_eventos.js`](06_motor_interactividad_web/07_estados_nutricionales_y_eventos.js)

---

### 7️⃣ [`07_exportacion_imprenta_y_utilidades/`](07_exportacion_imprenta_y_utilidades/) — Impresión y Herramientas
* Exportadores de póster (`01_generar_imprimible_v1.py`, `02_generar_imprimible_v2.py`), generador de reacciones base, exportador Excalidraw y verificador de capturas.
