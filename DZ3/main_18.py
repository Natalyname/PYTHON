# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

from random import randint

N = int(input("Введите количество элементов в массиве: "))

a = [randint(1, 100) for _ in range(N)]

print(f'Исходный массив: {a}')

x = int(input("Введите искомое число: "))

# Поиск элемента, ближайшего по величине к заданному числу
min_difference = abs(x - a[0])
closest_element = a[0]

for element in a:
    difference = abs(x - element)
    if difference < min_difference:
        min_difference = difference
        closest_element = element

print(f'Элемент массива, ближайший по величине к числу {x} - {closest_element}')