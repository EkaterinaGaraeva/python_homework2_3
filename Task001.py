# 1. Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр.
#
# Пример:
#
# - 6782 -> 23
# - 0,56 -> 11

def sum_of_digits(number):
    number = number.replace('.', '')
    number = number.replace(',', '')
    sum = 0
    for i in number:
        sum += int(i)
    return sum


n = input('Введите число: ')
print(f'Сумма цифр числа {n} = {sum_of_digits(n)}')
