# =============================================================================
# MÓDULO DE REVISIÓN: Vía 22: Lipoproteínas Plasmáticas y Transporte Reverso
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/generar_ampliacion.py (líneas 481 a 530 de 925)
# Descripción      : Cascada VLDL -> LPL -> IDL -> LDL (ApoB-100, receptor LDLR) y transporte reverso de colesterol por HDL (ApoA-I, LCAT, SR-B1).
# =============================================================================

def construir_banda_derecha():
    """Genera las rutas, estructuras y esquemas anatómicos de la banda derecha (X in [5800, 6560])."""
    p = ['<g id="ampliacion_tematica_derecha">']

    # -------------------------------------------------------------------------
    # VÍA 22: CASCADA DE LIPOPROTEÍNAS PLASMÁTICAS Y TRANSPORTE REVERSO
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_lipoproteinas" class="ruta-metabolica">')
    p.append(encabezado_via(5850, 480, 22, "LIPOPROTEÍNAS PLASMÁTICAS Y TRANSPORTE REVERSO", "VLDL ➔ IDL ➔ LDL (LDLR) • HDL y Transporte Reverso de Colesterol (SR-B1)", color="#2563eb"))

    p.append(ea.esquema_lipoproteina(cx=6020, cy=610, radio=66, tipo="VLDL HEPÁTICA", apoproteina="ApoB-100", color_apo="#dc2626"))
    p.append(ea.esquema_lipoproteina(cx=6380, cy=610, radio=58, tipo="LDL (COLESTEROL)", apoproteina="ApoB-100", color_apo="#dc2626"))

    p.append("""
    <g id="rx_lpl_lh" transform="translate(6120, 560)">
      <path d="M -30 50 L 50 50" fill="none" stroke="#2563eb" stroke-width="3" marker-end="url(#arrowBlue)"/>
      <rect x="-10" y="10" width="80" height="30" rx="5" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
      <text x="30" y="28" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#1d4ed8" text-anchor="middle">LPL + LH</text>
      <text x="30" y="66" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#64748b" text-anchor="middle">Pérdida TAG</text>
    </g>
    """)

    # Endocitosis de LDL mediada por Receptor (LDLR)
    p.append("""
    <g id="rx_ldlr_endocitosis" transform="translate(5860, 720)">
      <rect x="0" y="0" width="650" height="145" rx="10" fill="#f8fafc" stroke="#2563eb" stroke-width="2"/>
      <text x="325" y="26" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#1d4ed8" text-anchor="middle">ENDOCITOSIS DE LDL MEDIADA POR RECEPTOR (LDLR)</text>
      <text x="325" y="50" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">1. ApoB-100 se une al Receptor LDLR en fositas recubiertas de clatrina</text>
      <text x="325" y="72" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#0f172a" text-anchor="middle">2. Degradación lisosómica: Libera Colesterol Libre Intracelular</text>
      <line x1="30" y1="84" x2="620" y2="84" stroke="#cbd5e1" stroke-width="1.5"/>
      <text x="325" y="104" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" text-anchor="middle">Efecto del Colesterol Libre Intracelular:</text>
      <text x="325" y="126" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">↓ HMG-CoA Reductasa  |  ↓ Síntesis LDLR (SREBP-2)  |  ↑ ACAT (Ésteres de colesterilo)</text>
    </g>
    """)

    # HDL y Transporte Reverso de Colesterol
    p.append(ea.esquema_lipoproteina(cx=6020, cy=970, radio=52, tipo="HDL MADURA", apoproteina="ApoA-I", color_apo="#059669"))
    
    p.append("""
    <g id="rx_transporte_reverso_hdl" transform="translate(6120, 900)">
      <rect x="0" y="0" width="390" height="140" rx="10" fill="#f0fdf4" stroke="#059669" stroke-width="2"/>
      <text x="195" y="26" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#047857" text-anchor="middle">TRANSPORTE REVERSO DE COLESTEROL (HDL)</text>
      <text x="195" y="50" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#0f172a" text-anchor="middle">1. ApoA-I capta colesterol periférico vía ABCA1 / ABCG1</text>
      <text x="195" y="72" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#059669" text-anchor="middle">2. LCAT (activada por ApoA-I) esterifica el colesterol hacia el núcleo</text>
      <text x="195" y="94" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#0f172a" text-anchor="middle">3. Captación selectiva hepática mediante Receptor SR-B1</text>
      <text x="195" y="118" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#047857" text-anchor="middle">➔ Excreción hepática como Sales Biliares en bilis</text>
    </g>
    """)
    p.append('</g>')

