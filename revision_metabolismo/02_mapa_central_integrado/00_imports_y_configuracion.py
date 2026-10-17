# =============================================================================
# MÓDULO DE REVISIÓN: Imports de Estructuras y Configuración General
# =============================================================================
# Archivo original : scripts_generacion/generar_prueba_visual_integrada.py (líneas 1 a 158 de 4188)
# Descripción      : Importa los módulos de estructuras de las 17 vías y define el offset vertical.
# =============================================================================

#!/usr/bin/env python3
"""
GENERADOR DE PRUEBA VISUAL INTEGRADA (ENTORNO BIOLÓGICO REAL - SIN GLOBOS NI CAJAS)
==================================================================================
Implementa fielmente el diseño orgánico celular:
- Fondo acuoso citosólico continuo con gradientes biológicos y halo citoplasmático.
- Membrana plasmática ondulada continua bicapa lipídica arriba, con receptor GLUT-4.
- Citoesqueleto y polirribosomas tenues flotando libremente.
- Gran Mitocondria anatómica arriñonada con doble membrana (MME y MMI con espacio intermembrana) y crestas onduladas.
- TODAS las moléculas y estructuras químicas flotan LIBRES en el espacio biológico:
  * CERO globos, CERO tarjetas blancas, CERO cajas envolventes o marcos artificiales.
  * Texto mínimo: Nombre del metabolito, conteo de carbonos [6C], enzima concisa y arcos de energía.
  * Agrupaciones con 'data-arrastrable="1"' para mover en editor_arrastrable.html.
"""

import os
import sys

import sys
import os

DIR_SCRIPT = os.path.dirname(os.path.abspath(__file__))
DIR_BASE = os.path.dirname(DIR_SCRIPT) if os.path.basename(DIR_SCRIPT) == "scripts_generacion" else DIR_SCRIPT
DIR_HTML = os.path.join(DIR_BASE, "versiones_html")
sys.path.append(os.path.join(DIR_BASE, "06_REGULACION_Y_LEYENDA"))
import regulacion

sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "via_02_gluconeogenesis"))
from estructuras_gluconeogenesis import (
    OXALACETATO as GLUCONEO_OXALACETATO,
    MALATO as GLUCONEO_MALATO,
    RE_GLUCOSA_6_FOSFATASA,
    LACTATO as GLUCONEO_LACTATO,
    GLICEROL as GLUCONEO_GLICEROL,
    GLICEROL_3_FOSFATO as GLUCONEO_G3P,
    FRUCTOSA_2_6_BISFOSFATO as GLUCONEO_F26BP
)

sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "via_01_glucolisis"))
sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "via_03_glucogenogenesis_y_glucogenolisis"))
sys.path.append(os.path.join(DIR_BASE, "01_CARBOHIDRATOS", "via_04_pentosas_fosfato"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "via_05_complejo_pdh"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "via_06_ciclo_de_krebs"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "via_07_cadena_respiratoria_atp_sintasa"))
sys.path.append(os.path.join(DIR_BASE, "02_RESPIRACION_Y_ENERGIA", "via_08_lanzaderas"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "via_09_beta_oxidacion"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "via_10_lipogenesis"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "via_11_cetogenesis_y_cetolisis"))
sys.path.append(os.path.join(DIR_BASE, "03_LIPIDOS", "via_12_colesterol_y_lipoproteinas"))
sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "via_13_transaminacion_y_desaminacion"))
sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "via_14_ciclo_de_la_urea"))
sys.path.append(os.path.join(DIR_BASE, "04_NITROGENO_Y_AMINOACIDOS", "via_12b_destinos_esqueletos_carbonados"))
sys.path.append(os.path.join(DIR_BASE, "05_NUCLEOTIDOS_Y_OTRAS", "via_15_sintesis_purinas_y_pirimidinas"))
sys.path.append(os.path.join(DIR_BASE, "05_NUCLEOTIDOS_Y_OTRAS", "via_16_degradacion_y_acido_urico"))
from estructuras_nucleotidos import (
    PRPP, FOSFORRIBOSILAMINA_5 as NUC_5_PRA, IMP, AMP as NUC_AMP, GMP as NUC_GMP,
    CARBAMOIL_FOSFATO as NUC_CARBAMOIL_P, DIHIDROOROTATO as NUC_DHO,
    OROTATO as NUC_OROTATO, UMP as NUC_UMP, CTP as NUC_CTP, DTMP as NUC_DTMP
)
from estructuras_degradacion import (
    HIPOXANTINA, XANTINA, ACIDO_URICO, URACILO as DEG_URACILO,
    DIHIDROURACILO as DEG_DIHIDROURACILO, BETA_UREIDOPROPIONATO, BETA_ALANINA
)
from estructuras_lanzadera import (
    GLICEROL_3_FOSFATO as LANZ_G3P
)
from estructuras_destinos_aa import (
    FENILALANINA as AA_FENILALANINA,
    TIROSINA as AA_TIROSINA,
    PROPIONIL_COA as AA_PROPIONIL_COA,
    METILMALONIL_COA as AA_METILMALONIL_COA,
    HOMOCISTEINA as AA_HOMOCISTEINA
)

from estructuras_pdh import (
    HIDROXIETIL_TPP as PDH_HIDROXIETIL_TPP,
    ACETIL_LIPOAMIDA as PDH_ACETIL_LIPOAMIDA,
    DIHIDROLIPOAMIDA as PDH_DIHIDROLIPOAMIDA,
    LIPOAMIDA_OXIDADA as PDH_LIPOAMIDA_OXIDADA
)

