#!/usr/bin/env python3
"""
ESTRUCTURAS MOLECULARES ESPECÍFICAS DE LA GLUCONEOGÉNESIS
=========================================================
Fórmulas químicas vectoriales nítidas (Fischer / Haworth / Kekulé) para los intermediarios,
precursores gluconeogénicos y reguladores alostéricos.
Diseñadas bajo el estándar de Biología Estructural:
- Enlaces químicos negros nítidos (#0f172a)
- Oxígenos y carboxilatos en rojo (#dc2626)
- Hidroxilos en azul (#0284c7)
- Nitrógenos/aminas en azul violeta (#4338ca)
- Grupos fosfato en naranja/ámbar (#ea580c)
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

# 4. Cisterna del RE con bicapa, T1/T2/T3 y G6Pasa (cabeza catalítica en el lumen)
def _chip(cx, cy, w, txt, color, fondo):
    return (f'<rect x="{cx-w/2}" y="{cy-9}" width="{w}" height="18" rx="9" fill="{fondo}" stroke="{color}" stroke-width="1.6"/>'
            f'<text x="{cx}" y="{cy+3.8}" font-size="10.5" font-weight="900" fill="{color}" text-anchor="middle">{txt}</text>')

def _flecha(d, color, marker, ancho=2.2, extra=""):
    return f'<path d="{d}" fill="none" stroke="{color}" stroke-width="{ancho}" marker-end="url(#{marker})" {extra}/>'

def _bicapa(x0, x1, y0, y1):
    p = []
    p.append(f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="#f1f5f9"/>')
    y = y0 + 6
    while y < y1:
        for xh, xt in ((x0 + 1.5, x0 + 13), (x1 - 1.5, x1 - 13)):
            p.append(f'<line x1="{xh}" y1="{y}" x2="{xt}" y2="{y}" stroke="#94a3b8" stroke-width="1"/>')
            p.append(f'<circle cx="{xh}" cy="{y}" r="3.6" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>')
        y += 11
    return "\n".join(p)

def construir_re_g6pase():
    xm0, xm1 = 340, 374      # banda de la bicapa
    xc = (xm0 + xm1) / 2     # eje de proteínas (357)
    s = []
    s.append('<g class="organelo-re-g6pase" font-family="\'Inter\', sans-serif">')
    # --- Cisterna (lumen) ---
    s.append('<path d="M 340 6 C 160 -12 20 22 12 96 C 4 170 -2 236 46 274 C 110 312 240 306 340 296 Z" '
             'fill="#f5f3ff" stroke="#8b5cf6" stroke-width="2.2"/>')
    s.append('<text x="100" y="138" font-size="16" font-weight="900" fill="#7c3aed" opacity="0.55" text-anchor="middle" letter-spacing="2">LUMEN</text>')
    s.append('<text x="100" y="158" font-size="16" font-weight="900" fill="#7c3aed" opacity="0.55" text-anchor="middle" letter-spacing="2">DEL RE</text>')
    s.append('<text x="418" y="150" font-size="10" font-weight="900" fill="#94a3b8" letter-spacing="2">CITOSOL</text>')
    # --- Bicapa ---
    s.append(_bicapa(xm0, xm1, 4, 298))
    # --- Proteínas ---
    # T2 (Pi) y T3 (glucosa): exportan
    s.append(f'<rect x="{xc-24}" y="6" width="48" height="38" rx="9" fill="#0d9488" stroke="#0f766e" stroke-width="1.8"/>'
             f'<text x="{xc}" y="30" font-size="13" font-weight="900" fill="#fff" text-anchor="middle">T2</text>')
    s.append(f'<rect x="{xc-24}" y="56" width="48" height="44" rx="9" fill="#059669" stroke="#047857" stroke-width="1.8"/>'
             f'<text x="{xc}" y="83" font-size="13" font-weight="900" fill="#fff" text-anchor="middle">T3</text>')
    # G6Pasa: hélices transmembrana + cabeza catalítica en el lumen
    s.append(f'<rect x="{xm0-2}" y="128" width="{xm1-xm0+4}" height="56" rx="8" fill="#fde68a" stroke="#b45309" stroke-width="1.8"/>')
    s.append('<rect x="318" y="146" width="24" height="20" fill="#fde68a" stroke="#b45309" stroke-width="1.8"/>')
    s.append('<circle cx="290" cy="156" r="34" fill="#fef3c7" stroke="#b45309" stroke-width="2.4"/>')
    s.append('<path d="M 268 132 A 12 12 0 0 1 292 128" fill="none" stroke="#b45309" stroke-width="1.6" stroke-dasharray="3 2"/>')
    s.append('<text x="290" y="161" font-size="11.5" font-weight="900" fill="#92400e" text-anchor="middle">G6Pasa</text>')
    # T1: importa G6P
    s.append(f'<rect x="{xc-24}" y="242" width="48" height="50" rx="9" fill="#0284c7" stroke="#0369a1" stroke-width="1.8"/>'
             f'<text x="{xc}" y="272" font-size="13" font-weight="900" fill="#fff" text-anchor="middle">T1</text>')
    # --- Flujo dentro del lumen ---
    s.append(_chip(275, 267, 50, "G6P", "#7c3aed", "#ede9fe"))
    s.append(_flecha("M 331 267 L 302 267", "#7c3aed", "arrowPurple", 2.4))
    s.append(_flecha("M 278 257 L 286 194", "#7c3aed", "arrowPurple", 2.4))
    s.append(_chip(206, 202, 42, "H₂O", "#0284c7", "#e0f2fe"))
    s.append(_flecha("M 228 197 L 262 180", "#0284c7", "arrowBlue", 2))
    # productos
    s.append(_flecha("M 290 121 L 290 90", "#ea580c", "arrowFlow", 2.4))
    s.append(_chip(290, 78, 40, "Glc", "#ea580c", "#ffedd5"))
    s.append(_flecha("M 311 78 L 331 78", "#ea580c", "arrowFlow", 2.4))
    s.append(_flecha("M 262 134 C 210 112 214 38 268 26", "#475569", "arrowSlate", 2))
    s.append(_chip(290, 25, 40, "Pi", "#b45309", "#fef3c7"))
    s.append(_flecha("M 311 25 L 331 25", "#475569", "arrowSlate", 2))
    # --- Cabecera ---
    s.append('<text x="0" y="-26" font-size="11" font-weight="900" fill="#6d28d9">Glucosa-6-fosfatasa · EC 3.1.3.9</text>')
    # --- Inset: qué se salta ---
    ty = 336
    s.append(f'<rect x="0" y="{ty}" width="150" height="20" rx="10" fill="#fee2e2" stroke="#dc2626" stroke-width="1.6"/>'
             f'<text x="75" y="{ty+14}" font-size="10.5" font-weight="900" fill="#b91c1c" text-anchor="middle">SE SALTA HK / GK</text>')
    ya = ty + 40
    s.append(_chip(20, ya, 40, "Glc", "#64748b", "#f1f5f9"))
    s.append(_flecha(f"M 42 {ya} L 112 {ya}", "#94a3b8", "arrowSlate", 2, 'stroke-dasharray="5 3"'))
    s.append(f'<text x="80" y="{ya-13}" font-size="9.5" font-weight="800" fill="#64748b" text-anchor="middle">HK/GK</text>')
    s.append(f'<text x="80" y="{ya+21}" font-size="9.5" font-weight="800" fill="#64748b" text-anchor="middle">+ ATP</text>')
    s.append(f'<path d="M 75 {ya-6} L 85 {ya+6} M 85 {ya-6} L 75 {ya+6}" stroke="#dc2626" stroke-width="3" stroke-linecap="round"/>')
    s.append(_chip(142, ya, 50, "G6P", "#64748b", "#f1f5f9"))
    s.append(f'<text x="176" y="{ya+4}" font-size="9.5" font-weight="800" fill="#94a3b8">glucólisis</text>')
    yb = ya + 50
    s.append(_chip(24, yb, 50, "G6P", "#7c3aed", "#ede9fe"))
    s.append(_flecha(f"M 52 {yb} L 110 {yb}", "#7c3aed", "arrowPurple", 2.6))
    s.append(f'<text x="83" y="{yb-12}" font-size="9.5" font-weight="900" fill="#7c3aed" text-anchor="middle">G6Pasa</text>')
    s.append(f'<text x="83" y="{yb+21}" font-size="9.5" font-weight="800" fill="#0284c7" text-anchor="middle">+ H₂O → Pi</text>')
    s.append(_chip(138, yb, 40, "Glc", "#ea580c", "#ffedd5"))
    s.append(f'<text x="170" y="{yb+4}" font-size="9.5" font-weight="900" fill="#7c3aed">gluconeogénesis</text>')
    # tejido
    yt = yb + 40
    s.append(f'<rect x="0" y="{yt}" width="188" height="20" rx="10" fill="#fef3c7" stroke="#b45309" stroke-width="1.6"/>'
             f'<text x="94" y="{yt+14}" font-size="10" font-weight="900" fill="#92400e" text-anchor="middle">Solo hígado + riñón (no músculo)</text>')
    s.append('</g>')
    return "\n".join(s)

RE_GLUCOSA_6_FOSFATASA = construir_re_g6pase()

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

# 6. Glicerol-3-Fosfato (G-3-P) - Intermediario fosforilado del glicerol
# CH2OH - CH(OH) - CH2-O-PO3(2-)
GLICEROL_3_FOSFATO = """
<g class="molecula-glicerol-3-fosfato">
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
  <line x1="50" y1="55" x2="50" y2="70" stroke="#0f172a" stroke-width="2.2" />

  <!-- C3: CH2-O-P fosforilado -->
  <text x="50" y="80" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0f172a" text-anchor="middle">CH₂-O</text>
  <line x1="50" y1="84" x2="50" y2="94" stroke="#0f172a" stroke-width="2" />
  <circle cx="50" cy="106" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2" />
  <text x="50" y="110" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
