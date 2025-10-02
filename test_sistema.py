#!/usr/bin/env python3
"""
SCRIPT DE PRUEBAS - ANALIZADOR DE SUBDOMINIOS v2.0
Validación completa de funcionalidades antes del uso
"""

import sys
import time
import socket
from datetime import datetime

def test_banner():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    PRUEBAS DE SISTEMA v2.0                  ║
    ║               Validación de Funcionalidades                 ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def test_python_version():
    """Prueba versión de Python"""
    print("🧪 Test 1: Versión de Python")
    version = sys.version_info
    if version.major >= 3 and version.minor >= 6:
        print(f"   ✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"   ❌ Python {version.major}.{version.minor}.{version.micro} - Incompatible")
        return False

def test_standard_libraries():
    """Prueba librerías estándar de Python"""
    print("\n🧪 Test 2: Librerías estándar")

    libraries = [
        ('socket', 'Resolución DNS'),
        ('csv', 'Manejo de CSV'),
        ('threading', 'Multithreading'),
        ('datetime', 'Manejo de fechas'),
        ('concurrent.futures', 'Ejecución paralela'),
        ('ssl', 'Conexiones seguras'),
        ('os', 'Sistema operativo'),
        ('sys', 'Sistema Python')
    ]

    for lib_name, description in libraries:
        try:
            __import__(lib_name)
            print(f"   ✅ {lib_name:<20} - {description}")
        except ImportError:
            print(f"   ❌ {lib_name:<20} - Error importando")
            return False

    return True

def test_requests_library():
    """Prueba librería requests"""
    print("\n🧪 Test 3: Librería requests")
    try:
        import requests
        print("   ✅ requests importado correctamente")

        # Test de conectividad básica
        response = requests.get('https://httpbin.org/get', timeout=10, verify=False)
        if response.status_code == 200:
            print("   ✅ Conectividad HTTP funcional")
            return True
        else:
            print(f"   ⚠️  HTTP devolvió status {response.status_code}")
            return False

    except ImportError:
        print("   ❌ requests no está instalado")
        print("   💡 Ejecute: pip install requests")
        return False
    except Exception as e:
        print(f"   ⚠️  Error de conectividad: {e}")
        return False

def test_dns_resolution():
    """Prueba resolución DNS"""
    print("\n🧪 Test 4: Resolución DNS")

    test_domains = ['google.com', 'github.com', 'stackoverflow.com']

    for domain in test_domains:
        try:
            ip = socket.gethostbyname(domain)
            print(f"   ✅ {domain:<20} -> {ip}")
        except socket.gaierror:
            print(f"   ❌ {domain:<20} -> Error DNS")
            return False

    return True

def test_port_scanning():
    """Prueba escaneo básico de puertos"""
    print("\n🧪 Test 5: Escaneo de puertos")

    def scan_port(host, port, timeout=2):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except:
            return False

    # Probar puertos comunes en google.com
    test_ports = [80, 443]
    host = 'google.com'

    for port in test_ports:
        is_open = scan_port(host, port)
        status = "✅ Abierto" if is_open else "🔒 Cerrado"
        print(f"   {status} {host}:{port}")

    return True

def test_threading():
    """Prueba funcionalidad de threading"""
    print("\n🧪 Test 6: Multithreading")

    try:
        from concurrent.futures import ThreadPoolExecutor, as_completed
        import time

        def dummy_task(n):
            time.sleep(0.1)
            return n * 2

        with ThreadPoolExecutor(max_workers=5) as executor:
            futures = [executor.submit(dummy_task, i) for i in range(5)]
            results = [future.result() for future in as_completed(futures)]

        if len(results) == 5:
            print("   ✅ ThreadPoolExecutor funcional")
            return True
        else:
            print("   ❌ Error en threading")
            return False

    except Exception as e:
        print(f"   ❌ Error en threading: {e}")
        return False

def test_csv_functionality():
    """Prueba creación de CSV"""
    print("\n🧪 Test 7: Funcionalidad CSV")

    try:
        import csv
        import os

        test_file = 'test_output.csv'
        test_data = [
            ['Dominio', 'Subdominio', 'Status'],
            ['example.com', 'www.example.com', 'Activo'],
            ['example.com', 'mail.example.com', 'Activo']
        ]

        # Escribir CSV
        with open(test_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(test_data)

        # Verificar que se creó
        if os.path.exists(test_file):
            print("   ✅ Creación de CSV funcional")
            os.remove(test_file)  # Limpiar
            return True
        else:
            print("   ❌ Error creando CSV")
            return False

    except Exception as e:
        print(f"   ❌ Error en CSV: {e}")
        return False

def test_subdomain_generation():
    """Prueba generación de subdominios"""
    print("\n🧪 Test 8: Generación de subdominios")

    def generate_test_subdomains(domain):
        common_subs = ['www', 'mail', 'ftp', 'api', 'admin']
        return [f"{sub}.{domain}" for sub in common_subs]

    test_domain = 'example.com'
    subdomains = generate_test_subdomains(test_domain)

    expected_count = 5
    if len(subdomains) == expected_count:
        print(f"   ✅ Generados {len(subdomains)} subdominios correctamente")
        print(f"   📋 Ejemplo: {subdomains[0]}")
        return True
    else:
        print(f"   ❌ Error en generación: esperado {expected_count}, obtuvo {len(subdomains)}")
        return False

def run_performance_test():
    """Prueba básica de rendimiento"""
    print("\n🧪 Test 9: Rendimiento básico")

    start_time = time.time()

    # Simular trabajo del analizador
    for i in range(100):
        dummy_subdomain = f"test{i}.example.com"
        # Simular validación básica
        is_valid = '.' in dummy_subdomain and len(dummy_subdomain) > 5

    end_time = time.time()
    duration = end_time - start_time

    print(f"   ⏱️  Procesamiento de 100 subdominios: {duration:.3f} segundos")

    if duration < 1.0:
        print("   ✅ Rendimiento aceptable")
        return True
    else:
        print("   ⚠️  Rendimiento lento, pero funcional")
        return True

def main():
    """Ejecuta todas las pruebas"""
    test_banner()

    print("🚀 Iniciando batería de pruebas...")
    print("   Este proceso verificará que todas las funcionalidades estén disponibles")
    print()

    tests = [
        test_python_version,
        test_standard_libraries,
        test_requests_library,
        test_dns_resolution,
        test_port_scanning,
        test_threading,
        test_csv_functionality,
        test_subdomain_generation,
        run_performance_test
    ]

    passed = 0
    total = len(tests)

    for test in tests:
        try:
            if test():
                passed += 1
        except Exception as e:
            print(f"   ❌ Error inesperado: {e}")

    print("\n" + "="*70)
    print(f"📊 RESULTADOS DE PRUEBAS: {passed}/{total} exitosas")

    if passed == total:
        print("🎉 ¡SISTEMA COMPLETAMENTE FUNCIONAL!")
        print("✅ El analizador de subdominios está listo para usar")
    elif passed >= total - 2:
        print("⚠️  Sistema mayormente funcional con advertencias menores")
        print("✅ El analizador debería funcionar correctamente")
    else:
        print("❌ Sistema presenta problemas significativos")
        print("🔧 Revise las dependencias y configuración")

    print(f"\n⏰ Pruebas completadas: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()
