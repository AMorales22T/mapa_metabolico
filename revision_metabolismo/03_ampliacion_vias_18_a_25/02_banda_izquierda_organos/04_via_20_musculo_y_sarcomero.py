# =============================================================================
# MÓDULO DE REVISIÓN: Vía 20: Músculo Esquelético y Sarcómero en Contracción
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/generar_ampliacion.py (líneas 426 a 462 de 925)
# Descripción      : Deslizamiento actina-miosina, consumo de ATP y acoplamiento con los ciclos de Cori (lactato) y Cahill (alanina).
# =============================================================================

    # -------------------------------------------------------------------------
    # VÍA 20: MÚSCULO ESQUELÉTICO Y SARCÓMERO EN CONTRACCIÓN (CORI Y CAHILL)
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_musculo_esqueletico" class="ruta-metabolica">')
    p.append(encabezado_via(-710, 2350, 20, "MÚSCULO ESQUELÉTICO: SARCÓMERO EN CONTRACCIÓN", "Anatomía de la miofibrilla estriada • Ciclo de Cori (Lactato) • Cahill (Alanina)", color="#9f1239"))

    # Sarcómero anatómico detallado en contracción
    p.append(ea.esquema_sarcómero_muscular(cx=-380, cy=2520, w=620, h=270))

    # Flujo bioquímico muscular anaerobio acoplado a la contracción
    p.append("""
    <g transform="translate(-690, 2690)">
      <rect x="0" y="0" width="620" height="180" rx="10" fill="#fff1f2" stroke="#9f1239" stroke-width="2"/>
      
      <!-- Panel Cori -->
      <g transform="translate(30, 20)">
        <rect x="0" y="0" width="260" height="90" rx="8" fill="#ffffff" stroke="#e11d48" stroke-width="1.8"/>
        <text x="130" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#be123c" text-anchor="middle">ACOPLAMIENTO CORI (LACTATO)</text>
        <text x="130" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">Glucógeno ➔ Piruvato ➔ Lactato</text>
        <text x="130" y="66" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#059669" text-anchor="middle">LDH-M: Regenera NAD⁺ (+2 ATP)</text>
      </g>
      
      <!-- Panel Cahill -->
      <g transform="translate(330, 20)">
        <rect x="0" y="0" width="260" height="90" rx="8" fill="#ffffff" stroke="#059669" stroke-width="1.8"/>
        <text x="130" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#047857" text-anchor="middle">ACOPLAMIENTO CAHILL (ALANINA)</text>
        <text x="130" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" text-anchor="middle">Piruvato + BCAA ➔ L-Alanina</text>
        <text x="130" y="66" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#0d9488" text-anchor="middle">ALT muscular / Exporta nitrógeno</text>
      </g>

      <!-- Recaptación hepática -->
      <text x="310" y="135" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#881337" text-anchor="middle">➔ Lactato y Alanina viajan por sangre al hepatocito central (Gluconeogénesis y Urea)</text>
      <text x="310" y="155" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#64748b" text-anchor="middle">Permite sostener la contracción anaerobia máxima sin acidificar el sarcoplasma</text>
    </g>
    """)
    p.append('</g>')

