'''
Задание 6
Дан файл в котором записаны числа через пробел, необходимо вывести пользователю сумму этих чисел
'''

with open('Task6_file.txt', 'r') as file:
    data_string = file.read()

data_list = data_string.split()
total_sum = 0
for number in data_list:
    total_sum += int(number)
print(f'The sum is: {total_sum}')