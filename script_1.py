# Instalar las dependencias necesarias
import subprocess
import sys

def install_package(package):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✓ {package} instalado correctamente")
    except Exception as e:
        print(f"❌ Error instalando {package}: {e}")

# Instalar dependencias
print("📦 Instalando dependencias necesarias...")
install_package("dnspython")
install_package("requests")
print("✅ Dependencias instaladas")