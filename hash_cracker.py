import hashlib
import sys

if sys.argv[1] == "-h" or sys.argv[1] == "--help":
	print("Welcome to offline hash brute forcer")
	print("-------------------------------------")
	print("A typical attack looks like this: python3 hash.py hashtype hash wordlist.txt")
	print("-----------------------------------------------------------------------------")
	print("replace hashtype with md5/sha1/sha224/sha256")
	print("replace hash and wordlist.txt appropriately")
	sys.exit()


hash_type = sys.argv[1]
hashed_string = sys.argv[2]
wordlist = sys.argv[3]


def hash_md5(word):
	hash_object = hashlib.md5(f"{word}".encode('utf-8'))
	hashed = hash_object.hexdigest()
	# print(f"md5: {hashed}")
	if hashed_string == hashed:
		print(f"FOUND HASH: {word}")

def hash_sha1(word):
	hash_object = hashlib.sha1(f"{word}".encode('utf-8'))
	hashed = hash_object.hexdigest()
	# print(f"sha256: {hashed}")
	if hashed_string == hashed:
		print(f"FOUND HASH: {word}")

def hash_sha224(word):
	hash_object = hashlib.sha224(f"{word}".encode('utf-8'))
	hashed = hash_object.hexdigest()
	# print(f"sha256: {hashed}")
	if hashed_string == hashed:
		print(f"FOUND HASH: {word}")

def hash_sha256(word):
	hash_object = hashlib.sha256(f"{word}".encode('utf-8'))
	hashed = hash_object.hexdigest()
	# print(f"sha256: {hashed}")
	if hashed_string == hashed:
		print(f"FOUND HASH: {word}")




with open(wordlist , "r") as file:
	for line in file:
		for word in line.split():
			if hash_type == "md5":
				hash_md5(word)
			elif hash_type == "sha1":
				hash_sha1(word)
			elif hash_type == "sha224":
				hash_sha224(word)
			elif hash_type == "sha256":
				hash_sha256(word)
