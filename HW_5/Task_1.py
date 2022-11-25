"""
1. Вывести треугольник #1 с шириной N с помощью цикла for

1)
*****
****
***
**
*
"""


stars = '*****'
for i in range(0, 5):
    print(stars)
    stars = stars[:-1]
