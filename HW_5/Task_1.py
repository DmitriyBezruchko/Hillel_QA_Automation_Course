"""
1. Вывести треугольник #1 с шириной N с помощью цикла for

1)
*****
****
***
**
*
"""

print('Please enter triangle width:')
N = int(input())

stars = '*' * N
for i in range(0, N):
    print(stars)
    stars = stars[:-1]
