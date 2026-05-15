import os
import sys
import time
import subprocess

# 1. Error de Unicode en Windows solucionado:
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class DummyColor:
        def __getattr__(self, name): return ""
    Fore = DummyColor()
    Style = DummyColor()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    r = Fore.RED + Style.BRIGHT
    w = Fore.WHITE + Style.BRIGHT
    d = Fore.LIGHTBLACK_EX
    
    # Red Tiger style banner
    banner = f"""{r}
      ::::    :::  ::::::::   :::::::: ::::::::::: :::::::::      :::     :::    ::: ::::::::::: ::::::::::: :::::::::: ::::    ::: 
     :+:+:   :+: :+:    :+: :+:    :+:    :+:     :+:    :+:   :+: :+:   :+:    :+:     :+:         :+:     :+:        :+:+:   :+:  
    :+:+:+  +:+ +:+    +:+ +:+           +:+     +:+    +:+  +:+   +:+   +:+  +:+      +:+         +:+     +:+        :+:+:+  +:+   
   +#+ +:+ +#+ +#+    +:+ +#++:++#++    +#+     +#++:++#:  +#++:++#++:   +#++:+       +#+         +#+     +#++:++#   +#+ +:+ +#+    
  +#+  +#+#+# +#+    +#+        +#+    +#+     +#+    +#+ +#+     +#+  +#+  +#+      +#+         +#+     +#+        +#+  +#+#+#     
 #+#   #+#+# #+#    #+# #+#    #+#    #+#     #+#    #+# #+#     #+# #+#    #+#     #+#         #+#     #+#        #+#   #+#+#      
###    ####  ########   ########     ###     ###    ### ###     ### ###    ### ###########     ###     ########## ###    ####       
    {d}                                 github.com/nostraxiten/noxforens
    """
    print(banner)
    print(f"{r}[{w}I{r}]{w} Info                                                                 {w}Next {r}[{w}N{r}]")
    print(f"{r}[{w}S{r}]{w} Site")
    
    print(f"      {r}Forense & Recon (NOX){w}           {r}Classic OSINT & Tools{w}           {r}Utilities & Output{w}")
    print(f"      {r}---------------------{w}           {r}---------------------{w}           {r}------------------{w}")

def main():
    while True:
        clear_screen()
        print_banner()
        
        r = Fore.RED + Style.BRIGHT
        w = Fore.WHITE + Style.BRIGHT
        # 2. Error de variable 'd' no definida solucionado:
        d = Fore.LIGHTBLACK_EX
        
        col1 = [
            ("01", "NoxRecon (Full Scan)", "modules/nox/noxrecon.py"),
            ("02", "Browser Forensics", "modules/nox/browserforens.py"),
            ("03", "WiFi Keys Dump", "modules/nox/wifikeys.py"),
            ("04", "Credential Scanner", "modules/nox/credscan.py"),
            ("05", "Process Watcher", "modules/nox/procwatch.py"),
            ("06", "Network Sniffer", "modules/nox/netsniff.py"),
            ("07", "Port Scanner", "modules/nox/portscan.py"),
            ("08", "File Caver", "modules/nox/filecaver.py"),
            ("09", "Steg Detect", "modules/nox/stegdetect.py")
        ]
        
        col2 = [
            ("10", "Nmap Integration", "modules/classic/nmap.py"),
            ("11", "Tshark Dump", "modules/classic/tshark.py"),
            ("12", "TheHarvester", "modules/classic/theharvester.py"),
            ("13", "Sherlock", "modules/classic/sherlock.py"),
            ("14", "Recon-ng", "modules/classic/reconng.py"),
            ("15", "Spiderfoot", "modules/classic/spiderfoot.py"),
            ("16", "Steghide", "modules/classic/steghide.py"),
            ("17", "Binwalk", "modules/classic/binwalk.py"),
            ("18", "Exiftool", "modules/classic/exiftool.py")
        ]
        
        col3 = [
            ("20", "Timeline Gen", "modules/nox/timeline.py"),
            ("21", "Generate Report", "modules/nox/report.py"),
            ("22", "Binary Analyzer", "modules/nox/binary.py"),
            ("23", "Volatility", "modules/classic/volatility.py"),
            ("24", "Foremost", "modules/classic/foremost.py"),
            ("25", "Bulk Extractor", "modules/classic/bulk_extractor.py"),
            ("26", "Lynis Audit", "modules/classic/lynis.py"),
            ("27", "Chkrootkit", "modules/classic/chkrootkit.py")
        ]
        
        # Combinar todas las opciones para la búsqueda fácil
        all_options = {item[0]: item for item in col1 + col2 + col3}
        
        max_rows = max(len(col1), len(col2), len(col3))
        for i in range(max_rows):
            # Obtener datos
            c1_num, c1_text, _ = col1[i] if i < len(col1) else ("", "", "")
            c2_num, c2_text, _ = col2[i] if i < len(col2) else ("", "", "")
            c3_num, c3_text, _ = col3[i] if i < len(col3) else ("", "", "")
            
            # Formatear la cadena de visualización (rojo los corchetes, blanco el texto)
            str_c1 = f"{r}[{w}{c1_num}{r}]{w} {c1_text}" if c1_num else ""
            str_c2 = f"{r}[{w}{c2_num}{r}]{w} {c2_text}" if c2_num else ""
            str_c3 = f"{r}[{w}{c3_num}{r}]{w} {c3_text}" if c3_num else ""
            
            # Calcular espacios. Usamos el texto plano para calcular longitudes.
            plain_c1 = f"[{c1_num}] {c1_text}" if c1_num else ""
            plain_c2 = f"[{c2_num}] {c2_text}" if c2_num else ""
            
            pad1 = " " * (34 - len(plain_c1)) if plain_c1 else " " * 34
            pad2 = " " * (32 - len(plain_c2)) if plain_c2 else " " * 32
            
            print(f"      {str_c1}{pad1}{str_c2}{pad2}{str_c3}")

        print(f"\n      {r}[{w}00{r}]{w} Exit")
        print()
        
        try:
            choice = input(f"{r}nostraxiten{w}@{r}root{w}:~# ").strip()
        except KeyboardInterrupt:
            break
            
        if choice == '00':
            print(f"\n{w}[+] Exiting Nostraxiten Framework...")
            break
        elif choice in ['I', 'i']:
            print(f"\n{w}[i] Nostraxiten Framework - Advanced Forensic & OSINT Suite")
            print(f"{w}[i] Version 1.0 - Modular Edition")
            input(f"\n{d}Press Enter to return...")
        elif choice in ['S', 's']:
            print(f"\n{w}[i] Github: https://github.com/nostraxiten/noxforens")
            input(f"\n{d}Press Enter to return...")
        elif choice in all_options:
            module_num, module_name, module_path = all_options[choice]
            print(f"\n{w}[*] Iniciando {r}{module_name}{w}...")
            time.sleep(1)
            
            # Comprobar si el módulo existe
            if os.path.exists(module_path):
                try:
                    # Ejecutar el módulo con la misma versión de python que ejecuta este script
                    subprocess.run([sys.executable, module_path])
                except Exception as e:
                    print(f"\n{r}[X] Error al ejecutar el módulo: {e}")
            else:
                print(f"\n{r}[X] Módulo '{module_path}' no encontrado.")
            
            input(f"\n{d}Presiona Enter para volver al menú...")
        elif choice != '':
            print(f"\n{r}[X] Opción inválida.")
            time.sleep(1)

if __name__ == '__main__':
    main()
