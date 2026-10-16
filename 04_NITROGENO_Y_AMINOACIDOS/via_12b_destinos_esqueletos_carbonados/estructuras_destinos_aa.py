#!/usr/bin/env python3
"""
ESTRUCTURAS QUÍMICAS VECTORIALES SVG - DESTINOS DE LOS ESQUELETOS CARBONADOS DE AMINOÁCIDOS
========================================================================================
Manual de Estilo Editorial Bioquímico Científico:
- 100% de los carbonos explicitados con texto ('C', 'CH', 'CH₂', 'COO⁻', 'CH₃') o enlaces nítidos.
- CERO puntos o bolitas negras como átomos de carbono.
- CERO rectángulos contenedores o cajas artificiales.
- Oxígenos en rojo (#dc2626), nitrógenos en azul cobalto (#2563eb), azufre en ámbar (#d97706).
- Grupos fosfato en cápsula circular con símbolo Ⓟ (#ea580c, #ffedd5).
- Trazos de enlace en grafito oscuro (#0f172a, stroke-width: 2.2px).
- Cargas y estados fisiológicos a pH 7.4.
"""

# =============================================================================
# 1. LOS 7 INTERMEDIARIOS METABÓLICOS CENTRALES
# =============================================================================

# 1. PIRUVATO [3C] (α-cetoácido de 3 carbonos)
PIRUVATO = """
<g class="mol-piruvato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="35" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="35" y1="22" x2="35" y2="38" />

  <!-- C2: Carbonilo (C=O) -->
  <text x="35" y="52" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="43" y1="46" x2="60" y2="46" stroke="#dc2626" stroke-width="2.2" />
  <line x1="43" y1="52" x2="60" y2="52" stroke="#dc2626" stroke-width="2.2" />
  <text x="68" y="52" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none" text-anchor="start">O</text>

  <!-- C3: Metilo inferior -->
  <line x1="35" y1="57" x2="35" y2="72" />
  <text x="35" y="86" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₃</text>
</g>
"""

# 2. ACETIL-CoA [2C] (Tioéster activado)
ACETIL_COA = """
<g class="mol-acetil-coa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C2: Metilo izquierdo -->
  <text x="18" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₃C</text>
  <line x1="34" y1="34" x2="48" y2="34" />

  <!-- C1: Carbonilo (C=O) -->
  <text x="56" y="38" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="53" y1="26" x2="53" y2="12" stroke="#dc2626" stroke-width="2.2" />
  <line x1="59" y1="26" x2="59" y2="12" stroke="#dc2626" stroke-width="2.2" />
  <text x="56" y="8" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- Enlace tioéster (~S) -->
  <path d="M 64 34 Q 72 31 76 34" stroke="#d97706" stroke-width="2.2" />
  <text x="86" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#d97706" stroke="none" text-anchor="middle">S</text>
  <line x1="94" y1="34" x2="108" y2="34" stroke="#d97706" stroke-width="2" />
  <text x="124" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#475569" stroke="none" text-anchor="middle">CoA</text>
</g>
"""

# 3. ACETOACETIL-CoA [4C] (Cuerpo cetónico activado)
ACETOACETIL_COA = """
<g class="mol-acetoacetil-coa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C4: Metilo izquierdo -->
  <text x="18" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₃C</text>
  <line x1="33" y1="34" x2="45" y2="34" />

  <!-- C3: Carbonilo β (C=O) -->
  <text x="53" y="38" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="50" y1="26" x2="50" y2="12" stroke="#dc2626" stroke-width="2.2" />
  <line x1="56" y1="26" x2="56" y2="12" stroke="#dc2626" stroke-width="2.2" />
  <text x="53" y="8" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C2: Metileno alfa (-CH2-) -->
  <line x1="61" y1="34" x2="74" y2="34" />
  <text x="88" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="102" y1="34" x2="114" y2="34" />

  <!-- C1: Carbonilo tioéster -->
  <text x="122" y="38" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="119" y1="26" x2="119" y2="12" stroke="#dc2626" stroke-width="2.2" />
  <line x1="125" y1="26" x2="125" y2="12" stroke="#dc2626" stroke-width="2.2" />
  <text x="122" y="8" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- ~S-CoA -->
  <path d="M 130 34 Q 138 31 142 34" stroke="#d97706" stroke-width="2.2" />
  <text x="152" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#d97706" stroke="none" text-anchor="middle">S</text>
  <line x1="160" y1="34" x2="172" y2="34" stroke="#d97706" stroke-width="2" />
  <text x="188" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#475569" stroke="none" text-anchor="middle">CoA</text>
</g>
"""

