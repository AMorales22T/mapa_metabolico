# =============================================================================
# MÓDULO DE REVISIÓN: Estructuras Químicas de Cetogénesis y Cetólisis
# =============================================================================
# Archivo original : 03_LIPIDOS/via_11_cetogenesis_y_cetolisis/estructuras_ceto.py (líneas 1 a 192 de 192)
# Descripción      : Fórmulas estructurales 2D de los intermediarios de Cetogénesis y Cetólisis.
# =============================================================================

#!/usr/bin/env python3
"""
ESTRUCTURAS QUÍMICAS (SVG) - CETOGÉNESIS Y CETÓLISIS
====================================================
Diseñadas bajo el Manual de Estilo Editorial Científico del proyecto:
- Trazos oscuros nítidos (#0f172a) de 2.2 a 2.5 pt.
- Oxígenos y grupos carbonilo resaltados en rojo (#dc2626) en negrita.
- Grupos hidroxilo (-OH) en azul (#0284c7).
- Grupos carboxilato (-COO⁻) en rojo (#dc2626).
- Cápsulas de cofactores: CoA-S en púrpura (#ede9fe / #7c3aed), Succinil-CoA / Succinato.
- Cero polígonos cerrados no deseados: fill="none" en polilíneas y trazos.
"""

# =============================================================================
# 1. ACETIL-COA (2C)
# =============================================================================
ACETIL_COA_CETO = """
<g class="mol-acetil-coa" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Cápsula S-CoA -->
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9" stroke="none" text-anchor="middle">CoA-S</text>
  <line x1="48" y1="28" x2="72" y2="28" stroke="#7c3aed" stroke-width="2.3"/>

  <!-- Carbonilo C1 -->
  <line x1="69" y1="28" x2="69" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <line x1="75" y1="28" x2="75" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <text x="72" y="8" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- Metilo C2 -->
  <line x1="72" y1="28" x2="94" y2="40" />
  <text x="98" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none">CH₃</text>
</g>
"""

# =============================================================================
# 2. ACETOACETIL-COA (4C) - Producto de la Tiolasa
# =============================================================================
ACETOACETIL_COA = """
<g class="mol-acetoacetil-coa" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Cápsula CoA-S a la izquierda -->
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9" stroke="none" text-anchor="middle">CoA-S</text>
  <line x1="48" y1="28" x2="70" y2="28" stroke="#7c3aed" stroke-width="2.3"/>

  <!-- C1 Carbonilo tioéster -->
  <line x1="67" y1="28" x2="67" y2="12" stroke="#dc2626" stroke-width="2.1"/>
  <line x1="73" y1="28" x2="73" y2="12" stroke="#dc2626" stroke-width="2.1"/>
  <text x="70" y="8" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C2 metileno (alfa) -->
  <line x1="70" y1="28" x2="94" y2="44" />
  <circle cx="94" cy="44" r="3" fill="#ea580c" stroke="none"/>
  <text x="94" y="58" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#ea580c" stroke="none" text-anchor="middle">CH₂</text>

  <!-- C3 Carbonilo beta (cetona) -->
  <line x1="94" y1="44" x2="118" y2="28" />
  <line x1="115" y1="28" x2="115" y2="12" stroke="#dc2626" stroke-width="2.1"/>
  <line x1="121" y1="28" x2="121" y2="12" stroke="#dc2626" stroke-width="2.1"/>
  <text x="118" y="8" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C4 metilo terminal -->
  <line x1="118" y1="28" x2="140" y2="42" />
  <text x="144" y="46" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a" stroke="none">CH₃</text>
</g>
"""

# =============================================================================
# 3. HMG-COA (3-Hidroxi-3-Metilglutaril-CoA, 6C) - Intermediario Clave Marcapasos
# =============================================================================
HMG_COA = """
<g class="mol-hmg-coa" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Cápsula CoA-S a la izquierda -->
  <rect x="2" y="27" width="46" height="22" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="25" y="42" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9" stroke="none" text-anchor="middle">CoA-S</text>
  <line x1="48" y1="38" x2="70" y2="38" stroke="#7c3aed" stroke-width="2.3"/>

  <!-- C1 Carbonilo tioéster -->
  <line x1="67" y1="38" x2="67" y2="22" stroke="#dc2626" stroke-width="2.1"/>
  <line x1="73" y1="38" x2="73" y2="22" stroke="#dc2626" stroke-width="2.1"/>
  <text x="70" y="18" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C2 metileno -->
  <line x1="70" y1="38" x2="95" y2="38" />

  <!-- C3 central ramificado con OH y CH3 -->
  <line x1="95" y1="38" x2="120" y2="38" />
  <circle cx="120" cy="38" r="3.2" fill="#0f172a" stroke="none"/>
  <!-- C3 OH arriba -->
  <line x1="120" y1="38" x2="120" y2="18" stroke="#0284c7" stroke-width="2.2"/>
  <text x="120" y="13" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">OH</text>
  <!-- C3 CH3 ramificación abajo -->
  <line x1="120" y1="38" x2="120" y2="56" />
  <text x="120" y="69" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₃</text>

  <!-- C4 metileno -->
  <line x1="120" y1="38" x2="145" y2="38" />

  <!-- C5 carboxilato terminal (COO⁻) -->
  <line x1="145" y1="38" x2="168" y2="24" />
  <text x="172" y="27" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
</g>
"""

