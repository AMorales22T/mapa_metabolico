# =============================================================================
# MÓDULO DE REVISIÓN: Vía 23: Biosíntesis de TAG y Fosfolípidos (Vía de Kennedy)
# =============================================================================
# Archivo original : 07_AMPLIACION_TEMARIO/generar_ampliacion.py (líneas 531 a 566 de 925)
# Descripción      : Secuencia G3P -> GPAT -> LPA -> AGPAT -> PA -> Lipina-1 (PAP) -> 1,2-DAG y bifurcación a TAG (DGAT) y Fosfatidilcolina (CDP-colina).
# =============================================================================

    # -------------------------------------------------------------------------
    # VÍA 23: BIOSÍNTESIS DE TRIACILGLICEROLES Y FOSFOLÍPIDOS DE MEMBRANA
    # -------------------------------------------------------------------------
    p.append('<g id="ruta_sintesis_tag_fosfolipidos" class="ruta-metabolica">')
    p.append(encabezado_via(5850, 1130, 23, "BIOSÍNTESIS DE TRIACILGLICEROLES Y FOSFOLÍPIDOS", "Vía de Kennedy • Glicerol-3-P ➔ LPA ➔ PA ➔ DAG ➔ TAG / Fosfolípidos de Bicapa", color="#7c3aed"))

    p.append(nodo_libre(5880, 1240, "Glicerol-3-Fosfato", "3C", ea.GLICEROL_ESTRUCTURA, "m_der_g3p", dx=140, dy=20, detalle="Desde DHAP o Glicerol libre"))
    p.append(reaccion_flecha(6020, 1350, 70, "GPAT (Glicerol-3-P Aciltransferasa)", entra="+ Acil-CoA", sale="+ CoA-SH", ec="EC 2.3.1.15", color="#7c3aed", id_rx="rx_gpat"))
    
    p.append(nodo_libre(5880, 1450, "Lisofosfatidato (LPA)", "1-Acil", ea.LISOFOSFATIDATO, "m_der_lpa", dx=190, dy=20, detalle="Intermediario monoacilado"))
    p.append(reaccion_flecha(6020, 1570, 70, "AGPAT (Acilglicerol-P Aciltransferasa)", entra="+ Acil-CoA", sale="+ CoA-SH", ec="EC 2.3.1.51", color="#7c3aed", id_rx="rx_agpat"))

    p.append(nodo_libre(5880, 1670, "ÁCIDO FOSFATÍDICO (PA)", "1,2-Diacil-3-P", ea.ACIDO_FOSFATIDICO, "m_der_pa", dx=190, dy=20, detalle="PUNTO DE BIFURCACIÓN CENTRAL"))
    p.append(reaccion_flecha(6020, 1790, 70, "PAP (Fosfatidato Fosfatasa / Lipina-1)", entra="+ H₂O", sale="+ Pi", ec="EC 3.1.3.4", color="#7c3aed", id_rx="rx_pap"))

    p.append(nodo_libre(5880, 1890, "1,2-Diacilglicerol (DAG)", "DAG", ea.DIACILGLICEROL, "m_der_dag", dx=190, dy=20, detalle="Precursor de TAG y Fosfolípidos"))

    # Bifurcación TAG / Fosfolípidos
    p.append("""
    <g transform="translate(6020, 2010)">
      <path d="M -40 0 C -120 40, -140 70, -140 100" fill="none" stroke="#ea580c" stroke-width="3" marker-end="url(#arrowOrange)"/>
      <rect x="-240" y="30" width="150" height="40" rx="6" fill="#fff7ed" stroke="#ea580c" stroke-width="1.8"/>
      <text x="-165" y="48" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#c2410c" text-anchor="middle">DGAT + Acil-CoA</text>
      <text x="-165" y="62" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700" fill="#ea580c" text-anchor="middle">EC 2.3.1.20 (- CoA-SH)</text>

      <path d="M 40 0 C 70 40, 100 70, 100 100" fill="none" stroke="#0284c7" stroke-width="3" marker-end="url(#arrowBlue)"/>
      <rect x="135" y="30" width="160" height="40" rx="6" fill="#f0f9ff" stroke="#0284c7" stroke-width="1.8"/>
      <text x="215" y="48" font-family="'Inter', sans-serif" font-size="10.5" font-weight="900" fill="#0369a1" text-anchor="middle">CPT + CDP-Colina</text>
      <text x="215" y="62" font-family="'JetBrains Mono', monospace" font-size="8.5" font-weight="700" fill="#0284c7" text-anchor="middle">Vía de Kennedy (Bicapas)</text>
    </g>
    """)

    p.append(nodo_libre(5850, 2150, "Triacilglicerol (TAG)", "Reserva", ea.TRIACILGLICEROL, "m_der_tag_reserva", dx=190, dy=20, detalle="Almacenamiento energético en gotas"))
    p.append(nodo_libre(6220, 2150, "Fosfatidilcolina (PC)", "Membrana", ea.FOSFATIDILCOLINA, "m_der_pc_membrana", dx=175, dy=20, detalle="Fosfolípido mayoritario de bicapas"))
    p.append('</g>')

