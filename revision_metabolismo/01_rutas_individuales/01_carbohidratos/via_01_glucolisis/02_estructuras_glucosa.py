# =============================================================================
# MÓDULO DE REVISIÓN: Estructuras Químicas de la Glucólisis
# =============================================================================
# Archivo original : 01_CARBOHIDRATOS/via_01_glucolisis/estructuras_glucosa.py (líneas 1 a 271 de 271)
# Descripción      : Fórmulas 2D vectoriales de los 10 intermediarios glucolíticos.
# =============================================================================

"""
CATÁLOGO COMPLETO DE ESTRUCTURAS QUÍMICAS (SVG) - RUTA GLUCOLÍTICA
==================================================================
Diseñadas bajo el Manual de Estilo Editorial:
- Trazos oscuros nítidos (#0f172a)
- Oxígenos resaltados en rojo (#dc2626)
- Grupos fosfato con cápsula naranja (#ffedd5, borde #ea580c y Ⓟ)
- Coordenadas relativas en un lienzo mental de ~100x100 px sin amontonamiento
"""

# =============================================================================
# FASE 1: FASE PREPARATORIA (INVERSIÓN DE ENERGÍA)
# =============================================================================

# 1. D-GLUCOSA (Anillo Piranosa, 6 vértices)
GLUCOSA = """
  <!-- Anillo de 6 lados -->
  <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>

  <!-- Oxígeno del anillo -->
  <circle cx="16" cy="22" r="7" fill="#ffffff"/>
  <text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>

  <!-- Carbono 6: -CH2OH arriba -->
  <line x1="0" y1="36" x2="0" y2="12" stroke="#0f172a" stroke-width="2.2"/>
  <text x="0" y="7" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">CH₂OH</text>

  <!-- Grupos hidroxilo (-OH) -->
  <!-- C1 (derecha) -->
  <line x1="72" y1="36" x2="88" y2="36" stroke="#0f172a" stroke-width="2"/>
  <text x="98" y="40" fill="#0f172a" font-size="11" font-weight="700">OH</text>

  <!-- C2 (abajo derecha) -->
  <line x1="50" y1="58" x2="50" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="50" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">OH</text>

  <!-- C3 (abajo izquierda) -->
  <line x1="16" y1="58" x2="16" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="16" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">HO</text>

  <!-- C4 (izquierda) -->
  <line x1="0" y1="36" x2="-14" y2="36" stroke="#0f172a" stroke-width="2"/>
  <text x="-24" y="40" fill="#0f172a" font-size="11" font-weight="700">HO</text>
"""


# 2. GLUCOSA-6-FOSFATO (G6P)
GLUCOSA_6_FOSFATO = """
  <!-- Anillo de 6 lados -->
  <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>

  <!-- Oxígeno del anillo -->
  <circle cx="16" cy="22" r="7" fill="#ffffff"/>
  <text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>

  <!-- Carbono 6 con Grupo Fosfato nítido y despejado -->
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


# 3. FRUCTOSA-6-FOSFATO (F6P) - Anillo Furanosa (Pentágono de 5 lados)
FRUCTOSA_6_FOSFATO = """
  <!-- Anillo de furanosa (pentágono) -->
  <polygon points="35,18 68,38 52,68 18,68 2,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>

  <!-- Oxígeno en el vértice superior del pentágono -->
  <circle cx="35" cy="18" r="7" fill="#ffffff"/>
  <text x="35" y="22" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>

  <!-- C1 (a la derecha): -CH2OH libre -->
  <line x1="68" y1="38" x2="88" y2="24" stroke="#0f172a" stroke-width="2.2"/>
  <text x="94" y="22" fill="#0f172a" font-size="10" font-weight="800">CH₂OH</text>
  <line x1="68" y1="38" x2="82" y2="50" stroke="#0f172a" stroke-width="2"/>
  <text x="88" y="55" fill="#0f172a" font-size="10" font-weight="700">OH</text>

  <!-- C6 (a la izquierda): Grupo Fosfato -->
  <line x1="2" y1="38" x2="-10" y2="18" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="-16" cy="6" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="-16" y="11" fill="#c2410c" font-size="12" font-weight="900" text-anchor="middle">Ⓟ</text>
  <text x="-35" y="10" fill="#ea580c" font-size="9" font-weight="700" text-anchor="end">O-PO₃²⁻</text>

  <!-- C3 y C4 con -OH abajo -->
  <line x1="52" y1="68" x2="52" y2="82" stroke="#0f172a" stroke-width="2"/>
  <text x="52" y="92" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">OH</text>

  <line x1="18" y1="68" x2="18" y2="82" stroke="#0f172a" stroke-width="2"/>
  <text x="18" y="92" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">HO</text>
