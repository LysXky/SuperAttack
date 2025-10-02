import socket
import csv
import dns.resolver
import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
import ssl
import sys
import warnings

# Suprimir warnings de SSL
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

def banner():
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    ANALIZADOR DE SUBDOMINIOS                 ║
    ║                     Script de Reconocimiento                 ║  
    ║                          v1.0                               ║
    ╚══════════════════════════════════════════════════════════════╝
    """)

def get_domains_from_user():
    """Solicita al usuario los dominios a analizar"""
    print("=== CONFIGURACIÓN DE DOMINIOS ===")
    domains = []

    while True:
        print(f"\nDominios cargados: {len(domains)}")
        if domains:
            print("Dominios actuales:", ", ".join(domains))

        domain = input("\nIngrese un dominio para analizar (o 'fin' para terminar): ").strip()

        if domain.lower() == 'fin':
            break

        if domain and '.' in domain:
            # Limpiar el dominio
            domain = domain.replace('http://', '').replace('https://', '').replace('www.', '')
            domain = domain.split('/')[0]  # Remover cualquier path
            domains.append(domain)
            print(f"✓ Dominio '{domain}' agregado correctamente")
        else:
            print("❌ Formato de dominio inválido. Intente nuevamente.")

    return domains

def generate_subdomains(domain):
    """Genera lista de subdominios comunes para probar"""
    common_subdomains = [
        'www', 'mail', 'ftp', 'localhost', 'webmail', 'smtp', 'pop', 'ns1', 'webdisk',
        'ns2', 'cpanel', 'whm', 'autodiscover', 'autoconfig', 'test', 'api', 'admin',
        'blog', 'dev', 'staging', 'secure', 'cdn', 'support', 'shop', 'app', 'beta',
        'forum', 'store', 'mobile', 'wiki', 'cloud', 'demo', 'server', 'vpn', 'dns',
        'remote', 'backup', 'portal', 'crm', 'erp', 'mysql', 'sql', 'db', 'database',
        'prometheus', 'grafana', 'jenkins', 'git', 'svn', 'phpmyadmin', 'webmin',
        'monitoring', 'stats', 'status', 'analytics', 'mx', 'mx1', 'mx2', 'imap',
        'upload', 'download', 'files', 'news', 'media', 'images', 'img', 'video',
        'videos', 'stream', 'live', 'chat', 'support', 'help', 'docs', 'documentation',
        'old', 'new', 'legacy', 'v1', 'v2', 'internal', 'intranet', 'extranet',
        'staging', 'production', 'prod', 'stage', 'qa', 'uat', 'sandbox'
    ]

    return [f"{sub}.{domain}" for sub in common_subdomains]

def check_subdomain_dns(subdomain):
    """Verifica si el subdominio existe via DNS"""
    try:
        dns.resolver.resolve(subdomain, 'A')
        return True
    except:
        try:
            dns.resolver.resolve(subdomain, 'CNAME')
            return True
        except:
            return False

def check_subdomain_http(subdomain):
    """Verifica si el subdominio responde via HTTP/HTTPS"""
    for protocol in ['https', 'http']:
        try:
            response = requests.get(f"{protocol}://{subdomain}", 
                                  timeout=5, 
                                  verify=False,
                                  allow_redirects=True,
                                  headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
            if response.status_code < 400:
                return True, protocol
        except:
            continue
    return False, None

def scan_port(host, port, timeout=2):
    """Escanea un puerto específico"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((host, port))
        sock.close()
        return port if result == 0 else None
    except:
        return None

def scan_common_ports(host, max_workers=30):
    """Escanea puertos comunes de forma paralela"""
    common_ports = [
        21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 443, 993, 995,
        1723, 3306, 3389, 5432, 5900, 8080, 8443, 8888, 9090, 3000, 5000,
        6379, 27017, 1521, 1433, 5984, 6379, 11211, 50000, 50070
    ]

    open_ports = []

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_port = {executor.submit(scan_port, host, port): port for port in common_ports}

        for future in as_completed(future_to_port):
            result = future.result()
            if result:
                open_ports.append(result)

    return sorted(open_ports)

