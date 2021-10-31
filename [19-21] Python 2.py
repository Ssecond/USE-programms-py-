# Способ 2-ый, из видео: https://youtu.be/5FeZFxPrUgw
# Ходы: +1 или ×2;
# Игра звершается, когда ∑ всех куч ≥ 74;
# В начале (12;S), где 1 ≤ S ≤ 61
# Найти минимальное кол-во камней, чтобы Ваня выйграл своим 1-ым ходом,, при неуд. ходе Пети.

# Подключение кэширования для того, чтобы в последствии рекурсия выполнялась быстрее
# (уже вычисленные значения не вычисляются повторно)
from functools import lru_cache


def move(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


# Кэшируем функцию «h»
@lru_cache(None)
def f(h):
    if sum(h) >= 74:
        return '[The end]'
    elif any(f(x) == '[The end]' for x in move(h)):
        return 'П1'
    elif all(f(x) == 'П1' for x in move(h)):
        return 'В1'
    elif any(f(x) == 'В1' for x in move(h)):
        return 'П2'
    elif all(f(x) == 'П2' or f(x) == 'П1' for x in move(h)):
        return 'В2'


for s in range(1, 61 + 1):
    h = 12, s
    print(f'[{s}]', f(h))

print('—' * 50)


# Для одной кучки.
# Ходы: +1, или +2, или ×3;
# Игра звершается, когда ∑ всех куч ≥ 54;
# В начале (12;S), где 1 ≤ S ≤ 54
# 19) Найти минимальное кол-во камней, чтобы Ваня выйграл своим 1-ым ходом, при неуд. ходе Пети.
# 20) Два значения S: Петя не выигрывает за один ход И может выйграть 2-ым ходом, незавимо от ходов Вани.
# 21) Найти мин. S, при котором Ваня может выйграть 1-ым или 2-ым ходом,
# но не гарантированно 1-ым.
def moves(h):
    return h + 1, h + 2, h * 3


@lru_cache(None)
def f1(h):
    if h > 54:
        return 'END'
    elif any(f1(x) == 'END' for x in moves(h)):
        return 'П1'
    elif all(f1(x) == 'П1' for x in moves(h)):
        return 'В1'
    elif any(f1(x) == 'В1' for x in moves(h)):
        return 'П2'
    elif all(f1(x) == 'П2' or f1(x) == 'П1' for x in moves(h)):
        return 'В2'


for s in range(1, 54 + 1):
    print(s, f1(s))
