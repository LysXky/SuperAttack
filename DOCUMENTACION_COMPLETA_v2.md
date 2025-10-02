# ANALIZADOR DE SUBDOMINIOS v2.0 - DOCUMENTACIÓN COMPLETA

## 🎯 RESUMEN EJECUTIVO

**Analizador de Subdominios v2.0** es una herramienta profesional desarrollada específicamente para especialistas en ciberseguridad que permite enumerar subdominios y escanear puertos de manera automatizada y eficiente.

### Características Principales:
- ✅ **Sin dependencias problemáticas**: Solo requiere `requests`
- ✅ **85+ subdominios predefinidos**: Lista exhaustiva de patrones comunes  
- ✅ **30+ puertos críticos**: Enfoque en servicios de alta criticidad
- ✅ **Análisis paralelo optimizado**: ThreadPoolExecutor para máximo rendimiento
- ✅ **CSV con timestamp**: Reportes estructurados para análisis posterior
- ✅ **Resúmenes ejecutivos**: Output detallado y profesional
- ✅ **Manejo robusto de errores**: Continuidad ante fallos individuales
- ✅ **Completamente probado**: Suite de pruebas integrada

---

## 📦 ARCHIVOS INCLUIDOS

### Scripts Principales:
- **`analizador_subdominios_v2.py`** - Script principal de análisis
- **`demo_analizador_v2.py`** - Demostración funcional del sistema
- **`install_v2.py`** - Instalador automático de dependencias
- **`test_sistema.py`** - Suite de pruebas completa

### Archivos de Configuración:
- **`config_analizador_v2.py`** - Configuración personalizable (se crea con instalador)
- **`requirements.txt`** - Lista de dependencias (se crea con instalador)

---

## 🚀 INSTALACIÓN Y USO

### Paso 1: Instalación Automática
```bash
python install_v2.py
```

### Paso 2: Verificación del Sistema
```bash
python test_sistema.py
```

### Paso 3: Demostración (Opcional)
```bash
python demo_analizador_v2.py
```

### Paso 4: Análisis Real
```bash
python analizador_subdominios_v2.py
```

---

## 🔧 ESPECIFICACIONES TÉCNICAS

### Requisitos del Sistema:
- **Python**: 3.6 o superior
- **Dependencias**: requests (se instala automáticamente)
- **Sistema Operativo**: Windows, Linux, macOS
- **Memoria**: ~50-100MB durante ejecución
- **Red**: Conectividad a Internet para resolución DNS y HTTP

### Subdominios Investigados (85 total):
```
Web y aplicaciones: www, app, api, admin, blog, shop, store, portal, dashboard, panel, control, manager, console, ui

Mail y comunicación: mail, webmail, smtp, pop, imap, mx, mx1, mx2, email, messages, chat, support, help, contact

Infraestructura: ftp, sftp, ssh, vpn, proxy, gateway, firewall, router, switch, dns, ns1, ns2, ns3, ns4

Servicios técnicos: database, db, mysql, postgres, redis, mongo, elastic, search, index, cache, cdn, static

Desarrollo y testing: dev, test, stage, staging, prod, production, qa, uat, demo, beta, alpha, sandbox, preview

Monitoreo y analytics: monitor, monitoring, stats, analytics, metrics, grafana, prometheus, kibana, logs, status

Servicios de archivos: files, download, upload, share, docs, media, images, img, assets, resources, backup

Versioning y CI/CD: git, svn, jenkins, ci, build, deploy, release, v1, v2, v3, api-v1, api-v2

Subdominios especiales: autodiscover, autoconfig, cpanel, whm, webdisk, calendar, crm, erp, wiki, forum, news

Mobile y API: mobile, m, api-mobile, rest, graphql, webhook, oauth, auth, sso, identity, login

Cloud y contenedores: cloud, aws, azure, docker, k8s, kubernetes, rancher, nomad, consul, vault
```

