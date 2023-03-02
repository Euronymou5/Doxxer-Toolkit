# Doxxer-Toolkit by Euronymou5
# https://twitter.com/Euronymou51
# Discord: Euronymou5#3155
# LICENSE: MPL-2.0 license

import os
import time
import subprocess
import random
import pyshorteners
import requests
import pyqrcode
import png
from faker import Faker
from time import sleep
import webbrowser

Version = "2.5"

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

                     Version: v2.5
                     _____________
'''



def sher():
  os.system("clear")
  print(logo)
  print('\n[1] Search with Doxxer Toolkit')
  print('[2] Sherlock (Program)')
  print('[3] Nexfil (Program)')
  print('[4] Basic search with socialscan')
  print('[00] Back to main menu')
  print('[99] Exit')
  var = int(input('\n>> '))
  if var == 1:
     os.system("python3 modules/search_en.py")
  elif var == 2:
     if os.path.exists('.tools/sherlock'):
        user = input('\n[~] Enter the username to search in sherlock: ')
        print(' ')
        os.system(f"cd .tools/sherlock && python3 sherlock {user}")
     else:
       print('\n[!] Sherlock is not installed!')
       var = input('[?] You want to install sherlock [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Installing sherlock...')
          os.system("cd .tools && git clone https://github.com/sherlock-project/sherlock && cd sherlock && pip3 install -r requirements.txt")
          print('[~] Sherlock installed..')
          time.sleep(2)
          sher()
       elif var == "N" or var == "n":
           print('\n[~] Returning to the main menu')
           time.sleep(1)
           sher()
  elif var == 3:
     if os.path.exists('.tools/nexfil'):
        user = input('\n[~] Enter the username to search in nexfil: ')
        print(' ')
        os.system(f"cd .tools/nexfil && python3 nexfil.py -u {user}")
     else:
       print('\n[!] Nexfil is not installed!')
       var = input('[?] You want to install nexfil [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Instalando nexfil...')
          os.system("cd .tools && git clone https://github.com/thewhiteh4t/nexfil && cd nexfil && pip3 install -r requirements.txt")
          print('[~] Nexfil installed.')
          time.sleep(2)
          sher()
       elif var == "N" or var == "n":
           print('\n[~] Returning to the main menu')
           time.sleep(1)
           sher()
  elif var == 4:
     user = input('\n[~] Enter a user to search: ')
     os.system(f"socialscan {user} --show-urls")
  elif var == 00:
     menu()
  elif var == 99:
     exit()
  else:
    print('\n[!] Invalid option.')
    sher()

def iplog():
  os.system("clear")
  print(logo)
  print('\n[~] Enter an option..')
  print('''\n
  [1] IPlogger.org
  
  [2] Grabify
  
  [3] Create an IPlogger link 
  
  [00] Back to main menu
  
  [99] Exit
  ''')
  opc = int(input('>> '))
  if opc == 1:
    print('\n[1] Open link for linux')
    print('\n[2] Open link for termux')
    print('\n[00] Back to main menu')
    print('\n[99] Exit')
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
      print('[~] Invalid option.')
      time.sleep(2)
      iplog()
  elif opc == 2:
    print('\n[1] Open link for linux')
    print('\n[2] Open link for termux')
    print('\n[00] Back to main menu')
    print('\n[99] Exit')
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
      print('[~] Invalid option.')
      time.sleep(2)
      iplog()
  elif opc == 3:
    print(f'\n{Colores.verde}[~] IP will be saved in: Doxxer-Toolkit/.pages/en_pages/IPlogger/ip.txt')
    print(f'\n{Colores.amarillo}[~] You can view the IP ADDRESSES with the command: cat Doxxer-Toolkit/.pages/en_pages/IPlogger/ip.txt')
    print(f'\n{Colores.magenta}[~] To exit press CTRL + C')
    print(' ')
    cmd = "php -t .pages/en_pages/IPlogger -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
    p = subprocess.Popen(cmd, shell=True)
    a = p.communicate()[0]
  elif opc == 00:
    os.system("clear")
    menu()
  elif opc == 99:
    exit()
  else:
    print('[~] Invalid option.')
    time.sleep(2)
    os.system("clear")
    print(logo)
    iplog()
  
def fakerr():
  print(f'''{Colores.red}\n
  [1] Generate fake ipv4
  
  [2] Generate fake phone number
  
  [3] Generate profile of a fake person
  
  [4] Generate User-Agents

  [5] Generate fake Credit card
    
  [00] Back to main menu
  
  [99] Exit
  ''')
  fakk = int(input('>> '))
  if fakk == 1:
    print('\n[~] Generating a fake ipv4...')
    time.sleep(2)
    ip = ".".join(map(str, (random.randint(0, 255)
                            for _ in range(4))))
    print(f'{Colores.verde}[~] IP Generated: {ip}') 
    fakerr()
  elif fakk == 2:
    fake = Faker()
    Faker.seed(0)
    print('[~] How many times do you want to generate a fake number?')
    num = int(input('[~] Enter a number: '))
    print('[~] Generating fake phone number...')
    time.sleep(1)
    for _ in range(num):
      print(fake.phone_number())
    fakerr()
  elif fakk == 3:
    fake = Faker()
    Faker.seed(0)
    print('[~] How many times do you want to generate a fake profile?')
    num = int(input('[~] Enter a number: '))
    print('[~] Generating a fake profile...')
    time.sleep(1)
    for _ in range(num):
      print(fake.profile())
    fakerr()
  elif fakk == 4:
    fake = Faker()
    Faker.seed(0)
    print('[~] How many times do you want to generate a user-agent?')
    num = int(input('[~] Enter a number: '))
    print('[~] Generating a user-anget...')
    time.sleep(1)
    for _ in range(num):
      print(fake.user_agent())
    fakerr()
  elif fakk == 5:
    fake = Faker()
    Faker.seed(0)
    print('[~] How many times do you want to generate a credit card?')
    num = int(input('[~] Enter a number: '))
    print('[~] Generating a fake credit card...')
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
    print('[~] Invalid option.')
    time.sleep(2)
    os.system("clear")
    print(logo)
    fakerr()

def geoip():
  print('\n[1] Geolocate IP')
  print('\n[00] Back to main menu')
  print('\n[99] Exit')
  MC = int(input('\n>> '))
  if MC == 1:
        os.system(f"cd .geo && python3 geo_en.py")
  elif MC == 00:
    menu()
  elif MC == 99:
    exit()
  else:
    print('[~] Invalid option.')
    time.sleep(2)
    os.system("clear")
    print(logo)
    geoip()
    

def emailfak():
  os.system("clear")
  print(logo)
  print('\n[~] Enter an option')
  print('\n[1] Emkei')
  print('\n[2] Anonemail (Anonymouse)')
  print('\n[3] Temp-Mail')
  print('\n[00] Back to main menu')
  print('\n[99] Exit')
  OP = int(input('>> '))
  if OP == 1:
    os.system("clear")
    print(logo)
    print('\n[1] Open link for linux')
    print('\n[2] Open link for termux')
    print('\n[00] Back to main menu')
    print('\n[99] Exit')
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
       print('[~] Invalid option.')
       time.sleep(2)
       emailfak()
  elif OP == 2:
    os.system("clear")
    print(logo)
    print('\n[1] Open link for linx')
    print('\n[2] Open link for termux')
    print('\n[00] Back to main menu')
    print('\n[99] Exit')
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
       print('[~] Invalid option')
       time.sleep(2)
       emailfak()
  elif OP == 3:
    os.system("clear")
    print(logo)
    print('\n[1] Open link for linux')
    print('\n[2] Open link for termux')
    print('\n[00] Back to main menu')
    print('\n[99] Exit')
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
       print('[~] Invalid option.')
       time.sleep(2)
       emailfak()
  elif OP == 00:
    menu()
  elif OP == 99:
    exit()
  else:
    print('[~] Invalid option.')
    time.sleep(2)
    os.system("clear")
    print(logo)
    emailfak()
  
def phishing():
  os.system("clear")
  print(logo)
  print('[1] Using Doxxer Toolkit phishing')
  print('[2] Zphisher (Program)')
  print('[3] 0ni-Phish (Program) (Spanish only)')
  print('[00] Back to main menu')
  print('[99] Exit')
  var = int(input('\n>> '))
  if var == 1:
     print('''
     [~] Select a language from the page to use:
     
     [1] Spanish
     
     [2] English
     ''')
     lengua = int(input('\n>> '))
     if lengua == 1:
       print('''
       [1] Facebook
  
       [2] Google
    
       [3] Twitter
  
       [4] Instagram
  
       [00] Back to main menu
  
       [99] Exit
       ''')
       YP = int(input('>> '))
       if YP == 1:
         print(f'\n{Colores.azul}[~] Users will be saved in: Doxxer-Toolkit/.pages/Facebook/usuarios.txt')
         print(f'\n{Colores.verde}[~] You can see them with the command: cat Doxxer-Toolkit/.pages/Facebook/usuarios.txt')
         print(f'\n{Colores.magenta}[~] To exit press CTRL + C')
         print(' ')
         cmd = "php -t .pages/Facebook -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 2:
         print(f'\n{Colores.azul}[~] Users will be saved in: Doxxer-Toolkit/.pages/Google/usuarios.txt')
         print(f'\n{Colores.verde}[~] You can see them with the command: cat Doxxer-Toolkit/.pages/Google/usuarios.txt')
         print(f'\n{Colores.magenta}[~] To exit press CTRL + C')
         print(' ')
         cmd = "php -t .pages/Google -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 3:
         print(f'\n{Colores.azul}[~] Users will be saved in: Doxxer-Toolkit/.pages/Twitter/usuarios.txt')
         print(f'\n{Colores.verde}[~] You can see them with the command: cat Doxxer-Toolkit/.pages/Twitter/usuarios.txt')
         print(f'\n{Colores.magenta}[~] To exit press CTRL + C')
         print(' ')
         cmd = "php -t .pages/Twitter -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 4:
        print(f'\n{Colores.azul}[~] Users will be saved in: Doxxer-Toolkit/.pages/Instagram/usuarios.txt')
        print(f'\n{Colores.verde}[~] You can see them with the command: cat Doxxer-Toolkit/.pages/Instagram/usuarios.txt')
        print(f'\n{Colores.magenta}[~] To exit press CTRL + C')
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
  
       [00] Back to main menu
  
       [99] Exit
       ''')
       YP = int(input('>> '))
       if YP == 1:
         print(f'\n{Colores.azul}[~] Users will be saved in: Doxxer-Toolkit/.pages/en_pages/facebook/usernames.txt')
         print(f'\n{Colores.verde}[~] You can see them with the command: cat Doxxer-Toolkit/.pages/en_pages/facebook/usernames.txt')
         print(f'\n{Colores.magenta}[~] To exit press CTRL + C')
         print(' ')
         cmd = "php -t .pages/en_pages/facebook -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 2:
         print(f'\n{Colores.azul}[~] Users will be saved in: Doxxer-Toolkit/.pages/en_pages/google_new/usernames.txt')
         print(f'\n{Colores.verde}[~] You can see them with the command: cat Doxxer-Toolkit/.pages/en_pages/google_new/usernames.txt')
         print(f'\n{Colores.magenta}[~] To exit press CTRL + C')
         print(' ')
         cmd = "php -t .pages/en_pages/google_new -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 3:
         print(f'\n{Colores.azul}[~] Users will be saved in: Doxxer-Toolkit/.pages/en_pages/twitter/usernames.txt')
         print(f'\n{Colores.verde}[~] You can see them with the command: cat Doxxer-Toolkit/.pages/en_pages/twitter/usernames.txt')
         print(f'\n{Colores.magenta}[~] To exit press CTRL + C')
         print(' ')
         cmd = "php -t .pages/en_pages/twitter -S localhost:8080 & ssh -R 80:localhost:8080 nokey@localhost.run"
         p = subprocess.Popen(cmd, shell=True)
         a = p.communicate()[0]
       elif YP == 4:
        print(f'\n{Colores.azul}[~] Users will be saved in: Doxxer-Toolkit/.pages/en_pages/instagram/usernames.txt')
        print(f'\n{Colores.verde}[~] You can see them with the command: cat Doxxer-Toolkit/.pages/en_pages/instagram/usernames.txt')
        print(f'\n{Colores.magenta}[~] To exit press CTRL + C')
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
       print('\n[!] Zphisher is not installed!')
       var = input('[?] You want to install zphisher [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Installing zphisher...')
          os.system("cd .tools && git clone https://github.com/htr-tech/zphisher && cd zphisher && bash zphisher.sh")
          print('[~] Zphisher installed.')
          time.sleep(1)
          phishing()
       elif var == "N" or var == "n":
           print('\n[~] Back to main menu')
           time.sleep(1)
           phishing()
  elif var == 3:
     if os.path.exists('.tools/0ni-Phish'):
        os.system(f"cd .tools/0ni-Phish && python3 0ni.py")
     else:
       print('\n[!] 0ni-Phish is not installed!')
       var = input('[?] You want to install 0ni-Phish [Y/n]: ')
       if var == "Y" or var == "y":
          print('\n[~] Instalando 0ni-Phish...')
          os.system("cd .tools && git clone https://github.com/Euronymou5/0ni-Phish")
          print('[~] 0ni-Phish installed.')
          time.sleep(2)
          phishing()
       elif var == "N" or var == "n":
           print('\n[~] Back to main menu')
           time.sleep(1)
           phishing()
  elif var == 00:
     menu()
  elif var == 99:
    exit()
  
