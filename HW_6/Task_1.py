"""
Пользователь вводит слово, если это слово является полиндромом, то вывести '+', иначе '-'

"""

print('Please enter the word. I will check for you if it\'s a palindrome or not')

word = input()
reversed_word = word[::-1]

if word == reversed_word:
    print('+')
else:
    print('-')