### Puertos Escaneados (30 total):
```
Básicos: 21(FTP), 22(SSH), 23(Telnet), 25(SMTP), 53(DNS), 80(HTTP), 110(POP3), 143(IMAP), 443(HTTPS), 993(IMAPS), 995(POP3S)

Bases de datos: 3306(MySQL), 5432(PostgreSQL), 1521(Oracle), 1433(MSSQL), 27017(MongoDB), 6379(Redis)

Web alternos: 8080(HTTP-Alt), 8443(HTTPS-Alt), 8888(HTTP-Alt), 9090(HTTP-Alt), 3000(Node.js), 5000(Flask)

Remotos: 3389(RDP), 5900(VNC), 1723(PPTP)

Windows: 135(RPC), 139(NetBIOS), 445(SMB)

Otros: 111(RPC), 2049(NFS), 11211(Memcached), 50000(SAP), 50070(Hadoop)
```

---

## 📊 FORMATO DE SALIDA

### Estructura CSV:
| Campo | Descripción | Ejemplo |
|-------|-------------|---------|
| Dominio | Dominio principal analizado | example.com |
| Subdominio | Subdominio encontrado | www.example.com |
| DNS_Existe | Resolución DNS exitosa | Sí/No |
| HTTP_Accesible | Conectividad web | Sí/No |
| Protocolo | Protocolo web funcional | https/http/N/A |
| Status_Code | Código de respuesta HTTP | 200/403/404/N/A |
| Puertos_Abiertos | Puertos separados por punto y coma | 80;443;8080 |
| Timestamp | Fecha y hora del análisis | 2025-10-02 20:10:18 |

### Resumen Ejecutivo:
```
📋 RESUMEN EJECUTIVO PARA EXAMPLE.COM:
═══════════════════════════════════════════════════════════════
🔢 Subdominios encontrados: 5
🌐 Con acceso HTTP/HTTPS: 3
🔌 Puertos únicos encontrados: 21;22;25;80;443;8080
⏰ Análisis completado: 2025-10-02 20:10:18

📊 DETALLES POR SUBDOMINIO:
    🎯 www.example.com
       └─ Protocolo: https
       └─ Status: 200
       └─ Puertos: 80;443
```

---

## ⚡ OPTIMIZACIONES DE RENDIMIENTO

### Paralelización Inteligente:
- **ThreadPoolExecutor**: 20 hilos simultáneos para escaneo de puertos
- **Timeout optimizado**: 2 segundos por puerto para balance velocidad/precisión
- **DNS nativo**: Uso de socket.gethostbyname() sin dependencias externas
- **HTTP eficiente**: Requests con timeouts y headers optimizados

### Tiempos Estimados:
- **Por subdominio encontrado**: ~5-8 segundos (DNS + HTTP + puertos)
- **Por dominio completo**: ~8-15 minutos (85 subdominios verificados)
- **Múltiples dominios**: Procesamiento secuencial optimizado

---

## 🔒 CONSIDERACIONES DE SEGURIDAD

### Uso Ético y Legal:
⚠️ **IMPORTANTE**: Este script debe usarse únicamente en:
- Dominios propios
- Dominios con autorización explícita por escrito
- Entornos de laboratorio y pruebas controladas

### Detección y Mitigación:
- **Rate limiting natural**: Sin implementar intencionalmente para uso ético
- **User-Agent realista**: Simula navegador web estándar
- **SSL verification disabled**: Para manejar certificados auto-firmados en entornos de prueba
- **Headers estándar**: Reduce posibilidad de detección como herramienta automatizada

### Responsabilidad Legal:
El uso de esta herramienta en dominios sin autorización puede constituir:
- Violación de términos de servicio
- Actividad ilegal según leyes locales
- Reconocimiento no autorizado de infraestructura

---

## 🛠️ PERSONALIZACIÓN AVANZADA

### Modificar Configuración:
Edite `config_analizador_v2.py` para ajustar:
```python
# Timeouts
DNS_TIMEOUT = 3
HTTP_TIMEOUT = 5
PORT_TIMEOUT = 2

# Paralelización
MAX_WORKERS_PORTS = 20

# Puertos adicionales
ADDITIONAL_PORTS = [8081, 9000, 9001]

# Subdominios adicionales  
ADDITIONAL_SUBDOMAINS = ['custom', 'special', 'internal']
```

