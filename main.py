import colorama
from colorama import Fore
colorama.init(autoreset=True)

import emoticons
import facts
import jokes
import randJoke
import fake

options = '''
[1]     Feelings of Emoticons
[2]     Fun Facts
[3]     Python jokes
[4]     Random jokes
[5]     Create Fake Identity
[6]     Exit
'''

print(f"\n\t\t****************", f"{Fore.YELLOW}Fun with Python", "****************\n")

while(True):
    print(options)
    usr = input("Enter option: ")
    if usr == "1":
        emoticons.tell_about()
    elif usr == "2":
        facts.tell()
    elif usr == "3":
        jokes.get()
    elif usr == "4":
        randJoke.jok()
    elif usr == "5":
        fake.profile()
    elif usr == "6":
        print("\nThanks for using this script :)")
        break
    else:
        print(f"{Fore.RED}WARNING: Invalid Input!\n")