# # 2 (25122020)
# (a → b)  ¬ (b ≡ c)  (d → a)
# print('a b c d')
# for a in range(2):
#    for b in range(2):
#        for c in range(2):
#            for d in range(2):
#                if (a <= b) and (not(b == c)) and (d <= a):
#                    print(a, b, c, d)

# # 15 (# # 5 (25122020))
# def dell(n, m):
#    return n % m == 0
# A = 1
# while True:
#   miss = False
#    for x in range(1, 10**5):
#        if not((dell(A, 5)) and ((not dell(2020, A)) <= (dell(x, 1718) <= dell(2023, A)))):
#            miss = True
#            break
#    if not miss:
#        print(A)
#    A += 1

# # 5 (25122020)
# def cut(n1):
#     n1 = n1[2] + n1[3] + n1[4] + n1[5] + n1[6] + n1[7] + n1[8] + n1[9]
#     return n1
#
# countOfOne = 0
# n = 0
# n0 = 0
# for x in range(150, 250):
#     n0 = int(cut(bin(x)))
#     n = n0 // 100
#     n = (n * 10 + ((n // 10) % 10)) * 10 + ((n // 10000) % 10)
#     print(x, bin(x), n0, n)
#     if n == n0:
#         countOfOne += 1;
# print(countOfOne)
#
# def oneCounter(s, search):
#     count = 0
#     for x in s:
#         if x == search:
#             count += 1
#     return count
#
# countOfOne = 101
# s = '1' * countOfOne
# while 1:
#     while s.count('111') > 0:
#         s = s.replace('111', '2', 1)
#         s = s.replace('2222', '333', 1)
#         s = s.replace('33', '1', 1)
#     print('New:', s)
#     print('Original string:\t\t  ', countOfOne, '\nNew stirng\'s count of \'1\':', oneCounter(s, '1'))
#     print('-' * 32);
#     countOfOne += 1
#     s = '1' * countOfOne
#     count = 0

# # 14 (25122020)
# s = oct(64**150 + 4**300 - 32)
# count = 0
# for x in s:
#     if x == '7':
#         count += 1
# print(count)
#
# print(oct(64**150 + 4**300))
# print(s)

# # 22 (25122020)
# def F(n):
#     if n <= 15:
#         return n**2 + 11
#     elif (n > 15) and (n % 2 == 0):
#         return F(n // 2) + n**3 - 5 * n
#     elif (n > 15) and (n % 2 == 1):
#         return F(n - 1) + 2 * n + 3
#     else:
#         return None
#
# count = 0
# for n in range(1, 1000):
#     if str(F(n)).count('6') >= 3:
#         count += 1
#
# print(count)

# # 23 (25122020)
# def notMySolution():
#     a = []
#
#     for count in range(0, 8):
#         a.append([0]*100)
#
#     a[0][3] = 1
#
#     for count in range(7):
#         for j in range(27):
#             a[count + 1][j + 1] += a[count][j]
#             a[count + 1][j + 4] += a[count][j]
#             a[count + 1][j * 2] += a[count][j]
#         print(a[count + 1])
#
#     print(a[7][27])
#
# def F(number):
#     b = 3
#     buf = ''
#
#     while number != '0':
#         buf += str(int(number) % 3)
#         number = str(int(number) // 3)
#
#     number = buf[::-1]
#
#     for n in number:
#         if n == '0':
#             b += 1
#         elif n == '1':
#             b += 4
#         elif n == '2':
#             b *= 2
#     return b
#
# c = 0
# for x in range(729, 2187):
#     #print(F(str(x)))
#     if F(str(x)) == 27:
#         c += 1
# print(c)
#
# #notMySolution()

# 24 (25122020)
# alp = 'QWERTYUIOPASDFGHJKLZXCVBNM'
# a = [0]*26
# file = open('24.txt')
#
# s = file.readline()
#
# for x in range(len(s) - 1):
#     if s[x] == 'X':
#         a[alp.find(s[x + 1])] += 1
# print(a)
# max = 0
# for x in a:
#     if max < x:
#         max = x
# print(max)
# file.close()

# # 25 (25122020)
# for x in range(1000000, 1500000):
#     max = 0
#     count = 0
#     for z in range(int(x**0.5), int(x**0.5) - 110, -1):
#         if x % z == 0 and (x // z) - z <= 110:
#             count += 1
#             max = x // z # Последнее частное будет пнаибольшим
#     if count >= 3:
#         print(x, max)

