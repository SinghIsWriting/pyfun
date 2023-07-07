import colorama
from colorama import Fore
colorama.init(autoreset=True)
import requests

def jok():
	url = "http://official-joke-api.appspot.com/random_joke"
	data = requests.get(url).json()
	print("\n:)", f"{Fore.YELLOW}"+data['setup'])
	print(f"{Fore.YELLOW}"+data['punchline']+"\n")

if __name__ == "__main__":
	jok()
