BASE_FARE = 4.00
TRAVEL_140 = 0.25

total = 0.00
distance = float(input("Enter the distance that you passed(in kilometers): "))


def taxi_fare(dist):
    dist_meters = BASE_FARE + ((dist * 1000) // 1000) * 1000 * TRAVEL_140 + ((dist * 1000) - ((dist * 1000) // 1000) * 1000) * TRAVEL_140
    return dist_meters


print("Your distance is {0}, so you need to pay {1:.3f}".format(distance, taxi_fare(distance)))