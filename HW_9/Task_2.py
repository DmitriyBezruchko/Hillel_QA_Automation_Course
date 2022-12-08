'''
Задание 2
Запросить у пользователя текст и записать его в файл data.txt
'''

text = input('Please enter some text: ')
file = open('data.txt', 'w')
file.write(text)
file.close()
