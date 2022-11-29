"""
Запросить у пользователя число N
Запросить у пользователя N целых чисел и записать их в список A
Найти в нем минимальное и максимальное число с помощью цикла (запрещено использовать функцию min и max). Вывести эти числа.
"""
print('Please enter any number:')
N = input()

print(f'Please enter {N} numbers using whitespace as a separator')
numbers = input()
A = numbers.split()

max_number = int(A[0])
min_number = int(A[0])
for i in A:
    if int(i) > max_number:
        max_number = int(i)
    if int(i) < min_number:
        min_number = int(i)

print(f'Max number is {max_number}')
print(f'Min number is {min_number}')
