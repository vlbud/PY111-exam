import random as rnd
import networkx as ntw

arr = []
n = int(input("введите размер сетки"))
for i in range(n):
    arr.append([])
    for j in range(n):
        arr[i].append(rnd.randint(1, 100))

k = 1
arr_num = []
n = int(input("введите размер сетки"))
for i in range(n):
    arr_num.append([])
    for j in range(n):
        arr_num[i].append(k)
        k += 1

x1 = int(input("введите исходную строку"))
y1 = int(input("введите исходный столбец"))
x2 = int(input("введите целевую строку"))
y2 = int(input("введите целевой столбец"))

graph = ntw.MultiGraph

for i in arr_num:
    print(i)
print()
for i in arr:
    print(i)

graph = ntw.DiGraph()
lst1 = []
for i in range(n):
    for j in range(n - 1):
        lst1.append((arr_num[i][j], arr_num[i][j + 1], arr[i][j]))

for i in range(n - 1):
    for j in range(n):
        lst1.append((arr_num[i][j], arr_num[i + 1][j], arr[i][j]))

graph.add_weighted_edges_from(lst1)

coasts = ntw.dijkstra_predecessor_and_distance(graph, arr_num[x1][y1])
print(coasts)
n = int(input("введите размер сетки"))
for i in range(n):
    arr.append([])
    for j in range(n):
        arr[i].append(rnd.randint(1, 100))

k = 1
arr_num = []
n = int(input("введите размер сетки"))
for i in range(n):
    arr_num.append([])
    for j in range(n):
        arr_num[i].append(k)
        k += 1

x1 = int(input("введите исходную строку"))
y1 = int(input("введите исходный столбец"))
x2 = int(input("введите целевую строку"))
y2 = int(input("введите целевой столбец"))

graph = ntw.MultiGraph

for i in arr_num:
    print(i)
print()
for i in arr:
    print(i)

graph = ntw.DiGraph()
lst1 = []
for i in range(n):
    for j in range(n - 1):
        lst1.append((arr_num[i][j], arr_num[i][j + 1], arr[i][j]))

for i in range(n - 1):
    for j in range(n):
        lst1.append((arr_num[i][j], arr_num[i + 1][j], arr[i][j]))

graph.add_weighted_edges_from(lst1)

coasts = ntw.dijkstra_predecessor_and_distance(graph, arr_num[x1][y1])
print(coasts)
