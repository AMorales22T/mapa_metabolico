"""
CATÁLOGO DE ESTRUCTURAS QUÍMICAS (SVG) - VÍA DE LAS PENTOSAS FOSFATO
====================================================================
Estructuras vectoriales diseñadas bajo el Manual de Estilo Editorial:
- Trazos oscuros nítidos (#0f172a)
- Oxígenos resaltados en rojo (#dc2626)
- Grupos fosfato con cápsula naranja (#ffedd5, borde #ea580c y Ⓟ)
- Coordenadas relativas en un lienzo mental de ~100x100 px
"""

# =============================================================================
# 1. GLUCOSA-6-FOSFATO (G6P) - Sustrato inicial que bifurca desde la Glucólisis
# =============================================================================
GLUCOSA_6_FOSFATO = """
  <!-- Anillo de piranosa (6 lados) -->
  <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>

  <!-- Oxígeno del anillo -->
  <circle cx="16" cy="22" r="7" fill="#ffffff"/>
  <text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>

  <!-- Carbono 6 con Grupo Fosfato destacado -->
  <line x1="0" y1="36" x2="0" y2="12" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="0" cy="-2" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="0" y="3" fill="#c2410c" font-size="12" font-weight="900" text-anchor="middle">Ⓟ</text>
  <text x="-20" y="2" fill="#ea580c" font-size="9" font-weight="700" text-anchor="end">O-PO₃²⁻</text>

  <!-- Grupos hidroxilo (-OH) -->
  <line x1="72" y1="36" x2="88" y2="36" stroke="#0f172a" stroke-width="2"/>
  <text x="98" y="40" fill="#0f172a" font-size="11" font-weight="700">OH</text>

  <line x1="50" y1="58" x2="50" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="50" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">OH</text>

  <line x1="16" y1="58" x2="16" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="16" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">HO</text>

  <line x1="0" y1="36" x2="-14" y2="36" stroke="#0f172a" stroke-width="2"/>
  <text x="-24" y="40" fill="#0f172a" font-size="11" font-weight="700">HO</text>
"""


# =============================================================================
# 2. 6-FOSFOGLUCONO-δ-LACTONA - Éster intramolecular cíclico (Lactona)
# =============================================================================
FOSFOGLUCONO_LACTONA_6 = """
  <!-- Anillo de lactona de 6 vértices -->
  <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>

  <!-- Oxígeno éster intramolecular del anillo -->
  <circle cx="16" cy="22" r="7" fill="#ffffff"/>
  <text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>

  <!-- C1: Doble enlace carbonilo de la lactona (C=O) -->
  <line x1="72" y1="34" x2="88" y2="25" stroke="#0f172a" stroke-width="2"/>
  <line x1="74" y1="38" x2="90" y2="29" stroke="#0f172a" stroke-width="2"/>
  <text x="98" y="28" fill="#dc2626" font-size="13" font-weight="900">O</text>

  <!-- C6 con Grupo Fosfato -->
  <line x1="0" y1="36" x2="0" y2="12" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="0" cy="-2" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="0" y="3" fill="#c2410c" font-size="12" font-weight="900" text-anchor="middle">Ⓟ</text>
  <text x="-20" y="2" fill="#ea580c" font-size="9" font-weight="700" text-anchor="end">O-PO₃²⁻</text>

  <!-- Grupos hidroxilo en C2, C3 y C4 -->
  <line x1="50" y1="58" x2="50" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="50" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">OH</text>

  <line x1="16" y1="58" x2="16" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="16" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">HO</text>

  <line x1="0" y1="36" x2="-14" y2="36" stroke="#0f172a" stroke-width="2"/>
  <text x="-24" y="40" fill="#0f172a" font-size="11" font-weight="700">HO</text>
"""


# =============================================================================
# 3. 6-FOSFOGLUCONATO - Cadena lineal de 6 carbonos con carboxilato libre
# =============================================================================
FOSFOGLUCONATO_6 = """
  <!-- C1: Grupo Carboxilato COO- arriba -->
  <text x="40" y="14" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="18" x2="40" y2="30" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: H-C-OH -->
  <text x="40" y="40" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">H-C-OH</text>
  <line x1="40" y1="44" x2="40" y2="52" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C3: HO-C-H -->
  <text x="40" y="62" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">HO-C-H</text>
  <line x1="40" y1="66" x2="40" y2="74" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C4 y C5: (CHOH)2 -->
  <text x="40" y="84" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">(CHOH)₂</text>
  <line x1="40" y1="88" x2="40" y2="96" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C6: CH2-O-P con grupo fosfato -->
  <text x="40" y="106" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">CH₂-O</text>
  <circle cx="40" cy="126" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="40" y="130" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
"""


