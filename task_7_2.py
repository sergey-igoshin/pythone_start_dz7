"""
Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) этого
проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма). Это могут быть обычные числа: V и H,
соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы:
для пальто (V/6.5 + 0.5), для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""
from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    def __add__(self, other):
        return self.param + other.param

    @abstractmethod
    def abs_spend(self):
        pass


class Coat(Clothes):
    def abs_spend(self):
        return self.param / 6.5 + 0.5

    @property
    def prop_spend(self):
        return self.param / 6.5 + 0.5


class Suit(Clothes):
    def abs_spend(self):
        return 2 * self.param + 0.3

    @property
    def prop_spend(self):
        return 2 * self.param + 0.3


coat = Coat(48)  # размеры 46, 48, 50, 52, 54
suit = Suit(4)  # рост 1:156-162, 2:162-168, 3:168-172, 4:172-176, 5:176-182, 6:182-186

print(f'Расход на пальто {coat.abs_spend():0.2f} см'.replace('.', ' м '))
print(f'Расход на костюм {suit.abs_spend():0.2f} см'.replace('.', ' м '))
print(f'Всего: {coat.abs_spend() + suit.abs_spend():0.2f} см'.replace('.', ' м '))
print()
print(f'Расход на пальто: {coat.prop_spend:0.2f} см'.replace('.', ' м '))
print(f'Расход на костюм: {suit.prop_spend:0.2f} см'.replace('.', ' м '))
print(f'Всего: {coat.prop_spend + suit.prop_spend:0.2f} см'.replace('.', ' м '))
