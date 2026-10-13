#!/usr/bin/env python3
"""Genera el ciclo de Cori con la gramática visual del mapa de gluconeogénesis.

Músculo (izquierda) y hepatocito (derecha) en espejo, con la sangre en el centro:
  * Glucosa: hígado -> sangre (GLUT2) -> músculo (GLUT4)
  * Lactato: músculo -> sangre (MCT4) -> hígado (MCT1)
  * Mismos intermediarios (estructuras reales) recorridos hacia abajo (glucólisis) y hacia arriba (gluconeogénesis)
  * Pasos irreversibles del músculo (HK, PFK-1, PK) frente a los 3 bypasses del hígado
  * RE del hepatocito (T1 / G6Pasa / T2 / T3); el músculo no tiene G6Pasa
Autocontenido: no depende de otros módulos.
"""
from pathlib import Path

OUT = Path(__file__).parent
W, H = 1700, 1840

# Estructuras químicas (mismas que el mapa de gluconeogénesis). Origen local (0,0).
ESTR = {
    'GLC': '<!-- Anillo de 6 lados -->\n  <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>\n\n  <!-- Oxígeno del anillo -->\n  <circle cx="16" cy="22" r="7" fill="#ffffff"/>\n  <text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>\n\n  <!-- Carbono 6: -CH2OH arriba -->\n  <line x1="0" y1="36" x2="0" y2="12" stroke="#0f172a" stroke-width="2.2"/>\n  <text x="0" y="7" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">CH₂OH</text>\n\n  <!-- Grupos hidroxilo (-OH) -->\n  <!-- C1 (derecha) -->\n  <line x1="72" y1="36" x2="88" y2="36" stroke="#0f172a" stroke-width="2"/>\n  <text x="98" y="40" fill="#0f172a" font-size="11" font-weight="700">OH</text>\n\n  <!-- C2 (abajo derecha) -->\n  <line x1="50" y1="58" x2="50" y2="72" stroke="#0f172a" stroke-width="2"/>\n  <text x="50" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">OH</text>\n\n  <!-- C3 (abajo izquierda) -->\n  <line x1="16" y1="58" x2="16" y2="72" stroke="#0f172a" stroke-width="2"/>\n  <text x="16" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">HO</text>\n\n  <!-- C4 (izquierda) -->\n  <line x1="0" y1="36" x2="-14" y2="36" stroke="#0f172a" stroke-width="2"/>\n  <text x="-24" y="40" fill="#0f172a" font-size="11" font-weight="700">HO</text>',
    'G6P': '<!-- Anillo de 6 lados -->\n  <polygon points="50,22 72,36 50,58 16,58 0,36 16,22" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>\n\n  <!-- Oxígeno del anillo -->\n  <circle cx="16" cy="22" r="7" fill="#ffffff"/>\n  <text x="16" y="26" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>\n\n  <!-- Carbono 6 con Grupo Fosfato nítido y despejado -->\n  <line x1="0" y1="36" x2="0" y2="12" stroke="#0f172a" stroke-width="2.2"/>\n  <circle cx="0" cy="-2" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>\n  <text x="0" y="3" fill="#c2410c" font-size="12" font-weight="900" text-anchor="middle">Ⓟ</text>\n  <text x="-20" y="2" fill="#ea580c" font-size="9" font-weight="700" text-anchor="end">O-PO₃²⁻</text>\n\n  <!-- Grupos hidroxilo (-OH) -->\n  <line x1="72" y1="36" x2="88" y2="36" stroke="#0f172a" stroke-width="2"/>\n  <text x="98" y="40" fill="#0f172a" font-size="11" font-weight="700">OH</text>\n\n  <line x1="50" y1="58" x2="50" y2="72" stroke="#0f172a" stroke-width="2"/>\n  <text x="50" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">OH</text>\n\n  <line x1="16" y1="58" x2="16" y2="72" stroke="#0f172a" stroke-width="2"/>\n  <text x="16" y="83" fill="#0f172a" font-size="11" font-weight="700" text-anchor="middle">HO</text>\n\n  <line x1="0" y1="36" x2="-14" y2="36" stroke="#0f172a" stroke-width="2"/>\n  <text x="-24" y="40" fill="#0f172a" font-size="11" font-weight="700">HO</text>',
    'F6P': '<!-- Anillo de furanosa (pentágono) -->\n  <polygon points="35,18 68,38 52,68 18,68 2,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>\n\n  <!-- Oxígeno en el vértice superior del pentágono -->\n  <circle cx="35" cy="18" r="7" fill="#ffffff"/>\n  <text x="35" y="22" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>\n\n  <!-- C1 (a la derecha): -CH2OH libre -->\n  <line x1="68" y1="38" x2="88" y2="24" stroke="#0f172a" stroke-width="2.2"/>\n  <text x="94" y="22" fill="#0f172a" font-size="10" font-weight="800">CH₂OH</text>\n  <line x1="68" y1="38" x2="82" y2="50" stroke="#0f172a" stroke-width="2"/>\n  <text x="88" y="55" fill="#0f172a" font-size="10" font-weight="700">OH</text>\n\n  <!-- C6 (a la izquierda): Grupo Fosfato -->\n  <line x1="2" y1="38" x2="-10" y2="18" stroke="#0f172a" stroke-width="2.2"/>\n  <circle cx="-16" cy="6" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>\n  <text x="-16" y="11" fill="#c2410c" font-size="12" font-weight="900" text-anchor="middle">Ⓟ</text>\n  <text x="-35" y="10" fill="#ea580c" font-size="9" font-weight="700" text-anchor="end">O-PO₃²⁻</text>\n\n  <!-- C3 y C4 con -OH abajo -->\n  <line x1="52" y1="68" x2="52" y2="82" stroke="#0f172a" stroke-width="2"/>\n  <text x="52" y="92" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">OH</text>\n\n  <line x1="18" y1="68" x2="18" y2="82" stroke="#0f172a" stroke-width="2"/>\n  <text x="18" y="92" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">HO</text>',
    'FBP': '<!-- Anillo de furanosa (pentágono) -->\n  <polygon points="35,18 68,38 52,68 18,68 2,38" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>\n\n  <!-- Oxígeno superior -->\n  <circle cx="35" cy="18" r="7" fill="#ffffff"/>\n  <text x="35" y="22" fill="#dc2626" font-size="14" font-weight="800" text-anchor="middle">O</text>\n\n  <!-- C1 (a la derecha): Fosfato en C1 -->\n  <line x1="68" y1="38" x2="88" y2="24" stroke="#0f172a" stroke-width="2.2"/>\n  <circle cx="98" cy="14" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>\n  <text x="98" y="19" fill="#c2410c" font-size="12" font-weight="900" text-anchor="middle">Ⓟ</text>\n\n  <!-- C6 (a la izquierda): Fosfato en C6 -->\n  <line x1="2" y1="38" x2="-10" y2="18" stroke="#0f172a" stroke-width="2.2"/>\n  <circle cx="-16" cy="6" r="14" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>\n  <text x="-16" y="11" fill="#c2410c" font-size="12" font-weight="900" text-anchor="middle">Ⓟ</text>\n\n  <!-- C3 y C4 con -OH -->\n  <line x1="52" y1="68" x2="52" y2="82" stroke="#0f172a" stroke-width="2"/>\n  <text x="52" y="92" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">OH</text>\n\n  <line x1="18" y1="68" x2="18" y2="82" stroke="#0f172a" stroke-width="2"/>\n  <text x="18" y="92" fill="#0f172a" font-size="10" font-weight="700" text-anchor="middle">HO</text>',
    'PEP': '<!-- C1: Carboxilato COO- -->\n  <text x="35" y="16" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">COO⁻</text>\n  <line x1="35" y1="22" x2="35" y2="40" stroke="#0f172a" stroke-width="2.2"/>\n\n  <!-- C2: C-O-P con doble enlace hacia el C3 -->\n  <text x="35" y="50" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">C</text>\n  <!-- Fosfato lateral -->\n  <line x1="42" y1="46" x2="62" y2="46" stroke="#0f172a" stroke-width="2"/>\n  <circle cx="75" cy="46" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>\n  <text x="75" y="50" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>\n\n  <!-- Doble enlace C=CH2 hacia abajo -->\n  <line x1="31" y1="56" x2="31" y2="74" stroke="#0f172a" stroke-width="2.2"/>\n  <line x1="39" y1="56" x2="39" y2="74" stroke="#0f172a" stroke-width="2.2"/>\n  <text x="35" y="88" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">CH₂</text>',
    'OAA': '<g class="molecula-oxalacetato">\n  <!-- C1: Carboxilato Superior -->\n  <text x="50" y="18" font-family="\'Inter\', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>\n  <line x1="50" y1="24" x2="50" y2="38" stroke="#0f172a" stroke-width="2.2" />\n\n  <!-- C2: Carbonilo (C=O) -->\n  <text x="50" y="50" font-family="\'Inter\', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">C</text>\n  <line x1="58" y1="45" x2="74" y2="45" stroke="#dc2626" stroke-width="2.2" />\n  <line x1="58" y1="49" x2="74" y2="49" stroke="#dc2626" stroke-width="2.2" />\n  <text x="82" y="51" font-family="\'Inter\', sans-serif" font-size="13" font-weight="800" fill="#dc2626">O</text>\n\n  <!-- Enlace C2 - C3 -->\n  <line x1="50" y1="55" x2="50" y2="70" stroke="#0f172a" stroke-width="2.2" />\n\n  <!-- C3: Metileno (-CH2-) -->\n  <text x="50" y="82" font-family="\'Inter\', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">CH₂</text>\n\n  <!-- Enlace C3 - C4 -->\n  <line x1="50" y1="87" x2="50" y2="102" stroke="#0f172a" stroke-width="2.2" />\n\n  <!-- C4: Carboxilato Inferior -->\n  <text x="50" y="116" font-family="\'Inter\', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>\n</g>',
    'PYR': '<!-- C1: Carboxilato COO- -->\n  <text x="40" y="16" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">COO⁻</text>\n  <line x1="40" y1="22" x2="40" y2="40" stroke="#0f172a" stroke-width="2.2"/>\n\n  <!-- C2: C=O (Grupo carbonilo) -->\n  <text x="40" y="50" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">C</text>\n  <line x1="47" y1="44" x2="66" y2="44" stroke="#0f172a" stroke-width="2"/>\n  <line x1="47" y1="48" x2="66" y2="48" stroke="#0f172a" stroke-width="2"/>\n  <text x="74" y="50" fill="#dc2626" font-size="13" font-weight="800">O</text>\n\n  <!-- C3: Grupo metilo CH3 -->\n  <line x1="40" y1="55" x2="40" y2="74" stroke="#0f172a" stroke-width="2.2"/>\n  <text x="40" y="86" fill="#0f172a" font-size="12" font-weight="800" text-anchor="middle">CH₃</text>',
    'LAC': '\n<g class="molecula-lactato">\n  <!-- C1: Carboxilato Superior -->\n  <text x="50" y="18" font-family="\'Inter\', sans-serif" font-size="13" font-weight="800" fill="#dc2626" text-anchor="middle">COO⁻</text>\n  <line x1="50" y1="24" x2="50" y2="38" stroke="#0f172a" stroke-width="2.2" />\n\n  <!-- C2: Carbono quiral H-C-OH -->\n  <line x1="42" y1="46" x2="31" y2="46" stroke="#0f172a" stroke-width="2" />\n  <text x="24" y="50" font-family="\'Inter\', sans-serif" font-size="12" font-weight="700" fill="#64748b" text-anchor="end">H</text>\n  <text x="50" y="50" font-family="\'Inter\', sans-serif" font-size="12" font-weight="900" fill="#0f172a" text-anchor="middle">C</text>\n  <line x1="58" y1="46" x2="69" y2="46" stroke="#0284c7" stroke-width="2" />\n  <text x="75" y="50" font-family="\'Inter\', sans-serif" font-size="12.5" font-weight="800" fill="#0284c7">OH</text>\n\n  <!-- Enlace C2 - C3 -->\n  <line x1="50" y1="55" x2="50" y2="72" stroke="#0f172a" stroke-width="2.2" />\n\n  <!-- C3: Grupo Metilo -->\n  <text x="50" y="86" font-family="\'Inter\', sans-serif" font-size="12" font-weight="800" fill="#0f172a" text-anchor="middle">CH₃</text>\n</g>\n',
}

