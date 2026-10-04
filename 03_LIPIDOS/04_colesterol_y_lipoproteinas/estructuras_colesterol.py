#!/usr/bin/env python3
"""
ESTRUCTURAS QUÍMICAS (SVG) - SÍNTESIS DE COLESTEROL Y VÍA DEL MEVALONATO
========================================================================
Diseñadas bajo el Manual de Estilo Editorial Científico del proyecto:
- Trazos oscuros nítidos (#0f172a) de 2.2 a 2.5 pt.
- Oxígenos y carbonilos en rojo (#dc2626).
- Grupos hidroxilo (-OH) en azul (#0284c7).
- Grupos pirofosfato / fosfato (-O-PP) en naranja ámbar (#d97706 / #ea580c).
- Cápsula Coenzima A en púrpura (#7c3aed / #ede9fe).
- Ciclopentanoperhidrofenantreno esteroideo limpio y estilizado (anillos A, B, C, D).
- Cero polígonos cerrados no deseados: fill="none" en polilíneas y trazos.
"""

# =============================================================================
# 1. ACETOACETIL-COA (4C) - Condensación de 2 Acetil-CoA
# =============================================================================
ACETOACETIL_COA_COLEST = """
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
# 2. HMG-COA CITOSÓLICO (6C) - Sustrato del marcapasos HMGCR
# =============================================================================
HMG_COA_CITOSOL = """
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
# 3. MEVALONATO (6C) - Producto irreversible de la HMG-CoA Reductasa
# =============================================================================
MEVALONATO = """
<g class="mol-mevalonato" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato terminal -->
  <text x="8" y="22" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">⁻OOC</text>
  <line x1="46" y1="18" x2="72" y2="34" />

  <!-- C2 metileno -->
  <line x1="72" y1="34" x2="98" y2="34" />

  <!-- C3 central ramificado con OH y CH3 -->
  <circle cx="98" cy="34" r="3.2" fill="#0f172a" stroke="none"/>
  <!-- C3 OH arriba -->
  <line x1="98" y1="34" x2="98" y2="14" stroke="#0284c7" stroke-width="2.2"/>
  <text x="98" y="9" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0284c7" stroke="none" text-anchor="middle">OH</text>
  <!-- C3 CH3 abajo -->
  <line x1="98" y1="34" x2="98" y2="52" />
  <text x="98" y="65" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₃</text>

  <!-- C4 metileno -->
  <line x1="98" y1="34" x2="124" y2="34" />

  <!-- C5 alcohol primario terminal (CH2-CH2-OH reducido de tioéster) -->
  <line x1="124" y1="34" x2="148" y2="20" />
  <text x="152" y="23" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0284c7" stroke="none">CH₂OH</text>
</g>
"""

# =============================================================================
# 4. ISOPENTENIL PIROFOSFATO - IPP (5C) - Unidad Isoprénica Activada
# =============================================================================
ISOPENTENIL_PP = """
<g class="mol-ipp" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Doble enlace terminal CH2=C -->
  <text x="6" y="24" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a" stroke="none">H₂C</text>
  <line x1="32" y1="18" x2="52" y2="28" stroke-width="2.1"/>
  <line x1="34" y1="24" x2="54" y2="34" stroke-width="2.1"/>

  <!-- Carbono C3 con metilo ramificado hacia abajo -->
  <circle cx="53" cy="31" r="3" fill="#ea580c" stroke="none"/>
  <line x1="53" y1="31" x2="53" y2="50" />
  <text x="53" y="63" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">CH₃</text>

  <!-- Enlace hacia C2 metileno -->
  <line x1="53" y1="31" x2="80" y2="31" />
  <!-- Enlace hacia C1 con fosfatos -->
  <line x1="80" y1="31" x2="104" y2="18" />
  <text x="106" y="19" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" stroke="none">CH₂</text>

  <!-- Pirofosfato (O-PP) -->
  <line x1="130" y1="15" x2="148" y2="15" stroke="#ea580c" stroke-width="2.2"/>
  <rect x="150" y="4" width="46" height="22" rx="11" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
  <text x="173" y="19" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">O-PP</text>
</g>
"""

# =============================================================================
# 5. FARNESIL PIROFOSFATO - FPP (15C) - Punto de Ramificación
# =============================================================================
FARNESIL_PP = """
<g class="mol-fpp" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Cadena poliisoprénica en zigzag de 3 unidades (15C) -->
  <!-- Unidad 1 -->
  <line x1="10" y1="28" x2="26" y2="16" />
  <line x1="26" y1="16" x2="42" y2="28" />
  <line x1="42" y1="28" x2="58" y2="16" />
  <line x1="42" y1="28" x2="42" y2="44" />
  <text x="42" y="55" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₃</text>

  <!-- Unidad 2 -->
  <line x1="58" y1="16" x2="74" y2="28" />
  <line x1="74" y1="28" x2="90" y2="16" />
  <line x1="74" y1="28" x2="74" y2="44" />
  <text x="74" y="55" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₃</text>

  <!-- Unidad 3 con enlace a PPi -->
  <line x1="90" y1="16" x2="106" y2="28" />
  <line x1="106" y1="28" x2="122" y2="16" />
  <line x1="106" y1="28" x2="106" y2="44" />
  <text x="106" y="55" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₃</text>

  <!-- Pirofosfato O-PP -->
  <line x1="122" y1="16" x2="138" y2="16" stroke="#ea580c" stroke-width="2.2"/>
  <rect x="140" y="5" width="46" height="22" rx="11" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
  <text x="163" y="20" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">O-PP</text>
</g>
"""

