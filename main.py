import os
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
        os.remove("/Applications/zoom.us.app")
        print(Fore.GREEN + 'Zoom Deleted.')
    except FileNotFoundError:
        print(Fore.RED + 'Error Occured.')



input('')