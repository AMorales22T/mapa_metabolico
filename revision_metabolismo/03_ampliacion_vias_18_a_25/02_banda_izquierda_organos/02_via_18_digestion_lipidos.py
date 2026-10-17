# =============================================================================
# MÓDULO DE REVISIÓN: Vía 18: Digestión y Absorción de Lípidos Dietarios
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/generar_ampliacion.py (líneas 289 a 329 de 925)
# Descripción      : Emulsión por sales biliares, lipasa pancreática + colipasa, absorción en enterocito (CD36/NPC1L1), reesterificación y quilomicrón.
# =============================================================================

def construir_banda_izquierda():
    """Genera las rutas, estructuras y esquemas anatómicos de la banda izquierda (X in [-760, 0])."""
    p = ['<g id="ampliacion_tematica_izquierda">']

    # -------------------------------------------------------------------------
    # VÍA 18: DIGESTIÓN Y ABSORCIÓN DE LÍPIDOS DIETARIOS
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_digestion_lipidos" class="ruta-metabolica">')
    p.append(encabezado_via(-710, 480, 18, "DIGESTIÓN Y TRANSPORTE DE LÍPIDOS DIETARIOS", "Luz intestinal • Emulsión micelar • Enterocito • Linfa quilífera", color="#0d9488"))

    # Micela mixta y lipasa pancreática
    p.append(ea.esquema_micela_mixta(cx=-520, cy=610, radio=66))
    
    p.append("""
    <g id="rx_lipasa_pancreatica" transform="translate(-360, 560)">
      <rect x="0" y="0" width="260" height="92" rx="8" fill="#f0fdfa" stroke="#0d9488" stroke-width="2"/>
      <text x="130" y="22" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f766e" text-anchor="middle">LIPASA PANCREÁTICA</text>
      <text x="130" y="38" font-family="'JetBrains Mono', monospace" font-size="9.5" font-weight="700" fill="#134e4a" text-anchor="middle">EC 3.1.1.3 + Colipasa</text>
      <line x1="15" y1="46" x2="245" y2="46" stroke="#ccfbf1" stroke-width="1.5"/>
      <text x="130" y="64" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">TAG + 2 H₂O ➔</text>
      <text x="130" y="80" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#ea580c" text-anchor="middle">2-MAG + 2 Ácidos Grasos</text>
    </g>
    """)

    # Enterocito anatómico
    p.append(ea.esquema_enterocito(x=-690, y=720, w=620, h=360))

    # Quilomicrón naciente
    p.append(ea.esquema_lipoproteina(cx=-480, cy=1170, radio=66, tipo="QUILOMICRÓN", apoproteina="ApoB-48", color_apo="#dc2626"))
    
    # Canal linfático hacia el torrente vascular continuo (Y=350)
    p.append("""
    <g id="drenaje_linfatico_a_sangre">
      <path d="M -410 1170 C -150 1170, -70 560, -70 418" fill="none" stroke="#16a34a" stroke-width="3.5" stroke-dasharray="8 5" marker-end="url(#arrowGreen)"/>
      <rect x="-240" y="445" width="150" height="34" rx="6" fill="#f0fdf4" stroke="#16a34a" stroke-width="1.8"/>
      <text x="-165" y="461" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#15803d" text-anchor="middle">CONDUCTO TORÁCICO</text>
      <text x="-165" y="473" font-family="'Inter', sans-serif" font-size="8" font-weight="700" fill="#166534" text-anchor="middle">Drenaje linfático ➔ Sangre</text>
    </g>
    """)
    p.append('</g>')