def sms():
  print('\n[1] Send Anonymoussms (Page)')
  print('\n[2] Send an anonymous sms using TextBelt')
  print('\n[00] Back to main menu')
  print('\n[99] Exit')
  YR = int(input('>> '))
  if YR == 1:
     print('\n[1] Open link for linux')
     print('\n[2] Open link for termux')
     var = int(input('>> '))
     if var == 1:
        webbrowser.open('http://www.sendanonymoussms.com/')
     elif var == 2:
        os.system("termux-open http://www.sendanonymoussms.com/")
  elif YR ==  2:
      print('[~] Example: +14322009740')
      print(f'\n{Colores.azul}[!] Remember that you can only send 1 message per day')
      numero = input(f'{Colores.red}[~] Enter the phone number: ')
      mess = input('[~] Enter the message you want to send:')
      resp = requests.post('https://textbelt.com/text', {
           'phone': f'{numero}',
           'message': f'{mess}',
           'key': 'textbelt',
      })
      print(resp.json())
      print('[~] Message sent.')
      input('[~] Press enter to continue...')
      os.system("clear")
      print(logo)
      sms()
  elif YR == 00:
    menu()
  elif YR == 99:
    exit()
    
def numero():
    print('\n[1] RevealName (Page)')
    print('[2] Get information using Numverify (API)')
    print('[3] Get information using the Phonenumbers module')
    print('[00] Back to main menu')
    print('[99] Exit')
    var = int(input('\n>> '))
    if var == 1:
       print('\n[1] Open link for linux')
       print('[2] Open link for termux')
       var2 = int(input('>> '))
       if var2 == 1:
          webbrowser.open('https://www.revealname.com/')
          #numero()
       elif var2 == 2:
           os.system("termux-open https://www.revealname.com/")
           #numero()
    elif var == 2:
       print('[~] Example: +19087654321')
       keys = "https://github.com/Euronymou5/LineX/raw/main/keys.json"
       data_keys = requests.get(keys).json()
       numero = input('[~] Enter the phone number: ')
       payload = {}
       apikey11 = {
         "apikey": data_keys['key'],
       }
       apikey22 = { 
         "apikey2": data_keys['key1'],
       }
       apikey33 = {
         "apikey3": data_keys['key2'],
       }
       apikey44 = {
         "apikey4": data_keys['key3'],
       }
       apikey55 = {
         "apikey5": data_keys['key4']
       }
       api = f"https://api.apilayer.com/number_verification/validate?number={numero}"
       try: 
         data = requests.request("GET", api, headers=apikey11, data = payload).json()
         if data['valid'] == False:
           print('\n[!] The phone number is not valid!')
         else:
           print('\n[~] Phone number: ', data['number'])
           print('[~] Country code: ', data['country_code'])
           print('[~] Country Name: ', data['country_name'])
           print('[~] Location: ', data['location'])
           print('[~] Carrier: ', data['carrier'])
       except KeyError:
           try:
             api1 = f"https://api.apilayer.com/number_verification/validate?number={numero}"
             data1 = requests.request("GET", api1, headers=apikey22, data = payload).json()
             if data1['valid'] == False:
               print('\n[!] The phone number is not valid!')
             else:
               print('\n[~] Phone number: ', data1['number'])
               print('[~] Country code: ', data1['country_code'])
               print('[~] Country name: ', data1['country_name'])
               print('[~] Location: ', data1['location'])
               print('[~] Carrier: ', data1['carrier'])
           except KeyError:
              try:
                api3 = f"https://api.apilayer.com/number_verification/validate?number={numero}"
                data3 = requests.request("GET", api3, headers=apikey33, data = payload).json()
                if data3['valid'] == False:
                  print('\n[!] The phone number is not valid!')
                else:
                 print('\n[~] Phone number: ', data3['number'])
                 print('[~] Country code: ', data3['country_code'])
                 print('[~] Country name: ', data3['country_name'])
                 print('[~] Location: ', data3['location'])
                 print('[~] Carrier: ', data3['carrier'])
              except KeyError:
                 try:
                   api4 = f"https://api.apilayer.com/number_verification/validate?number={numero}"
                   data4 = requests.request("GET", api4, headers=apikey44, data = payload).json()
                   if data4['valid'] == False:
                      print('\n[!] The phone number is not valid!')
                   else:
                    print('\n[~] Phone number: ', data4['number'])
                    print('[~] Country code: ', data4['country_code'])
                    print('[~] Country name: ', data4['country_name'])
                    print('[~] Location: ', data4['location'])
                    print('[~] Carrier: ', data4['carrier'])
                 except KeyError:
                   try:
                     api5 = f"https://api.apilayer.com/number_verification/validate?number={numero}"
                     data5 = requests.request("GET", api5, headers=apikey55, data = payload).json()
                     if data5['valid'] == False:
                        print('\n[!] The phone number is not valid!')
                     else:
                        print('\n[~] Phone number: ', data5['number'])
                        print('[~] Country code: ', data5['country_code'])
                        print('[~] Country name: ', data5['country_name'])
                        print('[~] Location: ', data5['location'])
                        print('[~] Carrier: ', data5['carrier'])
                   except KeyError:
                      print('\n[!] Exhausted API you must wait for them to be updated')
                      sleep(2)
                      menu()
    elif var == 3:
       print('\n[~] Example: +19087654321')
       phone_number = str(input('[~] Enter the phone number: '))
       try:
           import phonenumbers
           from phonenumbers import geocoder, carrier, timezone

           phone = phonenumbers.parse(phone_number)
           international = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)
           countrycode = international.split(' ')[0]
           country = geocoder.country_name_for_number(phone, 'en')
           location = geocoder.description_for_number(phone, 'en')
           carrierr = carrier.name_for_number(phone, 'en')
           print(f'\n[~] International format: {international}')
           print(f'[~] Country name: {country} ({countrycode})')
           print(f'[~] City / Province: {location}')
           print(f'[~] Carrier: {carrierr}')
           for time in timezone.time_zones_for_number(phone):
                    print(f'[~] Time zone: {time}')
                    print('\n[~] Full scan.')
      
       except ImportError:
            print(f'\n{Colores.azul}[!] Phonenumbers module not found!')
            print('[~] Use the pip3 install phonenumbers command')
            time.sleep(2)
            print(f'{Colores.red}[~] Returning to the main menu...')
            time.sleep(1)
            numero()
    elif var == 00:
      menu()
    elif var == 99:
      exit()


