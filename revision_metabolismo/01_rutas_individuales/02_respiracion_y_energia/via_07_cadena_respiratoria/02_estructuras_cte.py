# =============================================================================
# MÓDULO DE REVISIÓN: Complejos Multiproteicos I-IV y ATP Sintasa
# =============================================================================
# Archivo original : 02_RESPIRACION_Y_ENERGIA/via_07_cadena_respiratoria_atp_sintasa/estructuras_cadena_transporte.py (líneas 1 a 327 de 327)
# Descripción      : Geometría vectorial de los complejos respiratorios, CoQ, Citocromo c y F0F1.
# =============================================================================

"""
CATÁLOGO DE ESTRUCTURAS QUÍMICAS (SVG) - CADENA TRANSPORTADORA DE ELECTRONES
===========================================================================
Diseñadas bajo el mismo Manual de Estilo Editorial que las estructuras de la
Glucólisis (estructuras_glucosa.py):

- Trazos oscuros nítidos (#0f172a) de 2.1 a 2.5 pt.
- Oxígenos y grupos carbonilo resaltados en rojo (#dc2626).
- Nitrógenos en tinta oscura, con la misma jerarquía visual que los carbonos.
- Metal del grupo hemo (Fe) en ámbar mitocondrial (#b45309).
- Grupos fosfato como cápsula naranja (#ffedd5 de fondo, #ea580c de borde, Ⓟ).
- Origen de coordenadas (0,0) en la esquina superior izquierda de cada molécula.
- 1 unidad de dibujo ≡ 1 px de SVG (usar el parámetro `escala` al insertarlas).
"""

# =============================================================================
# BLOQUES REUTILIZABLES (NUCLEÓTIDOS)
# =============================================================================

def _bloque_adenina_ribosa():
    """
    Adenina (purina bicíclica) unida por enlace N-glucosídico a una ribosa.
    Punto de unión al fosfato (C5'): vértice inferior-derecho, local (44, 94).
    """
    return """
  <!-- Adenina (núcleo purínico bicíclico) -->
  <polygon points="4,46 18,34 36,34 46,46 36,58 18,58" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <polygon points="18,34 36,34 48,20 27,10 6,20" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <text x="27" y="53" fill="#0f172a" font-size="9" font-weight="900" text-anchor="middle">N</text>
  <text x="27" y="31" fill="#0f172a" font-size="9" font-weight="900" text-anchor="middle">N</text>

  <!-- Ribosa (anillo furanósico) -->
  <line x1="36" y1="58" x2="31" y2="74" stroke="#0f172a" stroke-width="2"/>
  <polygon points="14,74 36,74 44,94 25,106 7,94" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="14" cy="74" r="5" fill="#ffffff"/>
  <text x="14" y="77" fill="#dc2626" font-size="9" font-weight="900" text-anchor="middle">O</text>
"""


def _ribosa():
    """Ribosa suelta (anillo furanósico) con el O del anillo marcado en rojo."""
    return """
  <polygon points="14,0 36,0 44,20 25,32 7,20" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="14" cy="0" r="5" fill="#ffffff"/>
  <text x="14" y="3" fill="#dc2626" font-size="9" font-weight="900" text-anchor="middle">O</text>
"""


# =============================================================================
# 1. PORTADORES ELECTRÓNICOS SOLUBLES: NAD(H) Y FAD(H₂)
# =============================================================================

