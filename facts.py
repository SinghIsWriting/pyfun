import colorama
from colorama import Fore
colorama.init(autoreset=True)
import randfacts

def tell():
    x = randfacts.get_fact()
    print("\nDid you know that?",f"{Fore.GREEN}"+x)
    print()

if __name__ == "__main__":
    tell()
