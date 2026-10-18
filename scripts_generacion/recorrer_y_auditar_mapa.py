#!/usr/bin/env python3
"""
MÓDULO DE COMPATIBILIDAD
========================
La lógica de recorrido y auditoría del mapa metabólico ha sido consolidada en:
  scripts_generacion/verificar_y_capturar.py

Este script redirige directamente la ejecución al nuevo sistema unificado.
"""
import os
import sys

if __name__ == "__main__":
    dir_script = os.path.dirname(os.path.abspath(__file__))
    script_unificado = os.path.join(dir_script, "verificar_y_capturar.py")
    os.execv(sys.executable, [sys.executable, script_unificado] + sys.argv[1:])