def _dinucleotido_nad(reducido=True):
    """
    NAD⁺ (piridinio aromático) o NADH (1,4-dihidropiridina reducida).
    Esqueleto: adenina-ribosa-Ⓟ-O-Ⓟ-ribosa-nicotinamida.
    """
    if reducido:
        nucleo_nicotinamida = """
  <!-- Nicotinamida REDUCIDA (1,4-dihidropiridina): H extra sobre C4 -->
  <polygon points="198,62 217,73 217,95 198,106 179,95 179,73" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
  <text x="185" y="100" fill="#0f172a" font-size="11" font-weight="900">N</text>
  <line x1="217" y1="73" x2="230" y2="66" stroke="#0f172a" stroke-width="1.9"/>
  <text x="234" y="63" fill="#0f172a" font-size="10" font-weight="800">H</text>
  <line x1="217" y1="95" x2="230" y2="102" stroke="#0f172a" stroke-width="1.9"/>
  <text x="234" y="108" fill="#0f172a" font-size="10" font-weight="800">H</text>
"""
    else:
        nucleo_nicotinamida = """
  <!-- Nicotinamida OXIDADA (piridinio): N⁺ sin hidrógenos de anillo -->
  <polygon points="198,62 217,73 217,95 198,106 179,95 179,73" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
  <text x="185" y="100" fill="#0f172a" font-size="11" font-weight="900">N</text>
  <text x="176" y="90" fill="#dc2626" font-size="12" font-weight="900">⁺</text>
"""

    return f"""{_bloque_adenina_ribosa()}

  <!-- Puente pirofosfato (cápsulas Ⓟ) -->
  <line x1="44" y1="94" x2="62" y2="108" stroke="#0f172a" stroke-width="2"/>
  <circle cx="76" cy="114" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="76" y="118" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
  <line x1="89" y1="114" x2="101" y2="114" stroke="#0f172a" stroke-width="2"/>
  <text x="95" y="109" fill="#dc2626" font-size="9" font-weight="900" text-anchor="middle">O</text>
  <circle cx="114" cy="114" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="114" y="118" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>

  <!-- Ribosa 2 -->
  <line x1="127" y1="114" x2="130" y2="96" stroke="#0f172a" stroke-width="2"/>
  <polygon points="136,76 158,76 166,96 147,108 129,96" fill="#ffffff" stroke="#0f172a" stroke-width="2.2"/>
  <circle cx="136" cy="76" r="5" fill="#ffffff"/>
  <text x="136" y="79" fill="#dc2626" font-size="9" font-weight="900" text-anchor="middle">O</text>
  <line x1="166" y1="96" x2="179" y2="95" stroke="#0f172a" stroke-width="2"/>
{nucleo_nicotinamida}
  <!-- Grupo carbamoilo (-CONH₂) sobre C3 -->
  <line x1="198" y1="62" x2="198" y2="46" stroke="#0f172a" stroke-width="2"/>
  <text x="198" y="42" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">C</text>
  <line x1="192" y1="34" x2="186" y2="20" stroke="#0f172a" stroke-width="1.8"/>
  <line x1="198" y1="32" x2="192" y2="18" stroke="#0f172a" stroke-width="1.8"/>
  <text x="182" y="17" fill="#dc2626" font-size="11" font-weight="800" text-anchor="end">O</text>
  <line x1="204" y1="42" x2="216" y2="38" stroke="#0f172a" stroke-width="1.8"/>
  <text x="220" y="36" fill="#0f172a" font-size="9.5" font-weight="800">NH₂</text>
"""


NADH = _dinucleotido_nad(reducido=True)
NAD_PLUS = _dinucleotido_nad(reducido=False)


def _flavina(reducida=True):
    """
    Núcleo tricíclico de isoaloxazina (flavina).
    El ribitilo se une en N10 (vértice local 72.3, 55).
    """
    hidrogenos = (
        '<text x="63" y="76" fill="#0f172a" font-size="9" font-weight="800">H</text>'
        '<text x="97" y="76" fill="#0f172a" font-size="9" font-weight="800">H</text>'
    ) if reducida else ""

    return f"""
  <!-- Anillo A: benceno con los dos metilos -->
  <polygon points="55,25 72.3,35 72.3,55 55,65 37.7,55 37.7,35" fill="#ffffff" stroke="#0f172a" stroke-width="2.4"/>
  <line x1="37.7" y1="35" x2="24" y2="29" stroke="#0f172a" stroke-width="2"/>
  <text x="21" y="25" fill="#0f172a" font-size="9.5" font-weight="800" text-anchor="end">CH₃</text>
  <line x1="37.7" y1="55" x2="24" y2="61" stroke="#0f172a" stroke-width="2"/>
  <text x="21" y="67" fill="#0f172a" font-size="9.5" font-weight="800" text-anchor="end">CH₃</text>

  <!-- Anillo B: pirazina central -->
  <polygon points="72.3,35 89.6,25 106.9,35 106.9,55 89.6,65 72.3,55" fill="#ffffff" stroke="#0f172a" stroke-width="2.4"/>

  <!-- Anillo C: pirimidina con los dos carbonilos -->
  <polygon points="106.9,35 124.2,25 141.5,35 141.5,55 124.2,65 106.9,55" fill="#ffffff" stroke="#0f172a" stroke-width="2.4"/>
  <line x1="124.2" y1="25" x2="128" y2="8" stroke="#0f172a" stroke-width="2.1"/>
  <line x1="130.5" y1="27" x2="134.5" y2="10" stroke="#0f172a" stroke-width="2.1"/>
  <text x="133" y="5" fill="#dc2626" font-size="12" font-weight="900" text-anchor="middle">O</text>
  <line x1="141.5" y1="35" x2="156" y2="29" stroke="#0f172a" stroke-width="2.1"/>
  <line x1="144" y1="41" x2="158.5" y2="35" stroke="#0f172a" stroke-width="2.1"/>
  <text x="163" y="32" fill="#dc2626" font-size="12" font-weight="900">O</text>

  <!-- Nitrógenos del anillo central (N10 y N5) -->
  <circle cx="72.3" cy="55" r="6.5" fill="#ffffff"/>
  <text x="72.3" y="58.5" fill="#0f172a" font-size="10" font-weight="900" text-anchor="middle">N</text>
  <circle cx="106.9" cy="55" r="6.5" fill="#ffffff"/>
  <text x="106.9" y="58.5" fill="#0f172a" font-size="10" font-weight="900" text-anchor="middle">N</text>
  {hidrogenos}
"""


