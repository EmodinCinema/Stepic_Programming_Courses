# n = int(input())
# num = 0
# for i in range(n):
#     num += int(input())
# print(num)
# ---------------------------------------------------------------------------------------------------

# x = [1, 2, 3]
# z = [1, 2, 3]
# y = x
# print(id(x))
# print(id(y))
# print(id(z))
# print(id([1, 2, 3]))
# print(type(id(x)))
# ---------------------------------------------------------------------------------------------------
# objects = [1, 2, 1, 2, 3]
# spis = []
# a = 0
# for obj in objects:
#     if obj not in spis:
#         spis.append(obj)
#     else:
#         for s in spis:
#             if obj is s == True:
#                 a+=1
#                 break
# print(len(spis))
# print(a)

# s=set()
# for obj in objects:
#     if id(obj) not in s:
#         s.add(id(obj))
# print(len(s))

# s = []
# for obj in objects:
#     if id(obj) not in s:
#         s.append(id(obj))
# print(len(s))
# ---------------------------------------------------------------------------------------------------
# n = int(input())


# def closest_mod_5(x):
#     while True:
#         if x % 5 == 0:
#             return x
#         x += 1


# print(closest_mod_5(n))
# ---------------------------------------------------------------------------------------------------
# n, k = (int(i) for i in input().split())


# def Cnk(n, k):
#     if k == 0:
#         return 1
#     elif k > n:
#         return 0
#     else:
#         return Cnk(n-1, k)+Cnk(n-1, k-1)

# print(Cnk(n,k))
# ---------------------------------------------------------------------------------------------------
# n = int(input())
# builtins = dict()


# def create_space(namespace, parent=None):
#     builtins[namespace] = {'variables': [],
#                            'parent': parent}


# def add_variable_in_spase(namespace, var):
#     for key in builtins.keys():
#         if key in namespace:
#             builtins[key]['variables'].append(var)


# def get_space(namespace, var):
#     print('---', namespace, var)
#     if var in builtins[namespace]['variables']:
#         return namespace
#     elif builtins[namespace]['parent'] is None:
#         return 'None'
#     return get_space(builtins[namespace]['parent'], var)


# if 1 <= n <= 100:
#     create_space('global')
#     for i in range(n):
#         cmd, namespace, arg = [str(stroc) for stroc in input().split()]
#         if cmd == 'create':
#             create_space(namespace, arg)
#         elif cmd == 'add':
#             add_variable_in_spase(namespace, arg)
#         elif cmd == 'get':
#             print(get_space(namespace, arg))
#         print('-', builtins)
# ---------------------------------------------------------------------------------------------------

# class MoneyBox:
#     def __init__(self, capacity):
#         # конструктор с аргументом – вместимость копилки
#         self.capacity = capacity

#     def can_add(self, v):
#         # True, если можно добавить v монет, False иначе
#         # print(v, self.capacity)
#         if v <= self.capacity:
#             return True
#         else:
#             return False

#     def add(self, v):
#         # положить v монет в копилку
#         if self.can_add(v) == True:
#             self.capacity -= v


# x = MoneyBox(10)

# x.add(3)

# x.add(2)
# x.add(5)
# print(x.can_add(0))
# ---------------------------------------------------------------------------------------------------
# class Buffer:
#     def __init__(self):
#         # конструктор без аргументов
#         self.stolb = []
#         self.stroc = []
#         self.itog = []
#         self.s = 0

#     def add(self, *a):
#         # добавить следующую часть последовательности
#         for index in a:
#             self.stroc.append(index)
#             if len(self.stroc) == 5:
#                 self.stolb.append(self.stroc)
#                 self.stroc = []
#         # print(self.stolb)

#         for i in self.stolb:
#             for j in i:
#                 self.s += j
#             if self.s not in self.itog:
#                 self.itog.append(self.s)
#             self.s = 0
#         self.stolb = []
#         print(*self.itog)

#     def get_current_part(self):
#         # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
#         return self.stroc


# buf = Buffer()
# buf.add(1, 2, 3)
# print(buf.get_current_part())  # вернуть [1, 2, 3]
# buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
# print(buf.get_current_part())  # вернуть [6]
# buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
# print(buf.get_current_part())  # вернуть []
# # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# print(buf.get_current_part())  # вернуть [1]
# ---------------------------------------------------------------------------------------------------
# class Buffer:
#     def __init__(self):
#         # конструктор без аргументов
#         self.stroc = []
#         self.itog = 0

#     def add(self, *a):
#         # добавить следующую часть последовательности
#         for index in a:
#             self.stroc.append(index)
#             if len(self.stroc) == 5:
#                 for s in self.stroc:
#                     self.itog += s
#                 print(self.itog)
#                 self.stroc = []
#                 self.itog = 0

