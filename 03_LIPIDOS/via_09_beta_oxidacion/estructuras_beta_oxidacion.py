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
  
  <!-- Carbono alfa (C2) y beta (C3) -->
  <line x1="80" y1="19" x2="98" y2="34" />
  <circle cx="98" cy="34" r="3" fill="#ea580c" stroke="none"/>
  <text x="98" y="50" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">α</text>

  <line x1="98" y1="34" x2="116" y2="19" />
  <circle cx="116" cy="19" r="3" fill="#0284c7" stroke="none"/>
  <text x="116" y="10" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">β</text>

  <!-- Cadena alifática en zigzag (C4 a C15) -->
  <polyline points="116,19 134,34 152,19 170,34 188,19 206,34" />
  
  <!-- Cola metilo terminal (CH3, C16) -->
  <line x1="206" y1="34" x2="224" y2="19" />
  <text x="228" y="22" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none">CH₃</text>
  <text x="152" y="52" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#64748b" stroke="none" text-anchor="middle">(CH₂)₁₂</text>
</g>
"""

# =============================================================================
# 2. PALMITOIL-COA (FORMA ACTIVADA [16C])
# =============================================================================

PALMITOIL_COA = """
<g class="mol-palmitoil-coa" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Carbonilo C1 (C=O) acoplado a tioéster -->
  <line x1="48" y1="28" x2="68" y2="28" />
  <line x1="65" y1="28" x2="65" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="28" x2="71" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="8" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  
  <!-- Tioéster S-CoA a la izquierda -->
  <line x1="68" y1="28" x2="48" y2="28" stroke="#7c3aed" stroke-width="2.3"/>
  <rect x="2" y="17" width="46" height="22" rx="11" fill="#ede9fe" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="25" y="32" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#6d28d9" stroke="none" text-anchor="middle">CoA-S</text>

  <!-- Carbono alfa (C2) y beta (C3) -->
  <line x1="68" y1="28" x2="88" y2="44" />
  <circle cx="88" cy="44" r="3" fill="#ea580c" stroke="none"/>
  <text x="88" y="59" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">α</text>

  <line x1="88" y1="44" x2="108" y2="28" />
  <circle cx="108" cy="28" r="3" fill="#0284c7" stroke="none"/>
  <text x="108" y="19" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">β</text>

  <!-- Cadena hidrocarbonada en zigzag -->
  <polyline points="108,28 128,44 148,28 168,44 188,28 208,44" />
  <line x1="208" y1="44" x2="226" y2="28" />
  <text x="230" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none">CH₃</text>
  <text x="148" y="58" font-family="'Inter', sans-serif" font-size="8.5" font-weight="700" fill="#64748b" stroke="none" text-anchor="middle">(CH₂)₁₂</text>
</g>
"""

# =============================================================================
# 3. CARNITINA Y PALMITOIL-CARNITINA (LANZADERA MITOCONDRIAL)
# =============================================================================

CARNITINA = """
<g class="mol-carnitina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo amonio cuaternario (trimetilamonio, C4) -->
  <text x="32" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0284c7" stroke="none" text-anchor="end">(CH₃)₃N⁺</text>
  <line x1="36" y1="20" x2="56" y2="20" />
  
  <!-- C3 con grupo -OH secundario -->
  <line x1="56" y1="20" x2="74" y2="34" />
  <circle cx="74" cy="34" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="74" y1="34" x2="74" y2="50" stroke="#0284c7" stroke-width="2.1"/>
  <text x="74" y="62" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">OH</text>

  <!-- C2 metileno y C1 carboxilato -->
  <line x1="74" y1="34" x2="94" y2="20" />
  <line x1="94" y1="20" x2="114" y2="20" />
  <text x="118" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
