from faker import Faker
from faker.providers import internet
import colorama
from colorama import Fore
colorama.init(autoreset=True)

fake = Faker()
fake.add_provider(internet)

def profile():
	lang = input("Select a language(hi/en) for profile: ").lower()
	if lang == "en":
		fake = Faker()

		print(f"{Fore.GREEN}\nName: ",fake.name())
		print(f"{Fore.GREEN}Email: ",fake.email())
		print(f"{Fore.GREEN}Address: ",fake.address())
		print(f"{Fore.GREEN}Country: ",fake.country())
		print(f"{Fore.GREEN}Phone no:",fake.phone_number())
		print(f"{Fore.GREEN}Location: ",fake.location_on_land())
		print(f"{Fore.GREEN}Credit card details:",fake.credit_card_number(),fake.credit_card_expire(),fake.credit_card_provider(),fake.credit_card_security_code())
		print(f"{Fore.GREEN}Url: ",fake.url())
		print(f"{Fore.GREEN}Text: ",fake.text())
		print(f"{Fore.CYAN}\nProfile: ")
		print(fake.simple_profile())
		print(f"{Fore.CYAN}\nInternet provider ipv4 add:",fake.ipv4_private(),fake.ipv4_private(),fake.ipv4_public())
		print(f"{Fore.CYAN}MAC address:",fake.mac_address())
	elif lang == "hi":
		fake1 = Faker('hi_IN')

		print(f"{Fore.GREEN}\nName: ",fake1.name())
		print(f"{Fore.GREEN}Email: ",fake1.email())
		print(f"{Fore.GREEN}Address: ",fake1.address())
		print(f"{Fore.GREEN}Country: ",fake1.country())
		print(f"{Fore.GREEN}Phone no:",fake.phone_number())
		print(f"{Fore.GREEN}Location: ",fake.location_on_land())
		print(f"{Fore.GREEN}Credit card details:",fake.credit_card_number(),fake.credit_card_expire(),fake.credit_card_provider(),fake.credit_card_security_code())
		print(f"{Fore.GREEN}Url: ",fake1.url())
		print(f"{Fore.GREEN}Text: ",fake1.text())
		print(f"{Fore.CYAN}\nProfile: ")
		print(fake1.simple_profile())
		print(f"{Fore.RED}\nInternet provider ipv4 add:",fake.ipv4_private(),fake.ipv4_public())
		print(f"{Fore.RED}MAC address:",fake.mac_address())
	else:
		print(f"{Fore.YELLOW}WARNING: Please enter language correctly(hi/en)!")
	print()

if __name__ == "__main__":
	profile()
