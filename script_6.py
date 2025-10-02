# Crear un script de instalación automática para facilitar el setup
installer_script = '''#!/usr/bin/env python3
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
    
    print("\\n📦 Instalando dependencias...")
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
    print("\\n🧪 Verificando instalación...")
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
    config_content = '''# CONFIGURACIÓN DEL ANALIZADOR DE SUBDOMINIOS
# Modifique estos valores según sus necesidades

# Configuración de timeouts (en segundos)
DNS_TIMEOUT = 5
HTTP_TIMEOUT = 5
PORT_TIMEOUT = 2

# Configuración de paralelización
MAX_WORKERS_PORTS = 30
MAX_WORKERS_SUBDOMAINS = 10

# Servidores DNS a utilizar
DNS_SERVERS = ["8.8.8.8", "8.8.4.4", "1.1.1.1"]

# Puertos adicionales a escanear (opcional)
CUSTOM_PORTS = []

# Subdominios adicionales (opcional)
CUSTOM_SUBDOMAINS = []
'''
    
    try:
        with open('config_analizador.py', 'w', encoding='utf-8') as f:
            f.write(config_content)
        print("📝 Archivo de configuración creado: config_analizador.py")
        return True
    except Exception as e:
        print(f"⚠️  No se pudo crear el archivo de configuración: {e}")
        return False

def main():
    """Función principal del instalador"""
    print_banner()
    
    # Verificar Python
    if not check_python_version():
        print("\\n❌ Instalación cancelada: Versión de Python incompatible")
        sys.exit(1)
    
    # Instalar dependencias
    if not install_dependencies():
        print("\\n❌ Instalación cancelada: Error instalando dependencias")
        sys.exit(1)
    
    # Verificar instalación
    if not verify_installation():
        print("\\n❌ Instalación cancelada: Error en verificación")
        sys.exit(1)
    
    # Crear configuración
    create_config_file()
    
    # Mostrar instrucciones finales
    print("""
    🎉 ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!
    ═══════════════════════════════════════════════════════════════
    
    📋 ARCHIVOS DISPONIBLES:
    • analizador_subdominios.py    - Script principal
    • demo_analizador.py          - Demostración de funcionamiento  
    • config_analizador.py        - Configuración personalizable
    • DOCUMENTACION_ANALIZADOR.md - Documentación técnica completa
    
    🚀 PARA COMENZAR:
    python analizador_subdominios.py
    
    📖 PARA VER DEMO:
    python demo_analizador.py
    
    ⚠️  RECORDATORIO DE SEGURIDAD:
    Use este script únicamente en dominios propios o con autorización explícita.
    El uso no autorizado puede violar términos de servicio o leyes locales.
    """)

if __name__ == "__main__":
    main()
'''

# Guardar el instalador
with open('install.py', 'w', encoding='utf-8') as f:
    f.write(installer_script)

print("✅ Script de instalación creado: 'install.py'")
print("\n🔧 Para configurar todo automáticamente, ejecute:")
print("python install.py")

# Crear un README.md simple
readme_content = """# Analizador de Subdominios v1.0

Script profesional de enumeración de subdominios y escaneo de puertos para especialistas en ciberseguridad.

## 🚀 Instalación Rápida
```bash
python install.py
```

## 📋 Uso Básico
```bash
python analizador_subdominios.py
```

## 📁 Archivos Incluidos
- `analizador_subdominios.py` - Script principal
- `demo_analizador.py` - Demostración  
- `install.py` - Instalador automático
- `DOCUMENTACION_ANALIZADOR.md` - Documentación completa

## ⚠️ Uso Responsable
Este script debe usarse únicamente en dominios propios o con autorización explícita.

## 🔧 Características
- Enumeración de 64 subdominios comunes
- Escaneo de 33 puertos críticos
- Ejecución paralela optimizada
- Generación de CSV por dominio
- Resúmenes detallados automáticos

## 📊 Salida
Cada dominio analizado genera:
- CSV con subdominios encontrados
- Lista de puertos abiertos por subdominio
- Resumen estadístico en consola

---
**Desarrollado por:** Especialista Cloud Security  
**Versión:** 1.0  
**Fecha:** Octubre 2025
"""

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_content)

print("✅ README.md creado con instrucciones básicas")

print("""
🎯 RESUMEN DE ARCHIVOS GENERADOS:
═══════════════════════════════════════════════════════════════
📜 analizador_subdominios.py       - Script principal ejecutable
🎬 demo_analizador.py             - Demostración del funcionamiento
🔧 install.py                     - Instalador automático de dependencias  
📖 DOCUMENTACION_ANALIZADOR.md    - Documentación técnica completa
📋 README.md                      - Guía de inicio rápido
📊 ejemplo_subdominios_example_com.csv - Ejemplo de salida CSV
⚙️  config_analizador.py          - Se crea al ejecutar install.py

🚀 PRÓXIMOS PASOS:
1. Ejecutar: python install.py (para instalar dependencias)
2. Ejecutar: python analizador_subdominios.py (para usar el script)
3. O ejecutar: python demo_analizador.py (para ver demo)
""")