#     def get_current_part(self):
#         # вернуть сохраненные в текущий момент элементы последовательности в порядке, в котором они были добавлены
#         return self.stroc


# buf = Buffer()
# buf.add(1, 2, 3)
# print(buf.get_current_part())  # вернуть [1, 2, 3]
# buf.add(4, 5, 6)  # print(15) – вывод суммы первой пятерки элементов
# print(buf.get_current_part())  # вернуть [6]
# buf.add(7, 8, 9, 10)  # print(40) – вывод суммы второй пятерки элементов
# print(buf.get_current_part())  # вернуть []
# # print(5), print(5) – вывод сумм третьей и четвертой пятерки
# buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# print(buf.get_current_part())  # вернуть [1]
# ---------------------------------------------------------------------------------------------------
# slov = dict()
# spis = []


# def empty_class(stroc):
#     return stroc, []


# def create_class(par, anc):
#     if par in slov:
#         for a in anc:
#             slov[par] += a
#             # print('+--', a)
#     else:
#         slov[par] = anc
#     # print(anc)
#     # print(slov)


# def search_class(ancestor, parent):
#     global spis
#     if parent in slov:
#         if len(slov.get(parent)) != 0:
#             spis.append(slov.get(parent))
#             # print('- ', ancestor, slov.get(parent))
#             for s in slov.get(parent):
#                 # print('-- ', ancestor, s)
#                 search_class(ancestor, s)
#             # print('--- ', spis)
#             for sp in spis:
#                 # print('---- ', sp)
#                 if ancestor in sp:
#                     return 'Yes'
#     return 'No'


# n = int(input())
# for i in range(n):
#     stroc = str(input())
#     if ':' not in stroc:
#         par, anc = empty_class(stroc.strip())
#     else:
#         par_do, anc_do = stroc.split(':')
#         par = par_do.replace(" ", "")
#         # print(par, '\n', anc_do)
#         anc = anc_do.split()
#         # print(anc)
#     create_class(par, anc)

# c = int(input())
# for j in range(c):
#     ancestor, parent = str(input()).split()
#     if ancestor != parent:
#         print(search_class(ancestor, parent))
#     else:
#         print('Yes')
#     spis = []
#     # print(spis)

# print(par, anc)
# print(slov)
# ---------------------------------------------------------------------------------------------------
# class ExtendedStack(list):
#     def sum(self):
#         # операция сложения
#         top1, top2 = self.pop(), self.pop()
#         self.append(top1+top2)

#     def sub(self):
#         # операция вычитания
#         top1, top2 = self.pop(), self.pop()
#         self.append(top1-top2)

#     def mul(self):
#         # операция умножения
#         top1, top2 = self.pop(), self.pop()
#         self.append(top1*top2)

#     def div(self):
#         # операция целочисленного деления
#         top1, top2 = self.pop(), self.pop()
#         self.append(top1//top2)


# class ExtendedStack(list):
#     def sum(self):
#         # операция сложения
#         self.append(self.pop()+self.pop())

#     def sub(self):
#         # операция вычитания
#         self.append(self.pop()-self.pop())

#     def mul(self):
#         # операция умножения
#         self.append(self.pop()*self.pop())

#     def div(self):
#         # операция целочисленного деления
#         self.append(self.pop()//self.pop())

# # Проверка с помощью входных данных
# ex_stack = ExtendedStack([1, 2, 3, 4, -3, 3, 5, 10])
# ex_stack.div()
# assert ex_stack.pop() == 2
# ex_stack.sub()
# assert ex_stack.pop() == 6
# ex_stack.sum()
# assert ex_stack.pop() == 7
# ex_stack.mul()
# assert ex_stack.pop() == 2
# assert len(ex_stack) == 0
# ---------------------------------------------------------------------------------------------------
# import time


# class Loggable:
#     def log(self, msg):
#         print(str(time.ctime()) + ": " + str(msg))


# class LoggableList(list, Loggable):
#     def append(self, stroc):
#         '''Метод append в классе list использует два аргумента:
#         1. self (сам список)- ссылка на класс.
#         2. p_object- объект, который нужно добавить в список
#         Переопределять его нужно так же.'''
#         super(LoggableList, self).append(stroc)
#         self.log(stroc)


# z = LoggableList()
# z.append('Hello!')
# z.append('Good bye!')
# print(z)
# ---------------------------------------------------------------------------------------------------
# try:
#     foo()
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except AssertionError:
#     print("AssertionError")
# except ArithmeticError:
#     print("ArithmeticError")


