'''
Задание 7
Дан файл в котором записан текст, необходимо вывести топ 5 строк которые чаще всего повторяются, пример:
'в' - 20 раз
'привет' - 10 раз
'как' - 9 раз
'у' - 7
'world' - 4
'''

from string import punctuation

with open('Task_7_file.txt', 'r') as file:
    text = file.read()

for char in punctuation:
    text = text.replace(char, '')

words_list = text.lower().split()

word_frequency = {}

for word in words_list:
    if word in word_frequency:
        word_frequency[word] += 1
    else:
        word_frequency[word] = 1

freq_numbers = (sorted(word_frequency.values(), reverse=True))

for key in word_frequency:
    if word_frequency[key] in freq_numbers[0:4]:
        print(key + ' : ' + str(word_frequency[key]))
