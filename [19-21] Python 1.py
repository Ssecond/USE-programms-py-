# Способ 1-ый, из видео: https://youtu.be/hSbDxT8i1uY
# Ходы: +2 или ×2;
# Игра звершается, когда ∑ всех куч ≥ 142;
# В начале (2;S), где 1 ≤ S ≤ 138
# Найти минимальное кол-во камней, чтобы Ваня выйграл своим 1-ым ходом, при неуд. ходе Пети.
print('Задача №19')
# p = 1 — исходная позиция, т.е. ничей ход.
def f(x, y, p):
    if x + y >= 142 and p == 3:
        return True
    elif x + y < 142 and p == 3:
        return False
    return f(x + 2, y, p + 1) or f(x, y + 2, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)

# Перебор идёт в диапазоне [1;50], можно больше, можно меньше,
# подбирается в зависимости от условий задачи.
for S in range(1, 50 + 1):
    if f(2, S, 1): # 2 — начальная позиция, (2, S); переменную S перебираем.
        print('[', end='')
        print(2, S, sep=', ', end=']\n')
        break # Т.к. в задаче нужно минимальное значение.

# Найти 2 таких значения S
# Петя не может выйграть за один ход;
# Петя может выйграть совоим вторым ходом независимо от того, как будет ходить Ваня.
print('Задача №20')
# p = 1 — исходная позиция, т.е. ничей ход.
def f(x, y, p):
    if x + y >= 142 and p == 4:
        return True
    elif x + y < 142 and p == 4:
        return False
    elif x + y >= 142:
        return False
    # В случае с решением задачи 20 нужно просчитать выигрышную стратегию
    # для Пети. Его ходы нечетные, в них достаточно подобрать одно значение, но для Вани, у которого ходы четные,
    # нужно просчитать все возможные варианты! Поэтому на четные ходы нужна конъюнкция, а на нечетные достаточно
    # дизъюнкции! Ах да, мы смотрим в следующий ход, поэтому четность проверяется наоборот.
    if p % 2 != 0:
        return f(x + 2, y, p + 1) or f(x, y + 2, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 2, y, p + 1) and f(x, y + 2, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1)

# Перебор идёт в диапазоне [1;100], можно больше, можно меньше,
# подбирается в зависимости от условий задачи.
for S in range(1, 100 + 1):
    if f(2, S, 1): # 2 — начальная позиция, (2, S); переменную S перебираем.
        print('[', end='')
        print(2, S, sep=', ', end=']\n')

# Найти минимальое значение S.
# У Вани есть выйгрышная стратегия, позволяющая ему выйграть 1-ым или 2-ым ходом при любой игре Пети;
# У Вани нет стратегии, которая позволит ему гарантированно выйграть первым ходом.
print('Задача №21')
# p = 1 — исходная позиция, т.е. ничей ход.
def f(x, y, p):
    if x + y >= 142 and (p == 5 or p == 3):
        return True
    elif x + y < 142 and p == 5:
        return False
    elif x + y >= 142:
        return False

    if p % 2 == 0:
        return f(x + 2, y, p + 1) or f(x, y + 2, p + 1) or f(x * 2, y, p + 1) or f(x, y * 2, p + 1)
    else:
        return f(x + 2, y, p + 1) and f(x, y + 2, p + 1) and f(x * 2, y, p + 1) and f(x, y * 2, p + 1)

def f1(x, y, p):
    if x + y >= 142 and p == 3:
        return True
    elif x + y < 142 and p == 3:
        return False
    elif x + y >= 142:
        return False
    # Петины ходы — чётные, а Ванины — не чётные.
    if p % 2 == 0:
        return f1(x + 2, y, p + 1) or f1(x, y + 2, p + 1) or f1(x * 2, y, p + 1) or f1(x, y * 2, p + 1)
    else:
        return f1(x + 2, y, p + 1) and f1(x, y + 2, p + 1) and f1(x * 2, y, p + 1) and f1(x, y * 2, p + 1)

# Перебор идёт в диапазоне [1;100], можно больше, можно меньше,
# подбирается в зависимости от условий задачи.
for S in range(1, 100 + 1):
    if f(2, S, 1): # 2 — начальная позиция, (2, S); переменную S перебираем.
        print('[', end='')
        print(2, S, sep=', ', end=']\n')
print('-'*7)
for S in range(1, 100 + 1):
    if f1(2, S, 1):
        print('[', end='')
        print(2, S, sep=', ', end=']\n')
# В условии на задачу 21 нельзя, чтобы Вани выиграл только лишь в свой первый ход, первая функция считает в том числе
# такие значения. Вторая функция нужна, чтобы определить такие значение! (При которых p=3)
print('Т.е. Значение S = 69 не подходит, т.к. даёт гарантию на победу Вани его 1-ым ходом. Значит, ответ: 66.')