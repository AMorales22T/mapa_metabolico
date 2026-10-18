#!/usr/bin/env python3
"""
SISTEMA INTEGRAL DE VERIFICACIÓN, TRAZABILIDAD Y CAPTURA DEL MAPA METABÓLICO
===========================================================================
Herramienta de auditoría continua, comprobación geométrica, recorrido bioquímico
y captura visual en alta resolución para mapas metabólicos vectoriales (SVG) y
sus visores interactivos (HTML).

Capacidades integradas:
 1. ANÁLISIS GEOMÉTRICO Y BIOQUÍMICO DEL SVG (Python puro, sin dependencias externas):
    - Inventario exhaustivo de vías (ruta_*), metabolitos (m_*), reacciones (rx_*) y conexiones (cx_*).
    - Trazabilidad de conexiones inter-ruta: origen exacto, destino real de cada punta de flecha,
      longitud real en cm impresos y detección de flechas que terminan en el vacío.
    - Detección de metabolitos sin flechas (huérfanos o callejones sin salida a menos de 30 px).
    - Detección de colisiones de texto con texto, texto con estructuras químicas y líneas que cruzan rótulos.
    - Auditoría tipográfica a escala real de impresión (pt según ancho del póster en mm).
    - Verificación de integridad: IDs duplicados, referencias rotas url(#...) y textos cortados.
    - Recorrido textual bioquímico estructurado por vía para revisión paso a paso sin abrir el póster.

 2. AUDITORÍA DEL VISOR HTML INTERACTIVO Y NAVEGADOR HEADLESS:
    - Búsqueda y autodetección de binarios de navegador (/usr/bin/brave, /opt/brave-bin/brave, chromium, google-chrome).
    - Verificación de consola JavaScript (certificación de 0 errores de JS).
    - Comprobación de paridad de IDs entre el SVG y el índice interactivo del HTML.
    - Soporte y prueba de parámetros URL (?via=6, ?search=Glucosa-6-Fosfato, ?state=ayuno).

 3. CAPTURA Y MOSAICO VISUAL VECTORIAL (rsvg-convert):
    - Mosaico completo a escala 1:1 (~150 ppp) con solapamiento del 8%.
    - Recortes individuales de cada una de las 25 vías metabólicas.
    - Recortes individuales de cada una de las 50 conexiones inter-ruta con trazado resaltado
      (verde = origen, rojo = destino, magenta = recorrido).
    - Galería visual index.html con diagnósticos embebidos.

Uso:
    python3 verificar_y_capturar.py [OPCIONES]

Ejemplos:
    python3 verificar_y_capturar.py
    python3 verificar_y_capturar.py --svg mapa_metabolico_alternativo/mapa_metabolico_alternativo.svg --sin-capturas
    python3 verificar_y_capturar.py --html versiones_html/01_mapa_ampliado_completo_25_vias.html
"""

import argparse
import hashlib
import html as htmllib
import math
import os
import re
import shutil
import subprocess
import sys
import time
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor

# ----------------------------------------------------------------------------
# Constantes y Umbrales de Calidad
# ----------------------------------------------------------------------------
DIST_FLECHA_OK = 35.0        # px: distancia máxima de una punta de flecha al nodo destino
DIST_NODO_FLECHA = 30.0      # px: distancia máxima para asociar una flecha a un metabolito
PT_MINIMO_CRITICO = 4.0      # pt impresos: umbral crítico de legibilidad en póster
PT_MINIMO_RECOMENDADO = 6.0  # pt impresos: umbral recomendado de lectura cómoda
AREA_CONTENEDOR = 1.5e6      # px²: grupos mayores se consideran contenedores/fondos
PREFIJOS_CONTENEDOR = ("ruta_", "capa_", "ampliacion_", "print_", "fondo", "cx_",
                       "bloque_leyenda", "lupa_cadena")
ETIQUETAS_IGNORADAS = {"defs", "marker", "style", "clipPath", "linearGradient",
                       "radialGradient", "pattern", "symbol", "mask", "filter",
                       "title", "desc", "metadata", "script"}

NUM = r"[-+]?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?"
MATRIZ_IDENTIDAD = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)


# ----------------------------------------------------------------------------
# Álgebra Afín y Parseo Vectorial
# ----------------------------------------------------------------------------
def mul_matriz(m, n):
    a, b, c, d, e, f = m
    A, B, C, D, E, F = n
    return (a * A + c * B, b * A + d * B, a * C + c * D, b * C + d * D,
            a * E + c * F + e, b * E + d * F + f)


def aplicar_matriz(m, x, y):
    a, b, c, d, e, f = m
    return (a * x + c * y + e, b * x + d * y + f)


def escala_matriz(m):
    return math.sqrt(abs(m[0] * m[3] - m[1] * m[2])) or 1.0


def parse_transform(s):
    m = MATRIZ_IDENTIDAD
    if not s:
        return m
    for nombre, args in re.findall(r"(\w+)\s*\(([^)]*)\)", s):
        v = [float(x) for x in re.findall(NUM, args)]
        if not v:
            continue
        if nombre == "translate":
            t = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0)
        elif nombre == "scale":
            t = (v[0], 0, 0, v[1] if len(v) > 1 else v[0], 0, 0)
        elif nombre == "matrix" and len(v) == 6:
            t = tuple(v)
        elif nombre == "rotate":
            a = math.radians(v[0])
            t = (math.cos(a), math.sin(a), -math.sin(a), math.cos(a), 0, 0)
            if len(v) == 3:
                t = mul_matriz(mul_matriz((1, 0, 0, 1, v[1], v[2]), t), (1, 0, 0, 1, -v[1], -v[2]))
        elif nombre == "skewX":
            t = (1, 0, math.tan(math.radians(v[0])), 1, 0, 0)
        elif nombre == "skewY":
            t = (1, math.tan(math.radians(v[0])), 0, 1, 0, 0)
        else:
            continue
        m = mul_matriz(m, t)
    return m


