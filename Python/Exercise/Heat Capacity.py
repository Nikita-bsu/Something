WATER_HEAR_CAPACITY = 4.186
ELECTRICITY_PRICE = 8.9
J_TO_KWH = 2.777e-7

volume = float(input("Enter the amount of water in milliters : "))
d_temp = float(input("Enter the temperature increase (degrees Celsius) : "))

q = volume * d_temp * WATER_HEAR_CAPACITY

kwh = q * J_TO_KWH
cost = kwh * ELECTRICITY_PRICE

print("That much energy will cost {:.2f} cents: ".format(cost))