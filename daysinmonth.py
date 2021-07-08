
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))



def is_leap(given_year):

    if given_year % 4 == 0:
        if given_year % 100 == 0:
            if given_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False







def days_in_month(year, month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # print(month_days[0:])
    if is_leap(year):
        month_days[1] = 29


    print(month_days[month - 1])


# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












