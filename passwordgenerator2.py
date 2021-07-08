import random
import string

nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

paslen = nr_letters + nr_symbols + nr_numbers


letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

passlet = random.sample(letters, nr_letters)
passsym = random.sample(symbols, nr_symbols)
passnum = random.sample(numbers, nr_numbers)

password = passlet + passsym + passnum
random.shuffle(password)
# password = random.sample(all, paslen)
password2 = ''.join(password)
print("Your password is:")
print(password2)
# print(password2)