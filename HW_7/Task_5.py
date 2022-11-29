"""
Запросить у пользователя 5 чисел и записать их в список A
Записать все числа из списка A которые больше 5 в список C
"""

print('Please enter 5 numbers using whitespace as a separator')
numbers = input()
A = numbers.split()
C = []

for i in A:
    if int(i) > 5:
        C.append(i)