# Ejes verticales de flechas y posición (y) de cada intermediario, iguales en ambas células
AX_M, AX_H = 410, 1285          # eje músculo / eje hígado
Y = dict(GLC=230, G6P=540, F6P=710, FBP=880, PEP=1060, OAA=1220, PYR=1400, LAC=1560)
HAWORTH = {"GLC", "G6P", "F6P", "FBP"}
NOMBRE = dict(GLC="D-Glucosa", G6P="Glucosa-6-fosfato", F6P="Fructosa-6-fosfato", FBP="Fructosa-1,6-bisfosfato",
              PEP="Fosfoenolpiruvato", OAA="Oxalacetato", PYR="Piruvato", LAC="L-Lactato")
CARB = dict(GLC="6 C", G6P="6 C", F6P="6 C", FBP="6 C", PEP="3 C", OAA="4 C", PYR="3 C", LAC="3 C")

def estructura(clave, ax, lado):
    """Dibuja una estructura centrada en su eje 'ax'. lado='izq' -> texto a la izquierda; 'der' -> a la derecha."""
    ox = ax - (36 if clave in HAWORTH else 50)
    y0 = Y[clave]
    return f'<g transform="translate({ox} {y0})">{ESTR[clave]}</g>'

def texto_nombre(clave, lado, detalle):
    y0 = Y[clave] + (10 if clave == "OAA" else 0)
    if lado == "izq":
        x, anc = 292, "end"
    else:
        x, anc = 1392, "start"
    return (f'<text x="{x}" y="{y0+24}" text-anchor="{anc}" class="name">{NOMBRE[clave]}</text>'
            f'<text x="{x}" y="{y0+43}" text-anchor="{anc}" class="carbon">{CARB[clave]}</text>'
            f'<text x="{x}" y="{y0+60}" text-anchor="{anc}" class="detail">{detalle}</text>')