def _dinucleotido_fad(reducido=True):
    """
    FAD (oxidado) o FADH₂ (reducido).
    Esqueleto: flavina-ribitilo-Ⓟ-O-Ⓟ-ribosa-adenina (AMP).
    """
    return f"""{_flavina(reducida=reducido)}

  <!-- Cadena de ribitilo -->
  <line x1="72.3" y1="55" x2="72.3" y2="74" stroke="#0f172a" stroke-width="2"/>
  <line x1="72.3" y1="74" x2="58" y2="86" stroke="#0f172a" stroke-width="2"/>
  <line x1="58" y1="86" x2="72" y2="98" stroke="#0f172a" stroke-width="2"/>
  <line x1="72" y1="98" x2="58" y2="110" stroke="#0f172a" stroke-width="2"/>
  <text x="52" y="80" fill="#0f172a" font-size="9" font-weight="800" text-anchor="end">OH</text>
  <text x="78" y="92" fill="#0f172a" font-size="9" font-weight="800">OH</text>
  <text x="52" y="116" fill="#0f172a" font-size="9" font-weight="800" text-anchor="end">OH</text>

  <!-- Puente pirofosfato -->
  <line x1="58" y1="110" x2="74" y2="122" stroke="#0f172a" stroke-width="2"/>
  <circle cx="88" cy="128" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="88" y="132" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
  <line x1="101" y1="128" x2="113" y2="128" stroke="#0f172a" stroke-width="2"/>
  <text x="107" y="123" fill="#dc2626" font-size="9" font-weight="900" text-anchor="middle">O</text>
  <circle cx="126" cy="128" r="13" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
  <text x="126" y="132" fill="#c2410c" font-size="11" font-weight="900" text-anchor="middle">Ⓟ</text>
  <line x1="139" y1="128" x2="178" y2="100" stroke="#0f172a" stroke-width="2"/>

  <!-- Resto de AMP (ribosa + adenina) -->
  <g transform="translate(134, 6)">
    {_bloque_adenina_ribosa()}
  </g>
"""


FADH2 = _dinucleotido_fad(reducido=True)
FAD = _dinucleotido_fad(reducido=False)


# =============================================================================
# 2. TRANSPORTADORES MÓVILES DE LA MEMBRANA: UBIQUINONA Y CITOCROMO c
# =============================================================================

