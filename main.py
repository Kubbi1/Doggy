#!/usr/bin/env python
import subprocess
import time
import sys
from colorama import Fore, Back


def install():
    clear_term()
    #aptupdate = subprocess.run('apt upgrade&&apt update', shell = True)
    bomber = subprocess.run('git clone https://github.com/TheSpeedX/TBomb&&pip install requests', shell = True)
    stealer = subprocess.run('git clone https://github.com/tiagorlampert/sAINT', shell = True)
    phish = subprocess.run('git clone https://github.com/KasRoudra/PyPhisher', shell = True)
    wifitee = subprocess.run('git clone https://github.com/derv82/wifite2', shell = True)
    stealer2 = subprocess.run('sudo apt install maven&&sudo --fix-broken install&&sudo apt install zlib1g-dev libncurses5-dev lib32z1 lib32ncurses6 -y', shell = True)
    time.sleep(10)
    clear_term()
    print('Done!')
    time.sleep(4)
    main()


def stealer():
    run = subprocess.run('cd sAINT&&sudo chmod +x configure.sh&&./configure.sh&&sudo java -jar sAINT.jar',
                         shell = True)
def phish():
    run = subprocess.run('cd PyPhisher&&python pyphisher.py', shell = True)

def bomberr():
    run = subprocess.run("cd TBomb&&python3 bomber.py ", shell = True)

def wifitee():
    run = subprocess.run('cd wifite2&&sudo ./Wifite.py', shell = True)

def clear_term():
    clear = subprocess.run("clear", shell = True)

def main():
    clear_term()
    print(Fore.BLACK + Back.LIGHTWHITE_EX + " ░░░░░░░░░░░░░░░▄▀▄▀▀▀▀▄▀▄░░░░░░░░░░\n",
          '░░░░░░░░░░░░░░░█░░░░░░░░▀▄░░░░░░▄░░\n',
          '░░░░░░' + Fore.RED + Back.BLACK + 'YOUR' + Fore.BLACK + Back.LIGHTWHITE_EX + '░░░░█░░▀░░▀░░░░░▀▄▄░░█░█░\n',
          '░░░' + Fore.LIGHTYELLOW_EX + Back.BLACK + 'PERSONAL' + Fore.BLACK + Back.LIGHTWHITE_EX + '░░░█░▄░█▀░▄░░░░░░░▀▀░░█░\n',
          '░░░' + Fore.BLUE + Back.BLACK + 'TERMINAL' + Fore.BLACK + Back.LIGHTWHITE_EX + '░░░█░░▀▀▀▀░░░░░░░░░░░░█░\n',
          '░░░░░░' + Fore.GREEN + Back.BLACK + 'PET' + Fore.BLACK + Back.LIGHTWHITE_EX + '░░░░░█░░░░░░░░░░░░░░░░░░█░\n',
          '░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░░░█░\n',
          '░░░░░░░░░░░░░░░█░░▄▄░░▄▄▄▄░░▄▄░░█░░\n',
          '░░░░░░░░░░░░░░░█░▄▀█░▄▀░░█░▄▀█░▄▀░░\n'
          '░░░░░░░░░░░░░░░░▀░░░▀░░░░░▀░░░▀░░░░░\n' + Back.RESET +
          Fore.MAGENTA + "Please, select an option:\n" +
          Fore.LIGHTYELLOW_EX + "[0] - install the necessary packages\n"
                                "[1] - bomber(SMS & Email)\n"
                                "[2] - keylogger maker\n"
                                "[3] - phishing\n" +
                                "[4] - WiFi attack\n" +  Fore.RED +
                                "[99] - exit\n")
    try:
        x = int(input(Fore.GREEN + '>'))
        if x == 1:
            bomberr()
            main()
        elif x == 2:
            stealer()
            time.sleep(2)
            main()
        elif x == 3:
            phish()
            main()
        elif x == 4:
            wifitee()
            main()
        elif x == 0:
            install()
            time.sleep(5)
            main()
        elif x > 4:
            main()
        elif x == 99:
            sys.exit(1)
    except:
        main()

main()
