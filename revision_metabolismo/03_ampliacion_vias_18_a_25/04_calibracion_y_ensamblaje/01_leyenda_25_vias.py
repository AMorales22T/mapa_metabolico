# =============================================================================
# MÓDULO DE REVISIÓN: Actualización de la Leyenda Institucional a 25 Vías
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/generar_ampliacion.py (líneas 681 a 770 de 925)
# Descripción      : Reorganiza las 25 vías en 3 columnas equilibradas (1-8, 9-16, 17-25) en el bloque inferior.
# =============================================================================

# =============================================================================
# REESTRUCTURACIÓN DE LA LEYENDA INSTITUCIONAL CENTRAL
# =============================================================================

def actualizar_bloque_leyenda_central(inner_svg):
    """
    Modifica el bloque de leyenda del mapa original para:
    1. Distribuir las 25 vías metabólicas en 3 columnas perfectamente equilibradas:
       - Columna 1 (X=40): Vías 1 a 8
       - Columna 2 (X=630): Vías 9 a 16
       - Columna 3 (X=1220): Vías 17 a 25
       Todas alineadas exactamente en la misma cota vertical (Y=100, y=-12).
    2. Cambiar 'CÓDIGO DE COLORES EDITORIAL:' a 'CÓDIGO DE COLORES:'.
    """
    # 1. Cambiar el título de la columna 4
    inner_svg = inner_svg.replace("CÓDIGO DE COLORES EDITORIAL:", "CÓDIGO DE COLORES:")

    vias_todas_col1 = [
        {"n": 1, "nombre": "Glucólisis", "resumen": "Glucosa → 2 Piruvato (+2 ATP, +2 NADH)", "color": "#0284c7"},
        {"n": 2, "nombre": "Gluconeogénesis", "resumen": "Piruvato → Glucosa (4 enzimas clave · hepática)", "color": "#7c3aed"},
        {"n": 3, "nombre": "Glucógeno (Síntesis y lisis)", "resumen": "Glucogenogénesis & Glucogenólisis citosólica", "color": "#b45309"},
        {"n": 4, "nombre": "Vía de las pentosas fosfato", "resumen": "G6P → NADPH + Ribosa-5-P (Fase ox. y no ox.)", "color": "#059669"},
        {"n": 5, "nombre": "Complejo PDH (Piruvato DH)", "resumen": "Piruvato → Acetil-CoA + CO₂ + NADH", "color": "#ea580c"},
        {"n": 6, "nombre": "Ciclo de Krebs (TCA)", "resumen": "Acetil-CoA → 2 CO₂ + 3 NADH + FADH₂ + GTP", "color": "#c2410c"},
        {"n": 7, "nombre": "Cadena Respiratoria & ATPsint", "resumen": "Fosforilación oxidativa (gradiente de H⁺)", "color": "#16a34a"},
        {"n": 8, "nombre": "Lanzaderas (Malato/G3P)", "resumen": "Reoxidación de NADH citosólico hacia la MMI", "color": "#0284c7"},
    ]

    vias_todas_col2 = [
        {"n": 9, "nombre": "β-oxidación (y carnitina)", "resumen": "Palmitoil-CoA → 8 Acetil-CoA + FADH₂ + NADH", "color": "#b45309"},
        {"n": 10, "nombre": "Lipogénesis (FAS)", "resumen": "Acetil-CoA → Malonil-CoA → Palmitato (FAS)", "color": "#0d9488"},
        {"n": 11, "nombre": "Cetogénesis", "resumen": "Acetil-CoA → Acetoacetato y β-Hidroxibutirato", "color": "#be123c"},
        {"n": 12, "nombre": "Síntesis de colesterol", "resumen": "Acetil-CoA → HMG-CoA → Mevalonato → Colesterol", "color": "#4f46e5"},
        {"n": "12B", "nombre": "Destinos esqueletos carbonados", "resumen": "Convergencia de los 20 AA en intermediarios", "color": "#2563eb"},
        {"n": 13, "nombre": "Transaminación y desaminación", "resumen": "Recogida de amino en Glutamato → NH₄⁺", "color": "#2563eb"},
        {"n": 14, "nombre": "Ciclo de la urea", "resumen": "NH₄⁺ + HCO₃⁻ + Aspartato → Urea (hepático)", "color": "#0891b2"},
        {"n": 15, "nombre": "Biosíntesis de nucleótidos", "resumen": "Purinas y Pirimidinas de novo / Salvamento", "color": "#0284c7"},
        {"n": 16, "nombre": "Catabolismo de nucleótidos", "resumen": "Purinas → Ácido Úrico (XOD); Pirimidinas → β-Ala", "color": "#475569"},
    ]

    vias_todas_col3 = [
        {"n": 17, "nombre": "Ciclo de Cori (Músculo ⇄ Hígado)", "resumen": "Lactato muscular anaeróbico ⇄ Glucosa hepática", "color": "#9f1239"},
        {"n": 18, "nombre": "Digestión de lípidos", "resumen": "Micela mixta → Enterocito → Quilomicrón → Linfa", "color": "#0d9488"},
        {"n": 19, "nombre": "Tejido adiposo (lipólisis)", "resumen": "TAG → ATGL/HSL/MGL → 3 AG + Glicerol", "color": "#ea580c"},
        {"n": 20, "nombre": "Músculo esquelético y sarcómero", "resumen": "Contracción de actomiosina; Cori & Cahill", "color": "#9f1239"},
        {"n": 21, "nombre": "Cerebro y combustibles neuronales", "resumen": "Glucosa (GLUT1/3) & adaptación a cetonas (MCT)", "color": "#2563eb"},
        {"n": 22, "nombre": "Lipoproteínas plasmáticas", "resumen": "VLDL → IDL → LDL (ApoB100) y HDL (SR-B1)", "color": "#2563eb"},
        {"n": 23, "nombre": "Biosíntesis de TAG y fosfolípidos", "resumen": "G3P → LPA → PA → DAG → TAG / Fosfolípidos", "color": "#7c3aed"},
        {"n": 24, "nombre": "Biosíntesis de AA no esenciales", "resumen": "Ala, Ser, Gly, Cys, Asp, Asn, Glu, Gln, Pro, Tyr", "color": "#059669"},
        {"n": 25, "nombre": "Integración y conmutador", "resumen": "Flujos de combustible: Posprandial vs Ayuno", "color": "#ea580c"},
    ]

    def render_col(items, x_offset, titulo):
        svg_items = []
        for i, v in enumerate(items):
            y_pos = i * 38
            nom = v['nombre'].replace('&', '&amp;')
            res = v['resumen'][:50].replace('&', '&amp;')
            svg_items.append(f'''
            <g id="badge_leyenda_{v['n']}" class="badge-via" data-via="{v['n']}" transform="translate(0, {y_pos})" style="cursor: pointer;">
              <circle cx="11" cy="0" r="9" fill="{v['color']}"/>
              <text x="11" y="3.5" fill="#ffffff" font-size="8.5" font-weight="900" font-family="'JetBrains Mono', monospace" text-anchor="middle">{v['n']}</text>
              <text x="26" y="3" fill="#0f172a" font-size="10.5" font-weight="800" font-family="'Inter', sans-serif">{nom}</text>
              <text x="26" y="15" fill="#64748b" font-size="8.5" font-family="'Inter', sans-serif">{res}</text>
            </g>''')
        return f'''
        <g transform="translate({x_offset}, 100)">
          <text x="0" y="-12" fill="#0284c7" font-size="12" font-weight="900" font-family="'Inter', sans-serif" letter-spacing="1">{titulo}</text>
          {''.join(svg_items)}
        </g>'''

    col1_svg = render_col(vias_todas_col1, 40, "VÍAS METABÓLICAS (1–8):")
    col2_svg = render_col(vias_todas_col2, 630, "VÍAS METABÓLICAS (9–16):")
    col3_svg = render_col(vias_todas_col3, 1220, "VÍAS DE INTEGRACIÓN Y ÓRGANOS (17–25):")

    bloque_3_cols = f"""
      <!-- 3 Columnas equilibradas de Vías (1 a 25) alineadas exactamente a Y=100 -->
      {col1_svg}
      {col2_svg}
      {col3_svg}
    """

    # Reemplazar desde el inicio de las columnas de vías hasta la línea divisoria de X=1840
    patron_reemplazo = r'<!-- Columnas 1 y 2: Vías.*?<line x1="1840"'
    if re.search(patron_reemplazo, inner_svg, re.DOTALL):
        inner_svg = re.sub(patron_reemplazo, bloque_3_cols + '\n      <line x1="1840"', inner_svg, count=1, flags=re.DOTALL)

    return inner_svg


