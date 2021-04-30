dB = int(input("Enter the number of decibel : "))

if dB < 40:
    print("The sound level less than 40")
elif dB == 40:
    print("The sound level 40")
elif 40 < dB < 70:
    print("The sound level between 41 and 69")
elif dB == 70:
    print("The sound level 70")
elif 70 < dB < 106:
    print("The sound level between 71 and 105")
elif dB == 106:
    print("The sound level 106")
elif 106 < dB < 130:
    print("The sound level between 107 and 129")
elif dB == 130:
    print("The sound level 130")
else:
    print("The sound level more than 130")