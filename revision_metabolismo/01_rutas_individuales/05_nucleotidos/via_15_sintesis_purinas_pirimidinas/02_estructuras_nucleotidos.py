# =============================================================================
# MÓDULO DE REVISIÓN: Estructuras de Purinas y Pirimidinas
# =============================================================================
# Archivo original : 05_NUCLEOTIDOS_Y_OTRAS/via_15_sintesis_purinas_y_pirimidinas/estructuras_nucleotidos.py (líneas 1 a 439 de 439)
# Descripción      : PRPP, IMP, AMP, GMP, carbamoil-aspartato, orotato, UMP, UTP, CTP y dTMP.
# =============================================================================

#!/usr/bin/env python3
"""
ESTRUCTURAS QUÍMICAS VECTORIALES SVG - SÍNTESIS DE PURINAS Y PIRIMIDINAS
========================================================================
Diseñadas bajo el Manual de Estilo Editorial Científico:
- Trazos grafito nítidos (#0f172a, stroke-width: 2.2px)
- Oxígenos (C=O, anillos) en rojo carmesí (#dc2626)
- Nitrógenos de anillos purina/pirimidina y grupos amino en azul cobalto (#2563eb)
- Grupos fosfato en cápsulas melocotón/naranja (#ffedd5, borde #ea580c y Ⓟ)
- Anillos de furanosa y bases nitrogenadas perfectamente orientados
- Mapas vectoriales didácticos del origen de cada átomo del anillo
- Texto siempre con stroke="none" para renderizado tipográfico perfecto.
"""

# =============================================================================
# 1. PRECURSORES CLAVE COMUNES (RIBOSA-5-P Y PRPP)
# =============================================================================

RIBOSA_5_FOSFATO = """
<g class="mol-ribosa-5p" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Anillo furanosa de 5 lados -->
  <polygon points="35,18 68,38 52,68 18,68 2,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.4"/>

  <!-- Oxígeno superior del anillo -->
  <circle cx="35" cy="18" r="7" fill="#ffffff" stroke="none"/>
  <text x="35" y="23" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C1 (derecha): OH anomérico -->
  <line x1="68" y1="38" x2="84" y2="38" stroke="#0f172a" stroke-width="2"/>
  <text x="88" y="42" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none">OH</text>

  <!-- C5 (izquierda): Grupo Fosfato -->
  <line x1="2" y1="38" x2="-12" y2="20" stroke="#0f172a" stroke-width="2"/>
  <circle cx="-20" cy="8" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="-20" y="12" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>

  <!-- C2 y C3: -OH abajo -->
  <line x1="52" y1="68" x2="52" y2="80" stroke="#0f172a" stroke-width="2"/>
  <text x="52" y="92" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">OH</text>
  <line x1="18" y1="68" x2="18" y2="80" stroke="#0f172a" stroke-width="2"/>
  <text x="18" y="92" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">HO</text>
</g>
"""

PRPP = """
<g class="mol-prpp" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Anillo furanosa central -->
  <polygon points="35,22 68,42 52,72 18,72 2,42" fill="#ffffff" stroke="#0f172a" stroke-width="2.4"/>

  <!-- Oxígeno del anillo -->
  <circle cx="35" cy="22" r="7" fill="#ffffff" stroke="none"/>
  <text x="35" y="27" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- C5 (izquierda): Fosfato monocatenario 5-P -->
  <line x1="2" y1="42" x2="-12" y2="24" stroke="#0f172a" stroke-width="2"/>
  <circle cx="-20" cy="12" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="-20" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>

  <!-- C1 (derecha): Grupo Pirofosfato (PPi en alfa) activador -->
  <line x1="68" y1="42" x2="84" y2="42" stroke="#ea580c" stroke-width="2.2"/>
  <!-- Pirofosfato cápsula doble -->
  <rect x="85" y="28" width="56" height="28" rx="14" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="113" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#b91c1c" stroke="none" text-anchor="middle">Ⓟ~Ⓟ</text>
  <text x="113" y="22" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="800" fill="#dc2626" stroke="none" text-anchor="middle">1-Pirofosfato</text>

  <!-- C2 y C3: -OH abajo -->
  <line x1="52" y1="72" x2="52" y2="84" stroke="#0f172a" stroke-width="2"/>
  <text x="52" y="96" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">OH</text>
  <line x1="18" y1="72" x2="18" y2="84" stroke="#0f172a" stroke-width="2"/>
  <text x="18" y="96" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">HO</text>
</g>
"""

