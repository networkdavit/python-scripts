import random

print("Welcome to the Password Generator")

all_chars = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"


def generate_password(chars):
	while True:
		try:
			password_length = int(input("How long should the password be?: "))
			password_count = int(input("How many passwords should be generated?: "))
			if password_length < 6 or password_length > 35:
				print("The length should be between 6 and 35")
			elif password_length >= 6 or password_length <= 35:
				break
		except ValueError:
			print("Not a valid number")

	for i in range(password_count):
		password = ""
		for z in range(password_length):
			random_char = random.choice(chars)
			password += random_char
		print(password)
		print("-" * len(password))
	print("Thank you for using the program!")


def main():
	while True:
		try:
			mode = int(input("For default character list, please enter 1 \nFor custom character list, please enter 2\nmode: "))
			if mode == 1:
				generate_password(all_chars)
				break
			if mode == 2:
				while True:
					custom_character_list = input("Please enter your custom charcaters: ")
					if " " in custom_character_list:
						print(("Can't use spaces in character list", "red"))
					else:
						break
				generate_password(custom_character_list)
				break
			else:
				print("Not a valid mode")
		except ValueError:
			print("Not a valid mode")


if __name__ == "__main__":
	main()