def pill(cx, cy, txt, color, bg, w=None):
    w = w or (len(txt) * 6.6 + 18)
    return (f'<rect x="{cx-w/2:.1f}" y="{cy-9}" width="{w:.1f}" height="18" rx="9" fill="{bg}" stroke="{color}" stroke-width="1.5"/>'
            f'<text x="{cx}" y="{cy+4}" text-anchor="middle" class="chip" fill="{color}">{txt}</text>')

def fila_chips(x, y, chips, lado):
    """Fila de pills. lado='izq': se alinean hacia la izquierda desde x. 'der': hacia la derecha."""
    s, cur = [], x
    for txt, col, bg in chips:
        w = len(txt) * 6.6 + 18
        cx = cur - w/2 if lado == "izq" else cur + w/2
        s.append(pill(cx, y, txt, col, bg, w))
        cur = cur - w - 6 if lado == "izq" else cur + w + 6
    return "".join(s)

def etiqueta(lado, yc, tag, tagcol, tagbg, enzima, chips):
    x = 395 if lado == "izq" else 1303
    anc = "end" if lado == "izq" else "start"
    out = []
    wt = len(tag) * 6.6 + 18
    out.append(pill(x - wt/2 if lado == "izq" else x + wt/2, yc - 22, tag, tagcol, tagbg, wt))
    out.append(f'<text x="{x}" y="{yc-1}" text-anchor="{anc}" class="enzyme">{enzima}</text>')
    out.append(fila_chips(x, yc + 18, chips, lado))
    return "".join(out)

