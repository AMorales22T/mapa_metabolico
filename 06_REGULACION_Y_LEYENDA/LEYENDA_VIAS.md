# Leyenda del mapa metabólico integrado

> Generado desde `regulacion.py`. Cada número aparece en el mapa como un badge circular junto a su vía.

## Vías metabólicas incluidas

| Nº | Vía | Localización | Resumen |
|---|---|---|---|
| 1 | **Glucólisis** | Citosol | Glucosa → 2 Piruvato (+2 ATP, +2 NADH) |
| 2 | **Gluconeogénesis** | Matriz + citosol + RE | Piruvato → Glucosa (4 enzimas de bypass) · hepática |
| 3 | **Glucogenogénesis y glucogenólisis** | Citosol | Síntesis y degradación del glucógeno |
| 4 | **Vía de las pentosas fosfato** | Citosol | G6P → NADPH + Ribosa-5-P (fase oxidativa y no oxidativa) |
| 5 | **Complejo piruvato deshidrogenasa (PDH)** | Matriz | Piruvato → Acetil-CoA + CO₂ + NADH |
| 6 | **Ciclo de Krebs** | Matriz | Acetil-CoA → 2 CO₂ + 3 NADH + FADH₂ + GTP |
| 7 | **Cadena de transporte de electrones y ATP sintasa** | Membrana mitocondrial interna | Fosforilación oxidativa (acoplamiento quimiosmótico) |
| 8 | **Lanzaderas (malato-aspartato, citrato)** | Membrana mitocondrial interna | Transporte de equivalentes de reducción y de Acetil-CoA |
| 9 | **β-oxidación (y lanzadera de carnitina)** | Citosol → Matriz | Palmitoil-CoA → 8 Acetil-CoA + FADH₂ + NADH |
| 10 | **Lipogénesis (síntesis de ácidos grasos)** | Citosol | Acetil-CoA → Malonil-CoA → Palmitato (FAS) |
| 11 | **Cetogénesis** | Matriz · hepática | Acetil-CoA → Acetoacetato / β-Hidroxibutirato |
| 12 | **Síntesis de colesterol** | Citosol + RE | Acetil-CoA → HMG-CoA → Mevalonato → Colesterol |
| 13 | **Transaminación y desaminación oxidativa** | Citosol + Matriz | Recogida del grupo amino en Glutamato → NH₄⁺ |
| 14 | **Ciclo de la urea** | Matriz + citosol · hepático | NH₄⁺ + HCO₃⁻ + Aspartato → Urea |

## Clave de símbolos

| Símbolo | Significado |
|---|---|
| `⊕` | Activador alostérico (efector positivo) |
| `⊖` | Inhibidor alostérico (efector negativo / retroinhibición) |
| `P` | Modificación covalente por fosforilación (se indica la forma activa) |
| `⇄` | Reacción reversible (doble flecha) |
| `→` | Reacción irreversible (flecha simple, punto de control) |
| `- - →` | Conexión entre vías / transporte entre compartimentos |
| `▭` | Transportador de membrana (GLUT, MPC, CACT, AGC…) |
| `[nC]` | Número de átomos de carbono del metabolito |

## Código de colores

| Color | Uso |
|---|---|
| Naranja | Flujo principal de carbono (glucólisis, Krebs, lípidos) |
| Violeta | Bypass de la gluconeogénesis |
| Ámbar | Metabolismo del glucógeno |
| Verde azulado | Vía de las pentosas fosfato y ciclo de la urea |
| Azul | Transporte entre compartimentos / grupos amino |
| Verde (texto) | ⊕ activadores · productos energéticos ganados |
| Rojo (texto) | ⊖ inhibidores · consumo de energía |
| Círculo amarillo **P** | Modificación covalente (fosforilación) |
