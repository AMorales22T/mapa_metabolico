#!/usr/bin/env python3
"""
GENERADOR DE VERSIÓN INTERACTIVA DEL MAPA METABÓLICO (HERRAMIENTA DE ESTUDIO)
=============================================================================
Reglas respetadas estrictamente:
1. Lee prueba_visual_integrada_conectada.html SIN modificarlo.
2. Genera prueba_visual_interactiva.html como COPIA enriquecida en CSS, JS y paneles HTML.
3. El contenido interior del SVG original se mantiene 100% IDÉNTICO byte a byte:
   - Cero IDs, grupos, coordenadas, textos o colores modificados o reordenados.
4. Funcionalidades añadidas:
   - Resaltado de vías al clic (vía o badge_via_N), atenuando el resto.
     Distingue clic de arrastre (umbral <= 4px).
   - Índice lateral plegable con las 16 vías (+8B y 12B) según la leyenda original,
     con zoom animado a cada vía mediante getBBox() / scale / pointX / pointY.
   - Buscador universal (sin acentos / mayúsculas), centra y resalta (pulse),
     con contador "n de N", Enter pasa a la siguiente.
   - Ficha / Tooltip flotante al pasar el ratón por rx_* o m_* con toda la información
     real del mapa (regulación (+), (-), (P), hormonal, etc.) y diccionario JS
     extensible vacío para datos futuros (sin inventar bioquímica).
   - Modos de estado metabólico: Posprandial y Ayuno (y Normal) con tabla JS
     editable y rótulo explicativo flotante.
   - Soporte táctil completo (arrastre con 1 dedo y pellizco para zoom).
   - Atajos de teclado: '/' enfoca buscador, 'Esc' limpia, 'F' ajusta vista.
   - Todo lo nuevo se oculta en @media print.
   - Alta fluidez y rendimiento.
5. Verificación estricta de integridad (SVG original vs copia).
"""
import json
import os
import re
import subprocess
import sys

DIR_SCRIPT = os.path.dirname(os.path.abspath(__file__))
DIR_BASE = os.path.dirname(DIR_SCRIPT) if os.path.basename(DIR_SCRIPT) == "scripts_generacion" else DIR_SCRIPT
DIR_HTML = os.path.join(DIR_BASE, "versiones_html")
RUTA_ORIGINAL = os.path.join(DIR_HTML, "prueba_visual_integrada_conectada.html")
RUTA_INTERACTIVA = os.path.join(DIR_HTML, "prueba_visual_interactiva.html")

sys.path.append(os.path.join(DIR_BASE, "06_REGULACION_Y_LEYENDA"))
try:
    import reacciones_estequiometria as re_est
    TABLA_REACCIONES_DATA = re_est.REACCIONES_ESTEQUIOMETRIA
except Exception:
    TABLA_REACCIONES_DATA = {}

