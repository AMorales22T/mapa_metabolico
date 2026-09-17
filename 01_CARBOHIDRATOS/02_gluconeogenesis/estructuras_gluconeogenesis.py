#!/usr/bin/env python3
"""
ESTRUCTURAS MOLECULARES ESPECÍFICAS DE LA GLUCONEOGÉNESIS
=========================================================
Contiene las fórmulas químicas vectoriales (Fischer / Kekulé) para los intermediarios
exclusivos de los bypasses mitocondriales y citosólicos:
1. Oxalacetato (OAA) - Dicarboxilato de 4C (α-cetoácido)
2. L-Malato - Intermediario de la lanzadera mitocondrial
3. L-Lactato - Sustrato gluconeogénico del Ciclo de Cori
4. Biotina-Carboxilasa (complejo activado con CO2)
"""

# 1. Oxalacetato (OAA) - C4H2O5 (2-)
# -OOC - CH2 - C(=O) - COO-
OXALACETATO = """
<g class="molecula-oxalacetato" stroke="#0f172a" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="50" y="20" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>
  <line x1="50" y1="25" x2="50" y2="42" />

  <!-- C2 Carbonilo (α-Ceto) -->
  <circle cx="50" cy="50" r="3" fill="#0f172a"/>
  <!-- Doble enlace =O a la derecha -->
  <line x1="52" y1="48" x2="72" y2="48" stroke="#dc2626" stroke-width="2.2"/>
  <line x1="52" y1="53" x2="72" y2="53" stroke="#dc2626" stroke-width="2.2"/>
  <text x="82" y="55" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">O</text>

  <!-- Enlace C2 - C3 -->
  <line x1="50" y1="52" x2="50" y2="75" />

  <!-- C3 Metileno (-CH2-) -->
  <circle cx="50" cy="80" r="3" fill="#0f172a"/>
  <text x="25" y="85" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle">H₂C</text>

  <!-- Enlace C3 - C4 -->
  <line x1="50" y1="84" x2="50" y2="102" />

  <!-- C4 Carboxilato Inferior -->
  <text x="50" y="118" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>
</g>
"""

# 2. L-Malato - C4H4O5 (2-)
# -OOC - CH2 - CH(OH) - COO-
MALATO = """
<g class="molecula-malato" stroke="#0f172a" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="50" y="20" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>
  <line x1="50" y1="25" x2="50" y2="44" />

  <!-- C2 Hidroxilo (-CH(OH)-) -->
  <circle cx="50" cy="50" r="3" fill="#0f172a"/>
  <!-- Enlace -OH a la derecha -->
  <line x1="53" y1="50" x2="72" y2="50" stroke="#0284c7" stroke-width="2"/>
  <text x="85" y="55" font-family="'Inter', sans-serif" font-size="12.5" font-weight="800" fill="#0284c7" text-anchor="middle">OH</text>
  <text x="32" y="55" font-family="'Inter', sans-serif" font-size="11.5" font-weight="700" fill="#64748b" text-anchor="middle">H</text>

  <!-- Enlace C2 - C3 -->
  <line x1="50" y1="54" x2="50" y2="76" />

  <!-- C3 Metileno (-CH2-) -->
  <circle cx="50" cy="80" r="3" fill="#0f172a"/>
  <text x="25" y="85" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle">H₂C</text>

  <!-- Enlace C3 - C4 -->
  <line x1="50" y1="84" x2="50" y2="102" />

  <!-- C4 Carboxilato Inferior -->
  <text x="50" y="118" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>
</g>
"""

# 3. L-Lactato - C3H5O3 (-)
# CH3 - CH(OH) - COO-
LACTATO = """
<g class="molecula-lactato" stroke="#0f172a" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="50" y="20" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>
  <line x1="50" y1="25" x2="50" y2="44" />

  <!-- C2 Carbono quiral con -OH -->
  <circle cx="50" cy="50" r="3" fill="#0f172a"/>
  <line x1="53" y1="50" x2="72" y2="50" stroke="#0284c7" stroke-width="2"/>
  <text x="85" y="55" font-family="'Inter', sans-serif" font-size="12.5" font-weight="800" fill="#0284c7" text-anchor="middle">OH</text>
  <text x="32" y="55" font-family="'Inter', sans-serif" font-size="11.5" font-weight="700" fill="#64748b" text-anchor="middle">H</text>

  <!-- Enlace C2 - C3 -->
  <line x1="50" y1="54" x2="50" y2="76" />

  <!-- C3 Grupo Metilo (-CH3) -->
  <text x="50" y="92" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">CH₃</text>
</g>
"""

# 4. Icono molecular del Complejo Translocasa del RE (Glucosa-6-Fosfatasa)
RE_GLUCOSA_6_FOSFATASA = """
<g class="organelo-re-g6pase" stroke-linecap="round" stroke-linejoin="round">
  <!-- Membrana del Retículo Endoplásmico Liso (Bicapa Luminal) -->
  <rect x="0" y="10" width="170" height="70" rx="8" fill="#f8fafc" stroke="#64748b" stroke-width="2"/>
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
