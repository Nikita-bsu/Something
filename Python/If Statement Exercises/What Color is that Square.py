let_num = input("Enter the letter and number : ")
letter = let_num[0]
number = int(let_num[1])

if letter == "a" or letter == "c" or letter == "e" or letter == "g":
    if number % 2 == 0:
        print("The square is white")
    else:
        print("The square is black")
elif letter == "b" or letter == "d" or letter == "f" or letter == "h":
    if number % 2 != 0:
        print("The square is black")
    else:
        print("The square is white")

# Доделать