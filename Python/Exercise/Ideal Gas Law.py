IDEAL_GAS_CONSTANT = 8.314

P = float(input("Enter the pressure in Pascals : "))
V = float(input("Enter the volume in liters : "))
T = input("Enter the temperature : ")

if T.split(" ") == "Celsius":
    new_T = float(T) + 273.15
    n = (P * V) + (IDEAL_GAS_CONSTANT * new_T)
    print("The number of moles of gas in a SCUBA tank is {:.3f}".format(n))
else:
    n = (P*V) / (IDEAL_GAS_CONSTANT * float(T))
    print("The number of moles of gas in a SCUBA tank is {:.3f}".format(n))

# Доделать