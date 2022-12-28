"""
Написать итератор ReverseIterator который принимает список любых обьектов и итерируется по ним в обратном порядке.
Нужно реализовать в виде класса.
Важно: Нужно использовать аннотации.
Пример:
it = ReverseIterator([1, 2, 3, 4, 5])

next(it)  # 5
next(it)  # 4
next(it)  # 3
В качестве решения отправить ссылку на github репозиторий
"""

class ReverseIterator:
    def __init__(self, input_list: list):
        self.input_list = input_list
        self.counter = len(self.input_list) - 1
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < 0:
            raise StopIteration
        current = self.input_list[self.counter]
        self.counter -= 1
        return current


it = ReverseIterator(["one", 'two', 'three', 'four', 'five'])

print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
