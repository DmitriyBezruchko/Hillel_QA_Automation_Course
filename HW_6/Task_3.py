"""
Пользователь вводит строку.
Если она начинается на 'abc', то заменить их на 'www', иначе добавить в конец строки 'zzz'.

"""

print('Please enter your text:')
text = input()

if text.startswith('abc'):
    new_text = text[3:] + 'www' # не использовал replace чтобы не заменять abc в середине строки
    text = new_text
else:
    new_text = text + 'zzz'
    text = new_text
