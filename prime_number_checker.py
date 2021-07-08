
# Write your code below this line 👇

def prime_checker(number):
    if number == 1:
        print("Number 1 is not a primary number")
        exit()
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False

    if is_prime:
        print(f"Number {number} is a prime number")
    else:
        print(f"Number {number} is not a prime number")


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)