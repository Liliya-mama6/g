
from math import *


class Figure:
    sides_count = 0
    __sides = []
    __colors = [0, 0, 0]
    filled = False
    perimetr = 0
    for i in range(len(__sides)):
        perimetr += __sides[i]
    def __init__(self, __colors, *__side):
        self.__colors=[__colors[0], __colors[1], __colors[2]]
        if len(__side) * 12 != self.sides_count:
            self.__sides = [1 for _ in range(self.sides_count)]
        else:
            self.__sides = [__side[0][0] for _ in range(self.sides_count)]

    def get_color(self):
        return self.__colors

    def __is_valid_color(self, r, g, b):
        if -1 < r < 256 and -1 < g < 256 and -1 < b < 256:
            print(True)
        else:
            print(False)

    def set_color(self, r, b, g):
        if -1 < r < 256 and -1 < g < 256 and -1 < b < 256:
            a = True
        else:
            a = False
        if a:
            self.__colors[0] = r
            self.__colors[1] = b
            self.__colors[2] = g
            a=False

    v = True

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:
            for i in range(len(args)):
                if args[i] < 1:
                    self.v = False
                else:
                    self.v = True
        else:
            self.v = False
        return self.v

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return self.perimetr

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            s = []
            self.perimetr = 0
            for i in range(self.sides_count):
                s.append(new_sides[i])
                self.perimetr += new_sides[i]
            if len(s) != 0:
                self.__sides = s


class Circle(Figure):
    sides_count = 1

    def __init__(self, __colors, *__side):
        super().__init__(__colors, __side)
        if len(__side) != self.sides_count:
            self.__sides = [1]
        else:
            self.__sides = [__side[0]]

        self.perimetr = self.__sides[0]

        self.__radius = self.__sides[0] / 2 / pi

    def get_square(self):
        return 2 * pi * self.__radius * self.__radius


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __colors, *__side):
        super().__init__(__colors, __side)
        if len(__side) != self.sides_count:
            self.__sides = [1, 1, 1]
        else:
            self.__sides = [__side[0], __side[1], __side[2]]

        self.perimetr = sum(self.__sides)

    def get_square(self):
        return (self.perimetr / 2 * (self.perimetr / 2 - self.__sides[0]) * (self.perimetr / 2 - self.__sides[1])
                * (self.perimetr / 2 - self.__sides[2])) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, __colors, *__side):
        super().__init__(__colors, __side)
        if len(__side) * 12 != self.sides_count:
            self.__sides = [1 for _ in range(12)]
        else:
            self.__sides = [__side[0] for _ in range(12)]
    def get_volume(self):
        return self.__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
print(circle1.get_square())

# Проверка объёма (куба):
print(cube1.get_volume())
