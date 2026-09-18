#!/usr/bin/env python3
"""
ESTRUCTURAS QUÍMICAS VECTORIALES SVG - LANZADERA MALATO-ASPARTATO
================================================================
Estructuras 2D precisas según el manual de estilo editorial:
- Trazos oscuros (#0f172a, stroke-width: 2.2px)
- Oxígenos y carboxilatos en rojo carmesí (#dc2626)
- Hidroxilos (-OH) en azul cian (#0284c7)
- Grupos amino (-NH3+) en azul cobalto (#2563eb)
- Texto siempre con stroke="none" para renderizado tipográfico perfecto.
"""

OXALACETATO = """
<g class="mol-oxalacetato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />

  <!-- C2: C=O (Grupo ceto / carbonilo) -->
  <circle cx="40" cy="48" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="47" y1="45" x2="66" y2="45" stroke="#dc2626" stroke-width="2"/>
  <line x1="47" y1="49" x2="66" y2="49" stroke="#dc2626" stroke-width="2"/>
  <text x="73" y="51" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" stroke="none">O</text>

  <!-- Enlace C2 - C3 -->
  <line x1="40" y1="54" x2="40" y2="70" />

  <!-- C3: Grupo metileno -CH2- -->
  <text x="40" y="84" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₂C</text>
  <line x1="40" y1="90" x2="40" y2="104" />

  <!-- C4: Carboxilato Inferior -->
  <text x="40" y="118" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""

MALATO = """
<g class="mol-malato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />

  <!-- C2: CH(OH) (Carbono quiral con hidroxilo) -->
  <circle cx="40" cy="48" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="33" y1="48" x2="22" y2="48" />
  <text x="14" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">H</text>
  
  <line x1="47" y1="48" x2="63" y2="48" stroke="#0284c7" stroke-width="2"/>
  <text x="70" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0284c7" stroke="none">OH</text>

  <!-- Enlace C2 - C3 -->
  <line x1="40" y1="54" x2="40" y2="70" />

  <!-- C3: Grupo metileno -CH2- -->
  <text x="40" y="84" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₂C</text>
  <line x1="40" y1="90" x2="40" y2="104" />

  <!-- C4: Carboxilato Inferior -->
  <text x="40" y="118" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
</g>
"""

ASPARTATO = """
<g class="mol-aspartato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />

  <!-- C2: CH(NH3+) (Carbono quiral con grupo amino) -->
  <circle cx="40" cy="48" r="2.5" fill="#0f172a" stroke="none"/>
  <line x1="33" y1="48" x2="22" y2="48" />
  <text x="14" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="end">H</text>
  
  <line x1="47" y1="48" x2="62" y2="48" stroke="#2563eb" stroke-width="2"/>
  <text x="69" y="52" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none">⁺NH₃</text>

  <!-- Enlace C2 - C3 -->
  <line x1="40" y1="54" x2="40" y2="70" />

  <!-- C3: Grupo metileno -CH2- -->
  <text x="40" y="84" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" stroke="none" text-anchor="middle">H₂C</text>
  <line x1="40" y1="90" x2="40" y2="104" />

  <!-- C4: Carboxilato Inferior -->
  <text x="40" y="118" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none" text-anchor="middle">COO⁻</text>
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
  
  <line x1="47" y1="43" x2="62" y2="43" stroke="#2563eb" stroke-width="2"/>
  <text x="69" y="47" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none">⁺NH₃</text>

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
