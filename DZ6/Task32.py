# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному
# диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random
my_vars = int(input('Введите количество элементов в списке: '))
my_list = [random.randint(0, 100) for i in range(my_vars)]
print(my_list)
min_number = int(input('Введите минимальное число: '))
max_number = int(input('Введите максимальное число: '))
for i in range(my_vars):
    if min_number <= my_list[i] <= max_number:
        # print(my_list)
        print(f'{i} - индекс числа {my_list[i]}')