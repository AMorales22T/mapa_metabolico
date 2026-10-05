#!/usr/bin/env python3
"""
ESTRUCTURAS QUÍMICAS VECTORIALES SVG - TRANSAMINACIÓN Y DESAMINACIÓN OXIDATIVA
==============================================================================
Diseñadas bajo el Manual de Estilo Editorial Científico:
- Trazos oscuros grafito (#0f172a, stroke-width: 2.2px)
- Oxígenos de grupos carbonilo (C=O) y carboxilatos en rojo carmesí (#dc2626)
- Grupos amino (-NH3+ / -NH4+) en azul cobalto (#2563eb) con cápsula tenue (#eff6ff)
- Anillos aromáticos y cadenas alifáticas nítidas y despejadas
- Coenzima Piridoxal Fosfato (PLP) con anillo de piridina y grupo aldehído/base de Schiff
- Texto siempre con stroke="none" para renderizado tipográfico perfecto.
"""

# =============================================================================
# 1. ESQUELETO Y GRUPO GENERAL: AMINOÁCIDO GENÉRICO / L-ALANINA
# =============================================================================

# Aminoácido genérico (con grupo R lateral)
AMINOACIDO_GENERICO = """
<g class="mol-aminoacido-gen" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />

  <!-- C2: C-alfa quiral -->
  <circle cx="40" cy="48" r="2.5" fill="#0f172a" stroke="none"/>
  <!-- H a la izquierda -->
  <line x1="33" y1="48" x2="22" y2="48" />
  <text x="14" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">H</text>
  
  <!-- Grupo Amino (-NH3+) a la derecha -->
  <line x1="47" y1="48" x2="60" y2="48" stroke="#2563eb" stroke-width="2"/>
  <rect x="62" y="36" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="81" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>

  <!-- Enlace C-alfa hacia grupo R -->
  <line x1="40" y1="55" x2="40" y2="72" />
  <circle cx="40" cy="85" r="13" fill="#f1f5f9" stroke="#64748b" stroke-width="2"/>
  <text x="40" y="89" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#334155" stroke="none" text-anchor="middle">R</text>
</g>
"""

# Alfa-Cetoácido genérico (resultado de la transaminación del aminoácido)
ALFACETOACIDO_GENERICO = """
<g class="mol-alfacetoacido-gen" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />

  <!-- C2: C=O (Grupo ceto / carbonilo en alfa) -->
  <circle cx="40" cy="48" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="47" y1="45" x2="66" y2="45" stroke="#dc2626" stroke-width="2"/>
  <line x1="47" y1="49" x2="66" y2="49" stroke="#dc2626" stroke-width="2"/>
  <text x="73" y="51" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" stroke="none">O</text>

  <!-- Enlace C2 hacia grupo R -->
  <line x1="40" y1="54" x2="40" y2="72" />
  <circle cx="40" cy="85" r="13" fill="#f1f5f9" stroke="#64748b" stroke-width="2"/>
  <text x="40" y="89" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#334155" stroke="none" text-anchor="middle">R</text>
</g>
"""

# L-Alanina (3 Carbonos)
ALANINA = """
<g class="mol-alanina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />

  <!-- C2: C-alfa con grupo amino -->
  <circle cx="40" cy="48" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="33" y1="48" x2="22" y2="48" />
  <text x="14" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">H</text>
  
  <line x1="47" y1="48" x2="60" y2="48" stroke="#2563eb" stroke-width="2"/>
  <rect x="62" y="36" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="81" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>

  <!-- C3: Grupo metilo -CH3 -->
  <line x1="40" y1="55" x2="40" y2="72" />
  <text x="40" y="85" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₃</text>
</g>
"""

# Piruvato (3 Carbonos - Contraparte cetoácido de la Alanina)
PIRUVATO_AMINO = """
<g class="mol-piruvato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />

  <!-- C2: C=O Grupo Carbonilo -->
  <circle cx="40" cy="48" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="47" y1="45" x2="66" y2="45" stroke="#dc2626" stroke-width="2"/>
  <line x1="47" y1="49" x2="66" y2="49" stroke="#dc2626" stroke-width="2"/>
  <text x="73" y="51" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" stroke="none">O</text>

  <!-- C3: Metilo -CH3 -->
  <line x1="40" y1="54" x2="40" y2="72" />
  <text x="40" y="85" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">CH₃</text>
</g>
"""