# try:
#     foo()
# except ZeroDivisionError:
#     print("ZeroDivisionError")
# except ArithmeticError:
#     print("ArithmeticError")
# except AssertionError:
#     print("AssertionError")
# ---------------------------------------------------------------------------------------------------
# ex_name, mas_hist = list(), list()
# ex_inher = dict()


# def empty_exception(inp):
#     return inp, []


# def create_exception(par, anc):
#     if par not in ex_inher:
#         ex_inher[par] = anc
#     else:
#         for a in anc:
#             ex_inher[par] += a


# def read_exception(inp):
#     global mas_hist
#     if ex_inher.get(inp):
#         for i in ex_inher[inp]:
#             mas_hist.append(i)
#             read_exception(i)


# def seacrh_exception(inp):
#     for i in ex_name:
#         if i in mas_hist:
#             return inp


# n = int(input())
# for i in range(n):
#     inp = str(input())
#     if ':' not in inp:
#         par, anc = empty_exception(inp.strip())
#     else:
#         par_do, anc_do = inp.split(':')
#         par = par_do.replace(" ", "")
#         anc = anc_do.split()
#     create_exception(par, anc)

# m = int(input())
# for j in range(m):
#     inp = str(input())
#     if len(ex_name) != 0:
#         if inp not in ex_name:
#             read_exception(inp)
#             ex = seacrh_exception(inp)
#             if ex != None:
#                 print(ex)
#             # print('---',seacrh_exception(inp))
#             ex_name.append(inp)
#             mas_hist.clear()
#         else:
#             print(inp)
#     else:
#         ex_name.append(inp)


# print(ex_inher)
# print(mas_hist)
# ---------------------------------------------------------------------------------------------------
# class NonPositiveError(Exception):
#     pass


# class PositiveList(list):
#     def append(self, x):
#         if isinstance(x, int) and x > 0:
#             super(PositiveList, self).append(x)
#         else:
#             raise NonPositiveError


# a = PositiveList()
# a.append(5)
# print(a)
# a.append(-7)
# print(a)

# print(AssertionError.mro())
# print(10 % 2)
# ---------------------------------------------------------------------------------------------------
# from datetime import date, timedelta as tm

# yer, mount, do_days = str(input()).split()
# po_days = int(input())

# s = date(year=int(yer), month=int(mount), day=int(do_days))+ tm(days=po_days)
# print(s.strftime('%Y %-m %-d'))

# ---------------------------------------------------------------------------------------------------
# from simplecrypt import decrypt
# import os

# path_to = os.path.join('passwords.txt')
# path_inf = os.path.join('encrypted.bin')
# spis_pas = list()
# text_r, de_text = str(), str()

# with open(path_to, 'r') as file:
#     for f in file:
#         spis_pas.append(f.strip())
# print(spis_pas)

# with open(path_inf, 'rb') as file_inf:
#     text_r = file_inf.read()
# print(text_r)

# for sp in spis_pas:
#     try:
#         de_text = decrypt(sp, text_r).decode('utf8')
#     except:
#         print('-- Неудача: ', spis_pas.index(sp), sp)
#     else:
#         print('---- Рабочий ключ', sp, '\n', de_text, sep='')
#         break
# print('Ответ: ', de_text)

# ---------------------------------------------------------------------------------------------------
# import os
# import simplecrypt

# spis_pas = list()
# path_to = os.path.join('passwords.txt')
# path_inf = os.path.join('encrypted.bin')
# text_r = str()
# de_text = str()

# with open(path_inf, 'rb') as file_inf:
#     text_r = file_inf.read()
# print(text_r)

# with open(path_to, 'r') as file:
#     for f in file:
#         f = f.strip()
#         print('--', f, '\n', text_r, sep='')
#         try:
#             de_text = simplecrypt.decrypt(f, text_r).decode('utf8')
#         except:
#             print('Неудача: ', f)
#         else:
#             print('------', f, '\n', de_text, sep='')
#             break

# Проба
# password='DRezNUVnr2zC0CP'
# ciphertext = simplecrypt.encrypt(password, 'my secret message')
# print(ciphertext)
# plaintext = simplecrypt.decrypt(password, ciphertext).decode('utf8')
# print(plaintext)
# print(de_text)

# Вариант №1 ----------------------------------------------------------------------------------------
# class multifilter:
#     def judge_half(pos, neg):
#         # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
#         if pos >= neg:
#             return True
#         return False

#     def judge_any(pos, neg):
#         # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
#         if pos >= 1:
#             return True
#         return False

#     def judge_all(pos, neg):
#         # допускает элемент, если его допускают все функции (neg == 0)
#         if neg == 0 and pos > 0:
#             return True
#         return False

