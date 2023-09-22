'''
Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов 
нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.

Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
(т.е. не меньше заданного минимума и не больше заданного максимума)
'''

def arif_prog(array: list[int], a_1: int, d: int, n: int) -> list[int]:
    array = [a_1 + i * d for i in range(n)]
    return array

first_element = int(input('Введите первый член арифм. прогрессии: '))
difference = int(input('Введите разность арифм. прогрессии: '))
elements = int(input('Введите сколько членов арифм. прогрессии нужно вывести: '))
list = arif_prog(array=list, a_1=first_element, d=difference, n=elements)
print(*list)

from random import randint as rnd

def new_list(array, min, max):
    array_1 = [i for i in range(0, len(array)) if min < array[i] < max]
    return array_1

minimum = int(input('Введите минимальное число диапозона поиска: '))
maximum = int(input('Введите максимальное число диапозона поиска: '))
list = [rnd(1, 50) for _ in range(1, 10)]

list_new = new_list(list, minimum, maximum)

print(f'{len(list)} elements in {list}')
print(list_new)