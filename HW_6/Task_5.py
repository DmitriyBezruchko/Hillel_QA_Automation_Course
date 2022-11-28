"""
Написать валидатор для почты. Пользователь вводит почту, а программа должна проверить,
что в почте есть символ '@' и '.', и если это так, то вывести "YES", иначе "NO"

"""

print('Please enter email adress:')
email = input()

if email.find('@') != -1 and email.find('.') != -1:
    print('YES')
else:
    print('NO')