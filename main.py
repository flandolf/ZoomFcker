import os
import sys
import platform
import shutil
from colorama import init, Fore, Back, Style
from pathlib import Path
home = str(Path.home())
zoompath = os.path.join(home, "AppData", "Roaming", "Zoom")
init(autoreset=True)
print(Fore.YELLOW + 'Zoom-F v27')
print(Fore.YELLOW + '--------------------------------')
print(Fore.RED + "Deleting Zoom...")
print(Fore.YELLOW + '--------------------------------')
osplatform = str(platform.system())
if osplatform == "Windows":
    try:
        shutil.rmtree(zoompath)
        print(Fore.GREEN + "Successfully deleted Zoom!")
        print(Fore.YELLOW + '--------------------------------')
    except FileNotFoundError:
        print(Fore.RED + "Couldn't delete Zoom.\nThis usually means you dont have permissions,\nor you dont have zoom installed.")
        print(Fore.YELLOW + '--------------------------------')
elif osplatform == "Darwin":
    try:
        shutil.rmtree("/Applications/zoom.us.app")
        print(Fore.RED + '--------------------------------')
        print(Fore.GREEN + "Successfully deleted Zoom!")
        print(Fore.YELLOW + '--------------------------------')
    except FileNotFoundError:
        print(Fore.YELLOW + '--------------------------------')
        print(Fore.RED + "Couldn't delete Zoom.")
        print(Fore.YELLOW + '--------------------------------')
        print(Fore.YELLOW + '--------------------------------')
        print(Fore.GREEN + "Trying Alternative Option...")
        print(Fore.YELLOW + '--------------------------------')
        try:
            shutil.rmtree(home + "/Applications/zoom.us.app")
            print(Fore.YELLOW + '--------------------------------')
            print(Fore.GREEN + "Successfully deleted Zoom!")
            print(Fore.YELLOW + '--------------------------------')
        except OSError:              
            print(Fore.YELLOW + '--------------------------------')
            print("Alternate method failed. Either you don't have Zoom installed or you didn't give your Terminal application Full Disk Access permission.")
            print(Fore.YELLOW + '--------------------------------')
elif osplatform == "Linux":
    print(Fore.YELLOW + '--------------------------------')
    print(Fore.RED + 'Linux added soon.')
    print(Fore.YELLOW + '--------------------------------')
input("")
sys.exit(0)
