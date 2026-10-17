# =============================================================================
# MÓDULO DE REVISIÓN: Estructuras Químicas para Biosíntesis de Aminoácidos
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/estructuras_ampliacion.py (líneas 533 a 611 de 611)
# Descripción      : 3-Fosfoglicerato, 3-fosfoserina, serina, glicina, cisteína, prolina, asparagina y tirosina.
# =============================================================================

# =============================================================================
# 4. BIOSÍNTESIS DE AMINOÁCIDOS: ESTRUCTURAS VECTORIALES
# =============================================================================

L_SERINA = """
<g class="mol-l-serina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="38" />
  <text x="40" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="32" y1="48" x2="20" y2="48" />
  <text x="14" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">H</text>
  <line x1="48" y1="48" x2="60" y2="48" stroke="#2563eb" stroke-width="2"/>
  <rect x="62" y="36" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="81" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>
  <line x1="40" y1="56" x2="40" y2="72" />
  <text x="40" y="85" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="40" y1="89" x2="40" y2="102" />
  <text x="40" y="115" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">OH</text>
</g>
"""

L_CISTEINA = """
<g class="mol-l-cisteina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="38" />
  <text x="40" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="32" y1="48" x2="20" y2="48" />
  <text x="14" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">H</text>
  <line x1="48" y1="48" x2="60" y2="48" stroke="#2563eb" stroke-width="2"/>
  <rect x="62" y="36" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="81" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>
  <line x1="40" y1="56" x2="40" y2="72" />
  <text x="40" y="85" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="40" y1="89" x2="40" y2="102" />
  <text x="40" y="115" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#d97706" stroke="none" text-anchor="middle">SH</text>
</g>
"""

L_GLICINA = """
<g class="mol-l-glicina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />
  <text x="40" y="54" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="56" y1="50" x2="70" y2="50" stroke="#2563eb" stroke-width="2"/>
  <rect x="72" y="38" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="91" y="54" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>
</g>
"""

L_ASPARAGINA = """
<g class="mol-l-asparagina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="38" />
  <text x="40" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="32" y1="48" x2="20" y2="48" />
  <text x="14" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">H</text>
  <line x1="48" y1="48" x2="60" y2="48" stroke="#2563eb" stroke-width="2"/>
  <rect x="62" y="36" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="81" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>
  <line x1="40" y1="56" x2="40" y2="72" />
  <text x="40" y="85" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="40" y1="89" x2="40" y2="104" />
  <text x="40" y="117" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="48" y1="113" x2="64" y2="113" stroke="#dc2626" stroke-width="2"/>
  <line x1="48" y1="117" x2="64" y2="117" stroke="#dc2626" stroke-width="2"/>
  <text x="70" y="120" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="32" y1="113" x2="18" y2="113" stroke="#2563eb" stroke-width="2"/>
  <text x="12" y="118" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="end">H₂N</text>
</g>
"""

L_PROLINA = """
<g class="mol-l-prolina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="40,40 68,52 58,82 22,82 12,52" fill="#eff6ff" stroke="#2563eb" stroke-width="2"/>
  <text x="40" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">N⁺H₂</text>
  <line x1="68" y1="52" x2="88" y2="40" stroke="#0f172a" stroke-width="2.2"/>
  <text x="94" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
</g>
"""