"""


# 4. FRUCTOSA-1,6-BISFOSFATO (F-1,6-BP) - Fosforilada en C1 y en C6
FRUCTOSA_1_6_BISFOSFATO = """
  <!-- Anillo de furanosa (pentágono) -->
  <polygon points="35,18 68,38 52,68 18,68 2,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>

  <!-- Oxígeno superior -->
  <circle cx="35" cy="18" r="7" fill="#ffffff"/>
  <text x="35" y="22" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>

  <!-- C1 (a la derecha): Fosfato en C1 -->
  <line x1="68" y1="38" x2="88" y2="24" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="98" cy="14" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="98" y="19" fill="#c2410c" font-size="12" font-weight="900" text-anchor="middle">Ⓟ</text>

  <!-- C6 (a la izquierda): Fosfato en C6 -->
  <line x1="2" y1="38" x2="-10" y2="18" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="-16" cy="6" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="-16" y="11" fill="#c2410c" font-size="12" font-weight="900" text-anchor="middle">Ⓟ</text>

  <!-- C3 y C4 con -OH -->
  <line x1="52" y1="68" x2="52" y2="82" stroke="#0f172a" stroke-width="2"/>
  <text x="52" y="92" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">OH</text>

  <line x1="18" y1="68" x2="18" y2="82" stroke="#0f172a" stroke-width="2"/>
  <text x="18" y="92" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">HO</text>
"""


# 5. DIHIDROXIACETONA FOSFATO (DHAP) - Cadena lineal 3C (Cetosa)
DIHIDROXIACETONA_FOSFATO = """
  <!-- C1: CH2OH arriba -->
  <text x="40" y="15" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">HO-CH₂</text>
  <line x1="40" y1="18" x2="40" y2="35" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: C=O (Grupo carbonilo cetona) -->
  <text x="40" y="46" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">C</text>
  <line x1="47" y1="41" x2="65" y2="41" stroke="#0f172a" stroke-width="2"/>
  <line x1="47" y1="45" x2="65" y2="45" stroke="#0f172a" stroke-width="2"/>
  <text x="73" y="47" fill="#dc2626" font-size="13" font-weight="800">O</text>

  <!-- C3: CH2-O-P hacia abajo -->
  <line x1="40" y1="52" x2="40" y2="68" stroke="#0f172a" stroke-width="2.2"/>
  <text x="40" y="78" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">CH₂-O</text>
  <line x1="40" y1="82" x2="40" y2="92" stroke="#0f172a" stroke-width="2"/>
  <circle cx="40" cy="104" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="40" y="108" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
"""


# 6. GLICERALDEHÍDO-3-FOSFATO (GAP / G3P) - Cadena lineal 3C (Aldosa)
GLICERALDEHIDO_3_FOSFATO = """
  <!-- C1: Choque aldehído H-C=O -->
  <text x="40" y="15" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">HC=O</text>
  <text x="59" y="15" fill="#dc2626" font-size="12" font-weight="800"></text>
  <line x1="40" y1="20" x2="40" y2="38" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: H-C-OH -->
  <text x="40" y="48" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">H-C-OH</text>
  <line x1="40" y1="53" x2="40" y2="70" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C3: CH2-O-P -->
  <text x="40" y="80" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">CH₂-O</text>
  <line x1="40" y1="84" x2="40" y2="94" stroke="#0f172a" stroke-width="2"/>
  <circle cx="40" cy="106" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="40" y="110" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