FOSFORRIBOSILAMINA_5 = """
<g class="mol-5-pra" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Anillo furanosa central -->
  <polygon points="35,16 68,36 52,66 18,66 2,36" fill="#ffffff" stroke="#0f172a" stroke-width="2.4"/>
  <circle cx="35" cy="16" r="7" fill="#ffffff" stroke="none"/>
  <text x="35" y="21" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <!-- C5: Fosfato 5-P -->
  <line x1="2" y1="36" x2="-12" y2="20" stroke="#0f172a" stroke-width="2"/>
  <circle cx="-20" cy="10" r="12" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="-20" y="14" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
  <!-- C1: Grupo β-Amino (-NH2, N9 del futuro anillo de purina) -->
  <line x1="68" y1="36" x2="84" y2="26" stroke="#2563eb" stroke-width="2.2"/>
  <rect x="84" y="13" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.6"/>
  <text x="103" y="28" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#1d4ed8" stroke="none" text-anchor="middle">β-NH₂</text>
  <!-- C2 y C3: -OH abajo -->
  <line x1="52" y1="66" x2="52" y2="76" stroke="#0f172a" stroke-width="1.8"/>
  <text x="52" y="87" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">OH</text>
  <line x1="18" y1="66" x2="18" y2="76" stroke="#0f172a" stroke-width="1.8"/>
  <text x="18" y="87" font-family="'Inter', sans-serif" font-size="9.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">HO</text>
</g>
"""

