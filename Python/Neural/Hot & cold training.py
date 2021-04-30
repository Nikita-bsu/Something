# weight = 0.1
#
# lr = 0.01
#
#
# def neural_network(input, weight):
#     prediction = input * weight
#     return prediction
#
#
# number_of_toes = [8.5]
# win_or_lose_binary = [1] # (победа!!!)
#
# input = number_of_toes[0]
# true = win_or_lose_binary[0]
#
# pred = neural_network(input,weight)
#
# error = (pred - true) ** 2
# print(error)
#
# # СРАВНЕНИЕ: Получение прогноза с увеличенным значением веса
# # и вычисление ошибки
#
# lr = 0.1
# p_up = neural_network(input,weight) + lr
# e_up = (p_up - true) ** 2
# print(e_up)
#
# # СРАВНЕНИЕ: получение прогноза с уменьшенным значением веса
# # и вычисление ошибки
#
# lr = 0.01
# p_dn = neural_network(input, weight) - lr
# e_dn = (p_dn - true) ** 2
# print(e_dn)


weight = 0.5
input = 0.5
goal_prediction = 0.8

step_amount = 0.001  # шаг изменения веса в каждой итерации

for iteration in range(1102):
    prediction = input * weight
    error = (prediction - goal_prediction) ** 2

    up_prediction = input * (weight + step_amount)  # попробовать увеличить
    up_error = (goal_prediction - up_prediction) ** 2

    down_prediction = input * (weight - step_amount)
    down_error = (goal_prediction - down_prediction) ** 2

    if down_error < up_error:
        weight = weight - step_amount  # если уменьшение дало лучший результат, уменьшить!

    if down_error > up_error:
        weight = weight + step_amount  # если увелечение дало лучший результат, увеличить!

    print("Error : " + str(error) + " Prediction : " + str(prediction))

# Проблема 1: он неэффективен
# Этот метод требует вычислить прогноз несколько раз, чтобы один раз изменить
# knob_weight. Это решение выглядит очень неэффективным.


# Проблема 2: иногда невозможно добиться идеальной точности
# прогнозирования
# При выбранном значении step_amount, если только идеальное значение веса
# не равно n*step_amount, сеть достигнет значения, отстоящего от точного прогноза на некоторую величину меньше step_amount, и начнет колебаться вокруг
# goal_prediction вверх и вниз. Присвойте переменной step_amount значение
# 0.2, чтобы убедиться в этом. Если для step_amount выбрать значение 10, вы
# фактически нарушите работу сети. Попробовав сделать так, вы увидите, что
# алгоритм даже не пытается приблизиться к 0.8!