def construir_interactiva():
    print(f"1. Leyendo archivo original: {RUTA_ORIGINAL}")
    with open(RUTA_ORIGINAL, "r", encoding="utf-8") as f:
        html_orig = f.read()

    # Extraer el interior exacto del SVG (desde <svg hasta </svg>)
    svg_open_idx = html_orig.find("<svg")
    if svg_open_idx == -1:
        raise ValueError("No se encontró la etiqueta <svg en el archivo original")
    svg_close_idx = html_orig.rfind("</svg>") + 6
    svg_completo_orig = html_orig[svg_open_idx:svg_close_idx]

    print(f"   ✓ SVG original extraído intacto: {len(svg_completo_orig):,} caracteres")

    # CSS adicional para componentes UI (con prefijos ui_ y #ui_)
    css_ui = """
    /* =============================================================
       ESTILOS DE LA HERRAMIENTA DE ESTUDIO INTERACTIVA (PREFIJO ui_)
       ============================================================= */

    /* Atenuación y resaltado de vías de alto rendimiento */
    .ui_dimmed {
      opacity: 0.12 !important;
      transition: opacity 0.22s cubic-bezier(0.4, 0, 0.2, 1);
      filter: grayscale(45%);
    }
    .ui_highlighted {
      opacity: 1 !important;
      transition: opacity 0.22s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .ui_state_active {
      opacity: 1 !important;
      transition: opacity 0.22s cubic-bezier(0.4, 0, 0.2, 1);
    }

    /* Animación de pulso para la búsqueda */
    .ui_search_pulse {
      outline: 5px solid #38bdf8 !important;
      outline-offset: 6px;
      border-radius: 8px;
      animation: ui_anim_pulse 1.4s infinite alternate ease-in-out;
    }
    @keyframes ui_anim_pulse {
      0% { filter: drop-shadow(0 0 4px #0284c7); }
      100% { filter: drop-shadow(0 0 20px #38bdf8); }
    }

    /* Cursor interactivo sobre elementos informativos */
    [id^="m_"], [id^="rx_"], .badge-via {
      cursor: pointer !important;
    }

    /* Barra superior con controles reorganizados */
    .header-bar {
      gap: 14px;
      flex-wrap: wrap;
      padding: 8px 18px !important;
    }
    .header-bar h2 {
      font-size: 1.05rem !important;
      margin-bottom: 2px;
      color: #38bdf8;
      font-weight: 800;
    }
    .header-bar p {
      font-size: 0.74rem !important;
      color: #94a3b8;
    }

    /* Grupo de estados metabólicos */
    .ui_state_group {
      display: inline-flex;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 7px;
      padding: 2px;
      gap: 2px;
    }
    .ui_state_btn {
      background: transparent !important;
      color: #94a3b8 !important;
      border: none !important;
      padding: 5px 11px !important;
      border-radius: 5px !important;
      font-size: 0.78rem !important;
      font-weight: 700 !important;
      cursor: pointer;
      transition: all 0.15s ease;
    }
    .ui_state_btn:hover {
      color: #ffffff !important;
      background: rgba(255, 255, 255, 0.06) !important;
    }
    .ui_state_btn.ui_active {
      background: #0284c7 !important;
      color: #ffffff !important;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.4);
    }
    .ui_state_btn#ui_btn_state_fasting.ui_active {
      background: #ea580c !important;
    }
    .ui_state_btn#ui_btn_state_fed.ui_active {
      background: #10b981 !important;
    }

    /* Buscador en la barra */
    #ui_search_container {
      display: flex;
      align-items: center;
      background: #0f172a;
      border: 1px solid #334155;
      border-radius: 7px;
      padding: 2px 8px;
      gap: 6px;
      min-width: 250px;
      max-width: 320px;
      transition: border-color 0.2s, box-shadow 0.2s;
    }
    #ui_search_container:focus-within {
      border-color: #38bdf8;
      box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.25);
    }
    .ui_search_icon {
      font-size: 0.82rem;
      color: #64748b;
    }
    #ui_search_input {
      background: transparent;
      border: none;
      outline: none;
      color: #f8fafc;
      font-size: 0.8rem;
      font-family: inherit;
      width: 100%;
    }
    #ui_search_input::placeholder {
      color: #64748b;
    }
    #ui_search_counter {
      font-size: 0.72rem;
      font-weight: 800;
      color: #38bdf8;
      font-family: 'JetBrains Mono', monospace;
      white-space: nowrap;
    }
    .ui_search_btn {
      background: transparent !important;
      border: none !important;
      color: #94a3b8 !important;
      padding: 2px 4px !important;
      font-size: 0.72rem !important;
      cursor: pointer;
      border-radius: 4px;
    }
    .ui_search_btn:hover {
      color: #f8fafc !important;
      background: rgba(255, 255, 255, 0.1) !important;
    }

    /* Botón de alternancia del índice de vías */
    #ui_btn_toggle_sidebar {
      background: #475569 !important;
      color: #ffffff !important;
      border: none;
      padding: 6px 12px;
      border-radius: 6px;
      font-weight: 800;
      font-size: 0.82rem;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 6px;
      transition: background 0.15s;
    }
    #ui_btn_toggle_sidebar:hover {
      background: #64748b !important;
    }
    #ui_btn_toggle_sidebar.ui_active {
      background: #0284c7 !important;
    }

    /* Panel lateral plegable (Índice de Vías) */
    #ui_sidebar_panel {
      position: absolute;
      top: 0;
      left: 0;
      bottom: 0;
      width: 380px;
      background: rgba(15, 23, 42, 0.95);
      backdrop-filter: blur(14px);
      -webkit-backdrop-filter: blur(14px);
      border-right: 1px solid #334155;
      z-index: 100;
      display: flex;
      flex-direction: column;
      transform: translateX(-100%);
      transition: transform 0.26s cubic-bezier(0.4, 0, 0.2, 1);
      box-shadow: 4px 0 24px rgba(0, 0, 0, 0.5);
    }
    #ui_sidebar_panel.ui_open {
      transform: translateX(0);
    }
    .ui_sidebar_header {
      padding: 14px 18px;
      border-bottom: 1px solid #334155;
      display: flex;
      justify-content: space-between;
      align-items: center;
      background: #1e293b;
    }
    .ui_sidebar_header h3 {
      font-size: 0.96rem;
      color: #38bdf8;
      font-weight: 800;
    }
    .ui_sidebar_header p {
      font-size: 0.72rem;
      color: #94a3b8;
    }
    .ui_sidebar_close {
      background: transparent;
      border: none;
      color: #94a3b8;
      font-size: 1.1rem;
      cursor: pointer;
      padding: 4px 8px;
      border-radius: 6px;
    }
    .ui_sidebar_close:hover {
      color: #ffffff;
      background: rgba(255, 255, 255, 0.1);
    }
    .ui_sidebar_filter {
      padding: 10px 14px;
      border-bottom: 1px solid #1e293b;
      background: #0f172a;
    }
    .ui_sidebar_filter input {
      width: 100%;
      background: #1e293b;
      border: 1px solid #334155;
      border-radius: 6px;
      padding: 6px 10px;
      color: #f8fafc;
      font-size: 0.78rem;
      font-family: inherit;
      outline: none;
    }
    .ui_sidebar_filter input:focus {
      border-color: #38bdf8;
    }
    .ui_sidebar_list {
      flex: 1;
      overflow-y: auto;
      padding: 10px;
      display: flex;
      flex-direction: column;
      gap: 6px;
    }
    .ui_sidebar_item {
      display: flex;
      align-items: flex-start;
      gap: 10px;
      padding: 8px 10px;
      border-radius: 7px;
      background: rgba(30, 41, 59, 0.4);
      border: 1px solid transparent;
      cursor: pointer;
      transition: all 0.14s ease;
    }
    .ui_sidebar_item:hover {
      background: #1e293b;
      border-color: #475569;
      transform: translateX(2px);
    }
    .ui_sidebar_item.ui_active {
      background: rgba(2, 132, 199, 0.18);
      border-color: #0284c7;
      box-shadow: 0 0 10px rgba(2, 132, 199, 0.2);
    }
    .ui_badge_circle {
      min-width: 24px;
      height: 24px;
      border-radius: 50%;
      background: #0284c7;
      color: #ffffff;
      font-size: 0.72rem;
      font-weight: 900;
      font-family: 'JetBrains Mono', monospace;
      display: flex;
      align-items: center;
      justify-content: center;
      box-shadow: 0 1px 3px rgba(0, 0, 0, 0.3);
    }
    .ui_item_text {
      flex: 1;
    }
    .ui_item_title {
      font-size: 0.84rem;
      font-weight: 800;
      color: #f1f5f9;
      line-height: 1.25;
    }
    .ui_item_desc {
      font-size: 0.72rem;
      color: #94a3b8;
      margin-top: 2px;
      line-height: 1.25;
    }

    /* Botón flotante para abrir el índice cuando está plegado */
    #ui_btn_sidebar_floating {
      position: absolute;
      top: 14px;
      left: 14px;
      z-index: 50;
      background: rgba(15, 23, 42, 0.88);
      backdrop-filter: blur(8px);
      color: #38bdf8;
      border: 1px solid #334155;
      padding: 8px 14px;
      border-radius: 8px;
      font-size: 0.82rem;
      font-weight: 800;
      cursor: pointer;
      display: flex;
      align-items: center;
      gap: 7px;
      box-shadow: 0 4px 14px rgba(0, 0, 0, 0.4);
      transition: all 0.15s ease;
    }
    #ui_btn_sidebar_floating:hover {
      background: #1e293b;
      border-color: #38bdf8;
      transform: translateY(-1px);
    }

    /* Ficha / Tooltip flotante al pasar el ratón */
    #ui_tooltip_card {
      position: fixed;
      pointer-events: none;
      z-index: 1000;
      max-width: 440px;
      min-width: 270px;
      background: rgba(15, 23, 42, 0.98);
      backdrop-filter: blur(16px);
      -webkit-backdrop-filter: blur(16px);
      color: #f8fafc;
      border: 1px solid #0284c7;
      border-radius: 12px;
      padding: 14px 18px;
      box-shadow: 0 14px 35px rgba(0, 0, 0, 0.75);
      font-family: 'Inter', sans-serif;
      font-size: 0.8rem;
      opacity: 0;
      transform: translateY(6px);
      transition: opacity 0.14s ease, transform 0.14s ease, border-color 0.2s, box-shadow 0.2s;
    }
    #ui_tooltip_card.ui_visible {
      opacity: 1;
      transform: translateY(0);
    }
    #ui_tooltip_card.ui_tt_pinned {
      pointer-events: auto !important;
      border: 1.8px solid #38bdf8 !important;
      box-shadow: 0 16px 45px rgba(0, 0, 0, 0.85), 0 0 24px rgba(56, 189, 248, 0.35) !important;
    }
    .ui_tt_close_btn {
      position: absolute;
      top: 10px;
      right: 12px;
      background: rgba(255, 255, 255, 0.08);
      border: 1px solid rgba(255, 255, 255, 0.15);
      color: #94a3b8;
      width: 22px;
      height: 22px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 11px;
      font-weight: 900;
      cursor: pointer;
      transition: all 0.15s;
    }
    .ui_tt_close_btn:hover {
      background: #ef4444;
      color: #ffffff;
      border-color: #ef4444;
    }
    .ui_tt_header_row {
      display: flex;
      align-items: center;
      gap: 6px;
      flex-wrap: wrap;
      margin-bottom: 6px;
    }
    .ui_tt_badge_via {
      display: inline-block;
      color: #ffffff;
      border-radius: 4px;
      padding: 2px 7px;
      font-size: 9.5px;
      font-weight: 900;
      letter-spacing: 0.3px;
    }
    .ui_tt_badge_ec {
      display: inline-block;
      background: #312e81;
      border: 1px solid #4f46e5;
      color: #c7d2fe;
      border-radius: 4px;
      padding: 2px 6px;
      font-size: 9px;
      font-weight: 800;
      font-family: 'JetBrains Mono', monospace;
    }
    .ui_tt_eq_box {
      background: rgba(2, 132, 199, 0.1);
      border: 1px solid rgba(56, 189, 248, 0.3);
      border-left: 3.5px solid #38bdf8;
      border-radius: 6px;
      padding: 8px 10px;
      margin: 8px 0;
    }
    .ui_tt_eq_label {
      font-size: 8.5px;
      font-weight: 900;
      color: #38bdf8;
      letter-spacing: 0.8px;
      margin-bottom: 3px;
    }
    .ui_tt_eq_text {
      font-family: 'JetBrains Mono', monospace;
      font-size: 11px;
      font-weight: 800;
      color: #ffffff;
      line-height: 1.4;
      word-break: break-word;
    }
    .ui_tt_grid {
      display: flex;
      flex-direction: column;
      gap: 3px;
      margin: 6px 0;
      font-size: 10.5px;
    }
    .ui_tt_grid_row {
      display: flex;
      line-height: 1.35;
    }
    .ui_tt_label {
      color: #94a3b8;
      font-weight: 800;
      width: 82px;
      flex-shrink: 0;
    }
    .ui_tt_val {
      color: #e2e8f0;
      flex-grow: 1;
    }
    .ui_tt_reg_box {
      background: rgba(30, 41, 59, 0.7);
      border: 1px solid #334155;
      border-radius: 6px;
      padding: 6px 9px;
      margin-top: 6px;
      font-size: 10.5px;
      color: #cbd5e1;
      line-height: 1.35;
    }
    .ui_tt_pin_hint {
      margin-top: 6px;
      padding-top: 4px;
      border-top: 1px dashed rgba(148, 163, 184, 0.25);
      font-size: 9px;
      color: #64748b;
      font-style: italic;
      text-align: right;
    }
    .ui_tooltip_tag {
      display: inline-block;
      font-size: 0.65rem;
      font-weight: 900;
      letter-spacing: 0.5px;
      padding: 2px 7px;
      border-radius: 4px;
      font-family: 'JetBrains Mono', monospace;
      margin-right: 6px;
    }
    .ui_tag_enzyme { background: #0f766e; color: #ccfbf1; }
    .ui_tag_metabolite { background: #92400e; color: #fef3c7; }
    .ui_tooltip_pathway {
      font-size: 0.7rem;
      font-weight: 700;
      color: #94a3b8;
    }
    .ui_tooltip_title {
      font-size: 0.98rem;
      font-weight: 900;
      color: #ffffff;
      margin-top: 5px;
      margin-bottom: 3px;
      line-height: 1.25;
    }
    .ui_tooltip_sub {
      font-size: 0.76rem;
      color: #38bdf8;
      font-family: 'JetBrains Mono', monospace;
      font-weight: 700;
      margin-bottom: 6px;
    }
    .ui_tooltip_rows {
      display: flex;
      flex-direction: column;
      gap: 3px;
      margin-top: 6px;
      border-top: 1px solid #334155;
      padding-top: 6px;
    }
    .ui_reg_row {
      display: flex;
      align-items: baseline;
      gap: 5px;
      font-size: 0.75rem;
      line-height: 1.3;
    }
    .ui_reg_act { color: #4ade80; }
    .ui_reg_inh { color: #f87171; }
    .ui_reg_phos { color: #facc15; }
    .ui_reg_horm { color: #60a5fa; }
    .ui_reg_other { color: #cbd5e1; }
    .ui_tooltip_extra {
      margin-top: 8px;
      padding-top: 6px;
      border-top: 1px dashed #475569;
      font-size: 0.74rem;
      color: #e2e8f0;
      background: rgba(56, 189, 248, 0.08);
      border-radius: 5px;
      padding: 6px 8px;
    }

    /* Rótulo flotante de Estado Metabólico */
    #ui_state_banner {
      position: absolute;
      bottom: 20px;
      left: 50%;
      transform: translateX(-50%) translateY(40px);
      background: rgba(15, 23, 42, 0.94);
      backdrop-filter: blur(12px);
      -webkit-backdrop-filter: blur(12px);
      border: 1px solid #334155;
      border-radius: 30px;
      padding: 8px 20px;
      display: flex;
      align-items: center;
      gap: 14px;
      z-index: 60;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.6);
      opacity: 0;
      pointer-events: none;
      transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
    }
    #ui_state_banner.ui_visible {
      opacity: 1;
      pointer-events: auto;
      transform: translateX(-50%) translateY(0);
    }
    .ui_banner_text {
      font-size: 0.82rem;
      color: #f8fafc;
    }
    .ui_banner_text strong {
      color: #38bdf8;
      font-weight: 800;
    }
    .ui_banner_close {
      background: #334155;
      border: none;
      color: #ffffff;
      padding: 3px 8px;
      border-radius: 12px;
      font-size: 0.72rem;
      font-weight: 800;
      cursor: pointer;
    }
    .ui_banner_close:hover {
      background: #475569;
    }

    /* Indicador flotante de vía resaltada activa */
    #ui_highlight_banner {
      position: absolute;
      top: 14px;
      left: 50%;
      transform: translateX(-50%) translateY(-40px);
      background: rgba(2, 132, 199, 0.94);
      backdrop-filter: blur(10px);
      color: #ffffff;
      border-radius: 20px;
      padding: 6px 18px;
      display: flex;
      align-items: center;
      gap: 10px;
      z-index: 60;
      box-shadow: 0 4px 16px rgba(2, 132, 199, 0.4);
      opacity: 0;
      pointer-events: none;
      font-size: 0.82rem;
      font-weight: 800;
      transition: all 0.22s cubic-bezier(0.4, 0, 0.2, 1);
    }
    #ui_highlight_banner.ui_visible {
      opacity: 1;
      pointer-events: auto;
      transform: translateX(-50%) translateY(0);
    }
    #ui_highlight_banner button {
      background: rgba(0, 0, 0, 0.25);
      border: none;
      color: #ffffff;
      padding: 2px 7px;
      border-radius: 10px;
      font-size: 0.72rem;
      cursor: pointer;
    }

    /* Ocultar todos los elementos interactivos en impresión */
    @media print {
      .header-bar,
      #ui_sidebar_panel,
      #ui_btn_sidebar_floating,
      #ui_tooltip_card,
      #ui_state_banner,
      #ui_highlight_banner,
      [class*="ui_"],
      [id*="ui_"] {
        display: none !important;
      }
      .ui_dimmed {
        opacity: 1 !important;
        filter: none !important;
      }
    }
    """

    # Bloque HTML de interfaz de usuario
    html_ui_components = """
  <!-- PANEL LATERAL PLEGABLE: ÍNDICE DE VÍAS (16) -->
  <div id="ui_sidebar_panel">
    <div class="ui_sidebar_header">
      <div>
        <h3>Índice de Vías Metabólicas</h3>
        <p>16 rutas integradas • Clic para centrar y resaltar</p>
      </div>
      <button class="ui_sidebar_close" onclick="toggleSidebar()" title="Cerrar índice (Esc)">✕</button>
    </div>
    <div class="ui_sidebar_filter">
      <input type="text" id="ui_sidebar_search" placeholder="Filtrar vías (ej. Krebs, Urea, Lipogénesis)..." oninput="filtrarSidebarVias()">
    </div>
    <div class="ui_sidebar_list" id="ui_sidebar_list">
      <!-- Se puebla dinámicamente con JavaScript desde TABLA_VIAS -->
    </div>
  </div>

  <!-- BOTÓN FLOTANTE PARA ÍNDICE (CUANDO ESTÁ REPLEGADO) -->
  <button id="ui_btn_sidebar_floating" onclick="toggleSidebar()">
    <span>📑</span>
    <span>Índice de Vías</span>
  </button>

  <!-- BANNER FLOTANTE DE VÍA RESALTADA -->
  <div id="ui_highlight_banner">
    <span id="ui_highlight_title">Vía resaltada</span>
    <button onclick="clearPathwayHighlight()" title="Quitar resaltado (Esc)">✕ Quitar</button>
  </div>

  <!-- RÓTULO FLOTANTE DE ESTADO METABÓLICO -->
  <div id="ui_state_banner">
    <span class="ui_banner_text" id="ui_state_banner_text">Estado activo</span>
    <button class="ui_banner_close" onclick="setMetabolicState('normal')">✕ Normal</button>
  </div>

  <!-- FICHA FLOTANTE / TOOLTIP PARA ENZIMAS Y METABOLITOS -->
  <div id="ui_tooltip_card"></div>
"""

    # Encontrar el bloque exacto de <div class="controls">...</div con conteo de etiquetas anidadas
    s_ctrl = html_orig.find('<div class="controls">')
    depth = 0
    e_ctrl = s_ctrl
    for i in range(s_ctrl, len(html_orig)):
        if html_orig[i:i+4] == '<div':
            depth += 1
        elif html_orig[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                e_ctrl = i + 6
                break
    controles_originales = html_orig[s_ctrl:e_ctrl]

    nuevos_controles = """<div class="controls">
      <!-- Botón de Índice -->
      <button id="ui_btn_toggle_sidebar" onclick="toggleSidebar()" title="Índice de Vías (16)">📑 Vías</button>
      
      <!-- Modos de Estado Metabólico -->
      <div class="ui_state_group">
        <button class="ui_state_btn ui_active" id="ui_btn_state_normal" onclick="setMetabolicState('normal')" title="Mapa completo sin atenuación">Normal</button>
        <button class="ui_state_btn" id="ui_btn_state_fed" onclick="setMetabolicState('posprandial')" title="Insulina alta ↑ • Glucagón bajo ↓">🍽️ Posprandial</button>
        <button class="ui_state_btn" id="ui_btn_state_fasting" onclick="setMetabolicState('ayuno')" title="Glucagón alto ↑ • Insulina baja ↓">⚡ Ayuno</button>
      </div>

      <!-- Buscador Global -->
      <div id="ui_search_container">
        <span class="ui_search_icon">🔍</span>
        <input type="text" id="ui_search_input" placeholder="Buscar metabolito / enzima... [/]" autocomplete="off" spellcheck="false">
        <span id="ui_search_counter"></span>
        <button class="ui_search_btn" id="ui_search_prev" onclick="searchPrev()" title="Anterior (Shift+Enter)">▲</button>
        <button class="ui_search_btn" id="ui_search_next" onclick="searchNext()" title="Siguiente (Enter)">▼</button>
        <button class="ui_search_btn" id="ui_search_clear" onclick="clearSearch()" title="Limpiar (Esc)">✕</button>
      </div>

      <div style="width: 1px; height: 20px; background: #475569; margin: 0 4px;"></div>
      <button onclick="zoomOut()">−</button>
      <span id="zoomLevel">100%</span>
      <button onclick="zoomIn()">+</button>
      <button onclick="resetView()">Reset</button>
      <button style="background: #16a34a;" onclick="fitView()" title="Ajustar vista (F)">Ajustar</button>
      <div style="width: 1px; height: 20px; background: #475569; margin: 0 4px;"></div>
      <button id="btnCopiarSvg" style="background: #7c3aed;" onclick="copiarSvgModificado()">💾 Copiar SVG</button>
      <button id="btnCopiarJson" style="background: #0284c7;" onclick="copiarAjustesJson()">📋 Copiar Ajustes JSON</button>
      <button style="background: #dc2626;" onclick="resetearPosiciones()">↺ Resetear Ajustes</button>
      <div style="width: 1px; height: 20px; background: #475569; margin: 0 4px;"></div>
      <!-- Selector de Vistas / Descargas -->
      <div class="ui_dropdown_wrapper" style="position: relative; display: inline-block;">
        <button id="ui_btn_menu_views" onclick="toggleMenuViews(event)" title="Cambiar de vista o descargar PDFs" style="background: #1e293b; border: 1px solid #475569; color: #f8fafc; font-weight: 700; border-radius: 6px; padding: 5px 11px; cursor: pointer; display: inline-flex; align-items: center; gap: 5px; font-size: 0.8rem;">
          <span>🌐 Vistas / PDF</span> <span style="font-size: 8px;">▼</span>
        </button>
        <div id="ui_menu_views" style="display: none; position: absolute; right: 0; top: 100%; margin-top: 6px; background: #0f172a; border: 1px solid #334155; border-radius: 8px; box-shadow: 0 10px 25px rgba(0,0,0,0.6); min-width: 250px; z-index: 1000; padding: 6px 0; text-align: left;">
          <a href="01_mapa_ampliado_completo_25_vias.html" style="display: block; padding: 8px 14px; color: #38bdf8; text-decoration: none; font-size: 0.8rem; font-weight: 700;">🌟 01. Mapa Ampliado (25 Vías)</a>
          <a href="02_ampliacion_rutas_18_25.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">🧩 02. Ampliación Vías 18–25 (Standalone)</a>
          <a href="03_mapa_central_interactivo_17_vias.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">🗺️ 03. Mapa Central (17 Vías)</a>
          <a href="04_cuadro_temario_bloques_A_E.html" style="display: block; padding: 8px 14px; color: #e2e8f0; text-decoration: none; font-size: 0.8rem;">📋 04. Temario A–E (Metabolismo Intermediario)</a>
          <div style="height: 1px; background: #334155; margin: 4px 0;"></div>
          <a href="../versiones_impresion/01_mapa_ampliado_completo_120x90cm.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #4ade80; text-decoration: none; font-size: 0.8rem; font-weight: 700;">📥 Descargar PDF 25 Vías (120×90 cm)</a>
          <a href="../versiones_impresion/03_mapa_central_original_120x90cm.pdf" target="_blank" style="display: block; padding: 8px 14px; color: #4ade80; text-decoration: none; font-size: 0.8rem;">📥 Descargar PDF Central (120×90 cm)</a>
        </div>
      </div>
      <span id="statusStorage" style="font-size: 0.75rem; color: #a7f3d0; margin-left: 6px;"></span>
    </div>"""

    # Extraer el script original intacto
    s_idx = html_orig.find("<script>")
    e_idx = html_orig.rfind("</script>") + 9
    script_original_contenido = html_orig[s_idx+8:e_idx-9]

    # Construir el script interactivo extendido manteniendo 100% las funciones originales
    script_interactivo = f"""<script>
    // =========================================================================
    // CÓDIGO ORIGINAL CONSERVADO INTACTO (ZOOM, PAN, ARRASTRE Y LOCALSTORAGE)
    // =========================================================================
{script_original_contenido}

    // =========================================================================
    // HERRAMIENTA DE ESTUDIO INTERACTIVA (VÍAS, ÍNDICE, BÚSQUEDA, ESTADOS, TOUCH)
    // =========================================================================

    /**
     * TABLA OFICIAL DE VÍAS METABÓLICAS
     * Extraída fielmente de la leyenda y los badges existentes en el SVG.
     */
    const TABLA_VIAS = {{
      "1": {{
        numero: "1",
        id: "1",
        nombre: "Glucólisis",
        subtitulo: "Glucosa → 2 Piruvato (+2 ATP, +2 NADH)",
        grupos: ["ruta_glucolisis", "badge_via_1"],
        color: "#0284c7"
      }},
      "2": {{
        numero: "2",
        id: "2",
        nombre: "Gluconeogénesis",
        subtitulo: "Piruvato → Glucosa (4 enzimas específicas) · hepática",
        grupos: ["ruta_gluconeogenesis", "badge_via_2"],
        color: "#7c3aed"
      }},
      "3": {{
        numero: "3",
        id: "3",
        nombre: "Glucogenogénesis y glucogenólisis",
        subtitulo: "Síntesis y degradación del glucógeno",
        grupos: ["ruta_glucogeno", "badge_via_3"],
        color: "#ea580c"
      }},
      "4": {{
        numero: "4",
        id: "4",
        nombre: "Vía de las pentosas fosfato",
        subtitulo: "G6P → NADPH + Ribosa-5-P (fase oxidativa y no oxidativa)",
        grupos: ["ruta_pentosas", "badge_via_4"],
        color: "#059669"
      }},
      "5": {{
        numero: "5",
        id: "5",
        nombre: "Complejo piruvato deshidrogenasa (PDH)",
        subtitulo: "Piruvato → Acetil-CoA + CO₂ + NADH",
        grupos: ["lupa_piruvato_deshidrogenasa", "badge_via_5"],
        color: "#c2410c"
      }},
      "6": {{
        numero: "6",
        id: "6",
        nombre: "Ciclo de Krebs",
        subtitulo: "Acetil-CoA → 2 CO₂ + 3 NADH + FADH₂ + GTP",
        grupos: ["ruta_krebs", "badge_via_6"],
        color: "#d97706"
      }},
      "7": {{
        numero: "7",
        id: "7",
        nombre: "Cadena respiratoria y ATP sintasa",
        subtitulo: "Fosforilación oxidativa (acoplamiento quimiosmótico)",
        grupos: ["lupa_cadena_respiratoria", "badge_via_7"],
        color: "#16a34a"
      }},
      "8": {{
        numero: "8",
        id: "8",
        nombre: "Lanzadera malato-aspartato",
        subtitulo: "Transporte de equivalentes redox (NADH citosólico a matriz)",
        grupos: ["lupa_lanzadera_malato_aspartato", "badge_via_8"],
        color: "#0284c7"
      }},
      "8B": {{
        numero: "8B",
        id: "8B",
        nombre: "Lanzadera glicerol-3-fosfato",
        subtitulo: "DHAP ➔ G3P (Reoxidación rápida de NADH hacia FAD en MMI)",
        grupos: ["lupa_lanzadera_glicerol_p", "badge_via_8B"],
        color: "#0d9488"
      }},
      "9": {{
        numero: "9",
        id: "9",
        nombre: "β-oxidación (y lanzadera de carnitina)",
        subtitulo: "Palmitoil-CoA → 8 Acetil-CoA + FADH₂ + NADH",
        grupos: ["ruta_beta_ox", "badge_via_9"],
        color: "#b45309"
      }},
      "10": {{
        numero: "10",
        id: "10",
        nombre: "Lipogénesis (síntesis de ácidos grasos)",
        subtitulo: "Acetil-CoA → Malonil-CoA → Palmitato (FAS)",
        grupos: ["ruta_lipogenesis", "badge_via_10"],
        color: "#0d9488"
      }},
      "11": {{
        numero: "11",
        id: "11",
        nombre: "Cetogénesis",
        subtitulo: "Acetil-CoA → Acetoacetato / β-Hidroxibutirato",
        grupos: ["ruta_ceto", "badge_via_11"],
        color: "#be123c"
      }},
      "12": {{
        numero: "12",
        id: "12",
        nombre: "Síntesis de colesterol",
        subtitulo: "Acetil-CoA → HMG-CoA → Mevalonato → Colesterol",
        grupos: ["ruta_colesterol", "badge_via_12"],
        color: "#4f46e5"
      }},
      "12B": {{
        numero: "12B",
        id: "12B",
        nombre: "Destinos esqueletos carbonados AA",
        subtitulo: "Convergencia de los 20 AA en Krebs, Piruvato y Cuerpos Cetónicos",
        grupos: ["ruta_destinos_aa", "badge_via_12B"],
        color: "#6366f1"
      }},
      "13": {{
        numero: "13",
        id: "13",
        nombre: "Transaminación y desaminación oxidativa",
        subtitulo: "Recogida del grupo amino en Glutamato → NH₄⁺",
        grupos: ["ruta_transaminacion_desaminacion", "badge_via_13"],
        color: "#2563eb"
      }},
      "14": {{
        numero: "14",
        id: "14",
        nombre: "Ciclo de la urea",
        subtitulo: "NH₄⁺ + HCO₃⁻ + Aspartato → Urea",
        grupos: ["ruta_ciclo_urea", "badge_via_14"],
        color: "#0891b2"
      }},
      "15": {{
        numero: "15",
        id: "15",
        nombre: "Biosíntesis de nucleótidos (de novo y salvamento)",
        subtitulo: "Rutas convergentes sobre PRPP (purinas y pirimidinas)",
        grupos: ["ruta_sintesis_nucleotidos", "badge_via_15"],
        color: "#0284c7"
      }},
      "16": {{
        numero: "16",
        id: "16",
        nombre: "Catabolismo de nucleótidos y ácido úrico",
        subtitulo: "Degradación de purinas a Ácido Úrico y pirimidinas a β-Alanina",
        grupos: ["ruta_degradacion_nucleotidos", "badge_via_16"],
        color: "#475569"
      }},
      "17": {{
        numero: "17",
        id: "17",
        nombre: "Ciclo de Cori",
        subtitulo: "Lactato muscular anaeróbico → Sangre → Glucosa hepática (GNG) → Músculo (-4 ATP neto)",
        grupos: ["ruta_ciclo_cori", "badge_via_17"],
        color: "#be123c"
      }}
    }};

    /**
     * TABLA DE ASIGNACIÓN DE ESTADOS METABÓLICOS
     * Fácilmente editable según tus apuntes de bioquímica.
     */
    const TABLA_ESTADOS_METABOLICOS = {{
      normal: {{
        id: "normal",
        nombre: "Normal (Mapa Completo)",
        subtitulo: "Visualización de referencia",
        descripcion: "Todas las vías se muestran con su intensidad gráfica estándar.",
        activas: [],
        atenuadas: []
      }},
      posprandial: {{
        id: "posprandial",
        nombre: "Estado Posprandial",
        hormonas: "Insulina alta ↑ • Glucagón bajo ↓",
        descripcion: "Favorece utilización de glucosa, almacenamiento de glucógeno, lipogénesis, vía de pentosas y síntesis de ATP.",
        activas: ["1", "3", "4", "5", "6", "7", "10", "12"],
        atenuadas: ["2", "9", "11"]
      }},
      ayuno: {{
        id: "ayuno",
        nombre: "Estado de Ayuno",
        hormonas: "Glucagón alto ↑ • Insulina baja ↓",
        descripcion: "Favorece gluconeogénesis hepática, degradación de glucógeno, β-oxidación, cetogénesis, ciclo de la urea y ciclo de Cori.",
        activas: ["2", "3", "9", "11", "14", "17"],
        atenuadas: ["1", "10", "12"]
      }}
    }};

    /**
     * DICCIONARIO DE DATOS BIOQUÍMICOS Y ESTEQUIOMETRÍA
     * Rellenado automáticamente con el catálogo balanceado de reacciones metabólicas.
     */
    const DATOS_BIOQUIMICOS_EXTRA = __TABLA_REACCIONES_JSON__;

    // Clave de almacenamiento exclusiva para preferencias UI
    const STORAGE_PREFS_KEY = 'mapa_metabolico_ui_prefs_v1';
    let uiPrefs = {{}};
    try {{
      uiPrefs = JSON.parse(localStorage.getItem(STORAGE_PREFS_KEY) || '{{}}');
    }} catch (e) {{
      uiPrefs = {{}};
    }}

    function guardarPref(k, val) {{
      uiPrefs[k] = val;
      try {{ localStorage.setItem(STORAGE_PREFS_KEY, JSON.stringify(uiPrefs)); }} catch (e) {{}}
    }}

    // Variables de estado interactivo
    let viaResaltadaActual = null;
    let estadoMetabolicoActual = 'normal';
    let pointerDownX = 0;
    let pointerDownY = 0;
    let searchMatches = [];
    let searchMatchIndex = 0;
    let searchPulseElement = null;

    // Normalizador de texto sin acentos ni mayúsculas
    function uiNormalize(str) {{
      return (str || '')
        .normalize('NFD')
        .replace(/[\\u0300-\\u036f]/g, '')
        .toLowerCase()
        .trim();
    }}

    // =========================================================================
    // 1. RESALTADO Y ATENUACIÓN DE VÍAS
    // =========================================================================

    // Lista de todos los grupos de vía conocidos
    const TODOS_LOS_GRUPOS_VIAS = new Set();
    Object.values(TABLA_VIAS).forEach(v => {{
      v.grupos.forEach(gid => TODOS_LOS_GRUPOS_VIAS.add(gid));
    }});

    function highlightPathway(viaId, shouldZoom = false) {{
      const via = TABLA_VIAS[viaId];
      if (!via) return;

      viaResaltadaActual = viaId;

      // Actualizar clases en grupos de vías
      TODOS_LOS_GRUPOS_VIAS.forEach(gid => {{
        const el = document.getElementById(gid);
        if (el) {{
          if (via.grupos.includes(gid)) {{
            el.classList.add('ui_highlighted');
            el.classList.remove('ui_dimmed');
          }} else {{
            el.classList.add('ui_dimmed');
            el.classList.remove('ui_highlighted');
          }}
        }}
      }});

      // Atenuar conexiones inter-ruta y fondos no activos
      const cxLayer = document.getElementById('capa_conexiones_inter_ruta');
      if (cxLayer) cxLayer.classList.add('ui_dimmed');

      const mitoBio = document.getElementById('mitocondria_biologica');
      if (mitoBio) {{
        if (["2", "5", "6", "7", "8", "8B", "9", "11", "13", "14"].includes(viaId)) {{
          mitoBio.classList.remove('ui_dimmed');
        }} else {{
          mitoBio.classList.add('ui_dimmed');
        }}
      }}

      // Para Vía 2 (Gluconeogénesis), mantener el eje troncal glucolítico visible a nivel intermedio (pasos reversibles compartidos)
      const glucoTroncal = document.getElementById('ruta_glucolisis');
      if (glucoTroncal) {{
        if (viaId === "2") {{
          glucoTroncal.classList.remove('ui_dimmed');
          glucoTroncal.style.opacity = '0.55';
        }} else {{
          glucoTroncal.style.opacity = '';
        }}
      }}

      // Actualizar banner de vía resaltada
      const banner = document.getElementById('ui_highlight_banner');
      const bannerTitle = document.getElementById('ui_highlight_title');
      if (banner && bannerTitle) {{
        bannerTitle.innerHTML = `<span style="background:${{via.color}}; color:#fff; border-radius:50%; width:18px; height:18px; display:inline-flex; align-items:center; justify-content:center; font-size:10px; margin-right:6px;">${{via.numero}}</span> Vía ${{via.numero}}: ${{via.nombre}}`;
        banner.classList.add('ui_visible');
      }}

      // Actualizar ítem activo en sidebar
      document.querySelectorAll('.ui_sidebar_item').forEach(it => {{
        if (it.getAttribute('data-via') === viaId) {{
          it.classList.add('ui_active');
          it.scrollIntoView({{ block: 'nearest', behavior: 'smooth' }});
        }} else {{
          it.classList.remove('ui_active');
        }}
      }});

      if (shouldZoom) {{
        const mainEl = document.getElementById(via.grupos[0]);
        if (mainEl) zoomToElement(mainEl);
      }}
    }}

    function clearPathwayHighlight() {{
      viaResaltadaActual = null;

      const glucoTroncal = document.getElementById('ruta_glucolisis');
      if (glucoTroncal) glucoTroncal.style.opacity = '';

      // Si hay un estado metabólico activo, restaurarlo en vez de dejar todo normal
      if (estadoMetabolicoActual !== 'normal') {{
        setMetabolicState(estadoMetabolicoActual);
        const banner = document.getElementById('ui_highlight_banner');
        if (banner) banner.classList.remove('ui_visible');
        return;
      }}

      TODOS_LOS_GRUPOS_VIAS.forEach(gid => {{
        const el = document.getElementById(gid);
        if (el) {{
          el.classList.remove('ui_dimmed');
          el.classList.remove('ui_highlighted');
        }}
      }});

      const cxLayer = document.getElementById('capa_conexiones_inter_ruta');
      if (cxLayer) cxLayer.classList.remove('ui_dimmed');

      const mitoBio = document.getElementById('mitocondria_biologica');
      if (mitoBio) mitoBio.classList.remove('ui_dimmed');

      const banner = document.getElementById('ui_highlight_banner');
      if (banner) banner.classList.remove('ui_visible');

      document.querySelectorAll('.ui_sidebar_item').forEach(it => it.classList.remove('ui_active'));
    }}

    // =========================================================================
    // 2. ZOOM ANIMADO A ELEMENTO (GETBBOX CONVERSIÓN VECTORIAL)
    // =========================================================================

    function getElementSvgBounds(el) {{
      try {{
        const bbox = el.getBBox();
        const svg = document.querySelector('#panLayer svg');
        const ctm = el.getCTM();
        const svgCtm = svg ? svg.getCTM() : null;
        if (ctm && svgCtm) {{
          const m = svgCtm.inverse().multiply(ctm);
          const pt1 = svg.createSVGPoint(); pt1.x = bbox.x; pt1.y = bbox.y;
          const pt2 = svg.createSVGPoint(); pt2.x = bbox.x + bbox.width; pt2.y = bbox.y + bbox.height;
          const p1 = pt1.matrixTransform(m);
          const p2 = pt2.matrixTransform(m);
          return {{
            x: Math.min(p1.x, p2.x),
            y: Math.min(p1.y, p2.y),
            width: Math.abs(p2.x - p1.x),
            height: Math.abs(p2.y - p1.y)
          }};
        }}
        return bbox;
      }} catch (e) {{
        const rect = el.getBoundingClientRect();
        const vpRect = viewport.getBoundingClientRect();
        return {{
          x: (rect.left - vpRect.left - pointX) / scale,
          y: (rect.top - vpRect.top - pointY) / scale,
          width: rect.width / scale,
          height: rect.height / scale
        }};
      }}
    }}

    function animateViewTo(targetScale, targetX, targetY, duration = 380) {{
      const startScale = scale;
      const startX = pointX;
      const startY = pointY;
      const startTime = performance.now();

      function step(now) {{
        const elapsed = now - startTime;
        const t = Math.min(1, elapsed / duration);
        const ease = 1 - Math.pow(1 - t, 3); // Ease-out cúbico

        scale = startScale + (targetScale - startScale) * ease;
        pointX = startX + (targetX - startX) * ease;
        pointY = startY + (targetY - startY) * ease;
        updateTransform();

        if (t < 1) {{
          requestAnimationFrame(step);
        }}
      }}
      requestAnimationFrame(step);
    }}

    function zoomToElement(el, paddingFactor = 1.18) {{
      if (!el) return;
      const b = getElementSvgBounds(el);
      if (!b || b.width <= 0 || b.height <= 0) return;

      const vw = viewport.clientWidth;
      const vh = viewport.clientHeight;

      const wPadded = Math.max(b.width * paddingFactor, 500);
      const hPadded = Math.max(b.height * paddingFactor, 400);

      let targetScale = Math.min(vw / wPadded, vh / hPadded);
      targetScale = Math.max(0.28, Math.min(targetScale, 2.2));

      const cx = b.x + b.width / 2;
      const cy = b.y + b.height / 2;

      const targetX = vw / 2 - cx * targetScale;
      const targetY = vh / 2 - cy * targetScale;

      animateViewTo(targetScale, targetX, targetY);
    }}

    function toggleMenuViews(e) {{
      if (e) e.stopPropagation();
      const menu = document.getElementById('ui_menu_views');
      if (menu) {{
        menu.style.display = menu.style.display === 'block' ? 'none' : 'block';
      }}
    }}
    document.addEventListener('click', () => {{
      const menu = document.getElementById('ui_menu_views');
      if (menu) menu.style.display = 'none';
    }});

    // =========================================================================
    // 3. ÍNDICE LATERAL PLEGABLE
    // =========================================================================

    function toggleSidebar(forceState) {{
      const panel = document.getElementById('ui_sidebar_panel');
      const btn = document.getElementById('ui_btn_toggle_sidebar');
      const floatBtn = document.getElementById('ui_btn_sidebar_floating');
      if (!panel) return;

      const isOpen = forceState !== undefined ? forceState : !panel.classList.contains('ui_open');
      if (isOpen) {{
        panel.classList.add('ui_open');
        if (btn) btn.classList.add('ui_active');
        if (floatBtn) floatBtn.style.display = 'none';
        guardarPref('sidebarOpen', true);
        const searchInput = document.getElementById('ui_sidebar_search');
        if (searchInput) setTimeout(() => searchInput.focus(), 280);
      }} else {{
        panel.classList.remove('ui_open');
        if (btn) btn.classList.remove('ui_active');
        if (floatBtn) floatBtn.style.display = 'flex';
        guardarPref('sidebarOpen', false);
      }}
    }}

    function poblarSidebar() {{
      const listEl = document.getElementById('ui_sidebar_list');
      if (!listEl) return;
      listEl.innerHTML = '';

      Object.values(TABLA_VIAS).forEach(via => {{
        const item = document.createElement('div');
        item.className = 'ui_sidebar_item';
        item.setAttribute('data-via', via.id);
        item.innerHTML = `
          <div class="ui_badge_circle" style="background:${{via.color}};">${{via.numero}}</div>
          <div class="ui_item_text">
            <div class="ui_item_title">${{via.nombre}}</div>
            <div class="ui_item_desc">${{via.subtitulo}}</div>
          </div>
        `;
        item.addEventListener('click', () => {{
          highlightPathway(via.id, true);
        }});
        listEl.appendChild(item);
      }});
    }}

    function filtrarSidebarVias() {{
      const q = uiNormalize(document.getElementById('ui_sidebar_search')?.value || '');
      document.querySelectorAll('.ui_sidebar_item').forEach(it => {{
        const viaId = it.getAttribute('data-via');
        const via = TABLA_VIAS[viaId];
        if (!via) return;
        const match = uiNormalize(via.nombre).includes(q) ||
                      uiNormalize(via.subtitulo).includes(q) ||
                      via.numero.toLowerCase().includes(q);
        it.style.display = match ? 'flex' : 'none';
      }});
    }}

    // =========================================================================
    // 4. BUSCADOR GLOBAL EN TODO EL SVG (METABOLITOS, ENZIMAS Y TEXTOS)
    // =========================================================================

    const INDICE_BUSQUEDA = [];

    function construirIndiceBusqueda() {{
      INDICE_BUSQUEDA.length = 0;
      const svg = document.querySelector('#panLayer svg');
      if (!svg) return;

      // 1. Metabolitos (m_*)
      svg.querySelectorAll('[id^="m_"]').forEach(el => {{
        const textArr = Array.from(el.querySelectorAll('text')).map(t => t.textContent.trim()).filter(Boolean);
        const formulaAtoms = new Set(['O', 'H', 'OH', 'HO', 'CH₂OH', 'Ⓟ', 'O-PO₃²⁻', 'NH₃⁺', 'COO⁻', 'CH₂', 'CH₃']);
        const realNames = textArr.filter(t => !formulaAtoms.has(t));
        const nombre = realNames[0] || textArr[0] || el.id;
        const textoCompleto = [nombre, ...textArr].join(' ');
        INDICE_BUSQUEDA.push({{
          tipo: 'Metabolito',
          nombre: nombre,
          textoNorm: uiNormalize(textoCompleto),
          elemento: el
        }});
      }});

      // 2. Enzimas y Reacciones (rx_*)
      svg.querySelectorAll('[id^="rx_"]').forEach(el => {{
        const textArr = Array.from(el.querySelectorAll('text')).map(t => t.textContent.trim()).filter(Boolean);
        const nombre = textArr[0] || el.id;
        const textoCompleto = textArr.join(' ');
        INDICE_BUSQUEDA.push({{
          tipo: 'Enzima / Reacción',
          nombre: nombre,
          textoNorm: uiNormalize(textoCompleto),
          elemento: el
        }});
      }});

      // 3. Lupas y Paneles de Detalle (lupa_*)
      svg.querySelectorAll('[id^="lupa_"]').forEach(el => {{
        const textArr = Array.from(el.querySelectorAll('text')).map(t => t.textContent.trim()).filter(Boolean);
        const nombre = textArr[0] || el.id;
        const textoCompleto = textArr.join(' ');
        INDICE_BUSQUEDA.push({{
          tipo: 'Panel de Detalle',
          nombre: nombre,
          textoNorm: uiNormalize(textoCompleto),
          elemento: el
        }});
      }});

      // 4. Badges de vía
      svg.querySelectorAll('.badge-via').forEach(el => {{
        const textArr = Array.from(el.querySelectorAll('text')).map(t => t.textContent.trim()).filter(Boolean);
        INDICE_BUSQUEDA.push({{
          tipo: 'Insignia de Vía',
          nombre: 'Vía ' + (textArr[0] || ''),
          textoNorm: uiNormalize('via ' + (textArr[0] || '')),
          elemento: el
        }});
      }});
    }}

    function ejecutarBusqueda() {{
      const input = document.getElementById('ui_search_input');
      const counter = document.getElementById('ui_search_counter');
      if (!input || !counter) return;

      const q = uiNormalize(input.value);

      if (searchPulseElement) {{
        searchPulseElement.classList.remove('ui_search_pulse');
        searchPulseElement = null;
      }}

      if (!q || q.length < 2) {{
        searchMatches = [];
        searchMatchIndex = 0;
        counter.textContent = '';
        return;
      }}

      // Filtrar coincidencias y deduplicar por elemento contenedor
      const seen = new Set();
      searchMatches = [];
      INDICE_BUSQUEDA.forEach(item => {{
        if (item.textoNorm.includes(q) && !seen.has(item.elemento)) {{
          seen.add(item.elemento);
          searchMatches.push(item);
        }}
      }});

      if (searchMatches.length > 0) {{
        searchMatchIndex = 0;
        irACoincidencia(searchMatchIndex);
      }} else {{
        counter.textContent = '0 de 0';
      }}
    }}

    function irACoincidencia(idx) {{
      const counter = document.getElementById('ui_search_counter');
      if (searchMatches.length === 0) return;

      searchMatchIndex = (idx + searchMatches.length) % searchMatches.length;
      const match = searchMatches[searchMatchIndex];

      if (counter) {{
        counter.textContent = `${{searchMatchIndex + 1}} de ${{searchMatches.length}}`;
      }}

      if (searchPulseElement) {{
        searchPulseElement.classList.remove('ui_search_pulse');
      }}

      searchPulseElement = match.elemento;
      searchPulseElement.classList.add('ui_search_pulse');

      zoomToElement(match.elemento, 2.2);
    }}

    function searchNext() {{
      if (searchMatches.length > 0) irACoincidencia(searchMatchIndex + 1);
    }}

    function searchPrev() {{
      if (searchMatches.length > 0) irACoincidencia(searchMatchIndex - 1);
    }}

    function clearSearch() {{
      const input = document.getElementById('ui_search_input');
      const counter = document.getElementById('ui_search_counter');
      if (input) input.value = '';
      if (counter) counter.textContent = '';
      if (searchPulseElement) {{
        searchPulseElement.classList.remove('ui_search_pulse');
        searchPulseElement = null;
      }}
      searchMatches = [];
      searchMatchIndex = 0;
    }}

    // =========================================================================
    // 5. FICHA FLOTANTE AL PASAR EL RATÓN (TOOLTIP PARA RX_* Y M_*)
    // =========================================================================

    const tooltipEl = document.getElementById('ui_tooltip_card');

    function buscarViaDeElemento(el) {{
      const parentRuta = el.closest('[id^="ruta_"], [id^="lupa_"]');
      if (!parentRuta) return null;
      const rid = parentRuta.id;
      for (const via of Object.values(TABLA_VIAS)) {{
        if (via.grupos.includes(rid)) return via;
      }}
      return null;
    }}

    let isTooltipPinned = false;
    let pinnedElement = null;

    function unpinTooltip() {{
      isTooltipPinned = false;
      pinnedElement = null;
      if (tooltipEl) {{
        tooltipEl.classList.remove('ui_tt_pinned');
        tooltipEl.classList.remove('ui_visible');
      }}
    }}

    function pinTooltip(el, mouseX, mouseY) {{
      if (!tooltipEl) return;
      isTooltipPinned = true;
      pinnedElement = el;
      mostrarTooltip(el, mouseX, mouseY, true);
    }}

    function mostrarTooltip(el, mouseX, mouseY, pinned = false) {{
      if (!tooltipEl || (isPanning && !isTooltipPinned) || arrastrandoElemento) return;
      if (isTooltipPinned && !pinned) return;

      const isMetabolito = el.id && el.id.startsWith('m_');
      const isEnzima = el.id && el.id.startsWith('rx_');
      if (!isMetabolito && !isEnzima) return;

      const via = buscarViaDeElemento(el);
      const textArr = Array.from(el.querySelectorAll('text')).map(t => t.textContent.trim()).filter(Boolean);

      let htmlContenido = '';
      const closeBtnHtml = pinned ? `<button class="ui_tt_close_btn" onclick="unpinTooltip()" title="Cerrar ficha (Esc)">✕</button>` : '';
      const pinHintHtml = !pinned 
        ? `<div class="ui_tt_pin_hint">Clic para fijar ficha y ver ecuación completa</div>` 
        : `<div class="ui_tt_pin_hint" style="color:#38bdf8;">Ficha fijada • Presiona Esc o clica fuera para cerrar</div>`;

      // CASO 1: REACCIÓN / ENZIMA CON ESTEQUIOMETRÍA
      if (isEnzima) {{
        const rxData = (typeof DATOS_BIOQUIMICOS_EXTRA !== 'undefined') ? DATOS_BIOQUIMICOS_EXTRA[el.id] : null;
        const colorVia = via ? via.color : '#0284c7';
        const nombreVia = via ? `Vía ${{via.numero}}: ${{via.nombre}}` : (rxData ? rxData.via : 'Vía Metabólica');

        if (rxData) {{
          const ecBadge = rxData.ec ? `<span class="ui_tt_badge_ec">${{rxData.ec}}</span>` : '';
          htmlContenido = `
            ${{closeBtnHtml}}
            <div class="ui_tt_header_row">
              <span class="ui_tt_badge_via" style="background:${{colorVia}}">${{nombreVia}}</span>
              ${{ecBadge}}
              <span style="font-size:9.5px; color:#94a3b8; margin-left:auto;">${{rxData.compartimento || ''}}</span>
            </div>
            <h4 style="margin:0 0 6px 0; font-size:1.02rem; font-weight:800; color:#f8fafc;">${{rxData.enzima}}</h4>
            <div class="ui_tt_eq_box">
              <div class="ui_tt_eq_label">ECUACIÓN QUÍMICA BALANCEADA:</div>
              <div class="ui_tt_eq_text">${{rxData.ecuacion}}</div>
            </div>
            <div class="ui_tt_grid">
              <div class="ui_tt_grid_row"><span class="ui_tt_label">Sustratos:</span> <span class="ui_tt_val">${{rxData.sustratos.join(', ')}}</span></div>
              <div class="ui_tt_grid_row"><span class="ui_tt_label">Productos:</span> <span class="ui_tt_val" style="color:#38bdf8; font-weight:700;">${{rxData.productos.join(', ')}}</span></div>
              ${{rxData.coproductos ? `<div class="ui_tt_grid_row"><span class="ui_tt_label">Coproductos:</span> <span class="ui_tt_val">${{rxData.coproductos}}</span></div>` : ''}}
              ${{rxData.deltaG ? `<div class="ui_tt_grid_row"><span class="ui_tt_label">Termodinámica:</span> <span class="ui_tt_val">${{rxData.deltaG}}</span></div>` : ''}}
            </div>
            ${{rxData.regulacion ? `<div class="ui_tt_reg_box"><strong style="color:#fbbf24;">Regulación:</strong> ${{rxData.regulacion}}</div>` : ''}}
            ${{rxData.relevancia ? `<div style="margin-top:6px; font-size:10px; color:#94a3b8; line-height:1.3;">${{rxData.relevancia}}</div>` : ''}}
            ${{pinHintHtml}}
          `;
        }} else {{
          // Reacción sin ficha estequiométrica específica: extraer del SVG
          let titulo = textArr[0] || el.id;
          let subtitulo = '';
          let filasHtml = [];

          textArr.slice(1).forEach(t => {{
            if (t.includes('EC ')) {{
              subtitulo = t;
            }} else if (t.startsWith('(+)')) {{
              filasHtml.push(`<div class="ui_reg_row ui_reg_act"><span>✓</span> <span>${{t}}</span></div>`);
            }} else if (t.startsWith('(-)')) {{
              filasHtml.push(`<div class="ui_reg_row ui_reg_inh"><span>✗</span> <span>${{t}}</span></div>`);
            }} else if (t.startsWith('(P)')) {{
              filasHtml.push(`<div class="ui_reg_row ui_reg_phos"><span>Ⓟ</span> <span>${{t}}</span></div>`);
            }} else if (t.includes('[Hormonal]')) {{
              filasHtml.push(`<div class="ui_reg_row ui_reg_horm"><span>⚡</span> <span>${{t}}</span></div>`);
            }} else {{
              filasHtml.push(`<div class="ui_reg_row ui_reg_other"><span>•</span> <span>${{t}}</span></div>`);
            }}
          }});

          htmlContenido = `
            ${{closeBtnHtml}}
            <div class="ui_tt_header_row">
              <span class="ui_tt_badge_via" style="background:${{colorVia}}">${{nombreVia}}</span>
              ${{subtitulo ? `<span class="ui_tt_badge_ec">${{subtitulo}}</span>` : ''}}
            </div>
            <div class="ui_tooltip_title">${{titulo}}</div>
            ${{filasHtml.length > 0 ? `<div class="ui_tooltip_rows">${{filasHtml.join('')}}</div>` : ''}}
            ${{pinHintHtml}}
          `;
        }}
      }} else {{
        // CASO 2: METABOLITO
        const formulaAtoms = new Set(['O', 'H', 'OH', 'HO', 'CH₂OH', 'Ⓟ', 'O-PO₃²⁻', 'NH₃⁺', 'COO⁻', 'CH₂', 'CH₃']);
        const realNames = textArr.filter(t => !formulaAtoms.has(t) && !t.startsWith('[') && !t.endsWith(']'));
        let titulo = realNames[0] || textArr[0] || el.id;
        const carbonTag = textArr.find(t => t.startsWith('[') && t.endsWith(']'));
        const colorVia = via ? via.color : '#0284c7';
        const nombreVia = via ? `Vía ${{via.numero}}: ${{via.nombre}}` : 'Metabolito Intermediario';

        let filasHtml = [];
        textArr.forEach(t => {{
          if (t !== titulo && t !== carbonTag && !formulaAtoms.has(t)) {{
            filasHtml.push(`<div class="ui_reg_row ui_reg_other">• ${{t}}</div>`);
          }}
        }});

        htmlContenido = `
          ${{closeBtnHtml}}
          <div class="ui_tt_header_row">
            <span class="ui_tt_badge_via" style="background:${{colorVia}}">${{nombreVia}}</span>
            ${{carbonTag ? `<span class="ui_tt_badge_ec" style="background:#0f766e; border-color:#14b8a6; color:#ccfbf1;">${{carbonTag}} Carbonos</span>` : ''}}
          </div>
          <div class="ui_tooltip_title">${{titulo}}</div>
          ${{filasHtml.length > 0 ? `<div class="ui_tooltip_rows">${{filasHtml.join('')}}</div>` : ''}}
          ${{pinHintHtml}}
        `;
      }}

      tooltipEl.innerHTML = htmlContenido;
      if (pinned) {{
        tooltipEl.classList.add('ui_tt_pinned');
      }} else {{
        tooltipEl.classList.remove('ui_tt_pinned');
      }}

      tooltipEl.classList.add('ui_visible');

      // Posicionamiento inteligente con clamping
      const cardRect = tooltipEl.getBoundingClientRect();
      let left = mouseX + 16;
      let top = mouseY + 16;

      if (left + cardRect.width > window.innerWidth - 14) {{
        left = mouseX - cardRect.width - 16;
      }}
      if (top + cardRect.height > window.innerHeight - 14) {{
        top = mouseY - cardRect.height - 16;
      }}
      if (left < 14) left = 14;
      if (top < 14) top = 14;

      tooltipEl.style.left = `${{left}}px`;
      tooltipEl.style.top = `${{top}}px`;
    }}

    function ocultarTooltip() {{
      if (tooltipEl && !isTooltipPinned) tooltipEl.classList.remove('ui_visible');
    }}

    // =========================================================================
    // 6. MODOS DE ESTADO METABÓLICO (POSPRANDIAL / AYUNO / NORMAL)
    // =========================================================================

    function setMetabolicState(stateId) {{
      const st = TABLA_ESTADOS_METABOLICOS[stateId] || TABLA_ESTADOS_METABOLICOS.normal;
      estadoMetabolicoActual = st.id;

      // Actualizar botones de estado
      document.querySelectorAll('.ui_state_btn').forEach(btn => {{
        if (btn.id === `ui_btn_state_${{st.id === 'posprandial' ? 'fed' : st.id === 'ayuno' ? 'fasting' : 'normal'}}`) {{
          btn.classList.add('ui_active');
        }} else {{
          btn.classList.remove('ui_active');
        }}
      }});

      const banner = document.getElementById('ui_state_banner');
      const bannerText = document.getElementById('ui_state_banner_text');

      if (st.id === 'normal') {{
        // Restaurar visibilidad total
        TODOS_LOS_GRUPOS_VIAS.forEach(gid => {{
          const el = document.getElementById(gid);
          if (el) {{
            el.classList.remove('ui_dimmed');
            el.classList.remove('ui_state_active');
          }}
        }});
        const cxLayer = document.getElementById('capa_conexiones_inter_ruta');
        if (cxLayer) cxLayer.classList.remove('ui_dimmed');
        const mitoBio = document.getElementById('mitocondria_biologica');
        if (mitoBio) mitoBio.classList.remove('ui_dimmed');
        if (banner) banner.classList.remove('ui_visible');
        return;
      }}

      // Obtener conjuntos de grupos activos y atenuados
      const gruposActivos = new Set();
      st.activas.forEach(vid => {{
        const v = TABLA_VIAS[vid];
        if (v) v.grupos.forEach(gid => gruposActivos.add(gid));
      }});

      const gruposAtenuados = new Set();
      st.atenuadas.forEach(vid => {{
        const v = TABLA_VIAS[vid];
        if (v) v.grupos.forEach(gid => gruposAtenuados.add(gid));
      }});

      TODOS_LOS_GRUPOS_VIAS.forEach(gid => {{
        const el = document.getElementById(gid);
        if (el) {{
          if (gruposActivos.has(gid)) {{
            el.classList.add('ui_state_active');
            el.classList.remove('ui_dimmed');
          }} else if (gruposAtenuados.has(gid)) {{
            el.classList.add('ui_dimmed');
            el.classList.remove('ui_state_active');
          }} else {{
            // Vías no participantes directas se atenúan suavemente
            el.classList.add('ui_dimmed');
            el.classList.remove('ui_state_active');
          }}
        }}
      }});

      // Mostrar banner explicativo
      if (banner && bannerText) {{
        bannerText.innerHTML = `<strong>${{st.nombre}} (${{st.hormonas}})</strong> • ${{st.descripcion}}`;
        banner.classList.add('ui_visible');
      }}
    }}

    // =========================================================================
    // 7. DISTINCIÓN CLIC VS ARRASTRE Y SOPORTE TÁCTIL (POINTER / TOUCH EVENTS)
    // =========================================================================

    function manejarClicEnLienzo(e, clientX, clientY) {{
      const target = document.elementFromPoint(clientX, clientY);
      if (!target) return;

      // Clic en badge de vía
      const badge = target.closest('.badge-via');
      if (badge) {{
        const viaEntry = Object.values(TABLA_VIAS).find(v => v.grupos.includes(badge.id));
        if (viaEntry) {{
          highlightPathway(viaEntry.id, false);
          return;
        }}
      }}

      // Clic en ruta o panel
      const ruta = target.closest('[id^="ruta_"], [id^="lupa_"]');
      if (ruta) {{
        const viaEntry = Object.values(TABLA_VIAS).find(v => v.grupos.includes(ruta.id));
        if (viaEntry) {{
          highlightPathway(viaEntry.id, false);
          return;
        }}
      }}

      // Clic en enzima o metabolito -> FIJAR FICHA ESTEQUIOMÉTRICA
      const targetRx = target.closest('[id^="rx_"], [id^="m_"]');
      if (targetRx) {{
        pinTooltip(targetRx, clientX, clientY);
        return;
      }}

      // Clic fuera de reacción y fuera de tooltip -> desanclar ficha
      if (!target.closest('#ui_tooltip_card')) {{
        unpinTooltip();
      }}

      // Clic en fondo o espacio vacío
      if (target.tagName === 'svg' || target.id === 'viewport' || target.id === 'panLayer' || target.tagName === 'rect') {{
        clearPathwayHighlight();
      }}
    }}

    // Interceptar puntero para registrar inicio
    viewport.addEventListener('mousedown', (e) => {{
      pointerDownX = e.clientX;
      pointerDownY = e.clientY;
    }}, true);

    viewport.addEventListener('mouseup', (e) => {{
      const dist = Math.hypot(e.clientX - pointerDownX, e.clientY - pointerDownY);
      if (dist <= 4 && !arrastrandoElemento) {{
        manejarClicEnLienzo(e, e.clientX, e.clientY);
      }}
    }}, true);

    // Eventos de ratón para el tooltip
    viewport.addEventListener('mousemove', (e) => {{
      if (isPanning || arrastrandoElemento) {{
        if (!isTooltipPinned) ocultarTooltip();
        return;
      }}
      if (isTooltipPinned) return; // Si está fijada, no la movemos con el cursor
      const target = e.target.closest('[id^="m_"], [id^="rx_"]');
      if (target) {{
        mostrarTooltip(target, e.clientX, e.clientY, false);
      }} else {{
        ocultarTooltip();
      }}
    }});

    viewport.addEventListener('mouseleave', () => {{
      if (!isTooltipPinned) ocultarTooltip();
    }});

    // Soporte táctil completo (1 dedo pan, 2 dedos pellizco para zoom)
    let touchIsPanning = false;
    let touchPinching = false;
    let touchStartDist = 0;
    let touchStartScale = 1;
    let touchMidX = 0;
    let touchMidY = 0;
    let touchStartX = 0;
    let touchStartY = 0;
    let touchDownTime = 0;

    viewport.addEventListener('touchstart', (e) => {{
      ocultarTooltip();
      if (e.touches.length === 1) {{
        const t = e.touches[0];
        touchStartX = t.clientX - pointX;
        touchStartY = t.clientY - pointY;
        pointerDownX = t.clientX;
        pointerDownY = t.clientY;
        touchDownTime = performance.now();
        touchIsPanning = true;
        touchPinching = false;
      }} else if (e.touches.length === 2) {{
        touchIsPanning = false;
        touchPinching = true;
        const t1 = e.touches[0];
        const t2 = e.touches[1];
        touchStartDist = Math.hypot(t2.clientX - t1.clientX, t2.clientY - t1.clientY);
        touchStartScale = scale;
        const rect = viewport.getBoundingClientRect();
        touchMidX = (t1.clientX + t2.clientX) / 2 - rect.left;
        touchMidY = (t1.clientY + t2.clientY) / 2 - rect.top;
      }}
    }}, {{ passive: false }});

    viewport.addEventListener('touchmove', (e) => {{
      if (touchPinching && e.touches.length === 2) {{
        e.preventDefault();
        const t1 = e.touches[0];
        const t2 = e.touches[1];
        const curDist = Math.hypot(t2.clientX - t1.clientX, t2.clientY - t1.clientY);
        if (touchStartDist > 0) {{
          const factor = curDist / touchStartDist;
          const targetScale = Math.max(0.15, Math.min(5, touchStartScale * factor));
          const prevScale = scale;
          scale = targetScale;
          pointX = touchMidX - (touchMidX - pointX) * (scale / prevScale);
          pointY = touchMidY - (touchMidY - pointY) * (scale / prevScale);
          updateTransform();
        }}
      }} else if (touchIsPanning && e.touches.length === 1) {{
        e.preventDefault();
        const t = e.touches[0];
        pointX = t.clientX - touchStartX;
        pointY = t.clientY - touchStartY;
        updateTransform();
      }}
    }}, {{ passive: false }});

    viewport.addEventListener('touchend', (e) => {{
      if (e.touches.length === 0) {{
        if (touchIsPanning && !touchPinching) {{
          const t = e.changedTouches[0];
          const dist = Math.hypot(t.clientX - pointerDownX, t.clientY - pointerDownY);
          const elapsed = performance.now() - touchDownTime;
          if (dist <= 6 && elapsed < 320) {{
            manejarClicEnLienzo(e, t.clientX, t.clientY);
          }}
        }}
        touchIsPanning = false;
        touchPinching = false;
      }} else if (e.touches.length === 1) {{
        touchPinching = false;
        touchIsPanning = true;
        const t = e.touches[0];
        touchStartX = t.clientX - pointX;
        touchStartY = t.clientY - pointY;
      }}
    }});

    // =========================================================================
    // 8. ATAJOS DE TECLADO Y PARÁMETROS URL
    // =========================================================================

    window.addEventListener('keydown', (e) => {{
      const tag = document.activeElement ? document.activeElement.tagName.toLowerCase() : '';
      const isInput = tag === 'input' || tag === 'textarea';

      if (e.key === 'Escape') {{
        unpinTooltip();
        ocultarTooltip();
        if (isInput) {{
          document.activeElement.blur();
        }}
        if (searchMatches.length > 0 || (document.getElementById('ui_search_input')?.value)) {{
          clearSearch();
        }} else if (viaResaltadaActual) {{
          clearPathwayHighlight();
        }} else if (estadoMetabolicoActual !== 'normal') {{
          setMetabolicState('normal');
        }} else {{
          toggleSidebar(false);
        }}
        return;
      }}

      if (isInput) {{
        if (e.key === 'Enter') {{
          e.preventDefault();
          if (e.shiftKey) searchPrev();
          else searchNext();
        }}
        return;
      }}

      if (e.key === '/') {{
        e.preventDefault();
        const inp = document.getElementById('ui_search_input');
        if (inp) {{
          inp.focus();
          inp.select();
        }}
      }} else if (e.key === 'f' || e.key === 'F') {{
        e.preventDefault();
        fitView();
      }}
    }});

    // Listeners del buscador
    document.getElementById('ui_search_input')?.addEventListener('input', ejecutarBusqueda);

    // Inicialización interactiva al cargar la página
    window.addEventListener('load', () => {{
      poblarSidebar();
      construirIndiceBusqueda();

      // Parámetros de URL
      const params = new URLSearchParams(window.location.search);
      const viaParam = params.get('via') || params.get('highlight');
      const searchParam = params.get('search');
      const stateParam = params.get('state');
      const sidebarParam = params.get('sidebar');

      if (sidebarParam === '1' || sidebarParam === 'open' || uiPrefs.sidebarOpen) {{
        toggleSidebar(true);
      }}
      if (viaParam && TABLA_VIAS[viaParam]) {{
        setTimeout(() => highlightPathway(viaParam, true), 200);
      }}
      if (searchParam) {{
        const inp = document.getElementById('ui_search_input');
        if (inp) {{
          inp.value = searchParam;
          setTimeout(ejecutarBusqueda, 250);
        }}
      }}
      if (stateParam && TABLA_ESTADOS_METABOLICOS[stateParam]) {{
        setTimeout(() => setMetabolicState(stateParam), 150);
      }}
      const hoverParam = params.get('hover');
      if (hoverParam) {{
        const el = document.getElementById(hoverParam);
        if (el) {{
          zoomToElement(el, 2.5);
          setTimeout(() => {{
            const rect = el.getBoundingClientRect();
            mostrarTooltip(el, rect.left + rect.width / 2, rect.top + rect.height / 2);
          }}, 400);
        }}
      }}
    }});
  </script>"""

    # Ensamblar el nuevo HTML
    # 1. Insertar CSS de UI justo antes de </style>
    style_close_idx = html_orig.find("</style>")
    html_step1 = html_orig[:style_close_idx] + css_ui + html_orig[style_close_idx:]

    # 2. Reemplazar los controles de la cabecera
    html_step2 = html_step1.replace(controles_originales, nuevos_controles)

    # 3. Insertar los componentes UI dentro de #viewport antes de #panLayer
    panlayer_str = '<div id="panLayer">'
    pan_idx = html_step2.find(panlayer_str)
    html_step3 = html_step2[:pan_idx] + html_ui_components + html_step2[pan_idx:]

    # 4. Reemplazar el bloque <script>...</script> por el script extendido
    s_idx = html_step3.find("<script>")
    e_idx = html_step3.rfind("</script>") + 9
    html_final = html_step3[:s_idx] + script_interactivo + html_step3[e_idx:]
    html_final = html_final.replace("__TABLA_REACCIONES_JSON__", json.dumps(TABLA_REACCIONES_DATA, ensure_ascii=False))

    # 5. Escribir archivo prueba_visual_interactiva.html y su alias numerado
    print(f"2. Guardando archivo interactivo: {RUTA_INTERACTIVA}")
    with open(RUTA_INTERACTIVA, "w", encoding="utf-8") as f:
        f.write(html_final)
    ruta_central_num = os.path.join(DIR_HTML, "03_mapa_central_interactivo_17_vias.html")
    with open(ruta_central_num, "w", encoding="utf-8") as f:
        f.write(html_final)
    print(f"   ✓ Archivo escrito con éxito ({os.path.getsize(RUTA_INTERACTIVA):,} bytes)")
    print(f"   ✓ Copia numerada guardada en: {ruta_central_num}")

    # 6. Verificación matemática estricta: Demostrar que el contenido del SVG quedó 100% intacto
    print("\n3. Verificación de integridad estricta (Original vs Copia Interactiva):")
    with open(RUTA_INTERACTIVA, "r", encoding="utf-8") as f:
        check_html = f.read()

    pos = check_html.find(svg_completo_orig)
    if pos != -1:
        print(f"   ✓ DEMOSTRACIÓN EXITOSA: Los {len(svg_completo_orig):,} bytes del SVG original")
        print("     están presentes de forma 100% EXACTA E IDÉNTICA bit a bit dentro de la copia.")
        print("     Ningún id, nodo, coordenada, texto ni color del SVG fue alterado.")
    else:
        print("   ✗ ERROR: El interior del SVG no coincide exactamente.")
        sys.exit(1)


if __name__ == "__main__":
    construir_interactiva()
