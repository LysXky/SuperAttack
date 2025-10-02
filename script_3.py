# Crear también una versión de ejemplo/demo para mostrar el funcionamiento
demo_script = '''# DEMO DEL ANALIZADOR DE SUBDOMINIOS
# Este es un ejemplo de cómo se vería la salida del script

import time

def demo_execution():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    ANALIZADOR DE SUBDOMINIOS                 ║
    ║                     Script de Reconocimiento                 ║  
    ║                          v1.0                               ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    print("=== CONFIGURACIÓN DE DOMINIOS ===")
    print("\\nDominios cargados: 0")
    print("\\nIngrese un dominio para analizar (o 'fin' para terminar): example.com")
    print("✓ Dominio 'example.com' agregado correctamente")
    
    print("\\nDominios cargados: 1")
    print("Dominios actuales: example.com")
    print("\\nIngrese un dominio para analizar (o 'fin' para terminar): fin")
    
    print("\\n🚀 Iniciando análisis de 1 dominio(s)...")
    print("⚠️  Este proceso puede tomar varios minutos por dominio...")
    
    print("\\n🔍 Analizando dominio: example.com")
    print("=" * 60)
    print("📋 Verificando 64 subdominios potenciales...")
    
    # Simular algunos resultados
    subdomains_found = [
        {"subdomain": "www.example.com", "ports": "80;443"},
        {"subdomain": "mail.example.com", "ports": "25;110;143;993;995"},
        {"subdomain": "ftp.example.com", "ports": "21;22"},
        {"subdomain": "api.example.com", "ports": "80;443;8080"}
    ]
    
    for i in range(1, 65):
        subdomain = f"test{i}.example.com" if i > 4 else ["www.example.com", "mail.example.com", "ftp.example.com", "api.example.com"][i-1]
        print(f"\\rProgreso: {i:2d}/64 - Verificando: {subdomain:<40}", end="", flush=True)
        time.sleep(0.1)  # Simular tiempo de verificación
        
        if i <= 4:  # Solo los primeros 4 "existen"
            print(f"\\n   ✓ DNS encontrado para {subdomain}")
            print(f"   🔍 Escaneando puertos para {subdomain}...")
            ports = subdomains_found[i-1]["ports"]
            print(f"   ✅ {subdomain} - Puertos abiertos: {ports}")
    
    print("\\n\\n✅ Análisis completado para example.com")
    print("📊 Subdominios encontrados: 4")
    
    print("💾 Archivo CSV guardado: subdominios_example_com.csv")
    
    print("""
    📋 RESUMEN PARA EXAMPLE.COM:
    ═══════════════════════════════════════════════════════════════
    🔢 Subdominios encontrados: 4
    🔌 Puertos encontrados en los distintos sitios: 21;22;25;80;110;143;443;993;995;8080
    
    📊 DETALLES POR SUBDOMINIO:
    
        • www.example.com
          └─ Puertos: 80;443
          └─ HTTP: Sí (https)
    
        • mail.example.com
          └─ Puertos: 25;110;143;993;995
          └─ HTTP: No (N/A)
    
        • ftp.example.com
          └─ Puertos: 21;22
          └─ HTTP: No (N/A)
    
        • api.example.com
          └─ Puertos: 80;443;8080
          └─ HTTP: Sí (https)
    """)
    
    print("\\n" + "="*80)
    
    print("\\n🎉 ANÁLISIS COMPLETADO")
    print("═══════════════════════════════════════════════════════════════")
    print("📁 Archivos CSV generados: 1")
    print("   • subdominios_example_com.csv")
    print("📊 Total de subdominios encontrados: 4")

if __name__ == "__main__":
    demo_execution()
'''

# Guardar el demo
with open('demo_analizador.py', 'w', encoding='utf-8') as f:
    f.write(demo_script)

print("✅ Archivo de demostración 'demo_analizador.py' creado")
print("\n🎬 Para ver cómo funciona el script, ejecute: python demo_analizador.py")