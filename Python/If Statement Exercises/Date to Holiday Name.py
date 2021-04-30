month_day = input("Enter a month and a day : ")
lst = list(month_day.split(" "))
month = lst[0]
day = int(lst[1])

if month == "January" and day == 1:
    print("It is New year's day")
elif month == "July" and day == 1:
    print("It is Canada day")
elif month == "December" and day == 25:
    print("It is Christmas day")
else:
    print("This day hasn't holiday in Canada, sorry")

