#!/usr/bin/env python3
"""
ESTRUCTURAS QUÍMICAS (SVG) - BETA-OXIDACIÓN DE ÁCIDOS GRASOS
=============================================================
Diseñadas bajo el Manual de Estilo Editorial Científico del proyecto:
- Trazos oscuros nítidos (#0f172a) de 2.2 a 2.5 pt.
- Oxígenos y grupos carbonilo resaltados en rojo (#dc2626) en negrita.
- Grupo hidroxilo (-OH) resaltado en azul (#0284c7).
- Enlace tioéster (-S-CoA) con cápsula Coenzima A en color ámbar/púrpura (#7c3aed / #d97706).
- Carbonos alfa (C2) y beta (C3) claramente señalizados visualmente.
- Escala: 1 unidad = 1 px.
"""

# =============================================================================
# BLOQUE COENZIMA A (CÁPSULA SIMBÓLICA ELEGANTE)
# =============================================================================

def _badge_coa(x=0, y=0):
    return f"""
    <g transform="translate({x}, {y})">
      <rect x="0" y="-11" width="46" height="22" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.8"/>
      <text x="23" y="4" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9" text-anchor="middle" stroke="none">S-CoA</text>
    </g>
    """

# =============================================================================
# 1. ÁCIDO PALMÍTICO / PALMITATO (ÁCIDO GRASO LIBRE [16C])
# =============================================================================

PALMITATO = """
<g class="mol-palmitato" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo Carboxilato terminal C1 -->
  <text x="18" y="24" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
  <line x1="60" y1="19" x2="80" y2="19" />
  
  <!-- Carbono alfa (C2) y beta (C3) explícitos -->
  <line x1="80" y1="19" x2="91" y2="29" />
  <text x="98" y="38" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <text x="98" y="50" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">α</text>

  <line x1="106" y1="29" x2="112" y2="23" />
  <text x="120" y="22" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <text x="120" y="10" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">β</text>

  <!-- Cadena alifática en zigzag (C4 a C15) -->
  <polyline points="129,23 140,34 156,19 172,34 188,19 206,34" />
  
  <!-- Cola metilo terminal (CH3, C16) -->
  <line x1="206" y1="34" x2="224" y2="19" />
  <text x="228" y="22" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none">CH₃</text>
  <text x="160" y="52" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#64748b" stroke="none" text-anchor="middle">(CH₂)₁₂</text>
</g>
"""

# =============================================================================
# 2. PALMITOIL-COA (FORMA ACTIVADA [16C])
# =============================================================================

PALMITOIL_COA = """
<g class="mol-palmitoil-coa" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Carbonilo C1 (C=O) acoplado a tioéster -->
  <line x1="48" y1="28" x2="62" y2="28" stroke="#7c3aed" stroke-width="2.3"/>
  <text x="68" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="65" y1="20" x2="65" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="20" x2="71" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="7" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  
  <!-- Tioéster S-CoA a la izquierda -->
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9" stroke="none" text-anchor="middle">CoA-S</text>

  <!-- Carbono alfa (C2) y beta (C3) explícitos -->
  <line x1="74" y1="32" x2="83" y2="40" />
  <text x="90" y="48" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <text x="90" y="60" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">α</text>

  <line x1="98" y1="40" x2="105" y2="33" />
  <text x="114" y="32" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <text x="114" y="19" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">β</text>

  <!-- Cadena hidrocarbonada en zigzag -->
  <polyline points="124,33 136,44 152,28 170,44 188,28 208,44" />
  <line x1="208" y1="44" x2="226" y2="28" />
  <text x="230" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none">CH₃</text>
  <text x="155" y="58" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#64748b" stroke="none" text-anchor="middle">(CH₂)₁₂</text>
</g>
"""

# =============================================================================
# 3. CARNITINA Y PALMITOIL-CARNITINA (LANZADERA MITOCONDRIAL)
# =============================================================================

