#!/usr/bin/env python3
"""
ESTRUCTURAS MOLECULARES ESPECÍFICAS DE LA GLUCONEOGÉNESIS
=========================================================
Fórmulas químicas vectoriales nítidas (Fischer / Kekulé) para los intermediarios
y precursores gluconeogénicos.
Diseñadas bajo el estándar de Biología Estructural:
- Enlaces químicos negros nítidos (#0f172a)
- Oxígenos y carboxilatos en rojo (#dc2626)
- Hidroxilos en azul (#0284c7)
- Nitrógenos/aminas en azul violeta (#4338ca)
- Textos limpios sin stroke heredado
"""

# 1. Oxalacetato (OAA) - C4H2O5 (2-)
# -OOC - CH2 - C(=O) - COO-
OXALACETATO = """
<g class="molecula-oxalacetato">
  <!-- C1: Carboxilato Superior -->
  <text x="50" y="18" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>
  <line x1="50" y1="24" x2="50" y2="38" stroke="#0f172a" stroke-width="2.2" />

  <!-- C2: Carbonilo (C=O) -->
  <text x="50" y="50" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">C</text>
  <line x1="58" y1="45" x2="74" y2="45" stroke="#dc2626" stroke-width="2.2" />
  <line x1="58" y1="49" x2="74" y2="49" stroke="#dc2626" stroke-width="2.2" />
  <text x="82" y="51" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626">O</text>

  <!-- Enlace C2 - C3 -->
  <line x1="50" y1="55" x2="50" y2="70" stroke="#0f172a" stroke-width="2.2" />

  <!-- C3: Metileno (-CH2-) -->
  <text x="50" y="82" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">CH₂</text>

  <!-- Enlace C3 - C4 -->
  <line x1="50" y1="87" x2="50" y2="102" stroke="#0f172a" stroke-width="2.2" />

  <!-- C4: Carboxilato Inferior -->
  <text x="50" y="116" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>
</g>
"""

# 2. L-Malato - C4H4O5 (2-)
# -OOC - CH2 - CH(OH) - COO-
MALATO = """
<g class="molecula-malato">
  <!-- C1: Carboxilato Superior -->
  <text x="50" y="18" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>
  <line x1="50" y1="24" x2="50" y2="38" stroke="#0f172a" stroke-width="2.2" />

  <!-- C2: Carbono quiral H-C-OH -->
  <line x1="42" y1="46" x2="31" y2="46" stroke="#0f172a" stroke-width="2" />
  <text x="24" y="50" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#64748b" text-anchor="end">H</text>
  <text x="50" y="50" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">C</text>
  <line x1="58" y1="46" x2="69" y2="46" stroke="#0284c7" stroke-width="2" />
  <text x="75" y="50" font-family="'Inter', sans-serif" font-size="12.5" font-weight="800" fill="#0284c7">OH</text>

  <!-- Enlace C2 - C3 -->
  <line x1="50" y1="55" x2="50" y2="70" stroke="#0f172a" stroke-width="2.2" />

  <!-- C3: Metileno (-CH2-) -->
  <text x="50" y="82" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">CH₂</text>

  <!-- Enlace C3 - C4 -->
  <line x1="50" y1="87" x2="50" y2="102" stroke="#0f172a" stroke-width="2.2" />

  <!-- C4: Carboxilato Inferior -->
  <text x="50" y="116" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>
</g>
"""

