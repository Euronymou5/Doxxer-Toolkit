#!/bin/bash

function install() {
   clear

   echo -e "\nInstalando paquetes básicos..."
   pacman -S --noconfirm python3 php wget

   echo -e "\nInstalando requerimientos..."
   pip3 install -r requirements.txt

   echo -e "\nInstalando cloudflared..."
   python3 install_cfd.py

   echo -e "\n\033[32mInstalación completa."
   echo -e "\n[~] Utiliza el comando: python3 dox.py para ejecutar la herramienta."
}

install