# =============================================================================
# 2. EL PAR CENTRAL DE CONVERGENCIA: ALFA-CETOGLUTARATO Y L-GLUTAMATO (5C)
# =============================================================================

ALFA_CETOGLUTARATO = """
<g class="mol-alfacetoglutarato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="20" x2="40" y2="36" />

  <!-- C2: Carbonilo C=O -->
  <circle cx="40" cy="43" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="47" y1="40" x2="66" y2="40" stroke="#dc2626" stroke-width="2"/>
  <line x1="47" y1="44" x2="66" y2="44" stroke="#dc2626" stroke-width="2"/>
  <text x="73" y="46" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" stroke="none">O</text>

  <!-- Enlace C2 - C3 -->
  <line x1="40" y1="49" x2="40" y2="62" />

  <!-- C3: -CH2- -->
  <text x="40" y="74" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₂C</text>
  <line x1="40" y1="80" x2="40" y2="92" />

  <!-- C4: -CH2- -->
  <text x="40" y="104" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₂C</text>
  <line x1="40" y1="110" x2="40" y2="122" />

  <!-- C5: Carboxilato Inferior -->
  <text x="40" y="136" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""

GLUTAMATO = """
<g class="mol-glutamato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="20" x2="40" y2="36" />

  <!-- C2: CH(NH3+) -->
  <circle cx="40" cy="43" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="33" y1="43" x2="22" y2="43" />
  <text x="14" y="47" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">H</text>
  
  <line x1="46" y1="43" x2="58" y2="43" stroke="#2563eb" stroke-width="2"/>
  <rect x="60" y="32" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="79" y="48" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>

  <!-- Enlace C2 - C3 -->
  <line x1="40" y1="49" x2="40" y2="62" />

  <!-- C3: -CH2- -->
  <text x="40" y="74" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₂C</text>
  <line x1="40" y1="80" x2="40" y2="92" />

  <!-- C4: -CH2- -->
  <text x="40" y="104" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₂C</text>
  <line x1="40" y1="110" x2="40" y2="122" />

  <!-- C5: Carboxilato Inferior -->
  <text x="40" y="136" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""

# =============================================================================
# 3. EL PAR DEL CICLO DE LA UREA Y LANZADERA: OXALACETATO Y L-ASPARTATO (4C)
# =============================================================================

OXALACETATO_AMINO = """
<g class="mol-oxalacetato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />

  <!-- C2: C=O (Grupo ceto) -->
  <circle cx="40" cy="48" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="47" y1="45" x2="66" y2="45" stroke="#dc2626" stroke-width="2"/>
  <line x1="47" y1="49" x2="66" y2="49" stroke="#dc2626" stroke-width="2"/>
  <text x="73" y="51" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" stroke="none">O</text>

  <!-- Enlace C2 - C3 -->
  <line x1="40" y1="54" x2="40" y2="70" />

  <!-- C3: -CH2- -->
  <text x="40" y="84" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₂C</text>
  <line x1="40" y1="90" x2="40" y2="104" />

  <!-- C4: Carboxilato Inferior -->
  <text x="40" y="118" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""

ASPARTATO_AMINO = """
<g class="mol-aspartato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />

  <!-- C2: CH(NH3+) -->
  <circle cx="40" cy="48" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="33" y1="48" x2="22" y2="48" />
  <text x="14" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">H</text>
  
  <line x1="46" y1="48" x2="58" y2="48" stroke="#2563eb" stroke-width="2"/>
  <rect x="60" y="37" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="79" y="53" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>

  <!-- Enlace C2 - C3 -->
  <line x1="40" y1="54" x2="40" y2="70" />

  <!-- C3: -CH2- -->
  <text x="40" y="84" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₂C</text>
  <line x1="40" y1="90" x2="40" y2="104" />

  <!-- C4: Carboxilato Inferior -->
  <text x="40" y="118" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""

# =============================================================================
# 4. PRODUCTO DE DESAMINACIÓN Y TRANSPORTE: AMONIO (NH4+) Y L-GLUTAMINA (5C)
# =============================================================================

ION_AMONIO = """
<g class="mol-amonio" stroke="#2563eb" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <circle cx="35" cy="35" r="24" fill="#eff6ff" stroke="#2563eb" stroke-width="2.2"/>
  <text x="35" y="40" font-family="'Inter', sans-serif" font-size="14" font-weight="900" fill="#1d4ed8" stroke="none" text-anchor="middle">NH₄⁺</text>
  <text x="35" y="70" font-family="'Inter', sans-serif" font-size="9.5" font-weight="700" fill="#dc2626" stroke="none" text-anchor="middle">¡Tóxico!</text>
</g>
"""

