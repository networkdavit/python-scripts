import wikipedia
from termcolor import colored

print("Welcome to wikipedia_search!")

def search():
	search = input("What would you like to search?: ")
	result = wikipedia.page(search)

	try:
		print("---------------------------")
		summary = wikipedia.summary(search)
		print(summary)
		print("---------------------------")
		print(colored(f"URL ==> {result.url}", "green"))
		print("------------------------------------------------------")
		print(colored("Press y to save or any other letter to quit", "green"))
		save_information = input("Would you like to the save the summary?:")
		if save_information == "y":
			file = open(f"summary of {search}.txt", "w")
			file.write(summary)
			file.close
		else:
			pass
	except:
		print(colored("This page doesn't exist", "red"))

search()
