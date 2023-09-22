'''
Последовательностью Фибоначчи называется
последовательность чисел 
a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
Требуется найти N-е число Фибоначчи
Input: 7
Output: 13
Задание необходимо решать через рекурсию
'''
def fib(number):
    if number in [1, 2]:
        return 1
    return fib(number - 1) + fib(number - 2)
    
print(fib(7))

'''
Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все
максимальные – на минимальные.
Input: 5 -> 1 3 3 3 4
Output: 1 3 3 3 1
'''
import random
size_marks = int(input('Введите кол-вл оценок: '))
list_marks = [random.randint(1,5) for _ in range(size_marks)]
# minNum = min(list_marks)
# maxNum = max(list_marks)

def max_min_search(list_1):
    min_num = list_1[0]
    max_num = list_1[0]
    for num in list_1[1:]:
        if num < min_num:
            min_num = num
        if num > max_num:
            max_num = num
    return min_num, max_num

minNum, maxNum = max_min_search(list_marks)
def change(minimum, maximum, lst):
    for i in range(len(lst)):
        if lst[i] == maximum:
            lst[i] = minimum
    return lst

print(*list_marks)
list_marks_2 = change(minNum, maxNum, list_marks)
print(*list_marks_2)
'''
Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число)
Input: 5
Output: yes
'''

def is_number_simple(num: int) -> bool:
    if num % 2 == 0 and num != 2:
        return False
    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False
    return True


n = int(input('Введите число: '))
if is_number_simple(num=n):
    print(f'Число {n} является простым')
else:
    print(f'Число {n} простым не является')

'''
Дано натуральное число N и последовательность из N элементов.
Требуется вывести эту последовательность в обратном порядке.
Примечание. В программе запрещается объявлять массивы и использовать циклы
(даже для ввода и вывода).
Input: 5 -> 3 4 5 7 8
Output: 8 7 5 4 3
'''
# from random import randint as rnd

n = int(input('Введите кол-во чисел в строке: '))

def print_nums(num: int):
    if num == 0:
        return ''
    line = input('Введите число: ')
    return print_nums(num - 1) + line

print(print_nums(n))