"""
Создайте супер класс Shape и его наследников Triangle, Rectangle.
Класс Shape содержит абстрактный метод draw
Класс Triangle в инициализаторе принимает параметр width: int - ширина треугольника и реализует метод draw (Выводит
в консоль треугольник с шириной width)
Класс Rectangle в инициализаторе принимает параметр width: int и height: int - ширина, высота прямоугольника и
реализует метод draw (Выводит в консоль прямоугольник с шириной width и высотой height)
Создайте список с этими фигурами и в цикле вызовите метод draw у этих обьектов

P.S. Треугольник может быть любой (Равносторонний, Равнобедренный, Разносторонним) главное чтобы состоял и был
заполнен символом '*'.
Прямоугольник тоже должен состоять и быть заполнен символом '*'.
Важно: Используйте аннотации!
В качестве решения нужно отправить ссылку на github репозиторий.
"""
from abc import ABCMeta, abstractmethod

class Shape:

    @abstractmethod
    def draw(self):
        pass


class Triangle(Shape):
    def __init__(self, width: int):
        self.width = width

    def draw(self):
        counter = self.width
        while counter != 0:
            print('*' * counter)
            counter -= 1


class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def draw(self):
        counter = self.height
        while counter != 0:
            print('*' * self.width)
            counter -= 1


triangle_object = Triangle(5)
rectangle_object = Rectangle(6,3)

shapes_list = [triangle_object, rectangle_object]

for i in shapes_list:
    i.draw()



