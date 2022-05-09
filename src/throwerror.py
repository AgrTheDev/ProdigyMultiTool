from colorama import Fore
import time

def throwerror(error):
    print(f"{Fore.RED}[ERROR] {error}{Fore.RESET}")
    print("Quitting... (10)")
    time.sleep(10)
    exit()