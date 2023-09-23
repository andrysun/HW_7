# # Урок 4. Функции высшего порядка, работа с файлами

def f(x):
    return x * x
a = f #ссылка на функцию
print(type(f))


def calk1(a, b):
    return a + b
def calk2(a, b):
    return a * b
def math(op, x, y):
    print(op(x, y))
math(calk1, 5, 45)

# Лямда функции

calk1 = lambda a, b: a + b
print(calk1(5, 45))

'''
1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
(число; квадрат числа).
Пример: 1 2 3 5 8 15 23 38
Получить: [(2, 4), (8, 64), (38, 1444)]
'''

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = []

for i in data:
    if i % 2 == 0:
        res.append((i, i ** 2))

print(res)

def select(f, col):
    return [f(x) for x in col]

def where(f, col):
    return [x for x in col if f(x)]

data = [1, 2, 3, 5, 8, 15, 23, 38]
res = select(int, data)
print(res)
res = where(lambda x: x % 2 == 0, res)
print(res)
res = list(select(lambda x: (x, x ** 2), res))
print(res)

list_1 = [x for x in range(1, 5)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)

data = '15 156 96 3 5 8 52 5'
# data = data.split()
# print(data)

data = list(map(int, data.split()))
print(data)



data = [15, 65, 9, 36, 175]
res = list(filter(lambda x: x % 10 == 5, data))
print(res)