DIHIDROOROTATO = """
<g class="mol-dihidroorotato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Anillo pirimidina saturado C5-C6 (sin doble enlace) -->
  <polygon points="36,16 64,30 64,58 36,72 10,58 10,30" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="10" y1="58" x2="-4" y2="66" stroke="#dc2626" stroke-width="2.2"/>
  <text x="-8" y="72" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>
  <text x="10" y="34" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
  <text x="36" y="75" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">HN</text>
  <line x1="64" y1="58" x2="78" y2="66" stroke="#dc2626" stroke-width="2.2"/>
  <text x="84" y="72" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <text x="68" y="34" font-family="'JetBrains Mono', monospace" font-size="8" font-weight="800" fill="#64748b" stroke="none">CH₂</text>
  <line x1="36" y1="16" x2="36" y2="2" stroke="#0f172a" stroke-width="2.2"/>
  <text x="36" y="-3" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""


# =============================================================================
# 2. ESQUEMAS DEL ORIGEN DE LOS ÁTOMOS DEL ANILLO (CLAVE DIDÁCTICA EDITORIAL)
# =============================================================================

ORIGEN_ATOMOS_PURINA = """
<g class="esquema-origen-purina" stroke-linecap="round" stroke-linejoin="round">
  <!-- Fondo y borde editorial suave -->
  <rect x="0" y="0" width="220" height="135" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="110" y="16" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#334155" stroke="none" text-anchor="middle">ORIGEN DE LOS ÁTOMOS (PURINA)</text>

  <!-- Anillo bicíclico esquemático centrado -->
  <!-- Pirimidina izquierda (6C/N): N1, C2, N3, C4, C5, C6 -->
  <!-- Imidazol derecho (5C/N): C4, C5, N7, C8, N9 -->
  <g transform="translate(42, 28)">
    <!-- Hexágono pirimidínico -->
    <polygon points="35,16 60,30 60,60 35,74 10,60 10,30" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
    <!-- Pentágono imidazol fusionado en (60,30)-(60,60) -->
    <polygon points="60,30 84,22 98,45 84,68 60,60" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>

    <!-- Átomos clave con colores de sus donadores -->
    <!-- N1: Aspartato (Verde esmeralda) -->
    <circle cx="10" cy="30" r="7" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
    <text x="10" y="34" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#059669" stroke="none" text-anchor="middle">N1</text>

    <!-- C2: N10-formil-THF (Morado) -->
    <circle cx="10" cy="60" r="7" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
    <text x="10" y="64" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#7c3aed" stroke="none" text-anchor="middle">C2</text>

    <!-- N3: Glutamina (Azul cobalto) -->
    <circle cx="35" cy="74" r="7" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="35" y="78" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">N3</text>

    <!-- C4, C5, N7: Glicina (Ámbar) -->
    <circle cx="60" cy="60" r="7" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="60" y="64" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#d97706" stroke="none" text-anchor="middle">C4</text>
    <circle cx="60" cy="30" r="7" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="60" y="34" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#d97706" stroke="none" text-anchor="middle">C5</text>
    <circle cx="84" cy="22" r="7" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
    <text x="84" y="26" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#d97706" stroke="none" text-anchor="middle">N7</text>

    <!-- C6: CO2 respiratorio (Rojo carmesí) -->
    <circle cx="35" cy="16" r="7" fill="#fef2f2" stroke="#dc2626" stroke-width="1.5"/>
    <text x="35" y="20" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">C6</text>

    <!-- C8: N10-formil-THF (Morado) -->
    <circle cx="98" cy="45" r="7" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
    <text x="98" y="49" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#7c3aed" stroke="none" text-anchor="middle">C8</text>

    <!-- N9: Glutamina (Azul cobalto) -->
    <circle cx="84" cy="68" r="7" fill="#eff6ff" stroke="#2563eb" stroke-width="1.5"/>
    <text x="84" y="72" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">N9</text>
  </g>

  <!-- Leyenda de donadores inferior -->
  <g transform="translate(10, 114)" font-family="'Inter', sans-serif" font-size="8" font-weight="800">
    <circle cx="4" cy="4" r="3" fill="#d97706"/>
    <text x="10" y="7" fill="#475569" stroke="none">Gly (C4,C5,N7)</text>
    <circle cx="75" cy="4" r="3" fill="#2563eb"/>
    <text x="81" y="7" fill="#475569" stroke="none">Gln (N3,N9)</text>
    <circle cx="137" cy="4" r="3" fill="#059669"/>
    <text x="143" y="7" fill="#475569" stroke="none">Asp (N1)</text>
    <circle cx="185" cy="4" r="3" fill="#7c3aed"/>
    <text x="191" y="7" fill="#475569" stroke="none">THF</text>
  </g>
</g>
"""

ORIGEN_ATOMOS_PIRIMIDINA = """
<g class="esquema-origen-pirimidina" stroke-linecap="round" stroke-linejoin="round">
  <!-- Fondo y borde editorial suave -->
  <rect x="0" y="0" width="220" height="135" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="1.5"/>
  <text x="110" y="16" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#334155" stroke="none" text-anchor="middle">ORIGEN DE LOS ÁTOMOS (PIRIMIDINA)</text>

  <!-- Anillo simple de pirimidina (6 miembros) -->
  <g transform="translate(68, 28)">
    <polygon points="40,16 68,32 68,64 40,80 12,64 12,32" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>

    <!-- N1: Aspartato (Verde esmeralda) -->
    <circle cx="12" cy="32" r="7.5" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
    <text x="12" y="36" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#059669" stroke="none" text-anchor="middle">N1</text>

    <!-- C2: Carbamoil-P (Naranja) -->
    <circle cx="12" cy="64" r="7.5" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
    <text x="12" y="68" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">C2</text>

    <!-- N3: Carbamoil-P (Naranja) -->
    <circle cx="40" cy="80" r="7.5" fill="#fff7ed" stroke="#ea580c" stroke-width="1.5"/>
    <text x="40" y="84" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#ea580c" stroke="none" text-anchor="middle">N3</text>

    <!-- C4, C5, C6: Aspartato (Verde esmeralda) -->
    <circle cx="68" cy="64" r="7.5" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
    <text x="68" y="68" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#059669" stroke="none" text-anchor="middle">C4</text>
    <circle cx="68" cy="32" r="7.5" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
    <text x="68" y="36" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#059669" stroke="none" text-anchor="middle">C5</text>
    <circle cx="40" cy="16" r="7.5" fill="#ecfdf5" stroke="#059669" stroke-width="1.5"/>
    <text x="40" y="20" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#059669" stroke="none" text-anchor="middle">C6</text>
  </g>

  <!-- Leyenda de donadores inferior -->
  <g transform="translate(20, 114)" font-family="'Inter', sans-serif" font-size="8" font-weight="800">
    <circle cx="4" cy="4" r="3" fill="#ea580c"/>
    <text x="12" y="7" fill="#475569" stroke="none">Carbamoil-P (C2, N3)</text>
    <circle cx="108" cy="4" r="3" fill="#059669"/>
    <text x="116" y="7" fill="#475569" stroke="none">L-Aspartato (N1, C4, C5, C6)</text>
  </g>
