# Osint a un email utilizando socialscan por el momento.

import os

def main():
   email = input('\n[~] Ingresa un email a buscar: ')
   os.system(f"socialscan {email}")
   
main()
