#!/usr/bin/env python3
"""
CATÁLOGO DE ESTRUCTURAS QUÍMICAS (SVG) - COMPLEJO PIRUVATO DESHIDROGENASA (PDH)
================================================================================
Diseñadas bajo el Manual de Estilo Editorial Bioquímico del proyecto:
- Carbonos explícitos con tipografía clara (sin puntos ciegos).
- Trazos oscuros nítidos (#0f172a, 2.0 a 2.4 pt).
- Carboxilatos (COO⁻) y carbonilos (C=O) con oxígeno en rojo (#dc2626).
- Hidroxilos (-OH) en azul bioquímico (#0284c7).
- Grupos tiol (-SH) en verde esmeralda (#059669).
- Tioésteres (~S-CoA, ~S-Lipoil) con azufre en dorado/ámbar (#d97706) y Coenzima A en púrpura (#7c3aed).
"""

# PIRUVATO (3 Carbonos: C1 Carboxilato, C2 Carbonilo, C3 Metilo)
PIRUVATO = """
<g class="mol-piruvato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2: Carbono Carbonilo explícito -->
  <text x="40" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <line x1="48" y1="45" x2="68" y2="45" stroke="#dc2626" stroke-width="2"/>
  <line x1="48" y1="49" x2="68" y2="49" stroke="#dc2626" stroke-width="2"/>
  <text x="76" y="52" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" stroke="none">O</text>

  <!-- C2 - C3 Enlace -->
  <line x1="40" y1="57" x2="40" y2="74" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C3: Grupo Metilo explícito -->
  <text x="40" y="88" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">CH₃</text>
</g>
"""

# HIDROXIETIL-TPP (Intermediario en E1: CH3 - CH(OH) - TPP)
HIDROXIETIL_TPP = """
<g class="mol-hidroxietil-tpp" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="24" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">H₃C</text>
  <line x1="38" y1="40" x2="54" y2="40" stroke="#0f172a" stroke-width="2.2"/>

  <!-- Carbono Cα hidroxilado explícito -->
  <text x="62" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <line x1="62" y1="32" x2="62" y2="20" stroke="#0f172a" stroke-width="2"/>
  <text x="62" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">H</text>
  <line x1="62" y1="48" x2="62" y2="60" stroke="#0284c7" stroke-width="2"/>
  <text x="62" y="73" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0284c7" text-anchor="middle" stroke="none">OH</text>

  <!-- Enlace al cofactor TPP -->
  <line x1="70" y1="40" x2="88" y2="40" stroke="#ea580c" stroke-width="2.4"/>
  <polygon points="90,30 110,24 124,38 114,54 94,48" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
  <text x="100" y="38" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#d97706" stroke="none">S</text>
  <text x="114" y="44" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none">N⁺</text>
  <rect x="130" y="28" width="56" height="24" rx="12" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
  <text x="158" y="44" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#c2410c" text-anchor="middle" stroke="none">TPP-E1</text>
</g>
"""

# ACETIL-LIPOAMIDA (Intermediario en E2: H3C - C(=O) ~ S - Lipoil-Lys)
ACETIL_LIPOAMIDA = """
<g class="mol-acetil-lipoamida" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="20" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">H₃C</text>
  <line x1="34" y1="40" x2="52" y2="40" stroke="#0f172a" stroke-width="2.2"/>

  <!-- Carbono Carbonilo explícito -->
  <text x="60" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <line x1="57" y1="32" x2="57" y2="18" stroke="#dc2626" stroke-width="2"/>
  <line x1="63" y1="32" x2="63" y2="18" stroke="#dc2626" stroke-width="2"/>
  <text x="60" y="14" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle" stroke="none">O</text>

  <!-- Enlace tioéster hacia S -->
  <line x1="68" y1="40" x2="86" y2="40" stroke="#d97706" stroke-width="2.4"/>
  <text x="94" y="44" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#d97706" text-anchor="middle" stroke="none">S</text>

  <!-- Brazo lipoamida -->
  <path d="M 102 40 L 122 40 L 132 54 L 150 54" stroke="#d97706" stroke-width="2"/>
  <line x1="122" y1="40" x2="122" y2="26" stroke="#059669" stroke-width="1.8"/>
  <text x="122" y="20" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#059669" text-anchor="middle" stroke="none">HS</text>

  <rect x="154" y="42" width="58" height="24" rx="12" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>
  <text x="183" y="58" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#b45309" text-anchor="middle" stroke="none">Lys-E2</text>
</g>
"""

# DIHIDROLIPOAMIDA (Forma reducida con los dos grupos -SH desplazados a la izquierda)
DIHIDROLIPOAMIDA = """
<g class="mol-dihidrolipoamida" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="-25" y="34" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#059669" stroke="none">HS</text>
  <line x1="-5" y1="30" x2="18" y2="30" stroke="#059669" stroke-width="2"/>
  <text x="18" y="64" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#059669" stroke="none">HS</text>
  <line x1="28" y1="52" x2="28" y2="36" stroke="#059669" stroke-width="2"/>
  <line x1="18" y1="30" x2="48" y2="30" stroke="#059669" stroke-width="2"/>
  <line x1="48" y1="30" x2="72" y2="30" stroke="#059669" stroke-width="2"/>
  <rect x="76" y="18" width="60" height="24" rx="12" fill="#dcfce7" stroke="#16a34a" stroke-width="1.8"/>
  <text x="106" y="34" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#15803d" text-anchor="middle" stroke="none">Lys-E2</text>
</g>
"""

# LIPOAMIDA OXIDADA
LIPOAMIDA_OXIDADA = """
<g class="mol-lipoamida-oxidada" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="35,30 52,18 68,30 62,46 40,46" fill="#fef3c7" stroke="#d97706" stroke-width="2.2"/>
  <text x="44" y="34" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#d97706" stroke="none">S</text>
  <text x="58" y="34" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#d97706" stroke="none">S</text>
  <line x1="68" y1="30" x2="105" y2="30" stroke="#047857" stroke-width="2"/>
  <rect x="108" y="18" width="86" height="24" rx="12" fill="#fef3c7" stroke="#d97706" stroke-width="1.8"/>
  <text x="151" y="34" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#b45309" text-anchor="middle" stroke="none">E2 (S-S activo)</text>
</g>
"""

# ACETIL-COENZIMA A
ACETIL_COA = """
<g class="mol-acetil-coa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="20" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">H₃C</text>
  <line x1="34" y1="40" x2="52" y2="40" stroke="#0f172a" stroke-width="2.2"/>

  <!-- Carbono carbonílico C=O explícito -->
  <text x="60" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <line x1="57" y1="32" x2="57" y2="18" stroke="#dc2626" stroke-width="2"/>
  <line x1="63" y1="32" x2="63" y2="18" stroke="#dc2626" stroke-width="2"/>
  <text x="60" y="14" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle" stroke="none">O</text>

  <!-- Enlace tioéster hacia S -->
  <line x1="68" y1="40" x2="86" y2="40" stroke="#d97706" stroke-width="2.4"/>
  <text x="94" y="44" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#d97706" text-anchor="middle" stroke="none">S</text>

  <!-- Coenzima A -->
  <line x1="102" y1="40" x2="114" y2="40" stroke="#7c3aed" stroke-width="2"/>
  <rect x="116" y="28" width="48" height="24" rx="12" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="140" y="44" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" fill="#6b21a8" text-anchor="middle" stroke="none">CoA</text>
</g>
"""
