#!/usr/bin/env python3
"""
ESTRUCTURAS QUÍMICAS VECTORIALES SVG - DEGRADACIÓN DE NUCLEÓTIDOS Y ÁCIDO ÚRICO
==============================================================================
Diseñadas bajo el Manual de Estilo Editorial Científico:
- Trazos oscuros grafito (#0f172a, stroke-width: 2.2px)
- Oxígenos (C=O, anillos) en rojo carmesí (#dc2626)
- Nitrógenos de anillos purina/pirimidina en azul cobalto (#2563eb)
- Grupos carboxilato y amino perfectamente diferenciados
- Estructuras nítidas 2D sin cajas contenedoras
- Texto con stroke="none" para renderizado tipográfico perfecto.
"""

# =============================================================================
# 1. CATABOLISMO DE PURINAS: BASES E INTERMEDIARIOS
# =============================================================================

# Adenosina (Nucleósido de adenina)
ADENOSINA = """
<g class="mol-adenosina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Ribosa (abajo) -->
  <polygon points="35,62 65,78 52,104 18,104 5,78" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="35" cy="62" r="6" fill="#ffffff" stroke="none"/>
  <text x="35" y="66" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <!-- 5'-CH2OH libre (sin fosfato) -->
  <line x1="5" y1="78" x2="-8" y2="64" stroke="#0f172a" stroke-width="2"/>
  <text x="-12" y="62" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">HO-CH₂</text>
  <!-- OH en C2/C3 -->
  <line x1="52" y1="104" x2="52" y2="114" stroke="#0f172a" stroke-width="1.8"/>
  <line x1="18" y1="104" x2="18" y2="114" stroke="#0f172a" stroke-width="1.8"/>

  <!-- Enlace beta N-glucosídico C1' -> N9 -->
  <line x1="65" y1="78" x2="65" y2="48" stroke="#2563eb" stroke-width="2.2"/>

  <!-- Anillo de Adenina -->
  <polygon points="48,38 50,16 72,16 82,32 65,48" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <polygon points="50,16 32,4 14,14 14,34 30,44 48,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C6-NH2 -->
  <line x1="32" y1="4" x2="32" y2="-10" stroke="#2563eb" stroke-width="2"/>
  <text x="32" y="-13" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH₂</text>
  <text x="14" y="27" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">N</text>
</g>
"""

# Inosina (Nucleósido de hipoxantina)
INOSINA = """
<g class="mol-inosina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Ribosa (abajo) -->
  <polygon points="35,62 65,78 52,104 18,104 5,78" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="35" cy="62" r="6" fill="#ffffff" stroke="none"/>
  <text x="35" y="66" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <line x1="5" y1="78" x2="-8" y2="64" stroke="#0f172a" stroke-width="2"/>
  <text x="-12" y="62" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">HO-CH₂</text>
  <line x1="52" y1="104" x2="52" y2="114" stroke="#0f172a" stroke-width="1.8"/>
  <line x1="18" y1="104" x2="18" y2="114" stroke="#0f172a" stroke-width="1.8"/>

  <!-- Enlace beta N-glucosídico C1' -> N9 -->
  <line x1="65" y1="78" x2="65" y2="48" stroke="#2563eb" stroke-width="2.2"/>

  <!-- Base: Hipoxantina (C6=O) -->
  <polygon points="48,38 50,16 72,16 82,32 65,48" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <polygon points="50,16 32,4 14,14 14,34 30,44 48,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C6=O -->
  <line x1="32" y1="4" x2="32" y2="-10" stroke="#dc2626" stroke-width="2.2"/>
  <text x="32" y="-13" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <text x="14" y="18" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
</g>
"""

# Hipoxantina libre (Base purínica)
HIPOXANTINA = """
<g class="mol-hipoxantina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Imidazol de 5 lados -->
  <polygon points="48,38 50,16 72,16 82,32 65,48" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- Pirimidina de 6 lados fusionada -->
  <polygon points="50,16 32,4 14,14 14,34 30,44 48,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C6=O -->
  <line x1="32" y1="4" x2="32" y2="-10" stroke="#dc2626" stroke-width="2.2"/>
  <text x="32" y="-13" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <text x="14" y="18" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
  <text x="65" y="52" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
</g>
"""

