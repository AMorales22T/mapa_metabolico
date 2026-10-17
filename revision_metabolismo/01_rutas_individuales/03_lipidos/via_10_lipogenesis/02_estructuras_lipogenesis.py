#!/usr/bin/env python3
"""
ESTRUCTURAS QUÍMICAS (SVG) - LIPOGÉNESIS (SÍNTESIS DE NOVO DE ÁCIDOS GRASOS)
=============================================================================
Diseñadas bajo el Manual de Estilo Editorial Científico del proyecto:
- Trazos oscuros nítidos (#0f172a) de 2.2 a 2.5 pt.
- Oxígenos y grupos carbonilo resaltados en rojo (#dc2626) en negrita.
- Grupos carboxilato (COO⁻) en rojo (#dc2626).
- Grupos hidroxilo (-OH) en azul (#0284c7).
- Cápsula Coenzima A en color púrpura (#7c3aed / #ede9fe).
- Cápsula ACP (Proteína Portadora de Acilos con 4'-fosfopanteteína) en verde azulado (#0d9488 / #ccfbf1).
- Carbonos alfa (C2) y beta (C3) claramente señalizados visualmente.
"""

# =============================================================================
# 1. CITRATO (6 Carbonos, Tricarboxilato)
# =============================================================================

CITRATO = """
<g class="mol-citrato" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato superior -->
  <text x="18" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">⁻OOC</text>
  <line x1="55" y1="12" x2="72" y2="24" />

  <!-- C2 metileno hacia C3 central explícito -->
  <text x="81" y="32" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="91" y1="28" x2="98" y2="28" />
  <text x="105" y="32" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  
  <!-- C3 central con -OH y -COO⁻ central -->
  <line x1="105" y1="20" x2="105" y2="10" stroke="#0284c7" stroke-width="2.2"/>
  <text x="105" y="6" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">OH</text>
  
  <line x1="105" y1="36" x2="105" y2="48" stroke="#dc2626" stroke-width="2.1"/>
  <text x="105" y="62" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>

  <!-- C3 a C4 metileno y C5 carboxilato -->
  <line x1="112" y1="28" x2="120" y2="28" />
  <text x="130" y="32" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="140" y1="24" x2="155" y2="12" />
  <text x="160" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
</g>
"""

# =============================================================================
# 2. ACETIL-COA (Citosólico, 2 Carbonos)
# =============================================================================

ACETIL_COA_LIPO = """
<g class="mol-acetil-coa" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Tioéster S-CoA a la izquierda -->
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9" stroke="none" text-anchor="middle">CoA-S</text>
  <line x1="48" y1="28" x2="65" y2="28" stroke="#7c3aed" stroke-width="2.3"/>

  <!-- Carbonilo C1 explícito -->
  <text x="72" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="69" y1="20" x2="69" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <line x1="75" y1="20" x2="75" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <text x="72" y="7" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- Metilo C2 -->
  <line x1="78" y1="32" x2="94" y2="40" />
  <text x="98" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none">CH₃</text>
</g>
"""

# =============================================================================
# 3. MALONIL-COA (3 Carbonos, Sustrato Clave de Elongación)
# =============================================================================

MALONIL_COA = """
<g class="mol-malonil-coa" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo Carboxilato terminal libre (COO⁻) que proveerá el CO2 -->
  <text x="18" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">⁻OOC</text>
  <line x1="56" y1="20" x2="70" y2="30" />
  
  <!-- Carbono C2 metileno central explícito -->
  <text x="80" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">CH₂</text>

  <!-- C1 Carbonilo tioéster explícito -->
  <line x1="90" y1="30" x2="101" y2="22" />
  <text x="108" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="105" y1="13" x2="105" y2="5" stroke="#dc2626" stroke-width="2.1"/>
  <line x1="111" y1="13" x2="111" y2="5" stroke="#dc2626" stroke-width="2.1"/>
  <text x="108" y="2" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- Tioéster S-CoA -->
  <line x1="115" y1="20" x2="132" y2="20" stroke="#7c3aed" stroke-width="2.3"/>
  <rect x="132" y="9" width="46" height="22" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="155" y="24" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9" stroke="none" text-anchor="middle">S-CoA</text>
</g>
"""

# =============================================================================
# 4. ACETOACETIL-ACP (Paso 1: Producto de Condensación [4C])
# =============================================================================

ACETOACETIL_ACP = """
<g class="mol-acetoacetil-acp" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Cápsula ACP a la izquierda -->
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f766e" stroke="none" text-anchor="middle">ACP-S</text>
  <line x1="48" y1="28" x2="61" y2="28" stroke="#0d9488" stroke-width="2.3"/>

  <!-- C1 Carbonilo explícito -->
  <text x="68" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="65" y1="20" x2="65" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="20" x2="71" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="7" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C2 (alfa) metileno explícito -->
  <line x1="74" y1="32" x2="82" y2="40" />
  <text x="90" y="48" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <text x="90" y="59" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#ea580c" stroke="none" text-anchor="middle">α</text>

  <!-- C3 (beta) Carbonilo ceto explícito -->
  <line x1="99" y1="40" x2="106" y2="32" />
  <text x="112" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="109" y1="20" x2="109" y2="10" stroke="#dc2626" stroke-width="2.1"/>
  <line x1="115" y1="20" x2="115" y2="10" stroke="#dc2626" stroke-width="2.1"/>
  <text x="112" y="7" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <text x="112" y="44" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#0284c7" stroke="none" text-anchor="middle">β</text>

  <!-- C4 Metilo terminal -->
  <line x1="118" y1="32" x2="130" y2="40" />
  <text x="134" y="44" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a" stroke="none">CH₃</text>
</g>
"""

