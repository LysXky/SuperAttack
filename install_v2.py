#!/usr/bin/env python3
"""
INSTALADOR AUTOMÁTICO v2.0 - ANALIZADOR DE SUBDOMINIOS
Script de configuración automática sin dependencias problemáticas
"""

import subprocess
import sys
import os

def print_banner():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                 INSTALADOR AUTOMÁTICO v2.0                  ║
    ║               Analizador de Subdominios Mejorado            ║
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
    """Instala solo las dependencias esenciales"""
    # Solo requests es necesario, sin dnspython problemático
    dependencies = ['requests']

    print("\n📦 Instalando dependencias esenciales...")
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
        import requests
        import socket  # Librería estándar
        import csv     # Librería estándar
        import threading  # Librería estándar
        print("✅ Todas las dependencias verificadas correctamente")
        return True
    except ImportError as e:
        print(f"❌ Error en la verificación: {e}")
        return False

def create_config_file():
    """Crea archivo de configuración mejorado"""
    config_content = """# CONFIGURACIÓN DEL ANALIZADOR DE SUBDOMINIOS v2.0
# Archivo de configuración personalizable

# Configuración de timeouts (en segundos)
DNS_TIMEOUT = 3
HTTP_TIMEOUT = 5
PORT_TIMEOUT = 2

# Configuración de paralelización
MAX_WORKERS_PORTS = 20
MAX_WORKERS_HTTP = 10

# Configuración de red
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
VERIFY_SSL = False
ALLOW_REDIRECTS = True

# Puertos críticos adicionales (se suman a los predefinidos)
ADDITIONAL_PORTS = [
    # Agregar puertos personalizados aquí
    # Ejemplo: 8081, 9000, 9001
]

# Subdominios adicionales (se suman a los predefinidos)
ADDITIONAL_SUBDOMAINS = [
    # Agregar subdominios personalizados aquí
    # Ejemplo: 'custom', 'special', 'internal'
]

# Configuración de salida
TIMESTAMP_FORMAT = '%Y%m%d_%H%M%S'
CSV_ENCODING = 'utf-8'
PROGRESS_UPDATE_FREQUENCY = 1  # Cada cuántos subdominios actualizar progreso
"""

    try:
        with open('config_analizador_v2.py', 'w', encoding='utf-8') as f:
            f.write(config_content)
        print("📝 Archivo de configuración creado: config_analizador_v2.py")
        return True
    except Exception as e:
        print(f"⚠️  No se pudo crear el archivo de configuración: {e}")
        return False

def create_requirements_file():
    """Crea archivo requirements.txt"""
    requirements = """# Dependencias del Analizador de Subdominios v2.0
requests>=2.25.0
"""
    try:
        with open('requirements.txt', 'w', encoding='utf-8') as f:
            f.write(requirements)
        print("📋 Archivo requirements.txt creado")
        return True
    except Exception as e:
        print(f"⚠️  No se pudo crear requirements.txt: {e}")
        return False

def test_basic_functionality():
    """Prueba funcionalidad básica del sistema"""
    print("\n🧪 Probando funcionalidad básica...")

    try:
        # Test de socket
        import socket
        socket.gethostbyname('google.com')
        print("   ✅ Resolución DNS funcional")

        # Test de requests
        import requests
        response = requests.get('https://httpbin.org/get', timeout=5, verify=False)
        if response.status_code == 200:
            print("   ✅ Requests HTTP funcional")

        # Test de threading
        from concurrent.futures import ThreadPoolExecutor
        print("   ✅ Threading funcional")

        return True
    except Exception as e:
        print(f"   ❌ Error en pruebas: {e}")
        return False

def main():
    """Función principal del instalador"""
    print_banner()

    # Verificaciones previas
    if not check_python_version():
        print("\n❌ Instalación cancelada: Versión de Python incompatible")
        sys.exit(1)

    # Instalar dependencias
    if not install_dependencies():
        print("\n❌ Instalación cancelada: Error instalando dependencias")
        sys.exit(1)

    # Verificar instalación
    if not verify_installation():
        print("\n❌ Instalación cancelada: Error en verificación")
        sys.exit(1)

    # Crear archivos de configuración
    create_config_file()
    create_requirements_file()

    # Probar funcionalidad
    if not test_basic_functionality():
        print("\n⚠️  Advertencia: Algunas funcionalidades pueden no estar disponibles")

    # Mostrar instrucciones finales
    print("""
🎉 ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!
═══════════════════════════════════════════════════════════════

📋 ARCHIVOS INSTALADOS:
• analizador_subdominios_v2.py  - Script principal mejorado
• demo_analizador_v2.py         - Demostración funcional
• config_analizador_v2.py       - Configuración personalizable
• requirements.txt              - Lista de dependencias
• install_v2.py                 - Este instalador

🚀 COMANDOS DISPONIBLES:

   Ejecutar análisis real:
   python analizador_subdominios_v2.py

   Ver demostración:
   python demo_analizador_v2.py

   Reinstalar dependencias:
   pip install -r requirements.txt

🔧 PERSONALIZACIÓN:
Edite config_analizador_v2.py para ajustar timeouts, puertos y subdominios.

⚠️  RECORDATORIO DE SEGURIDAD:
Este script debe usarse únicamente en dominios propios o con autorización.
El uso no autorizado puede violar términos de servicio o leyes locales.

🎯 CARACTERÍSTICAS v2.0:
• Sin dependencias problemáticas (solo requests)
• 85+ subdominios predefinidos
• 30+ puertos críticos
• Análisis paralelo optimizado
• CSV con timestamp automático
• Resúmenes ejecutivos detallados
• Manejo robusto de errores
""")

if __name__ == "__main__":
    main()
