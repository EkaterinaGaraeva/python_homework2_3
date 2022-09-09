# 5. Реализуйте алгоритм перемешивания списка.

import time

def new_random(min, max):
    rnd = time.time()
    rnd = rnd - int(rnd)
    rnd = int(rnd * (max - min)) + min
    return rnd

def shuffle_list(one_list):
    size = len(one_list)
    # print(size)
    new_list = []
    print(one_list)
    while size > 0:
        index = new_random(0, size)
        new_list.append(one_list[index])
        one_list.pop(index)
        size -= 1
    return new_list

one_list = [ 1, 4, 98, 'sddsd', True, 'rrr', False]
print(shuffle_list(one_list))
