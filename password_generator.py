import random
from termcolor import colored

print(colored("Welcome to the Password Generator", "green"))

all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def generate_password(chars):
	while True:
		try:
			password_length = int(input("How long should the password be?: "))
			password_count = int(input("How many passwords should be generated?: "))
			if password_length < 6 or password_length > 35:
				print(colored("The length should be between 6 and 35", "red"))
			elif password_length >= 6 or password_length <= 35:
				break
		except ValueError:
			print(colored("Not a valid number", "red"))

	for i in range(password_count):
		password = ""
		for z in range(password_length):
			random_char = random.choice(chars)
			password += random_char
		print(colored(password, "green"))
		print("-" * len(password))
	print(colored("Thank you for using the program!", "green"))


def main():
	while True:
		try:
			mode = int(input(colored("For default character list, please enter 1 \nFor custom character list, please enter 2\nmode: ", "green")))
			if mode == 1:
				generate_password(all_chars)
				break
			if mode == 2:
				while True:
					custom_character_list = input("Please enter your custom charcaters: ")
					if " " in custom_character_list:
						print(colored("Can't use spaces in character list", "red"))
					else:
						break
				generate_password(custom_character_list)
				break
			else:
				print(colored("Not a valid mode", "red"))
		except ValueError:
			print(colored("Not a valid mode", "red"))


if __name__ == "__main__":
	main()