</g>
"""

# =============================================================================
# 3. INTERMEDIARIOS Y PRODUCTOS PURÍNICOS (IMP, AMP, GMP, BASES LIBRES)
# =============================================================================

IMP = """
<g class="mol-imp" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Ribosa-5-P (parte inferior) -->
  <polygon points="35,62 65,78 52,104 18,104 5,78" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="35" cy="62" r="6" fill="#ffffff" stroke="none"/>
  <text x="35" y="66" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <!-- 5-Fosfato -->
  <line x1="5" y1="78" x2="-8" y2="64" stroke="#0f172a" stroke-width="2"/>
  <circle cx="-16" cy="54" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="-16" y="58" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
  <!-- OH en C2/C3 -->
  <line x1="52" y1="104" x2="52" y2="114" stroke="#0f172a" stroke-width="1.8"/>
  <line x1="18" y1="104" x2="18" y2="114" stroke="#0f172a" stroke-width="1.8"/>

  <!-- Enlace beta N-glucosídico C1' -> N9 -->
  <line x1="65" y1="78" x2="65" y2="48" stroke="#2563eb" stroke-width="2.2"/>

  <!-- Base Nitrogenada: Hipoxantina (Arriba) -->
  <!-- Imidazol: N9 en (65,48), C8 en (80,36), N7 en (72,16), C5 en (50,16), C4 en (48,38) -->
  <polygon points="48,38 50,16 72,16 82,32 65,48" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <text x="65" y="52" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">N</text>
  <text x="74" y="19" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">N</text>

  <!-- Pirimidina fusionada a la izquierda de (48,38)-(50,16): C6 en (32,4), N1 en (14,14), C2 en (14,34), N3 en (30,44) -->
  <polygon points="50,16 32,4 14,14 14,34 30,44 48,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C6=O (Carbonilo en C6) -->
  <line x1="32" y1="4" x2="32" y2="-10" stroke="#dc2626" stroke-width="2.2"/>
  <text x="32" y="-13" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <text x="14" y="18" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
</g>
"""

AMP = """
<g class="mol-amp" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Ribosa-5-P -->
  <polygon points="35,62 65,78 52,104 18,104 5,78" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="35" cy="62" r="6" fill="#ffffff" stroke="none"/>
  <text x="35" y="66" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <line x1="5" y1="78" x2="-8" y2="64" stroke="#0f172a" stroke-width="2"/>
  <circle cx="-16" cy="54" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="-16" y="58" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
  <line x1="52" y1="104" x2="52" y2="114" stroke="#0f172a" stroke-width="1.8"/>
  <line x1="18" y1="104" x2="18" y2="114" stroke="#0f172a" stroke-width="1.8"/>

  <!-- Enlace beta C1' -> N9 -->
  <line x1="65" y1="78" x2="65" y2="48" stroke="#2563eb" stroke-width="2.2"/>

  <!-- Base Nitrogenada: Adenina -->
  <polygon points="48,38 50,16 72,16 82,32 65,48" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <polygon points="50,16 32,4 14,14 14,34 30,44 48,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- Grupo amino en C6: -NH2 -->
  <line x1="32" y1="4" x2="32" y2="-10" stroke="#2563eb" stroke-width="2"/>
  <text x="32" y="-13" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH₂</text>
  <text x="14" y="27" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">N</text>
