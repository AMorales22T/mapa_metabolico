# =============================================================================
# MÓDULO DE REVISIÓN: Estructuras Químicas de Glicerolípidos y Fosfolípidos
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/estructuras_ampliacion.py (líneas 1 a 243 de 611)
# Descripción      : Glicerol, G3P, LPA, PA, DAG, 2-MAG, TAG, fosfatidilcolina y cuerpos cetónicos.
# =============================================================================

#!/usr/bin/env python3
"""
ESTRUCTURAS QUÍMICAS Y ESQUEMAS ANATÓMICOS VECTORIALES (SVG)
=============================================================
Manual de Estilo Editorial Científico del Mapa Metabólico:
- Trazos oscuros grafito (#0f172a, stroke-width: 2.2px)
- Oxígenos (C=O, OH, carboxilatos) en rojo carmesí (#dc2626)
- Grupos fosfato en cápsula naranja (#ffedd5 fondo, #ea580c borde y texto 'P')
- Grupos amino e iones de nitrógeno en azul cobalto (#2563eb / #1d4ed8)
- Enlaces y cadenas alifáticas nítidas sin cajas blancas ni emojis
- Tipografía estricta: 'Inter' para texto y 'JetBrains Mono' para fórmulas y números EC
"""

# =============================================================================
# 1. METABOLISMO DE LÍPIDOS: ESQUELETO DE GLICEROL, ACIL-COA Y ÉSTERES
# =============================================================================

# Triacilglicerol (TAG) con esqueleto de glicerol completo y 3 cadenas de acilos
TRIACILGLICEROL = """
<g class="mol-tag" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 (superior) -->
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="12" x2="88" y2="12" />
  <line x1="88" y1="12" x2="98" y2="4" />
  <line x1="88" y1="12" x2="98" y2="20" stroke="#dc2626" stroke-width="2.2" />
  <line x1="86" y1="15" x2="96" y2="23" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <!-- Cadena R1 (zig-zag saturado) -->
  <path d="M 98 4 L 110 12 L 122 4 L 134 12 L 146 4 L 158 12 L 170 4" stroke="#ea580c" stroke-width="2.2"/>
  <text x="178" y="8" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₁</text>

  <!-- Enlace vertical C1-C2 -->
  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2 (central) -->
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="42" x2="88" y2="42" />
  <line x1="88" y1="42" x2="98" y2="34" />
  <line x1="88" y1="42" x2="98" y2="50" stroke="#dc2626" stroke-width="2.2" />
  <line x1="86" y1="45" x2="96" y2="53" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="54" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <!-- Cadena R2 (con insaturación) -->
  <path d="M 98 34 L 110 42 L 122 34 L 132 44 L 145 38 L 158 48 L 170 42" stroke="#ea580c" stroke-width="2.2"/>
  <text x="178" y="46" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₂</text>

  <!-- Enlace vertical C2-C3 -->
  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C3 (inferior) -->
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="72" x2="88" y2="72" />
  <line x1="88" y1="72" x2="98" y2="64" />
  <line x1="88" y1="72" x2="98" y2="80" stroke="#dc2626" stroke-width="2.2" />
  <line x1="86" y1="75" x2="96" y2="83" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="84" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <!-- Cadena R3 -->
  <path d="M 98 64 L 110 72 L 122 64 L 134 72 L 146 64 L 158 72 L 170 64" stroke="#ea580c" stroke-width="2.2"/>
  <text x="178" y="68" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₃</text>
</g>
"""

# 2-Monoacilglicerol (2-MAG)
MONOACILGLICEROL_2 = """
<g class="mol-2mag" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <!-- C1 libre (-OH) -->
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>

  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C2 esterificado (-O-CO-R2) -->
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="42" x2="88" y2="42" />
  <line x1="88" y1="42" x2="98" y2="34" />
  <line x1="88" y1="42" x2="98" y2="50" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="54" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 34 L 110 42 L 122 34 L 134 42 L 146 34 L 158 42 L 170 34" stroke="#ea580c" stroke-width="2.2"/>
  <text x="178" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₂</text>

  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>

  <!-- C3 libre (-OH) -->
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>
</g>
"""

# Glicerol libre
GLICEROL_ESTRUCTURA = """
<g class="mol-glicerol-libre" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>
  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>
  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>
</g>
"""

