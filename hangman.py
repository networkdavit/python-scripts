import random

hangman_states = ["""
|
""",
"""
|
|""",
"""
|_
|
|""",
"""
|__
|
|""",
"""
|__
|  |
|"""]

def split(word): 
    return [char for char in word]  

def listToString(s):  
    final_word = "" 
    return (final_word.join(s))  

chosen_word = random.randint(0,1) 

words = [
	["nice", ["_","_","_","_"]],
	["clean", ["_","_","_","_","_"]]
]

guess_count = 0
word = "nice"
new_word = split(words[chosen_word][0])


while guess_count < 5:
	guess = input("Enter a word: ")
	if guess in new_word:
		location = new_word.index(guess)
		words[chosen_word][1][location] = new_word[location]
		result_word = listToString(words[chosen_word][1])
		print(result_word)
		if words[chosen_word][0] == result_word:
			print("You win")
			break
	elif guess not in new_word:
		print(hangman_states[guess_count])
		guess_count += 1
		if guess_count == 5:
			print("Game Over")