def flecha(ax, y1, y2, col, marker, ancho=3.4):
    return f'<line x1="{ax}" y1="{y1}" x2="{ax}" y2="{y2}" stroke="{col}" stroke-width="{ancho}" marker-end="url(#{marker})"/>'

def reversible(ax, y1, y2):
    return (f'<line x1="{ax-4}" y1="{y1}" x2="{ax-4}" y2="{y2}" stroke="#059669" stroke-width="2.4" marker-end="url(#aGreen)"/>'
            f'<line x1="{ax+4}" y1="{y2}" x2="{ax+4}" y2="{y1}" stroke="#059669" stroke-width="2.4" marker-end="url(#aGreen)"/>')

def bicapa(x0, x1, y0, y1):
    p = [f'<rect x="{x0}" y="{y0}" width="{x1-x0}" height="{y1-y0}" fill="#f1f5f9"/>']
    y = y0 + 6
    while y < y1:
        for xh, xt in ((x0 + 1.5, x0 + 7), (x1 - 1.5, x1 - 7)):
            p.append(f'<line x1="{xh}" y1="{y}" x2="{xt}" y2="{y}" stroke="#94a3b8" stroke-width="1"/>')
            p.append(f'<circle cx="{xh}" cy="{y}" r="2.8" fill="#cbd5e1" stroke="#94a3b8" stroke-width="1"/>')
        y += 10
    return "\n".join(p)