#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.count = 0
#         self.judge = judge
#         # iterable - исходная последовательность
#         self.iterable = iterable
#         # funcs - допускающие функции
#         self.funcs = funcs

#     def __iter__(self):
#         # возвращает итератор по результирующей последовательности
#         return self

#     def __next__(self):
#         while self.count < len(self.iterable):
#             self.pos = 0
#             self.neg = 0
#             self.count += 1
#             for fn in self.funcs:
#                 if fn(self.iterable[self.count-1]):
#                     self.pos += 1
#                 else:
#                     self.neg += 1
#             # print(self.pos, self.neg)
#             if self.judge(self.pos, self.neg):
#                 return self.iterable[self.count-1]
#         else:
#             raise StopIteration


# def mul2(x):
#     return x % 2 == 0


# def mul3(x):
#     return x % 3 == 0


# def mul5(x):
#     return x % 5 == 0


# a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

# print(list(multifilter(a, mul2, mul3, mul5)))
# # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# # [0, 6, 10, 12, 15, 18, 20, 24, 30]

# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# # [0, 30]

# print(0 % 5)

# Вариант №2 ----------------------------------------------------------------------------------------
# class multifilter:
#     def judge_half(pos, neg):
#         # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
#         if pos >= neg:
#             return True
#         return False

#     def judge_any(pos, neg):
#         # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
#         if pos >= 1:
#             return True
#         return False

#     def judge_all(pos, neg):
#         # допускает элемент, если его допускают все функции (neg == 0)
#         if neg == 0 and pos > 0:
#             return True
#         return False

#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.count = 0
#         self.judge = judge
#         # iterable - исходная последовательность
#         self.iterable = iterable
#         # funcs - допускающие функции
#         self.funcs = funcs

#     def __iter__(self):
#         # возвращает итератор по результирующей последовательности
#         return self

#     def __next__(self):
#         self.pos = 0
#         self.neg = 0
#         if self.count < len(self.iterable):
#             self.count += 1
#             for fn in self.funcs:
#                 if fn(self.iterable[self.count-1]):
#                     self.pos += 1
#                 else:
#                     self.neg += 1
#             # print(self.pos, self.neg)
#             if self.judge(self.pos, self.neg):
#                 return self.iterable[self.count-1]
#             else:
#                 return self.__next__()
#         else:
#             raise StopIteration


# def mul2(x):
#     return x % 2 == 0


# def mul3(x):
#     return x % 3 == 0


# def mul5(x):
#     return x % 5 == 0


# a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

# print(list(multifilter(a, mul2, mul3, mul5)))
# # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# # [0, 6, 10, 12, 15, 18, 20, 24, 30]

# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# # [0, 30]

# Вариант №3 ----------------------------------------------------------------------------------------
# class multifilter:
#     def judge_half(pos, neg):
#         # допускает элемент, если его допускает хотя бы половина фукнций (pos >= neg)
#         if pos >= neg:
#             return True
#         return False

#     def judge_any(pos, neg):
#         # допускает элемент, если его допускает хотя бы одна функция (pos >= 1)
#         if pos >= 1:
#             return True
#         return False

#     def judge_all(pos, neg):
#         # допускает элемент, если его допускают все функции (neg == 0)
#         if neg == 0 and pos > 0:
#             return True
#         return False

#     def __init__(self, iterable, *funcs, judge=judge_any):
#         self.judge = judge
#         # iterable - исходная последовательность
#         self.iterable = iterable
#         # funcs - допускающие функции
#         self.funcs = funcs

#     def __iter__(self):
#         # возвращает итератор по результирующей последовательности
#         return Iterator_multifilter(self.iterable, self.funcs, self.judge)


# class Iterator_multifilter:
#     def __init__(self, iterable, funcs, judge):
#         self.count = 0
#         self.iterable = iterable
#         self.funcs = funcs
#         self.judge = judge

#     def __next__(self):
#         while self.count < len(self.iterable):
#             self.pos = 0
#             self.neg = 0
#             self.count += 1
#             for multifilter.fn in self.funcs:
#                 if multifilter.fn(self.iterable[self.count-1]):
#                     self.pos += 1
#                 else:
#                     self.neg += 1
#             # print(self.pos, self.neg)
#             if self.judge(self.pos, self.neg):
#                 return self.iterable[self.count-1]
#         else:
#             raise StopIteration


# def mul2(x):
#     return x % 2 == 0


# def mul3(x):
#     return x % 3 == 0


# def mul5(x):
#     return x % 5 == 0


# a = [i for i in range(31)]  # [0, 1, 2, ... , 30]