### Integración con Otros Tools:
- **Output CSV**: Compatible con Excel, Power BI, Splunk
- **Logging personalizado**: Modificable en el código fuente
- **APIs externas**: Fácil integración con sistemas SIEM

---

## 🧪 VALIDACIÓN Y PRUEBAS

### Suite de Pruebas Incluida:
1. **Versión de Python**: Compatibilidad 3.6+
2. **Librerías estándar**: Verificación de imports
3. **Conectividad**: Prueba de requests y DNS
4. **Funcionalidad**: Threading, CSV, generación de subdominios
5. **Rendimiento**: Benchmark básico de velocidad

### Ejecución de Pruebas:
```bash
python test_sistema.py
```

**Resultado esperado**: 9/9 pruebas exitosas

---

## 📈 MÉTRICAS Y ESTADÍSTICAS

### Cobertura de Análisis:
- **Subdominios verificados**: 85 por dominio
- **Puertos escaneados**: 30 puertos críticos
- **Protocolos soportados**: HTTP, HTTPS, DNS, TCP
- **Formatos de salida**: CSV, consola, resúmenes ejecutivos

### Casos de Uso Empresariales:
- **Red Team Exercises**: Reconocimiento autorizado
- **Auditorías de seguridad**: Mapeo de superficie de ataque
- **Compliance**: Verificación de exposición de servicios
- **Gestión de assets**: Inventario de subdominios activos

---

## 🎯 EJEMPLOS DE USO PROFESIONAL

### Escenario 1: Auditoría de Seguridad
```bash
# Análisis de infraestructura corporativa
python analizador_subdominios_v2.py
# Input: miempresa.com
# Output: CSV con subdominios expuestos y puertos abiertos
```

### Escenario 2: Red Team Exercise
```bash
# Reconocimiento pasivo autorizado
python analizador_subdominios_v2.py  
# Input: objetivo-autorizado.com
# Output: Mapeo de superficie de ataque para pentesting
```

### Escenario 3: Gestión de Assets
```bash
# Inventario regular de infraestructura
python analizador_subdominios_v2.py
# Input: múltiples dominios corporativos
# Output: Reportes CSV para dashboard ejecutivo
```

---

## 📞 SOPORTE Y MANTENIMIENTO

### Solución de Problemas Comunes:

**Error de conectividad**:
```bash
python test_sistema.py  # Verificar conectividad
```

**Dependencias faltantes**:
```bash
python install_v2.py  # Reinstalar dependencias
```

**Rendimiento lento**:
- Reducir MAX_WORKERS_PORTS en configuración
- Verificar conectividad de red
- Usar en horarios de menor congestión

### Actualizaciones y Mejoras:
- **Versión actual**: 2.0
- **Última actualización**: Octubre 2025
- **Compatibilidad**: Python 3.6 - 3.12+

---

## 📋 CONCLUSIÓN

El **Analizador de Subdominios v2.0** representa una solución completa y profesional para especialistas en ciberseguridad que requieren herramientas confiables para reconocimiento y auditoría de infraestructura.

### Ventajas Competitivas:
✅ **Simplicidad**: Sin dependencias problemáticas  
✅ **Completitud**: 85 subdominios + 30 puertos  
✅ **Profesionalismo**: Output estructurado y reportes ejecutivos  
✅ **Confiabilidad**: Suite de pruebas integrada  
✅ **Flexibilidad**: Configuración personalizable  

### Ideal Para:
- Especialistas en ciberseguridad
- Equipos de Red Team
- Auditores de seguridad  
- Consultores en seguridad informática
- Administradores de infraestructura

---

**Desarrollado por:** Especialista Cloud Security - BUPA Chile  
**Versión:** 2.0  
**Fecha:** Octubre 2025  
**Licencia:** Uso profesional autorizado únicamente
