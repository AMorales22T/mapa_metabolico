# =============================================================================
# MÓDULO DE REVISIÓN: Constructores Visuales de Nodos, Badges y Reacciones
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 159 a 338 de 4188)
# Descripción      : Funciones nodo_libre, nodo_aa, badge_clinico, badge_via, etiqueta_regulacion y reaccion_libre.
# =============================================================================

def nodo_libre(x, y, nombre, carbonos, svg_mol, id_nodo="", text_right=True, dx=135, dy=24, text_pos="side", detalle=""):
    """Metabolito 100% libre sin tarjetas ni globos."""
    if text_pos == "top":
        align = 'text-anchor="middle"'
        tx = dx if dx != 135 else 70
        ty = dy if dy != 24 else -22
        txt_det = f'<text x="{tx}" y="{ty + 30}" fill="#64748b" font-size="9.5" font-weight="600" font-family="\'Inter\', sans-serif" {align}>{detalle}</text>' if detalle else ""
        return f"""
        <!-- Metabolito Libre: {nombre} -->
        <g id="{id_nodo}" data-arrastrable="1" transform="translate({x}, {y})">
          <g>{svg_mol}</g>
          <text x="{tx}" y="{ty}" fill="#0f172a" font-size="14.5" font-weight="800" font-family="'Inter', sans-serif" {align}>{nombre}</text>
          <text x="{tx}" y="{ty + 16}" fill="#ea580c" font-size="11.5" font-weight="700" font-family="'JetBrains Mono', monospace" {align}>[{carbonos}]</text>
          {txt_det}
        </g>
        """
    elif text_pos == "bottom":
        align = 'text-anchor="middle"'
        tx = dx if dx != 135 else 50
        ty = dy if dy != 24 else 135
        txt_det = f'<text x="{tx}" y="{ty + 28}" fill="#64748b" font-size="9.5" font-weight="600" font-family="\'Inter\', sans-serif" {align}>{detalle}</text>' if detalle else ""
        return f"""
        <!-- Metabolito Libre: {nombre} -->
        <g id="{id_nodo}" data-arrastrable="1" transform="translate({x}, {y})">
          <g>{svg_mol}</g>
          <text x="{tx}" y="{ty}" fill="#0f172a" font-size="14.5" font-weight="800" font-family="'Inter', sans-serif" {align}>{nombre}</text>
          <text x="{tx}" y="{ty + 15}" fill="#ea580c" font-size="11.5" font-weight="700" font-family="'JetBrains Mono', monospace" {align}>[{carbonos}]</text>
          {txt_det}
        </g>
        """
    if text_right:
        tx = dx
    else:
        tx = dx if dx != 135 else -20
    align = "" if text_right else 'text-anchor="end"'
    txt_det = f'<text x="{tx}" y="{dy + 32}" fill="#64748b" font-size="9.5" font-weight="600" font-family="\'Inter\', sans-serif" {align}>{detalle}</text>' if detalle else ""
    return f"""
    <!-- Metabolito Libre: {nombre} -->
    <g id="{id_nodo}" data-arrastrable="1" transform="translate({x}, {y})">
      <g>{svg_mol}</g>
      <text x="{tx}" y="{dy}" fill="#0f172a" font-size="15" font-weight="800" font-family="'Inter', sans-serif" {align}>{nombre}</text>
      <text x="{tx}" y="{dy + 17}" fill="#ea580c" font-size="11.5" font-weight="700" font-family="'JetBrains Mono', monospace" {align}>[{carbonos}]</text>
      {txt_det}
    </g>
    """


def nodo_aa(x, y, nombre, carbonos, clasificacion="glu", detalle="", id_nodo=""):
    """
    Rótulo tipográfico orgánico para aminoácidos sin cajas contenedoras ni puntos de carbono.
    Clasificación: glu (verde), ceto (rojo), mixto (púrpura).
    """
    colores = {
        "glu": {"dot": "#16a34a", "txt": "#14532d"},
        "ceto": {"dot": "#dc2626", "txt": "#881337"},
        "mixto": {"dot": "#9333ea", "txt": "#581c87"}
    }
    cfg = colores.get(clasificacion, colores["glu"])
    detalle_svg = f'<text x="0" y="27" fill="#64748b" font-size="9" font-weight="600" font-family="\'Inter\', sans-serif">{detalle}</text>' if detalle else ""
    id_attr = f'id="{id_nodo}"' if id_nodo else ""

    return f"""
    <!-- AA: {nombre} -->
    <g {id_attr} data-arrastrable="1" transform="translate({x}, {y})">
      <circle cx="-10" cy="-4" r="4.5" fill="{cfg['dot']}" />
      <text x="0" y="0" fill="{cfg['txt']}" font-size="13.5" font-weight="800" font-family="'Inter', sans-serif">{nombre}</text>
      <text x="0" y="15" fill="#ea580c" font-size="10.5" font-weight="800" font-family="'JetBrains Mono', monospace">[{carbonos}]</text>
      {detalle_svg}
    </g>
    """