# Guanina libre
GUANINA = """
<g class="mol-guanina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Imidazol -->
  <polygon points="48,38 50,16 72,16 82,32 65,48" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- Pirimidina -->
  <polygon points="50,16 32,4 14,14 14,34 30,44 48,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C6=O -->
  <line x1="32" y1="4" x2="32" y2="-10" stroke="#dc2626" stroke-width="2.2"/>
  <text x="32" y="-13" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <!-- C2-NH2 -->
  <line x1="14" y1="34" x2="-2" y2="40" stroke="#2563eb" stroke-width="2"/>
  <text x="-6" y="44" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="end">H₂N</text>
  <text x="14" y="18" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
  <text x="65" y="52" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
</g>
"""

# Xantina (2,6-Dioxipurina)
XANTINA = """
<g class="mol-xantina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Imidazol -->
  <polygon points="48,38 50,16 72,16 82,32 65,48" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- Pirimidina -->
  <polygon points="50,16 32,4 14,14 14,34 30,44 48,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C6=O (Primer carbonilo) -->
  <line x1="32" y1="4" x2="32" y2="-10" stroke="#dc2626" stroke-width="2.2"/>
  <text x="32" y="-13" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <!-- C2=O (Segundo carbonilo introducido por XOD o Guanasa) -->
  <line x1="14" y1="34" x2="-2" y2="40" stroke="#dc2626" stroke-width="2.2"/>
  <text x="-6" y="45" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>
  <!-- N1-H y N3-H -->
  <text x="14" y="18" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
  <text x="30" y="47" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">HN</text>
  <text x="65" y="52" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
</g>
"""

# Ácido Úrico (2,6,8-Trioxipurina / Urato)
ACIDO_URICO = """
<g class="mol-acido-urico" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Imidazol con C8=O -->
  <polygon points="48,38 50,16 72,16 82,32 65,48" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C8=O (Tercer carbonilo característico de ácido úrico) -->
  <line x1="82" y1="32" x2="98" y2="32" stroke="#dc2626" stroke-width="2.2"/>
  <text x="103" y="36" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>

  <!-- Pirimidina con C6=O y C2=O -->
  <polygon points="50,16 32,4 14,14 14,34 30,44 48,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C6=O -->
  <line x1="32" y1="4" x2="32" y2="-10" stroke="#dc2626" stroke-width="2.2"/>
  <text x="32" y="-13" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <!-- C2=O -->
  <line x1="14" y1="34" x2="-2" y2="40" stroke="#dc2626" stroke-width="2.2"/>
  <text x="-6" y="45" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>

  <!-- 4 Grupos N-H en las 4 posiciones del anillo -->
  <text x="14" y="18" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
  <text x="30" y="47" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">HN</text>
  <text x="72" y="14" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">HN</text>
  <text x="65" y="52" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
</g>
"""

# =============================================================================
# 2. CATABOLISMO DE PIRIMIDINAS: INTERMEDIARIOS Y PRODUCTOS SOLUBLES
# =============================================================================

# Uracilo (Base pirimidínica libre)
URACILO = """
<g class="mol-uracilo" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="40,34 20,24 20,0 40,-10 60,0 60,24" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C2=O -->
  <line x1="20" y1="24" x2="6" y2="30" stroke="#dc2626" stroke-width="2.2"/>
  <text x="2" y="35" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>
  <!-- C4=O -->
  <line x1="60" y1="0" x2="74" y2="-6" stroke="#dc2626" stroke-width="2.2"/>
  <text x="78" y="-2" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <text x="40" y="-7" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
  <text x="40" y="38" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">HN</text>
</g>
"""