def transportador(cx, cy, txt, col, borde, w=54):
    return (f'<rect x="{cx-w/2}" y="{cy-15}" width="{w}" height="30" rx="8" fill="{col}" stroke="{borde}" stroke-width="2"/>'
            f'<text x="{cx}" y="{cy+4}" text-anchor="middle" class="tr">{txt}</text>')

def chip_re(cx, cy, w, txt, col, bg):
    return pill(cx, cy, txt, col, bg, w)

def mini_re():
    """RE del hepatocito: bicapa vertical + T1/G6Pasa/T2/T3 + flujo en el lumen."""
    s = []
    s.append('<path d="M 1432 332 C 1560 308 1656 340 1656 430 C 1656 512 1560 534 1432 524 Z" fill="#f5f3ff" stroke="#8b5cf6" stroke-width="2"/>')
    s.append('<text x="1590" y="505" text-anchor="middle" class="lumen">LUMEN DEL RE</text>')
    s.append(bicapa(1410, 1432, 330, 526))
    # T3 (glucosa), T2 (Pi), G6Pasa, T1 (G6P)
    s.append(transportador(1421, 352, "T3", "#059669", "#047857", 48))
    s.append(transportador(1421, 390, "T2", "#0d9488", "#0f766e", 48))
    s.append('<rect x="1406" y="418" width="30" height="42" rx="6" fill="#fde68a" stroke="#b45309" stroke-width="1.8"/>')
    s.append('<rect x="1434" y="436" width="14" height="16" fill="#fde68a" stroke="#b45309" stroke-width="1.8"/>')
    s.append('<circle cx="1478" cy="444" r="28" fill="#fef3c7" stroke="#b45309" stroke-width="2.2"/>')
    s.append('<text x="1478" y="448" text-anchor="middle" class="g6p">G6Pasa</text>')
    s.append(transportador(1421, 496, "T1", "#0284c7", "#0369a1", 48))
    # flujo en el lumen
    s.append(chip_re(1500, 497, 40, "G6P", "#7c3aed", "#ede9fe"))
    s.append('<line x1="1447" y1="497" x2="1478" y2="497" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#aPurple)"/>')
    s.append('<line x1="1500" y1="488" x2="1490" y2="474" stroke="#7c3aed" stroke-width="2.2" marker-end="url(#aPurple)"/>')
    s.append(chip_re(1600, 444, 44, "H₂O", "#0284c7", "#e0f2fe"))
    s.append('<line x1="1577" y1="444" x2="1509" y2="444" stroke="#0284c7" stroke-width="2" marker-end="url(#aBlue)"/>')
    s.append(chip_re(1520, 392, 34, "Pi", "#b45309", "#fef3c7"))
    s.append('<line x1="1503" y1="392" x2="1448" y2="391" stroke="#475569" stroke-width="2" marker-end="url(#aSlate)"/>')
    s.append('<line x1="1486" y1="416" x2="1510" y2="400" stroke="#475569" stroke-width="2" marker-end="url(#aSlate)"/>')
    s.append(chip_re(1520, 352, 40, "Glc", "#ea580c", "#ffedd5"))
    s.append('<path d="M 1506 417 C 1570 400 1590 360 1543 353" fill="none" stroke="#ea580c" stroke-width="2.2" marker-end="url(#aOrange)"/>')
    s.append('<line x1="1500" y1="352" x2="1448" y2="352" stroke="#ea580c" stroke-width="2.2" marker-end="url(#aOrange)"/>')
    # salida/entrada al citosol
    s.append('<line x1="1396" y1="352" x2="1352" y2="308" stroke="#ea580c" stroke-width="2.8" marker-end="url(#aOrange)"/>')
    s.append(pill(1364, 392, "Pi", "#b45309", "#fef3c7", 30))
    s.append('<line x1="1396" y1="390" x2="1382" y2="391" stroke="#475569" stroke-width="2" marker-end="url(#aSlate)"/>')
    s.append('<line x1="1338" y1="560" x2="1398" y2="510" stroke="#7c3aed" stroke-width="2.8" marker-end="url(#aPurple)"/>')
    # etiqueta bypass
    s.append(pill(1440, 316, "BYPASS 3 · RE", "#6d28d9", "#ede9fe", 104))
    return "\n".join(s)

