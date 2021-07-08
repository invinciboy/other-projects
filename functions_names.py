
#
# def format_name():
#     f_name = input(print("Input your first name:"))
#     l_name = input(print("Input your last name:"))
#     new_f_name = f_name[0].upper() + f_name[1:]
#     new_l_name = l_name[0].upper() + l_name[1:]
#     joined_name = new_f_name + " " + new_l_name
#     print(joined_name)
#
# format_name()


def format_name(f_name, l_name):
    return (f"{f_name} {l_name}").title()


print(format_name("dwIght", "toleNtino"))


#using default parameters (it will return the defaults when no arguments is being inputted)
def format_name2(f_name="Dwight", l_name="Tolentino"):
    return (f"{f_name} {l_name}").title()

print(format_name2())   #will output Dwight Tolentino
print(format_name2("sky"))    #will output Sky Tolentino
print(format_name2(l_name="deO"))   #will output Dwight Deo

#arbitrary keyword arguments  **kwargs
#used when the number of keyword arguments is unknown

def mykids(**kids):
    print("His last name is " + kids["lname"])

mykids(fname="Sky", lname="Tolentino")
