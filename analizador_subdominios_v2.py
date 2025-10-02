#!/usr/bin/env python3
"""
ANALIZADOR DE SUBDOMINIOS v2.0 - COMPLETO Y PROBADO
Script profesional sin dependencias externas problemáticas
Desarrollado para especialistas en ciberseguridad
"""

import socket
import csv
import requests
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.parse import urlparse
import ssl
import sys
import warnings
import os
from datetime import datetime

# Suprimir warnings de SSL
warnings.filterwarnings('ignore', message='Unverified HTTPS request')

class SubdomainAnalyzer:
    def __init__(self):
        self.results = {}
        self.csv_files = []

    def banner(self):
        print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                    ANALIZADOR DE SUBDOMINIOS v2.0           ║
    ║                  Script de Reconocimiento Profesional       ║
    ║                     Sin Dependencias Externas               ║
    ╚══════════════════════════════════════════════════════════════╝
        """)

    def get_domains_from_user(self):
        """Solicita dominios al usuario con validación mejorada"""
        print("=== CONFIGURACIÓN DE DOMINIOS ===")
        domains = []

        while True:
            print(f"\nDominios cargados: {len(domains)}")
            if domains:
                print("Dominios actuales:", ", ".join(domains))

            domain = input("\nIngrese un dominio para analizar (o 'fin' para terminar): ").strip()

            if domain.lower() in ['fin', 'exit', 'quit']:
                break

            if self.validate_domain(domain):
                clean_domain = self.clean_domain(domain)
                if clean_domain not in domains:
                    domains.append(clean_domain)
                    print(f"✅ Dominio '{clean_domain}' agregado correctamente")
                else:
                    print("⚠️  Dominio ya existe en la lista")
            else:
                print("❌ Formato de dominio inválido. Ejemplo: google.com")

        return domains

    def validate_domain(self, domain):
        """Valida formato básico de dominio"""
        if not domain or len(domain) < 4:
            return False
        if '.' not in domain:
            return False
        if ' ' in domain:
            return False
        return True

    def clean_domain(self, domain):
        """Limpia y normaliza el dominio"""
        domain = domain.lower()
        domain = domain.replace('http://', '').replace('https://', '')
        domain = domain.replace('www.', '')
        domain = domain.split('/')[0]
        domain = domain.split(':')[0]
        return domain

    def generate_subdomains(self, domain):
        """Genera lista extendida de subdominios comunes"""
        common_subdomains = [
            # Web y aplicaciones
            'www', 'app', 'api', 'admin', 'blog', 'shop', 'store', 'portal',
            'dashboard', 'panel', 'control', 'manager', 'console', 'ui',

            # Mail y comunicación
            'mail', 'webmail', 'smtp', 'pop', 'imap', 'mx', 'mx1', 'mx2',
            'email', 'messages', 'chat', 'support', 'help', 'contact',

            # Infraestructura
            'ftp', 'sftp', 'ssh', 'vpn', 'proxy', 'gateway', 'firewall',
            'router', 'switch', 'dns', 'ns1', 'ns2', 'ns3', 'ns4',

            # Servicios técnicos
            'database', 'db', 'mysql', 'postgres', 'redis', 'mongo',
            'elastic', 'search', 'index', 'cache', 'cdn', 'static',

            # Desarrollo y testing
            'dev', 'test', 'stage', 'staging', 'prod', 'production',
            'qa', 'uat', 'demo', 'beta', 'alpha', 'sandbox', 'preview',

            # Monitoreo y analytics
            'monitor', 'monitoring', 'stats', 'analytics', 'metrics',
            'grafana', 'prometheus', 'kibana', 'logs', 'status',

            # Servicios de archivos
            'files', 'download', 'upload', 'share', 'docs', 'media',
            'images', 'img', 'assets', 'resources', 'backup',

            # Versioning y CI/CD
            'git', 'svn', 'jenkins', 'ci', 'build', 'deploy', 'release',
            'v1', 'v2', 'v3', 'api-v1', 'api-v2',

            # Subdominios especiales
            'autodiscover', 'autoconfig', 'cpanel', 'whm', 'webdisk',
            'calendar', 'crm', 'erp', 'wiki', 'forum', 'news',

            # Mobile y API
            'mobile', 'm', 'api-mobile', 'rest', 'graphql', 'webhook',
            'oauth', 'auth', 'sso', 'identity', 'login',

            # Cloud y contenedores
            'cloud', 'aws', 'azure', 'docker', 'k8s', 'kubernetes',
            'rancher', 'nomad', 'consul', 'vault'
        ]

        return [f"{sub}.{domain}" for sub in common_subdomains]

    def check_subdomain_dns(self, subdomain):
        """Verifica existencia del subdominio usando socket nativo"""
        try:
            socket.gethostbyname(subdomain)
            return True
        except (socket.gaierror, socket.timeout):
            return False

    def check_subdomain_http(self, subdomain):
        """Verifica conectividad HTTP/HTTPS del subdominio"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        for protocol in ['https', 'http']:
            try:
                response = requests.get(
                    f"{protocol}://{subdomain}", 
                    timeout=5, 
                    verify=False,
                    allow_redirects=True,
                    headers=headers
                )
                if response.status_code < 400:
                    return True, protocol, response.status_code
            except:
                continue
        return False, None, None

    def scan_port(self, host, port, timeout=2):
        """Escanea un puerto específico"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            return port if result == 0 else None
        except:
            return None

    def scan_common_ports(self, host, max_workers=20):
        """Escanea puertos comunes con optimización"""
        # Puertos más críticos y comunes
        critical_ports = [
            21, 22, 23, 25, 53, 80, 110, 143, 443, 993, 995,  # Básicos
            3306, 5432, 1521, 1433, 27017, 6379,              # Bases de datos
            8080, 8443, 8888, 9090, 3000, 5000,               # Web alternos
            3389, 5900, 1723,                                  # Remotos
            135, 139, 445,                                     # Windows
            111, 2049,                                         # NFS
            11211, 50000, 50070                               # Otros servicios
        ]

        open_ports = []

        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            future_to_port = {
                executor.submit(self.scan_port, host, port): port 
                for port in critical_ports
            }

            for future in as_completed(future_to_port):
                result = future.result()
                if result:
                    open_ports.append(result)

        return sorted(open_ports)

    def analyze_domain(self, domain):
        """Análisis completo de un dominio con progreso detallado"""
        print(f"\n🔍 Analizando dominio: {domain}")
        print("=" * 70)

        candidate_subdomains = self.generate_subdomains(domain)
        found_subdomains = []

        print(f"📋 Verificando {len(candidate_subdomains)} subdominios potenciales...")

        for i, subdomain in enumerate(candidate_subdomains, 1):
            progress = f"[{i:2d}/{len(candidate_subdomains)}]"
            print(f"\r{progress} Verificando: {subdomain:<40}", end="", flush=True)

            # Verificar DNS
            if self.check_subdomain_dns(subdomain):
                print(f"\n   ✅ DNS resuelto: {subdomain}")

                # Verificar HTTP
                http_exists, protocol, status_code = self.check_subdomain_http(subdomain)
                http_info = f"HTTP {status_code} ({protocol})" if http_exists else "No accesible"
                print(f"   🌐 Web: {http_info}")

                # Escanear puertos
                print(f"   🔍 Escaneando puertos...")
                open_ports = self.scan_common_ports(subdomain)
                ports_str = ';'.join(map(str, open_ports)) if open_ports else 'Ninguno'

                subdomain_info = {
                    'subdomain': subdomain,
                    'dns_exists': True,
                    'http_accessible': http_exists,
                    'protocol': protocol if http_exists else 'N/A',
                    'status_code': status_code if http_exists else 'N/A',
                    'open_ports': open_ports,
                    'ports_string': ports_str
                }

                found_subdomains.append(subdomain_info)
                print(f"   🔌 Puertos abiertos: {ports_str}")
                print()

        print(f"\n✅ Análisis completado para {domain}")
        print(f"📊 Subdominios encontrados: {len(found_subdomains)}")

        return found_subdomains

    def save_to_csv(self, domain, subdomains_data):
        """Guarda resultados en CSV con timestamp"""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"subdominios_{domain.replace('.', '_')}_{timestamp}.csv"

        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'Dominio', 'Subdominio', 'DNS_Existe', 'HTTP_Accesible', 
                'Protocolo', 'Status_Code', 'Puertos_Abiertos', 'Timestamp'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for data in subdomains_data:
                writer.writerow({
                    'Dominio': domain,
                    'Subdominio': data['subdomain'],
                    'DNS_Existe': 'Sí' if data['dns_exists'] else 'No',
                    'HTTP_Accesible': 'Sí' if data['http_accessible'] else 'No',
                    'Protocolo': data['protocol'],
                    'Status_Code': data['status_code'],
                    'Puertos_Abiertos': data['ports_string'],
                    'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })

        print(f"💾 CSV guardado: {filename}")
        return filename

    def generate_summary(self, domain, subdomains_data):
        """Genera resumen detallado del análisis"""
        total_subdomains = len(subdomains_data)
        http_accessible = sum(1 for d in subdomains_data if d['http_accessible'])
        all_ports = set()

        for data in subdomains_data:
            all_ports.update(data['open_ports'])

        ports_summary = ';'.join(map(str, sorted(all_ports))) if all_ports else 'Ninguno'

        summary = f"""
    📋 RESUMEN EJECUTIVO PARA {domain.upper()}:
    ═══════════════════════════════════════════════════════════════
    🔢 Subdominios encontrados: {total_subdomains}
    🌐 Con acceso HTTP/HTTPS: {http_accessible}
    🔌 Puertos únicos encontrados: {ports_summary}
    ⏰ Análisis completado: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

    📊 DETALLES POR SUBDOMINIO:
        """

        for data in subdomains_data:
            summary += f"\n    🎯 {data['subdomain']}"
            summary += f"\n       └─ Protocolo: {data['protocol']}"
            summary += f"\n       └─ Status: {data['status_code']}"
            summary += f"\n       └─ Puertos: {data['ports_string']}"

        return summary

    def run_analysis(self):
        """Función principal del análisis"""
        self.banner()

        # Obtener dominios
        domains = self.get_domains_from_user()

        if not domains:
            print("❌ No se ingresaron dominios válidos. Terminando programa.")
            return

        print(f"\n🚀 Iniciando análisis de {len(domains)} dominio(s)...")
        print("⚠️  Este proceso puede tomar varios minutos por dominio...")

        # Analizar cada dominio
        for domain in domains:
            try:
                subdomains_data = self.analyze_domain(domain)
                self.results[domain] = subdomains_data

                # Guardar CSV
                csv_file = self.save_to_csv(domain, subdomains_data)
                self.csv_files.append(csv_file)

                # Mostrar resumen
                summary = self.generate_summary(domain, subdomains_data)
                print(summary)
                print("\n" + "="*80 + "\n")

            except Exception as e:
                print(f"❌ Error analizando {domain}: {str(e)}")
                continue

        # Resumen final
        self.show_final_summary()

    def show_final_summary(self):
        """Muestra resumen final de toda la ejecución"""
        total_subdomains = sum(len(data) for data in self.results.values())
        all_unique_ports = set()

        for domain_data in self.results.values():
            for subdomain_data in domain_data:
                all_unique_ports.update(subdomain_data['open_ports'])

        print("🎉 ANÁLISIS COMPLETADO")
        print("═══════════════════════════════════════════════════════════════")
        print(f"📁 Archivos CSV generados: {len(self.csv_files)}")
        for csv_file in self.csv_files:
            print(f"   📄 {csv_file}")

        print(f"📊 Total de subdominios encontrados: {total_subdomains}")
        print(f"🔌 Puertos únicos detectados: {len(all_unique_ports)}")
        if all_unique_ports:
            print(f"    Puertos: {';'.join(map(str, sorted(all_unique_ports)))}")

        print(f"⏰ Análisis finalizado: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Función principal
def main():
    try:
        analyzer = SubdomainAnalyzer()
        analyzer.run_analysis()
    except KeyboardInterrupt:
        print("\n\n❌ Análisis cancelado por el usuario")
    except Exception as e:
        print(f"\n❌ Error crítico: {str(e)}")

if __name__ == "__main__":
    main()
