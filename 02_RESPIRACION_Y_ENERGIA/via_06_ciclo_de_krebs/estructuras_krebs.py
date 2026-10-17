#!/usr/bin/env python3
"""
CATÁLOGO COMPLETO DE ESTRUCTURAS QUÍMICAS (SVG) - CICLO DE KREBS (TCA)
======================================================================
Diseñadas bajo el Manual de Estilo Editorial Bioquímico:
- Trazos oscuros nítidos (#0f172a, grosor 2.0 a 2.4 pt).
- Grupos carboxilato (COO⁻) resaltados con oxígeno en rojo (#dc2626).
- Grupos carbonilo (C=O) con doble enlace nítido y oxígeno rojo (#dc2626).
- Grupos hidroxilo (-OH) en azul bioquímico (#0284c7) para diferenciar oxidaciones.
- Enlace tioéster (~S-CoA) con azufre en dorado/ámbar (#d97706) y coenzima A destacada (#7c3aed).
- Sin cajas delimitadoras: moléculas limpias y suspendidas en el espacio orgánico.
"""

# =============================================================================
# 0. PRECURSOR / SUSTRATO ALIMENTADOR
# =============================================================================

# PIRUVATO (3 Carbonos - α-cetoácido proveniente de la Glucólisis)
# H3C - C(=O) - COO-
PIRUVATO = """
<g class="mol-piruvato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1: Carboxilato Superior -->
  <text x="40" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="40" y1="22" x2="40" y2="40" />

  <!-- C2: C=O (Grupo carbonilo α) -->
  <text x="40" y="52" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <line x1="47" y1="44" x2="66" y2="44" stroke="#dc2626" stroke-width="2"/>
  <line x1="47" y1="48" x2="66" y2="48" stroke="#dc2626" stroke-width="2"/>
  <text x="74" y="50" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" stroke="none">O</text>

  <!-- Enlace C2 - C3 -->
  <line x1="40" y1="54" x2="40" y2="72" />

  <!-- C3: Grupo metilo CH3 -->
  <text x="40" y="86" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">CH₃</text>
</g>
"""

# ACETIL-COENZIMA A (2 Carbonos activados en enlace tioéster de alta energía)
# H3C - C(=O) ~ S-CoA
ACETIL_COA = """
<g class="mol-acetil-coa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- CH3 Metilo izquierdo -->
  <text x="20" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">H₃C</text>
  <line x1="34" y1="40" x2="48" y2="40" />

  <!-- Carbono carbonílico C=O -->
  <text x="56" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <!-- Doble enlace =O arriba -->
  <line x1="53" y1="34" x2="53" y2="18" stroke="#dc2626" stroke-width="2"/>
  <line x1="58" y1="34" x2="58" y2="18" stroke="#dc2626" stroke-width="2"/>
  <text x="56" y="12" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle" stroke="none">O</text>

  <!-- Enlace tioéster hacia azufre S -->
  <line x1="64" y1="40" x2="78" y2="40" stroke="#d97706" stroke-width="2.4"/>
  <text x="86" y="44" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#d97706" text-anchor="middle" stroke="none">S</text>

  <!-- Enlace hacia Coenzima A -->
  <line x1="94" y1="40" x2="108" y2="40" stroke="#7c3aed" stroke-width="2"/>
  <!-- Cápsula / Badge de Coenzima A -->
  <rect x="110" y="28" width="48" height="24" rx="12" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="134" y="44" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" fill="#6b21a8" text-anchor="middle" stroke="none">CoA</text>
</g>
"""

# =============================================================================
# LOS 8 INTERMEDIARIOS DEL CICLO DE KREBS
# =============================================================================

# 1. OXALACETATO (OAA) - Dicarboxilato de 4C (α-cetoácido que reinicia el ciclo)
# -OOC - C(=O) - CH2 - COO-
OXALACETATO = """
<g class="mol-oxalacetato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="45" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="45" y1="22" x2="45" y2="38" />

  <!-- C2 Carbonilo (α-Ceto) -->
  <text x="45" y="48" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <!-- Doble enlace =O a la derecha -->
  <line x1="53" y1="42" x2="68" y2="42" stroke="#dc2626" stroke-width="2"/>
  <line x1="53" y1="46" x2="68" y2="46" stroke="#dc2626" stroke-width="2"/>
  <text x="77" y="48" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" stroke="none">O</text>

  <!-- Enlace C2 - C3 -->
  <line x1="45" y1="52" x2="45" y2="66" />

  <!-- C3 Metileno (-CH2-) -->
  <text x="45" y="78" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">CH₂</text>

  <!-- Enlace C3 - C4 -->
  <line x1="45" y1="84" x2="45" y2="98" />

  <!-- C4 Carboxilato Inferior -->
  <text x="45" y="112" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
</g>
"""

