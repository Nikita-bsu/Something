#          # games %wins fans
# ih_wgt = [ [0.1, 0.2, -0.1], #hid[0]
#            [-0.1, 0.1, 0.9], #hid[1]
#            [0.1, 0.4, 0.1]] #hid[2]
#          # hid[0] hid[1] hid[2]
# hp_wgt = [ [0.3, 1.1, -0.3], # травмы
#            [0.1, 0.2, 0.0], # победа
#            [0.0, 1.3, 0.1]] # печаль
#
# weights = [ih_wgt, hp_wgt]
#
# def w_sum(a, b):
#     assert (len(a) == len(b))
#     output = 0
#     for i in range(len(a)):
#         output += (a[i] * b[i])
#     return output
#
#
# def vect_mat_mul(vect, matrix):
#     assert (len(vect) == len(matrix))
#     output = [0, 0, 0]
#
#     for i in range(len(vect)):
#         output[i] = w_sum(vect, matrix[i])
#     return output
#
#
# def neural_network(input, weights):
#     hid = vect_mat_mul(input, weights[0])
#     pred = vect_mat_mul(hid, weights[1])
#     return pred
#
# toes = [8.5, 9.5, 9.9, 9.0]
# wlrec = [0.65, 0.8, 0.8, 0.9]
# nfans = [1.2, 1.3, 0.5, 1.0]
#
# input = [toes[0], wlrec[0], nfans[0]]
# pred = neural_network(input, weights)
# print(pred)

# With Numpy

import numpy as np
# games %wins fans
ih_wgt = np.array([
    [0.1, 0.2, -0.1], # hid[0]
    [-0.1, 0.1, 0.9], # hid[1]
    [0.1, 0.4, 0.1]]) # hid[2]
# hid[0] hid[1] hid[2]
hp_wgt = np.array([
    [0.3, 1.1, -0.3], # травмы?
    [0.1, 0.2, 0.0], # победы?
    [0.0, 1.3, 0.1]]) # печаль?

weights = [ih_wgt, hp_wgt]

def neural_network(input, weights):
    hid = input.dot(weights[0])
    pred = hid.dot(weights[1])
    return pred

toes = np.array([8.5, 9.5, 9.9, 9.0])
wlrec = np.array([0.65, 0.8, 0.8, 0.9])
nfans = np.array([1.2, 1.3, 0.5, 1.0])

input = np.array([toes[0], wlrec[0], nfans[0]])

pred = neural_network(input,weights)

print(pred)