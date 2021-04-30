len1 = float(input("Enter the first side: "))
len2 = float(input("Enter the second side: "))
len3 = float(input("Enter the third side: "))


def valid_trian(s1, s2, s3):
    if s1 == s2 == s3:
        return True
    elif s1 >= s2 + s3 or s2 >= s1 + s3 or s3 >= s1 + s2:
        return False
    else:
        return True


def main():
    print("Your side are {0}, {1}, {2}. If they can be triangle you will see True, else False...{3}".format(len1, len2,
                                                                                                            len3,
                                                                                                            valid_trian(
                                                                                                                len1,
                                                                                                                len2,
                                                                                                                len3)))


main()
