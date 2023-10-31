#!/usr/bin/python
# -*- coding: utf-8 -*-

# Code of: https://github.com/Euronymou5/Spyrod-v2
# License:  MPL-2.0 license

import requests, json
import os
import time
from platform import system

class colores:
    red="\033[31;1m"


os.system("clear")
logo = colores.red + '''
             uu$:$:$:$:$:$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
         u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$*   *$$$*   *$$$$$$u
       *$$$$*      u$u       $$$$*
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         *$$$$uu$$$   $$$uu$$$$*
          *$$$$$$$*   *$$$$$$$*
            u$$$$$$$u$$$$$$$u
             u$*$*$*$*$*$*$u
  uuu        $$u$ $ $ $ $u$$       uuu
 u$$$$        $$u$u$u$u$u$$       u$$$$
  $$$$$uu      *$$$$$$$$$*     uu$$$$$$
u$$$$$$$$$$$      *****    uuuu$$$$$$$$$
$$$$***$$$$$$$$$$uuu   uu$$$$$$$$$***$$$*
 ***      **$$$$$$$$$$$uu **$***
          uuuu **$$$$$$$$$$uuu
 u$$$uuu$$$$$$$$$uu **$$$$$$$$$$$uuu$$$
 $$$$$$$$$$****           **$$$$$$$$$$$*
   *$$$$$*                      **$$$$**
     $$$*    ___________________  $$$$*
            |Made by: Euronymou5|
            |___________________|
            | Spyrod Version: v3|
            |___________________|
     
     '''  

try:
  print(logo)
  print('[~] Enter the IP: ')
  ip = input('[~] IP: ')
  print(f'[~] Looking up data for: {ip}')
  time.sleep(2)
  api = f"http://ip-api.com/json/{ip}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query&lang=es"

  data = requests.get(api).json()
  ##-----------Query---------##
  print("\n[~] [IP]:", data['query'])
  ##--------------ISP-----------
  print("[~] [ISP]:", data['isp'])
  if data['isp'] == False:
    print('[~] [ISP not found!]')
  ##------------Org-----------##
  print("[~] [Organization]:", data['org'])
  if data['org'] == False:
    print('[~] [Organization not found!]')
  ##-----------City---------##
  print("[~] [City]:", data['city'])
  if data['city'] == False:
    print('[~] [City not found!]')
  ##-----------Country---------##
  print("[~] [Country Name]:", data['country'])
  if data['country'] == False:
    print('[~] [Country Name not found!]')
  ##----------Region-------##
  print("[~] [Region]:", data['region'])
  if data['region'] == False:
    print('[~] [Region not found!]')
  ##---------Continent Name---
  print("[~] [Continent Name]:", data['continent'])
  if data['country'] == False:
    print('[~] [Continent Name not found!]')
  #-----------Region / State-------##
  print("[~] [Region / State]:", data['regionName'])
  if data['regionName'] == False:
    print('[~] [Region / State not found!]')
  ##----------2-letter Continent Code##---
  print("[~] [Two-letter Continent Code]:", data['continentCode'])
  if data['country'] == False:
    print('[~] [Two-letter Continent Code not found!]')
  #---Latitude----##
  print("[~] [Latitude]:", data['lat'])
  if data['lat'] == False:
    print('[~] [Latitude not found!]')
  ##----------Longitude------##
  print("[~] [Longitude]:", data['lon'])
  if data['lon'] == False:
    print('[~] [Longitude not found!]')
  ##--------------Timezone---------##
  print("[~] [Timezone]:", data['timezone'])
  if data['timezone'] == False:
    print('[~] [Timezone not found!]')
  ##-------------- ZIP--------------##
  print("[~] [ZIP Code]:", data['zip'])
  if data['zip'] == False:
    print('[~] [ZIP Code not found!]')
  ##------------ AS -------------------##
  print("[~] [AS Number and Organization]:", data['as'])
  if data['as'] == False:
    print('[~] [AS Number and Organization not found!]')
  ##-----------Country Code-----##
  print("[~] [Two-letter Country Code]:", data['countryCode'])
  if data['countryCode'] == False:
    print('[~] [Two-letter Country Code not found!]')
  ##-----------Reverse IP---------##
  print("[~] [Reverse DNS of IP]:", data['reverse'])
  if data['reverse'] == False:
    print('[~] [Reverse DNS not found!]')
  ##--------------Mobile------##
  print("[~] [Mobile Connection]:", data['mobile'])
  if data['mobile'] == False:
    print('[~] [Mobile Connection not found!]')
  #----Currency----##
  print('[~] [National Currency]:', data['currency'])
  if data['currency'] == False:
    print('[~] [National Currency not found!]')
  #-----District----#
  print('[~] [District (city subdivision)]:', data['district'])
  if data['district'] == False:
    print('[~] [District not found!]')
  #-------Proxy-----#
  print('[~] [Proxy, VPN, or Tor]:', data['proxy'])
  if data['proxy'] == False:
    print('[~] [Proxy, VPN, or Tor not found!]')

except KeyboardInterrupt:
        print('\nExiting the program...')
        time.sleep(1)
        exit()