# 26 (25122020)
# f = open('26.txt', 'r')
# n, m = (f.readline()).split(' ') # n — общее кол-во грузов, m — грузоподъёмность
# n, m = int(n), int(m)
# a = [0]*n
# a1 = []
# i1 = 0
# for count in range(0, n):
#     a[count] = int(f.readline())
# a.sort()
# i0 = a.index(310)
# x = a[i0]
# while 310 <= x <= 320:
#     a1.append(x)
#     a.remove(x)
#     i0 += 1
#     x = a[i0]
#
# print(a1)
# print(a)
# f.close()

# def F(array, firstNumber, lastNumber, excludedNumbers):
#     for count in range(firstNumber, lastNumber + 1):
#         array[count] += array[count - 1]
#         array[count] += array[count - 2]
#         if count % 3 == 0:
#             array[count] += array[count // 3]
#         if count in excludedNumbers:
#             array[count] = 0
#     print('Debug: ', array)
#
# n0 = 4
# n = 23
#
# a = [0]*(n + 1)
# a[n0] = 1
# F(a, n0, 8, [-1])
#
# buff = a[8]
# a = [0]*(n + 1)
# a[8] = buff
#
# F(a, 8, 23, [11, 18])

# print(int('43322', base=5) + 1)
# num = int(input())
# name = input()
# content = {'message': [], 'error': []}
# # далее идет код проверок например:
# if num:
#     if type(num) is int:
#         content['message'].append(f'  - Введено число: {num}')
#     else:
#         content['error'].append(f'  - {num} - это не целое число')
# else:
#     content['error'].append('  - Вы не ввели число')
#
# if name:
#     if len(name) > 3:
#         content['message'].append(f'  - Введено имя: {name}')
#     else:
#         content['error'].append('  - Имя не должно быть короче 3-ёх букв')
# else:
#     content['error'].append('  - Вы не ввели имя')
#
# # в конце кода итоговые проверки и вывод сообщения
# if content['error']:
#     # если есть какие-то ошибки
#     content['error'].insert(0, 'При вводе данных возникли ошибки:\n')
#     result_message = '\n'.join(content['error'])
# else:
#     # если все хорошо.
#     content['message'].insert(0, 'Результаты ввода данных:\n')
#     result_message = '\n'.join(content['message'])
#
# print(result_message)

# x = [[0] * 3] * 10
#
# for row in x:
#     for num in row:
#         print(num, end=' ')
#     print('', end='\n')
#
# print(x)

# №17
# count = 0
# min = 0
# for x in range(95433, 34517, -1):
#     if x % 10 == 5 or x % 10 == 3:
#         if x % 7 != 0 and x % 11 != 0:
#             count += 1
#             min = x
# print(count, min)

# ‼ НЕВЕРНАЯ ВЕРСИЯ ПРОГРАММЫ
# f = open('24 (09.12.2021).txt')
# s = f.readline()
# f.close()
#
# count = 0
# maxCount = 0
# for count in range(len(s) - 3):
#     if s[count] + s[count + 1] + s[count + 2] != 'XYZ':
#         count += 1
#     else:
#         if count > maxCount:
#             maxCount = count
#         count = 0
# print(maxCount)
# ДРУГАЯ ВЕРСИЯ (8561 answer)
# f = open('24 (09.12.2021).txt')
# s = f.readline()
# f.close()
#
# i = 0
# count = 0
# maxCount = 0
# for i in range(len(s) - 3):
#     if s[i] + s[i + 1] + s[i + 2] != 'XYZ':
#         i += 1
#         count += 1
#     else:
#         if count > maxCount:
#             maxCount = i
#         count = 0
# print(maxCount)

# def summDel(n):
#     summ = 0
#     for x in range(2, n):
#         if n % x == 0:
#             summ += x
#     return  summ
#
# start = 136179
# count = 0
# summOfDel = 0
# while count < 4:
#     start += 1
#     summOfDel = summDel(start)
#     if summOfDel % 385 == 91:
#         count += 1
#         print(start, summOfDel)

# f = open('26 (09.12.2021).txt')
# S, N = f.readline().split(' ')
# S, N = int(S), int(N)
# a = [0]*N
#
# for x in range(N):
#     a[x] = int(f.readline())
# f.close()
#
# a.sort()
# print(a)
# summ = 0
# count = 0
# while summ + a[count + 1] < S:
#     summ += a[count]
#     print(a[count], end=' ')
#     count += 1
#     if count % 10 == 0:
#         print('\n', end='')
# summ -= 22
# summ += 33
# # Максимально возм. объём, кол-во файлов никак не сохраняемых.
# print(S - summ, summ, N - count)

