# 2 → (4 → 11) → 15
print('Способ через массив.')
def fNull(a, end):
    for x in range(end):
        a[x] = 0
    return a

a = [0]*16
a[2] = 1

for i in range(3, 4 + 1):
    if i % 3 == 0 and i // 3 >= 2:
        a[i] += a[i // 3]
    if i >= 4:
        a[i] += a[i - 2]
    if i >= 3:
        a[i] += a[i - 1]
print('До обнуления:\t', a)
a = fNull(a, 4)
print('После обнуления:', a)

for i in range(4, 11 + 1):
    if i % 3 == 0 and i // 3 >= 2:
        a[i] += a[i // 3]
    if i >= 4:
        a[i] += a[i - 2]
    if i >= 3:
        a[i] += a[i - 1]
print('До обнуления:\t', a)
a = fNull(a, 11)
print('После обнуления:', a)

for i in range(11, 15 + 1):
    if i % 3 == 0 and i // 3 >= 2:
        a[i] += a[i // 3]
    if i >= 4:
        a[i] += a[i - 2]
    if i >= 3:
        a[i] += a[i - 1]
print('Конечный массив:', a)
print('Ответ:', a[len(a) - 1], 'способов получить из двойки пятнадцать.')
print('—' * 20)
print('Рекурсивный способ.')
def f(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    elif x < y:
        return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)

print(f(2, 4) * f(4, 11) * f(11, 15))

# (№ 4036)
# https://kpolyakov.spb.ru/school/ege/gen.php?action=viewAllEgeNo&egeId=23&cat78=on&cat79=on&cat80=on&cat162=on
a = set()
for x1 in range(1, 2 + 1):
    for x2 in range(1, 2 + 1):
        for x3 in range(1, 2 + 1):
            for x4 in range(1, 2 + 1):
                for x5 in range(1, 2 + 1):
                    for x6 in range(1, 2 + 1):
                        for x7 in range(1, 2 + 1):
                            for x8 in range(1, 2 + 1):
                                for x9 in range(1, 2 + 1):
                                    for x10 in range(1, 2 + 1):
                                        for x11 in range(1, 2 + 1):
                                            for x12 in range(1, 2 + 1):
                                                for x13 in range(1, 2 + 1):
                                                    for x14 in range(1, 2 + 1):
                                                        for x15 in range(1, 2 + 1):
                                                            s = str(x1) + str(x2) + str(x3) + str(x4) + str(x5) + str(x6) + str(
                                                                x7) + str(x8) + str(x9) + str(x10) + str(x11) + str(
                                                                x12) + str(x13) + str(x14) + str(x15)
                                                            h = 1
                                                            for c in s:
                                                                if c == '1':
                                                                    h *= 2
                                                                else:
                                                                    h = h * 2 + 1
                                                            a.add(h)

# print(a)
print(len(a))
