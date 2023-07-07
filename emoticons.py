import colorama
from colorama import Fore
colorama.init(autoreset=True)
import demoji   # python library that tells about an emoticon


def tell_about():
	print("\n\t\t***************", f"{Fore.MAGENTA}Feelings of Emoticons", "***************\n")

	print(f"You can use these: 🫂👍💪😋😅😒🤨😉❤️🙄😳🤔😂😥🙏🥺😔😁\n")
	text = input("Paste emojies here: ")
	print()
	l = demoji.findall(text)
	for value in l:
		print(value,"-",str(l[value]).title())
	print()

if __name__ == "__main__":
	tell_about()