</g>
"""

PALMITOIL_CARNITINA = """
<g class="mol-palmitoil-carnitina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Amonio cuaternario -->
  <text x="32" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0284c7" stroke="none" text-anchor="end">(CH₃)₃N⁺</text>
  <line x1="36" y1="20" x2="56" y2="20" />

  <!-- C3 con enlace éster a palmitato -->
  <line x1="56" y1="20" x2="74" y2="34" />
  <circle cx="74" cy="34" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="74" y1="34" x2="74" y2="48" stroke="#dc2626" stroke-width="2"/>
  <text x="74" y="58" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  
  <!-- Enlace éster hacia acilo -->
  <line x1="74" y1="61" x2="74" y2="72" />
  <line x1="74" y1="72" x2="62" y2="72" stroke="#dc2626" stroke-width="2"/>
  <text x="56" y="75" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O=C</text>
  <line x1="74" y1="72" x2="88" y2="82" />
  <text x="92" y="86" font-family="'Inter', sans-serif" font-size="9" font-weight="700" fill="#64748b" stroke="none">—(CH₂)₁₄CH₃</text>

  <!-- C2 metileno y C1 carboxilato -->
  <line x1="74" y1="34" x2="94" y2="20" />
  <line x1="94" y1="20" x2="114" y2="20" />
  <text x="118" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
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
  <line x1="48" y1="28" x2="68" y2="28" />

  <!-- C1 Carbonilo -->
  <line x1="65" y1="28" x2="65" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="28" x2="71" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="8" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C1 a C2 (alfa) -->
  <line x1="68" y1="28" x2="90" y2="44" />
  <circle cx="90" cy="44" r="3" fill="#ea580c" stroke="none"/>
  <text x="86" y="59" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#ea580c" stroke="none">α</text>

  <!-- DOBLE ENLACE TRANS (C2 = C3) con geometría trans claramente visible -->
  <line x1="90" y1="42" x2="114" y2="26" stroke="#ea580c" stroke-width="2.4" />
  <line x1="93" y1="46" x2="117" y2="30" stroke="#ea580c" stroke-width="2.4" />
  <circle cx="114" cy="26" r="3" fill="#0284c7" stroke="none"/>
  <text x="114" y="17" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">β</text>
  
  <text x="103" y="52" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">trans-Δ²</text>

  <!-- Cadena hidrocarbonada restante (R) -->
  <line x1="114" y1="26" x2="136" y2="42" />
  <polyline points="136,42 156,26 176,42 196,26" />
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
  <line x1="48" y1="28" x2="68" y2="28" />

  <!-- C1 Carbonilo -->
  <line x1="65" y1="28" x2="65" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="28" x2="71" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="8" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C1 a C2 (alfa) -->
  <line x1="68" y1="28" x2="88" y2="44" />
  <circle cx="88" cy="44" r="3" fill="#ea580c" stroke="none"/>
  <text x="88" y="59" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">α</text>

  <!-- C2 a C3 (beta con OH) -->
  <line x1="88" y1="44" x2="108" y2="28" />
  <circle cx="108" cy="28" r="3" fill="#0284c7" stroke="none"/>
  <text x="108" y="18" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">β</text>
  
  <!-- Hidroxilo beta (-OH) resaltado en azul -->
  <line x1="108" y1="28" x2="108" y2="44" stroke="#0284c7" stroke-width="2.4"/>
  <text x="108" y="58" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">OH</text>

  <!-- Cadena hidrocarbonada restante (R) -->
  <line x1="108" y1="28" x2="128" y2="20" />
  <polyline points="128,20 148,36 168,20 188,36" />
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
  <line x1="48" y1="28" x2="68" y2="28" />

  <!-- C1 Carbonilo -->
  <line x1="65" y1="28" x2="65" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <line x1="71" y1="28" x2="71" y2="12" stroke="#dc2626" stroke-width="2.1" />
  <text x="68" y="8" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C1 a C2 (alfa) -->
  <line x1="68" y1="28" x2="88" y2="44" />
  <circle cx="88" cy="44" r="3" fill="#ea580c" stroke="none"/>
  <text x="88" y="59" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">α</text>

  <!-- C2 a C3 (beta carbonilo C=O) -->
  <line x1="88" y1="44" x2="108" y2="28" />
  <circle cx="108" cy="28" r="3" fill="#0284c7" stroke="none"/>
  <text x="108" y="18" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">β</text>
  
  <!-- Carbonilo beta (C=O) resaltado en rojo -->
  <line x1="105" y1="28" x2="105" y2="44" stroke="#dc2626" stroke-width="2.1"/>
  <line x1="111" y1="28" x2="111" y2="44" stroke="#dc2626" stroke-width="2.1"/>
  <text x="108" y="58" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- Sitio de corte tiolítico entre alfa y beta -->
  <line x1="98" y1="20" x2="98" y2="52" stroke="#dc2626" stroke-width="1.8" stroke-dasharray="3 3"/>
  <text x="98" y="12" font-family="'Inter', sans-serif" font-size="8" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">✂ TIÓLISIS</text>

  <!-- Cadena hidrocarbonada restante (R) -->
  <line x1="108" y1="28" x2="128" y2="20" />
  <polyline points="128,20 148,36 168,20" />
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
