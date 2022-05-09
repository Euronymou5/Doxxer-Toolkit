import os

def install():
    os.system("clear")
    # Actualizar paquetes
    print('\033[31m[~] Actualizando paquetes...')
    os.system("apt update")
    # Instalar python
    print('\n[~] Instalando python...')
    os.system("apt install python -y")
    # Instalar python3
    print('\n[~] Instalando python3...')
    os.system("apt install python3 -y")
    # Instalar php
    print('\n[~] Instalando php...')
    os.system("apt install php -y")
    # Descargar y instalar pip3
    print('\n[~] Instalando pip3...')
    os.system("wget https://bootstrap.pypa.io/get-pip.py")
    os.system("python3 get-pip.py")
    os.system("rm get-pip.py")
    # Instalar requerimientos
    print('\n[~] Instalando requerimientos...')
    os.system("pip3 install -r requirements.txt")
    print('\n\033[32m[+] Instalacion completada.')
    print('\n[~] Utiliza el comando: python3 dox.py para ejecutar la herramienta.')
    exit()
    
install()
