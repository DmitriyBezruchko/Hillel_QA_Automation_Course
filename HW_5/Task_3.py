"""
3. Вывести треугольник #1 с шириной N с помощью цикла for

3)
*****
 ****
  ***
   **
    *
"""


stars = '*****'
for i in range(0, 5):
    print((' ' * i) + stars)
    stars = stars[:-1]