# 2. CITRATO - Tricarboxilato simétrico de 6C con alcohol terciario
# -OOC-CH2 - C(OH)(COO-) - CH2-COO-
CITRATO = """
<g class="mol-citrato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="50" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="50" y1="20" x2="50" y2="34" />

  <!-- C2 Metileno (-CH2-) -->
  <text x="50" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">CH₂</text>
  <line x1="50" y1="48" x2="50" y2="59" />

  <!-- C3 Carbono Central Cuaternario explícito -->
  <text x="50" y="71" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <!-- Grupo -OH a la izquierda -->
  <line x1="42" y1="67" x2="28" y2="67" stroke="#0284c7" stroke-width="2.2"/>
  <text x="16" y="71" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0284c7" text-anchor="middle" stroke="none">HO</text>
  <!-- Grupo -COO- central a la derecha -->
  <line x1="58" y1="67" x2="74" y2="67" stroke="#dc2626" stroke-width="2"/>
  <text x="94" y="71" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>

  <!-- Enlace C3 - C4 -->
  <line x1="50" y1="75" x2="50" y2="86" />

  <!-- C4 Metileno (-CH2-) -->
  <text x="50" y="96" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">CH₂</text>
  <line x1="50" y1="100" x2="50" y2="114" />

  <!-- C5 Carboxilato Inferior -->
  <text x="50" y="128" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
</g>
"""

# 3. cis-ACONITATO - Intermediario tricarboxilato insaturado (6C)
# -OOC-CH2 - C(COO-) = CH - COO-
CIS_ACONITATO = """
<g class="mol-cis-aconitato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="50" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="50" y1="20" x2="50" y2="34" />

  <!-- C2 Metileno (-CH2-) -->
  <text x="50" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">CH₂</text>
  <line x1="50" y1="48" x2="50" y2="59" />

  <!-- C3 Carbono alqueno con -COO- -->
  <text x="50" y="71" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <line x1="58" y1="67" x2="74" y2="67" stroke="#dc2626" stroke-width="2"/>
  <text x="94" y="71" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>

  <!-- Doble enlace C3 = C4 -->
  <line x1="47" y1="75" x2="47" y2="88" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="53" y1="75" x2="53" y2="88" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C4 Carbono alqueno (=CH-) -->
  <text x="50" y="98" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">CH</text>
  <line x1="50" y1="102" x2="50" y2="114" />

  <!-- C5 Carboxilato Inferior -->
  <text x="50" y="128" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
</g>
"""

# 4. D-ISOCITRATO - Tricarboxilato de 6C con alcohol secundario en C2
# -OOC-CH2 - CH(COO-) - CH(OH) - COO-
ISOCITRATO = """
<g class="mol-isocitrato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="50" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="50" y1="20" x2="50" y2="34" />

  <!-- C2 Metileno (-CH2-) -->
  <text x="50" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">CH₂</text>
  <line x1="50" y1="48" x2="50" y2="59" />

  <!-- C3 Carbono quiral con carboxilato (H-C-COO-) -->
  <text x="50" y="71" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <line x1="58" y1="67" x2="74" y2="67" stroke="#dc2626" stroke-width="2"/>
  <text x="94" y="71" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="42" y1="67" x2="32" y2="67" stroke="#0f172a" stroke-width="2"/>
  <text x="24" y="71" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">H</text>

  <!-- Enlace C3 - C4 -->
  <line x1="50" y1="75" x2="50" y2="85" />

  <!-- C4 Carbono quiral con alcohol secundario (HO-C-H) -->
  <text x="50" y="96" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <!-- Grupo -OH a la izquierda resaltado en azul -->
  <line x1="42" y1="92" x2="28" y2="92" stroke="#0284c7" stroke-width="2.2"/>
  <text x="16" y="96" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0284c7" text-anchor="middle" stroke="none">HO</text>
  <line x1="58" y1="92" x2="68" y2="92" stroke="#0f172a" stroke-width="2"/>
  <text x="75" y="96" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">H</text>

  <!-- Enlace C4 - C5 -->
  <line x1="50" y1="100" x2="50" y2="114" />

  <!-- C5 Carboxilato Inferior -->
  <text x="50" y="128" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
</g>
"""