</g>
"""

GMP = """
<g class="mol-gmp" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Ribosa-5-P -->
  <polygon points="35,62 65,78 52,104 18,104 5,78" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="35" cy="62" r="6" fill="#ffffff" stroke="none"/>
  <text x="35" y="66" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <line x1="5" y1="78" x2="-8" y2="64" stroke="#0f172a" stroke-width="2"/>
  <circle cx="-16" cy="54" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="-16" y="58" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
  <line x1="52" y1="104" x2="52" y2="114" stroke="#0f172a" stroke-width="1.8"/>
  <line x1="18" y1="104" x2="18" y2="114" stroke="#0f172a" stroke-width="1.8"/>

  <!-- Enlace beta C1' -> N9 -->
  <line x1="65" y1="78" x2="65" y2="48" stroke="#2563eb" stroke-width="2.2"/>

  <!-- Base Nitrogenada: Guanina (C6=O, C2-NH2) -->
  <polygon points="48,38 50,16 72,16 82,32 65,48" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <polygon points="50,16 32,4 14,14 14,34 30,44 48,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C6=O -->
  <line x1="32" y1="4" x2="32" y2="-10" stroke="#dc2626" stroke-width="2.2"/>
  <text x="32" y="-13" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <!-- C2-NH2 -->
  <line x1="14" y1="34" x2="-2" y2="40" stroke="#2563eb" stroke-width="2"/>
  <text x="-6" y="44" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="end">H₂N</text>
  <text x="14" y="18" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
</g>
"""

# =============================================================================
# 4. PRECURSORES Y PRODUCTOS PIRIMIDÍNICOS (CARBAMOIL-P, OROTATO, UMP, CTP, dTMP)
# =============================================================================

CARBAMOIL_FOSFATO = """
<g class="mol-carbamoil-p" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo amino H2N- -->
  <text x="12" y="32" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#2563eb" stroke="none" text-anchor="end">H₂N</text>
  <line x1="16" y1="28" x2="38" y2="28" stroke="#0f172a" stroke-width="2.2"/>

  <!-- Carbono C=O -->
  <circle cx="44" cy="28" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="44" y1="22" x2="44" y2="6" stroke="#dc2626" stroke-width="2.2"/>
  <text x="44" y="2" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- Enlace éster fosfato -O-Ⓟ -->
  <line x1="48" y1="28" x2="68" y2="28" stroke="#ea580c" stroke-width="2.2"/>
  <circle cx="84" cy="28" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="84" y="32" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
</g>
"""

OROTATO = """
<g class="mol-orotato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Anillo de pirimidina-diona de 6 lados -->
  <polygon points="36,16 64,30 64,58 36,72 10,58 10,30" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2=O -->
  <line x1="10" y1="58" x2="-4" y2="66" stroke="#dc2626" stroke-width="2.2"/>
  <text x="-8" y="72" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>

  <!-- N1-H y N3-H -->
  <text x="10" y="34" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
  <text x="36" y="75" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">HN</text>

  <!-- C4=O -->
  <line x1="64" y1="58" x2="78" y2="66" stroke="#dc2626" stroke-width="2.2"/>
  <text x="84" y="72" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>

  <!-- C6: Carboxilato -COO- característico de Orotato -->
  <line x1="36" y1="16" x2="36" y2="0" stroke="#0f172a" stroke-width="2.2"/>
  <text x="36" y="-5" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""

UMP = """
<g class="mol-ump" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Ribosa-5-P -->
  <polygon points="35,58 65,74 52,100 18,100 5,74" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="35" cy="58" r="6" fill="#ffffff" stroke="none"/>
  <text x="35" y="62" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <line x1="5" y1="74" x2="-8" y2="60" stroke="#0f172a" stroke-width="2"/>
  <circle cx="-16" cy="50" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="-16" y="54" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
  <line x1="52" y1="100" x2="52" y2="110" stroke="#0f172a" stroke-width="1.8"/>
  <line x1="18" y1="100" x2="18" y2="110" stroke="#0f172a" stroke-width="1.8"/>

  <!-- Enlace beta N-glucosídico C1' -> N1 -->
  <line x1="65" y1="74" x2="65" y2="44" stroke="#2563eb" stroke-width="2.2"/>

  <!-- Base Nitrogenada: Uracilo (C2=O, C4=O) -->
  <polygon points="65,44 45,34 45,10 65,0 85,10 85,34" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C2=O -->
  <line x1="45" y1="34" x2="32" y2="40" stroke="#dc2626" stroke-width="2.2"/>
  <text x="28" y="45" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>
  <!-- C4=O -->
  <line x1="85" y1="10" x2="98" y2="4" stroke="#dc2626" stroke-width="2.2"/>
  <text x="103" y="8" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <!-- N3-H -->
  <text x="65" y="3" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
</g>
"""