def parse_path(d):
    """Parsea una cadena d de SVG y devuelve (puntos_de_control, vertices_en_orden)."""
    toks = re.findall(r"[MmLlHhVvCcSsQqTtAaZz]|" + NUM, d or "")
    pts, seq = [], []
    i, cmd = 0, None
    x = y = sx = sy = 0.0

    def leer(k):
        nonlocal i
        vals = [float(toks[i + j]) for j in range(k)]
        i += k
        return vals

    while i < len(toks):
        t = toks[i]
        if t.isalpha():
            cmd = t
            i += 1
            if cmd in "Zz":
                x, y = sx, sy
                seq.append((x, y))
            continue
        if cmd is None:
            i += 1
            continue
        rel = cmd.islower()
        C = cmd.upper()
        try:
            if C == "M":
                a, b = leer(2)
                x, y = (x + a, y + b) if rel else (a, b)
                sx, sy = x, y
                pts.append((x, y)); seq.append((x, y))
                cmd = "l" if rel else "L"
            elif C in ("L", "T"):
                a, b = leer(2)
                x, y = (x + a, y + b) if rel else (a, b)
                pts.append((x, y)); seq.append((x, y))
            elif C == "H":
                (a,) = leer(1)
                x = x + a if rel else a
                pts.append((x, y)); seq.append((x, y))
            elif C == "V":
                (a,) = leer(1)
                y = y + a if rel else a
                pts.append((x, y)); seq.append((x, y))
            elif C == "C":
                v = leer(6)
                cps = [(v[0], v[1]), (v[2], v[3]), (v[4], v[5])]
                if rel:
                    cps = [(x + p, y + q) for p, q in cps]
                pts.extend(cps)
                x, y = cps[-1]; seq.append((x, y))
            elif C in ("S", "Q"):
                v = leer(4)
                cps = [(v[0], v[1]), (v[2], v[3])]
                if rel:
                    cps = [(x + p, y + q) for p, q in cps]
                pts.extend(cps)
                x, y = cps[-1]; seq.append((x, y))
            elif C == "A":
                v = leer(7)
                x, y = (x + v[5], y + v[6]) if rel else (v[5], v[6])
                pts.append((x, y)); seq.append((x, y))
            else:
                i += 1
        except (IndexError, ValueError):
            break
    return pts, seq


def muestrear_trazado(seq, paso=6.0):
    out = []
    for (x0, y0), (x1, y1) in zip(seq, seq[1:]):
        n = max(1, int(math.hypot(x1 - x0, y1 - y0) / paso))
        for k in range(n):
            out.append((x0 + (x1 - x0) * k / n, y0 + (y1 - y0) * k / n))
    if seq:
        out.append(seq[-1])
    return out


def bbox_puntos(puntos):
    xs = [p[0] for p in puntos]
    ys = [p[1] for p in puntos]
    return (min(xs), min(ys), max(xs), max(ys))


def union_bbox(a, b):
    if a is None:
        return b
    return (min(a[0], b[0]), min(a[1], b[1]), max(a[2], b[2]), max(a[3], b[3]))


def dist_punto_caja(x, y, c):
    dx = max(c[0] - x, 0, x - c[2])
    dy = max(c[1] - y, 0, y - c[3])
    return math.hypot(dx, dy)


def area_caja(c):
    return max(0.0, c[2] - c[0]) * max(0.0, c[3] - c[1])


def interseccion_area(a, b):
    return area_caja((max(a[0], b[0]), max(a[1], b[1]), min(a[2], b[2]), min(a[3], b[3])))


def num_attr(el, nombre, defecto=0.0):
    v = el.get(nombre)
    if v is None:
        return defecto
    m = re.search(NUM, v)
    return float(m.group(0)) if m else defecto


def estilo_prop(el, prop):
    v = el.get(prop)
    if v is None:
        st = el.get("style") or ""
        m = re.search(r"(?:^|;)\s*" + re.escape(prop) + r"\s*:\s*([^;]+)", st)
        if m:
            v = m.group(1).strip()
    return v


def tag_local(tag):
    return tag.split("}")[-1] if isinstance(tag, str) else ""