# ---------------------------------------------------------------------------
partes = []
A = partes.append

A(f'<rect width="{W}" height="{H}" fill="#f8fafc"/>')
A('<text x="70" y="52" class="title">CICLO DE CORI</text>')
A('<text x="70" y="76" class="detail">1 glucosa ⇄ 2 lactato · músculo (glucólisis) ⇄ hígado (gluconeogénesis)</text>')
# leyenda
lx = 1010
A(f'<line x1="{lx}" y1="42" x2="{lx+34}" y2="42" stroke="#ea580c" stroke-width="3.4" marker-end="url(#aOrange)"/><text x="{lx+42}" y="46" class="detail">paso irreversible de la glucólisis</text>')
A(f'<line x1="{lx}" y1="66" x2="{lx+34}" y2="66" stroke="#7c3aed" stroke-width="3.4" marker-end="url(#aPurple)"/><text x="{lx+42}" y="70" class="detail">bypass de la gluconeogénesis</text>')
A(f'<line x1="{lx+300}" y1="38" x2="{lx+300}" y2="50" stroke="#059669" stroke-width="2.4" marker-end="url(#aGreen)"/><line x1="{lx+308}" y1="50" x2="{lx+308}" y2="38" stroke="#059669" stroke-width="2.4" marker-end="url(#aGreen)"/><text x="{lx+322}" y="46" class="detail">reacción reversible (compartida)</text>')

# Células y sangre
A('<rect x="540" y="130" width="620" height="1670" fill="url(#gSangre)"/>')
A('<rect x="30" y="130" width="510" height="1670" rx="28" fill="url(#gMusculo)" stroke="#fda4af" stroke-width="2"/>')
A('<rect x="1160" y="130" width="510" height="1670" rx="28" fill="url(#gHigado)" stroke="#fbbf24" stroke-width="2"/>')
A(bicapa(530, 552, 130, 1800)); A(bicapa(1150, 1172, 130, 1800))
A('<text x="80" y="172" class="region" fill="#be123c">MÚSCULO ESQUELÉTICO</text><text x="80" y="194" class="detail">citosol · ejercicio intenso / anaerobiosis</text>')
A('<text x="1215" y="172" class="region" fill="#a16207">HEPATOCITO</text><text x="1215" y="194" class="detail">citosol · recuperación de glucosa</text>')
A('<text x="850" y="172" text-anchor="middle" class="region" fill="#0369a1">SANGRE</text>')

# Flujos en sangre
A('<line x1="1218" y1="272" x2="496" y2="272" stroke="#0284c7" stroke-width="5" marker-end="url(#aBlue)"/>')
A(pill(850, 246, "D-GLUCOSA · 6 C", "#0369a1", "#e0f2fe", 138))
A('<text x="850" y="300" text-anchor="middle" class="detail">hígado → músculo</text>')
A('<line x1="462" y1="1606" x2="1244" y2="1606" stroke="#ea580c" stroke-width="5" marker-end="url(#aOrange)"/>')
A(pill(850, 1580, "L-LACTATO · 3 C", "#c2410c", "#ffedd5", 142))
A('<text x="850" y="1634" text-anchor="middle" class="detail">músculo → hígado</text>')
A(transportador(541, 272, "GLUT4", "#0284c7", "#0369a1", 56)); A(transportador(1161, 272, "GLUT2", "#059669", "#047857", 56))
A(transportador(541, 1606, "MCT4", "#ea580c", "#c2410c", 56)); A(transportador(1161, 1606, "MCT1", "#ea580c", "#c2410c", 56))

# ---- MÚSCULO ---------------------------------------------------------------
for k, det in [("GLC", "entra por GLUT4"), ("G6P", "atrapada: no sale del músculo"), ("F6P", ""), ("FBP", ""),
               ("PEP", ""), ("PYR", "aceptor de electrones"), ("LAC", "sale por MCT4")]:
    A(estructura(k, AX_M, "izq")); A(texto_nombre(k, "izq", det))
