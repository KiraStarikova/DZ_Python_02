'''Реализуйте алгоритм перемешивания списка.'''


def shuff(a):
    import random
    b = a[:]
    random.shuffle(b)
    return b

a = shuff([23, 1.36, 3, -4, 78])
print (a)