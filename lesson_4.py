'''
TASK 1
Напишите программу, которая принимает на вход строку, и отслеживает, сколько раз каждый символ
уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
Input: a a a b c a a d c d d
Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
Для решения данной задачи используйте функцию .split()
'''
string_new = 'a a a b c a a d c d d'.split()
# string_new.split() # ['a', 'a', 'a', 'b', 'c', 'a', 'a', 'd', 'c', 'd', 'd']
dict = {}
for letter in string_new:
    if letter in dict:
        dict[letter] += 1
        print(letter + '_' + str(dict[letter]), end = " ")
    else:
        dict[letter] = 0
        print(letter, end = " ")
print(' ')
'''
TASK 2
Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих
подряд, слова разделены одним или большим числом пробелов. Определите, сколько различных слов
содержится в этом тексте. 
Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea
shells on the sea shore I'm sure that the shells are sea shore shells
Output: 13
'''
text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
lower_text = set(text.lower().split())
print(len(lower_text))
'''
TASK 3
Задача – «На вход программе подаются цифры,как только пользователь введёт 0 ввод прекращается.
Вывести наибольший элемент получившейся последовательности».
Есть два кода с ошибками, нужно определить где ошибок меньше.

n = int(input())                n = int(input())
max_number = 1000               max_number = -1
while n != 0:                   while n < 0:
    n = int(input())                n = int(input())
    if max_number > n:              if max_number < n:
    max_number = n                  n = max_number
print(max_number)               print(n)
'''
n = int(input())
max_number = n
while n != 0:
    if n > max_number:
        max_number = n
    n = int(input())
print(max_number)