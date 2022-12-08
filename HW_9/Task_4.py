'''
Задание 4
Сгенерировать 100 рандомных чисел и записать их в файл random_numbers.txt, где одна строка = одно число
'''
import random

random_list = [random.randint(0, 1000) for i in range(100)]
file = open('random_numbers.txt', 'w')
for idx, number in enumerate(random_list):
    if idx <= 98:
        file.write(f'{number}' + '\n')
    if idx == 99:
        file.write(f'{number}')
    

file.close()