"""


# =============================================================================
# FASE 2: FASE DE BENEFICIO / RENDIMIENTO ENERGÉTICO (3C)
# =============================================================================

# 7. 1,3-BISFOSFOGLICERATO (1,3-BPG) - Acil-fosfato de alta energía
BISFOSFOGLICERATO_1_3 = """
  <!-- C1: Acil-fosfato P-O-C=O -->
  <circle cx="15" cy="14" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="15" y="18" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
  <line x1="28" y1="14" x2="40" y2="14" stroke="#0f172a" stroke-width="2"/>
  <text x="46" y="18" fill="#0f172a" font-size="11" font-weight="800">C=O</text>

  <!-- Enlace C1 a C2 -->
  <line x1="52" y1="22" x2="52" y2="38" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C2: H-C-OH -->
  <text x="52" y="48" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">H-C-OH</text>

  <!-- Enlace C2 a C3 -->
  <line x1="52" y1="53" x2="52" y2="68" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C3: CH2-O-P -->
  <text x="52" y="78" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">CH₂-O</text>
  <circle cx="52" cy="100" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="52" y="104" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
"""


# 8. 3-FOSFOGLICERATO (3-PG)
FOSFOGLICERATO_3 = """
  <!-- C1: Carboxilato COO- -->
  <text x="40" y="16" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="38" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: H-C-OH -->
  <text x="40" y="48" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">H-C-OH</text>
  <line x1="40" y1="53" x2="40" y2="68" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C3: CH2-O-P -->
  <text x="40" y="78" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">CH₂-O</text>
  <circle cx="40" cy="100" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="40" y="104" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
"""


# 9. 2-FOSFOGLICERATO (2-PG) - Fosfato transferido al C2
FOSFOGLICERATO_2 = """
  <!-- C1: Carboxilato COO- -->
  <text x="35" y="16" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">COO⁻</text>
  <line x1="35" y1="22" x2="35" y2="40" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: H-C-O-P (Fosfato lateral en C2) -->
  <text x="35" y="50" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">H-C-O</text>
  <line x1="52" y1="46" x2="68" y2="46" stroke="#0f172a" stroke-width="2"/>
  <circle cx="80" cy="46" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="80" y="50" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>

  <!-- C3: CH2OH abajo -->
  <line x1="35" y1="55" x2="35" y2="72" stroke="#0f172a" stroke-width="2.2"/>
  <text x="35" y="84" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">CH₂OH</text>
"""


# 10. FOSFOENOLPIRUVATO (PEP) - Enlace éster fosfato de altísima energía
FOSFOENOLPIRUVATO = """
  <!-- C1: Carboxilato COO- -->
  <text x="35" y="16" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">COO⁻</text>
  <line x1="35" y1="22" x2="35" y2="40" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: C-O-P con doble enlace hacia el C3 -->
  <text x="35" y="50" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">C</text>
  <!-- Fosfato lateral -->
  <line x1="42" y1="46" x2="62" y2="46" stroke="#0f172a" stroke-width="2"/>
  <circle cx="75" cy="46" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="75" y="50" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>

  <!-- Doble enlace C=CH2 hacia abajo -->
  <line x1="31" y1="56" x2="31" y2="74" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="39" y1="56" x2="39" y2="74" stroke="#0f172a" stroke-width="2.2"/>
  <text x="35" y="88" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">CH₂</text>
"""


# 11. PIRUVATO (Producto final de la Glucólisis)
PIRUVATO = """
  <!-- C1: Carboxilato COO- -->
  <text x="40" y="16" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: C=O (Grupo carbonilo) -->
  <text x="40" y="50" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">C</text>
  <line x1="47" y1="44" x2="66" y2="44" stroke="#0f172a" stroke-width="2"/>
  <line x1="47" y1="48" x2="66" y2="48" stroke="#0f172a" stroke-width="2"/>
  <text x="74" y="50" fill="#dc2626" font-size="13" font-weight="800">O</text>

  <!-- C3: Grupo metilo CH3 -->
  <line x1="40" y1="55" x2="40" y2="74" stroke="#0f172a" stroke-width="2.2"/>
  <text x="40" y="86" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">CH₃</text>
"""