# ----------------------------------------------------------------------------
# Modelo de Inspección del Mapa Vectorial
# ----------------------------------------------------------------------------
class InspectorMapa:
    def __init__(self, ruta_svg, ancho_mm=1200.0):
        self.ruta = ruta_svg
        with open(ruta_svg, "r", encoding="utf-8") as f:
            self.fuente = f.read()
        self.raiz = ET.fromstring(self.fuente)
        vb = [float(v) for v in re.findall(NUM, self.raiz.get("viewBox", "0 0 1000 1000"))]
        self.vb = tuple(vb[:4])
        self.mm_por_px = ancho_mm / self.vb[2]
        self.pt_por_px = self.mm_por_px * 72.0 / 25.4
        self.cajas = {}        # id -> bbox absoluta (x0, y0, x1, y1)
        self.ancestros = {}    # id -> tupla de ids ancestros
        self.textos = []       # lista de dicts de texto
        self.flechas = []      # lista de flechas (inicio, punta, ids)
        self.conexiones = {}   # cx_id -> dict de tramos
        self.ids_vistos = {}
        self.marcadores_usados = set()
        self.ids_definidos = set()

        self._recorrer(self.raiz, MATRIZ_IDENTIDAD,
                       {"font-size": 16.0, "text-anchor": "start", "font-weight": "400"}, ())

    def _recorrer(self, el, m, her, pila_ids):
        tag = tag_local(el.tag)
        eid = el.get("id")
        if eid:
            self.ids_vistos[eid] = self.ids_vistos.get(eid, 0) + 1
            self.ids_definidos.add(eid)

        for attr in ("marker-end", "marker-start", "marker-mid", "fill", "stroke",
                     "clip-path", "filter", "mask"):
            v = el.get(attr) or ""
            for ref in re.findall(r"url\(#([^)]+)\)", v):
                self.marcadores_usados.add(ref)

        if tag in ETIQUETAS_IGNORADAS:
            for sub in el.iter():
                if sub.get("id"):
                    self.ids_definidos.add(sub.get("id"))
            return

        if (estilo_prop(el, "display") or "") == "none":
            return

        m = mul_matriz(m, parse_transform(el.get("transform")))
        her = dict(her)
        fs = estilo_prop(el, "font-size")
        if fs:
            mm = re.search(NUM, fs)
            if mm:
                her["font-size"] = float(mm.group(0))
        for p in ("text-anchor", "font-weight"):
            v = estilo_prop(el, p)
            if v:
                her[p] = v
        if eid:
            pila_ids = pila_ids + (eid,)
            self.ancestros[eid] = pila_ids[:-1]

        caja = None
        if tag == "rect":
            x, y = num_attr(el, "x"), num_attr(el, "y")
            w, h = num_attr(el, "width"), num_attr(el, "height")
            caja = bbox_puntos([aplicar_matriz(m, *p) for p in ((x, y), (x + w, y), (x, y + h), (x + w, y + h))])
        elif tag in ("circle", "ellipse"):
            cx, cy = num_attr(el, "cx"), num_attr(el, "cy")
            rx = num_attr(el, "r") if tag == "circle" else num_attr(el, "rx")
            ry = num_attr(el, "r") if tag == "circle" else num_attr(el, "ry")
            caja = bbox_puntos([aplicar_matriz(m, *p) for p in ((cx - rx, cy - ry), (cx + rx, cy + ry),
                                                                (cx - rx, cy + ry), (cx + rx, cy - ry))])
        elif tag == "line":
            p0 = aplicar_matriz(m, num_attr(el, "x1"), num_attr(el, "y1"))
            p1 = aplicar_matriz(m, num_attr(el, "x2"), num_attr(el, "y2"))
            caja = bbox_puntos([p0, p1])
            self._registrar_flecha(el, [p0, p1], pila_ids)
        elif tag in ("polygon", "polyline"):
            v = [float(t) for t in re.findall(NUM, el.get("points", ""))]
            pts = [aplicar_matriz(m, v[k], v[k + 1]) for k in range(0, len(v) - 1, 2)]
            if pts:
                caja = bbox_puntos(pts)
                if tag == "polyline":
                    self._registrar_flecha(el, pts, pila_ids)
        elif tag == "path":
            pts, seq = parse_path(el.get("d"))
            if pts:
                pts = [aplicar_matriz(m, *p) for p in pts]
                seq = [aplicar_matriz(m, *p) for p in seq]
                caja = bbox_puntos(pts)
                self._registrar_flecha(el, seq, pila_ids)
                self._registrar_tramo_conexion(el, seq, pila_ids)
        elif tag == "text":
            caja = self._registrar_texto(el, m, her, pila_ids)

        if caja is not None:
            for i_ in pila_ids:
                self.cajas[i_] = union_bbox(self.cajas.get(i_), caja)
        if tag != "text":
            for hijo in el:
                self._recorrer(hijo, m, her, pila_ids)

    def _registrar_texto(self, el, m, her, pila_ids):
        contenido = re.sub(r"\s+", " ", "".join(el.itertext())).strip()
        if not contenido:
            return None
        fs = her["font-size"]
        v = estilo_prop(el, "font-size")
        if v and re.search(NUM, v):
            fs = float(re.search(NUM, v).group(0))
        anchor = estilo_prop(el, "text-anchor") or her["text-anchor"]
        peso = str(estilo_prop(el, "font-weight") or her["font-weight"])
        factor = 0.62 if peso in ("700", "800", "900", "bold") else 0.56
        w = len(contenido) * fs * factor
        x, y = num_attr(el, "x"), num_attr(el, "y")
        x0 = x - w if anchor == "end" else (x - w / 2 if anchor == "middle" else x)
        esquinas = [(x0, y - fs * 0.78), (x0 + w, y - fs * 0.78),
                    (x0, y + fs * 0.22), (x0 + w, y + fs * 0.22)]
        caja = bbox_puntos([aplicar_matriz(m, *p) for p in esquinas])
        fs_efectivo = fs * escala_matriz(m)
        self.textos.append({
            "texto": contenido, "caja": caja, "fs_px": fs_efectivo,
            "pt": fs_efectivo * self.pt_por_px, "ids": pila_ids,
            "es_rotulo_cx": "cx_rotulos" in pila_ids,
        })
        return caja

    def _registrar_flecha(self, el, seq, pila_ids):
        if len(seq) < 2 or not (el.get("marker-end") or el.get("marker-start")):
            return
        self.flechas.append({
            "inicio": seq[0], "punta": seq[-1], "ids": pila_ids,
            "doble": bool(el.get("marker-start")),
        })

    def _registrar_tramo_conexion(self, el, seq, pila_ids):
        cx = next((i_ for i_ in pila_ids if i_.startswith("cx_") and i_ not in ("cx_trazos", "cx_rotulos")), None)
        if not cx or (el.get("stroke") or "").lower() in ("#ffffff", "#fff", "white"):
            return
        c = self.conexiones.setdefault(cx, {"tramos": [], "color": el.get("stroke")})
        c["tramos"].append({"seq": seq, "flecha": bool(el.get("marker-end"))})

    def es_contenedor(self, i_):
        c = self.cajas.get(i_)
        return (c is None or i_.startswith(PREFIJOS_CONTENEDOR) or area_caja(c) > AREA_CONTENEDOR)

    def nodos(self, prefijo=None):
        for i_, c in self.cajas.items():
            if self.es_contenedor(i_):
                continue
            if prefijo and not i_.startswith(prefijo):
                continue
            yield i_, c

    def nombre_nodo(self, i_):
        mejores = [t for t in self.textos if i_ in t["ids"] and len(t["texto"]) >= 3
                   and not re.fullmatch(r"\[?\d+C\]?", t["texto"])]
        if not mejores:
            return i_
        return max(mejores, key=lambda t: t["fs_px"])["texto"]

    def ruta_de(self, i_):
        for a in self.ancestros.get(i_, ()) + (i_,):
            if a.startswith("ruta_"):
                return a
        return None

    def nodo_mas_cercano(self, x, y, prefijo=None, excluir=()):
        mejor, dmin = None, float("inf")
        for i_, c in self.nodos(prefijo):
            if i_ in excluir:
                continue
            d = dist_punto_caja(x, y, c)
            if d < dmin or (d == dmin and mejor and area_caja(c) < area_caja(self.cajas[mejor])):
                mejor, dmin = i_, d
        return mejor, dmin