# print(list(multifilter(a, mul2, mul3, mul5)))
# # [0, 2, 3, 4, 5, 6, 8, 9, 10, 12, 14, 15, 16, 18, 20, 21, 22, 24, 25, 26, 27, 28, 30]

# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_half)))
# # [0, 6, 10, 12, 15, 18, 20, 24, 30]

# print(list(multifilter(a, mul2, mul3, mul5, judge=multifilter.judge_all)))
# # [0, 30]
# Вариант №1 ----------------------------------------------------------------------------------------
# import itertools
# from math import factorial as fact


# def primes():
#     p = 1
#     while True:
#         prost = fact(p-1)+1
#         if prost % p == 0 and p > 1:
#             yield p
#         p += 1


# print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# Вариант №2 ----------------------------------------------------------------------------------------
# import itertools


# def primes():
#     p = 2
#     lst = list()
#     while True:
#         st = True
#         if len(lst) != 0:
#             for l in lst:
#                 if p % l == 0:
#                     st = False
#                     break
#         if st:
#             lst.append(p)
#             yield p
#         p += 1


# print(list(itertools.takewhile(lambda x: x <= 31, primes())))
# ---------------------------------------------------------------------------------------------------
# import os

# path_to = os.path.join('dataset_24465_4.txt')
# path_out = os.path.join('Otvet_dataset_24465_4.txt')

# with open(path_to, 'r') as text_to, open(path_out, 'w') as text_out:
#     spis = list()
#     for tx_to in text_to:
#         spis.append(tx_to)
#     print(spis)
#     for s in spis[::-1]:
#         text_out.write(s)
# ---------------------------------------------------------------------------------------------------
# import os
# from zipfile import ZipFile as ZiFi

# spis = list()
# file_name = 'main.zip'
# file_split = os.path.splitext(file_name)

# path_to = os.path.join(file_name)
# path_out = os.path.join(file_split[0] + '_out.txt')

# with ZiFi(path_to, 'r') as zip_f:
#     zip_f.extractall('.')

# for curret_dir, dirs, files in os.walk(file_split[0]):
#     for file in files:
#         name, extention = file.split('.')
#         if extention == 'py' and curret_dir not in spis:
#             spis.append(curret_dir)
#             break

# with open(path_out, 'w') as text:
#     spis.sort()
#     for s in spis:
#         text.write(s + "\n")
# ---------------------------------------------------------------------------------------------------
# def mod_checker(x, mod=0):
#     return lambda y: y % x == mod


# mod_3 = mod_checker(3)

# print(mod_3(3))  # True
# print(mod_3(4))  # False

# mod_3_1 = mod_checker(3, 1)
# print(mod_3_1(4))  # True
# Вариант №1 ----------------------------------------------------------------------------------------
# s = str(input())
# a = str(input())
# b = str(input())


# def replacing_occuren(string, substring,
#                       replacement, count=0):
#     if substring in string and substring in replacement:
#         return 'Impossible'
#     elif substring not in string or substring == replacement:
#         return 0

#     while substring in string:
#         string = string.replace(substring, replacement)
#         count += 1
#     return count


# print(str(replacing_occuren(s, a, b)))
# Вариант №2 ----------------------------------------------------------------------------------------
# s = str(input())
# a = str(input())
# b = str(input())


# def replacing_occuren(string, substring,
#                       replacement, count=0):
#     if substring in string:
#         if substring in replacement:
#             return 'Impossible'
#         while substring in string:
#             string = string.replace(substring, replacement)
#             count += 1
#     return count


# print(str(replacing_occuren(s, a, b)))
# ---------------------------------------------------------------------------------------------------
# s, t = (input() for _ in range(2))


# def palindrome(string, substring, count=0):
#     while substring in string:
#         string = string[string.find(substring) + 1:]
#         count += 1
#     return count


# print(palindrome(s, t))
# Вариант №1 ----------------------------------------------------------------------------------------
# import re
# import sys

# pattern = r'cat'
# for line in sys.stdin:
#     line = line.rstrip()
#     if len(re.findall(pattern, line)) > 1:
#         print(line)
# Вариант №2 ----------------------------------------------------------------------------------------
# import re
# import sys

# pattern = r'(cat.*){2,}'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern, line) is not None:
#         print(line)
# ---------------------------------------------------------------------------------------------------
# import re
# import sys

# pattern = r'\b(cat)\b'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern,line) is not None:
#         print(line)
# ---------------------------------------------------------------------------------------------------
# import re
# import sys

# pattern = r'z.{3}z'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern, line) is not None:
#         print(line)
# ---------------------------------------------------------------------------------------------------
# import re
# import sys

