#!/bin/bash

function is_installed() {
    if dpkg -l $1 &>/dev/null; then
        echo -e "\033[32m\n$1 ya está instalado.\033[0m"
    else
        echo -e "\033[32m\nInstalando $1..."
        apt install $1 -y
    fi
}

function install() {
    clear

    echo -e "\033[31mActualizando paquetes..."
    apt update

    is_installed "python"
    is_installed "python3"
    is_installed "php"

    which pip3 > /dev/null 2>&1
    if [ "$?" -eq "0" ]; then
        echo -e "\033[32m\npip3 ya está instalado."
    else
        echo -e "\033[32m\nInstalando pip3..."
        wget https://bootstrap.pypa.io/get-pip.py
        sudo python3 get-pip.py
        rm -rf get-pip.py
    fi

    echo -e "\033[32m\nInstalando requerimientos...\n"
    pip3 install -r requirements.txt

    echo -e "\033[32m\nInstalando cloudflared..."
    python3 install_cfd.py

    echo -e "\n\033[32mInstalación completa.\033[0m"
    echo -e "\033[34m\n[~] Utiliza el comando: python3 dox.py para ejecutar la herramienta."
}

install
