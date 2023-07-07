import colorama
from colorama import Fore
colorama.init(autoreset=True)
import pyjokes
from random import choice

def get():
	col = list(vars(colorama.Fore).values())
	try:
		l = int(input("\nHow many jokes do you want: "))
		My_joke = pyjokes.get_jokes(language="en", category="all")
		for i in range(0,l):
			print(f"[;)]", end=" ")
			print(choice(col)+My_joke[i])
	except:
		print(f"{Fore.RED}WARNING: Invalid Input!")
	print()

if __name__ == "__main__":
	get()
