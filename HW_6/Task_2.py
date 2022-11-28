"""
Пользователь вводит текст и слово которое нужно найти, если это слово есть в тексте, вывести 'YES', иначе 'NO'
"""

print('Please enter the text:')
text = input()

print('Please enter the word:')
word = input()

res = text.find(word)

if res == -1:
    print('NO')
else:
    print('YES')