# Урок 3. Функции, рекурсия, алгоритмы

# ФУНКЦИИ
def sumNum(n, y):
    print(y)
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum

a = sumNum(5, 'QWERTY')
print(a)

def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'r', 'f'))

# МОДУЛЬНОСТЬ

import modul_lec_3

print(modul_lec_3.max(5, 9))

from modul_lec_3 import max
print(max(10, 9))

from modul_lec_3 import *
print(max(10, 19))

import modul_lec_3 as m1
print(m1.max(5, 8))

# РЕКУРСИИ

def fib(n):
    if n in [1, 2]: # БАЗИС ОБЯЗАТЕЛЕН ДЛЯ РЕКУРСИИ - Выход из рекурсии
        return 1
    return fib(n-1) + fib(n-2)
list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)

# АЛГОРИТМЫ СОРТИРОВКИ
# БЫСТРАЯ СОРТИРОВКА (что-то большое поделить на маленькие - разделяй и влавствуй)

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([10, 5, 2]))

# СОРТИРОВКА СЛИЯНИЯ 
# (БОЛЬШОЙ СПИСОК / 2 / 2 / 2 - ДЕРЕВО, СОЗДАНИЕ ПАР)

def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        rigth = nums[mid:]
        merge_sort(left)
        merge_sort(rigth)
        i = j = k = 0
        while i < len(left) and j < len(rigth):
            if left[i] < rigth[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = rigth[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(rigth):
            nums[k] = rigth[j]
            j += 1
            k += 1

list_2 = [1, 5, 6, 9, 7, 8, 2, 1, 55, 2, 4]
merge_sort(list_2)
print(list_2)