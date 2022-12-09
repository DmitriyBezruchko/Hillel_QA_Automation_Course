'''
Напишите функцию change(lst), которая принимает список и меняет местами его первый и последний элемент.
В исходном списке минимум 2 элемента.
'''


def change(lst: list):
    if len(lst) < 2:
        return None

    changed_list = lst[:]
    changed_list[-1] = lst[0]
    changed_list[0] = lst[-1]

    return changed_list


