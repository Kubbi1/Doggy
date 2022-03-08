#!/usr/bin/env python
import subprocess
import time
import sys
from colorama import Fore, Back
#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

def install():
    clear_term()
    aptupdate = subprocess.run('apt upgrade&&apt update&&pkg install git', shell = True)
    bomber = subprocess.run('git clone https://github.com/TheSpeedX/TBomb&&pip install requests', shell = True)
    stealer = subprocess.run('git clone https://github.com/tiagorlampert/sAINT.git', shell = True)
    stealer2 = subprocess.run('sudo apt install maven&&sudo --fix-broken install&&sudo apt install zlib1g-dev libncurses5-dev lib32z1 lib32ncurses6 -y', shell = True)
    phish = subprocess.run('git clone https://github.com/An0nUD4Y/blackeye', shell= True)
    clear_term()
    print('Done!')
    time.sleep(4)
    main()


def stealer():
    run = subprocess.run('cd sAINT&&sudo chmod +x configure.sh&&./configure.sh&&sudo java -jar sAINT.jar',
                         shell = True)


def bomberr():
    use = subprocess.run("cd TBomb&&python3 bomber.py ", shell = True)  # ,stdout=subprocess.DEVNULL)


def clear_term():
    clear = subprocess.run("clear", shell = True)
def phish():
    use = subprocess.run('cd blackeye&&./blackeye.sh')

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
                                "[3] - phishing\n" + Fore.RED +
                                "[99] - exit\n")
    try:
        x = input(Fore.GREEN + '>')
        x = int(x)
        if x == 1:
            bomberr()
            main()
        elif x == 2:
            stealer()
            time.sleep(2)
            main()
        elif x == 3:
            clear_term()
            main()
        elif x == 0:
            install()
            time.sleep(5)
            main()
        elif x == 99:
            sys.exit(1)
    except:
        main()


main()
