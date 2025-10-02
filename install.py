#!/usr/bin/env python3
"""
INSTALADOR AUTOMÁTICO - ANALIZADOR DE SUBDOMINIOS
Script de configuración automática para el entorno de análisis
"""

import subprocess
import sys
import os

def print_banner():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                 INSTALADOR AUTOMÁTICO                        ║
    ║               Analizador de Subdominios v1.0                ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def check_python_version():
    """Verifica la versión de Python"""
    print("🔍 Verificando versión de Python...")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 6:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Se requiere Python 3.6+")
        return False

def install_dependencies():
    """Instala las dependencias necesarias"""
    dependencies = ['dnspython', 'requests']

    print("\n📦 Instalando dependencias...")
    for dep in dependencies:
        try:
            print(f"   Instalando {dep}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", dep], 
                                stdout=subprocess.DEVNULL, 
                                stderr=subprocess.DEVNULL)
            print(f"   ✅ {dep} instalado correctamente")
        except subprocess.CalledProcessError:
            print(f"   ❌ Error instalando {dep}")
            return False
    return True

def verify_installation():
    """Verifica que las dependencias se instalaron correctamente"""
    print("\n🧪 Verificando instalación...")
    try:
        import dns.resolver
        import requests
        print("✅ Todas las dependencias verificadas correctamente")
        return True
    except ImportError as e:
        print(f"❌ Error en la verificación: {e}")
        return False

def create_config_file():
    """Crea archivo de configuración opcional"""
    config_content = 