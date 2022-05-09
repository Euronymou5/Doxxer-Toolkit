function install() {
   clear
   echo -e "\033[31mActualizando paquetes..."
   apt update
   echo -e "\nInstalando python..."
   apt install python -y
   echo -e "\nInstalando python3..."
   apt install python3 -y
   echo -e "\nInstalando php..."
   apt install php -y
   echo -e "\nInstalando pip3..."
   wget https://bootstrap.pypa.io/get-pip.py
   python3 get-pip.py
   rm get-pip.py
   echo -e "\nInstalando requerimientos..."
   pip3 install -r requirements.txt
   echo -e "\n\033[32mInstalacion completa."
   echo -e "\n[~] Utiliza el comando: python3 dox.py para ejecutar la herramienta."
}

install