# =============================================================================
# 4. ACETOACETATO (4C) - Primer Cuerpo Cetónico
# =============================================================================
ACETOACETATO = """
<g class="mol-acetoacetato" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo Carboxilato terminal C1 (COO⁻) -->
  <text x="18" y="28" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none">⁻OOC</text>
  <line x1="56" y1="24" x2="80" y2="38" />

  <!-- C2 metileno central (CH2) -->
  <circle cx="80" cy="38" r="3" fill="#ea580c" stroke="none"/>
  <text x="80" y="52" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#ea580c" stroke="none" text-anchor="middle">CH₂</text>

  <!-- C3 Carbonilo beta (cetona) -->
  <line x1="80" y1="38" x2="108" y2="24" />
  <line x1="105" y1="24" x2="105" y2="8" stroke="#dc2626" stroke-width="2.1"/>
  <line x1="111" y1="24" x2="111" y2="8" stroke="#dc2626" stroke-width="2.1"/>
  <text x="108" y="4" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C4 metilo terminal -->
  <line x1="108" y1="24" x2="132" y2="38" />
  <text x="136" y="42" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none">CH₃</text>
</g>
"""

# =============================================================================
# 5. D-BETA-HIDROXIBUTIRATO (4C) - Principal Cuerpo Cetónico Circulante
# =============================================================================
D_BETA_HIDROXIBUTIRATO = """
<g class="mol-hidroxibutirato" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo Carboxilato terminal C1 (COO⁻) -->
  <text x="18" y="28" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none">⁻OOC</text>
  <line x1="56" y1="24" x2="80" y2="38" />

  <!-- C2 metileno (alfa) -->
  <circle cx="80" cy="38" r="3" fill="#ea580c" stroke="none"/>
  <text x="80" y="52" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#ea580c" stroke="none" text-anchor="middle">CH₂</text>

  <!-- C3 beta-alcohol (-OH) -->
  <line x1="80" y1="38" x2="108" y2="24" />
  <circle cx="108" cy="24" r="3" fill="#0284c7" stroke="none"/>
  <line x1="108" y1="24" x2="108" y2="6" stroke="#0284c7" stroke-width="2.2"/>
  <text x="108" y="2" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">OH</text>

  <!-- C4 metilo terminal -->
  <line x1="108" y1="24" x2="132" y2="38" />
  <text x="136" y="42" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none">CH₃</text>
</g>
"""

# =============================================================================
# 6. ACETONA (3C) - Subproducto Volátil (Exhalación pulmonar)
# =============================================================================
ACETONA = """
<g class="mol-acetona" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Metilo izquierdo -->
  <text x="18" y="38" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a" stroke="none">H₃C</text>
  <line x1="42" y1="34" x2="68" y2="20" />

  <!-- C2 Carbonilo central (C=O) -->
  <circle cx="68" cy="20" r="3" fill="#0f172a" stroke="none"/>
  <line x1="65" y1="20" x2="65" y2="4" stroke="#dc2626" stroke-width="2.1"/>
  <line x1="71" y1="20" x2="71" y2="4" stroke="#dc2626" stroke-width="2.1"/>
  <text x="68" y="0" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C3 Metilo derecho -->
  <line x1="68" y1="20" x2="94" y2="34" />
  <text x="98" y="38" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a" stroke="none">CH₃</text>
</g>
"""

# =============================================================================
# 7. SUCCINIL-COA y SUCCINATO (Cofactores de Donación en Cetólisis)
# =============================================================================
SUCCINIL_COA_BADGE = """
<g class="badge-succinil" stroke="#0f172a" stroke-width="2" fill="none">
  <!-- Mini molécula Succinil-CoA -->
  <rect x="0" y="0" width="105" height="26" rx="6" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="1.4"/>
  <text x="52" y="17" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#6d28d9" stroke="none" text-anchor="middle">Succinil-CoA [4C]</text>
</g>
"""

SUCCINATO_BADGE = """
<g class="badge-succinato" stroke="#0f172a" stroke-width="2" fill="none">
  <!-- Mini molécula Succinato -->
  <rect x="0" y="0" width="95" height="26" rx="6" fill="#ecfdf5" stroke="#10b981" stroke-width="1.4"/>
  <text x="47" y="17" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#047857" stroke="none" text-anchor="middle">Succinato [4C]</text>
</g>
"""
