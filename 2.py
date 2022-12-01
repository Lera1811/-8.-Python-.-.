#Задача 2. Дана квадратная матрица, заполненная случайными числами. Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.

from random import randint
import statistics

size = 4

matrix = [0] * size

for i in range(size):
    matrix[i] = list(randint(1, 10) for c in range(size))

for i in matrix:
    print(i)

sum_diagonal = 0

for i in range(size):
    print(matrix[i][i], end = '')
    sum_diagonal += matrix [i][i]

print()
print(sum_diagonal)