# 4. α-CETOGLUTARATO [5C] (Dicarboxilato con cetona en C2)
ALFACETOGLUTARATO = """
<g class="mol-alfacetoglutarato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="38" />

  <!-- C2: Carbonilo (C=O) -->
  <text x="40" y="52" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="48" y1="46" x2="65" y2="46" stroke="#dc2626" stroke-width="2.2" />
  <line x1="48" y1="52" x2="65" y2="52" stroke="#dc2626" stroke-width="2.2" />
  <text x="73" y="52" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none" text-anchor="start">O</text>

  <!-- C3: CH2 -->
  <line x1="40" y1="57" x2="40" y2="72" />
  <text x="40" y="86" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- C4: CH2 -->
  <line x1="40" y1="91" x2="40" y2="105" />
  <text x="40" y="119" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- C5: Carboxilato Inferior -->
  <line x1="40" y1="124" x2="40" y2="138" />
  <text x="40" y="152" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""

# 5. SUCCINIL-CoA [4C]
SUCCINIL_COA = """
<g class="mol-succinil-coa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C4: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="38" />

  <!-- C3: CH2 -->
  <text x="40" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="40" y1="57" x2="40" y2="72" />

  <!-- C2: CH2 -->
  <text x="40" y="86" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="40" y1="91" x2="40" y2="105" />

  <!-- C1: Carbonilo tioéster -->
  <text x="40" y="119" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="48" y1="113" x2="65" y2="113" stroke="#dc2626" stroke-width="2.2" />
  <line x1="48" y1="119" x2="65" y2="119" stroke="#dc2626" stroke-width="2.2" />
  <text x="73" y="119" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none" text-anchor="start">O</text>

  <!-- Enlace ~S-CoA abajo -->
  <line x1="40" y1="124" x2="40" y2="136" />
  <text x="40" y="150" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#d97706" stroke="none" text-anchor="middle">S-CoA</text>
</g>
"""

# 6. FUMARATO [4C] (Trans-dicarboxilato con doble enlace)
FUMARATO = """
<g class="mol-fumarato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Carboxilato 1 (Izquierda superior) -->
  <text x="18" y="20" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">⁻OOC</text>
  <line x1="38" y1="20" x2="52" y2="34" />

  <!-- C2: CH (trans) -->
  <text x="60" y="42" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>

  <!-- Doble enlace trans -->
  <line x1="72" y1="36" x2="90" y2="36" stroke="#0f172a" stroke-width="2.4" />
  <line x1="72" y1="42" x2="90" y2="42" stroke="#0f172a" stroke-width="2.4" />

  <!-- C3: HC -->
  <text x="102" y="42" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">HC</text>
  <line x1="112" y1="38" x2="126" y2="52" />

  <!-- Carboxilato 2 (Derecha inferior) -->
  <text x="144" y="58" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""

# 7. OXALACETATO [4C]
OXALACETATO = """
<g class="mol-oxalacetato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="38" />

  <!-- C2: Carbonilo (C=O) -->
  <text x="40" y="52" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="48" y1="46" x2="65" y2="46" stroke="#dc2626" stroke-width="2.2" />
  <line x1="48" y1="52" x2="65" y2="52" stroke="#dc2626" stroke-width="2.2" />
  <text x="73" y="52" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none" text-anchor="start">O</text>

  <!-- C3: Metileno (-CH2-) -->
  <line x1="40" y1="57" x2="40" y2="72" />
  <text x="40" y="86" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- C4: Carboxilato Inferior -->
  <line x1="40" y1="91" x2="40" y2="105" />
  <text x="40" y="119" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""

# =============================================================================
# 2. MOLÉCULAS DE INTERÉS CLÍNICO Y RAMIFICACIONES CLAVE
# =============================================================================

# L-FENILALANINA [9C]
FENILALANINA = """
<g class="mol-fenilalanina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: COO- -->
  <text x="45" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="45" y1="22" x2="45" y2="38" />

  <!-- C2: CH con NH3+ -->
  <text x="45" y="50" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <line x1="56" y1="46" x2="72" y2="46" stroke="#2563eb" stroke-width="2" />
  <text x="88" y="50" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>

  <!-- C3: CH2 -->
  <line x1="45" y1="55" x2="45" y2="70" />
  <text x="45" y="84" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- Anillo aromático fenilo (Hexágono nítido sin rectángulos) -->
  <line x1="45" y1="89" x2="45" y2="102" />
  <polygon points="45,102 62,112 62,132 45,142 28,132 28,112" stroke="#0f172a" stroke-width="2" fill="none" />
  <circle cx="45" cy="122" r="10" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="4 3" fill="none" />
