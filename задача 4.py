import random as r


def merge(lst, start, end):
    '''Функця сортировки слиянием'''
    if end - start > 1:
        middle = (start + end) // 2
        merge(lst, start, middle)
        merge(lst, middle, end)
        join(lst, start, middle, end)


def join(lst, start, middle, end):
    '''Функця слияния'''

    left = lst[start:middle]
    right = lst[middle:end]
    k = start
    i = 0
    j = 0
    while (start + i < middle and middle + j < end):
        if (left[i] <= right[j]):
            lst[k] = left[i]
            i += 1
        else:
            lst[k] = right[j]
            j += 1
        k += 1
    if start + i < middle:
        while k < end:
            lst[k] = left[i]
            i += 1
            k += 1
    else:
        while k < end:
            lst[k] = right[j]
            j += 1
            k += 1


lst = []
for i in range(10 ** 6):
    lst.append(r.randint(13, 25))
merge(lst, 0, 10 ** 6)
print(lst)
