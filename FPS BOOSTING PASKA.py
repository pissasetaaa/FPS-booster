import subprocess
import time

print(""" 
______ _____ _____ _____  ___   _____ _____ _____ _   _ 
| ___ \_   _/  ___/  ___|/ _ \ /  ___|  ___|_   _(_)_(_)
| |_/ / | | \ `--.\ `--./ /_\ \\ `--.| |__   | |  / _ \ 
|  __/  | |  `--. \`--. \  _  | `--. \  __|  | | / /_\ 
| |    _| |_/\__/ /\__/ / | | |/\__/ / |___  | | |  _  |
\_|    \___/\____/\____/\_| |_/\____/\____/  \_/ \_| |_/
""") 

import subprocess
import time

def print_menu():
    print("1. Sulje selaimet")
    print("2. SUlje vittu äpit (saattaa sulkea hyödyllisiä)")
    print("3. SUlje koko paska")

def sulje_paskat():
    subprocess.call("TASKKILL /F /IM msedge.exe", shell=True)
    subprocess.call("TASKKILL /F /IM chrome.exe", shell=True)
    subprocess.call("TASKKILL /F /IM brave.exe", shell=True)
    subprocess.call("TASKKILL /F /IM firefox.exe", shell=True)

def sulje_apinpaskat():
    apps_to_close = ["netflix.exe", 
                     "steam.exe", 
                     "facebook.exe", 
                     "twitter.exe", 
                     "whatsApp.exe", 
                     "sähköposti.exe", 
                     "spotify.exe", 
                     "firefox.exe"
                     "vlc.exe"
                     "winword.exe"
                     "excel.exe"
                     "powerpnt.exe"
                     "Dropbox.exe"
                     "EpicGamesLauncher.exe"
                     "discord.exe"]
    for app in apps_to_close:
        subprocess.call(f"TASKKILL /F /IM {app}", shell=True)

def main():
    print("\nTervetuloa Käyttämään FPS boosteria!")
    while True:
        print_menu()
        valinta = input("Valitse toiminto: ")

        if valinta == "1":
            print("Suljetaan selaimet...")
            sulje_paskat()
            print("Selaimet suljettu.")

        elif valinta == "2":
            print("Suljetaan valikoidut sovellukset...")
            sulje_apinpaskat()
            print("Valitut sovellukset suljettu.")

        elif valinta == "3":
            print("Kiitos käytöstä!")
            break

        else:
            print("Virheellinen valinta. Yritä uudelleen.")

if __name__ == "__main__":
    main()
