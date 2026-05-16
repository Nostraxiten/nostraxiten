# Nostraxiten v1.0

Nostraxiten es una herramienta de auditoría orientada a OSINT, forense y análisis de seguridad. Su interfaz de consola centraliza el acceso a módulos de investigación, análisis de red, extracción de artefactos y herramientas de diagnóstico.

## ¿Qué es?

<img width="1887" height="741" alt="WhatsApp Image 2026-05-16 at 04 39 45" src="https://github.com/user-attachments/assets/2958866c-c2ca-4c53-b74f-76ad429991f2" />

Nostraxiten ofrece un framework modular que reúne:

- análisis de red y escaneo con `nmap`, `tshark`, `theHarvester`, `recon-ng`, `spiderfoot`
- análisis forense local con `volatility`, `foremost`, `bulk_extractor`, `chkrootkit`, `lynis`
- capacidades de análisis de navegación y credenciales, como browser forensics y detección de malware
- utilidades para WiFi, procesos, puertos y análisis binario

El script principal `nostraxiten.py` carga un menú interactivo desde el que se ejecutan los distintos módulos y permite instalar dependencias desde la misma herramienta.

## Características principales

- menú interactivo para lanzar herramientas y módulos
- instalación cruzada de dependencias en Windows, Linux y Termux
- soporte para ejecutar módulos Python propios con configuración de `PYTHONPATH`
- opciones de forense y OSINT integradas

## Requisitos

- Python 3.x
- acceso a la terminal en Windows, Linux o Termux
- permisos de administrador/root para instalar paquetes del sistema

## Instalación

### 1. Preparar el repositorio

```powershell
Set-Location C:\Users\tuUsuario\Documents\nostraxiten
```

### 2. Windows

En Windows, la herramienta incluye un instalador de dependencias en el menú principal. Para instalar dependencias:

```powershell
python nostraxiten.py
```

Luego, en el menú, selecciona la opción `99` para `Install Dependencies (Win/Lin/Android)`.

También puedes instalar manualmente los componentes Python necesarios:

```powershell
python -m pip install --upgrade pip
python -m pip install requests colorama cryptography pycryptodome scapy pywin32
git clone https://github.com/Nostraxiten/nostraxiten.git // git previamente instalado.
```

Para las herramientas externas, descarga e instala manualmente:

- `nmap`: https://nmap.org/download.html
- `tshark`/Wireshark: https://www.wireshark.org/
- `exiftool`: https://exiftool.org/
- `steghide`: https://github.com/StefanoDeVuono/steghide
- `foremost`: compilar desde fuente o instalar desde repositorios compatibles

### 3. Linux

Ejecuta el instalador integrado con Python:

```bash
python3 nostraxiten.py
```

En el menú, selecciona `99` para instalar dependencias.

También puedes instalar manualmente los paquetes de sistema necesarios:

```bash
sudo apt update
sudo apt install -y python3 python3-pip git nmap curl wget tshark binwalk exiftool steghide foremost bulk-extractor chkrootkit lynis
python3 -m pip install --upgrade pip
python3 -m pip install requests colorama cryptography pycryptodome scapy
git clone https://github.com/Nostraxiten/nostraxiten.git
```

### 4. Android (Termux)

En Termux, abre la terminal y ejecuta el instalador integrado:

```bash
python3 nostraxiten.py
```

Elige la opción `99` para instalar dependencias.

Manual:

```bash
pkg update && pkg upgrade
pkg install python git nmap curl wget binwalk exiftool steghide foremost
python3 -m pip install --upgrade pip
python3 -m pip install requests colorama cryptography pycryptodome scapy
git clone https://github.com/Nostraxiten/nostraxiten.git
```

## Uso

Para iniciar la herramienta:

```bash
python nostraxiten.py
```

El menú principal está compuesto por módulos agrupados en:

- Nox: utilidades de análisis profundo y forense
- Classic: herramientas OSINT y de análisis de sistema
- Utilities: análisis binario, generación de reportes y extracción forense

Presiona el número correspondiente para ejecutar un módulo, o `99` para instalar dependencias.

## Instalación de dependencias desde la herramienta

El menú principal de `nostraxiten.py` incluye la opción `99`, que lanza el instalador cruzado de dependencias. Esta opción detecta si estás en:

- Windows
- Linux
- Android/Termux

y ejecuta los comandos adecuados para instalar paquetes de sistema y dependencias Python.

## Contribuir

Se recomienda revisar el código de los módulos existentes y añadir nuevas integraciones siguiendo la estructura de `nostraxiten/modules/nox` y `nostraxiten/modules/classic`.

