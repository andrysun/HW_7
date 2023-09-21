# Задача 1 
'''
По данному целому неотрицательному числу n вычислите значние n!
'''
print("ЗАДАЧА №1")
n = input("Введите значение n: ")
i = 1
k = 1
while (i <= int(n)):
    k = k * i
    i += 1
print(f" n! = {k}")
print("-----------------------------------------------------------------------------------------------------------------")
#Задача 2
'''
Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. Если А не
является числом Фибоначчи, выведите число -1.
'''
print("ЗАДАЧА №2")
a = input("Введите число А: ")
flag = False
count = 0
i = 1
res = 0

if a.isdigit() == True and int(a) > 1:
    a = int(a)
    while res <= a:
        res += i
        i = res - i
        count += 1
        if i != a != res:
            flag = False
        else:
            flag = True
    if flag == True:
        print(f"Натуральное число {a} является числом Фибонначи по счёту {count}")
    else:
        print(f"Натуральное число {a} не является числом Фибонначи")
else:
    print("Ошибка ввода")
print("-----------------------------------------------------------------------------------------------------------------")
#Задача 3
'''
Задайте список из нескольких чисел. Напигите программу,
которая найдёт сумму элементов списка, стоящих на нечётных позициях.
[2, 3, 5, 9, 3] -> 3, 9 -> 3 + 9 = 12
'''
print("ЗАДАЧА №3")
s = [2, 3, 5, 9, 3]
print(f"список в обратном порядке - {s[::-1]}")#список в обратном порядке
print(f"сумма чисел на нечетных позициях - {sum(s[1::2])}")
print("-----------------------------------------------------------------------------------------------------------------")
#Задача 4
'''
Задача с орлами и решками
'''
print("ЗАДАЧА №4")
s = 'OOPPOPOPPOOPOOPOPPO'
n = 0
print("P" in s) #наличие определенных символов в строке
while 'P'*n in s:
    n += 1
print(n - 1)
print("-----------------------------------------------------------------------------------------------------------------")