year = int(input("How old are you? : "))

if year <= 2:
    dog_years = year * 10.5
    print("Your age is {0}, your dog age is {1}".format(year, dog_years))
else:
    dog_years = (year - 2) * 4 + 2 * 10.5
    print("Your age is {0}, your dog age is {1}".format(year, dog_years))