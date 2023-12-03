#!/bin/bash

function is_installed() {
    if pacman -Qi $1 &>/dev/null; then
        echo -e "\033[32m$1 ya está instalado.\033[0m"
    else
        echo -e "\nInstalando $1..."
        pacman -S $1 --noconfirm
    fi
}

function install() {
    clear

    is_installed "python"
    is_installed "python3"
    is_installed "php"
    is_installed "wget"

    echo -e "\nInstalando requerimientos..."
    pip3 install -r requirements.txt

    echo -e "\nInstalando cloudflared..."
    python3 install_cfd.py

    echo -e "\n\033[32mInstalación completa.\033[0m"
    echo -e "\n[~] Utiliza el comando: python3 dox.py para ejecutar la herramienta."
}

install
