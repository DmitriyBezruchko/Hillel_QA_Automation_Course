"""
Задание 3:
Запросить у пользователя 10 чисел и записать их в список A
Запросить у пользователя число N
Вывести пользователю сколько в списке A повторяется число N
"""

print('Please enter 10 numbers using whitespace as a separator')
numbers = input()
A = numbers.split()
print('Enter any number')
N = input()

if A.count(N) != 0:
    print (f'Value {N} appears in a list {A.count(N)} times')
else:
    print(f'Valie {N} doesn\'t appear in a list')