# 5. α-CETOGLUTARATO (2-Oxoglutarato) - Dicarboxilato de 5C (α-cetoácido)
# -OOC - C(=O) - CH2 - CH2 - COO-
ALFA_CETOGLUTARATO = """
<g class="mol-alfa-cetoglutarato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="45" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="45" y1="20" x2="45" y2="33" />

  <!-- C2 Carbonilo (α-Ceto) explícito -->
  <text x="45" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <line x1="53" y1="38" x2="68" y2="38" stroke="#dc2626" stroke-width="2"/>
  <line x1="53" y1="42" x2="68" y2="42" stroke="#dc2626" stroke-width="2"/>
  <text x="77" y="44" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" stroke="none">O</text>

  <!-- Enlace C2 - C3 -->
  <line x1="45" y1="48" x2="45" y2="60" />

  <!-- C3 Metileno (-CH2-) -->
  <text x="45" y="70" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">CH₂</text>
  <line x1="45" y1="74" x2="45" y2="88" />

  <!-- C4 Metileno (-CH2-) -->
  <text x="45" y="98" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">CH₂</text>
  <line x1="45" y1="102" x2="45" y2="116" />

  <!-- C5 Carboxilato Inferior -->
  <text x="45" y="130" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
</g>
"""

# 6. SUCCINIL-COA - Tioéster de alta energía (4C + S-CoA)
# -OOC - CH2 - CH2 - C(=O) ~ S-CoA
SUCCINIL_COA = """
<g class="mol-succinil-coa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="45" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="45" y1="20" x2="45" y2="34" />

  <!-- C2 Metileno (-CH2-) -->
  <text x="45" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">CH₂</text>
  <line x1="45" y1="48" x2="45" y2="62" />

  <!-- C3 Metileno (-CH2-) -->
  <text x="45" y="72" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">CH₂</text>
  <line x1="45" y1="76" x2="45" y2="88" />

  <!-- C4 Carbonilo acoplado a tioéster explícito -->
  <text x="45" y="100" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <!-- Doble enlace =O a la izquierda -->
  <line x1="37" y1="94" x2="22" y2="94" stroke="#dc2626" stroke-width="2"/>
  <line x1="37" y1="98" x2="22" y2="98" stroke="#dc2626" stroke-width="2"/>
  <text x="14" y="100" font-family="'Inter', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="end" stroke="none">O</text>

  <!-- Enlace tioéster hacia azufre S a la derecha -->
  <line x1="53" y1="96" x2="68" y2="96" stroke="#d97706" stroke-width="2.4"/>
  <text x="76" y="100" font-family="'Inter', sans-serif" font-size="13" font-weight="900" fill="#d97706" text-anchor="middle" stroke="none">S</text>

  <!-- Enlace hacia Coenzima A -->
  <line x1="84" y1="96" x2="98" y2="96" stroke="#7c3aed" stroke-width="2"/>
  <rect x="100" y="84" width="46" height="24" rx="12" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.8"/>
  <text x="123" y="100" font-family="'JetBrains Mono', monospace" font-size="11" font-weight="800" fill="#6b21a8" text-anchor="middle" stroke="none">CoA</text>
</g>
"""

# 7. SUCCINATO - Dicarboxilato simétrico de 4C
# -OOC - CH2 - CH2 - COO-
SUCCINATO = """
<g class="mol-succinato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="45" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="45" y1="20" x2="45" y2="34" />

  <!-- C2 Metileno (-CH2-) -->
  <text x="45" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">CH₂</text>
  <line x1="45" y1="48" x2="45" y2="64" />

  <!-- C3 Metileno (-CH2-) -->
  <text x="45" y="74" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">CH₂</text>
  <line x1="45" y1="78" x2="45" y2="94" />

  <!-- C4 Carboxilato Inferior -->
  <text x="45" y="110" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
</g>
"""