IRR = ("IRREVERSIBLE", "#c2410c", "#ffedd5"); REV = ("REVERSIBLE", "#047857", "#d1fae5")
ATPm = lambda t: (t, "#b91c1c", "#fee2e2"); ATPp = lambda t: (t, "#047857", "#d1fae5")
A(flecha(AX_M, 322, 518, "#ea580c", "aOrange"));  A(etiqueta("izq", 420, IRR[0], IRR[1], IRR[2], "Hexoquinasa", [ATPm("−1 ATP")]))
A(reversible(AX_M, 630, 700));                    A(etiqueta("izq", 665, REV[0], REV[1], REV[2], "Fosfoglucosa isomerasa", []))
A(flecha(AX_M, 808, 868, "#ea580c", "aOrange"));  A(etiqueta("izq", 838, IRR[0], IRR[1], IRR[2], "PFK-1", [ATPm("−1 ATP")]))
A(reversible(AX_M, 980, 1062));                   A(etiqueta("izq", 1021, REV[0], REV[1], REV[2], "6 pasos (aldolasa → enolasa)", [ATPp("+2 ATP"), ATPp("+2 NADH")]))
A(flecha(AX_M, 1155, 1396, "#ea580c", "aOrange"));A(etiqueta("izq", 1275, IRR[0], IRR[1], IRR[2], "Piruvato quinasa", [ATPp("+2 ATP")]))
A(reversible(AX_M, 1495, 1560));                  A(etiqueta("izq", 1528, REV[0], REV[1], REV[2], "Lactato deshidrogenasa", [("NADH → NAD⁺", "#0f766e", "#ccfbf1")]))
# G6Pasa ausente en el músculo
A('<rect x="92" y="612" width="200" height="22" rx="11" fill="#fee2e2" stroke="#dc2626" stroke-width="1.6"/><text x="192" y="627" text-anchor="middle" class="chip" fill="#b91c1c">✕ SIN G6Pasa: no exporta glucosa</text>')
# reciclaje de NAD+
A('<path d="M 428 1528 C 520 1528 520 1021 428 1021" fill="none" stroke="#0f766e" stroke-width="2" stroke-dasharray="5 4" marker-end="url(#aTeal)"/>')
A(pill(495, 1275, "NAD⁺", "#0f766e", "#ccfbf1", 54))
A('<text x="495" y="1296" text-anchor="middle" class="detail">regenera NAD⁺</text>')
A('<text x="495" y="1309" text-anchor="middle" class="detail">para la glucólisis</text>')

# ---- HÍGADO ----------------------------------------------------------------
for k, det in [("GLC", "sale por GLUT2"), ("G6P", ""), ("F6P", ""), ("FBP", ""), ("PEP", ""),
               ("OAA", "sale de la mito como malato"), ("PYR", "sustrato gluconeogénico"), ("LAC", "entra por MCT1")]:
    A(estructura(k, AX_H, "der")); A(texto_nombre(k, "der", det))
BY = lambda n: (f"BYPASS {n}", "#6d28d9", "#ede9fe")
A(reversible(AX_H, 1495, 1560));  A(etiqueta("der", 1528, REV[0], REV[1], REV[2], "Lactato deshidrogenasa", [("NAD⁺ → NADH", "#0f766e", "#ccfbf1")]))
A(flecha(AX_H, 1397, 1345, "#7c3aed", "aPurple")); A(etiqueta("der", 1371, *BY(1), "Piruvato carboxilasa (mito)", [ATPm("−2 ATP"), ("+2 CO₂", "#0369a1", "#e0f2fe")]))
A(flecha(AX_H, 1218, 1155, "#7c3aed", "aPurple")); A(etiqueta("der", 1188, *BY("1b"), "PEPCK", [ATPm("−2 GTP"), ("−2 CO₂", "#0369a1", "#e0f2fe")]))
A(reversible(AX_H, 980, 1058));   A(etiqueta("der", 1019, REV[0], REV[1], REV[2], "6 pasos inversos", [ATPm("−2 ATP"), ATPm("−2 NADH")]))
A(flecha(AX_H, 866, 810, "#7c3aed", "aPurple")); A(etiqueta("der", 838, *BY(2), "Fructosa-1,6-bisfosfatasa", [("+H₂O → Pi", "#0369a1", "#e0f2fe")]))
A(reversible(AX_H, 630, 698));    A(etiqueta("der", 664, REV[0], REV[1], REV[2], "Fosfoglucosa isomerasa", []))
A(mini_re())
# mitocondria (aviso) junto a bypass 1