# fA = open('27_A  (09.12.2021).txt')
# nA = int(fA.readline())
#
# a = ['0']*3
# b = [0]*3
# summ = 0
# for x in range(nA):
#     a = fA.readline().split(' ')
#     for i in range(len(a)):
#         b[i] = int(a[i])
#
#     summ += min(b)
#
# print(summ, summ % 117, sep=', ',end=' ')
# fA.close()
#
# fB = open('27_B  (09.12.2021).txt')
# nB = int(fB.readline())
#
# a = ['0']*3
# b = [0]*3
# minDiff = 10**6
# summ = 0
# s = [0]*0
# for x in range(nB):
#     a = fB.readline().split(' ')
#     for i in range(len(a)):
#         b[i] = int(a[i])
#
#     summ += min(b)
#     b.sort()
#     if b[1] - b[0] != 0:
#         s.append(b[1] - b[0])
# s.sort()
# i = 0
# while summ + s[i] % 117 == 11:
#     i += 1
# print(summ + s[i], summ + s[i] % 117, sep=', ', end=' ')
# print('\n', s[i])
# fB.close()

# s = int(input())
# n = 1
# while s <= 45:
#     s = s + 4
#     n = n * 2
# print(n)
# i = 0
# p, s = 1, 0
# while s != 5 or p != 24:
#     i += 1
#     x = i
#     p, s = 1, 0
#     while x > 0:
#         if x % 2 == 0:
#             p = p * (x % 10)
#         else:
#             s = s + (x % 10)
#         x = x // 10
#     print(i, p, s, sep=', ', end=';\n')
#
# print(s)
# print(p)
# print(i)

# n = 3*256**320 - 2*64**290 + 4**250 - 1023
# s = ''
# while n != 0:
#     s += str(n % 4)
#     n //= 4
#
# count = 0
# for c in s:
#     if c != '0':
#         count += 1
# print(count)

# 15 задание проверка
# P = [x for x in range(10, 20 + 1)]
# Q = [x for x in range(25, 55 + 1)]
# #A = P + Q
# A = [x for x in range(25, 55 + 1)]
# final = 0
#
# a = []
# for x in range(1, 10**5):
#     if not (not x in A or x in P or x in Q):
#         final += 1
#         a += [x]
#
# print(a)
# print('Final', final)

# s = bin(2**10)
# s = s.replace('0b','')
# print(s)
#
# print(int(s, 2))

# P = [2, 4, 6, 8, 10, 12]
# Q = [4, 8, 12, 116]
# A = Q
# print(A)
# c = 0
# for x in range(1, 10**5 + 1):
#     if not ((x in P) <= ((x in Q) and ((x not in A) <= (x not in P)))):
#         print(x)
#         c += 1
# print('c =', c)
#
# c = 0
# for x in range(1, 10**5 + 1):
#     if not (x not in P or x in Q and x in A):
#         print(x)
#         c += 1
# print('c =', c)

# Задание 24 № 27694 РешуЕГЭ
# import re
#
# s = open('zadanie24_1.txt', 'r').read()
# rRes = re.findall(r'((AB)+)', s) + re.findall(r'((AB)+A)', s)
# #                ABABABAB...                     ABAB<...>A
# answers = []
# for x in rRes:
#     answers.append(x[0])
# print(max(answers))
# print(len(max(answers)))
# Стандартный способ
# count = 0
# maxCount = 0
# s = open('zadanie24_1.txt', 'r').readline()
# for x in range(len(s) - 1):
#     if s[x] + s[x + 1] == 'AB':
#         count += 1
#     elif s[x] + s[x + 1] == 'BA':
#         count += 1
#     else:
#         if maxCount < count:
#             maxCount = count
#         count = 0
# if maxCount < count:
#     maxCount = count
# print(maxCount)

# Задание 24 № 27696
# s = open('zadanie24_2.txt', 'r').readline()
# count = 0
# maxCount = 1 # Хотя бы один символ 'L' есть.
# for x in s:
#     if x == 'L':
#         count += 1
#     else:
#         if count > maxCount:
#             maxCount = count
#         count = 0
# if count > maxCount:
#     maxCount = count
# print(maxCount)

# import re
# s = re.findall(r'L+', open('zadanie24_2.txt', 'r').readline())
# print(len(max(s)))

# s = open('24.txt', 'r').readline()
# array = []
# for x in range(len(s) - 1):
#     if s[x] == 'X':
#         array.append(s[x + 1])
# array.sort()
# maxCh = ''
# maxCount = 1
# Count = 1
# for x in range(len(array) - 1):
#     if array[x] == array[x + 1]:
#         Count += 1
#     else:
#         if maxCount < Count:
#             maxCount = Count
#             maxCh = array[x]
#         Count = 1
#
# if maxCount < Count:
#     maxCount = Count
#     maxCh = array[len(array) - 1]
#
# print(maxCh, maxCount, sep='')