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
if osplatform == "Windows":
    try:
        shutil.rmtree(zoompath)
        print(Fore.GREEN + "Successfully deleted Zoom!")
    except FileNotFoundError:
        print(Fore.RED + "Couldn't delete Zoom.")
elif osplatform == "Darwin":
    try:
        shutil.rmtree("/Applications/zoom.us.app")
        print(Fore.GREEN + "Successfully deleted Zoom!")
    except FileNotFoundError:
        print(Fore.RED + "Couldn't delete Zoom.")
        print(Fore.GREEN + "Trying Alternative Option...")
        try:
            shutil.rmtree(home + "/Applications/zoom.us.app")
            print(Fore.GREEN + "Successfully deleted Zoom!")
        except OSError:
            print("Alternate method failed. Either you don't have Zoom installed or you didn't give your Terminal application Full Disk Access permission.")
input("")
sys.exit(0)
