'''
Задача №47. Решение в группах
У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
программы используется множество раз и вы не хотите ничего сломать):
transformation = <???>
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
transormed_values = list(map(transformation, values))
Единственный способ вашего взаимодействия с этим кодом - посредством задания
функции transformation.
Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
список значений, а нужно получить его как есть.
Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
копией values.

Ввод:
    values = [1, 23, 42, 'asdfg']
    transformed_values = list(map(trasformation, values))
    if values == transformed_values:
        print('ok')
    else:
        print('fail')
Вывод:
ok
'''

transformation = lambda x: x
values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
transformed_values = list(map(transformation, values))
print(transformed_values)
if values == transformed_values:
    print('ok')
else:
    print('fail')
print(transformation)

'''
Задача №49. Решение в группах
Дан список размеров(длина, ширина) эллипсов
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
Напишите функцию find_farthest_orbit(list_of_orbits), которая находит площадь самого большого эллипса и возвращает кортеж с его размерами.
Площадь эллипса вычисляется по формуле S = pi*a*b, где a и b – длины и ширина осей эллипса
- Площадь кругов учитывать не нужно, т.е если у эллипса a == b, то это круг.
При решении задачи используйте списочные выражения.
Гарантируется, что самый большой эллипс всего один.
Ввод:
orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(*find_farthest_orbit(orbits))
Вывод:
2.5 10
'''
def find_farthest_orbit(list_of_orbits):
    pi = 3.14
    # list_of_orbits = [pair for pair in list_of_orbits if pair[0] != pair[1]]
    list_of_orbits = list(filter(lambda pair: pair[0] != pair[1], list_of_orbits))
    list_areas = [pair[0] * pair[1] * pi for pair in list_of_orbits]
    max_area = max(list_areas)
    max_area_index = list_areas.index(max_area)
    return list_of_orbits[max_area_index]

orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
print(find_farthest_orbit(orbits))

'''
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
Ввод:                                        Вывод:
values = [0, 2, 10, 6]                       same
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')
'''

def same_by(characteristic, objects):
    result_list = list(filter(characteristic, objects))

    if objects == result_list or result_list == []:
        return True
    return False

values = [0, 2, 10, 6]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')

# def same_by(characteristic, objects):
#     result_list = []
#     for num in objects:
#         if characteristic(num):
#             result_list.append(num)
#     if objects == result_list or result_list == []:
#         return True
#     return False


# def same_by(characteristic, objects):
#     result_list = list(map(characteristic, objects))

#     if len(objects) == sum(result_list) or sum(result_list) == 0:
#         return True
#     return False