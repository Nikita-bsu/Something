import random


def password():
    randomLength = random.randint(7, 10)

    result = ""
    for i in range(randomLength):
        randomChar = chr(random.randint(33, 126))
        result = result + randomChar

    return result


def main():
    print("Your random password is:", password())


if __name__ == "__main__":
    main()