def badge_clinico(x, y, texto, es_alerta=True, rx=11):
    """
    Píldora reducida para patologías o cofactores anclada a diana.
    """
    fill = "#fee2e2" if es_alerta else "#e0e7ff"
    stroke = "#dc2626" if es_alerta else "#4f46e5"
    txt_col = "#991b1b" if es_alerta else "#312e81"
    ancho = max(len(texto) * 6.8 + 20, 95)

    return f"""
    <!-- Badge clínico: {texto} -->
    <g data-arrastrable="1" transform="translate({x}, {y})">
      <rect x="0" y="0" width="{ancho}" height="22" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="1.2" opacity="0.95"/>
      <text x="{ancho/2}" y="15" fill="{txt_col}" font-size="9.5" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">{texto}</text>
    </g>
    """


def badge_via(n, x, y, id_badge=None):
    """Badge circular numerado de vía metabólica para la leyenda (arrastrable)."""
    bid = id_badge or f"badge_via_{str(n).replace(' ', '_')}"
    return f"""
    <g id="{bid}" data-arrastrable="1" class="badge-via" transform="translate({x}, {y})" style="cursor: grab;">
      <circle cx="0" cy="0" r="13" fill="#0284c7" stroke="#ffffff" stroke-width="2.2" />
      <text x="0" y="4.5" fill="#ffffff" font-size="11" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{n}</text>
    </g>
    """

def badge_rodeo_gng(num_rodeo, x, y, id_badge=None):
    """Badge distintivo para los 3 rodeos (bypasses) de la gluconeogénesis."""
    bid = id_badge or f"badge_rodeo_gng_{num_rodeo}"
    return f"""
    <g id="{bid}" data-arrastrable="1" class="badge-rodeo-gng" transform="translate({x}, {y})">
      <rect x="-38" y="-12" width="76" height="24" rx="6" fill="#7c3aed" stroke="#ffffff" stroke-width="1.8" filter="drop-shadow(0 2px 4px rgba(0,0,0,0.2))"/>
      <text x="0" y="4" fill="#ffffff" font-size="10" font-weight="900" font-family="'Inter', sans-serif" text-anchor="middle">RODEO {num_rodeo}</text>
    </g>
    """

def etiqueta_regulacion(id_enzima, x, y, dx=0, dy=0, anchor="start"):
    """
    Genera etiqueta compacta de regulación alostérica y covalente:
    (+) Verde para activadores, (-) Rojo para inhibidores, (P) Amarillo para fosforilación, [Hormonal] Azul para control hormonal.
    """
    e = regulacion.ENZIMAS_POR_ID.get(id_enzima)
    if not e:
        return ""
    lineas = []
    if e.get("activadores"):
        lineas.append((f"(+) {', '.join(e['activadores'])}", "#16a34a"))
    if e.get("inhibidores"):
        lineas.append((f"(-) {', '.join(e['inhibidores'])}", "#dc2626"))
    if e.get("mapa_cov"):
        lineas.append((f"(P) {e['mapa_cov']}", "#ca8a04"))
    if e.get("mapa_hor"):
        lineas.append((f"[Hormonal] {e['mapa_hor']}", "#0284c7"))

    if not lineas:
        return ""

    spans = []
    curr_y = dy
    for txt, col in lineas:
        anchor_attr = f'text-anchor="{anchor}"' if anchor != "start" else ""
        font_attr = "font-family=\"'Inter', sans-serif\""
        spans.append(f'<text x="{dx}" y="{curr_y}" fill="{col}" font-size="9" font-weight="800" {font_attr} {anchor_attr}>{txt}</text>')
        curr_y += 12

    return f"""
    <g class="etiqueta-regulacion" transform="translate({x}, {y})">
      {''.join(spans)}
    </g>
    """

def reaccion_libre(x, y, h, enzima, entra="", sale="", es_ganancia=False, reversible=False, id_rx="", text_dx=14, text_anchor="start"):
    """Flecha de reacción libre con enzima y curvas Bézier de energía."""
    curvas = ""
    if entra:
        col_in = "#dc2626" if not es_ganancia else "#475569"
        curvas += f"""
        <path d="M -65 6 Q -20 6 -4 16" fill="none" stroke="{col_in}" stroke-width="1.8" marker-end="url(#arrowRed)"/>
        <text x="-70" y="9" fill="{col_in}" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{entra}</text>
        """
    if sale:
        col_out = "#059669" if es_ganancia else "#475569"
        curvas += f"""
        <path d="M -4 22 Q -20 32 -65 32" fill="none" stroke="{col_out}" stroke-width="1.8" marker-end="url(#arrowGreen)"/>
        <text x="-70" y="36" fill="{col_out}" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif" text-anchor="end">{sale}</text>
        """

    if reversible:
        lineas = f"""
        <line x1="-3" y1="0" x2="-3" y2="{h}" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        <line x1="3" y1="{h}" x2="3" y2="0" stroke="#ea580c" stroke-width="2" marker-end="url(#arrowFlow)"/>
        """
    else:
        lineas = f"""<line x1="0" y1="0" x2="0" y2="{h}" stroke="#ea580c" stroke-width="2.6" marker-end="url(#arrowFlow)"/>"""

    anchor_attr = f'text-anchor="{text_anchor}"' if text_anchor != "start" else ""
    return f"""
    <!-- Reacción: {enzima} -->
    <g id="{id_rx}" data-arrastrable="1" transform="translate({x}, {y})">
      {lineas}
      {curvas}
      <text x="{text_dx}" y="{h//2 + 4}" fill="#0f172a" font-size="12" font-weight="700" font-family="'Inter', sans-serif" {anchor_attr}>{enzima}</text>
    </g>
    """


