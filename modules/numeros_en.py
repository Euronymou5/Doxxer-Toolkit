import requests
from time import sleep
import os


def inicio():
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
                      os.system("python3 dox.py")