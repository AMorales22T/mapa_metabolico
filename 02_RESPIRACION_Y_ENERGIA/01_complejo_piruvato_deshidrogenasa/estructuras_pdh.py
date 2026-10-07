#!/usr/bin/env python3
"""
CATÁLOGO COMPLETO DE ESTRUCTURAS QUÍMICAS (SVG) - COMPLEJO PIRUVATO DESHIDROGENASA (PDH)
========================================================================================
Diseñadas bajo el Manual de Estilo Editorial Bioquímico (idéntico a Glucólisis y Krebs):
- Trazos oscuros nítidos (#0f172a, grosor 2.0 a 2.4 pt).
- Carboxilatos (COO⁻) y carbonilos (C=O) con oxígeno en rojo (#dc2626).
- Grupos hidroxilo (-OH) en azul bioquímico (#0284c7).
- Grupos tiol (-SH) en verde esmeralda (#059669).
- Tioésteres (~S-CoA, ~S-Lipoil) con azufre en dorado/ámbar (#d97706) y Coenzima A en púrpura (#7c3aed).
- Sin cajas delimitadoras: moléculas limpias suspendidas en el espacio orgánico.
"""

# PIRUVATO (3 Carbonos - Sustrato que ingresa desde Glucólisis vía MPC)
# H3C - C(=O) - COO⁻
PIRUVATO = """
<g class="mol-piruvato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />

  <!-- C2: C=O (Grupo carbonilo α) -->
  <circle cx="40" cy="48" r="3" fill="#0f172a"/>
  <line x1="47" y1="44" x2="66" y2="44" stroke="#dc2626" stroke-width="2"/>
  <line x1="47" y1="48" x2="66" y2="48" stroke="#dc2626" stroke-width="2"/>
  <text x="74" y="50" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" stroke="none">O</text>

  <!-- Enlace C2 - C3 -->
  <line x1="40" y1="54" x2="40" y2="72" />

  <!-- C3: Grupo metilo CH3 -->
  <text x="40" y="86" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">CH₃</text>
</g>
"""

# HIDROXIETIL-TPP (Intermediario en E1 unido al cofactor TPP)
# CH3 - CH(OH) - [TPP-E1]
HIDROXIETIL_TPP = """
<g class="mol-hidroxietil-tpp" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo metilo H3C -->
  <text x="22" y="38" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">H₃C</text>
  <line x1="36" y1="34" x2="54" y2="34" />

  <!-- Carbono Cα hidroxilado -->
  <circle cx="58" cy="34" r="3" fill="#0f172a"/>
  <!-- H arriba -->
  <line x1="58" y1="30" x2="58" y2="16" />
  <text x="58" y="12" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">H</text>
  <!-- OH abajo -->
  <line x1="58" y1="38" x2="58" y2="52" stroke="#0284c7" stroke-width="2"/>
  <text x="58" y="66" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0284c7" text-anchor="middle" stroke="none">OH</text>

  <!-- Enlace covalente al C2 del anillo tiazólico de TPP -->
  <line x1="62" y1="34" x2="84" y2="34" stroke="#ea580c" stroke-width="2.4"/>
  <!-- Anillo tiazol esquemático -->
  <path d="M 86 24 L 108 18 L 122 34 L 110 50 L 88 44 Z" fill="#fff7ed" stroke="#ea580c" stroke-width="2"/>
  <text x="96" y="32" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#d97706" stroke="none">S</text>
  <text x="110" y="38" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none">N⁺</text>
  <text x="105" y="66" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#c2410c" text-anchor="middle" stroke="none">TPP-E1</text>
</g>
"""

