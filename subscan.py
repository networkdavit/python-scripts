import requests 
import sys

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
	print("Welcome to subdomain scanner")
	print("-------------------------------------")
	print("A typical attack looks like this: python3 domain subdomain_wordlist.txt output.txt")
	sys.exit()

try:
	domain = sys.argv[1]
	wordlist = sys.argv[2]
	output = sys.argv[3]
except IndexError:
	output = "output.txt"

file = open(wordlist)
content = file.read()
subdomain_list = content.splitlines()

for subdomain in subdomain_list:
	url = f"https://{subdomain}.{domain}"
	try:
		r = requests.get(url, timeout=2)
		print(f"FOUND {url}")
		with open(output, "a") as f:
			f.write(url + "\n")
	except requests.ConnectionError:
		pass
