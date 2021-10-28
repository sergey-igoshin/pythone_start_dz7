"""
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()), который должен
принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем
с первым элементом первой строки второй матрицы и т.д.
"""
import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return str('\n'.join([''.join([str(f'{el:4}') for el in i]) for i in self.matrix]))

    def __add__(self, other):
        for x in range(len(self.matrix)):
            for y in range(len(self.matrix[x])):
                self.matrix[x][y] = self.matrix[x][y] + other.matrix[x][y]
        return self


class SetMatrix:
    def __init__(self, *args):
        self.row, self.col = args

    @property
    def matrix(self):
        return np.random.randint(-50, 50, (self.row, self.col))


set_m = SetMatrix(int(input('Укажите число строк матрицы: ')), int(input('Укажите число столбцов матрицы: ')))

first_m = Matrix(set_m.matrix)
second_m = Matrix(set_m.matrix)
print(first_m)
print()
print(second_m)
print()
print(first_m + second_m)