# Timina (5-Metiluracilo libre)
TIMINA = """
<g class="mol-timina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="40,34 20,24 20,0 40,-10 60,0 60,24" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C2=O -->
  <line x1="20" y1="24" x2="6" y2="30" stroke="#dc2626" stroke-width="2.2"/>
  <text x="2" y="35" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>
  <!-- C4=O -->
  <line x1="60" y1="0" x2="74" y2="-6" stroke="#dc2626" stroke-width="2.2"/>
  <text x="78" y="-2" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <!-- C5-CH3 -->
  <line x1="60" y1="24" x2="76" y2="28" stroke="#7c3aed" stroke-width="2.2"/>
  <text x="82" y="32" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#7c3aed" stroke="none">CH₃</text>
  <text x="40" y="-7" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
  <text x="40" y="38" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">HN</text>
</g>
"""

# Dihidrouracilo (Anillo saturado sin C=C)
DIHIDROURACILO = """
<g class="mol-dihidrouracilo" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Anillo saturado (enlaces simples) -->
  <polygon points="40,34 20,24 20,0 40,-10 60,0 60,24" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C2=O -->
  <line x1="20" y1="24" x2="6" y2="30" stroke="#dc2626" stroke-width="2.2"/>
  <text x="2" y="35" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>
  <!-- C4=O -->
  <line x1="60" y1="0" x2="74" y2="-6" stroke="#dc2626" stroke-width="2.2"/>
  <text x="78" y="-2" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <!-- N1-H y N3-H -->
  <text x="40" y="-7" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
  <text x="40" y="38" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">HN</text>
  <!-- C5 y C6 saturados (-CH2-CH2-) -->
  <text x="64" y="22" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="700" fill="#64748b" stroke="none">H₂</text>
  <text x="48" y="35" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="700" fill="#64748b" stroke="none">H₂</text>
</g>
"""

# Dihidrotimina (Anillo saturado con metilo en C5)
DIHIDROTIMINA = """
<g class="mol-dihidrotimina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <polygon points="40,34 20,24 20,0 40,-10 60,0 60,24" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <!-- C2=O -->
  <line x1="20" y1="24" x2="6" y2="30" stroke="#dc2626" stroke-width="2.2"/>
  <text x="2" y="35" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="end">O</text>
  <!-- C4=O -->
  <line x1="60" y1="0" x2="74" y2="-6" stroke="#dc2626" stroke-width="2.2"/>
  <text x="78" y="-2" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <!-- C5-CH3 -->
  <line x1="60" y1="24" x2="76" y2="28" stroke="#7c3aed" stroke-width="2.2"/>
  <text x="82" y="32" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#7c3aed" stroke="none">CH₃</text>
  <text x="40" y="-7" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
  <text x="40" y="38" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">HN</text>
  <text x="48" y="35" font-family="'JetBrains Mono', monospace" font-size="7.5" font-weight="700" fill="#64748b" stroke="none">H₂</text>
</g>
"""

# Beta-Ureidopropionato (Cadena abierta lineal de Uracilo)
BETA_UREIDOPROPIONATO = """
<g class="mol-beta-ureidopropionato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo carbamoil/ureido: H2N-C(=O)-NH- -->
  <text x="10" y="24" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#2563eb" stroke="none" text-anchor="end">H₂N</text>
  <line x1="14" y1="20" x2="27" y2="20" stroke="#0f172a" stroke-width="2"/>
  <!-- C=O -->
  <text x="34" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="32" y1="14" x2="32" y2="4" stroke="#dc2626" stroke-width="2"/>
  <line x1="36" y1="14" x2="36" y2="4" stroke="#dc2626" stroke-width="2"/>
  <text x="34" y="0" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <!-- -NH- -->
  <line x1="41" y1="20" x2="53" y2="20" stroke="#2563eb" stroke-width="2"/>
  <text x="64" y="24" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
  <!-- -CH2-CH2- -->
  <line x1="75" y1="20" x2="83" y2="20" stroke="#0f172a" stroke-width="2"/>
  <text x="95" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="107" y1="20" x2="115" y2="20" stroke="#0f172a" stroke-width="2"/>
  <text x="127" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <!-- -COO- terminal -->
  <line x1="139" y1="20" x2="147" y2="20" stroke="#0f172a" stroke-width="2"/>
  <text x="150" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
</g>
"""

