"""
Запросить у пользователя число N
Запросить у пользователя N чисел и записать их в список A
Вывести список в обратной последовательности
"""

print('Please enter any number:')
N = input()
A = []

for i in range(1, int(N)+1):
    print(f'Please enter number {i}:')
    num = input()
    A.append(num)

A.reverse()
print(A)

