width_of_room = input("Введите ширину в футах или метрах : ")
length_of_room = input("Введите длину в футах или метрах : ")


def area_of_a_room(width, length):
    square = translation_and_square_in_foot(width, length)
    print("Square of the room in foot is {}".format(square))


def translation_and_square_in_foot(width_meters, length_meters):
    lst_width = list(width_of_room.split(" "))
    lst_length = list(length_of_room.split(" "))
    if lst_width[1] == "meters":
        width_foot = float(width_of_room[0]) * 3.28
    if lst_length[1] == "meters":
        length_foot = float(length_of_room[0]) * 3.28
    return width_foot * length_foot


area_of_a_room(width_of_room, length_of_room)