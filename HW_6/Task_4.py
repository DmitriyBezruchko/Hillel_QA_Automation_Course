"""
Пользователь вводит текст, удалить в тексте все цифры и вывести строку пользователю.'

"""

print('Please enter your text:')
text = input()

arr = []
for i in text:
    if not i.isdigit():
        arr.append(i)

text_without_digits = "".join(arr)
print('Your text without digits:')
print(text_without_digits)