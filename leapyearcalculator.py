# This is how it works out whether if a particular year is a leap year.
#
# > `on every year that is evenly divisible by 4
# >   **except** every year that is evenly divisible by 100
# >     **unless** the year is also evenly divisible by 400`
#
# e.g. The year 2000:
#
# 2000 ÷ 4 = 500 (Leap)
#
# 2000 ÷ 100 = 20 (Not Leap)
#
# 2000 ÷ 400 = 5 (Leap!)



year1 = (input("Input a year: "))
year = int(year1)

div4 = year % 4
div100 = year % 100
div400 = year % 400
#


#############################3
#solution 1
if div4 == 0:
    if div100 == 0:
        if div400 == 0:
            print("Leap Year")
        else:
            print("Not a leap year")
    else:
        print("Leap Year")
else:
    print("Not a leap year")


########################3
# solution 2
# # print(year1[-2:])
#
# if year1[-2:] == "00":
#     if div100 == 0 and div400 == 0:
#         print("Leap Year")
#     else:
#         print("Not a Leap Year")
#
# elif div4 == 0:
#     print("Leap Year")
#
# else:
#     print("Not a Leap Year")