# ACETIL-LIPOAMIDA (Intermediario en E2 con el grupo acetilo unido al tioéster del brazo lipoil-lisina)
# H3C - C(=O) ~ S - Lipoil-Lys
ACETIL_LIPOAMIDA = """
<g class="mol-acetil-lipoamida" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo metilo H3C -->
  <text x="18" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">H₃C</text>
  <line x1="32" y1="40" x2="50" y2="40" />

  <!-- Carbonilo C=O -->
  <circle cx="54" cy="40" r="3" fill="#0f172a"/>
  <line x1="51" y1="36" x2="51" y2="18" stroke="#dc2626" stroke-width="2"/>
  <line x1="56" y1="36" x2="56" y2="18" stroke="#dc2626" stroke-width="2"/>
  <text x="54" y="12" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle" stroke="none">O</text>

  <!-- Enlace tioéster hacia C8 del lipoato -->
  <line x1="58" y1="40" x2="76" y2="40" stroke="#d97706" stroke-width="2.4"/>
  <text x="84" y="44" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#d97706" text-anchor="middle" stroke="none">S</text>

  <!-- Cadena hidrocarbonada del lipoato con C6-SH reducido -->
  <path d="M 92 40 L 112 40 L 122 55 L 140 55" stroke="#d97706" stroke-width="2"/>
  <!-- Grupo tiol libre en C6 -->
  <line x1="112" y1="40" x2="112" y2="25" stroke="#059669" stroke-width="1.8"/>
  <text x="112" y="18" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#059669" text-anchor="middle" stroke="none">HS</text>

  <!-- Brazo unido a Lisina -->
  <line x1="140" y1="55" x2="158" y2="55" stroke="#047857" stroke-width="2"/>
  <text x="162" y="59" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#047857" stroke="none">Lys-E2</text>
</g>
"""

# DIHIDROLIPOAMIDA (Forma reducida de la lipoamida tras transferir el acetilo a CoA-SH)
DIHIDROLIPOAMIDA = """
<g class="mol-dihidrolipoamida" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="25" y="34" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#059669" stroke="none">HS</text>
  <line x1="45" y1="30" x2="68" y2="30" stroke="#059669" stroke-width="2"/>
  <text x="78" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#059669" stroke="none">HS</text>
  <path d="M 68 30 L 78 46 L 98 46 L 122 46" stroke="#059669" stroke-width="2"/>
  <line x1="122" y1="46" x2="142" y2="46" stroke="#047857" stroke-width="2"/>
  <text x="146" y="50" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#047857" stroke="none">Lys-E2</text>
</g>
"""

# LIPOAMIDA OXIDADA (Forma regenerada con puente disulfuro cíclico S-S activo)
LIPOAMIDA_OXIDADA = """
<g class="mol-lipoamida-oxidada" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Anillo ditiolano de 5 miembros -->
  <path d="M 35 30 L 52 18 L 68 30 L 62 46 L 40 46 Z" fill="#fef3c7" stroke="#d97706" stroke-width="2.2"/>
  <text x="44" y="34" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#d97706" stroke="none">S</text>
  <text x="58" y="34" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#d97706" stroke="none">S</text>
  <line x1="68" y1="30" x2="105" y2="30" stroke="#047857" stroke-width="2"/>
  <text x="109" y="34" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#047857" stroke="none">Lys-E2 (S-S activo)</text>
</g>
"""

# ACETIL-COENZIMA A (2 Carbonos activados en tioéster - Producto final)
# H3C - C(=O) ~ S-CoA
ACETIL_COA = """
<g class="mol-acetil-coa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- CH3 Metilo izquierdo -->
  <text x="20" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">H₃C</text>
  <line x1="34" y1="40" x2="52" y2="40" />

  <!-- Carbono carbonílico C=O -->
  <circle cx="56" cy="40" r="3" fill="#0f172a"/>
  <!-- Doble enlace =O arriba -->
  <line x1="53" y1="36" x2="53" y2="18" stroke="#dc2626" stroke-width="2"/>
  <line x1="58" y1="36" x2="58" y2="18" stroke="#dc2626" stroke-width="2"/>
  <text x="56" y="12" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle" stroke="none">O</text>

  <!-- Enlace tioéster hacia azufre S -->
  <line x1="60" y1="40" x2="78" y2="40" stroke="#d97706" stroke-width="2.4"/>
  <text x="86" y="44" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#d97706" text-anchor="middle" stroke="none">S</text>

  <!-- Enlace hacia Coenzima A -->
  <line x1="94" y1="40" x2="108" y2="40" stroke="#7c3aed" stroke-width="2"/>
  <text x="126" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#7c3aed" stroke="none">CoA</text>
</g>
"""
