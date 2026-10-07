#!/usr/bin/env python3
"""
ESTRUCTURAS QUÍMICAS Y COFACTORES SVG - COMPLEJO PIRUVATO DESHIDROGENASA (PDH)
==============================================================================
Diseñadas bajo el Manual de Estilo Editorial Bioquímico:
- Trazos oscuros (#0f172a, 2.0 - 2.4 pt).
- Carboxilatos y carbonilos con oxígeno en rojo (#dc2626).
- Hidroxilos en azul (#0284c7).
- Azufres y puentes disulfuro / tioésteres en ámbar/dorado (#d97706).
- Grupos fosfato en ámbar (#d97706 / #b45309).
- Coenzima A en púrpura (#7c3aed).
"""

# PIRUVATO (Sustrato inicial, 3C)
PIRUVATO = """
<g class="mol-piruvato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />
  <circle cx="40" cy="48" r="3" fill="#0f172a"/>
  <line x1="47" y1="44" x2="66" y2="44" stroke="#dc2626" stroke-width="2"/>
  <line x1="47" y1="48" x2="66" y2="48" stroke="#dc2626" stroke-width="2"/>
  <text x="74" y="50" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <line x1="40" y1="54" x2="40" y2="72" />
  <text x="40" y="86" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">CH₃</text>
</g>
"""

# HIDROXIETIL-TPP (Intermediario unido covalentemente al anillo tiazólico de E1)
HIDROXIETIL_TPP = """
<g class="mol-hidroxietil-tpp" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo hidroxietilo -->
  <text x="25" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">H₃C</text>
  <line x1="38" y1="20" x2="55" y2="20" />
  <circle cx="58" cy="20" r="3" fill="#0f172a"/>
  <line x1="58" y1="24" x2="58" y2="38" />
  <text x="58" y="50" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0284c7" text-anchor="middle" stroke="none">OH</text>
  <!-- Enlace hacia C2 activo del TPP -->
  <line x1="62" y1="20" x2="82" y2="20" stroke="#ea580c" stroke-width="2.4"/>
  <!-- Anillo tiazol esquemático de TPP -->
  <path d="M 85 10 L 110 5 L 125 20 L 115 35 L 90 30 Z" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
  <text x="96" y="22" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#d97706" stroke="none">S</text>
  <text x="112" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none">N⁺</text>
  <text x="105" y="48" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#c2410c" text-anchor="middle" stroke="none">TPP-E1</text>
</g>
"""

# ACETIL-LIPOAMIDA (Intermediario en E2: brazo oscilante de lipoamida acetilado)
ACETIL_LIPOAMIDA = """
<g class="mol-acetil-lipoamida" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo acetilo -->
  <text x="20" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">H₃C</text>
  <line x1="34" y1="20" x2="52" y2="20" />
  <circle cx="55" cy="20" r="3" fill="#0f172a"/>
  <line x1="53" y1="16" x2="53" y2="2" stroke="#dc2626" stroke-width="2"/>
  <line x1="57" y1="16" x2="57" y2="2" stroke="#dc2626" stroke-width="2"/>
  <text x="55" y="-1" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#dc2626" text-anchor="middle" stroke="none">O</text>
  <!-- Enlace tioéster al S del C8 del lipoato -->
  <line x1="59" y1="20" x2="76" y2="20" stroke="#d97706" stroke-width="2.4"/>
  <text x="84" y="24" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#d97706" text-anchor="middle" stroke="none">S</text>
  <!-- Brazo oscilante lipoilo -->
  <path d="M 92 20 L 115 20 L 125 35 L 140 35" stroke="#d97706" stroke-width="2"/>
  <text x="118" y="48" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#059669" text-anchor="middle" stroke="none">HS</text>
  <line x1="140" y1="35" x2="155" y2="35" stroke="#047857" stroke-width="2"/>
  <text x="190" y="39" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#047857" stroke="none">Brazo-Lys (E2)</text>
</g>
"""

# DIHIDROLIPOAMIDA (Forma reducida de la lipoamida tras transferir acetilo a CoA)
DIHIDROLIPOAMIDA = """
<g class="mol-dihidrolipoamida" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="25" y="24" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#059669" stroke="none">HS</text>
  <line x1="45" y1="20" x2="65" y2="20" stroke="#059669" stroke-width="2"/>
  <text x="75" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#059669" stroke="none">HS</text>
  <path d="M 65 20 L 75 34 L 95 34 L 115 34" stroke="#059669" stroke-width="2"/>
  <text x="150" y="38" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#047857" text-anchor="middle" stroke="none">Lipoamida reducida (2 -SH)</text>
</g>
"""

# LIPOAMIDA OXIDADA (Forma activa con puente disulfuro cíclico lista para otro ciclo)
LIPOAMIDA_OXIDADA = """
<g class="mol-lipoamida-oxidada" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Anillo ditiolano de 5 miembros -->
  <path d="M 40 20 L 55 10 L 70 20 L 65 35 L 45 35 Z" fill="#fef3c7" stroke="#d97706" stroke-width="2.2"/>
  <text x="48" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#d97706" stroke="none">S</text>
  <text x="62" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#d97706" stroke="none">S</text>
  <line x1="70" y1="20" x2="105" y2="20" stroke="#047857" stroke-width="2"/>
  <text x="145" y="24" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="800" fill="#047857" stroke="none">Puente S-S activo (E2)</text>
</g>
"""

# ACETIL-COENZIMA A (Producto clave de la descarboxilación oxidativa)
ACETIL_COA = """
<g class="mol-acetil-coa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="20" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">H₃C</text>
  <line x1="34" y1="40" x2="52" y2="40" />
  <circle cx="56" cy="40" r="3" fill="#0f172a"/>
  <line x1="53" y1="36" x2="53" y2="18" stroke="#dc2626" stroke-width="2"/>
  <line x1="58" y1="36" x2="58" y2="18" stroke="#dc2626" stroke-width="2"/>
  <text x="56" y="12" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle" stroke="none">O</text>
  <line x1="60" y1="40" x2="78" y2="40" stroke="#d97706" stroke-width="2.4"/>
  <text x="86" y="44" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#d97706" text-anchor="middle" stroke="none">S</text>
  <line x1="94" y1="40" x2="108" y2="40" stroke="#7c3aed" stroke-width="2"/>
  <text x="126" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#7c3aed" stroke="none">CoA</text>
</g>
"""

# COENZIMA A LIBRE (CoA-SH)
COA_SH = """
<g class="mol-coa-sh" stroke="#0f172a" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="15" y="20" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#059669" stroke="none">HS</text>
  <line x1="35" y1="16" x2="50" y2="16" stroke="#7c3aed" stroke-width="2"/>
  <text x="56" y="20" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#7c3aed" stroke="none">CoA</text>
</g>
"""
