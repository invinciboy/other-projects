# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
length_names = int(len(names)) - 1


random_name = random.randint(0,length_names)

lucky_person = names[random_name]

print(f"{lucky_person} will pay the bill!!!")