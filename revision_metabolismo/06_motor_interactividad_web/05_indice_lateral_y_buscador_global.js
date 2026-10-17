/* ============================================================================
 * MÓDULO DE REVISIÓN: Índice Lateral Desplegable y Buscador Sin Acentos
 * ============================================================================
 * Archivo original : 07_AMPLIACION_TEMARIO/interactividad_html.py (líneas 1001 a 1157 de 1638)
 * Descripción      : Construcción dinámica del menú de 25 vías e indexación de textos SVG normalizados (NFD) con pulso visual.
 * ============================================================================ */

    // 3. PANEL LATERAL (ÍNDICE DE VÍAS)
    // =========================================================================
    function toggleSidebar() {
      const panel = document.getElementById('ui_sidebar_panel');
      const btn = document.getElementById('ui_btn_toggle_sidebar');
      if (!panel) return;
      panel.classList.toggle('ui_open');
      if (btn) btn.classList.toggle('ui_active');
    }

    function poblarSidebarVias() {
      const listEl = document.getElementById('ui_sidebar_list');
      if (!listEl) return;
      listEl.innerHTML = '';

      let viasCount = 0;
      Object.values(TABLA_VIAS).forEach(via => {
        const existeEnDoc = via.grupos.some(gid => document.getElementById(gid) !== null);
        if (!existeEnDoc) return;
        viasCount++;

        const item = document.createElement('div');
        item.className = 'ui_sidebar_item';
        item.setAttribute('data-via', via.id);
        item.onclick = () => {
          highlightPathway(via.id, true);
        };

        item.innerHTML = `
          <div class="ui_sidebar_badge" style="background: ${via.color}; color: #ffffff;">${via.numero}</div>
          <div class="ui_sidebar_info">
            <h4>${via.nombre}</h4>
            <p>${via.subtitulo}</p>
          </div>
        `;
        listEl.appendChild(item);
      });

      const btnToggle = document.getElementById('ui_btn_toggle_sidebar');
      if (btnToggle) {
        btnToggle.textContent = `📑 Vías (${viasCount})`;
        btnToggle.title = `Índice de Vías (${viasCount})`;
      }
    }

    function filtrarSidebarVias() {
      const input = document.getElementById('ui_sidebar_search');
      if (!input) return;
      const q = uiNormalize(input.value);
      document.querySelectorAll('.ui_sidebar_item').forEach(it => {
        const vid = it.getAttribute('data-via');
        const v = TABLA_VIAS[vid];
        if (!v) return;
        const texto = uiNormalize(v.numero + ' ' + v.nombre + ' ' + v.subtitulo);
        it.style.display = texto.includes(q) ? 'flex' : 'none';
      });
    }

    // =========================================================================
    // 4. BUSCADOR GLOBAL
    // =========================================================================
    let INDICE_BUSQUEDA = [];
    function construirIndiceBusqueda() {
      INDICE_BUSQUEDA = [];
      const svg = document.querySelector('#panLayer svg');
      if (!svg) return;

      const textNodes = svg.querySelectorAll('text');
      textNodes.forEach(tNode => {
        const raw = tNode.textContent.trim();
        if (!raw || raw.length < 2) return;
        const norm = uiNormalize(raw);
        const parentElem = tNode.closest('[id^="m_"], [id^="rx_"], [id^="ruta_"], [id^="lupa_"], .badge-via, .encabezado-seccion') || tNode;
        INDICE_BUSQUEDA.push({
          textoRaw: raw,
          textoNorm: norm,
          elemento: parentElem,
          textNode: tNode
        });
      });
    }

    function ejecutarBusqueda() {
      const input = document.getElementById('ui_search_input');
      const counter = document.getElementById('ui_search_counter');
      if (!input || !counter) return;

      const q = uiNormalize(input.value);

      if (searchPulseElement) {
        searchPulseElement.classList.remove('ui_search_pulse');
        searchPulseElement = null;
      }

      if (!q || q.length < 2) {
        searchMatches = [];
        searchMatchIndex = 0;
        counter.textContent = '';
        return;
      }

      const seen = new Set();
      searchMatches = [];
      INDICE_BUSQUEDA.forEach(item => {
        if (item.textoNorm.includes(q) && !seen.has(item.elemento)) {
          seen.add(item.elemento);
          searchMatches.push(item);
        }
      });

      if (searchMatches.length > 0) {
        searchMatchIndex = 0;
        irACoincidencia(searchMatchIndex);
      } else {
        counter.textContent = '0 de 0';
      }
    }

    function irACoincidencia(idx) {
      const counter = document.getElementById('ui_search_counter');
      if (searchMatches.length === 0) return;

      searchMatchIndex = (idx + searchMatches.length) % searchMatches.length;
      const match = searchMatches[searchMatchIndex];

      if (counter) counter.textContent = `${searchMatchIndex + 1} de ${searchMatches.length}`;

      if (searchPulseElement) searchPulseElement.classList.remove('ui_search_pulse');

      searchPulseElement = match.elemento;
      searchPulseElement.classList.add('ui_search_pulse');

      zoomToElement(match.elemento, 2.2);
    }

    function searchNext() {
      if (searchMatches.length > 0) irACoincidencia(searchMatchIndex + 1);
    }

    function searchPrev() {
      if (searchMatches.length > 0) irACoincidencia(searchMatchIndex - 1);
    }

    function clearSearch() {
      const input = document.getElementById('ui_search_input');
      const counter = document.getElementById('ui_search_counter');
      if (input) input.value = '';
      if (counter) counter.textContent = '';
      if (searchPulseElement) {
        searchPulseElement.classList.remove('ui_search_pulse');
        searchPulseElement = null;
      }
      searchMatches = [];
      searchMatchIndex = 0;
    }

    // =========================================================================