CARNITINA = """
<g class="mol-carnitina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo amonio cuaternario (trimetilamonio, C4) -->
  <text x="32" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0284c7" stroke="none" text-anchor="end">(CH₃)₃N⁺</text>
  <line x1="36" y1="20" x2="46" y2="20" />
  <text x="55" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  
  <!-- C3 con grupo -OH secundario explícito -->
  <line x1="64" y1="24" x2="70" y2="30" />
  <text x="76" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <line x1="76" y1="41" x2="76" y2="51" stroke="#0284c7" stroke-width="2.1"/>
  <text x="76" y="63" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">OH</text>

  <!-- C2 metileno y C1 carboxilato -->
  <line x1="84" y1="30" x2="90" y2="24" />
  <text x="100" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="110" y1="20" x2="118" y2="20" />
  <text x="122" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
</g>
"""

PALMITOIL_CARNITINA = """
<g class="mol-palmitoil-carnitina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Amonio cuaternario -->
  <text x="32" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0284c7" stroke="none" text-anchor="end">(CH₃)₃N⁺</text>
  <line x1="36" y1="20" x2="46" y2="20" />
  <text x="55" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>

  <!-- C3 con enlace éster a palmitato explícito -->
  <line x1="64" y1="24" x2="70" y2="30" />
  <text x="76" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <line x1="76" y1="41" x2="76" y2="49" stroke="#dc2626" stroke-width="2"/>
  <text x="76" y="59" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  
  <!-- Enlace éster hacia acilo -->
  <line x1="76" y1="62" x2="76" y2="70" />
  <text x="76" y="80" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="69" y1="74" x2="58" y2="74" stroke="#dc2626" stroke-width="1.8"/>
  <line x1="69" y1="78" x2="58" y2="78" stroke="#dc2626" stroke-width="1.8"/>
  <text x="54" y="80" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>
  <line x1="83" y1="78" x2="92" y2="83" />
  <text x="95" y="87" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#64748b" stroke="none">(CH₂)₁₄CH₃</text>

  <!-- C2 metileno y C1 carboxilato -->
  <line x1="84" y1="30" x2="90" y2="24" />
  <text x="100" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="110" y1="20" x2="118" y2="20" />
  <text x="122" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
</g>
"""

# =============================================================================
# 4. PASO 1 BETA-OX: TRANS-DELTA2-ENOIL-COA (DOBLE ENLACE ALFA-BETA)
# =============================================================================

TRANS_DELTA2_ENOIL_COA = """
<g class="mol-trans-enoil-coa" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Tioéster S-CoA -->
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9" stroke="none" text-anchor="middle">CoA-S</text>
  <line x1="48" y1="28" x2="62" y2="28" />

  <!-- C1 Carbonilo explícito -->
  <text x="68" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="65" y1="20" x2="65" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="20" x2="71" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="7" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C1 a C2 (alfa CH) -->
  <line x1="74" y1="32" x2="83" y2="40" />
  <text x="90" y="48" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <text x="90" y="60" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">α</text>

  <!-- DOBLE ENLACE TRANS (C2 = C3) con carbonos CH explícitos -->
  <line x1="99" y1="40" x2="110" y2="30" stroke="#ea580c" stroke-width="2.2" />
  <line x1="102" y1="44" x2="113" y2="34" stroke="#ea580c" stroke-width="2.2" />
  <text x="120" y="30" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <text x="120" y="17" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">β</text>
  
  <text x="108" y="54" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">trans-Δ²</text>

  <!-- Cadena hidrocarbonada restante (R) -->
  <line x1="129" y1="30" x2="140" y2="42" />
  <polyline points="140,42 158,26 176,42 196,26" />
  <text x="200" y="30" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none">R (C₁₆)</text>
</g>
"""

# =============================================================================
# 5. PASO 2 BETA-OX: L-BETA-HIDROXIACIL-COA (GRUPO -OH EN CARBONO BETA)
# =============================================================================

