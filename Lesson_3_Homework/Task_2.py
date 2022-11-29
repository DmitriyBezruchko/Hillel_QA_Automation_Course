"""
Пользователь вводит с клавиатуры три числа в переменные a, b, c.
Найдите наибольшее число из них и запишите в переменную max.
"""
print("Please enter three values. But don't enter same values")

print('Enter first value:')
a = int(input())
print('Enter second value:')
b = int(input())
print('Enter third value')
c = int(input())

if a > b and a > c:
    max = a
    print(f"{max} is the largest number you've entered")
elif b > a and b > c:
    max = b
    print(f"{max} is the largest number you've entered")
elif c > a and c > b:
    max = c
    print(f"{max} is the largest number you've entered")
else:
    print("You've entered the same values!")