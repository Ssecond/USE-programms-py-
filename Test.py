## Аналог try-catch в C#
## Простейший калькулятор
#try:
#    print("Формат ввода: \n[Первое число]\n[Действие]\n[Второе число]");
#    print("Чтобы завершить работу программы, введите что угодно.")
#    while 1:
#        a = int(input());
#        operation = input();
#        b = int(input());

#        if (type(a) is int) & (type(b) is int) & (len(operation) == 1):
#            # Просто Hello World по стандарту.
#            #print("HelloWorld: ", a)

#            # Простенький калькулятор
#            if operation == '+':
#                a += b
#            elif (operation == '-') | (operation == '–') | (operation == '—'):
#                a -= b
#            elif (operation == '/') | (operation == '÷') | (operation == ':'):
#                a /= b
#            elif (operation == '*') | (operation == '•'):
#                a *= b
#            else:
#                print("Error or smth, idk.");
#                break;

#            print("Result:", a)
#        else:
#            raise Exception # throw C#
#except Exception as error:
#    print('Caught this error: ' + repr(error))

# 12 UFE exam.
#s = '1' * 101;
#while (s.find("1111") != -1):
#    s = s.replace("1111", "22", 1);
#    s = s.replace("222", "1", 1);
#print(s);

## 16 UFE exam.
#def F(n):
#    if n < 8:
#        F(2 * n)
#        print(n)
#        F(n + 3)

#F(1);

## 17 UFE exam.
#count = 0;
#min = 5 * 10**10;
#i = 2*10**10
#while i <= 4*10**10:
#    if (i % 7 == 0) & (i % 100000 == 0) & (i % 13 != 0) & (i % 29 != 0) & (i % 43 != 0) & (i % 101 != 0):
#        count += 1;
#        if (i < min):
#            min = i;
#    i += 100000;
#print(str(count) + str(min));

## 2 UFE exam.
## ((y → z) ∨ (¬x ∧ w)) ≡ (w ≡ z)
#i = 0;
#print('     x y z w');
#for x in range(2):
#    for y in range(2):
#        for z in range(2):
#            for w in range(2):
#                if ((not(y) or z) or (not(x) and w)) == (w == z):
#                    i += 1;
#                    print('[' + str(i) + ']:', x, y, z, w);
#x = 1;
#a = 0; 
#b = 1; 
#i = 0;
#while 1:
#    a = 0
#    b = 1
#    while x > 0:
#        if x % 2 > 0:
#            a += x % 12
#        else:
#            b *= x % 12
#        x = x // 12
#    x = i
#    if (a == 2) and (b == 10):
#        print(a, b, x)
#    i += 1
#    x = i


#print('f:', a, b, x)

## Встроенные функции перевода в 2, 8, 16 системы исчисления. И функция преобразующая в 10 (int)
#print(bin(2), oct(8), hex(10));
#print(int('30', 30)); # Перевод числа 30₃₀ в 10 систему исчисления
#print(int('100', 2));
#print(float('101.01'))
## Мой калькулятор на системы от 2 до 36.
#x = int(input());
#n = int(input());
#o = '';
#al = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
#while x != 0:
#    o += al[x % n]
#    x //= n;
#print(o[::-1]) # Переворот строки (СТРОКА[::1])

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if x and not(y) and (not(z) or w):
                    print(x, y, z, w)