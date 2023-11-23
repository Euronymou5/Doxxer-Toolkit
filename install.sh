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

   which pip3 > /dev/null 2>&1
   if [ "$?" -eq "0" ]; then
   echo -e "\npip3 ya esta instalado."
   else
   echo -e "\nInstalando pip3...."
   wget https://bootstrap.pypa.io/get-pip.py
   python3 get-pip.py
   rm -rf get-pip.py
   fi

   echo -e "\nInstalando requerimientos..."
   pip3 install -r requirements.txt

   echo -e "\nInstalando cloudflared..."
   python3 install_cfd.py

   echo -e "\n\033[32mInstalacion completa."
   echo -e "\n[~] Utiliza el comando: python3 dox.py para ejecutar la herramienta."
}

install