def osintpa():
  os.system("clear")
  print(logo)
  print('''\n
  [1] osintframework
  
  [2] osint techniques
  
  [00] Regresar al menu principal
  
  [99] Salir
  ''')
  osint = int(input('>> '))
  if osint == 1:
    print('\n[1] Open link for linux')
    print('\n[2] Open link for termux')
    print('\n[00] Back to main menu')
    print('\n[99] Exit')
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
      print('[~] Invalid option.')
      time.sleep(2)
      os.system("clear")
      osintpa()
  elif osint == 2:
    print('\n[1] Open link for linux')
    print('\n[2] Open link for termux')
    print('\n[00] Back to main menu')
    print('\n[99] Exit')
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
      print('[~] Invalid option.')
      time.sleep(2)
      os.system("clear")
      osintpa()
  elif osint == 00:
    menu()
  elif osint == 99:
    exit()
  else:
    print('[~] Invalid option.')
    time.sleep(2)
    os.system("clear")
    osintpa()

def qrcodigo():
  os.system("clear")
  print(logo)
  print('\n[~] Enter a text or url to convert to qr code')
  s = input('[~] Enter a text: ')
  n = input('[~] Input the image name: ')
  d=n+".png"
  url=pyqrcode.create(s)
  url.show()
  url.png(d, scale =40)
  print(f'{Colores.azul}[~] Image saved in the Doxxer-Toolkit folder with the name: {n}.png')
  ll = input(f'{Colores.red}[?]  Do you want to return to the main menu [Y/n]: ')
  if ll == "Y" or ll == "y":
    menu()
  elif ll == "N" or ll == "n":
    print('[~] Exiting...')
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
  print('\n[1] Cutt.ly (Requires API Key)')
  print('\n[2] Shorturl')
  print('\n[3] n9.cl')
  print('\n[4] xurl.es')
  print('\n[5] TinyURL (API)')
  print('\n[6] Chilp.it')
  print('\n[7] Clck.ru')
  print('\n[8] Da.gd')
  print('\n[9] Is.gd')
  print('\n[00] Back to main menu')
  print('\n[99] Exit')
  cortarel = int(input('>> '))
  if cortarel == 1:
    print("[~] If you don't have a Cuttly API Key you need to create an account")
    key = input('[~] Enter your Cuttly API key: ')
    s = pyshorteners.Shortener(api_key=key)
    url1 = input('[~] Link: ')
    print(f'{Colores.azul} Shortened link:', s.cuttly.short(url1))
  elif cortarel == 2:
    os.system("clear")
    print(logo)
    print('\n[1] Open link for linux')
    print('\n[2] Open link for termux')
    print('\n[00] Back to main menu')
    print('\n[99] Exit')
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
      print('[~] Invalid option.')
      time.sleep(2)
      os.system("clear")
      print(logo)
      cortarlink()
  elif cortarel == 3:
    os.system("clear")
    print(logo)
    print('\n[1] Open link for linux')
    print('\n[2] Open link for termux')
    print('\n[00] Back to main menu')
    print('\n[99] Exit')
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
      print('[~] Invalid option.')
      time.sleep(2)
      os.system("clear")
      print(logo)
      cortarlink()
  elif cortarel == 4:
    os.system("clear")
    print(logo)
    print('\n[1] Open link for linux')
    print('\n[2] Open link for termux')
    print('\n[00] Back to main menu')
    print('\n[99] Exit')
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
      print('[~] Invalid option.')
      time.sleep(2)
      os.system("clear")
      print(logo)
      cortarlink()
  elif cortarel == 5:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.azul}[~] Shortened link:', s.tinyurl.short(url))
    time.sleep(2)
  elif cortarel == 6:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.azul}[~] Shortened link:', s.chilpit.short(url))
  elif cortarel == 7:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.azul}[~] Shortened link:', s.clckru.short(url))
  elif cortarel == 8:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.azul}[~] Shortened link:', s.dagd.short(url))
  elif cortarel == 9:
    url = input('[~] Link: ')
    s = pyshorteners.Shortener()
    print(f'{Colores.azul}[~] Shortened link:', s.isgd.short(url))
  elif cortarel == 00:
    menu()
  elif cortarel == 99:
    exit()

def menu():
    os.system("clear")
    print(logo)
    print('''\n
    
    [~] Welcome to Doxxer Toolkit!
                      
    [1] IPloggers      
    [2] Geolocate IP           
    [3] Get information from a phone number
    [4] Phishing       
    [5] SMS                        
    [6] Anonymous emails   
    [7] User search 
    [8] Generate fake information
    [9] OSINT Pages
    [10] Link shorteners
    [11] Generate qr code
    [12] OSINT Email (BETA)
    [99] Exit
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
       os.system("python3 modules/emails_en.py")
    elif elejir == 99:
      exit()
    else:
      print('[~] Invalid option.')
      time.sleep(2)
      os.system("clear")
      menu()
    

menu()
