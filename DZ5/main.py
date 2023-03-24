# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в
# целую степень B с помощью рекурсии.


def power(A, B):
    if B == 0:
        return 1
    elif B % 2 == 0:
        return power(A, B//2)**2
    else:
        return A * power(A, B-1)

A = int(input("Введите число A: "))
B = int(input("Введите степень, в которую нужно возвести число: "))

result = power(A, B)
print(f"{A} в степени {B} равно {result}")