def _ubiquinona(reducida=False):
    """
    Anillo benzoquinónico 2,3-dimetoxi-5-metil-1,4-benzoquinona con la cola
    isoprenoide característica (CoQ₁₀), simplificada con el rótulo (isopreno ×10).
    """
    if reducida:
        # Ubiquinol (QH₂): los dos carbonilos pasan a hidroxilos fenólicos
        grupo_c1 = """
  <line x1="97" y1="28" x2="97" y2="12" stroke="#0f172a" stroke-width="2.1"/>
  <text x="97" y="8" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">OH</text>
"""
        grupo_c4 = """
  <line x1="97" y1="72" x2="97" y2="88" stroke="#0f172a" stroke-width="2.1"/>
  <text x="97" y="100" fill="#0f172a" font-size="10" font-weight="800" text-anchor="middle">OH</text>
"""
    else:
        # Ubiquinona (Q): dos carbonilos quinónicos
        grupo_c1 = """
  <line x1="93.5" y1="28" x2="93.5" y2="10" stroke="#0f172a" stroke-width="2.1"/>
  <line x1="100.5" y1="28" x2="100.5" y2="10" stroke="#0f172a" stroke-width="2.1"/>
  <text x="97" y="6" fill="#dc2626" font-size="13" font-weight="900" text-anchor="middle">O</text>
"""
        grupo_c4 = """
  <line x1="93.5" y1="72" x2="93.5" y2="90" stroke="#0f172a" stroke-width="2.1"/>
  <line x1="100.5" y1="72" x2="100.5" y2="90" stroke="#0f172a" stroke-width="2.1"/>
  <text x="97" y="102" fill="#dc2626" font-size="13" font-weight="900" text-anchor="middle">O</text>
"""
    return f"""
  <!-- Anillo benzoquinónico -->
  <polygon points="97,28 116,39 116,61 97,72 78,61 78,39" fill="#ffffff" stroke="#0f172a" stroke-width="2.5"/>
{grupo_c1}
{grupo_c4}
  <!-- Metoxilos (posiciones 2 y 3) -->
  <line x1="116" y1="39" x2="132" y2="34" stroke="#0f172a" stroke-width="2"/>
  <text x="136" y="34" fill="#0f172a" font-size="10" font-weight="800">OCH₃</text>
  <line x1="116" y1="61" x2="132" y2="66" stroke="#0f172a" stroke-width="2"/>
  <text x="136" y="70" fill="#0f172a" font-size="10" font-weight="800">OCH₃</text>

  <!-- Metilo (posición 5) -->
  <line x1="78" y1="61" x2="64" y2="68" stroke="#0f172a" stroke-width="2"/>
  <text x="60" y="74" fill="#0f172a" font-size="10" font-weight="800" text-anchor="end">CH₃</text>

  <!-- Cola isoprenoide (posición 6) -->
  <polyline points="78,39 62,28 46,40 30,28 14,40" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linejoin="round"/>
  <text x="20" y="56" fill="#0f172a" font-size="9.5" font-weight="800" text-anchor="middle">(isopreno ×10)</text>
"""


UBIQUINONA = _ubiquinona(reducida=False)
UBIQUINOL = _ubiquinona(reducida=True)


CITOCROMO_C = """
  <!-- Macrociclo tetrapirrólico del grupo hemo c -->
  <polygon points="80,50 99,36 92,14 68,14 61,36" fill="#ffffff" stroke="#0f172a" stroke-width="2.3"/>
  <polygon points="96,62 110,43 132,50 132,74 110,81" fill="#ffffff" stroke="#0f172a" stroke-width="2.3"/>
  <polygon points="80,78 99,92 92,114 68,114 61,92" fill="#ffffff" stroke="#0f172a" stroke-width="2.3"/>
  <polygon points="64,62 50,43 28,50 28,74 50,81" fill="#ffffff" stroke="#0f172a" stroke-width="2.3"/>

  <!-- Puentes meteno que cierran el macrociclo -->
  <line x1="99" y1="36" x2="110" y2="43" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="110" y1="81" x2="99" y2="92" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="61" y1="92" x2="50" y2="81" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="50" y1="43" x2="61" y2="36" stroke="#0f172a" stroke-width="2.2"/>

  <!-- Nitrógenos coordinantes -->
  <text x="80" y="48" fill="#0f172a" font-size="8.5" font-weight="900" text-anchor="middle">N</text>
  <text x="97" y="65" fill="#0f172a" font-size="8.5" font-weight="900" text-anchor="middle">N</text>
  <text x="80" y="82" fill="#0f172a" font-size="8.5" font-weight="900" text-anchor="middle">N</text>
  <text x="63" y="65" fill="#0f172a" font-size="8.5" font-weight="900" text-anchor="middle">N</text>

  <!-- Hierro central (ciclo Fe³⁺ ⇄ Fe²⁺) -->
  <circle cx="80" cy="63" r="8.5" fill="#ffedd5" stroke="#b45309" stroke-width="2"/>
  <text x="80" y="67" fill="#b45309" font-size="10" font-weight="900" text-anchor="middle">Fe</text>

  <!-- Metilos de los puentes meteno -->
  <line x1="104.5" y1="39.5" x2="114" y2="28" stroke="#0f172a" stroke-width="2"/>
  <text x="117" y="25" fill="#0f172a" font-size="9.5" font-weight="800">CH₃</text>
  <line x1="55.5" y1="39.5" x2="46" y2="28" stroke="#0f172a" stroke-width="2"/>
  <text x="43" y="25" fill="#0f172a" font-size="9.5" font-weight="800" text-anchor="end">CH₃</text>

  <!-- Cadenas propionato (unidas por enlace tioéter a dos Cys de la proteína) -->
  <line x1="104.5" y1="86.5" x2="118" y2="96" stroke="#0f172a" stroke-width="2"/>
  <line x1="118" y1="96" x2="126" y2="112" stroke="#0f172a" stroke-width="2"/>
  <text x="129" y="122" fill="#0f172a" font-size="9.5" font-weight="800">COO⁻</text>
  <line x1="55.5" y1="86.5" x2="42" y2="96" stroke="#0f172a" stroke-width="2"/>
  <line x1="42" y1="96" x2="34" y2="112" stroke="#0f172a" stroke-width="2"/>
  <text x="31" y="122" fill="#0f172a" font-size="9.5" font-weight="800" text-anchor="end">COO⁻</text>
"""


