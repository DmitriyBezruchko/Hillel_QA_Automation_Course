"""
Необходимо создать класс Human с атрибутами:
name
surname
age
phone
address
Атрибуты должны заполняться в методе __init__
Так-же нужно написать методы:
get_info(self) - который возвращает словарь в котором находится информация о человеке
call(self, phone_number) - который будет выводить "{self.phone} вызывает абонента {phone_number}"
Нужно создать 3 обьекта класса Human и вызвать у них метод get_info

В качестве решения нужно отправить ссылку на GitHub репозиторий.
"""


class Human:
    def __init__(self, name: str, surname: str, age: int, phone: int, address: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def get_info(self):
        info_dict = {'name': self.name, 'surname': self.surname, 'age': self.age, 'phone': self.phone,
                     'address': self.address}

        return info_dict

    def call(self, phone_number: int):
        print(f'{self.phone} вызывает абонента {phone_number}')


Dima = Human('Dima', 'Bezruchko', 30, +380967966671, 'Knyazhuy Zaton 23')
Dima.get_info()
Sasha = Human('Sasha', 'Kostenko', 37, +380505466787, 'Zarechnaya 47')
Sasha.get_info()
Vika = Human('Vika', 'Vasylchenko', 26, +380688763321, 'Yaroshenko 28')
Dima.get_info()