# =============================================================================
# 6. ESCUALENO (30C) - Hidrocarburo Poliisoprénico Lineal
# =============================================================================
ESCUALENO = """
<g class="mol-escualeno" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Representación simétrica cabeza con cabeza (2 x 15C) -->
  <path d="M 10 24 L 25 14 L 40 24 L 55 14 L 70 24 L 85 14 L 100 24 L 115 14 L 130 24 L 145 14 L 160 24 L 175 14 L 190 24" />
  <!-- Metilos ramificados característicos -->
  <line x1="25" y1="14" x2="25" y2="4" />
  <line x1="55" y1="14" x2="55" y2="4" />
  <line x1="85" y1="14" x2="85" y2="4" />
  <line x1="115" y1="14" x2="115" y2="4" />
  <line x1="145" y1="14" x2="145" y2="4" />
  <line x1="175" y1="14" x2="175" y2="4" />
  <!-- Rótulo de simetría -->
  <text x="100" y="38" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#64748b" stroke="none" text-anchor="middle">Condensación cola-con-cola (30C)</text>
</g>
"""

# =============================================================================
# 7. LANOSTEROL (30C) - Primer Intermedio Tetracíclico Esteroideo
# =============================================================================
LANOSTEROL = """
<g class="mol-lanosterol" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Anillo A (con OH en C3 y dos metilos gemelos en C4) -->
  <polygon points="20,40 32,20 54,20 66,40 54,60 32,60" />
  <!-- OH en C3 -->
  <line x1="20" y1="40" x2="4" y2="40" stroke="#0284c7" stroke-width="2.2"/>
  <text x="2" y="36" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0284c7" stroke="none">HO</text>
  <!-- Metilos gem-dimetilo en C4 -->
  <line x1="32" y1="60" x2="24" y2="72" />
  <line x1="32" y1="60" x2="38" y2="72" />

  <!-- Anillo B -->
  <polygon points="66,40 78,20 100,20 112,40 100,60 66,60" />
  <!-- Metilo angular C10 -->
  <line x1="66" y1="40" x2="66" y2="24" />

  <!-- Anillo C (con doble enlace 8-9) -->
  <polygon points="112,40 124,20 146,20 158,40 146,60 112,60" />
  <!-- Metilo angular C13 y C14 -->
  <line x1="124" y1="20" x2="124" y2="6" />
  <line x1="112" y1="60" x2="112" y2="72" />

  <!-- Anillo D (Ciclopentano de 5 vértices) -->
  <polygon points="158,40 174,26 190,38 184,58 158,60" />

  <!-- Cola alifática en C17 -->
  <path d="M 190 38 L 206 28 L 220 38 L 234 28" />
  <line x1="234" y1="28" x2="244" y2="20" />
  <line x1="234" y1="28" x2="244" y2="36" />
</g>
"""

# =============================================================================
# 8. COLESTEROL (27C) - Molécula Final Esteroidea
# =============================================================================
COLESTEROL = """
<g class="mol-colesterol" stroke="#0f172a" stroke-width="2.3" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- ANILLO A (con grupo hidroxilo beta en C3) -->
  <polygon points="26,42 38,22 60,22 72,42 60,62 38,62" />
  <line x1="26" y1="42" x2="8" y2="42" stroke="#0284c7" stroke-width="2.3"/>
  <text x="6" y="37" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0284c7" stroke="none">HO</text>
  <text x="28" y="52" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#64748b" stroke="none">A</text>

  <!-- ANILLO B (con doble enlace Δ5-6) -->
  <polygon points="72,42 84,22 106,22 118,42 106,62 72,62" />
  <!-- Doble enlace Δ5-6 -->
  <line x1="75" y1="58" x2="103" y2="58" stroke-width="2.1"/>
  <!-- Metilo angular C19 en C10 -->
  <line x1="72" y1="42" x2="72" y2="26" />
  <circle cx="72" cy="26" r="2.5" fill="#0f172a" stroke="none"/>
  <text x="88" y="44" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#64748b" stroke="none">B</text>

  <!-- ANILLO C -->
  <polygon points="118,42 130,22 152,22 164,42 152,62 118,62" />
  <!-- Metilo angular C18 en C13 -->
  <line x1="152" y1="22" x2="152" y2="8" />
  <circle cx="152" cy="8" r="2.5" fill="#0f172a" stroke="none"/>
  <text x="134" y="44" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#64748b" stroke="none">C</text>

  <!-- ANILLO D (Pentágono) -->
  <polygon points="164,42 180,28 196,40 190,60 164,62" />
  <text x="175" y="48" font-family="'Inter', sans-serif" font-size="8.5" font-weight="900" fill="#64748b" stroke="none">D</text>

  <!-- CADENA LATERAL HIDROCARBONADA EN C17 (8 carbonos: C20-C27) -->
  <path d="M 196 40 L 210 30 L 224 40 L 238 30 L 252 40" stroke-width="2.3"/>
  <!-- Ramificación isopropilo terminal esquelética (C25 -> C26, C27) -->
  <line x1="252" y1="40" x2="266" y2="28" stroke-width="2.3"/>
  <line x1="252" y1="40" x2="266" y2="52" stroke-width="2.3"/>
</g>
"""