# =============================================================================
# 3. ACEPTOR FINAL DE ELECTRONES Y PRODUCTOS
# =============================================================================

OXIGENO = """
  <circle cx="18" cy="14" r="12" fill="#ffffff" stroke="#dc2626" stroke-width="2.5"/>
  <text x="18" y="19" fill="#dc2626" font-size="14" font-weight="900" text-anchor="middle">O</text>
  <circle cx="18" cy="56" r="12" fill="#ffffff" stroke="#dc2626" stroke-width="2.5"/>
  <text x="18" y="61" fill="#dc2626" font-size="14" font-weight="900" text-anchor="middle">O</text>
  <line x1="13" y1="26" x2="13" y2="44" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="23" y1="26" x2="23" y2="44" stroke="#0f172a" stroke-width="2.2"/>
"""


AGUA = """
  <circle cx="30" cy="30" r="15" fill="#ffffff" stroke="#dc2626" stroke-width="2.5"/>
  <text x="30" y="36" fill="#dc2626" font-size="16" font-weight="900" text-anchor="middle">O</text>
  <line x1="19" y1="19" x2="8" y2="8" stroke="#0f172a" stroke-width="2.2"/>
  <text x="4" y="6" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">H</text>
  <line x1="41" y1="19" x2="52" y2="8" stroke="#0f172a" stroke-width="2.2"/>
  <text x="56" y="6" fill="#0f172a" font-size="11" font-weight="800" text-anchor="middle">H</text>
"""


# =============================================================================
# 4. SUSTRATO Y PRODUCTO DEL COMPLEJO II (SDH)
# =============================================================================

SUCCINATO = """
  <text x="0" y="22" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">⁻OOC</text>
  <line x1="16" y1="28" x2="38" y2="14" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="38" y1="14" x2="60" y2="28" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="60" y1="28" x2="82" y2="14" stroke="#0f172a" stroke-width="2.2"/>
  <text x="98" y="22" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">COO⁻</text>
  <text x="38" y="42" fill="#0f172a" font-size="9" font-weight="700" text-anchor="middle">CH₂</text>
  <text x="60" y="42" fill="#0f172a" font-size="9" font-weight="700" text-anchor="middle">CH₂</text>
"""


FUMARATO = """
  <text x="0" y="22" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">⁻OOC</text>
  <line x1="16" y1="28" x2="38" y2="14" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="38" y1="14" x2="60" y2="14" stroke="#0f172a" stroke-width="2.2"/>
  <line x1="60" y1="20" x2="60" y2="26" stroke="#0f172a" stroke-width="2.2"/>
  <text x="98" y="22" fill="#0f172a" font-size="12" font-weight="900" text-anchor="middle">COO⁻</text>
  <text x="49" y="8" fill="#0f172a" font-size="9" font-weight="700" text-anchor="middle">C=C (trans)</text>
  <text x="70" y="34" fill="#0f172a" font-size="9" font-weight="700">H</text>
"""