# =============================================================================
# 5. D-BETA-HIDROXIACIL-ACP (Paso 2: Producto de 1ª Reducción por KR [4C])
# =============================================================================

D_BETA_HIDROXIACIL_ACP = """
<g class="mol-hidroxiacil-acp" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- ACP-S -->
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f766e" stroke="none" text-anchor="middle">ACP-S</text>
  <line x1="48" y1="28" x2="61" y2="28" stroke="#0d9488" stroke-width="2.3"/>

  <!-- C1 Carbonilo explícito -->
  <text x="68" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="65" y1="20" x2="65" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="20" x2="71" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="7" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C2 (alfa CH2) -->
  <line x1="74" y1="32" x2="82" y2="40" />
  <text x="90" y="48" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <text x="90" y="59" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#ea580c" stroke="none" text-anchor="middle">α</text>

  <!-- C3 (beta CH con grupo -OH isómero D) -->
  <line x1="99" y1="40" x2="106" y2="32" />
  <text x="114" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <line x1="114" y1="35" x2="114" y2="46" stroke="#0284c7" stroke-width="2.4"/>
  <text x="114" y="59" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">OH</text>
  <text x="114" y="19" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">D-β</text>

  <!-- C4 Metilo terminal -->
  <line x1="123" y1="28" x2="132" y2="22" />
  <text x="136" y="24" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a" stroke="none">CH₃</text>
</g>
"""

# =============================================================================
# 6. TRANS-DELTA2-ENOIL-ACP (Paso 3: Producto de Deshidratación por DH [4C])
# =============================================================================

TRANS_DELTA2_ENOIL_ACP = """
<g class="mol-trans-enoil-acp" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- ACP-S -->
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f766e" stroke="none" text-anchor="middle">ACP-S</text>
  <line x1="48" y1="28" x2="61" y2="28" stroke="#0d9488" stroke-width="2.3"/>

  <!-- C1 Carbonilo explícito -->
  <text x="68" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="65" y1="20" x2="65" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="20" x2="71" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="7" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C2 (alfa CH) a C3 (beta CH): DOBLE ENLACE TRANS (CH=CH) -->
  <line x1="74" y1="32" x2="83" y2="40" />
  <text x="90" y="48" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  
  <line x1="99" y1="40" x2="110" y2="30" stroke="#ea580c" stroke-width="2.2"/>
  <line x1="102" y1="44" x2="113" y2="34" stroke="#ea580c" stroke-width="2.2"/>
  <text x="120" y="30" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>

  <text x="90" y="59" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">α</text>
  <text x="120" y="17" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">β</text>
  <text x="108" y="54" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">trans-Δ²</text>

  <!-- C4 Metilo terminal -->
  <line x1="129" y1="30" x2="140" y2="40" />
  <text x="144" y="44" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a" stroke="none">CH₃</text>
</g>
"""

# =============================================================================
# 7. BUTIRIL-ACP (Paso 4: Producto de 2ª Reducción por ER [4C / Ciclo 1 completado])
# =============================================================================

BUTIRIL_ACP = """
<g class="mol-butiril-acp" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- ACP-S -->
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ccfbf1" stroke="#0d9488" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f766e" stroke="none" text-anchor="middle">ACP-S</text>
  <line x1="48" y1="28" x2="61" y2="28" stroke="#0d9488" stroke-width="2.3"/>

  <!-- C1 Carbonilo explícito -->
  <text x="68" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="65" y1="20" x2="65" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="20" x2="71" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="7" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- Cadena saturada reducida (C2 a C4) con CH2 explícitos -->
  <line x1="74" y1="32" x2="82" y2="40" />
  <text x="90" y="48" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="99" y1="40" x2="106" y2="32" />
  <text x="114" y="32" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="123" y1="32" x2="132" y2="42" />
  
  <text x="136" y="48" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a" stroke="none">CH₃</text>
  <text x="102" y="60" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#0d9488" stroke="none" text-anchor="middle">Acilo saturado (+2C)</text>
</g>
"""

# =============================================================================
# 8. PALMITATO LIBRE (Producto Final de la Tioesterasa [16C])
# =============================================================================

PALMITATO_LIBRE = """
<g class="mol-palmitato-libre" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo Carboxilato terminal C1 libre -->
  <text x="18" y="24" font-family="'Inter', sans-serif" font-size="13.5" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
  <line x1="60" y1="19" x2="80" y2="19" />
  
  <!-- Carbono alfa y beta explícitos -->
  <line x1="80" y1="19" x2="91" y2="29" />
  <text x="98" y="38" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <text x="98" y="49" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">α</text>

  <line x1="106" y1="29" x2="112" y2="23" />
  <text x="120" y="22" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <text x="120" y="11" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">β</text>

  <!-- Cadena en zigzag (C4 a C15) -->
  <polyline points="129,23 140,34 156,19 172,34 188,19 206,34" />
  <line x1="206" y1="34" x2="224" y2="19" />
  
  <text x="228" y="22" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none">CH₃</text>
  <text x="160" y="52" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#64748b" stroke="none" text-anchor="middle">(CH₂)₁₂</text>
</g>
"""
