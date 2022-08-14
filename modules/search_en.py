# User search with Doxxer Toolkit

import requests
import time

class Colores:
  red="\033[31;1m"
  verde="\033[92m"
  azul="\033[94m"
  magenta="\033[36m"
  amarillo="\033[33m"
  
print(f'{Colores.verde}[~] Attention not always the results are 100% accurate')
usuario = input(f'{Colores.red}[~] Enter the user name: ')
print(' ')
url = "https://www.instagram.com/" + usuario
response = requests.get(url)
if response.status_code == 200:
    response.close()
    print(f'[~] User found on Instagram!: {url}')
    time.sleep(2)
else:
    print('[~] User not found on Instagram!')
    time.sleep(2)
  #-----------------Twitter-------------------
print(' ')
url = "https://twitter.com/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] User found on Twitter!: {url}')
    time.sleep(2)
else:
    print('[~] User not found on Twitter!')
    time.sleep(2)
  #--------------Reditt------------------
print(' ')
url = "https://www.reddit.com/user/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] User found on reddit!: {url}')
    time.sleep(2)
else:
    print('[~] User not found on reddit!')
    time.sleep(2)
  #--------------Pintirest--------------
print(' ')
url = f"https://www.pinterest.com/{usuario}/"
if response.status_code == 200:
    response.close()
    print(f'[~] User found on pinterest!: {url}')
    time.sleep(2)
else:
    print('[~] User not found on pinterest!')
    time.sleep(2)
  #-----------------Pornhub------------
print(' ')
url = "https://pornhub.com/users/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] User found on pornhub!: {url}')
    time.sleep(2)
else:
    print('[~] User not found on pornhub!')
    time.sleep(2)
  #--------------------Youtube-----------
print(' ')
url = "https://www.youtube.com/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] User found on youtube!: {url}')
    time.sleep(2)
else:
    print('[~] User not found on youtube!')
    time.sleep(2)
  #------------------Xbox------------------
print(' ')
url = "https://xboxgamertag.com/search/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] User found on Xbox: {url}')
    time.sleep(2)
else:
    print('[~] User not found on Xbox!')
    time.sleep(2)
  #---------------------Spotify------------
print(' ')
url = "https://open.spotify.com/user/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] User found on Spotify!: {url}')
    time.sleep(2)
else:
    print('[~] User not found on Spotify!')
    time.sleep(2)
  #------------------Patreon-------------
print(' ')
url = "https://www.patreon.com/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] User found on Patreon!: {url}')
    time.sleep(2)
else:
    print('[~] User not found on Patreon!')
    time.sleep(2)
  #------------Myspace-----------------------
print(' ')
url = "https://myspace.com/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] User found on Myspace!: {url}')
    time.sleep(2)
else:
    print('[~] User not found on Myspace!')
    time.sleep(2)
  #---------------Myanimelist----------------
print(' ')
url = "https://myanimelist.net/profile/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] User found on Myanimelist!: {url}')
    time.sleep(2)
else:
    print('[~] User not found on Myanimelist!')
    time.sleep(2)
  #-----------------Github--------------
print(' ')
url = "https://github.com/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] User found on Github!: {url}')
    time.sleep(2)
else:
    print('[~] User not found on Github!')
    time.sleep(2)
  #----------------Twitch-----------
print(' ')
url = "https://www.twitch.tv/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] User found on Twitch!: {url}')
    time.sleep(2)
else:
    print('[~] User not found on Twitch!')
    time.sleep(2)
