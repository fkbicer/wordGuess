import random

name = input("What is your name? ")
print("Good Luck ! ", name)

words = ['equal', 'bogazici', 'university', 'arcade',
		'python', 'mathematics', 'player', 'internal',
		'metaverse', 'problem', 'board', 'behavior']

# Function will choose one random
# word from this list of words
word = random.choice(words)
print("Guess the characters")

#An empty guesses list.
guesses = ''

# number of turns to end.
turns = 12


while turns > 0:
	
	# counts the number of times a user fails
    # all the end of the for loop, failed count should be equal to zero.
	failed = 0
	
	# firs taking a char in word
	for char in word:
		
		# and comparing that character with list of guesses
		if char in guesses:
			print(char)
            
			
		else:
			print("_")
			
			# for every failure 1 will be
			# incremented in failure
			failed += 1
			

	if failed == 0:
		# user will win the game if failure is 0
		# and 'You Win' will be given as output
		print("You Win")
		
		# this print the correct word
		print("The word is: ", word)
		break
	
	# getting char from user.
	guess = input("guess a character:")
	
	# every input character will be stored in guesses
	guesses += guess
	
	# check input with the character in word
	if guess not in word:
		
		turns -= 1
		
		# if the character doesn’t match the word
		# then “Wrong” will be given as output
		print("Wrong")
		
		# this will print the number of
		# turns left for the user
		print("You have", + turns, 'more guesses')
		
		
		if turns == 0:
			print("You Loose")
