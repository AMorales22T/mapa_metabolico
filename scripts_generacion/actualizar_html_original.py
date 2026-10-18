#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os

RUTA_HTML = "/home/dolfius/Escritorio/materias/mapa_metabolico/versiones_html/01_mapa_ampliado_completo_25_vias.html"

def main():
    if not os.path.exists(RUTA_HTML):
        print(f"Error: {RUTA_HTML} no existe")
        return

    with open(RUTA_HTML, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Limpieza de emojis
    emojis = [
        ('📑 Vías (25)', 'Vias (25)'),
        ('🍽️ Posprandial', 'Posprandial'),
        ('⚡ Ayuno', 'Ayuno'),
        ('🌐 Vistas / PDF', 'Vistas / PDF'),
        ('<span class="ui_search_icon">🔍</span>', '<span class="ui_search_icon" style="font-size:10px; font-weight:800; color:#94a3b8; margin-right:4px;">BUSCAR</span>'),
        ('🌟 01. Mapa Ampliado (25 Vías)', '01. Mapa Ampliado (25 Vias)'),
        ('🧩 02. Ampliación Vías 18–25 (Standalone)', '02. Ampliacion Vias 18–25 (Standalone)'),
        ('🗺️ 03. Mapa Central (17 Vías)', '03. Mapa Central (17 Vias)'),
        ('📋 04. Temario A–E (Metabolismo Intermediario)', '04. Temario A–E (Metabolismo Intermediario)'),
        ('📥 Descargar PDF 25 Vías (120×90 cm)', 'Descargar PDF 25 Vias (120×90 cm)'),
        ('📥 Descargar PDF Standalone Vías 18–25', 'Descargar PDF Standalone Vias 18–25'),
        ('<span>📑</span>', '<span>[Vias]</span>'),
        ('`📑 Vías (${viasCount})`', '`Vias (${viasCount})`'),
        ('`📑 Vias (${viasCount})`', '`Vias (${viasCount})`'),
    ]
    for viejo, nuevo in emojis:
        content = content.replace(viejo, nuevo)

    # 2. Inyección de estilos
    estilos = """
    /* Selector de Version del Mapa y Selector Rapido de Vias */
    .ui_map_version_group {
      display: inline-flex;
      align-items: center;
      background: #090d16;
      border: 1px solid #334155;
      border-radius: 8px;
      padding: 2px;
      gap: 2px;
    }
    .ui_ver_link {
      display: inline-flex;
      align-items: center;
      gap: 6px;
      padding: 5px 10px;
      font-size: 0.78rem;
      font-weight: 600;
      text-decoration: none;
      color: #94a3b8;
      border-radius: 6px;
      transition: all 0.15s ease;
      white-space: nowrap;
      cursor: pointer;
    }
    .ui_ver_link:hover {
      color: #f8fafc;
      background: #1e293b;
    }
    .ui_ver_link.active {
      color: #38bdf8;
      background: #1e293b;
      border: 1px solid #0284c7;
      font-weight: 700;
      box-shadow: 0 1px 4px rgba(2, 132, 199, 0.3);
    }
    .ui_live_dot {
      width: 7px;
      height: 7px;
      border-radius: 50%;
      background: #38bdf8;
      box-shadow: 0 0 6px #38bdf8;
      display: inline-block;
    }
    .ui_quick_via_wrapper {
      display: inline-flex;
      align-items: center;
      gap: 4px;
    }
    #ui_select_quick_via {
      background: #1e293b;
      border: 1px solid #475569;
      color: #f8fafc;
      font-size: 0.8rem;
      font-weight: 600;
      padding: 5px 8px;
      border-radius: 6px;
      outline: none;
      cursor: pointer;
      max-width: 260px;
      transition: border-color 0.15s ease;
    }
    #ui_select_quick_via:hover, #ui_select_quick_via:focus {
      border-color: #38bdf8;
    }
    #ui_select_quick_via optgroup {
      background: #0f172a;
      color: #94a3b8;
      font-weight: 700;
      font-size: 0.75rem;
    }
    #ui_select_quick_via option {
      background: #1e293b;
      color: #f8fafc;
      font-weight: 500;
      font-size: 0.8rem;
      padding: 3px 6px;
    }
    body.ui_isolate_mode .ui_dimmed {
      display: none !important;
    }
    .ui_state_btn.ui_btn_active_custom {
      background: #0284c7 !important;
      color: #ffffff !important;
    }
  </style>"""
    if 'ui_map_version_group' not in content:
        content = content.replace('  </style>', estilos, 1)

    # 3. Inyección de controles al inicio de .controls
    controles_inicio = """      <!-- Selector de Version del Mapa -->
      <div class="ui_map_version_group">
        <a href="../index.html" class="ui_ver_link" onclick="irAMapaAlternativo(); return false;" title="Mapa interactivo con flujo animado continuo a 60 FPS, lanzaderas y monitor CTE">
          <span class="ui_live_dot"></span> Mapa Alternativo (Vivo)
        </a>
        <a href="01_mapa_ampliado_completo_25_vias.html" class="ui_ver_link active" onclick="irAMapaOriginal(); return false;" title="Mapa cartulina base clasico ampliado de 25 vias">
          Mapa Original (Base)
        </a>
      </div>

      <!-- Selector Rapido de Vias (1 a 25) y Aislamiento -->
      <div class="ui_quick_via_wrapper">
        <select id="ui_select_quick_via" onchange="seleccionarViaRapida(this.value)" title="Seleccionar via metabolica individual">
          <option value="">-- Ver Via Individual (1 a 25) --</option>
          <optgroup label="Carbohidratos y Respiracion Celular">
            <option value="1">Via 1: Glucolisis (Citosol)</option>
            <option value="2">Via 2: Gluconeogenesis (Matriz / Citosol / RE)</option>
            <option value="3">Via 3: Glucogeno (Genesis y Lisis)</option>
            <option value="4">Via 4: Via de las Pentosas Fosfato</option>
            <option value="5">Via 5: Complejo Piruvato Deshidrogenasa (PDH)</option>
            <option value="6">Via 6: Ciclo de Krebs (ATC)</option>
            <option value="7">Via 7: Cadena Respiratoria y ATP Sintasa</option>
            <option value="8">Via 8: Lanzadera Malato-Aspartato</option>
            <option value="8B">Via 8B: Lanzadera Glicerol-3-Fosfato</option>
          </optgroup>
          <optgroup label="Lipidos y Cuerpos Cetonicos">
            <option value="9">Via 9: Beta-Oxidacion y Lanzadera de Carnitina</option>
            <option value="10">Via 10: Lipogenesis de Novo y Lanzadera de Citrato</option>
            <option value="11">Via 11: Cetogenesis Hepatica</option>
            <option value="12">Via 12: Biosintesis de Colesterol</option>
          </optgroup>
          <optgroup label="Nitrogeno, Aminoacidos y Nucleotidos">
            <option value="12B">Via 12B: Transulfuracion y Destino Carbonado AA</option>
            <option value="13">Via 13: Transaminacion y Ciclo Glucosa-Alanina</option>
            <option value="14">Via 14: Ciclo de la Urea y Biciclo Krebs-Henseleit</option>
            <option value="15">Via 15: Biosintesis de Purinas y Pirimidinas</option>
            <option value="16">Via 16: Catabolismo Nucleotidos y Acido Urico (URAT1)</option>
          </optgroup>
          <optgroup label="Ampliacion Fisiologica Intertisular">
            <option value="17">Via 17: Ciclo de Cori y Ciclo de Cahill (Vascular)</option>
            <option value="18">Via 18: Digestion y Absorcion de Lipidos (Enterocito)</option>
            <option value="19">Via 19: Lipolisis Adipocitaria (ATGL/HSL/MGL)</option>
            <option value="20">Via 20: Musculo Esqueletico y Sarcomero</option>
            <option value="21">Via 21: Cerebro, Barrera Hematoencefalica y Cetolisis</option>
            <option value="22">Via 22: Metabolismo Lipoproteinas Plasmaticas</option>
            <option value="23">Via 23: Via de Kennedy (Fosfolipidos Membrana)</option>
            <option value="24">Via 24: Biosintesis Aminoacidos No Esenciales</option>
            <option value="25">Via 25: Conmutador Hormonal Pancreatico</option>
          </optgroup>
        </select>
        <button id="ui_btn_isolate" class="ui_state_btn" onclick="toggleModoAislar()" title="Oculta por completo las vias atenuadas para ver unicamente la via seleccionada">Aislar</button>
        <button id="ui_btn_open_svg" class="ui_state_btn" onclick="abrirSvgViaActual()" style="background:#0284c7; color:#ffffff; font-weight:700;" title="Abrir el diagrama SVG vectorial individual de esta ruta en una pestaña nueva">Ver SVG</button>
      </div>

      <div style="width: 1px; height: 20px; background: #475569; margin: 0 4px;"></div>

      <!-- Botón de Índice -->"""
    if 'ui_select_quick_via' not in content:
        content = content.replace('      <!-- Botón de Índice -->', controles_inicio, 1)
    elif 'ui_btn_open_svg' not in content:
        content = content.replace(
            '<button id="ui_btn_isolate" class="ui_state_btn" onclick="toggleModoAislar()" title="Oculta por completo las vias atenuadas para ver unicamente la via seleccionada">Aislar</button>',
            '<button id="ui_btn_isolate" class="ui_state_btn" onclick="toggleModoAislar()" title="Oculta por completo las vias atenuadas para ver unicamente la via seleccionada">Aislar</button>\n        <button id="ui_btn_open_svg" class="ui_state_btn" onclick="abrirSvgViaActual()" style="background:#0284c7; color:#ffffff; font-weight:700;" title="Abrir el diagrama SVG vectorial individual de esta ruta en una pestaña nueva">Ver SVG</button>'
        )

    # Inyectar boton de Ver SVG Individual en el banner flotante
    banner_viejo = """  <!-- BANNER FLOTANTE DE VÍA RESALTADA -->
  <div id="ui_highlight_banner">
    <span id="ui_highlight_title">Vía resaltada</span>
    <button onclick="clearPathwayHighlight()" title="Quitar resaltado (Esc)">✕ Quitar</button>
  </div>"""
    banner_nuevo = """  <!-- BANNER FLOTANTE DE VÍA RESALTADA -->
  <div id="ui_highlight_banner">
    <span id="ui_highlight_title">Vía resaltada</span>
    <button id="ui_btn_banner_svg" onclick="abrirSvgViaActual()" style="background:#0284c7; color:#ffffff; border:none; padding:4px 10px; border-radius:4px; font-weight:700; cursor:pointer; font-size:0.75rem; margin-right:4px;">Abrir Diagrama SVG</button>
    <button onclick="clearPathwayHighlight()" title="Quitar resaltado (Esc)">✕ Quitar</button>
  </div>"""
    content = content.replace(banner_viejo, banner_nuevo, 1)

    # 4. Actualizar menú de vistas en 01_mapa_ampliado_completo_25_vias.html
    menu_vistas_nuevo = """        <div id="ui_menu_views" style="display: none; position: absolute; right: 0; top: 100%; margin-top: 6px; background: #0f172a; border: 1px solid #334155; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.6); min-width: 280px; z-index: 1000; padding: 6px 0; text-align: left;">
          <a href="../index.html" onclick="irAMapaAlternativo(); return false;" style="display: block; padding: 8px 14px; color: #38bdf8; text-decoration: none; font-size: 0.8rem; font-weight: 700;">* Mapa Alternativo (Flujo Vivo 60 FPS)</a>
          <a href="01_mapa_ampliado_completo_25_vias.html" onclick="irAMapaOriginal(); return false;" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem; font-weight: 700;">* Mapa Original Base (25 Vias)</a>
          <div style="height: 1px; background: #334155; margin: 4px 0;"></div>
          <a href="02_ampliacion_rutas_18_25.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">02. Ampliacion Vias 18–25 (Standalone)</a>
          <a href="03_mapa_central_interactivo_17_vias.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">03. Mapa Central (17 Vias)</a>
          <a href="04_cuadro_temario_bloques_A_E.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">04. Temario A–E (Metabolismo Intermediario)</a>
          <div style="height: 1px; background: #334155; margin: 4px 0;"></div>
          <a href="../versiones_impresion/01_mapa_ampliado_completo_120x90cm.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #4ade80; text-decoration: none; font-size: 0.8rem; font-weight: 700;">Descargar PDF 25 Vias Base (120×90 cm)</a>
          <a href="../mapa_metabolico_alternativo/mapa_metabolico_alternativo_120x90cm.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #38bdf8; text-decoration: none; font-size: 0.8rem; font-weight: 700;">Descargar PDF Alternativo (120×90 cm)</a>
          <a href="../versiones_impresion/02_ampliacion_rutas_18_25.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #4ade80; text-decoration: none; font-size: 0.8rem;">Descargar PDF Standalone Vias 18–25</a>
        </div>"""
    menu_vistas_viejo = """        <div id="ui_menu_views" style="display: none; position: absolute; right: 0; top: 100%; margin-top: 6px; background: #0f172a; border: 1px solid #334155; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.6); min-width: 260px; z-index: 1000; padding: 6px 0; text-align: left;">
          <a href="01_mapa_ampliado_completo_25_vias.html" style="display: block; padding: 8px 14px; color: #38bdf8; text-decoration: none; font-size: 0.8rem; font-weight: 700;">01. Mapa Ampliado (25 Vias)</a>
          <a href="02_ampliacion_rutas_18_25.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">02. Ampliacion Vias 18–25 (Standalone)</a>
          <a href="03_mapa_central_interactivo_17_vias.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">03. Mapa Central (17 Vias)</a>
          <a href="04_cuadro_temario_bloques_A_E.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">04. Temario A–E (Metabolismo Intermediario)</a>
          <div style="height: 1px; background: #334155; margin: 4px 0;"></div>
          <a href="../versiones_impresion/01_mapa_ampliado_completo_120x90cm.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #4ade80; text-decoration: none; font-size: 0.8rem; font-weight: 700;">Descargar PDF 25 Vias (120×90 cm)</a>
          <a href="../versiones_impresion/02_ampliacion_rutas_18_25.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #4ade80; text-decoration: none; font-size: 0.8rem;">Descargar PDF Standalone Vias 18–25</a>
        </div>"""
    content = content.replace(menu_vistas_viejo, menu_vistas_nuevo, 1)

    # 5. Inyección de JavaScript antes de </script>
    js_original = """
    const MAPA_VIAS_SVG = {
      "1": "01_CARBOHIDRATOS/via_01_glucolisis/Glucolisis.svg",
      "2": "01_CARBOHIDRATOS/via_02_gluconeogenesis/Gluconeogenesis.svg",
      "3": "01_CARBOHIDRATOS/via_03_glucogenogenesis_y_glucogenolisis/Glucogenesis.svg",
      "4": "01_CARBOHIDRATOS/via_04_pentosas_fosfato/Pentosas.svg",
      "5": "02_RESPIRACION_Y_ENERGIA/via_05_complejo_pdh/Piruvato_Deshidrogenasa.svg",
      "6": "02_RESPIRACION_Y_ENERGIA/via_06_ciclo_de_krebs/Ciclo_de_Krebs.svg",
      "7": "02_RESPIRACION_Y_ENERGIA/via_07_cadena_respiratoria_atp_sintasa/Cadena_Transporte_Electrones.svg",
      "8": "02_RESPIRACION_Y_ENERGIA/via_08_lanzaderas/Lanzadera_Malato_Aspartato.svg",
      "8B": "02_RESPIRACION_Y_ENERGIA/via_08_lanzaderas/Lanzadera_Glicerol_3_Fosfato.svg",
      "9": "03_LIPIDOS/via_09_beta_oxidacion/Beta_Oxidacion.svg",
      "10": "03_LIPIDOS/via_10_lipogenesis/Lipogenesis.svg",
      "11": "03_LIPIDOS/via_11_cetogenesis_y_cetolisis/Cetogenesis_y_Cetolisis.svg",
      "12": "03_LIPIDOS/via_12_colesterol_y_lipoproteinas/Colesterol.svg",
      "12B": "04_NITROGENO_Y_AMINOACIDOS/via_12b_destinos_esqueletos_carbonados/Destinos_Esqueletos_Carbonados.svg",
      "13": "04_NITROGENO_Y_AMINOACIDOS/via_13_transaminacion_y_desaminacion/Transaminacion_y_Desaminacion.svg",
      "14": "04_NITROGENO_Y_AMINOACIDOS/via_14_ciclo_de_la_urea/Ciclo_de_la_Urea.svg",
      "15": "05_NUCLEOTIDOS_Y_OTRAS/via_15_sintesis_purinas_y_pirimidinas/Sintesis_Purinas_y_Pirimidinas.svg",
      "16": "05_NUCLEOTIDOS_Y_OTRAS/via_16_degradacion_y_acido_urico/Degradacion_Nucleotidos_y_Acido_Urico.svg",
      "17": "01_CARBOHIDRATOS/via_17_ciclo_de_cori/Ciclo_de_Cori.svg",
      "18": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "19": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "20": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "21": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "22": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "23": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "24": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg",
      "25": "07_AMPLIACION_TEMARIO/ampliacion_rutas_18_25_interactiva.svg"
    };

    function getSvgUrlDeVia(viaId) {
      const rel = MAPA_VIAS_SVG[viaId];
      if (!rel) return null;
      const isSubdir = window.location.pathname.includes('/versiones_html') || window.location.pathname.includes('/mapa_metabolico_alternativo');
      return (isSubdir ? '../' : '') + rel;
    }

    function abrirSvgViaActual() {
      const sel = document.getElementById('ui_select_quick_via');
      const viaId = (sel && sel.value) ? sel.value : (typeof viaResaltadaActual !== 'undefined' ? viaResaltadaActual : null);
      if (!viaId) {
        alert('Por favor selecciona primero una vía en el selector o en el mapa.');
        return;
      }
      const url = getSvgUrlDeVia(viaId);
      if (url) {
        window.open(url, '_blank');
      }
    }

    let modoAislarActivo = false;
    function toggleModoAislar() {
      modoAislarActivo = !modoAislarActivo;
      document.body.classList.toggle('ui_isolate_mode', modoAislarActivo);
      const btn = document.getElementById('ui_btn_isolate');
      if (btn) btn.classList.toggle('ui_btn_active_custom', modoAislarActivo);
    }

    function irAMapaAlternativo() {
      try {
        const params = window.location.search;
        const isSubdir = window.location.pathname.includes('/versiones_html') || window.location.pathname.includes('/mapa_metabolico_alternativo');
        const target = isSubdir ? '../index.html' : 'index.html';
        window.location.href = target + params;
      } catch (e) {
        window.location.href = '../index.html';
      }
    }

    function irAMapaOriginal() {
      try {
        const params = window.location.search;
        const isSubdir = window.location.pathname.includes('/versiones_html') || window.location.pathname.includes('/mapa_metabolico_alternativo');
        let target = '01_mapa_ampliado_completo_25_vias.html';
        if (isSubdir) {
          target = window.location.pathname.includes('/versiones_html') ? '01_mapa_ampliado_completo_25_vias.html' : '../versiones_html/01_mapa_ampliado_completo_25_vias.html';
        } else if (window.location.protocol === 'file:') {
          target = 'versiones_html/01_mapa_ampliado_completo_25_vias.html';
        }
        window.location.href = target + params;
      } catch (e) {
        window.location.href = '01_mapa_ampliado_completo_25_vias.html';
      }
    }

    function seleccionarViaRapida(val) {
      if (!val) {
        if (typeof clearPathwayHighlight === 'function') clearPathwayHighlight();
        actualizarParametroURL('via', null);
        return;
      }
      if (typeof highlightPathway === 'function') {
        highlightPathway(val, true);
        actualizarParametroURL('via', val);
      }
    }

    function actualizarParametroURL(clave, valor) {
      try {
        const url = new URL(window.location.href);
        if (valor) {
          url.searchParams.set(clave, valor);
        } else {
          url.searchParams.delete(clave);
        }
        window.history.replaceState(null, '', url.toString());
      } catch (e) {
        // Fallback silencioso
      }
    }

    // Enganches para mantener sincronizado el selector rapido y la URL
    if (typeof highlightPathway === 'function') {
      const origHighlightPathway = highlightPathway;
      highlightPathway = function(viaId, shouldZoom = false) {
        origHighlightPathway(viaId, shouldZoom);
        const sel = document.getElementById('ui_select_quick_via');
        if (sel && sel.value !== String(viaId)) {
          sel.value = String(viaId);
        }
        actualizarParametroURL('via', viaId);

        const bannerBtn = document.getElementById('ui_btn_banner_svg');
        if (bannerBtn) bannerBtn.style.display = MAPA_VIAS_SVG[viaId] ? 'inline-block' : 'none';
      };
    }

    if (typeof clearPathwayHighlight === 'function') {
      const origClearPathwayHighlight = clearPathwayHighlight;
      clearPathwayHighlight = function() {
        origClearPathwayHighlight();
        const sel = document.getElementById('ui_select_quick_via');
        if (sel) {
          sel.value = '';
        }
        actualizarParametroURL('via', null);

        const bannerBtn = document.getElementById('ui_btn_banner_svg');
        if (bannerBtn) bannerBtn.style.display = 'none';
      };
    }

    // Inyectar boton [SVG] en cada elemento del indice lateral
    const fnOrigPoblar = window.poblarSidebarVias;
    if (typeof fnOrigPoblar === 'function') {
      window.poblarSidebarVias = function() {
        fnOrigPoblar();
        document.querySelectorAll('.ui_sidebar_item').forEach(it => {
          const vid = it.getAttribute('data-via');
          const svgUrl = getSvgUrlDeVia(vid);
          if (svgUrl && !it.querySelector('.ui_sidebar_svg_btn')) {
            const btn = document.createElement('a');
            btn.className = 'ui_sidebar_svg_btn';
            btn.href = svgUrl;
            btn.target = '_blank';
            btn.title = 'Abrir diagrama SVG individual';
            btn.textContent = 'SVG';
            btn.onclick = (e) => e.stopPropagation();
            btn.style.cssText = 'margin-left:auto; background:rgba(56,189,248,0.15); border:1px solid #0284c7; color:#38bdf8; font-size:10px; font-weight:800; padding:2px 6px; border-radius:4px; text-decoration:none; white-space:nowrap;';
            it.appendChild(btn);
          }
        });
      };
    }

    function procesarParametrosURL() {
      try {
        const params = new URLSearchParams(window.location.search);
        
        const svgParam = params.get('svg') || params.get('img');
        if (svgParam) {
          const raw = svgParam.trim();
          const upper = raw.toUpperCase();
          const target = MAPA_VIAS_SVG[upper] ? upper : (MAPA_VIAS_SVG[raw] ? raw : null);
          if (target) {
            const url = getSvgUrlDeVia(target);
            if (url) {
              window.location.href = url;
              return;
            }
          }
        }

        const viaParam = params.get('via');
        if (viaParam) {
          const raw = viaParam.trim();
          const upper = raw.toUpperCase();
          const targetVia = (typeof TABLA_VIAS !== 'undefined' && TABLA_VIAS[upper]) ? upper : ((typeof TABLA_VIAS !== 'undefined' && TABLA_VIAS[raw]) ? raw : null);
          if (targetVia) {
            setTimeout(() => {
              if (typeof highlightPathway === 'function') highlightPathway(targetVia, true);
            }, 300);
          } else {
            const vNum = parseInt(raw, 10);
            if (!isNaN(vNum) && vNum >= 1 && vNum <= 25) {
              setTimeout(() => {
                if (typeof highlightPathway === 'function') highlightPathway(String(vNum), true);
              }, 300);
            }
          }
        }
        const searchParam = params.get('search') || params.get('q');
        if (searchParam) {
          setTimeout(() => {
            const input = document.getElementById('ui_search_input');
            if (input) {
              input.value = searchParam;
              if (typeof ejecutarBusqueda === 'function') ejecutarBusqueda();
            }
          }, 300);
        }
        const stateParam = params.get('state');
        if (stateParam) {
          setTimeout(() => {
            if (typeof setMetabolicState === 'function') setMetabolicState(stateParam);
          }, 300);
        }
      } catch (err) {
        console.warn('Error al procesar parametros URL:', err);
      }
    }

    window.addEventListener('DOMContentLoaded', () => {
      procesarParametrosURL();
    });
    if (document.readyState !== 'loading') {
      procesarParametrosURL();
    }
  </script>"""
    if 'MAPA_VIAS_SVG' not in content:
        content = content.replace('  </script>', js_original, 1)

    with open(RUTA_HTML, "w", encoding="utf-8") as f:
        f.write(content)
    print("01_mapa_ampliado_completo_25_vias.html actualizado exitosamente!")

if __name__ == "__main__":
    main()
