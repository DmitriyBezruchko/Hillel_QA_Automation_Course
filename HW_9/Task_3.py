'''
Задание 3
Запросить у пользователя число N и запросить N чисел у пользователя, потом записать их в файл numbers.txt через пробел
'''

N = int(input('Please enter amount of numbers: '))
numbers_list = []
for i in range(1, N+1):
    number = (input(f'Please Enter number {i}: '))
    numbers_list.append(number)
numbers_string = ' '.join(numbers_list)

file = open('numbers.txt', 'w')
file.write(numbers_string)
file.close()
