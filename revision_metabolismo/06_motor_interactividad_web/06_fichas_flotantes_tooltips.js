/* ============================================================================
 * MÓDULO DE REVISIÓN: Fichas Flotantes Estequiométricas (Tooltips)
 * ============================================================================
 * Archivo original : 07_AMPLIACION_TEMARIO/interactividad_html.py (líneas 1158 a 1304 de 1638)
 * Descripción      : Muestra sustratos, productos, cofactores, ΔG°' y regulación al pasar el cursor o hacer clic sobre enzimas y metabolitos.
 * ============================================================================ */

    // 5. FICHA FLOTANTE INTELIGENTE / TOOLTIP ESTEQUIOMÉTRICO
    // =========================================================================
    const tooltipEl = document.getElementById('ui_tooltip_card');
    let isTooltipPinned = false;
    let pinnedElement = null;

    function unpinTooltip() {
      isTooltipPinned = false;
      pinnedElement = null;
      if (tooltipEl) {
        tooltipEl.classList.remove('ui_tt_pinned');
        tooltipEl.style.pointerEvents = 'none';
        tooltipEl.style.display = 'none';
      }
    }

    function pinTooltip(el, mouseX, mouseY) {
      if (!tooltipEl) return;
      isTooltipPinned = true;
      pinnedElement = el;
      mostrarTooltip(el, mouseX, mouseY, true);
    }

    function buscarViaDeElemento(el) {
      const parentRuta = el.closest('[id^="ruta_"], [id^="lupa_"]');
      if (!parentRuta) return null;
      const rid = parentRuta.id;
      for (const via of Object.values(TABLA_VIAS)) {
        if (via.grupos.includes(rid)) return via;
      }
      return null;
    }

    function mostrarTooltip(el, mouseX, mouseY, pinned = false) {
      if (!tooltipEl || (isPanning && !isTooltipPinned)) return;
      if (isTooltipPinned && !pinned) return; // Si ya está fijada, no sobreescribir con hover

      const isMetabolito = el.id && el.id.startsWith('m_');
      const isEnzima = el.id && el.id.startsWith('rx_');
      if (!isMetabolito && !isEnzima) return;

      const via = buscarViaDeElemento(el);
      const textArr = Array.from(el.querySelectorAll('text')).map(t => t.textContent.trim()).filter(Boolean);

      let htmlContenido = '';
      const closeBtnHtml = pinned ? `<button class="ui_tt_close_btn" onclick="unpinTooltip()" title="Cerrar ficha (Esc)">✕</button>` : '';
      const pinHintHtml = !pinned 
        ? `<div class="ui_tt_pin_hint">Clic para fijar ficha y ver ecuación completa</div>` 
        : `<div class="ui_tt_pin_hint" style="color:#38bdf8;">Ficha fijada • Presiona Esc o clica fuera para cerrar</div>`;

      // CASO 1: REACCIÓN / ENZIMA CON ESTEQUIOMETRÍA
      if (isEnzima) {
        const rxData = (typeof TABLA_REACCIONES_ESTEQUIOMETRIA !== 'undefined') ? TABLA_REACCIONES_ESTEQUIOMETRIA[el.id] : null;
        const colorVia = via ? via.color : '#0284c7';
        const nombreVia = via ? `Vía ${via.numero}: ${via.nombre}` : (rxData ? rxData.via : 'Vía Metabólica');

        if (rxData) {
          const ecBadge = rxData.ec ? `<span class="ui_tt_badge_ec">${rxData.ec}</span>` : '';
          htmlContenido = `
            ${closeBtnHtml}
            <div class="ui_tt_header_row">
              <span class="ui_tt_badge_via" style="background:${colorVia}">${nombreVia}</span>
              ${ecBadge}
              <span style="font-size:9.5px; color:#94a3b8; margin-left:auto;">${rxData.compartimento || ''}</span>
            </div>
            <h4>${rxData.enzima}</h4>
            <div class="ui_tt_eq_box">
              <div class="ui_tt_eq_label">ECUACIÓN QUÍMICA BALANCEADA:</div>
              <div class="ui_tt_eq_text">${rxData.ecuacion}</div>
            </div>
            <div class="ui_tt_grid">
              <div class="ui_tt_grid_row"><span class="ui_tt_label">Sustratos:</span> <span class="ui_tt_val">${rxData.sustratos.join(', ')}</span></div>
              <div class="ui_tt_grid_row"><span class="ui_tt_label">Productos:</span> <span class="ui_tt_val" style="color:#38bdf8; font-weight:700;">${rxData.productos.join(', ')}</span></div>
              ${rxData.coproductos ? `<div class="ui_tt_grid_row"><span class="ui_tt_label">Coproductos:</span> <span class="ui_tt_val">${rxData.coproductos}</span></div>` : ''}
              ${rxData.deltaG ? `<div class="ui_tt_grid_row"><span class="ui_tt_label">Termodinámica:</span> <span class="ui_tt_val">${rxData.deltaG}</span></div>` : ''}
            </div>
            ${rxData.regulacion ? `<div class="ui_tt_reg_box"><strong style="color:#fbbf24;">Regulación:</strong> ${rxData.regulacion}</div>` : ''}
            ${rxData.relevancia ? `<div style="margin-top:6px; font-size:10px; color:#94a3b8; line-height:1.3;">${rxData.relevancia}</div>` : ''}
            ${pinHintHtml}
          `;
        } else {
          // Reacción sin ficha estequiométrica específica: extraer del SVG
          let titulo = textArr[0] || el.id;
          let sub = textArr.find(t => t.includes('EC ')) || '';
          let filas = textArr.filter(t => t !== titulo && t !== sub).map(t => `<div class="ui_tt_row">• ${t}</div>`).join('');
          htmlContenido = `
            ${closeBtnHtml}
            <div class="ui_tt_header_row">
              <span class="ui_tt_badge_via" style="background:${colorVia}">${nombreVia}</span>
              ${sub ? `<span class="ui_tt_badge_ec">${sub}</span>` : ''}
            </div>
            <h4>${titulo}</h4>
            ${filas}
            ${pinHintHtml}
          `;
        }
      } else {
        // CASO 2: METABOLITO
        const formulaAtoms = new Set(['O', 'H', 'OH', 'HO', 'CH₂OH', 'Ⓟ', 'O-PO₃²⁻', 'NH₃⁺', 'COO⁻', 'CH₂', 'CH₃']);
        const realNames = textArr.filter(t => !formulaAtoms.has(t) && !t.startsWith('[') && !t.endsWith(']'));
        let titulo = realNames[0] || textArr[0] || el.id;
        const carbonTag = textArr.find(t => t.startsWith('[') && t.endsWith(']'));
        const colorVia = via ? via.color : '#0284c7';
        const nombreVia = via ? `Vía ${via.numero}: ${via.nombre}` : 'Metabolito Intermediario';

        let filas = [];
        textArr.forEach(t => {
          if (t !== titulo && t !== carbonTag && !formulaAtoms.has(t)) {
            filas.push(`<div class="ui_tt_row">• ${t}</div>`);
          }
        });

        htmlContenido = `
          ${closeBtnHtml}
          <div class="ui_tt_header_row">
            <span class="ui_tt_badge_via" style="background:${colorVia}">${nombreVia}</span>
            ${carbonTag ? `<span class="ui_tt_badge_ec" style="background:#0f766e; border-color:#14b8a6; color:#ccfbf1;">${carbonTag} Carbonos</span>` : ''}
          </div>
          <h4>${titulo}</h4>
          ${filas.join('')}
          ${pinHintHtml}
        `;
      }

      tooltipEl.innerHTML = htmlContenido;
      if (pinned) {
        tooltipEl.classList.add('ui_tt_pinned');
      } else {
        tooltipEl.classList.remove('ui_tt_pinned');
      }

      tooltipEl.style.display = 'block';
      const tw = tooltipEl.offsetWidth || 340;
      const th = tooltipEl.offsetHeight || 160;
      let left = mouseX + 16;
      let top = mouseY + 16;
      if (left + tw > window.innerWidth - 14) left = mouseX - tw - 16;
      if (top + th > window.innerHeight - 14) top = mouseY - th - 16;
      tooltipEl.style.left = `${Math.max(12, left)}px`;
      tooltipEl.style.top = `${Math.max(12, top)}px`;
    }

    function ocultarTooltip() {
      if (tooltipEl && !isTooltipPinned) tooltipEl.style.display = 'none';
    }

    // =========================================================================
