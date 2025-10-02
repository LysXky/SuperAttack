# ANALIZADOR DE SUBDOMINIOS - DOCUMENTACIÓN TÉCNICA

## 📋 DESCRIPCIÓN GENERAL
Script avanzado en Python para enumerar subdominios y escanear puertos de manera automatizada.
Desarrollado específicamente para profesionales de ciberseguridad y auditores de seguridad.

## 🎯 FUNCIONALIDADES PRINCIPALES

### 1. Enumeración de Subdominios
- **Método**: Fuerza bruta usando diccionario de subdominios comunes
- **Verificación DNS**: Resuelve registros A y CNAME
- **Verificación HTTP/HTTPS**: Prueba conectividad web
- **64 subdominios comunes** incluidos en el diccionario base

### 2. Escaneo de Puertos
- **Puertos comunes**: 33 puertos críticos pre-configurados
- **Ejecución paralela**: ThreadPoolExecutor para mayor velocidad
- **Timeout ajustable**: 2 segundos por defecto para optimizar velocidad

### 3. Generación de Reportes
- **CSV individual por dominio**: Formato estructurado para análisis
- **Resúmenes detallados**: Output en consola con estadísticas
- **Encoding UTF-8**: Soporte completo para caracteres especiales

## 🔧 REQUISITOS TÉCNICOS

### Dependencias Python
```bash
pip install dnspython requests
```

### Puertos Escaneados
```
21 (FTP), 22 (SSH), 23 (Telnet), 25 (SMTP), 53 (DNS), 80 (HTTP), 
110 (POP3), 111 (RPC), 135 (RPC), 139 (NetBIOS), 143 (IMAP), 
443 (HTTPS), 993 (IMAPS), 995 (POP3S), 1723 (PPTP), 3306 (MySQL), 
3389 (RDP), 5432 (PostgreSQL), 5900 (VNC), 8080 (HTTP-Alt), 
8443 (HTTPS-Alt), 8888 (HTTP-Alt), 9090 (HTTP-Alt), 3000 (Node.js), 
5000 (Flask), 6379 (Redis), 27017 (MongoDB), 1521 (Oracle), 
1433 (MSSQL), 5984 (CouchDB), 11211 (Memcached), 50000 (SAP), 
50070 (Hadoop)
```

### Subdominios Investigados
```
www, mail, ftp, localhost, webmail, smtp, pop, ns1, webdisk, ns2, 
cpanel, whm, autodiscover, autoconfig, test, api, admin, blog, dev, 
staging, secure, cdn, support, shop, app, beta, forum, store, mobile, 
wiki, cloud, demo, server, vpn, dns, remote, backup, portal, crm, 
erp, mysql, sql, db, database, prometheus, grafana, jenkins, git, 
svn, phpmyadmin, webmin, monitoring, stats, status, analytics, mx, 
mx1, mx2, imap, upload, download, files, news, media, images, img, 
video, videos, stream, live, chat, support, help, docs, documentation, 
old, new, legacy, v1, v2, internal, intranet, extranet, production, 
prod, stage, qa, uat, sandbox
```

## 📊 FORMATO DE SALIDA

### Estructura CSV
| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| Dominio | Dominio principal analizado | example.com |
| Subdominio | Subdominio encontrado | www.example.com |
| DNS_Existe | Resolución DNS exitosa | Sí/No |
| HTTP_Accesible | Conectividad web | Sí/No |
| Protocolo | Protocolo web funcional | https/http/N/A |
| Puertos_Abiertos | Lista de puertos abiertos | 80;443;8080 |

### Resumen por Consola
```
📋 RESUMEN PARA EXAMPLE.COM:
═══════════════════════════════════════════════════════════════
🔢 Subdominios encontrados: 4
🔌 Puertos encontrados en los distintos sitios: 21;22;25;80;443
```

## ⚡ OPTIMIZACIONES DE RENDIMIENTO

### Paralelización
- **ThreadPoolExecutor**: 30 hilos simultáneos para escaneo de puertos
- **Timeout optimizado**: 2 segundos por puerto para balance velocidad/precisión
- **DNS caching**: Resolver configurado con servidores públicos (8.8.8.8, 8.8.4.4)

### Manejo de Errores
- **Timeout requests**: 5 segundos para verificación HTTP
- **SSL verification disabled**: Para sitios con certificados auto-firmados
- **Exception handling**: Continuidad de ejecución ante errores individuales

## 🔒 CONSIDERACIONES DE SEGURIDAD

### Uso Ético
⚠️ **IMPORTANTE**: Este script debe usarse únicamente en dominios propios o con autorización explícita.
El uso no autorizado puede constituir una violación de términos de servicio o leyes locales.

### Detección
- **Rate limiting**: Sin implementar - puede ser detectado por WAFs
- **User-Agent**: Configurado para simular navegador web
- **Request headers**: Headers estándar para reducir detección

## 🚀 INSTRUCCIONES DE USO

### Ejecución Básica
```bash
python analizador_subdominios.py
```

### Flujo de Trabajo
1. **Inicio**: Banner informativo y configuración DNS
2. **Input**: Solicitud interactiva de dominios
3. **Análisis**: Enumeración y escaneo paralelo
4. **Output**: Generación de CSV y resúmenes
5. **Finalización**: Estadísticas totales

### Ejemplo de Sesión
```
Ingrese un dominio para analizar: example.com
✓ Dominio 'example.com' agregado correctamente

Ingrese un dominio para analizar: testsite.org  
✓ Dominio 'testsite.org' agregado correctamente

Ingrese un dominio para analizar: fin

🚀 Iniciando análisis de 2 dominio(s)...
```

## 📈 MÉTRICAS DE RENDIMIENTO

### Tiempos Estimados
- **Por subdominio**: ~3-5 segundos (DNS + HTTP + puertos)
- **Por dominio completo**: ~5-10 minutos (64 subdominios)
- **Múltiples dominios**: Lineal (sin paralelización entre dominios)

### Recursos del Sistema
- **Memoria**: ~50-100MB durante ejecución
- **CPU**: Intensivo durante escaneo de puertos paralelo
- **Red**: ~1-2KB por verificación de subdominio
- **Disco**: ~1-5KB por CSV generado

## 🔧 PERSONALIZACIÓN AVANZADA

### Modificar Lista de Subdominios
Editar la función `generate_subdomains()` para agregar/remover subdominios específicos.

### Ajustar Puertos Escaneados
Modificar la lista `common_ports` en `scan_common_ports()` según necesidades específicas.

### Cambiar Paralelización
Ajustar `max_workers` para controlar la intensidad del escaneo según recursos disponibles.

---
**Desarrollado para especialistas en ciberseguridad | Uso responsable y autorizado únicamente**