# =============================================================================
# 4. D-RIBULOSA-5-FOSFATO (Ru5P) - Pentosa cetosa (5C), fin de fase oxidativa
# =============================================================================
RIBULOSA_5_FOSFATO = """
  <!-- C1: CH2OH arriba -->
  <text x="40" y="14" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">CH₂OH</text>
  <line x1="40" y1="18" x2="40" y2="32" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: C=O (Grupo carbonilo cetona) -->
  <text x="40" y="44" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">C</text>
  <line x1="47" y1="39" x2="65" y2="39" stroke="#0f172a" stroke-width="2"/>
  <line x1="47" y1="43" x2="65" y2="43" stroke="#0f172a" stroke-width="2"/>
  <text x="73" y="45" fill="#dc2626" font-size="13" font-weight="900">O</text>

  <!-- Enlace C2 a C3 -->
  <line x1="40" y1="49" x2="40" y2="60" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C3 y C4: (CHOH)2 -->
  <text x="40" y="70" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">(CHOH)₂</text>

  <!-- C5: CH2-O-P -->
  <line x1="40" y1="75" x2="40" y2="86" stroke="#0f172a" stroke-width="2.2"/>
  <text x="40" y="96" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">CH₂-O</text>
  <circle cx="40" cy="116" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="40" y="120" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
"""


# =============================================================================
# 5. D-RIBOSA-5-FOSFATO (R5P) - Precursora de Nucleótidos / ADN / ARN
# =============================================================================
RIBOSA_5_FOSFATO = """
  <!-- Anillo furanosa de 5 lados (Pentosa aldosa cíclica) -->
  <polygon points="35,18 68,38 52,68 18,68 2,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>

  <!-- Oxígeno superior del anillo -->
  <circle cx="35" cy="18" r="7" fill="#ffffff"/>
  <text x="35" y="22" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>

  <!-- C1 (derecha): OH anomérico -->
  <line x1="68" y1="38" x2="84" y2="38" stroke="#0f172a" stroke-width="2"/>
  <text x="94" y="42" fill="#0f172a" font-size="10" font-weight="700">OH</text>

  <!-- C5 (izquierda): Grupo Fosfato -->
  <line x1="2" y1="38" x2="-10" y2="18" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="-16" cy="6" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="-16" y="10" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>

  <!-- C2 y C3 con grupos -OH abajo -->
  <line x1="52" y1="68" x2="52" y2="80" stroke="#0f172a" stroke-width="2"/>
  <text x="52" y="90" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">OH</text>

  <line x1="18" y1="68" x2="18" y2="80" stroke="#0f172a" stroke-width="2"/>
  <text x="18" y="90" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">HO</text>
"""


# =============================================================================
# 6. D-XILULOSA-5-FOSFATO (Xu5P) - Epímero en C3 de la Ribulosa-5-P
# =============================================================================
XILULOSA_5_FOSFATO = """
  <!-- C1: CH2OH arriba -->
  <text x="40" y="14" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">HO-CH₂</text>
  <line x1="40" y1="18" x2="40" y2="32" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: C=O -->
  <text x="40" y="44" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">C</text>
  <line x1="47" y1="39" x2="65" y2="39" stroke="#0f172a" stroke-width="2"/>
  <line x1="47" y1="43" x2="65" y2="43" stroke="#0f172a" stroke-width="2"/>
  <text x="73" y="45" fill="#dc2626" font-size="13" font-weight="900">O</text>

  <!-- Enlace C2 a C3 (Inversión epimérica de -OH) -->
  <line x1="40" y1="49" x2="40" y2="60" stroke="#0f172a" stroke-width="2.2"/>
  <text x="40" y="70" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">HO-C-H</text>

  <!-- C4 y C5: CHOH - CH2O-P -->
  <line x1="40" y1="75" x2="40" y2="86" stroke="#0f172a" stroke-width="2.2"/>
  <text x="40" y="96" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">H-C-OH</text>
  <circle cx="40" cy="116" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="40" y="120" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
"""


# =============================================================================
# 7. SEDOHEPTULOSA-7-FOSFATO (S7P) - Azúcar intermediario de 7 carbonos (Cetosa)
# =============================================================================
SEDOHEPTULOSA_7_FOSFATO = """
  <text x="40" y="14" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">HO-CH₂</text>
  <line x1="40" y1="18" x2="40" y2="30" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C2: C=O -->
  <text x="40" y="42" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">C=O</text>
  <line x1="40" y1="46" x2="40" y2="56" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C3-C6: Poliol de 4C -->
  <text x="40" y="66" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">(CHOH)₄</text>
  <line x1="40" y1="70" x2="40" y2="82" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C7: CH2-O-P -->
  <text x="40" y="92" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">CH₂-O</text>
  <circle cx="40" cy="112" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="40" y="116" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
"""
