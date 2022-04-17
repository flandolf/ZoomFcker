import os
import sys
import platform
import shutil
from colorama import init, Fore, Back, Style
from pathlib import Path
home = str(Path.home())
zoompath = os.path.join(home, "AppData", "Roaming", "Zoom")
init(autoreset=True)
print(Fore.RED + "Deleting Zoom...")
osplatform = str(platform.system())
if osplatform == 'Windows':
    try:
        shutil.rmtree(zoompath)
        print(Fore.GREEN + 'Zoom Deleted.')
        input('')
    except FileNotFoundError:
        print(Fore.RED + 'Error Occured.')
        input('')
elif osplatform == 'Darwin':
    try:
        shutil.rmtree("/Applications/zoom.us.app")
        print(Fore.GREEN + 'Zoom Deleted.')
    except FileNotFoundError:
        print(Fore.RED + 'Error Occured.')
        print(Fore.GREEN + "Trying Alternative Option...")
        try:    
            shutil.rmtree("sudo rm /Applications/zoom.us.app")
        except OSError:
            print('Alternate Method Failed.')

sys.exit(0)

input('')
