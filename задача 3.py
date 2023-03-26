d = []
flag = True
zayavki = [(12, 15), (17, 18), (19, 20)]
'''определяем хватит ли ракет'''
for i in zayavki:
    x = [j for j in range(i[0], i[1])]
    for a in x:
        if a in d:
            flag = False
            break
        else:
            d.append(a)
print("Хватит" if flag else "Не хватит одной ракеты")