# 8. FUMARATO - Dicarboxilato insaturado trans (4C) con carbonos explícitos
# trans- -OOC - CH = CH - COO-
FUMARATO = """
<g class="mol-fumarato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="45" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="45" y1="20" x2="45" y2="33" />

  <!-- C2 Carbono alqueno superior (H — C) -->
  <text x="45" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <line x1="37" y1="40" x2="25" y2="40" stroke="#0f172a" stroke-width="2"/>
  <text x="19" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="end" stroke="none">H</text>

  <!-- Doble enlace trans central C2 = C3 -->
  <line x1="42" y1="48" x2="42" y2="64" stroke="#0f172a" stroke-width="2.3"/>
  <line x1="48" y1="48" x2="48" y2="64" stroke="#0f172a" stroke-width="2.3"/>
  <text x="72" y="59" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">(trans)</text>

  <!-- C3 Carbono alqueno inferior (C — H en posición trans) -->
  <text x="45" y="76" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <line x1="53" y1="72" x2="65" y2="72" stroke="#0f172a" stroke-width="2"/>
  <text x="71" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="start" stroke="none">H</text>

  <!-- Enlace C3 - C4 -->
  <line x1="45" y1="81" x2="45" y2="96" />

  <!-- C4 Carboxilato Inferior -->
  <text x="45" y="110" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
</g>
"""

# 9. L-MALATO - Hidroxi dicarboxilato de 4C
# -OOC - CH2 - CH(OH) - COO-
MALATO = """
<g class="mol-malato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="45" y="14" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="45" y1="20" x2="45" y2="34" />

  <!-- C2 Carbono quiral con alcohol secundario (-CH-OH-) -->
  <text x="45" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <!-- Grupo -OH a la derecha en azul -->
  <line x1="53" y1="40" x2="68" y2="40" stroke="#0284c7" stroke-width="2.2"/>
  <text x="78" y="44" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0284c7" stroke="none">OH</text>
  <!-- H a la izquierda -->
  <line x1="37" y1="40" x2="27" y2="40" stroke="#0f172a" stroke-width="2"/>
  <text x="21" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="end" stroke="none">H</text>

  <!-- Enlace C2 - C3 -->
  <line x1="45" y1="48" x2="45" y2="64" />

  <!-- C3 Metileno (-CH2-) -->
  <text x="45" y="76" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle" stroke="none">CH₂</text>
  <line x1="45" y1="82" x2="45" y2="96" />

  <!-- C4 Carboxilato Inferior -->
  <text x="45" y="110" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
</g>
"""

# =============================================================================
# ESTRUCTURAS DE LAS VÍAS ANAPLERÓTICAS Y CATAPLERÓTICAS
# =============================================================================

# L-GLUTAMATO (Anaplerosis / Cataplerosis con α-Cetoglutarato)
# -OOC - CH(NH3+) - CH2 - CH2 - COO-
GLUTAMATO = """
<g class="mol-glutamato" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="40" y="14" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="40" y1="20" x2="40" y2="33" />

  <!-- C2: CH(NH3+) quiral con grupo amino -->
  <text x="40" y="44" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <line x1="48" y1="40" x2="58" y2="40" stroke="#2563eb" stroke-width="2"/>
  <text x="64" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" stroke="none">⁺NH₃</text>
  <line x1="32" y1="40" x2="24" y2="40" stroke="#0f172a" stroke-width="2"/>
  <text x="18" y="44" font-family="'Inter', sans-serif" font-size="10.5" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">H</text>

  <!-- Enlace C2 - C3 -->
  <line x1="40" y1="48" x2="40" y2="58" />

  <!-- C3: -CH2- -->
  <text x="40" y="69" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">H₂C</text>
  <line x1="40" y1="74" x2="40" y2="85" />

  <!-- C4: -CH2- -->
  <text x="40" y="96" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">H₂C</text>
  <line x1="40" y1="101" x2="40" y2="112" />

  <!-- C5 Carboxilato Inferior -->
  <text x="40" y="125" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
</g>
"""

