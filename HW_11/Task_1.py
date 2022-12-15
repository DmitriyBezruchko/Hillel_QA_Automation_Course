"""
Написать декоратор call_times, который будет принимать в качестве параметра file_name, считать
количество вызовов функций и записывать в файл в формате f'{func_name} была вызвана {count} раза.\n'
"""

import os.path


def call_times(file_name):

    def decorator(function):

        def wrapper(*args):
            wrapper.count += 1
            file_txt = []
            res = function(*args,)
            if not os.path.exists(file_name):
                with open(file_name, 'w+') as file:
                    file.write(f'{function.__name__} была вызвана {wrapper.count} раза.\n')
            else:
                with open(file_name, 'r+') as file:
                    file_string = file.read()

                if f'{function.__name__}' in file_string:
                    with open(file_name, 'r') as file:
                        for line in file:
                            if line.startswith(f'{function.__name__}'):
                                file_txt.append(f'{function.__name__} была вызвана {wrapper.count} раза.\n')
                            else:
                                file_txt.append(line)

                    with open(file_name, 'w') as file:
                        file.writelines(file_txt)

                else:
                    with open(file_name, 'a') as file:
                        file.write(f'{function.__name__} была вызвана {wrapper.count} раза.\n')



            return res

        wrapper.count = 0

        return wrapper

    return decorator


@call_times('foo.txt')
def foo():
    pass


@call_times('foo.txt')
def boo():
    pass


@call_times('calls.txt')
def doo():
    pass


foo()
boo()
foo()
foo()
boo()
doo()
