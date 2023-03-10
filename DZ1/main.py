# Задача 2: Найдите сумму цифр трехзначного числа
a = input('Введите трехзначное число: ')
result = list(map(int, a))
summ = sum(result)
# summ = int(a%100/10) + int(a%10) + int(a/100)
print(summ)
