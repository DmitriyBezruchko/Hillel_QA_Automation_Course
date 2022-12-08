'''
Задание 1
Дан файл с произвольным текстом, необходимо найти все числа в файле и записать в список numbers
'''

f = open('Task1_text.txt', 'r')
text = f.read()
f.close()
text_list = text.split()
numbers = [i for i in text_list if i.isnumeric()]
print(numbers)
