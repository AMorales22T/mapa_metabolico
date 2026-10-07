#!/usr/bin/env python3
"""
Genera REGULACION_ENZIMATICA.md y LEYENDA_VIAS.md a partir de regulacion.py.
Uso:  python3 06_REGULACION_Y_LEYENDA/generar_documentos.py
"""
import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, DIR)
from regulacion import VIAS, SIMBOLOS, ENZIMAS, VIAS_POR_N  # noqa: E402


def _lista(xs):
    return ", ".join(xs) if xs else "—"


def doc_regulacion():
    out = [
        "# Regulación enzimática del mapa metabólico integrado",
        "",
        "> Documento generado automáticamente desde `regulacion.py` (misma fuente que las etiquetas del mapa).",
        "> Símbolos: **⊕** activador alostérico · **⊖** inhibidor alostérico · **P** modificación covalente (fosforilación).",
        "",
        "> **Nota:** el mapa representa una célula *didáctica/genérica*. La gluconeogénesis, la cetogénesis y el ciclo de la urea",
        "> son procesos **hepáticos** (la gluconeogénesis también renal).",
        "",
    ]
    vias_usadas = sorted({e["via"] for e in ENZIMAS})
    for n in vias_usadas:
        v = VIAS_POR_N[n]
        out.append(f"## {n}. {v['nombre']}")
        out.append("")
        out.append("| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |")
        out.append("|---|---|---|---|---|---|")
        for e in [e for e in ENZIMAS if e["via"] == n]:
            out.append(
                f"| **{e['enzima']}** | {e['ec']} | {_lista(e['activadores'])} | {_lista(e['inhibidores'])} "
                f"| {e['covalente'] or '—'} | {e['hormonal'] or '—'} |"
            )
        out.append("")
    out += [
        "## Ideas clave de integración",
        "",
        "- **Insulina** (estado alimentado): desfosforila (PP1/PP2A) → activa glucógeno sintasa, PFK-2, piruvato quinasa, PDH, ACC y HMG-CoA reductasa.",
        "- **Glucagón / adrenalina** (ayuno/estrés): AMPc → PKA fosforila → activa glucógeno fosforilasa y FBPasa-2; inactiva glucógeno sintasa, piruvato quinasa L, ACC.",
        "- **AMPK** (AMP alto, poca energía): fosforila e inactiva ACC y HMG-CoA reductasa → frena síntesis y favorece oxidación.",
        "- **Fructosa-2,6-bisfosfato**: regulador recíproco (⊕ PFK-1 / ⊖ FBPasa-1) que conecta la señal hormonal con glucólisis vs gluconeogénesis.",
        "- **Malonil-CoA** (⊖ CPT-1): impide que se oxiden los ácidos grasos que se están sintetizando.",
        "- **Acetil-CoA**: ⊖ PDH y ⊕ piruvato carboxilasa → desvía el piruvato hacia la gluconeogénesis cuando abunda la β-oxidación.",
        "",
    ]
    return "\n".join(out)


def doc_leyenda():
    out = [
        "# Leyenda del mapa metabólico integrado",
        "",
        "> Generado desde `regulacion.py`. Cada número aparece en el mapa como un badge circular junto a su vía.",
        "",
        "## Vías metabólicas incluidas",
        "",
        "| Nº | Vía | Localización | Resumen |",
        "|---|---|---|---|",
    ]
    for v in VIAS:
        out.append(f"| {v['n']} | **{v['nombre']}** | {v['lugar']} | {v['resumen']} |")
    out += ["", "## Clave de símbolos", "", "| Símbolo | Significado |", "|---|---|"]
    for s, t in SIMBOLOS:
        out.append(f"| `{s}` | {t} |")
    out += [
        "",
        "## Código de colores",
        "",
        "| Color | Uso |",
        "|---|---|",
        "| Naranja | Flujo principal de carbono (glucólisis, Krebs, lípidos) |",
        "| Violeta | Bypass de la gluconeogénesis |",
        "| Ámbar | Metabolismo del glucógeno |",
        "| Verde azulado | Vía de las pentosas fosfato y ciclo de la urea |",
        "| Azul | Transporte entre compartimentos / grupos amino |",
        "| Verde (texto) | ⊕ activadores · productos energéticos ganados |",
        "| Rojo (texto) | ⊖ inhibidores · consumo de energía |",
        "| Círculo amarillo **P** | Modificación covalente (fosforilación) |",
        "",
    ]
    return "\n".join(out)


if __name__ == "__main__":
    with open(os.path.join(DIR, "REGULACION_ENZIMATICA.md"), "w", encoding="utf-8") as f:
        f.write(doc_regulacion())
    with open(os.path.join(DIR, "LEYENDA_VIAS.md"), "w", encoding="utf-8") as f:
        f.write(doc_leyenda())
    print("✓ REGULACION_ENZIMATICA.md y LEYENDA_VIAS.md generados")
