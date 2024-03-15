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
        Examples:
        phoneinfoga scan -n <number>

        Available Commands:
        help        Help about any command
        scan        Scan a phone number
        scanners    Display list of loaded scanners
        serve       Serve web client
        version     Print current version of the tool
        """)
        arg = input('\n[~] Enter a phoneinfoga argument: ')
        if arg:
             os.system(f"./.tools/phoneinfoga {arg}")
        print('')
     else:
       print('\n[!] Phoneinfoga is not installed!')
       var = input('[?] Do you want to install Phoneinfoga [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Installing Phoneinfoga...')
          
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

          print('\n[~] Phoneinfoga installed.')
          time.sleep(2)
          
          install()
       elif var == "N" or var == "n":
           print('\n[~] Returning to the main menu')
           time.sleep(1)
           os.system("python3 dox_en.py")
