""""
Задание 1:
Запросить у пользователя 5 чисел и записать их в список
"""
numbers_list = []
for i in range(1, 6):
    print(f'Enter number {i}: ')
    number = input()
    numbers_list.append(number)

print(f'You entered numbers: {numbers_list}')