GLUTAMINA = """
<g class="mol-glutamina" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="20" x2="40" y2="36" />

  <!-- C2: CH(NH3+) -->
  <circle cx="40" cy="43" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="33" y1="43" x2="22" y2="43" />
  <text x="14" y="47" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">H</text>
  
  <line x1="46" y1="43" x2="58" y2="43" stroke="#2563eb" stroke-width="2"/>
  <rect x="60" y="32" width="38" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="79" y="48" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">⁺NH₃</text>

  <!-- Enlace C2 - C3 -->
  <line x1="40" y1="49" x2="40" y2="62" />
  <!-- C3: -CH2- -->
  <text x="40" y="74" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₂C</text>
  <line x1="40" y1="80" x2="40" y2="92" />

  <!-- C4: -CH2- -->
  <text x="40" y="104" font-family="'Inter', sans-serif" font-size="11.5" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₂C</text>
  <line x1="40" y1="110" x2="40" y2="122" />

  <!-- C5: Grupo Amida terminal -CONH2 -->
  <text x="40" y="136" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" stroke="none" text-anchor="middle">C</text>
  <!-- O carbonílico -->
  <line x1="33" y1="135" x2="20" y2="135" stroke="#dc2626" stroke-width="2"/>
  <text x="12" y="139" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#dc2626" stroke="none" text-anchor="end">O</text>
  <!-- NH2 amídico -->
  <line x1="48" y1="135" x2="60" y2="135" stroke="#2563eb" stroke-width="2"/>
  <rect x="62" y="124" width="42" height="22" rx="6" fill="#eff6ff" stroke="#2563eb" stroke-width="1.4"/>
  <text x="83" y="140" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">NH₂</text>
</g>
"""

# =============================================================================
# 5. COENZIMA VITAL: PIRIDOXAL FOSFATO (PLP / VITAMINA B6)
# =============================================================================

PLP_COENZIMA = """
<g class="mol-plp" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Anillo de Piridina (Hexágono aromático con Nitrógeno) -->
  <polygon points="40,25 65,39 65,68 40,82 15,68 15,39" fill="#f8fafc" stroke="#0f172a" stroke-width="2.2"/>

  <!-- N en la base del anillo (posición 1 de piridina) -->
  <circle cx="40" cy="82" r="7" fill="#ffffff" stroke="none"/>
  <text x="40" y="86" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#2563eb" stroke="none" text-anchor="middle">N⁺</text>
  <!-- H en nitrógeno -->
  <line x1="40" y1="90" x2="40" y2="98" stroke="#0f172a" stroke-width="1.8"/>
  <text x="40" y="108" font-family="'Inter', sans-serif" font-size="10" font-weight="700" fill="#64748b" stroke="none" text-anchor="middle">H</text>

  <!-- C4 (Arriba): Grupo Aldehído C=O (o Base de Schiff con enzima) -->
  <line x1="40" y1="25" x2="40" y2="10" stroke="#0f172a" stroke-width="2.2"/>
  <text x="40" y="6" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">HC=O</text>
  <text x="40" y="-7" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#0d9488" stroke="none" text-anchor="middle">(Sitio de Unión)</text>

  <!-- C3 (Arriba-derecha): Grupo Fenólico -OH -->
  <line x1="65" y1="39" x2="78" y2="32" stroke="#dc2626" stroke-width="2"/>
  <text x="82" y="34" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#dc2626" stroke="none">O⁻</text>

  <!-- C2 (Abajo-derecha): Grupo Metilo -CH3 -->
  <line x1="65" y1="68" x2="80" y2="76" stroke="#0f172a" stroke-width="2"/>
  <text x="84" y="82" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#0f172a" stroke="none">CH₃</text>

  <!-- C5 (Arriba-izquierda): Cadena hacia el Fosfato (-CH2-O-P) -->
  <line x1="15" y1="39" x2="-2" y2="30" stroke="#0f172a" stroke-width="2"/>
  <circle cx="-16" cy="22" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="-16" y="27" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
  <text x="-36" y="26" font-family="'Inter', sans-serif" font-size="8.5" font-weight="800" fill="#ea580c" stroke="none" text-anchor="end">O-PO₃²⁻</text>
</g>
"""