# 3. L-Lactato - C3H5O3 (-)
# CH3 - CH(OH) - COO-
LACTATO = """
<g class="molecula-lactato">
  <!-- C1: Carboxilato Superior -->
  <text x="50" y="18" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>
  <line x1="50" y1="24" x2="50" y2="38" stroke="#0f172a" stroke-width="2.2" />

  <!-- C2: Carbono quiral H-C-OH -->
  <line x1="42" y1="46" x2="31" y2="46" stroke="#0f172a" stroke-width="2" />
  <text x="24" y="50" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#64748b" text-anchor="end">H</text>
  <text x="50" y="50" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">C</text>
  <line x1="58" y1="46" x2="69" y2="46" stroke="#0284c7" stroke-width="2" />
  <text x="75" y="50" font-family="'Inter', sans-serif" font-size="12.5" font-weight="800" fill="#0284c7">OH</text>

  <!-- Enlace C2 - C3 -->
  <line x1="50" y1="55" x2="50" y2="72" stroke="#0f172a" stroke-width="2.2" />

  <!-- C3: Grupo Metilo -->
  <text x="50" y="86" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">CH₃</text>
</g>
"""

# 4. Icono molecular del Complejo Translocasa del RE (Glucosa-6-Fosfatasa)
RE_GLUCOSA_6_FOSFATASA = """
<g class="organelo-re-g6pase">
  <!-- Membrana del Retículo Endoplásmico Liso (Bicapa Luminal) -->
  <rect x="0" y="10" width="170" height="70" rx="8" fill="#f8fafc" stroke="#64748b" stroke-width="1.8"/>
  <line x1="0" y1="32" x2="170" y2="32" stroke="#94a3b8" stroke-dasharray="4 2"/>
  <line x1="0" y1="58" x2="170" y2="58" stroke="#94a3b8" stroke-dasharray="4 2"/>

  <!-- Transportador T1 (Importa G-6-P) -->
  <rect x="15" y="24" width="28" height="38" rx="5" fill="#0284c7" stroke="#0369a1" stroke-width="1.8"/>
  <text x="29" y="48" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="900" fill="#ffffff" text-anchor="middle">T1</text>

  <!-- Subunidad Catalítica (Cara Luminal del RE) -->
  <circle cx="85" cy="43" r="18" fill="#fef3c7" stroke="#b45309" stroke-width="2"/>
  <text x="85" y="47" font-family="'JetBrains Mono', monospace" font-size="10.5" font-weight="900" fill="#92400e" text-anchor="middle">G6Pase</text>

  <!-- Transportadores T2 (Exporta Pi) y T3 (Exporta Glucosa) -->
  <rect x="125" y="24" width="28" height="38" rx="5" fill="#059669" stroke="#047857" stroke-width="1.8"/>
  <text x="139" y="48" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#ffffff" text-anchor="middle">T2/T3</text>

  <!-- Rótulo de compartimento -->
  <text x="85" y="5" font-family="'Inter', sans-serif" font-size="9" font-weight="800" fill="#64748b" text-anchor="middle">LUMEN DEL RE</text>
</g>
"""

# 5. Glicerol - Precursor gluconeogénico de lipólisis
# CH2OH - CH(OH) - CH2OH
GLICEROL = """
<g class="molecula-glicerol">
  <!-- C1: Hidroximetilo Superior -->
  <text x="50" y="18" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0284c7" text-anchor="middle">CH₂OH</text>
  <line x1="50" y1="24" x2="50" y2="38" stroke="#0f172a" stroke-width="2.2" />

  <!-- C2: Carbono quiral H-C-OH -->
  <line x1="42" y1="46" x2="31" y2="46" stroke="#0f172a" stroke-width="2" />
  <text x="24" y="50" font-family="'Inter', sans-serif" font-size="12" font-weight="700" fill="#64748b" text-anchor="end">H</text>
  <text x="50" y="50" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">C</text>
  <line x1="58" y1="46" x2="69" y2="46" stroke="#0284c7" stroke-width="2" />
  <text x="75" y="50" font-family="'Inter', sans-serif" font-size="12.5" font-weight="800" fill="#0284c7">OH</text>

  <!-- Enlace C2 - C3 -->
  <line x1="50" y1="55" x2="50" y2="72" stroke="#0f172a" stroke-width="2.2" />

  <!-- C3: Hidroximetilo Inferior -->
  <text x="50" y="86" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0284c7" text-anchor="middle">CH₂OH</text>
</g>
"""