# Beta-Ureidoisobutirato (Cadena abierta lineal de Timina con metilo)
BETA_UREIDOISOBUTIRATO = """
<g class="mol-beta-ureidoisobutirato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- H2N-C(=O)-NH- -->
  <text x="10" y="24" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#2563eb" stroke="none" text-anchor="end">H₂N</text>
  <line x1="14" y1="20" x2="27" y2="20" stroke="#0f172a" stroke-width="2"/>
  <!-- C=O -->
  <text x="34" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <line x1="32" y1="14" x2="32" y2="4" stroke="#dc2626" stroke-width="2"/>
  <line x1="36" y1="14" x2="36" y2="4" stroke="#dc2626" stroke-width="2"/>
  <text x="34" y="0" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">O</text>
  <!-- -NH- -->
  <line x1="41" y1="20" x2="53" y2="20" stroke="#2563eb" stroke-width="2"/>
  <text x="64" y="24" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH</text>
  <!-- -CH2- -->
  <line x1="75" y1="20" x2="83" y2="20" stroke="#0f172a" stroke-width="2"/>
  <text x="95" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <!-- -CH(CH3)- con metilo en C-alfa -->
  <line x1="107" y1="20" x2="115" y2="20" stroke="#0f172a" stroke-width="2"/>
  <text x="125" y="24" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <line x1="125" y1="13" x2="125" y2="5" stroke="#7c3aed" stroke-width="2"/>
  <text x="125" y="2" font-family="'Inter', sans-serif" font-size="9" font-weight="900" fill="#7c3aed" stroke="none" text-anchor="middle">CH₃</text>
  <!-- -COO- terminal -->
  <line x1="135" y1="20" x2="143" y2="20" stroke="#0f172a" stroke-width="2"/>
  <text x="147" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
</g>
"""

# Beta-Alanina (Producto soluble final de Uracilo y Citosina)
BETA_ALANINA = """
<g class="mol-beta-alanina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Grupo amino beta: H3N+-CH2-CH2-COO- -->
  <text x="12" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="end">⁺H₃N</text>
  <line x1="16" y1="20" x2="26" y2="20" stroke="#0f172a" stroke-width="2"/>
  <!-- C-beta CH2 -->
  <text x="38" y="24" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="50" y1="20" x2="58" y2="20" stroke="#0f172a" stroke-width="2"/>
  <!-- C-alfa CH2 -->
  <text x="70" y="24" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <line x1="82" y1="20" x2="90" y2="20" stroke="#0f172a" stroke-width="2"/>
  <!-- Carboxilato terminal -->
  <text x="94" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
</g>
"""

# Beta-Aminoisobutirato (Producto soluble final de Timina)
BETA_AMINOISOBUTIRATO = """
<g class="mol-beta-aminoisobutirato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- H3N+-CH2-CH(CH3)-COO- -->
  <text x="12" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="end">⁺H₃N</text>
  <line x1="16" y1="20" x2="26" y2="20" stroke="#0f172a" stroke-width="2"/>
  <text x="38" y="24" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₂</text>
  <!-- C-alfa con grupo metilo -->
  <line x1="50" y1="20" x2="58" y2="20" stroke="#0f172a" stroke-width="2"/>
  <text x="68" y="24" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH</text>
  <line x1="68" y1="13" x2="68" y2="5" stroke="#7c3aed" stroke-width="2"/>
  <text x="68" y="2" font-family="'Inter', sans-serif" font-size="9.5" font-weight="900" fill="#7c3aed" stroke="none" text-anchor="middle">CH₃</text>
  <!-- Carboxilato -->
  <line x1="78" y1="20" x2="86" y2="20" stroke="#0f172a" stroke-width="2"/>
  <text x="90" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none">COO⁻</text>
</g>
"""

