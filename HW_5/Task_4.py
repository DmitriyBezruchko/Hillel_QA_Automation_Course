"""
4. Вывести треугольник #1 с шириной N с помощью цикла for

2)
    *
   **
  ***
 ****
*****
"""
print('Please enter triangle width:')
N = int(input())

arr = list(range(N, 0, -1))

stars = '*'
for i in arr:
    print((' ' * i) + stars)
    stars += '*'