L_BETA_HIDROXIACIL_COA = """
<g class="mol-hidroxiacil-coa" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Tioéster S-CoA -->
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9" stroke="none" text-anchor="middle">CoA-S</text>
  <line x1="48" y1="28" x2="62" y2="28" />

  <!-- C1 Carbonilo explícito -->
  <text x="68" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="65" y1="20" x2="65" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="20" x2="71" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="7" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C1 a C2 (alfa CH2) -->
  <line x1="74" y1="32" x2="83" y2="40" />
  <text x="90" y="48" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <text x="90" y="60" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">α</text>

  <!-- C2 a C3 (beta CH con OH) -->
  <line x1="99" y1="40" x2="106" y2="32" />
  <text x="114" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <text x="114" y="18" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">β</text>
  
  <!-- Hidroxilo beta (-OH) resaltado en azul -->
  <line x1="114" y1="35" x2="114" y2="46" stroke="#0284c7" stroke-width="2.4"/>
  <text x="114" y="59" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">OH</text>

  <!-- Cadena hidrocarbonada restante (R) -->
  <line x1="123" y1="28" x2="134" y2="20" />
  <polyline points="134,20 152,36 170,20 188,36" />
  <text x="192" y="40" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none">R</text>
</g>
"""

# =============================================================================
# 6. PASO 3 BETA-OX: BETA-CETOACIL-COA (GRUPO C=O EN CARBONO BETA)
# =============================================================================

BETA_CETOACIL_COA = """
<g class="mol-cetoacil-coa" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Tioéster S-CoA -->
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9" stroke="none" text-anchor="middle">CoA-S</text>
  <line x1="48" y1="28" x2="62" y2="28" />

  <!-- C1 Carbonilo explícito -->
  <text x="68" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="65" y1="20" x2="65" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="20" x2="71" y2="10" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="7" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C1 a C2 (alfa CH2) -->
  <line x1="74" y1="32" x2="83" y2="40" />
  <text x="90" y="48" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <text x="90" y="60" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">α</text>

  <!-- C2 a C3 (beta carbonilo C=O explícito) -->
  <line x1="99" y1="40" x2="108" y2="32" />
  <text x="114" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <text x="114" y="18" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">β</text>
  
  <!-- Carbonilo beta (C=O) resaltado en rojo -->
  <line x1="111" y1="35" x2="111" y2="46" stroke="#dc2626" stroke-width="2.1"/>
  <line x1="117" y1="35" x2="117" y2="46" stroke="#dc2626" stroke-width="2.1"/>
  <text x="114" y="59" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- Sitio de corte tiolítico entre alfa y beta -->
  <line x1="102" y1="20" x2="102" y2="52" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="3 3"/>
  <text x="102" y="12" font-family="'Inter', sans-serif" font-size="8" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">✂ TIÓLISIS</text>

  <!-- Cadena hidrocarbonada restante (R) -->
  <line x1="120" y1="28" x2="132" y2="20" />
  <polyline points="132,20 150,36 168,20" />
  <text x="172" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none">R (C₁₄)</text>
</g>
"""

# =============================================================================
# 7. PRODUCTOS DE LA TIÓLISIS: ACETIL-COA Y ACIL-COA ACORTADO (-2C)
# =============================================================================

ACETIL_COA_BETA = """
<g class="mol-acetil-coa" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Tioéster S-CoA -->
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9" stroke="none" text-anchor="middle">CoA-S</text>
  <line x1="48" y1="28" x2="68" y2="28" />

  <!-- Carbonilo C1 -->
  <line x1="65" y1="28" x2="65" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="28" x2="71" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="8" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- Metilo C2 -->
  <line x1="68" y1="28" x2="88" y2="40" />
  <text x="92" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none">CH₃</text>
</g>
"""

MIRISTOIL_COA = """
<g class="mol-miristoil-coa" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Nueva Coenzima A incorporada -->
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9" stroke="none" text-anchor="middle">CoA-S</text>
  <line x1="48" y1="28" x2="68" y2="28" />

  <!-- Carbonilo C1 -->
  <line x1="65" y1="28" x2="65" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="28" x2="71" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="8" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- Cadena acil acortada (n-2) -->
  <polyline points="68,28 88,44 108,28 128,44 148,28 168,44" />
  <line x1="168" y1="44" x2="186" y2="28" />
  <text x="190" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none">CH₃</text>
  <text x="118" y="58" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#d97706" stroke="none" text-anchor="middle">Acil-CoA acortado [14C]</text>
</g>
"""
