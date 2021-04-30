def prime(num: int) -> bool:
    if num <= 1:
        return False
    if num <= 3:
        return True

    if num % 2 == 0 or num % 3 == 0:
        return False

    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i = i + 6
    return True


def main():
    num1 = int(input("Enter the number: "))
    print("The number {0}, if True(It is prime), else not prime...{1}".format(num1, prime(num1)))


if __name__ == "__main__":
    main()
