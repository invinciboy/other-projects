#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6

print("Welcome to the tip calculator")
total_bill = input("What was the total bill?$")

tip = input("what percentage tip would you like to give 10 , 12, 0r 15?")

numofpeople = input("how many people to split the bill?")

totalbill2 = float(total_bill) + (float(total_bill) * (int(tip)/100))

splitbill = float(totalbill2) / int(numofpeople)
splitbill2 = round(splitbill, 2)

print(f"Each person should pay ${splitbill2}")
