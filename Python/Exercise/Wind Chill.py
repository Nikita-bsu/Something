T_A = float(input("Enter the air temperature : "))
W_S = float(input("Enter the wind speed : "))

WCI = 13.12 + 0.6215*T_A - 11.37 * (W_S ** 0.16) + 0.3965 * T_A * (W_S ** 0.16)

print("The air temperature is {0}, the wind speed is {1} and WCI is {2}".format(T_A, W_S, round(WCI)))