# Regulación enzimática del mapa metabólico integrado

> Documento generado automáticamente desde `regulacion.py` (misma fuente que las etiquetas del mapa).
> Símbolos: **⊕** activador alostérico · **⊖** inhibidor alostérico · **P** modificación covalente (fosforilación).

> **Nota:** el mapa representa una célula *didáctica/genérica*. La gluconeogénesis, la cetogénesis y el ciclo de la urea
> son procesos **hepáticos** (la gluconeogénesis también renal).

## 1. Glucólisis

| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |
|---|---|---|---|---|---|
| **Hexoquinasa (I–III)** | 2.7.1.1 | — | Glucosa-6-P | — | En hígado actúa la Glucoquinasa (HK IV): no inhibida por G6P; secuestrada en el núcleo por GKRP (⊖ F6P); inducida por insulina |
| **Fosfofructoquinasa-1 (PFK-1)** | 2.7.1.11 | AMP, ADP, Fructosa-2,6-BP | ATP, Citrato, H⁺ | — | Indirecto vía Fructosa-2,6-BP (PFK-2): insulina ↑, glucagón ↓ |
| **Piruvato quinasa** | 2.7.1.40 | Fructosa-1,6-BP | ATP, Alanina, Acetil-CoA | Isoforma L (hígado): fosforilada por PKA = INACTIVA; desfosforilada = activa | Glucagón la inactiva (PKA); insulina la activa (fosfatasa) |

## 2. Gluconeogénesis

| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |
|---|---|---|---|---|---|
| **Piruvato carboxilasa** | 6.4.1.1 | Acetil-CoA (obligado) | ADP | — | Glucagón y cortisol inducen su síntesis |
| **PEP carboxiquinasa (PEPCK)** | 4.1.1.32 | — | — | — | Control transcripcional: glucagón (AMPc) y cortisol inducen; insulina reprime |
| **Fructosa-1,6-bisfosfatasa (FBPasa-1)** | 3.1.3.11 | Citrato | AMP, Fructosa-2,6-BP | — | Indirecto vía Fructosa-2,6-BP: glucagón ↑ actividad, insulina ↓ |
| **Glucosa-6-fosfatasa** | 3.1.3.9 | — | — | — | Control transcripcional: glucagón y glucocorticoides inducen; insulina reprime. Luz del RE (hígado y riñón) |
| **PFK-2 / FBPasa-2 (bifuncional)** | 2.7.1.105 / 3.1.3.46 | Fructosa-6-P (⊕ PFK-2) | Citrato (⊖ PFK-2) | Hígado: fosforilada por PKA → FBPasa-2 activa / PFK-2 inactiva (↓ F-2,6-BP). Desfosforilada (PP2A) → PFK-2 activa (↑ F-2,6-BP) | Glucagón → PKA → ↓ F-2,6-BP → gluconeogénesis. Insulina → fosfatasa → ↑ F-2,6-BP → glucólisis |

## 3. Glucogenogénesis y glucogenólisis

| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |
|---|---|---|---|---|---|
| **Glucógeno sintasa** | 2.4.1.11 | Glucosa-6-P | — | Fosforilada (GSK-3, PKA) = INACTIVA (forma b); desfosforilada por PP1 = activa (forma a) | Insulina la activa (inhibe GSK-3, activa PP1); glucagón y adrenalina la inactivan (PKA) |
| **Glucógeno fosforilasa** | 2.4.1.1 | AMP (músculo), Ca²⁺ (músculo) | ATP, Glucosa-6-P, Glucosa (hígado) | Fosforilada por fosforilasa quinasa = ACTIVA (forma a); desfosforilada por PP1 = inactiva (forma b) | Glucagón (hígado) y adrenalina (músculo) la activan vía AMPc–PKA; insulina la inactiva |

## 4. Vía de las pentosas fosfato

| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |
|---|---|---|---|---|---|
| **Glucosa-6-P deshidrogenasa (G6PDH)** | 1.1.1.49 | NADP⁺ | NADPH | — | Inducida por insulina y dieta rica en hidratos de carbono |

## 5. Complejo piruvato deshidrogenasa (PDH)

| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |
|---|---|---|---|---|---|
| **Complejo piruvato deshidrogenasa (PDH)** | 1.2.4.1 (E1) | Piruvato, ADP, NAD⁺, CoA, Ca²⁺ | Acetil-CoA, NADH, ATP | PDH quinasa (PDK) fosforila E1 = INACTIVA; PDH fosfatasa (PDP, ⊕ Ca²⁺) = activa | Insulina activa la PDP (hígado/adiposo); en ayuno aumenta la PDK |

## 6. Ciclo de Krebs

| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |
|---|---|---|---|---|---|
| **Citrato sintasa** | 2.3.3.1 | ADP | ATP, NADH, Succinil-CoA, Citrato | — | — |
| **Isocitrato deshidrogenasa** | 1.1.1.41 | ADP, Ca²⁺, NAD⁺ | ATP, NADH | — | — |
| **α-Cetoglutarato deshidrogenasa** | 1.2.4.2 | Ca²⁺, AMP | Succinil-CoA, NADH, ATP | — | — |

## 7. Cadena de transporte de electrones y ATP sintasa

| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |
|---|---|---|---|---|---|
| **ATP sintasa (Complejo V)** | 7.1.2.2 | ADP + Pi (control respiratorio) | ATP/ADP alto, IF1, Oligomicina | — | Hormona tiroidea aumenta la actividad mitocondrial; desacopladores (UCP1/termogenina) disipan el gradiente |

## 9. β-oxidación (y lanzadera de carnitina)

| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |
|---|---|---|---|---|---|
| **Carnitina palmitoiltransferasa-1 (CPT-1)** | 2.3.1.21 | — | Malonil-CoA | — | Glucagón la favorece indirectamente (inactiva la ACC → ↓ malonil-CoA). Paso limitante de la β-oxidación |

## 10. Lipogénesis (síntesis de ácidos grasos)

| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |
|---|---|---|---|---|---|
| **ATP-citrato liasa** | 2.3.3.8 | — | — | Fosforilada por Akt (vía insulina) = más activa | Insulina la activa e induce su síntesis (SREBP-1c) |
| **Acetil-CoA carboxilasa (ACC)** | 6.4.1.2 | Citrato | Palmitoil-CoA | Fosforilada por AMPK y PKA = INACTIVA; desfosforilada por PP2A = activa | Insulina la activa; glucagón y adrenalina la inactivan. Paso limitante de la lipogénesis |
| **Ácido graso sintasa (FAS)** | 2.3.1.85 | — | Palmitoil-CoA | — | Control transcripcional: insulina la induce (SREBP-1c); ayuno y AG poliinsaturados la reprimen |

## 11. Cetogénesis

| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |
|---|---|---|---|---|---|
| **HMG-CoA sintasa mitocondrial (HMGCS2)** | 2.3.3.10 | — | Succinil-CoA | — | Inducida por glucagón y ayuno (PPARα); reprimida por insulina. Paso limitante de la cetogénesis |

## 12. Síntesis de colesterol

| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |
|---|---|---|---|---|---|
| **HMG-CoA reductasa** | 1.1.1.34 | — | Colesterol, Mevalonato, Oxisteroles, Estatinas (fármaco) | Fosforilada por AMPK = INACTIVA; desfosforilada (fosfatasa, insulina) = activa | Insulina la activa; glucagón la inactiva. El colesterol reprime su gen (SREBP-2) y acelera su degradación (INSIG) |

## 13. Transaminación y desaminación oxidativa

| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |
|---|---|---|---|---|---|
| **Glutamato deshidrogenasa (GLDH)** | 1.4.1.3 | ADP, GDP | ATP, GTP | — | — |

## 14. Ciclo de la urea

| Enzima | EC | ⊕ Activadores | ⊖ Inhibidores | P Modificación covalente | Control hormonal / génico |
|---|---|---|---|---|---|
| **Carbamoil fosfato sintetasa I (CPS-I)** | 6.3.4.16 | N-Acetilglutamato (obligado) | — | — | La NAG sintasa se activa por arginina; dieta rica en proteínas y glucagón inducen las enzimas del ciclo |

## Ideas clave de integración

- **Insulina** (estado alimentado): desfosforila (PP1/PP2A) → activa glucógeno sintasa, PFK-2, piruvato quinasa, PDH, ACC y HMG-CoA reductasa.
- **Glucagón / adrenalina** (ayuno/estrés): AMPc → PKA fosforila → activa glucógeno fosforilasa y FBPasa-2; inactiva glucógeno sintasa, piruvato quinasa L, ACC.
- **AMPK** (AMP alto, poca energía): fosforila e inactiva ACC y HMG-CoA reductasa → frena síntesis y favorece oxidación.
- **Fructosa-2,6-bisfosfato**: regulador recíproco (⊕ PFK-1 / ⊖ FBPasa-1) que conecta la señal hormonal con glucólisis vs gluconeogénesis.
- **Malonil-CoA** (⊖ CPT-1): impide que se oxiden los ácidos grasos que se están sintetizando.
- **Acetil-CoA**: ⊖ PDH y ⊕ piruvato carboxilasa → desvía el piruvato hacia la gluconeogénesis cuando abunda la β-oxidación.