# Estructuras químicas
from estructuras_aminoacidos import (
    ALANINA as AMINO_ALANINA,
    GLUTAMATO as AMINO_GLUTAMATO,
    ALFA_CETOGLUTARATO as AMINO_AKG,
    ASPARTATO_AMINO as AMINO_ASPARTATO,
    OXALACETATO_AMINO as AMINO_OAA,
    ION_AMONIO as AMINO_NH4,
    GLUTAMINA as AMINO_GLUTAMINA,
    PLP_COENZIMA as AMINO_PLP
)
from estructuras_urea import (
    IONES_INICIALES as UREA_IONES_INICIALES,
    CARBAMOIL_FOSFATO as UREA_CARBAMOIL_P,
    ORNITINA as UREA_ORNITINA,
    CITRULINA as UREA_CITRULINA,
    ASPARTATO as UREA_ASPARTATO,
    ARGININOSUCCINATO as UREA_ARGININOSUCCINATO,
    FUMARATO as UREA_FUMARATO,
    ARGININA as UREA_ARGININA,
    UREA as UREA_MOL,
    N_ACETILGLUTAMATO as UREA_NAG
)
from estructuras_glucosa import (
    GLUCOSA, GLUCOSA_6_FOSFATO, FRUCTOSA_6_FOSFATO, FRUCTOSA_1_6_BISFOSFATO,
    DIHIDROXIACETONA_FOSFATO, GLICERALDEHIDO_3_FOSFATO, BISFOSFOGLICERATO_1_3,
    FOSFOGLICERATO_3, FOSFOGLICERATO_2, FOSFOENOLPIRUVATO, PIRUVATO
)
from estructuras_glucogeno import (
    GLUCOSA_1_FOSFATO, UDP_GLUCOSA, CADENA_GLUCOGENO
)
from estructuras_pentosas import (
    FOSFOGLUCONO_LACTONA_6, FOSFOGLUCONATO_6, RIBULOSA_5_FOSFATO,
    RIBOSA_5_FOSFATO, XILULOSA_5_FOSFATO, SEDOHEPTULOSA_7_FOSFATO, ERITROSA_4_FOSFATO,
    GLICERALDEHIDO_3_FOSFATO as PENTOSAS_GAP, FRUCTOSA_6_FOSFATO as PENTOSAS_F6P
)
from estructuras_krebs import (
    ACETIL_COA, OXALACETATO as KREBS_OXALACETATO, CITRATO, ISOCITRATO,
    ALFA_CETOGLUTARATO as KREBS_ALFA_CETOGLUTARATO, SUCCINIL_COA, SUCCINATO, FUMARATO, MALATO as KREBS_MALATO
)
from estructuras_lanzadera import (
    OXALACETATO as LANZ_OAA, MALATO as LANZ_MALATO,
    ASPARTATO as LANZ_ASP, GLUTAMATO as LANZ_GLU, ALFA_CETOGLUTARATO as LANZ_AKG
)
from estructuras_cadena_transporte import (
    UBIQUINONA, CITOCROMO_C, OXIGENO, AGUA, NADH as CTE_NADH, FADH2 as CTE_FADH2
)
from estructuras_beta_oxidacion import (
    PALMITATO, PALMITOIL_COA, CARNITINA, PALMITOIL_CARNITINA, TRANS_DELTA2_ENOIL_COA, L_BETA_HIDROXIACIL_COA, BETA_CETOACIL_COA, ACETIL_COA_BETA, MIRISTOIL_COA
)
from estructuras_lipogenesis import (
    MALONIL_COA, ACETOACETIL_ACP, D_BETA_HIDROXIACIL_ACP, TRANS_DELTA2_ENOIL_ACP, BUTIRIL_ACP, PALMITATO_LIBRE
)
from estructuras_ceto import (
    ACETOACETIL_COA, HMG_COA, ACETOACETATO, D_BETA_HIDROXIBUTIRATO, ACETONA
)
from estructuras_colesterol import (
    ACETOACETIL_COA_COLEST, HMG_COA_CITOSOL, MEVALONATO, ISOPENTENIL_PP, FARNESIL_PP, ESCUALENO, LANOSTEROL, COLESTEROL
)

ANCHO_CANVAS = 5800
ALTO_CANVAS = 5120
Y_OFFSET = 350
MOSTRAR_CONEXIONES_INTER_RUTA = False

GLICEROL_MOL = """
<g class="molecula-glicerol" stroke="#0f172a" stroke-width="2" fill="none" stroke-linecap="round" stroke-linejoin="round">
  <text x="35" y="18" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0284c7" text-anchor="middle">CH₂OH</text>
  <line x1="35" y1="22" x2="35" y2="38" />
  <circle cx="35" cy="44" r="2.5" fill="#0f172a"/>
  <line x1="38" y1="44" x2="52" y2="44" stroke="#0284c7" stroke-width="1.8"/>
  <text x="64" y="48" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0284c7" text-anchor="middle">OH</text>
  <line x1="35" y1="48" x2="35" y2="64" />
  <text x="35" y="78" font-family="'Inter', sans-serif" font-size="11" font-weight="800" fill="#0284c7" text-anchor="middle">CH₂OH</text>
</g>
"""

