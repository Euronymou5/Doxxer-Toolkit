import requests
from time import sleep
import os

def inicio():
       print('\n[~] Ejemplo: +19087654321')
       keys = "https://github.com/Euronymou5/LineX/raw/main/keys.json"
       data_keys = requests.get(keys).json()
       numero = input('[~] Ingresa el numero de telefono: ')
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
           print('\n[!] El numero no es valido!')
         else:
           print('\n[~] Numero: ', data['number'])
           print('[~] Codigo del pais: ', data['country_code'])
           print('[~] Nombre del pais: ', data['country_name'])
           print('[~] Ubicacion: ', data['location'])
           print('[~] Transportador: ', data['carrier'])
       except KeyError:
           try:
             api1 = f"https://api.apilayer.com/number_verification/validate?number={numero}"
             data1 = requests.request("GET", api1, headers=apikey22, data = payload).json()
             if data1['valid'] == False:
               print('\n[!] El numero no es valido!')
             else:
               print('\n[~] Numero: ', data1['number'])
               print('[~] Codigo del pais: ', data1['country_code'])
               print('[~] Nombre del pais: ', data1['country_name'])
               print('[~] Ubicacion: ', data1['location'])
               print('[~] Transportador: ', data1['carrier'])
           except KeyError:
              try:
                api3 = f"https://api.apilayer.com/number_verification/validate?number={numero}"
                data3 = requests.request("GET", api3, headers=apikey33, data = payload).json()
                if data3['valid'] == False:
                  print('\n[!] El numero no es valido!')
                else:
                 print('\n[~] Numero: ', data3['number'])
                 print('[~] Codigo del pais: ', data3['country_code'])
                 print('[~] Nombre del pais: ', data3['country_name'])
                 print('[~] Ubicacion: ', data3['location'])
                 print('[~] Transportador: ', data3['carrier'])
              except KeyError:
                 try:
                   api4 = f"https://api.apilayer.com/number_verification/validate?number={numero}"
                   data4 = requests.request("GET", api4, headers=apikey44, data = payload).json()
                   if data4['valid'] == False:
                      print('\n[!] El numero no es valido!')
                   else:
                    print('\n[~] Numero: ', data4['number'])
                    print('[~] Codigo del pais: ', data4['country_code'])
                    print('[~] Nombre del pais: ', data4['country_name'])
                    print('[~] Ubicacion: ', data4['location'])
                    print('[~] Transportador: ', data4['carrier'])
                 except KeyError:
                   try:
                     api5 = f"https://api.apilayer.com/number_verification/validate?number={numero}"
                     data5 = requests.request("GET", api5, headers=apikey55, data = payload).json()
                     if data5['valid'] == False:
                        print('\n[!] El numero no es valido!')
                     else:
                        print('\n[~] Numero: ', data5['number'])
                        print('[~] Codigo del pais: ', data5['country_code'])
                        print('[~] Nombre del pais: ', data5['country_name'])
                        print('[~] Ubicacion: ', data5['location'])
                        print('[~] Transportador: ', data5['carrier'])
                   except KeyError:
                      print('\n[!] APIs agotadas debes esperar a que sean actualizadas')
                      sleep(2)
                      os.system("python3 dox.py")