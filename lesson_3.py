'''
Дан список чисел. Определите, сколько в нем встречается различных чисел.
Input: [1, 1, 2, 0, -1, 3, 4, 4]
Output: 6
'''
list_nums = []
size = int(input('Введите количество чисел, которые вы введёте: '))
for i in range(size):
    list_nums.append(int(input('Введите число: ')))
# print(*list_nums)
set_nums = set(list_nums)
# print(len(set(list_nums))) # set() превращает лист в множество
print(len(set_nums))

'''
Дана последовательность из N целых чисел и число
K. Необходимо сдвинуть всю последовательность
(сдвиг - циклический) на K элементов вправо, K –
положительное число.
Input: [1, 2, 3, 4, 5] k = 3
Output: [3, 4, 5, 1, 2]
'''

size_n = int(input('Введите сколько чисел вы введёте: '))
k = int(input('Введите сдвиг последовательности: '))

list_1 = [int(input('Введите число: ')) for _ in range (1, size_n + 1)]

list_2 = []
list_2 = list_1[-k:] + list_1[:-k] # срезы
print(list_2)

'''
Напишите программу для печати всех уникальных
значений в словаре.
Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
":" S007 "}]
Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

lib = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
       {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

res_list = []
for cur_dict in lib:
    for key in cur_dict:
        res_list.append(cur_dict[key])
res_set = set(res_list)
print(res_set)

'''
Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество
элементов массива, больших предыдущего (элемента с предыдущим номером)
Input: [0, -1, 5, 2, 3]
Output: 2 (-1 < 5, 2 < 3)
'''
num_list = [0, -1, 5, 2, 3]
count = 0

for i in range(len(num_list) - 1):
    if num_list[i] < num_list[i + 1]:
        count += 1

print(count)

res_num_list = [num_list[i + 1] for i in range(len(num_list) - 1) if num_list[i] < num_list[i + 1]]