# ---- Balance ---------------------------------------------------------------
A('<rect x="70" y="1690" width="1560" height="110" rx="18" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.6"/>')
A('<text x="850" y="1718" text-anchor="middle" class="enzyme">BALANCE ENERGÉTICO POR 1 GLUCOSA (= 2 PIRUVATO)</text>')
A(pill(330, 1760, "MÚSCULO · glucólisis · +2 ATP netos (+2 NADH → lactato)", "#be123c", "#ffe4e6", 470))
A(pill(860, 1760, "HÍGADO · gluconeogénesis · −4 ATP −2 GTP (−2 NADH)", "#a16207", "#fef3c7", 440))
A(pill(1350, 1760, "CICLO · −4 ATP-eq netos: lo paga el hígado", "#b91c1c", "#fee2e2", 400))

DEFS = '''<defs>
  <linearGradient id="gMusculo" x2="0" y2="1"><stop stop-color="#fff7f8"/><stop offset="1" stop-color="#fff1f2"/></linearGradient>
  <linearGradient id="gHigado" x2="0" y2="1"><stop stop-color="#fffcf0"/><stop offset="1" stop-color="#fff7d6"/></linearGradient>
  <linearGradient id="gSangre" x2="0" y2="1"><stop stop-color="#e0f2fe"/><stop offset="1" stop-color="#f0f9ff"/></linearGradient>
  <marker id="aOrange" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" refX="9" refY="6" orient="auto"><path d="M0 0L12 6L0 12Z" fill="#ea580c"/></marker>
  <marker id="aPurple" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" refX="9" refY="6" orient="auto"><path d="M0 0L12 6L0 12Z" fill="#7c3aed"/></marker>
  <marker id="aGreen" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" refX="9" refY="6" orient="auto"><path d="M0 0L12 6L0 12Z" fill="#059669"/></marker>
  <marker id="aBlue" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" refX="9" refY="6" orient="auto"><path d="M0 0L12 6L0 12Z" fill="#0284c7"/></marker>
  <marker id="aSlate" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" refX="9" refY="6" orient="auto"><path d="M0 0L12 6L0 12Z" fill="#475569"/></marker>
  <marker id="aTeal" markerUnits="userSpaceOnUse" markerWidth="12" markerHeight="12" refX="9" refY="6" orient="auto"><path d="M0 0L12 6L0 12Z" fill="#0f766e"/></marker>
  <style>
    text{stroke:none}
    .title{font:900 30px Inter,Arial,sans-serif;fill:#172033;letter-spacing:1.5px}
    .region{font:900 19px Inter,Arial,sans-serif;letter-spacing:2px}
    .name{font:900 19px Inter,Arial,sans-serif;fill:#172033}
    .carbon{font:900 13px Inter,Arial,sans-serif;fill:#f97316}
    .detail{font:700 12px Inter,Arial,sans-serif;fill:#64748b}
    .enzyme{font:900 14px Inter,Arial,sans-serif;fill:#334155}
    .chip{font:900 10.5px Inter,Arial,sans-serif}
    .tr{font:900 11px Inter,Arial,sans-serif;fill:#fff}
    .g6p{font:900 11px Inter,Arial,sans-serif;fill:#92400e}
    .lumen{font:900 10px Inter,Arial,sans-serif;fill:#7c3aed;letter-spacing:2px;opacity:.7}
  </style>
</defs>'''

SVG = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">\n{DEFS}\n'
       + "\n".join(partes) + '\n</svg>')

HTML = ('<!doctype html><html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
        '<title>Ciclo de Cori</title><link rel="preconnect" href="https://fonts.googleapis.com">'
        '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;700;800;900&display=swap" rel="stylesheet">'
        '<style>body{margin:0;padding:20px;background:#0b0f19}main{max-width:1700px;margin:auto;background:#fff;box-shadow:0 24px 60px #0008}'
        'svg{display:block;width:100%;height:auto}</style></head><body><main>' + SVG + '</main></body></html>')

(OUT / 'Ciclo_de_Cori.svg').write_text(SVG, encoding='utf-8')
(OUT / 'Ciclo_de_Cori.html').write_text(HTML, encoding='utf-8')
print('Generados: Ciclo_de_Cori.svg y Ciclo_de_Cori.html')
