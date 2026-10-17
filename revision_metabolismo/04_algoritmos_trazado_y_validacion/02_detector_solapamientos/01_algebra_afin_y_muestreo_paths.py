# =============================================================================
# MÓDULO DE REVISIÓN: Álgebra Afín 2D y Muestreo de Curvas SVG
# =============================================================================
# Archivo original : scripts_generacion/detectar_solapamientos.py (líneas 1 a 247 de 552)
# Descripción      : Multiplicación de matrices SVG, parser de atributos transform y discretización de comandos path (M, L, C, Q, A).
# =============================================================================

#!/usr/bin/env python3
"""
DETECTOR AUTOMÁTICO DE SOLAPAMIENTOS EN EL SVG DEL MAPA
========================================================
Analiza prueba_visual_integrada.svg (sin navegador) y reporta:
  1. TEXTO-TEXTO   : dos rótulos que se pisan.
  2. FLECHA-TEXTO  : una flecha / conector que atraviesa un rótulo.
  3. TEXTO-ESTRUC. : un rótulo que cae encima del dibujo de una molécula.
  4. FLECHA-ESTRUC.: una flecha que atraviesa una molécula (sin contar sus extremos).

El ancho del texto se estima (≈0.6·font-size por carácter), por lo que puede
haber algún falso positivo leve. Genera también un SVG de control con los
problemas marcados en rojo:  solapamientos_debug.svg

Uso:
    python3 detectar_solapamientos.py [archivo.svg] [--debug] [--max N]
"""
import math
import os
import re
import sys
import xml.etree.ElementTree as ET

NS = "{http://www.w3.org/2000/svg}"

# Grupos que no se analizan (decorado de fondo o insertos con diseño propio cerrado)
GRUPOS_EXCLUIDOS = {
    "mitocondria_biologica", "eritrocitos_torrente", "musculo_esqueletico_biologico", "sistema_vascular_extrahepatico",
}
# Dentro de estos grupos sólo se comprueba su propio contorno, no su interior
GRUPOS_INSERTO = {
    "lupa_cadena_respiratoria",
    "lupa_piruvato_deshidrogenasa",
    "lupa_lanzadera_malato_aspartato",
    "lupa_lanzadera_glicerol_p",
}

ANCHO_CHAR = {"mono": 0.62, "sans": 0.60}


# --------------------------------------------------------------------------
# Álgebra afín
# --------------------------------------------------------------------------
def mat_mul(a, b):
    return (
        a[0] * b[0] + a[2] * b[1], a[1] * b[0] + a[3] * b[1],
        a[0] * b[2] + a[2] * b[3], a[1] * b[2] + a[3] * b[3],
        a[0] * b[4] + a[2] * b[5] + a[4], a[1] * b[4] + a[3] * b[5] + a[5],
    )


def aplicar(m, x, y):
    return (m[0] * x + m[2] * y + m[4], m[1] * x + m[3] * y + m[5])


IDENT = (1, 0, 0, 1, 0, 0)


def parse_transform(t):
    m = IDENT
    if not t:
        return m
    for nombre, args in re.findall(r"(\w+)\s*\(([^)]*)\)", t):
        v = [float(n) for n in re.findall(r"-?[\d.]+(?:e-?\d+)?", args)]
        if nombre == "translate":
            mm = (1, 0, 0, 1, v[0], v[1] if len(v) > 1 else 0)
        elif nombre == "scale":
            sx = v[0]
            sy = v[1] if len(v) > 1 else sx
            mm = (sx, 0, 0, sy, 0, 0)
        elif nombre == "rotate":
            a = math.radians(v[0])
            c, s = math.cos(a), math.sin(a)
            r = (c, s, -s, c, 0, 0)
            if len(v) == 3:
                cx, cy = v[1], v[2]
                mm = mat_mul(mat_mul((1, 0, 0, 1, cx, cy), r), (1, 0, 0, 1, -cx, -cy))
            else:
                mm = r
        elif nombre == "matrix":
            mm = tuple(v[:6])
        else:
            continue
        m = mat_mul(m, mm)
    return m


# --------------------------------------------------------------------------
# Geometría de paths
# --------------------------------------------------------------------------
def tokens_path(d):
    for cmd, args in re.findall(r"([MmLlHhVvCcSsQqTtAaZz])([^MmLlHhVvCcSsQqTtAaZz]*)", d):
        yield cmd, [float(n) for n in re.findall(r"-?\d*\.?\d+(?:e-?\d+)?", args)]


def bezier(p0, p1, p2, p3, n=10):
    pts = []
    for i in range(1, n + 1):
        t = i / n
        u = 1 - t
        pts.append((
            u ** 3 * p0[0] + 3 * u * u * t * p1[0] + 3 * u * t * t * p2[0] + t ** 3 * p3[0],
            u ** 3 * p0[1] + 3 * u * u * t * p1[1] + 3 * u * t * t * p2[1] + t ** 3 * p3[1],
        ))
    return pts


