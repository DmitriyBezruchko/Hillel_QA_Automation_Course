"""
2. Вывести треугольник #1 с шириной N с помощью цикла for

2)
*
**
***
****
*****
"""

print('Please enter triangle width:')
N = int(input())


stars = '*'
for i in range(0, N):
    print(stars)
    stars += '*'
    