CTP = """
<g class="mol-ctp" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Ribosa central -->
  <polygon points="40,58 70,74 57,100 23,100 10,74" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="40" cy="58" r="6" fill="#ffffff" stroke="none"/>
  <text x="40" y="62" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>

  <!-- Cadena Trifosfato en C5': Ⓟ~Ⓟ~Ⓟ -->
  <line x1="10" y1="74" x2="-8" y2="60" stroke="#ea580c" stroke-width="2"/>
  <rect x="-70" y="46" width="60" height="26" rx="13" fill="#fee2e2" stroke="#dc2626" stroke-width="2"/>
  <text x="-40" y="63" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#b91c1c" stroke="none" text-anchor="middle">Ⓟ~Ⓟ~Ⓟ</text>

  <!-- Enlace C1' -> N1 -->
  <line x1="70" y1="74" x2="70" y2="44" stroke="#2563eb" stroke-width="2.2"/>

  <!-- Base Nitrogenada: Citosina (C2=O, C4-NH2) -->
  <polygon points="70,44 50,34 50,10 70,0 90,10 90,34" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C2=O -->
  <line x1="50" y1="34" x2="38" y2="40" stroke="#dc2626" stroke-width="2"/>
  <text x="34" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>
  <!-- C4-NH2 -->
  <line x1="90" y1="10" x2="104" y2="4" stroke="#2563eb" stroke-width="2"/>
  <text x="108" y="8" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none">NH₂</text>
</g>
"""

DTMP = """
<g class="mol-dtmp" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- 2'-Desoxirribosa-5-P (sin OH en C2') -->
  <polygon points="35,58 65,74 52,100 18,100 5,74" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="35" cy="58" r="6" fill="#ffffff" stroke="none"/>
  <text x="35" y="62" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <line x1="5" y1="74" x2="-8" y2="60" stroke="#0f172a" stroke-width="2"/>
  <circle cx="-16" cy="50" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="-16" y="54" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
  <!-- Solo OH en C3' (C2' desoxi = sólo H) -->
  <line x1="18" y1="100" x2="18" y2="110" stroke="#0f172a" stroke-width="1.8"/>
  <text x="18" y="120" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">3'-OH</text>
  <text x="52" y="112" font-family="'JetBrains Mono', monospace" font-size="9" font-weight="700" fill="#64748b" stroke="none" text-anchor="middle">2'-H</text>

  <!-- Enlace beta N-glucosídico C1' -> N1 -->
  <line x1="65" y1="74" x2="65" y2="44" stroke="#2563eb" stroke-width="2.2"/>

  <!-- Base Nitrogenada: Timina (C2=O, C4=O, C5-CH3) -->
  <polygon points="65,44 45,34 45,10 65,0 85,10 85,34" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C2=O -->
  <line x1="45" y1="34" x2="32" y2="40" stroke="#dc2626" stroke-width="2.2"/>
  <text x="28" y="45" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>
  <!-- C4=O -->
  <line x1="85" y1="10" x2="98" y2="4" stroke="#dc2626" stroke-width="2.2"/>
  <text x="103" y="8" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <!-- C5-CH3 (Metilo distintivo transferido por Timidilato Sintasa) -->
  <line x1="85" y1="34" x2="102" y2="38" stroke="#7c3aed" stroke-width="2.4"/>
  <rect x="104" y="28" width="36" height="20" rx="5" fill="#f5f3ff" stroke="#7c3aed" stroke-width="1.5"/>
  <text x="122" y="42" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#7c3aed" stroke="none" text-anchor="middle">CH₃</text>
</g>
"""
