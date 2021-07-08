#Step 1
import random
word_list = ["aardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

guessletter = (input("Guess a letter: ")).lower()

guessword = random.choice(word_list)
wordlen = int(len(guessword))


for i in range(wordlen):
  if guessletter == guessword[i]:
    print("Right")
  else:
    print("Wrong")

print("solution2")
for letter in guessword:
    if letter == guessletter:
        print("Right")
    else:
        print("Wrong")