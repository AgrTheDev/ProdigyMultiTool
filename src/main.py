import time, os, ctypes
from colorama import Fore
from tokenify import *

logo = f"""{Fore.GREEN}
    ____                _ _                 __  __       _____ 
    |  _ \ _ __ ___   __| (_) __ _ _   _    |  \/  |     |_   _|
    | |_) | '__/ _ \ / _` | |/ _` | | | |   | |\/| |       | |  
    |  __/| | | (_) | (_| | | (_| | |_| |   | |  | |  _    | |  
    |_|   |_|  \___/ \__,_|_|\__, |\__, |   |_|  |_| (_)   |_|  
                            |___/ |___/                        
    {Fore.RESET}"""

ctypes.windll.kernel32.SetConsoleTitleW("Prodigy Multi Tool | https://discord.gg/HDntGJAK6c")

# Login implementation (save username, password, userID to settings.json)
def login():
  os.system("cls")

  print(logo)

  print(f"{Fore.BLUE}~{Fore.RESET}" * 65)
  
  username = input(f"{Fore.CYAN}Prodigy Username\n>>> ")
  print()
  password = input(f"{Fore.CYAN}Prodigy Password\n>>> ")
  print(Fore.RESET)
  tokenify(username, password)

# Menu system (display menu, get user input, call function)
def main():
    os.system("cls")

    print(logo)

    print(f"{Fore.BLUE}~{Fore.RESET}" * 65)
    print(f"""
    (1) - Player Hacks
    (2) - Logout
    {Fore.CYAN}
    ╔════════════════════════╗
      Logged in as: [name]
    ╚════════════════════════╝{Fore.RESET}
    """)
    print(f"{Fore.BLUE}~{Fore.RESET}" * 60)

    input(">>> ")

login()