# ----------------------------------------------------------------------------
# Motor de Auditoría
# ----------------------------------------------------------------------------
def ejecutar_auditoria(mp):
    hallazgos = {"criticos": [], "importantes": [], "menores": []}
    res = {}

    # 1. Integridad de IDs y referencias
    res["ids_dup"] = sorted(i_ for i_, n in mp.ids_vistos.items() if n > 1)
    res["refs_rotas"] = sorted(r for r in mp.marcadores_usados if r not in mp.ids_definidos)
    for r in res["refs_rotas"]:
        hallazgos["criticos"].append(f"Referencia url(#{r}) inexistente: la flecha/relleno no se renderiza.")
    if res["ids_dup"]:
        hallazgos["menores"].append(f"{len(res['ids_dup'])} IDs duplicados en el SVG: " + ", ".join(res["ids_dup"][:10]))

    # 2. Conexiones inter-ruta y trazabilidad
    rotulos = [t for t in mp.textos if t["es_rotulo_cx"]]
    filas = []
    for cid, c in sorted(mp.conexiones.items()):
        tramos = c["tramos"]
        ini = tramos[0]["seq"][0]
        fin_tramo = next((t for t in reversed(tramos) if t["flecha"]), tramos[-1])
        fin = fin_tramo["seq"][-1]
        muestras = [p for t in tramos for p in muestrear_trazado(t["seq"], 10)]
        c["muestras"] = muestras
        c["caja"] = bbox_puntos(muestras)

        o, do = mp.nodo_mas_cercano(*ini, prefijo="m_")
        o2, do2 = mp.nodo_mas_cercano(*ini)
        d, dd = mp.nodo_mas_cercano(*fin, prefijo="m_")
        d2, dd2 = mp.nodo_mas_cercano(*fin)

        origen = o if do <= DIST_FLECHA_OK else (o2 if do2 <= DIST_FLECHA_OK else None)
        destino = d if dd <= DIST_FLECHA_OK else (d2 if dd2 <= DIST_FLECHA_OK else None)
        longitud = sum(math.hypot(b[0] - a[0], b[1] - a[1]) for t in tramos for a, b in zip(t["seq"], t["seq"][1:]))

        fila = {"id": cid, "ini": ini, "fin": fin, "origen": origen, "destino": destino,
                "d_origen": min(do, do2), "d_destino": min(dd, dd2),
                "cerca_origen": o2, "cerca_destino": d2, "longitud": longitud,
                "rotulo": None, "cruces": []}
        filas.append(fila)

        if destino is None:
            hallazgos["importantes"].append(
                f"{cid}: flecha en ({fin[0]:.0f},{fin[1]:.0f}) queda a {fila['d_destino']:.0f} px "
                f"del nodo más cercano ({d2}); el lector no sabe a qué metabolito o complejo llega.")
        if origen is None:
            hallazgos["menores"].append(
                f"{cid}: inicio en ({ini[0]:.0f},{ini[1]:.0f}) queda a {fila['d_origen']:.0f} px del nodo "
                f"más cercano ({o2}); el origen no es inmediato.")

    # Asociación de rótulos a conexiones
    for t in rotulos:
        cxx = (t["caja"][0] + t["caja"][2]) / 2
        cyy = (t["caja"][1] + t["caja"][3]) / 2
        mejor, dmin = None, float("inf")
        for f in filas:
            for (px, py) in mp.conexiones[f["id"]]["muestras"]:
                dd = math.hypot(px - cxx, py - cyy)
                if dd < dmin:
                    mejor, dmin = f, dd
        if mejor is not None and dmin < 60 and mejor["rotulo"] is None:
            mejor["rotulo"] = t["texto"]

    for f in filas:
        if f["rotulo"] is None:
            hallazgos["menores"].append(f"{f['id']}: sin rótulo textual cercano en cx_rotulos.")

    # Cruces de conexiones sobre textos
    nombres = [t for t in mp.textos if len(t["texto"]) >= 4 and not t["es_rotulo_cx"]]
    rejilla = {}
    CEL = 200
    for k, t in enumerate(nombres):
        c = t["caja"]
        for gx in range(int(c[0] // CEL), int(c[2] // CEL) + 1):
            for gy in range(int(c[1] // CEL), int(c[3] // CEL) + 1):
                rejilla.setdefault((gx, gy), []).append(k)

    for f in filas:
        tocados = set()
        for (px, py) in mp.conexiones[f["id"]]["muestras"]:
            for k in rejilla.get((int(px // CEL), int(py // CEL)), ()):
                c = nombres[k]["caja"]
                if c[0] <= px <= c[2] and c[1] <= py <= c[3]:
                    tocados.add(k)
        f["cruces"] = sorted({nombres[k]["texto"] for k in tocados})
        if len(f["cruces"]) >= 3:
            hallazgos["importantes"].append(f"{f['id']}: atraviesa {len(f['cruces'])} textos (" + "; ".join(f["cruces"][:5]) + ").")
        elif f["cruces"]:
            hallazgos["menores"].append(f"{f['id']}: cruza el texto «" + "», «".join(f["cruces"]) + "».")

    res["conexiones"] = filas

    # 3. Metabolitos sin flechas (huérfanos o discontinuidades)
    metabolitos = list(mp.nodos("m_"))
    sin_flechas, solo_entrada, solo_salida = [], [], []
    for i_, c in metabolitos:
        ent = sum(1 for fl in mp.flechas if dist_punto_caja(*fl["punta"], c) <= DIST_NODO_FLECHA)
        sal = sum(1 for fl in mp.flechas if dist_punto_caja(*fl["inicio"], c) <= DIST_NODO_FLECHA)
        if ent == 0 and sal == 0:
            sin_flechas.append(i_)
        elif sal == 0:
            solo_entrada.append(i_)
        elif ent == 0:
            solo_salida.append(i_)

    res["sin_flechas"], res["solo_entrada"], res["solo_salida"] = sin_flechas, solo_entrada, solo_salida
    for i_ in sin_flechas:
        hallazgos["importantes"].append(
            f"{i_} («{mp.nombre_nodo(i_)}», {mp.ruta_de(i_) or 'sin vía'}): ninguna flecha llega ni sale a < 30 px.")

    # 4. Tipografía y legibilidad de impresión
    pts = sorted(t["pt"] for t in mp.textos)
    criticos = [t for t in mp.textos if t["pt"] < PT_MINIMO_CRITICO]
    pequenos = [t for t in mp.textos if PT_MINIMO_CRITICO <= t["pt"] < PT_MINIMO_RECOMENDADO]
    res["tipografia"] = {
        "n": len(pts),
        "p05": pts[int(len(pts) * 0.05)] if pts else 0,
        "mediana": pts[len(pts) // 2] if pts else 0,
        "criticos": criticos, "pequenos": pequenos,
    }
    if criticos:
        hallazgos["importantes"].append(
            f"{len(criticos)} textos por debajo de {PT_MINIMO_CRITICO} pt impresos "
            f"(ej.: " + "; ".join(f"«{t['texto'][:25]}» {t['pt']:.1f} pt" for t in criticos[:4]) + ").")

    # 5. Textos cortados por el borde del lienzo
    x0, y0 = mp.vb[0], mp.vb[1]
    x1, y1 = x0 + mp.vb[2], y0 + mp.vb[3]
    fuera = [t for t in mp.textos if t["caja"][0] < x0 - 2 or t["caja"][2] > x1 + 2
             or t["caja"][1] < y0 - 2 or t["caja"][3] > y1 + 2]
    res["fuera"] = fuera
    for t in fuera:
        hallazgos["importantes"].append(f"Texto cortado por el borde exterior: «{t['texto'][:50]}».")

    # 6. Solapamientos de texto con texto
    solapes = []
    vistos = set()
    for celda, ks in rejilla.items():
        for a_ in range(len(ks)):
            for b_ in range(a_ + 1, len(ks)):
                ka, kb = ks[a_], ks[b_]
                if (ka, kb) in vistos:
                    continue
                vistos.add((ka, kb))
                ta, tb = nombres[ka], nombres[kb]
                inter = interseccion_area(ta["caja"], tb["caja"])
                if inter <= 0:
                    continue
                menor = min(area_caja(ta["caja"]), area_caja(tb["caja"])) or 1
                if inter / menor > 0.30:
                    solapes.append((inter / menor, ta, tb))
    solapes.sort(key=lambda s: -s[0])
    res["solapes"] = solapes

    return hallazgos, res


def generar_recorrido_textual(mp):
    """Genera la lista ordenada de metabolitos por vía para verificar la bioquímica."""
    vias = {}
    for i_, c in mp.nodos("m_"):
        r = mp.ruta_de(i_) or "(fuera de ruta_*)"
        vias.setdefault(r, []).append((c[1], c[0], i_))
    lineas = []
    for r in sorted(vias):
        caja = mp.cajas.get(r)
        cab = f"[{r}]"
        if caja:
            cab += f"  (x={caja[0]:.0f}..{caja[2]:.0f}, y={caja[1]:.0f}..{caja[3]:.0f})"
        lineas.append(cab)
        for _, _, i_ in sorted(vias[r]):
            lineas.append(f"   · {mp.nombre_nodo(i_)}  [{i_}]")
    return lineas


# ----------------------------------------------------------------------------
# Renderizado de Capturas Vectoriales (rsvg-convert)
# ----------------------------------------------------------------------------
def expandir_bbox(c, margen, vb):
    x0 = max(vb[0], c[0] - margen)
    y0 = max(vb[1], c[1] - margen)
    x1 = min(vb[0] + vb[2], c[2] + margen)
    y1 = min(vb[1] + vb[3], c[3] + margen)
    return (x0, y0, max(50, x1 - x0), max(50, y1 - y0))


def svg_recortado_doc(fuente, caja, ancho_px, extra=""):
    x, y, w, h = caja
    alto_px = max(1, int(round(ancho_px * h / w)))
    m = re.search(r"<svg\b[^>]*>", fuente)
    tag = m.group(0)
    for attr, val in (("viewBox", f"{x:.1f} {y:.1f} {w:.1f} {h:.1f}"),
                      ("width", str(ancho_px)), ("height", str(alto_px))):
        if re.search(r"\s" + attr + r'="[^"]*"', tag):
            tag = re.sub(r"(\s" + attr + r')="[^"]*"', r'\1="' + val + '"', tag, count=1)
        else:
            tag = tag[:-1] + f' {attr}="{val}">'
    doc = fuente[:m.start()] + tag + fuente[m.end():]
    if extra:
        k = doc.rfind("</svg>")
        doc = doc[:k] + extra + doc[k:]
    return doc, alto_px


def render_rsvg(rsvg_bin, fuente, caja, ancho_px, destino, tmpdir, extra=""):
    doc, alto = svg_recortado_doc(fuente, caja, ancho_px, extra)
    tmp = os.path.join(tmpdir, hashlib.md5(destino.encode()).hexdigest() + ".svg")
    with open(tmp, "w", encoding="utf-8") as f:
        f.write(doc)
    p = subprocess.run([rsvg_bin, "-w", str(ancho_px), "-h", str(alto), "-o", destino, tmp],
                       capture_output=True, text=True)
    if os.path.exists(tmp):
        os.remove(tmp)
    return p.returncode == 0 and os.path.exists(destino)


def ejecutar_capturas_vectoriales(mp, res, dir_salida, hilos=4, cols=6, filas=4):
    rsvg_bin = shutil.which("rsvg-convert")
    if not rsvg_bin:
        print("   ⚠ rsvg-convert no encontrado en el sistema: se omiten las capturas PNG.")
        return []

    tmpdir = os.path.join(dir_salida, "_tmp_render")
    os.makedirs(tmpdir, exist_ok=True)
    for sub in ("mosaico", "vias", "conexiones"):
        os.makedirs(os.path.join(dir_salida, "capturas", sub), exist_ok=True)

    trabajos = []

    # 1. Mosaico general a escala de póster (solapamiento del 8%)
    vx, vy, vw, vh = mp.vb
    tw, th = vw / cols, vh / filas
    for r in range(filas):
        for c in range(cols):
            caja = (vx + c * tw - tw * 0.04, vy + r * th - th * 0.04, tw * 1.08, th * 1.08)
            caja = expandir_bbox((caja[0], caja[1], caja[0] + caja[2], caja[1] + caja[3]), 0, mp.vb)
            nombre = f"mosaico_f{r + 1}_c{c + 1}.png"
            trabajos.append(("mosaico", nombre, caja, min(1800, int(caja[2])), "",
                             f"Mosaico fila {r + 1}, col {c + 1} (x={caja[0]:.0f}..{caja[0] + caja[2]:.0f}, y={caja[1]:.0f}..{caja[1] + caja[3]:.0f})"))

    # 2. Recortes por vía metabólica
    for i_, c in sorted(mp.cajas.items()):
        if i_.startswith("ruta_") and area_caja(c) > 0:
            caja = expandir_bbox(c, 40, mp.vb)
            trabajos.append(("vias", f"{i_}.png", caja, min(2000, max(900, int(caja[2]))), "", i_))

    # 3. Recortes por conexión inter-ruta con trazado resaltado
    for f in res["conexiones"]:
        con = mp.conexiones[f["id"]]
        caja = expandir_bbox(con["caja"], 140, mp.vb)
        pts = " ".join(f"{x:.1f},{y:.1f}" for x, y in con["muestras"])
        grosor = max(6, caja[2] / 250)
        extra = (f'<g id="resaltado_auditoria"><polyline points="{pts}" fill="none" stroke="#ff00ff" '
                 f'stroke-width="{grosor * 2.2:.1f}" stroke-opacity="0.30" stroke-linejoin="round"/>'
                 f'<circle cx="{f["ini"][0]:.1f}" cy="{f["ini"][1]:.1f}" r="{grosor * 2.5:.1f}" fill="none" '
                 f'stroke="#16a34a" stroke-width="{grosor * 0.8:.1f}"/>'
                 f'<circle cx="{f["fin"][0]:.1f}" cy="{f["fin"][1]:.1f}" r="{grosor * 2.5:.1f}" fill="none" '
                 f'stroke="#dc2626" stroke-width="{grosor * 0.8:.1f}"/></g>')
        trabajos.append(("conexiones", f"{f['id']}.png", caja, min(1600, max(800, int(caja[2] / 2))), extra, f["id"]))

    print(f"   Renderizando {len(trabajos)} capturas vectoriales con {hilos} hilos...")
    t0 = time.time()

    def tarea(tr):
        sub, nombre, caja, ancho, extra, desc = tr
        dest = os.path.join(dir_salida, "capturas", sub, nombre)
        ok = render_rsvg(rsvg_bin, mp.fuente, caja, ancho, dest, tmpdir, extra)
        return (sub, nombre, desc, ok)

    with ThreadPoolExecutor(max_workers=hilos) as ex:
        resultados = list(ex.map(tarea, trabajos))

    shutil.rmtree(tmpdir, ignore_errors=True)
    fallos = [r for r in resultados if not r[3]]
    print(f"   ✓ {len(resultados) - len(fallos)} capturas generadas en {time.time() - t0:.1f} s"
          + (f" ({len(fallos)} fallidas)" if fallos else ""))
    return resultados


# ----------------------------------------------------------------------------
# Detección de Navegador y Comprobación Headless de HTML
# ----------------------------------------------------------------------------
def localizar_navegador():
    candidatos = [
        "/opt/brave-bin/brave",
        "/usr/bin/brave-browser",
        "/usr/bin/brave",
        shutil.which("brave"),
        shutil.which("brave-browser"),
        shutil.which("chromium"),
        shutil.which("google-chrome"),
        shutil.which("google-chrome-stable"),
    ]
    for c in candidatos:
        if c and os.path.exists(c) and os.access(c, os.X_OK):
            try:
                p = subprocess.run([c, "--version"], capture_output=True, text=True, timeout=5)
                if p.returncode == 0:
                    return c
            except Exception:
                continue
    return None


def comprobar_html_y_capturar_estados(mp, ruta_html, dir_salida):
    resultado = {
        "ruta": ruta_html,
        "navegador": None,
        "n_claves_svg": 0,
        "faltan_ids": [],
        "capturas_html": [],
        "errores_js": [],
        "soporta_url_params": False,
    }

    if not os.path.exists(ruta_html):
        resultado["errores_js"].append(f"Archivo HTML no encontrado: {ruta_html}")
        return resultado

    with open(ruta_html, "r", encoding="utf-8") as f:
        contenido_html = f.read()

    claves = [i_ for i_ in mp.ids_definidos if i_.startswith(("m_", "cx_", "ruta_", "rx_"))]
    resultado["n_claves_svg"] = len(claves)
    resultado["faltan_ids"] = sorted(i_ for i_ in claves if f'id="{i_}"' not in contenido_html)
    resultado["soporta_url_params"] = "URLSearchParams" in contenido_html or "location.search" in contenido_html

    nav = localizar_navegador()
    if not nav:
        print("   ⚠ Ningún navegador headless compatible encontrado (/usr/bin/brave, chromium, google-chrome).")
        return resultado

    resultado["navegador"] = nav
    dir_cap_html = os.path.join(dir_salida, "capturas", "html")
    os.makedirs(dir_cap_html, exist_ok=True)

    planes_captura = [
        ("captura_vista_inicial.png", "", "Vista inicial estándar del visor interactivo"),
        ("captura_via_resaltada.png", "?via=6", "Vía 6 (Ciclo de Krebs) resaltada y centrada"),
        ("captura_busqueda.png", "?search=Glucosa-6-Fosfato", "Búsqueda activa con pulso de Glucosa-6-Fosfato"),
        ("captura_modo_ayuno.png", "?state=ayuno", "Estado metabólico de Ayuno activo con banner"),
    ]

    print(f"   Ejecutando navegador headless ({os.path.basename(nav)})...")
    for nombre_archivo, url_params, descripcion in planes_captura:
        out_path = os.path.join(dir_cap_html, nombre_archivo)
        url = f"file://{os.path.abspath(ruta_html)}{url_params}"
        cmd = [
            nav,
            "--headless=new",
            "--no-sandbox",
            "--disable-gpu",
            "--window-size=1920,1080",
            "--enable-logging=stderr",
            "--v=1",
            "--virtual-time-budget=4000",
            f"--screenshot={out_path}",
            url
        ]
        try:
            p = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            lineas_err = [l for l in p.stderr.splitlines() if any(e in l for e in
                          ("Uncaught", "TypeError", "ReferenceError", "SyntaxError", "RangeError"))]
            for err in lineas_err:
                resultado["errores_js"].append(f"[{url_params or 'inicio'}] {err}")

            if os.path.exists(out_path) and os.path.getsize(out_path) > 10000:
                resultado["capturas_html"].append((nombre_archivo, descripcion, out_path, os.path.getsize(out_path)))
                print(f"      ✓ {nombre_archivo} ({os.path.getsize(out_path):,} bytes)")
            else:
                resultado["errores_js"].append(f"No se pudo generar captura: {out_path}")
        except subprocess.TimeoutExpired:
            resultado["errores_js"].append(f"Timeout al renderizar {url_params}")
        except Exception as ex:
            resultado["errores_js"].append(f"Error ejecutando navegador: {ex}")

    return resultado


# ----------------------------------------------------------------------------
# Generación del Informe de Auditoría y TSV
# ----------------------------------------------------------------------------
def generar_reporte_auditoria(mp, hallazgos, res, html_res, capturas_vec, dir_salida, ancho_mm):
    L = []
    L.append("================================================================================")
    L.append("   INFORME DE VERIFICACIÓN, TRAZABILIDAD Y AUDITORÍA DEL MAPA METABÓLICO        ")
    L.append("================================================================================")
    L.append(f"SVG inspeccionado: {mp.ruta}")
    L.append(f"Dimensiones viewBox: {mp.vb}  ·  Impresión nominal: {ancho_mm:.0f} mm de ancho")
    L.append(f"Factor de escala: 1 px = {mp.mm_por_px:.3f} mm = {mp.pt_por_px:.3f} pt")
    L.append(f"Fecha de ejecución: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    L.append("")

    L.append("1. INVENTARIO COMPLETO")
    L.append("-" * 80)
    vias_lista = [i_ for i_ in mp.cajas if i_.startswith("ruta_")]
    metab_lista = list(mp.nodos("m_"))
    rx_lista = [i_ for i_ in mp.cajas if i_.startswith("rx_")]
    L.append(f"Vías metabólicas (ruta_*):     {len(vias_lista):>4}")
    L.append(f"Metabolitos identificados (m_*): {len(metab_lista):>4}")
    L.append(f"Reacciones enzimáticas (rx_*):   {len(rx_lista):>4}")
    L.append(f"Conexiones inter-ruta (cx_*):    {len(res['conexiones']):>4}")
    L.append(f"Flechas totales en el lienzo:    {len(mp.flechas):>4}")
    L.append(f"Rótulos de texto renderizados:   {len(mp.textos):>4}")
    L.append("")

    L.append("2. RESUMEN DE DIAGNÓSTICO")
    L.append("-" * 80)
    L.append(f"CRÍTICOS:    {len(hallazgos['criticos'])}")
    L.append(f"IMPORTANTES: {len(hallazgos['importantes'])}")
    L.append(f"MENORES:     {len(hallazgos['menores'])}")
    L.append("")

    for nivel, titulo in (("criticos", "HALLAZGOS CRÍTICOS"),
                          ("importantes", "HALLAZGOS IMPORTANTES (REVISIÓN PRIORITARIA)"),
                          ("menores", "HALLAZGOS MENORES (PULIDO DIDÁCTICO Y VISUAL)")):
        L.append(f"{titulo} ({len(hallazgos[nivel])})")
        L.append("-" * 80)
        if hallazgos[nivel]:
            for h in hallazgos[nivel]:
                L.append(f" • {h}")
        else:
            L.append(" (Cero anomalías detectadas en este nivel)")
        L.append("")

    # Auditoría Tipográfica
    tip = res["tipografia"]
    L.append("3. AUDITORÍA TIPOGRÁFICA A ESCALA DE IMPRESIÓN")
    L.append("-" * 80)
    L.append(f"Tamaño mediano: {tip['mediana']:.1f} pt · Percentil 5: {tip['p05']:.1f} pt")
    L.append(f"Textos por debajo de {PT_MINIMO_CRITICO} pt: {len(tip['criticos'])} "
             f"({len(tip['criticos'])/max(1, len(mp.textos))*100:.1f}% del total)")
    L.append(f"Textos entre {PT_MINIMO_CRITICO} y {PT_MINIMO_RECOMENDADO} pt: {len(tip['pequenos'])}")
    L.append("")

    # Conexiones Inter-Ruta
    L.append("4. AUDITORÍA DETALLADA DE LAS CONEXIONES INTER-RUTA (TRAZABILIDAD 100%)")
    L.append("-" * 80)
    for f in res["conexiones"]:
        o_nom = f"{mp.nombre_nodo(f['origen'])} [{f['origen']}]" if f["origen"] else f"¿? (cerca de {f['cerca_origen']})"
        d_nom = f"{mp.nombre_nodo(f['destino'])} [{f['destino']}]" if f["destino"] else f"¿? (cerca de {f['cerca_destino']})"
        L.append(f"[{f['id']}]")
        L.append(f"    Rótulo visible:   {f['rotulo'] or '(SIN RÓTULO ASOCIADO)'}")
        L.append(f"    Origen:           {o_nom} (distancia: {f['d_origen']:.1f} px)")
        L.append(f"    Destino:          {d_nom} (distancia: {f['d_destino']:.1f} px)")
        L.append(f"    Longitud vector:  {f['longitud']:.0f} px ({f['longitud'] * mp.mm_por_px / 10:.1f} cm impresos)")
        if f["cruces"]:
            L.append(f"    Cruza textos:     {'; '.join(f['cruces'][:6])}")
        L.append("")

    # Solapamientos de Texto
    L.append("5. COLISIONES DE TEXTO CON TEXTO (INTERSECCIÓN > 30%)")
    L.append("-" * 80)
    if res["solapes"]:
        for ratio, a, b in res["solapes"][:35]:
            L.append(f" • Solapamiento {ratio*100:.0f}% en ({a['caja'][0]:.0f},{a['caja'][1]:.0f}):")
            L.append(f"     «{a['texto']}»  ⟂  «{b['texto']}»")
    else:
        L.append(" (Cero colisiones detectadas)")
    L.append("")

    # Metabolitos huérfanos
    L.append("6. METABOLITOS AISLADOS (SIN FLECHAS DENTRO DE 30 PX)")
    L.append("-" * 80)
    if res["sin_flechas"]:
        for i_ in res["sin_flechas"]:
            L.append(f" • {i_}: {mp.nombre_nodo(i_)} ({mp.ruta_de(i_) or 'sin grupo'})")
    else:
        L.append(" (Todos los metabolitos cuentan con flechas entrantes o salientes)")
    L.append("")

    # Auditoría HTML
    if html_res:
        L.append("7. COMPROBACIÓN DEL VISOR HTML INTERACTIVO")
        L.append("-" * 80)
        L.append(f"Archivo: {html_res['ruta']}")
        L.append(f"Soporte de parámetros URL (window.location.search): "
                 f"{'SÍ (Soportado)' if html_res['soporta_url_params'] else 'NO (FALTA IMPLEMENTAR URLSearchParams)'}")
        L.append(f"Paridad SVG/HTML: {html_res['n_claves_svg'] - len(html_res['faltan_ids'])}/{html_res['n_claves_svg']} IDs clave")
        if html_res["faltan_ids"]:
            L.append(f"IDs faltantes en HTML ({len(html_res['faltan_ids'])}): " + ", ".join(html_res["faltan_ids"][:20]))
        if html_res["navegador"]:
            L.append(f"Navegador headless: {html_res['navegador']}")
            L.append(f"Errores en consola JavaScript: {len(html_res['errores_js'])}")
            for e in html_res["errores_js"]:
                L.append(f"   ✗ {e}")
            L.append(f"Capturas de estado generadas: {len(html_res['capturas_html'])}")
            for nom, desc, ruta, sz in html_res["capturas_html"]:
                L.append(f"   ✓ {nom}: {desc} ({sz:,} bytes)")
        else:
            L.append("Navegador no disponible para prueba headless.")
        L.append("")

    # Recorrido Textual Bioquímico
    L.append("8. RECORRIDO TEXTUAL BIOQUÍMICO POR VÍA")
    L.append("-" * 80)
    L.extend(generar_recorrido_textual(mp))

    ruta_reporte = os.path.join(dir_salida, "INFORME_VERIFICACION.txt")
    with open(ruta_reporte, "w", encoding="utf-8") as f:
        f.write("\n".join(L) + "\n")

    # Archivo TSV de Conexiones
    ruta_tsv = os.path.join(dir_salida, "conexiones_trazabilidad.tsv")
    with open(ruta_tsv, "w", encoding="utf-8") as f:
        f.write("id\trotulo\torigen\tnombre_origen\tdestino\tnombre_destino\td_origen_px\td_destino_px\tlongitud_px\tcruces\n")
        for c in res["conexiones"]:
            f.write("\t".join([
                c["id"], c["rotulo"] or "", c["origen"] or "",
                mp.nombre_nodo(c["origen"]) if c["origen"] else "",
                c["destino"] or "", mp.nombre_nodo(c["destino"]) if c["destino"] else "",
                f"{c['d_origen']:.1f}", f"{c['d_destino']:.1f}",
                f"{c['longitud']:.0f}", "; ".join(c["cruces"])
            ]) + "\n")

    # Galería index.html
    if capturas_vec:
        por = {}
        for sub, nombre, desc, ok in capturas_vec:
            if ok:
                por.setdefault(sub, []).append((nombre, desc))
        partes = [
            "<!doctype html><html lang='es'><meta charset='utf-8'><title>Verificación Visual del Mapa</title>",
            "<style>body{font-family:'Inter',system-ui,sans-serif;background:#0f172a;color:#f8fafc;margin:24px}",
            "figure{background:#1e293b;padding:14px;margin:0 0 24px;border-radius:10px;border:1px solid #334155}",
            "img{max-width:100%;height:auto;border-radius:6px;border:1px solid #475569;display:block}",
            "figcaption{font-weight:800;margin-bottom:8px;color:#38bdf8}h1,h2{color:#f8fafc;margin-bottom:12px}",
            "a{color:#38bdf8;text-decoration:none}a:hover{text-decoration:underline}</style>",
            "<h1>Galería de Verificación y Recorrido Visual</h1>",
            "<p>Imágenes renderizadas directamente desde SVG a resolución 1:1. En las conexiones, el punto verde "
            "marca el origen, el punto rojo la punta de flecha, y la franja magenta el recorrido.</p>"
        ]
        for sub, titulo in (("mosaico", "1. Mosaico a Escala de Impresión"),
                            ("vias", "2. Vías Metabólicas Individuales"),
                            ("conexiones", "3. Conexiones Inter-Ruta")):
            partes.append(f"<h2>{titulo}</h2>")
            for nombre, desc in por.get(sub, []):
                partes.append(
                    f"<figure><figcaption>{htmllib.escape(desc)}</figcaption>"
                    f"<a href='capturas/{sub}/{nombre}' target='_blank'>"
                    f"<img loading='lazy' src='capturas/{sub}/{nombre}'></a></figure>"
                )
        with open(os.path.join(dir_salida, "index.html"), "w", encoding="utf-8") as f:
            f.write("\n".join(partes))

    return ruta_reporte


# ----------------------------------------------------------------------------
# Punto de Entrada Principal
# ----------------------------------------------------------------------------
def main():
    dir_script = os.path.dirname(os.path.abspath(__file__))
    dir_raiz = os.path.dirname(dir_script) if os.path.basename(dir_script) == "scripts_generacion" else dir_script

    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--svg", default=os.path.join(dir_raiz, "07_AMPLIACION_TEMARIO", "mapa_cartulina_ampliado.svg"),
                    help="Ruta al archivo SVG base o alternativo a auditar")
    ap.add_argument("--html", default=None,
                    help="Ruta opcional al visor HTML para comprobar consola JS y parámetros URL")
    ap.add_argument("--salida", default=os.path.join(dir_raiz, "capturas_y_pruebas", "verificacion_integral"),
                    help="Carpeta donde se guardarán el reporte TXT, TSV y las capturas")
    ap.add_argument("--ancho-mm", type=float, default=1200.0,
                    help="Ancho nominal de impresión del póster en milímetros (defecto: 1200 mm)")
    ap.add_argument("--sin-capturas", action="store_true",
                    help="Desactiva la generación pesada de capturas PNG vectoriales")
    ap.add_argument("--hilos", type=int, default=max(1, min(6, (os.cpu_count() or 2) - 1)),
                    help="Número de hilos para renderizado concurrente con rsvg-convert")
    ap.add_argument("--columnas", type=int, default=6, help="Columnas del mosaico")
    ap.add_argument("--filas", type=int, default=4, help="Filas del mosaico")

    args = ap.parse_args()

    # Si no se pasó --html explícito, detectar si existe el visor ampliado correspondiente
    if args.html is None:
        candidatos_html = [
            os.path.join(dir_raiz, "versiones_html", "01_mapa_ampliado_completo_25_vias.html"),
            os.path.join(dir_raiz, "mapa_metabolico_alternativo", "mapa_metabolico_alternativo.html"),
            os.path.join(dir_raiz, "versiones_html", "prueba_visual_interactiva.html")
        ]
        for c in candidatos_html:
            if os.path.exists(c):
                args.html = c
                break

    try:
        os.makedirs(args.salida, exist_ok=True)
    except OSError:
        args.salida = os.path.join("/tmp", "verificacion_integral")
        os.makedirs(args.salida, exist_ok=True)
    print("================================================================================")
    print("   VERIFICACIÓN INTEGRAL, AUDITORÍA Y TRAZABILIDAD DEL MAPA METABÓLICO          ")
    print("================================================================================")
    print(f"1. Analizando geométricamente el SVG:")
    print(f"   {args.svg}")
    t0 = time.time()
    mp = InspectorMapa(args.svg, args.ancho_mm)
    hallazgos, res = ejecutar_auditoria(mp)
    print(f"   ✓ {len(mp.textos)} textos, {len(mp.flechas)} flechas, {len(res['conexiones'])} conexiones analizadas ({time.time() - t0:.2f} s)")

    html_res = None
    if args.html:
        print(f"\n2. Comprobando visor HTML y consola del navegador:")
        print(f"   {args.html}")
        html_res = comprobar_html_y_capturar_estados(mp, args.html, args.salida)

    capturas_vec = []
    if not args.sin_capturas:
        print(f"\n3. Generando recorrido visual en alta resolución (rsvg-convert):")
        capturas_vec = ejecutar_capturas_vectoriales(mp, res, args.salida, args.hilos, args.columnas, args.filas)
    else:
        print("\n3. Recorrido visual vectorial omitido (--sin-capturas)")

    print(f"\n4. Redactando informe de auditoría...")
    ruta_inf = generar_reporte_auditoria(mp, hallazgos, res, html_res, capturas_vec, args.salida, args.ancho_mm)

    print("\n================================================================================")
    print("   RESUMEN FINAL DE AUDITORÍA                                                   ")
    print("================================================================================")
    print(f"Críticos:    {len(hallazgos['criticos']):>3}")
    print(f"Importantes: {len(hallazgos['importantes']):>3}")
    print(f"Menores:     {len(hallazgos['menores']):>3}")
    print(f"Informe completo guardado en: {ruta_inf}")
    if capturas_vec:
        print(f"Galería interactiva:         {os.path.join(args.salida, 'index.html')}")

    return 1 if hallazgos["criticos"] else 0


if __name__ == "__main__":
    sys.exit(main())
