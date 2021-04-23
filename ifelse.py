# next date of give input date

day = int(input("Enter the day :"))
month = int(input("Enter the month :"))
year = int(input("Enter the year :"))

if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    if month == 2:
        no_of_days = 29
    elif month in [4, 6, 9, 11]:
        no_of_days = 30
    else:
        no_of_days = 31

else:
    if month == 2:
        no_of_days = 28
    elif month in [4, 6, 9, 11]:
        no_of_days = 30
    else:
        no_of_days = 31

if day < no_of_days:

    print(day + 1, "-", month, "-", year)

else:
    if month == 12:
        print(1, "-", 1, "-", year + 1)
    else:
        print(1, "-", month + 1, "-", year)


# user input

x = (input("enter the input\t"))

if x == "lol":
    print("laugh out loud")
elif x == "rofl":
    print("rolling on the floor laughing")
elif x == "lmk":
    print("let me know")
elif x == "smh":
    print("shaking my head")
else:
    print("oops give proper input")
    exit()

# type of input

#x = input("enter the number")

if x == int(input):
    print("number is integer type")
elif x == float(input):
    print("number is float type")
elif x == complex(input):
    print("number is complex type")
elif x == str(input):
    print("number is string type")
elif x == 0:
    print("number is zero")

# pizza Slice

number_of_pizza = int(input("enter number of pizza slice:\n"))

if number_of_pizza % 2 ==0:
    print("price per slice is Rs 120")
    tot_price = number_of_pizza * 120
    print(tot_price)
else:
    print("price per slice is Rs 123")
    tot = number_of_pizza * 123
    print(tot)