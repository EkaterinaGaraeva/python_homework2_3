# 4. Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

def create_list(number):
    list_of_numbers = [x for x in range(-number, number + 1)]
    print(list_of_numbers)
    multy = 1

    with open('file.txt', 'r') as rn:
        positions = rn.readlines()
        for position in positions:
            position = int(position.replace('\n', ''))
            multy *= list_of_numbers[position]
            print(f'Позиция => {position}, значение => {list_of_numbers[position]}')
    return multy

n = int(input('Введите число: '))
print(f'Произведение => {create_list(n)}')

