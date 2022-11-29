"""
Пользователь вводит текст нужно вывести количество чисел в этом тексте
Пример:
> 'Lorem 222 ipsum, 123 dolor 1 sit amet
Количество чисел: 3
"""

print('Please enter any text')
text = input()
count = 0
for i, char in enumerate(text):
    if char.isdigit() and not text[i+1].isdigit():
        count += 1

print(f'We found {count} numbers in your text.')
