import random
word_list = ["aardvark", "baboon", "camel"]
guessword = random.choice(word_list)
wordlen = int(len(guessword))

display = []
for i in range(wordlen):
    display.append("_")
print(display)

blank_count = display.count("_")


while blank_count !=0:
    guessletter = (input("Guess a letter of the word: ")).lower()
    for i in range(wordlen):
        if guessletter == guessword[i]:
            display[i] = guessletter
            blank_count -= 1
            if blank_count == 0:
                print("You win!!!")
    print(display)









