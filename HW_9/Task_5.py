'''
Задание 5
Дан файл с произвольным текстом, нужно найти количество слов в файле и вывести пользователю
'''

with open('Task5_text.txt', 'r') as file:
    text = file.read()
    text_list = text.split()
    print(len(text_list))
