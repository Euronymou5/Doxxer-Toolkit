function install() {
   clear
   echo -e "\nInstalando python..."
   pacman -S python
   echo -e "\nInstalando python3..."
   pacman -S python3
   echo -e "\nInstalando php..."
   pacman -S php
   echo -e "\nInstalando wget..."
   pacman -S wget
   echo -e "\nInstalando requerimientos..."
   pip3 install -r requirements.txt
   echo -e "\n\033[32mInstalacion completa."
   echo -e "\n[~] Utiliza el comando: python3 dox.py para ejecutar la herramienta."
}

install