# DELTA-AMINOLEVULINATO / ALA (Cataplerosis desde Succinil-CoA hacia Porfirinas y Grupo Hemo)
# -OOC - CH2 - CH2 - C(=O) - CH2 - NH3+
DELTA_AMINOLEVULINATO = """
<g class="mol-ala" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="40" y="14" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="40" y1="20" x2="40" y2="34" />

  <!-- C2: -CH2- -->
  <text x="40" y="44" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">H₂C</text>
  <line x1="40" y1="48" x2="40" y2="58" />

  <!-- C3: -CH2- -->
  <text x="40" y="68" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">H₂C</text>
  <line x1="40" y1="72" x2="40" y2="81" />

  <!-- C4: Carbonilo C=O -->
  <text x="40" y="92" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <line x1="48" y1="85" x2="62" y2="85" stroke="#dc2626" stroke-width="2"/>
  <line x1="48" y1="89" x2="62" y2="89" stroke="#dc2626" stroke-width="2"/>
  <text x="70" y="91" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#dc2626" stroke="none">O</text>

  <!-- Enlace C4 - C5 -->
  <line x1="40" y1="96" x2="40" y2="105" />

  <!-- C5: -CH2-NH3+ -->
  <text x="40" y="116" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">H₂C</text>
  <line x1="40" y1="120" x2="40" y2="128" stroke="#2563eb" stroke-width="2"/>
  <text x="40" y="139" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#2563eb" text-anchor="middle" stroke="none">⁺NH₃</text>
</g>
"""

# FOSFOENOLPIRUVATO / PEP (Cataplerosis desde Oxalacetato hacia Gluconeogénesis vía PEPCK)
# -OOC - C(=CH2) - O - PO3(2-)
FOSFOENOLPIRUVATO = """
<g class="mol-pep" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 Carboxilato Superior -->
  <text x="40" y="14" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#dc2626" text-anchor="middle" stroke="none">COO⁻</text>
  <line x1="40" y1="20" x2="40" y2="36" />

  <!-- C2: C(=CH2) con fosfato -->
  <text x="40" y="49" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  
  <!-- Doble enlace =CH2 hacia la izquierda -->
  <line x1="32" y1="43" x2="16" y2="43" stroke="#0f172a" stroke-width="2"/>
  <line x1="32" y1="47" x2="16" y2="47" stroke="#0f172a" stroke-width="2"/>
  <text x="8" y="49" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="end" stroke="none">H₂C</text>

  <!-- Enlace hacia éster fosfato -O-PO3(2-) a la derecha -->
  <line x1="48" y1="45" x2="62" y2="45" stroke="#f59e0b" stroke-width="2.2"/>
  <rect x="65" y="32" width="46" height="26" rx="6" fill="#fef3c7" stroke="#d97706" stroke-width="1.4"/>
  <text x="88" y="49" font-family="'JetBrains Mono', monospace" font-size="10" font-weight="900" fill="#b45309" text-anchor="middle" stroke="none">O-P</text>
</g>
"""

# PROPIONIL-COA (Anaplerosis hacia Succinil-CoA desde aminoácidos ramificados Val / Ile / Met)
# H3C - CH2 - C(=O) ~ S-CoA
PROPIONIL_COA = """
<g class="mol-propionil-coa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- Etilo H3C-CH2- -->
  <text x="12" y="38" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" stroke="none">H₃C</text>
  <line x1="32" y1="35" x2="44" y2="35" />
  <text x="56" y="38" font-family="'Inter', sans-serif" font-size="11" font-weight="700" fill="#64748b" text-anchor="middle" stroke="none">CH₂</text>
  <line x1="68" y1="35" x2="77" y2="35" />

  <!-- C(=O) explícito -->
  <text x="84" y="39" font-family="'Inter', sans-serif" font-size="11.5" font-weight="900" fill="#0f172a" text-anchor="middle" stroke="none">C</text>
  <line x1="82" y1="28" x2="82" y2="16" stroke="#dc2626" stroke-width="2"/>
  <line x1="86" y1="28" x2="86" y2="16" stroke="#dc2626" stroke-width="2"/>
  <text x="84" y="11" font-family="'Inter', sans-serif" font-size="12" font-weight="800" fill="#dc2626" text-anchor="middle" stroke="none">O</text>

  <!-- Enlace tioéster ~S-CoA -->
  <line x1="91" y1="35" x2="100" y2="35" stroke="#d97706" stroke-width="2.2"/>
  <text x="108" y="39" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#d97706" text-anchor="middle" stroke="none">S</text>
  <line x1="116" y1="35" x2="126" y2="35" stroke="#7c3aed" stroke-width="2"/>
  <rect x="128" y="24" width="34" height="22" rx="4" fill="#f3e8ff" stroke="#7c3aed" stroke-width="1.3"/>
  <text x="145" y="39" font-family="'Inter', sans-serif" font-size="10" font-weight="900" fill="#6b21a8" text-anchor="middle" stroke="none">CoA</text>
</g>
"""
