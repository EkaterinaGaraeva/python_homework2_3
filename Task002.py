# 2. Напишите программу, которая принимает на вход число N
# и выдает набор произведений чисел от 1 до N.
#
# Пример:
#
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def products(number):
    list_of_products = [1]
    for i in range(2, number + 1):
        list_of_products.append(list_of_products[i-2]*i)
    return list_of_products


n = int(input('Введите число: '))
print(products(n))

