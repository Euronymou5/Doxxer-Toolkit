# -*- coding: utf-8 -*-

import os
import platform
import time
import subprocess

logo = '''\033[31;1m
·▄▄▄▄        ▐▄• ▄ ▐▄• ▄ ▄▄▄ .▄▄▄      ▄▄▄▄▄            ▄▄▌  ▄ •▄ ▪  ▄▄▄▄▄
██▪ ██ ▪      █▌█▌▪ █▌█▌▪▀▄.▀·▀▄ █·    •██  ▪     ▪     ██•  █▌▄▌▪██ •██  
▐█· ▐█▌ ▄█▀▄  ·██·  ·██· ▐▀▀▪▄▐▀▀▄      ▐█.▪ ▄█▀▄  ▄█▀▄ ██▪  ▐▀▀▄·▐█· ▐█.▪
██. ██ ▐█▌.▐▌▪▐█·█▌▪▐█·█▌▐█▄▄▌▐█•█▌     ▐█▌·▐█▌.▐▌▐█▌.▐▌▐█▌▐▌▐█.█▌▐█▌ ▐█▌·
▀▀▀▀▀•  ▀█▄▀▪•▀▀ ▀▀•▀▀ ▀▀ ▀▀▀ .▀  ▀     ▀▀▀  ▀█▄▀▪ ▀█▄▀▪.▀▀▀ ·▀  ▀▀▀▀ ▀▀▀ 
                   
                    By:  Euronymou5
                    _______________

                     Version: v2.6
                     _____________
'''

def install():
     os.system("clear")
     print(logo)
     if os.path.isfile('.tools/phoneinfoga'):
        print("""
        Ejemplo:
        phoneinfoga scan -n <numero>

        Comandos disponibles:
        help        Ayuda sobre cualquier comando
        scan        Escanear un número de teléfono
        scanners    Mostrar lista de escáneres cargados
        serve       Montar interfaz web
        version     Imprimir la versión actual de la herramienta.
        """)
        arg = input('\n[~] Ingresa un argumento de phoneinfoga: ')
        if arg:
             os.system(f"./.tools/phoneinfoga {arg}")
        print('')
     else:
       print('\n[!] Phoneinfoga no esta instalado!')
       var = input('[?] Deseas instalar Phoneinfoga [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Instalando Phoneinfoga...')
          
          arch = platform.machine()
          if 'arm' in arch or 'Android' in arch:
              url = 'https://github.com/sundowndev/phoneinfoga/releases/download/v2.10.8/phoneinfoga_Linux_armv6.tar.gz'
          elif 'x86_64' in arch:
              url = 'https://github.com/sundowndev/phoneinfoga/releases/download/v2.10.8/phoneinfoga_Linux_x86_64.tar.gz'
          else:
              url = 'https://github.com/sundowndev/phoneinfoga/releases/download/v2.10.8/phoneinfoga_Linux_i386.tar.gz'

          url_n = os.path.basename(url)
          os.system(f'wget "{url}" &&  tar -xvzf {url_n}')
          os.system("mv 'phoneinfoga' .tools/ ")
          os.remove(url_n)

          print('\n[~] Phoneinfoga instalado.')
          time.sleep(2)
          
          install()
       elif var == "N" or var == "n":
           print('\n[~] Regresando al menu principal')
           time.sleep(1)
           os.system("python3 dox.py")
