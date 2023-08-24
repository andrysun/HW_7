# n = int(input("Введите число: "))
# print(f"{n} * 2 = {n * 2}")
# print("Рассмотрим виды деления")
# print(5 // 2) # целочисленное деление
# print(5 / 2)  # деление с дробной частью
# print(5 % 2)  # остаток от деления

# Задача №1. Решение в группах
# За день машина проезжает n километров. Сколько дней нужно, чтобы проехать маршрут длиной m километров?
# При решении этой задачи нельзя пользоваться условной инструкцией if и циклами.
'''
n = int(input("Сколько километров в день проезжает машина? "))
m = int(input("Какова длина маршрута (в км)? "))
print((m + n - 1) // n)
'''
# Задача №2. Решение в группах
# В некоторой школе решили набрать три новых математических класса и оборудовать кабинеты для них новыми партами.
# За каждой партой может сидеть два учащихся. Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.
'''
a = int(input("Введите количество учеников в 1-ом классе: "))
b = int(input("Введите количество учеников в 2-ом классе: "))
c = int(input("Введите количество учеников в 3-ем классе: "))

print(a // 2 + a % 2 + b // 2 + b % 2 + c // 2 + c % 2)
'''
# Задача №3. Решение в группах
# Вагоны в электричке пронумерованы натуральными числами, начиная с 1 
# (при этом иногда вагоны нумеруются от «головы» поезда, а иногда – с «хвоста»; 
# это зависит от того, в какую сторону едет электричка). В каждом вагоне написан его номер. 
# Витя сел в i-й вагон от головы поезда и обнаружил, что его вагон имеет номер j. 
# Он хочет определить, сколько всего вагонов в электричке. Напишите программу, которая будет это делать или сообщать, 
# что без дополнительной информации это сделать невозможно.
'''
i = int(input("Введите в какой вагон Вы попали: "))
j = int(input("Введите вагон поезда: "))
if i == j:
    print("Нужна дополнительная информация")
else:
    print(i + j - 1)
'''
# Задача №4. Решение в группах
# Дано натуральное число. Требуется определить, является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарем, год является високосным, 
# если его номер кратен 4, но не кратен 100, а также если он кратен 400.
'''
year = int(input("Введите год. Программа определит: високосный ли этот год: "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("YES")
else:
    print("NO")
'''