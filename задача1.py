''' считалочка '''
n, k = int(input()), int(input())
a = [i for i in range(1, n + 1)]
while len(a) > 1:
    k1 = k % len(a)
    del a[k1 - 1]
print(a)
