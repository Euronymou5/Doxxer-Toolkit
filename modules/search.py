# Busqueda de usuario con Doxxer Toolkit

import requests
import time
import re
import os

class Colores:
  red="\033[31;1m"
  verde="\033[92m"
  azul="\033[94m"
  magenta="\033[36m"
  amarillo="\033[33m"
  
#print(f'{Colores.verde}[~] Atencion no siempre los resultados son 100% precisos')
usuario = input(f'\n{Colores.red}[~] Ingresa el nombre del usuario: ')
print(' ')
sites = [f"https://github.com/{usuario}", f"https://twitter.com/{usuario}", f"https://instagram.com/{usuario}", f"https://www.reddit.com/user/{usuario}", f"https://www.pinterest.com/{usuario}", f"https://www.twitch.tv/{usuario}", f"https://xboxgamertag.com/search/{usuario}", f"https://open.spotify.com/user/{usuario}", f"https://www.roblox.com/user.aspx?username={usuario}", f"https://t.me/{usuario}", f"https://xvideos.com/profiles/{usuario}", f"https://www.youtube.com/user/{usuario}", f"https://gitlab.com/{usuario}", f"https://api.mojang.com/users/profiles/minecraft/{usuario}", f"https://www.codecademy.com/profiles/{usuario}", f"https://www.codewars.com/users/{usuario}", f"https://forum.hackthebox.eu/profile/{usuario}", f"https://replit.com/@{usuario}"]
for url in sites:
    pagina = requests.get(url)
    final = re.findall(usuario, pagina.text)
    if final:
        print(f'\n{Colores.verde}[  ✔️   ] Usuario encontrado! {url}')
    else:
        print(f'\n{Colores.red}[!] Usuario no encontrado')