# pattern = r'\\'
# for line in sys.stdin:
#     line = line.rstrip()
#     if re.search(pattern, line) is not None:
#         print(line)
# ---------------------------------------------------------------------------------------------------
# import re
# from sys import stdin


# pattern = r'(\w+)\1\b'
# for line in stdin:
#     line = line.rstrip()
#     # print(re.match(pattern, line))
#     if re.match(pattern, line) is not None:
#         print(line)

# Вариант №1 ----------------------------------------------------------------------------------------
# import re
# from sys import stdin

# pattern = r'human'
# for line in stdin:
#     line = line.rstrip()
#     print(re.sub(pattern, r"computer", line, count=0))

# Вариант №2 ----------------------------------------------------------------------------------------
# import re
# from sys import stdin

# pattern = r'human'
# for line in stdin:
#     line = line.rstrip()
#     line = re.sub(pattern, r"computer", line, count=0)
#     print(line)

# Вариант №2 ----------------------------------------------------------------------------------------
# import re
# from sys import stdin

# pattern_ = r'(a|A)+\b'
# repl_ = r'argh'
# for line in stdin:
#     line = line.rstrip()
#     line = re.sub(pattern_, repl_, line, count=1)
#     print(line)

# Вариант №2 ----------------------------------------------------------------------------------------
# import re
# from sys import stdin

# pattern_ = r'a+\b'
# repl_ = r'argh'
# for line in stdin:
#     line = line.rstrip()
#     line = re.sub(pattern_, repl_, line, count=1, flags=re.IGNORECASE)
#     print(line)

# ---------------------------------------------------------------------------------------------------
# import re
# from sys import stdin

# pattern_ = r'\b(\w)(\w)(\w*)'
# repl_ = r'\2\1\3'
# for line in stdin:
#     line = line.rstrip()
#     line = re.sub(pattern_, repl_, line)
#     print(line)

# ---------------------------------------------------------------------------------------------------
# import re
# from sys import stdin

# pattern_ = r'(\w)\1+'
# repl_ = r'\1'
# for line in stdin:
#     line = line.strip()
#     line = re.sub(pattern_, repl_, line)
#     print(line)

# ---------------------------------------------------------------------------------------------------
# import re
# from sys import stdin

# # r'(0*((1{1,2})0{2})1+)' r'0*((1{1,2})(0{2})+?)1+?'
# pattern_ = r'(1(01*0)*1|0)*'
# for line in stdin:
#     line = line.rstrip()
#     if line.isdigit() and re.match(pattern_, line) is not None:
#         print(line)

# Вариант №2 ----------------------------------------------------------------------------------------
# import re
# import requests

# start_page, final_page = (input() for _ in range(2))


# def search_page_path(start, stop):
#     content_page = requests.get(start).text
#     pattern_ = r'(?:<a href="(.+)")'
#     lst_page = re.findall(pattern_, content_page)
#     if lst_page is not None:
#         for p in lst_page:
#             content_page = requests.get(p).text
#             # print(content_page)
#             lst_page_tow = re.findall(pattern_, content_page)
#             if lst_page_tow is not None:
#                 # print(stop, lst_page_to)
#                 lst = list()
#                 for l in lst_page_tow:
#                     lst.append(l.replace('stepic.org', 'stepik.org'))
#                 if stop in lst:
#                     return 'Yes'
#     return 'No'


# print(search_page_path(start_page, final_page))

# Вариант №2 ----------------------------------------------------------------------------------------
# import re
# import requests

# start_page, final_page = (input() for _ in range(2))


# def search_page_path(start, stop):
#     lst_page = requests_page(start)
#     if lst_page is not None:
#         for p in lst_page:
#             lst_page_tow = requests_page(p)
#             if lst_page_tow is not None:
#                 if stop in lst_page_tow:
#                     return 'Yes'
#     return 'No'


# def requests_page(url):
#     lst_change = list()
#     content_page = requests.get(url).text
#     pattern_ = r'(?:<a href="(.+)")'
#     for l in re.findall(pattern_, content_page):
#         lst_change.append(l.replace('stepic.org', 'stepik.org'))
#     return lst_change


# print(search_page_path(start_page, final_page))

# ---------------------------------------------------------------------------------------------------
# import os
# import re
# import requests

# # Ссылка с готовыми данными: 'http://pastebin.com/raw/7543p0ns'
# # r = requests.get('http://pastebin.com/raw/7543p0ns').text
# inp = str(input())
# r = requests.get(inp).text
# mas = list()