</g>
"""

# L-TIROSINA [9C] (Con grupo -OH fenólico en para)
TIROSINA = """
<g class="mol-tirosina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: COO- -->
  <text x="45" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="45" y1="22" x2="45" y2="38" />

  <!-- C2: CH con NH3+ -->
  <text x="45" y="50" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <line x1="56" y1="46" x2="72" y2="46" stroke="#2563eb" stroke-width="2" />
  <text x="88" y="50" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>

  <!-- C3: CH2 -->
  <line x1="45" y1="55" x2="45" y2="70" />
  <text x="45" y="84" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- Anillo fenólico con -OH -->
  <line x1="45" y1="89" x2="45" y2="102" />
  <polygon points="45,102 62,112 62,132 45,142 28,132 28,112" stroke="#0f172a" stroke-width="2" fill="none" />
  <circle cx="45" cy="122" r="10" stroke="#0f172a" stroke-width="1.6" stroke-dasharray="4 3" fill="none" />
  
  <!-- Enlace C4-OH -->
  <line x1="45" y1="142" x2="45" y2="155" stroke="#dc2626" stroke-width="2.2" />
  <text x="45" y="169" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">OH</text>
</g>
"""

# PROPIONIL-CoA [3C] (Vía de degradación de Met, Val, Ile, Thr)
PROPIONIL_COA = """
<g class="mol-propionil-coa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="18" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₃C</text>
  <line x1="33" y1="34" x2="46" y2="34" />
  <text x="59" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="72" y1="34" x2="85" y2="34" />
  <text x="93" y="38" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="90" y1="26" x2="90" y2="12" stroke="#dc2626" stroke-width="2.2" />
  <line x1="96" y1="26" x2="96" y2="12" stroke="#dc2626" stroke-width="2.2" />
  <text x="93" y="8" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <path d="M 101 34 Q 109 31 113 34" stroke="#d97706" stroke-width="2.2" />
  <text x="123" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#d97706" stroke="none" text-anchor="middle">S</text>
  <line x1="131" y1="34" x2="143" y2="34" stroke="#d97706" stroke-width="2" />
  <text x="159" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#475569" stroke="none" text-anchor="middle">CoA</text>
</g>
"""

# D/L-METILMALONIL-CoA [4C] (Intermediario carboxilado entre PCC y MCM)
METILMALONIL_COA = """
<g class="mol-metilmalonil-coa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="18" y="36" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">⁻OOC</text>
  <line x1="38" y1="32" x2="50" y2="32" />
  <text x="60" y="36" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <line x1="60" y1="22" x2="60" y2="12" />
  <text x="60" y="8" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0284c7" stroke="none" text-anchor="middle">CH₃</text>
  <line x1="70" y1="32" x2="82" y2="32" />
  <text x="90" y="36" font-family="'Inter', sans-serif" font-size="12.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="87" y1="24" x2="87" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <line x1="93" y1="24" x2="93" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <text x="90" y="8" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <path d="M 98 32 Q 105 29 109 32" stroke="#d97706" stroke-width="2.2" />
  <text x="118" y="36" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#d97706" stroke="none" text-anchor="middle">S</text>
  <line x1="125" y1="32" x2="136" y2="32" stroke="#d97706" stroke-width="2" />
  <text x="150" y="36" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#475569" stroke="none" text-anchor="middle">CoA</text>
</g>
"""


# L-HOMOCISTEÍNA [4C] (Intermediario tiol clave en metionina)
HOMOCISTEINA = """
<g class="mol-homocisteina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="35" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="35" y1="22" x2="35" y2="36" />
  <text x="35" y="48" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <line x1="45" y1="45" x2="59" y2="45" stroke="#2563eb" stroke-width="2" />
  <text x="74" y="49" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>
  <line x1="35" y1="53" x2="35" y2="67" />
  <text x="35" y="79" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="35" y1="84" x2="35" y2="98" />
  <text x="35" y="110" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="35" y1="115" x2="35" y2="128" stroke="#d97706" stroke-width="2.2" />
  <text x="35" y="141" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#d97706" stroke="none" text-anchor="middle">SH</text>
</g>
"""

# L-GLUTAMATO [5C]
L_GLUTAMATO = """
<g class="mol-glutamato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="35" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="35" y1="22" x2="35" y2="36" />
  <text x="35" y="48" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <line x1="45" y1="45" x2="59" y2="45" stroke="#2563eb" stroke-width="2" />
  <text x="74" y="49" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>
  <line x1="35" y1="53" x2="35" y2="67" />
  <text x="35" y="79" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="35" y1="84" x2="35" y2="98" />
  <text x="35" y="110" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="35" y1="115" x2="35" y2="128" />
  <text x="35" y="141" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""

# L-ASPARTATO [4C]
L_ASPARTATO = """
<g class="mol-aspartato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="35" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="35" y1="22" x2="35" y2="36" />
  <text x="35" y="48" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <line x1="45" y1="45" x2="59" y2="45" stroke="#2563eb" stroke-width="2" />
  <text x="74" y="49" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>
  <line x1="35" y1="53" x2="35" y2="67" />
  <text x="35" y="79" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="35" y1="84" x2="35" y2="98" />
  <text x="35" y="110" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""