def puntos_path(d):
    """Devuelve lista de polilíneas (listas de puntos) aproximando el path."""
    polis, actual = [], []
    x = y = 0.0
    sx = sy = 0.0
    last_ctrl = None
    for cmd, v in tokens_path(d):
        rel = cmd.islower()
        c = cmd.upper()
        if c == "Z":
            if actual:
                actual.append((sx, sy))
            x, y = sx, sy
            continue
        i = 0
        while True:
            if c == "M":
                if i + 2 > len(v):
                    break
                nx, ny = v[i], v[i + 1]
                if rel:
                    nx, ny = x + nx, y + ny
                if actual:
                    polis.append(actual)
                actual = [(nx, ny)]
                x, y, sx, sy = nx, ny, nx, ny
                i += 2
                c = "L"  # pares siguientes son L implícitos
                last_ctrl = None
            elif c == "L":
                if i + 2 > len(v):
                    break
                nx, ny = v[i], v[i + 1]
                if rel:
                    nx, ny = x + nx, y + ny
                actual.append((nx, ny))
                x, y = nx, ny
                i += 2
                last_ctrl = None
            elif c == "H":
                if i + 1 > len(v):
                    break
                x = x + v[i] if rel else v[i]
                actual.append((x, y))
                i += 1
            elif c == "V":
                if i + 1 > len(v):
                    break
                y = y + v[i] if rel else v[i]
                actual.append((x, y))
                i += 1
            elif c == "C":
                if i + 6 > len(v):
                    break
                p = v[i:i + 6]
                if rel:
                    p = [p[0] + x, p[1] + y, p[2] + x, p[3] + y, p[4] + x, p[5] + y]
                actual += bezier((x, y), (p[0], p[1]), (p[2], p[3]), (p[4], p[5]))
                last_ctrl = (p[2], p[3])
                x, y = p[4], p[5]
                i += 6
            elif c == "S":
                if i + 4 > len(v):
                    break
                p = v[i:i + 4]
                if rel:
                    p = [p[0] + x, p[1] + y, p[2] + x, p[3] + y]
                c1 = (2 * x - last_ctrl[0], 2 * y - last_ctrl[1]) if last_ctrl else (x, y)
                actual += bezier((x, y), c1, (p[0], p[1]), (p[2], p[3]))
                last_ctrl = (p[0], p[1])
                x, y = p[2], p[3]
                i += 4
            elif c == "Q":
                if i + 4 > len(v):
                    break
                p = v[i:i + 4]
                if rel:
                    p = [p[0] + x, p[1] + y, p[2] + x, p[3] + y]
                c1 = (x + 2 / 3 * (p[0] - x), y + 2 / 3 * (p[1] - y))
                c2 = (p[2] + 2 / 3 * (p[0] - p[2]), p[3] + 2 / 3 * (p[1] - p[3]))
                actual += bezier((x, y), c1, c2, (p[2], p[3]))
                last_ctrl = (p[0], p[1])
                x, y = p[2], p[3]
                i += 4
            elif c == "T":
                if i + 2 > len(v):
                    break
                q = (2 * x - last_ctrl[0], 2 * y - last_ctrl[1]) if last_ctrl else (x, y)
                nx, ny = v[i], v[i + 1]
                if rel:
                    nx, ny = x + nx, y + ny
                c1 = (x + 2 / 3 * (q[0] - x), y + 2 / 3 * (q[1] - y))
                c2 = (nx + 2 / 3 * (q[0] - nx), ny + 2 / 3 * (q[1] - ny))
                actual += bezier((x, y), c1, c2, (nx, ny))
                last_ctrl = q
                x, y = nx, ny
                i += 2
            elif c == "A":
                if i + 7 > len(v):
                    break
                nx, ny = v[i + 5], v[i + 6]
                if rel:
                    nx, ny = x + nx, y + ny
                actual.append((nx, ny))
                x, y = nx, ny
                i += 7
            else:
                break
            if i >= len(v):
                break
    if actual:
        polis.append(actual)
    return polis


# --------------------------------------------------------------------------
# Recorrido del árbol
# --------------------------------------------------------------------------
class Elem:
    __slots__ = ("tipo", "bbox", "texto", "segs", "grupo_mol", "nodo", "ruta", "es_flecha", "inserto")


def heredado(attrs_stack, clave, defecto=None):
    for a in reversed(attrs_stack):
        if clave in a:
            return a[clave]
    return defecto


def estilo(el):
    d = dict(el.attrib)
    st = el.get("style")
    if st:
        for par in st.split(";"):
            if ":" in par:
                k, v = par.split(":", 1)
                d[k.strip()] = v.strip()
    return d