def analyze_domain(domain):
    """Analiza completamente un dominio"""
    print(f"\n🔍 Analizando dominio: {domain}")
    print("=" * 60)

    # Generar subdominios candidatos
    candidate_subdomains = generate_subdomains(domain)
    found_subdomains = []

    print(f"📋 Verificando {len(candidate_subdomains)} subdominios potenciales...")

    # Verificar subdominios
    for i, subdomain in enumerate(candidate_subdomains, 1):
        print(f"\rProgreso: {i:2d}/{len(candidate_subdomains)} - Verificando: {subdomain:<40}", end="", flush=True)

        if check_subdomain_dns(subdomain):
            print(f"\n   ✓ DNS encontrado para {subdomain}")
            http_exists, protocol = check_subdomain_http(subdomain)

            # Escanear puertos
            print(f"   🔍 Escaneando puertos para {subdomain}...")
            open_ports = scan_common_ports(subdomain)

            subdomain_info = {
                'subdomain': subdomain,
                'dns_exists': True,
                'http_accessible': http_exists,
                'protocol': protocol if http_exists else 'N/A',
                'open_ports': open_ports,
                'ports_string': ';'.join(map(str, open_ports)) if open_ports else 'Ninguno'
            }

            found_subdomains.append(subdomain_info)
            print(f"   ✅ {subdomain} - Puertos abiertos: {subdomain_info['ports_string']}")

    print(f"\n\n✅ Análisis completado para {domain}")
    print(f"📊 Subdominios encontrados: {len(found_subdomains)}")

    return found_subdomains

def save_to_csv(domain, subdomains_data):
    """Guarda los resultados en un archivo CSV"""
    filename = f"subdominios_{domain.replace('.', '_')}.csv"

    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Dominio', 'Subdominio', 'DNS_Existe', 'HTTP_Accesible', 'Protocolo', 'Puertos_Abiertos']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for data in subdomains_data:
            writer.writerow({
                'Dominio': domain,
                'Subdominio': data['subdomain'],
                'DNS_Existe': 'Sí' if data['dns_exists'] else 'No',
                'HTTP_Accesible': 'Sí' if data['http_accessible'] else 'No',
                'Protocolo': data['protocol'],
                'Puertos_Abiertos': data['ports_string']
            })

    print(f"💾 Archivo CSV guardado: {filename}")
    return filename

def generate_summary(domain, subdomains_data):
    """Genera un resumen del análisis"""
    total_subdomains = len(subdomains_data)
    all_ports = set()

    for data in subdomains_data:
        all_ports.update(data['open_ports'])

    ports_summary = ';'.join(map(str, sorted(all_ports))) if all_ports else 'Ninguno'

    summary = f"""
    📋 RESUMEN PARA {domain.upper()}:
    ═══════════════════════════════════════════════════════════════
    🔢 Subdominios encontrados: {total_subdomains}
    🔌 Puertos encontrados en los distintos sitios: {ports_summary}

    📊 DETALLES POR SUBDOMINIO:
    """

    for data in subdomains_data:
        summary += f"\n    • {data['subdomain']}"
        summary += f"\n      └─ Puertos: {data['ports_string']}"
        summary += f"\n      └─ HTTP: {'Sí' if data['http_accessible'] else 'No'} ({data['protocol']})"

    return summary

def main():
    """Función principal del script"""
    banner()

    # Configurar DNS resolver
    try:
        dns.resolver.default_resolver = dns.resolver.Resolver(configure=False)
        dns.resolver.default_resolver.nameservers = ['8.8.8.8', '8.8.4.4']
    except:
        pass

    # Obtener dominios del usuario
    domains = get_domains_from_user()

    if not domains:
        print("❌ No se ingresaron dominios válidos. Terminando programa.")
        return

    print(f"\n🚀 Iniciando análisis de {len(domains)} dominio(s)...")
    print("⚠️  Este proceso puede tomar varios minutos por dominio...")

    results = {}
    csv_files = []

    # Analizar cada dominio
    for domain in domains:
        try:
            subdomains_data = analyze_domain(domain)
            results[domain] = subdomains_data

            # Guardar CSV
            csv_file = save_to_csv(domain, subdomains_data)
            csv_files.append(csv_file)

            # Mostrar resumen
            summary = generate_summary(domain, subdomains_data)
            print(summary)
            print("\n" + "="*80 + "\n")

        except Exception as e:
            print(f"❌ Error analizando {domain}: {str(e)}")
            continue

    # Resumen final
    print("🎉 ANÁLISIS COMPLETADO")
    print("═══════════════════════════════════════════════════════════════")
    print(f"📁 Archivos CSV generados: {len(csv_files)}")
    for csv_file in csv_files:
        print(f"   • {csv_file}")

    total_subdomains = sum(len(data) for data in results.values())
    print(f"📊 Total de subdominios encontrados: {total_subdomains}")

if __name__ == "__main__":
    main()
