'''
# Списки

list_1 = [] # создание пустого списка
list_2 = list() # создание пустого списка, с помощью функции

list_3 = [1, 2, 3, 8] 
print(list_3) # вывод списка с квадратными скобками
print(*list_3) # вывод списка без квадратными скобками, просто значения
# цикл for
for i in list_3:
    print(i)
print(len(list_3)) # 4
print(list_3[3]) # 8

list_4 = [1, 5]
print(list_4)
list_4.append(8) # добавление значений в конец списка
print(list_4)
'''
'''
list = []
print(list)
for i in range(5):
    list.append(i)
    print(list)
'''
'''
Удаление последнего элемента списка - pop
list = [1, 7, 8, 89, 0, 2]
print(list.pop()) # 2
print(list) # [1, 7, 8, 89, 0]
print(list.pop()) # 0
print(list) # [1, 7, 8, 89]
print(list.pop()) # 89
print(list) # [1, 7, 8]
print(list.pop()) # 8
print(list) # [1, 7]
print(list.pop()) # 7
print(list) # [1]

Удаление конкретного элемента из списка
list = [2, 5, 0, 7]
print(list.pop(0)) # 2
print(list) # [5, 0, 7]

Добавление элемента на нужную позицию - insert(позиция, значение)

list = [2, 5, 0, 7]
print(list.insert(2, 11))
print(list) # [2, 5, 11, 0, 7]

Работа со срезами
list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list[0]) # 1
print(list[1]) # 2
print(list[-1]) # 10
print(list[-5]) # 6
print(list[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [начало списка:конец списка]
print(list[:2]) # [1, 2]
print(list[len(list)-2:]) # [9, 10]
print(list[2:9]) # [3, 4, 5, 6, 7, 8, 9]
print(list[0:len(list):6]) # [1, 7]
print(list[::6]) # [1, 7] шаг - 6

Кортежи - неизменяемый список

t = () # создание пустого кортежа
print(type(t)) # <class 'tuple'>

t = (1)
print(type(t)) # <class 'int'>

t = (1, )
print(type(t)) # <class 'tuple'>

v = [1, 8, 9]
print(v) # [1, 8, 9]
print(type(v)) # <class 'list'>

v = tuple(v)
print(v) # (1, 8, 9)
print(type(v)) # <class 'tuple'>

a, b, c = v
print(a, b, c) # 1 8 9

t = (1, 2, 4, 5,)
print(t[1]) # 2

for i in t:
    print(i) 
for i in range(len(t)):
    ptint(t[i])
#1
#2
#4
#5

Словари - неупорядоченные коллекции произвольных объектов
с доступом по ключу

d = {} # пустой слова
d = dict()

d['q'] = 'qwerty' # {'q' : 'qwerty'}
d['w'] = 'werty' # {'w' : 'werty'}

print(d['q']) # qwerty

for item in d:
    print('{}: {}'.format(item, d[item])) # вывод ключей

for (k,v) in d.item():
    print(k,v)

Множества - элементы не могут повторяться

colors = {'red', 'green', 'blue'}
print(colors)
colors.add('red')
print(colors) # {'red', 'green', 'blue'}
colors.add('gray')
print(colors) # {'red', 'green', 'blue', 'gray'}
colors.remove('red')
print(colors) # {'green', 'blue', 'gray'}
colors.discard('red') # удаление, если есть в множеств, пропуск, если нет
colors.clear()
print(colors) # set()

d = set() # создание пустого множества
a = {1, 2, 3, 5, 8}
b = {2, 5, 8, 13, 21}
c = a.copy() # c = {1, 2, 3, 5, 8}
u = a.union(b) # u = {1, 2, 3, 5, 8, 13, 21}
i = a.intersection(b) # i = {2, 5, 8}
dl = a.difference(b) # dl = {1, 3}
dr = b.difference(a) # dr = {13, 21}
q = a.union(b).difference(a.intersection(b)) # {1, 3, 13, 21}

Замороженное множество
a = {1, 8, 6}
b = frozenset(a)
print(b) # frozenset({8, 1, 6})
'''