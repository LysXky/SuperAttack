# Crear un ejemplo de CSV que se generaría
import csv

# Datos de ejemplo para mostrar el formato del CSV
example_data = [
    {"Dominio": "example.com", "Subdominio": "www.example.com", "DNS_Existe": "Sí", "HTTP_Accesible": "Sí", "Protocolo": "https", "Puertos_Abiertos": "80;443"},
    {"Dominio": "example.com", "Subdominio": "mail.example.com", "DNS_Existe": "Sí", "HTTP_Accesible": "No", "Protocolo": "N/A", "Puertos_Abiertos": "25;110;143;993;995"},
    {"Dominio": "example.com", "Subdominio": "ftp.example.com", "DNS_Existe": "Sí", "HTTP_Accesible": "No", "Protocolo": "N/A", "Puertos_Abiertos": "21;22"},
    {"Dominio": "example.com", "Subdominio": "api.example.com", "DNS_Existe": "Sí", "HTTP_Accesible": "Sí", "Protocolo": "https", "Puertos_Abiertos": "80;443;8080"},
    {"Dominio": "example.com", "Subdominio": "admin.example.com", "DNS_Existe": "Sí", "HTTP_Accesible": "Sí", "Protocolo": "https", "Puertos_Abiertos": "80;443;8443"}
]

# Crear CSV de ejemplo
with open('ejemplo_subdominios_example_com.csv', 'w', newline='', encoding='utf-8') as csvfile:
    fieldnames = ['Dominio', 'Subdominio', 'DNS_Existe', 'HTTP_Accesible', 'Protocolo', 'Puertos_Abiertos']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    for row in example_data:
        writer.writerow(row)

print("✅ Archivo CSV de ejemplo creado: 'ejemplo_subdominios_example_com.csv'")

# Mostrar el contenido del CSV
print("\n📊 CONTENIDO DEL CSV GENERADO:")
print("=" * 80)
with open('ejemplo_subdominios_example_com.csv', 'r', encoding='utf-8') as f:
    content = f.read()
    print(content)

print("=" * 80)