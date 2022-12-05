""""
Права доступа
Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить определенные действия:
запись – W;
чтение – R;
запуск – X.
На вход программе подается:
число n – количество файлов;
n строк с именами файлов и допустимыми операциями;
число m – количество запросов к файлам;
m запросов вида «операция файл».
Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.

Пример ввода:
3
python.exe X
book.txt R W
notebook.exe R W X
5
read python.exe
read book.txt
write notebook.exe
execute notebook.exe
write book.txt

Пример вывода:
Access denied
OK
OK
OK
OK
"""

n = int(input('Please enter amount of files '))

files_dict = {}
for i in range(1, n+1):
    f_data = input(f'''Enter name of file № {i} in a format: filename.extension and operations for a file in a format:\n
 R - read, W - write, X - execute, using spaces as a separator ''')
    f_data_list = f_data.split()
    f_name = f_data_list[0]
    f_operations = ' '.join(f_data_list[1:])
    files_dict[f_name] = f_operations

m = int(input('Please enter amount of operations with files '))

operations = []
for i in range(1, m+1):
    operation_data = input(f'''Enter operation number {i} and filename in a format: operation\n 
(you have options: read, write or execute) and filename.extension using whitespace as a separator ''')
    operation_data_list = operation_data.split()
    operations.append(operation_data_list)

for i in range(0, m):
    if operations[i][0] == "read":
        operations[i][0] = "R"
    elif operations[i][0] == "write":
        operations[i][0] = "W"
    elif operations[i][0] == "execute":
        operations[i][0] = "X"

    if operations[i][0] in files_dict[operations[i][1]]:
        print('OK')
    elif not(operations[i][0] in files_dict[operations[i][1]]):
        print('Access denied')