# pattern = r'(?:<a.*href=[\"\'](?:(?:[a-zA-Z]+://)?((?:\w+\-*\w+\.)+[a-z]+)[\'\"\/\:]))'
# findall_object = re.findall(pattern, r)

# if findall_object is not None:
#     for f in findall_object:
#         if f not in mas:
#             mas.append(f.strip())
#     mas = sorted(mas)
# print('\n'.join(mas))

# # # Проверка всё ли подошло с готовыми данными: 'http://pastebin.com/raw/7543p0ns'
# # path_to = os.path.join('ot_main2.txt')
# # with open(path_to, 'r') as file:
# #     count = 0
# #     for f in file:
# #         if f.strip() not in mas:
# #             count += 1
# #             print(count, '-', f, end='')

# Вариант №1 ----------------------------------------------------------------------------------------
# import os
# import csv

# path_to = os.path.join('Crimes.csv')
# yer_of_crime = '2015'
# spis = list()
# ctnoc = dict()

# with open(path_to, 'r') as file:
#     read_file = csv.reader(file)
#     for rf in read_file:
#         if yer_of_crime in rf[2]:
#             spis.append(rf)


# def search_more_crime(spis):
#     max_num_crime = 0
#     for s in spis:
#         if s[5] not in ctnoc:
#             ctnoc[s[5]] = 1
#         ctnoc[s[5]] += 1
#     for key, index in ctnoc.items():
#         if index > max_num_crime:
#             max_num_crime = index
#             name_crime = key
#     return name_crime


# print(search_more_crime(spis))

# Вариант №2 ----------------------------------------------------------------------------------------
# import os
# import csv

# path_to = os.path.join('Crimes.csv')
# yer_of_crime = '2015'
# ctnoc = dict()

# with open(path_to, 'r') as file:
#     read_file = csv.reader(file)
#     for rf in read_file:
#         if yer_of_crime in rf[2]:
#             if rf[5] not in ctnoc:
#                 ctnoc[rf[5]] = 1
#             ctnoc[rf[5]] += 1


# def search_more_crime(slov):
#     max_num_crime = 0
#     for key, index in slov.items():
#         if index > max_num_crime:
#             max_num_crime = index
#             name_crime = key
#     return name_crime


# print(search_more_crime(ctnoc))

# Вариант №1 ----------------------------------------------------------------------------------------
# import json

# inheritance_json = json.loads(input())
# # inheritance_json = [{"name": "B", "parents": ["A", "C"]},
# #                     {"name": "C", "parents": ["A"]},
# #                     {"name": "A", "parents": []},
# #                     {"name": "D", "parents": ["C", "F"]},
# #                     {"name": "E", "parents": ["D"]},
# #                     {"name": "F", "parents": []}]
# slov = dict()


# for inj in inheritance_json:
#     for i in inj["parents"]:
#         if i not in slov:
#             slov[i] = [inj["name"]]
#         if inj["name"] not in slov[i]:
#             slov[i].append(inj["name"])

# for inj in inheritance_json:
#     if inj["name"] not in slov:
#         slov[inj["name"]] = ['object']


# def search_all_ancestors(key, index):
#     global slov
#     # print(index)
#     if index is None:
#         return
#     for i in index:
#         # print(key,'-', i)
#         if i not in slov[key]:
#             if i == 'object':
#                 slov[key].append('object')
#             else:
#                 slov[key].append(i)
#         inx = slov.get(i)
#         search_all_ancestors(key, inx)


# for key, index in slov.items():
#     search_all_ancestors(key, index)
#     # print(spis)
# # print(slov)

# slov_sort = dict(sorted(slov.items()))

# for key, index in slov_sort.items():
#     print(key, ':', len(index))

# Вариант №2 ----------------------------------------------------------------------------------------
# import json


# def classes_and_ancestors():
#     for inj in inheritance_json:
#         for i in inj["parents"]:
#             if i not in slov:
#                 slov[i] = [inj["name"]]
#             if inj["name"] not in slov[i]:
#                 slov[i].append(inj["name"])
#         if inj["name"] not in slov:
#             slov[inj["name"]] = ['object']


# def search_all_ancestors(key, index):
#     if index is None:
#         return
#     for i in index:
#         if i not in slov[key]:
#             slov[key].append(i)
#         inx = slov.get(i)
#         search_all_ancestors(key, inx)


# inheritance_json = json.loads(input())
# slov = dict()

# classes_and_ancestors()
# for key, index in slov.items():
#     search_all_ancestors(key, index)

# slov_sort = dict(sorted(slov.items()))
# for key, index in slov_sort.items():
#     print(key, ':', len(index))

# ---------------------------------------------------------------------------------------------------
# import requests
# import json
# import os


