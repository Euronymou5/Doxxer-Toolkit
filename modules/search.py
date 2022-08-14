# Busqueda de usuario con Doxxer Toolkit

import requests
import time

class Colores:
  red="\033[31;1m"
  verde="\033[92m"
  azul="\033[94m"
  magenta="\033[36m"
  amarillo="\033[33m"
  
print(f'{Colores.verde}[~] Atencion no siempre los resultados son 100% precisos')
usuario = input(f'{Colores.red}[~] Ingresa el nombre del usuario: ')
print(' ')
url = "https://www.instagram.com/" + usuario
response = requests.get(url)
if response.status_code == 200:
    response.close()
    print(f'[~] Usuario encontrado en Instagram!: {url}')
    time.sleep(2)
else:
    print('[~] Usuario no encontrado en Instagram!')
    time.sleep(2)
  #-----------------Twitter-------------------
print(' ')
url = "https://twitter.com/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] Usuario encontrado en Twitter!: {url}')
    time.sleep(2)
else:
    print('[~] Usuario no encontrado en Twitter!')
    time.sleep(2)
  #--------------Reditt------------------
print(' ')
url = "https://www.reddit.com/user/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] Usuario encontrado en reddit!: {url}')
    time.sleep(2)
else:
    print('[~] Usuario no encontrado en reddit!')
    time.sleep(2)
  #--------------Pintirest--------------
print(' ')
url = f"https://www.pinterest.com/{usuario}/"
if response.status_code == 200:
    response.close()
    print(f'[~] Usuario encontrado en Pinterest!: {url}')
    time.sleep(2)
else:
    print('[~] Usuario no encontrado en Pinterest!')
    time.sleep(2)
  #-----------------Pornhub------------
print(' ')
url = "https://pornhub.com/users/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] Usuario encontrado en Pornhub!: {url}')
    time.sleep(2)
else:
    print('[~] Usuario no encontrado en Pornhub!')
    time.sleep(2)
  #--------------------Youtube-----------
print(' ')
url = "https://www.youtube.com/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] Usuario encontrado en Youtube!: {url}')
    time.sleep(2)
else:
    print('[~] Usuario no encontrado en Youtube!')
    time.sleep(2)
  #------------------Xbox------------------
print(' ')
url = "https://xboxgamertag.com/search/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] Usuario encontrado en Xbox!: {url}')
    time.sleep(2)
else:
    print('[~] Usuario no encontrado en Xbox!')
    time.sleep(2)
  #---------------------Spotify------------
print(' ')
url = "https://open.spotify.com/user/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] Usuario encontrado en Spotify!: {url}')
    time.sleep(2)
else:
    print('[~] Usuario no encontrado en Spotify!')
    time.sleep(2)
  #------------------Patreon-------------
print(' ')
url = "https://www.patreon.com/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] Usuario encontrado en Patreon!: {url}')
    time.sleep(2)
else:
    print('[~] Usuario no encontrado en Patreon!')
    time.sleep(2)
  #------------Myspace-----------------------
print(' ')
url = "https://myspace.com/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] Usuario encontrado en Myspace!: {url}')
    time.sleep(2)
else:
    print('[~] Usuario no encontrado en Myspace!')
    time.sleep(2)
  #---------------Myanimelist----------------
print(' ')
url = "https://myanimelist.net/profile/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] Usuario encontrado en Myanimelist!: {url}')
    time.sleep(2)
else:
    print('[~] Usuario no encontrado en Myanimelist!')
    time.sleep(2)
  #-----------------Github--------------
print(' ')
url = "https://github.com/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] Usuario encontrado en Github!: {url}')
    time.sleep(2)
else:
    print('[~] Usuario no encontrado en Github!')
    time.sleep(2)
  #----------------Twitch-----------
print(' ')
url = "https://www.twitch.tv/" + usuario
if response.status_code == 200:
    response.close()
    print(f'[~] Usuario encontrado en Twitch!: {url}')
    time.sleep(2)
else:
    print('[~] Usuario no encontrado en Twitch!')
    time.sleep(2)