</g>
"""

# 7. Fructosa-2,6-Bisfosfato (F-2,6-BP) - Regulador alostérico clave
# Anillo furanósido con fosfatos en C2 y C6
FRUCTOSA_2_6_BISFOSFATO = """
<g class="molecula-fructosa-2-6-bisfosfato">
  <!-- Anillo de furanosa (pentágono) -->
  <polygon points="35,18 68,38 52,68 18,68 2,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>

  <!-- Oxígeno en el vértice superior del pentágono -->
  <circle cx="35" cy="18" r="7" fill="#ffffff"/>
  <text x="35" y="22" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>

  <!-- C2 (a la derecha): C1 (-CH2OH) y Fosfato en C2 (2-P) -->
  <line x1="68" y1="38" x2="88" y2="24" stroke="#0f172a" stroke-width="2.2"/>
  <text x="94" y="22" fill="#0f172a" font-size="9.5" font-weight="800">CH₂OH</text>
  
  <line x1="68" y1="38" x2="88" y2="52" stroke="#ea580c" stroke-width="2.2"/>
  <circle cx="100" cy="58" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="100" y="62" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ₂</text>

  <!-- C6 (a la izquierda): Fosfato en C6 (6-P) -->
  <line x1="2" y1="38" x2="-10" y2="18" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="-16" cy="6" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="-16" y="10" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ₆</text>

  <!-- C3 y C4 con -OH abajo -->
  <line x1="52" y1="68" x2="52" y2="82" stroke="#0f172a" stroke-width="2"/>
  <text x="52" y="92" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">OH</text>

  <line x1="18" y1="68" x2="18" y2="82" stroke="#0f172a" stroke-width="2"/>
  <text x="18" y="92" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">HO</text>
</g>
"""