# def search_found(num):
#     params_ = {'default': 'Boring'}
#     api_website = 'http://numbersapi.com/{}/math?json=true'
#     info_website_json = requests.get(api_website.format(num),
#                                      params=params_).text
#     # print(info_website_json)
#     info_website = json.loads(info_website_json)
#     if info_website['found']:
#         return 'Interesting'
#     return 'Boring'


# path_to = os.path.join('dataset_24476_3.txt')
# path_out = os.path.join('dataset_24476_3_otvet.txt')
# with open(path_to, 'r') as text_in, open(path_out, 'w') as text_out:
#     for t in text_in:
#         t = t.strip()
#         print(t)
#         otv = search_found(t)
#         print(otv)
#         text_out.write(otv + '\n')

# ---------------------------------------------------------------------------------------------------
# import os
# import requests
# import json

# slov = dict()
# '''
# Получаем токен для получения доступа к сайту
# https://developers.artsy.net/v2/start?id=234aa43a-d1e3-4433-bcfd-42f544029acb
# '''
# client_id_secret = {'client_id': '0f8cf65e784707e6b735',
#                     'client_secret': '30f277e15c753879fabb293fa04909c0'}
# get_token = 'https://api.artsy.net/api/tokens/xapp_token'
# api_token_json = requests.post(get_token, params=client_id_secret).text
# api_token = json.loads(api_token_json)
# print(api_token)


# def search_artist(id_artist):
#     website = 'https://api.artsy.net/api/artists/{}'
#     headers_ = {"X-Xapp-Token": api_token['token']}
#     api_website_artist_json = requests.get(website.format(id_artist),
#                                            headers=headers_).text
#     info_artist = json.loads(api_website_artist_json)
#     print(info_artist['birthday'], info_artist['sortable_name'])

#     if info_artist['birthday'] not in slov:
#         slov[info_artist['birthday']] = [info_artist['sortable_name']]
#     else:
#         slov[info_artist['birthday']].append(info_artist['sortable_name'])


# path_to = os.path.join('dataset_24476_4.txt')
# path_out = os.path.join('dataset_24476_4_otvet.txt')
# with open(path_to, 'r') as text_to, open(path_out, 'w', encoding='utf-8') as text_out:
#     for to in text_to:
#         to = to.strip()
#         search_artist(to)

#     slov_sorted = dict(sorted(slov.items()))
#     print(slov_sorted)
#     for key, index in slov_sorted.items():
#         if len(index) > 1:
#             index.sort()
#         for i in index:
#             text_out.write(i + '\n')

# ---------------------------------------------------------------------------------------------------
# from xml.etree import ElementTree

# tree = ElementTree.fromstring(input())
# slov = dict()
# value = 0


# def definition_of_value(element):
#     global value
#     value += 1
#     # print(value)
#     # print(element.attrib['color'])
#     if element.attrib['color'] not in slov:
#         slov[element.attrib['color']] = value
#     else:
#         slov[element.attrib['color']] += value
#     for e in element:
#         definition_of_value(e)
#     value -= 1


# definition_of_value(tree)
# print(slov['red'], slov['green'], slov['blue'])

# ---------------------------------------------------------------------------------------------------
"""
Эксперементы с созданием классов на основе словарей
"""
count = 0
slov = {
    'card_3': {'name': 'gib',
               'number': 3,
               'color': 'red',
               'status': 'Warning'},
    'card_4': {'name': 'bib',
               'number': 4,
               'color': 'elov',
               'status': 'Warning'},
    'card_5': {'name': 'blob',
               'number': 5,
               'color': 'green',
               'status': None}
}


class Card():
    count += 1

    def __init__(self, name='card'+'_'+str(count), number=count, color='green', status=None):
        self.number = number
        self.name = name
        self.color = color
        self.status = status


card1 = Card()
print(card1.name, '-', card1.number, card1.color, card1.status)
card2 = Card()
print(card2.name, '-', card2.number, card2.color, card2.status)

# Создание классов из атрибутов словаря
for key, index in slov.items():
    slov[key] = Card(name=index['name'], number=index['number'],
                     color=index['color'], status=index['status'])

# slov['card_3']=Card(name=slov['card_3']['name'], number=slov['card_3']['number'], color=slov['card_3']['color'], status=slov['card_3']['status'])
print(slov['card_3'].name, '-', slov['card_3'].number,
      slov['card_3'].color, slov['card_3'].status)
print(slov['card_4'].name, '-', slov['card_4'].number,
      slov['card_4'].color, slov['card_4'].status)
print('--------')

for key in slov.keys():
    print(slov[key].name, '-', slov[key].number,
          slov[key].color, slov[key].status)