# Lisofosfatidato (LPA / 1-Acil-glicerol-3-P)
LISOFOSFATIDATO = """
<g class="mol-lpa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="12" x2="88" y2="12" />
  <line x1="88" y1="12" x2="98" y2="4" />
  <line x1="88" y1="12" x2="98" y2="20" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 4 L 110 12 L 122 4 L 134 12 L 146 4" stroke="#ea580c" stroke-width="2.2"/>
  <text x="154" y="8" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₁</text>

  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>

  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="72" x2="84" y2="72" />
  <circle cx="98" cy="72" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
  <text x="98" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
</g>
"""

# Ácido Fosfatídico (PA)
ACIDO_FOSFATIDICO = """
<g class="mol-pa" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="12" x2="88" y2="12" />
  <line x1="88" y1="12" x2="98" y2="4" />
  <line x1="88" y1="12" x2="98" y2="20" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 4 L 110 12 L 122 4 L 134 12 L 146 4" stroke="#ea580c" stroke-width="2.2"/>
  <text x="154" y="8" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₁</text>

  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="42" x2="88" y2="42" />
  <line x1="88" y1="42" x2="98" y2="34" />
  <line x1="88" y1="42" x2="98" y2="50" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="54" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 34 L 110 42 L 122 34 L 134 42 L 146 34" stroke="#ea580c" stroke-width="2.2"/>
  <text x="154" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₂</text>

  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="72" x2="84" y2="72" />
  <circle cx="98" cy="72" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
  <text x="98" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
</g>
"""

# 1,2-Diacilglicerol (DAG)
DIACILGLICEROL = """
<g class="mol-dag" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="12" x2="88" y2="12" />
  <line x1="88" y1="12" x2="98" y2="4" />
  <line x1="88" y1="12" x2="98" y2="20" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 4 L 110 12 L 122 4 L 134 12 L 146 4" stroke="#ea580c" stroke-width="2.2"/>
  <text x="154" y="8" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₁</text>

  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="42" x2="88" y2="42" />
  <line x1="88" y1="42" x2="98" y2="34" />
  <line x1="88" y1="42" x2="98" y2="50" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="54" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 34 L 110 42 L 122 34 L 134 42 L 146 34" stroke="#ea580c" stroke-width="2.2"/>
  <text x="154" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₂</text>

  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">OH</text>
</g>
"""

# Fosfatidilcolina (PC)
FOSFATIDILCOLINA = """
<g class="mol-pc" stroke="#0f172a" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="32" y="16" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="12" x2="52" y2="12" />
  <text x="60" y="16" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="12" x2="88" y2="12" />
  <line x1="88" y1="12" x2="98" y2="4" />
  <line x1="88" y1="12" x2="98" y2="20" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="24" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 4 L 110 12 L 122 4 L 134 12" stroke="#ea580c" stroke-width="2.2"/>
  <text x="142" y="8" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₁</text>

  <line x1="26" y1="20" x2="26" y2="38" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="46" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">HC</text>
  <line x1="36" y1="42" x2="52" y2="42" />
  <text x="60" y="46" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="42" x2="88" y2="42" />
  <line x1="88" y1="42" x2="98" y2="34" />
  <line x1="88" y1="42" x2="98" y2="50" stroke="#dc2626" stroke-width="2.2" />
  <text x="104" y="54" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#dc2626" stroke="none">O</text>
  <path d="M 98 34 L 110 42 L 122 34 L 134 42" stroke="#ea580c" stroke-width="2.2"/>
  <text x="142" y="38" font-family="'Inter', sans-serif" font-size="10.5" font-weight="800" fill="#ea580c" stroke="none">R₂</text>

  <line x1="26" y1="50" x2="26" y2="68" stroke="#0f172a" stroke-width="2.2"/>
  <text x="32" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#2563eb" stroke="none" text-anchor="end">H₂C</text>
  <line x1="36" y1="72" x2="52" y2="72" />
  <text x="60" y="76" font-family="'Inter', sans-serif" font-size="12" font-weight="900" fill="#dc2626" stroke="none">O</text>
  <line x1="72" y1="72" x2="84" y2="72" />
  <circle cx="98" cy="72" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="1.8"/>
  <text x="98" y="76" font-family="'Inter', sans-serif" font-size="11" font-weight="900" fill="#c2410c" stroke="none" text-anchor="middle">Ⓟ</text>
  <line x1="98" y1="85" x2="98" y2="98" stroke="#0f172a" stroke-width="2"/>
  <text x="98" y="112" font-family="'Inter', sans-serif" font-size="10" font-weight="800" fill="#2563eb" stroke="none" text-anchor="middle">O–CH₂CH₂–N⁺(CH₃)₃</text>
</g>
"""

