"""
Дано два множества A и B
В множестве А находятся имена должников за Сентябрь
В множестве B находятся имена должников за Октябрь
Найти:
* Вывести имена людей которые должны за Сентябрь и Октябрь
* Вывести должников за Октябрь у которых нет долга за Сентябрь
"""

A = {"Vasya Pupkin", "Grigoriy Kalashnikov", "Viktor Kovalenko", "Ivan Maslenko"}
B = {"Innokentiy Bulykin", "Ivan Maslenko"}

print(A.intersection(B))
print(B.difference(A))
