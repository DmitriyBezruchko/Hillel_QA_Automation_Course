'''
Напишите функцию read_last(lines, file), которая будет открывать определенный файл file и выводить на печать построчно
последние строки в количестве lines (на всякий случай проверим, что задано положительное целое число).
'''


def read_last(lines, file):
    if (lines <= 0) or (not isinstance(lines, int)):
        return None
    with open(file, 'r') as file:
        data = file.readlines()

    data.reverse()
    while lines != 0:
        print(data[lines-1])
        lines -= 1


read_last(4, 'Task_4_file.txt')

