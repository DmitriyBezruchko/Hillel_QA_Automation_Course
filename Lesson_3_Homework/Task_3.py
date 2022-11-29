"""
Пользователь с клавиатуры вводит трех значное число в переменную number.
Переставьте первую и последнюю цифру переменной number, полученный результат запишите в переменную reversed_number.
Важно, что переменная number обязательно должна быть типа данных int и для
решения задачи можно использовать преобразование типов данных только при получении числа из функции input.
"""

print("Enter three numeric number:")
number = int(input())
reversed_number = 0

while number > 0:
    var = number % 10
    reversed_number = reversed_number * 10 + var
    number = number // 10

print(reversed_number)
