# a = 5
# while a <= 55:
#     if a % 2 != 0:
#         print(a, sep=' ')
#     a += 1
# ---------------------------------------------------------------------------------------------------

# i = 0
# while i <= 10:
#     i = i + 1
#     if i > 7:
#         i = i + 2
# print(i)
# ---------------------------------------------------------------------------------------------------

# n=int(input())
# star = '*'
# while len(star) <= n:
#     print(star)
#     star += '*'
# ---------------------------------------------------------------------------------------------------

# i = 0
# while i < 5:
#     print('*')
#     if i % 2 == 0:
#         print('**')
#     if i > 2:
#         print('***')
#     i = i + 1
# ---------------------------------------------------------------------------------------------------


# i_lev = int(input('Введите первое число диапозона: '))
# i_prav = int(input('Введите второе число диапозона: '))
# while i_lev <= i_prav:
#     print(i_lev, end=' ')
#     i_lev += 1
# ---------------------------------------------------------------------------------------------------


# num = int(input())
# num_sum = 0
# while num != 0:
#     num_sum += num
#     num = int(input())
# print(num_sum)
# ---------------------------------------------------------------------------------------------------


# per, vtor = int(input()), int(input())
# delitel = 1  # Делитель
# nok = 1
# itog = 1

# if per > vtor:
#     max_n = per
#     min_n = vtor
# else:
#     max_n = vtor
#     min_n = per

# while nok % per != 0 or nok % vtor != 0:
#     nok = min_n*delitel
#     itog = nok % max_n
#     if itog != 0:
#         delitel += 1

#     print('Делитель цикла', delitel)
#     print('Цикл НОК ', nok)
# print('Итоговый НОК ', nok)
# ---------------------------------------------------------------------------------------------------


# while True:
#     one = int(input())
#     if one < 10:
#         continue
#     elif one > 100:
#         break
#     print(one)
# ---------------------------------------------------------------------------------------------------

# n = int(input())
# for i in range(n):
#     print(n*'*')
# ---------------------------------------------------------------------------------------------------

# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# raz_cd = d-c
# raz_ab = b-a
# con_ab = b-raz_ab
# con_cd = d-raz_cd
# n = 0
# l = 0
# g = con_ab

# if a <= b and c <= d:
#     for i in range(a, b+1):
#         for j in range(c, d+1):
#             itog = i*j
#             if l == 0:
#                 while con_cd <= d:
#                     print('\t', con_cd, sep='', end='')
#                     con_cd += 1
#                 print('\n', g, sep='', end='')
#             if n <= raz_cd:
#                 print('\t', itog, sep='', end='')
#             else:
#                 n = 0
#                 print('\n', g, '\t', itog, sep='', end='')
#             n += 1
#             l += 1
#         g += 1
#         n += 1

# ---------------------------------------------------------------------------------------------------

# a, b = int(input()), int(input())
# con = 0
# sm = 0

# for i in range(a, b+1):
#     if i % 3 != 0:
#         continue
#     else:
#         sm += i
#         con += 1

# otv = sm/con
# print(otv)
# ---------------------------------------------------------------------------------------------------


# gen = 'CACCTGGAC'
# cn = 0
# for c in gen:
#     if c == 'C':
#         cn += 1
# print(cn)
# ---------------------------------------------------------------------------------------------------


# vod = str(input()).upper()
# vod_len = len(vod)
# col = 0
# for i in vod:
#     if i == 'G' or i == 'C':
#         col += 1
# otvet = (col/vod_len)*100
# print(otvet)
# ---------------------------------------------------------------------------------------------------

# vod = str(input()).upper()
# vod_len = len(vod)
# vod_G = vod.count('G')
# vod_C = vod.count('C')
# otvet = ((vod_C+vod_G)/vod_len)*100
# print(otvet)
# ---------------------------------------------------------------------------------------------------


# ivod = str(input()) + ' '
# con = 0
# j = ivod[0]
# otv = ''
# for i in ivod:
#     print('Входные данные: ', j, i)
#     if i == j:
#         con += 1
#     elif i != j:
#         otv += j+str(con)
#         j = i
#         con = 1
# print(otv)
# ---------------------------------------------------------------------------------------------------

# ivod = str(input())+' '
# j = ivod[0]
# con = 0
# otv = ''
# for i in ivod:
#     if j != i:
#         otv += j + str(con)
#         j = i
#         con = 0
#     con += 1
# print(otv, end='')
# ---------------------------------------------------------------------------------------------------


# c = 0
# list_in = [int(i) for i in input().split()]
# list_out = []
# lli = len(list_in)
# if lli != 1:
#     while c < lli:
#         l_index = c-1
#         r_index = c+1
#         if c == 0:
#             l_index = lli-1
#         elif c == lli-1:
#             r_index = 0
#         s = list_in[l_index]+list_in[r_index]
#         list_out.insert(c, s)
#         print(list_out[c], end=' ')
#         c += 1
# else:
#     list_out = list_in
#     print(list_out[c])
# ---------------------------------------------------------------------------------------------------


# lin = [int(i) for i in input().split()]
# lin_s = sorted(lin)
# lin_len = len(lin_s)
# lin_prepre=lin_len-2
# l_pred = ''
# c = 0
# s = ''
# if lin_len > 1:
#     for l in lin_s:
#         if l != l_pred:
#             if c > 0:
#                 s += str(l_pred) + ' '
#                 c = 0
#         else:
#             c += 1
#         l_pred = l
#     if lin_s[lin_prepre] == max(lin_s):
#         s += str(lin_s[lin_prepre])
# print(s)
# ---------------------------------------------------------------------------------------------------


# spis=[int(i) for i in input().split()]
# min_chis=spis[0]
# for i in spis:
#     if i<min_chis:
#         min_chis=i
# print(min_chis)
# ---------------------------------------------------------------------------------------------------

# n, m, k = (int(i) for i in input().split())
# a = [[0 for j in range(m)] for i in range(n)]
# for i in range(k):
#     row, col = (int(i)-1 for i in input().split())
#     a[row][col] = -1
# print(a)
# ---------------------------------------------------------------------------------------------------


# spis = []
# sum_kvad = 0
# spis_sum = 0

# while True:
#     a = int(input())
#     spis.append(a)
#     spis_sum += a
#     if spis_sum == 0:
#         break

# for chi in spis:
#     sum_kvad += chi*chi
# print(sum_kvad)
# ---------------------------------------------------------------------------------------------------


# sum_kvad = 0
# spis_sum = 0

# while True:
#     a = int(input())
#     spis_sum += a
#     sum_kvad += a*a
#     if spis_sum == 0:
#         break
# print(sum_kvad)
# ---------------------------------------------------------------------------------------------------


# chi = int(input())
# c = 1
# stroc = ''
# step = 1
# no_step = 0
# while c <= chi:
#     if step > no_step:
#         stroc += str(step)+' '
#         no_step += 1
#         c += 1
#     else:
#         no_step = 0
#         step += 1
# print(stroc)
# ---------------------------------------------------------------------------------------------------

# arr = []
# arr_to = []
# arr_to_be = []

# while True:
#     arr = [str(i) for i in input().split()]
#     if arr[0] == 'end':
#         break

#     for c in range(len(arr)):
#         arr[c] = int(arr[c])
#     arr_to.append(arr)
#     row = len(arr_to)
#     col = len(arr)


# print(row, col)
# print(arr_to)
# arr_sum = 0
# for i in range(row):
#     for j in range(col):
#         for di in range(-1, 2, 1):
#             for dj in range(-1, 2, 1):
#                 if di == dj or di == -1 and dj == 1 or di == 1 and dj == -1:
#                     continue

#                 sum_i = i+di
#                 sum_j = j+dj

#                 if sum_i >= row:
#                     sum_i = 0
#                 if sum_j >= col:
#                     sum_j = 0

#                 print('I- ', i, j)
#                 print('D: ', di, dj)
#                 print('Sum: ', sum_i, sum_j, '\n',
#                       'Добавление- ', arr_to[sum_i][sum_j])
#                 arr_sum += arr_to[sum_i][sum_j]
#                 print(arr_sum)
#                 print('----------------------------')

#         arr_to_be.append(arr_sum)
#         # print(arr_to_be[i][j])
#         print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
#         arr_sum = 0

#         # arr_to[i][j] = arr_to[i][j]
# print(arr_to_be)
# ---------------------------------------------------------------------------------------------------


# arr = []
# arr_to = []
# arr_to_be = []
# arr_sum = 0

# while True:
#     arr = [str(i) for i in input().split()]
#     if arr[0] == 'end':
#         break

#     for c in range(len(arr)):
#         arr[c] = int(arr[c])
#     arr_to.append(arr)
#     row = len(arr_to)
#     col = len(arr)

# for i in range(row):
#     for j in range(col):
#         for di in range(-1, 2, 1):
#             for dj in range(-1, 2, 1):
#                 if di == dj or di == -1 and dj == 1 or di == 1 and dj == -1:
#                     continue

#                 sum_i = i+di
#                 sum_j = j+dj

#                 if sum_i >= row:
#                     sum_i = 0
#                 if sum_j >= col:
#                     sum_j = 0
#                 arr_sum += arr_to[sum_i][sum_j]
#         arr_to_be.append(arr_sum)
#         arr_sum = 0

# c = 0
# for a in arr_to_be:
#     if c < col-1:
#         print(a, end=' ')
#         c += 1
#     else:
#         print(a, '\t')
#         c = 0
# ---------------------------------------------------------------------------------------------------


# vodd = int(input())
# i, j = 0, 0
# vodd_con = vodd*vodd
# mas = [[0 for j in range(vodd)]for i in range(vodd)]
# end = vodd
# start = 0
# num = 0
# c = 1

# while c <= vodd_con:
#     for j in range(start, end):
#         if mas[i][j] == 0:
#             num += 1
#             mas[i][j] = num
#             c += 1
#             # print('+J', 's:', start, 'e:', end, 'I:', i, 'J:', j, 'O:', num)

#     for i in range(start, end):
#         if mas[i][j] == 0:
#             num += 1
#             mas[i][j] = num
#             c += 1
#             # print('+I', 's:', start, 'e:', end, 'I:', i, 'J:', j, 'O:', num)
#     end -= 1

#     for j in range(end, start, -1):
#         if mas[i][j] == 0:
#             num += 1
#             mas[i][j] = num
#             c += 1
#             # print('-J', 'e:', end, 's:', start,  'I:', i, 'J:', j, 'O:', num)
#     for i in range(end, start, -1):
#         j = start
#         if mas[i][j] == 0:
#             num += 1
#             mas[i][j] = num
#             c += 1
#             # print('-I', 'e:', end, 's:', start, 'I:', i, 'J:', j, 'O:', num)
#     start += 1

# for i in range(0, len(mas)):
#     for j in range(0, len(mas[i])):
#         print(mas[i][j], end=' ')
#     print('\n', end='')
# ---------------------------------------------------------------------------------------------------


# lst = [1, 2, 3, 4, 5, 6]
# print(lst)

# def modify_list(l):
#     l_len = len(l)-1
#     for i in range(l_len, -1, -1):
#         if l[i] % 2 != 0:
#             # print('Удаление', l[i])
#             del l[i]
#         else:
#             # print(l[i])
#             a = int(l[i]/2)
#             l[i] = a
#             # print('Значение', a, i)
#             # print('Изменённое занчение', l[i])


# print(modify_list(lst))  # None
# print(lst)               # [1, 2, 3]
# modify_list(lst)
# print(lst)               # [1]
# ---------------------------------------------------------------------------------------------------


# d = {}
# x = {}
# def update_dictionary(d, key, value):
#     if len(d) != 0:
#         if d.get(key) != None:
#             d[key] += [value]
#         elif d.get(key*2) != None:
#             d[key*2] += [value]
#         else:
#             d[key*2] = [value]
#     else:
#         d[key*2] = [value]

# print(update_dictionary(d, 1, -1))  # None
# print(d)                            # {2: [-1]}
# update_dictionary(d, 2, -2)
# print(d)                            # {2: [-1, -2]}
# update_dictionary(d, 1, -3)
# print(d)                            # {2: [-1, -2, -3]}
# print(update_dictionary(x, 0, -5))  # None
# print(x)                            # {0: [-5]}  (0*0=2)
# update_dictionary(x, 1, -1)
# print(x)                            # {0: [-5], 2: [-1]} (тк индекса 1 нет создаем key*2=2)
# update_dictionary(x, 2, -2)
# print(x)                            # {0: [-5], 2: [-1, -2]} (тк индекс 2 есть добавляем -2 в него)
# update_dictionary(x, 3, -3)
# print(x)                            # 0: [-5], 2: [-1, -2], 6: [-3]}
# ---------------------------------------------------------------------------------------------------


# vod = input().lower().split()
# slov = {}

# for v in vod:
#     if v in slov:
#         slov[v] += 1
#     else:
#         slov[v] = 1
# for key, value in slov.items():
#     print(key, value)
# ---------------------------------------------------------------------------------------------------


# def f(x):
#     return (x)

# n = int(input())
# i = 1
# slov = {}
# spis = []

# while i <= n:
#     one = int(input())
#     if one in slov:
#         for key, value in slov.items():
#             if key == one:
#                 spis.append(value)
#                 break
#     else:
#         value = f(one)
#         slov[one] = value
#         spis.append(value)
#     i += 1

# # print(slov)
# # print(spis)
# for i in spis:
#     print(i)
# ---------------------------------------------------------------------------------------------------
# import os
# spath = os.path.join('.', 'dataset_3363_2.txt')
# stroc = ''

# with open(spath, 'r') as text:
#     for line in text:
#         stroc += line.strip()

# stroc = stroc + ' '
# num = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
# len_stroc = len(stroc)
# c = 0
# chis = ''
# buk = ''
# stroc_pre = ''

# for i in range(len_stroc):
#     if stroc[i] in num:
#         if c > 0:
#             chis += stroc[i]
#         else:
#             chis = stroc[i]
#         c += 1
#     else:
#         print(chis)
#         if buk != '':
#             stroc_pre += buk*int(chis)
#         buk = stroc[i]
#         c = 0
# print(stroc_pre)

# with open('re_text.txt', 'w') as t:
#     t.write(stroc_pre)
# ---------------------------------------------------------------------------------------------------

# import os
# spath = os.path.join('.', 'dataset_3363_2.txt')
# stroc = ''

# with open(spath, 'r') as text:
#     for line in text:
#         stroc += line.strip()
# # stroc = 'a3b4c2e10b1'
# len_stroc = len(stroc)
# i = 0
# g = 0
# buk = ''
# stroc_pre = ''
# chis = ''

# while i < len_stroc:
#     if stroc[i].isalpha() == True:
#         buk = stroc[i]
#         i += 1
#         g = i
#         while g < len_stroc:
#             if stroc[g].isdigit() == True:
#                 chis += stroc[g]
#                 g += 1
#             else:
#                 print(buk, chis)
#                 break
#         stroc_pre += buk*int(chis)
#         chis = ''
#         i = g
# print(stroc_pre)

# with open('re_text.txt', 'w') as t:
#     t.write(stroc_pre)
# ---------------------------------------------------------------------------------------------------
# import os
# path_to = os.path.join('.', 'dataset_3363_3.txt')
# dan = ''

# with open(path_to, 'r') as text:
#     for line in text:
#         dan += line.strip()

# # dan = 'abc a bCd bC AbC BC BCD bcd ABC'
# dan_spis = []
# dan_spis = dan.lower().split()
# slov = {}
# big_znach = 0

# print(dan_spis)
# for i in range(len(dan_spis)):
#     znach = dan_spis.count(dan_spis[i])
#     if znach >= big_znach:
#         if dan_spis[i] in slov:
#             continue
#         else:
#             slov[dan_spis[i]] = znach
#         big_znach = znach
# print(slov)
# print(big_znach)

# key_pos = ''
# for key, volue in slov.items():
#     if volue == big_znach and key < key_pos:
#         key_pos = key
#     else:
#         key_pos = key


# print(key_pos, slov[key_pos])
# v = str(key_pos) + ' ' + str(slov[key_pos])

# with open('text_ret.txt', 'w') as text:
#     text.write(v)

# ---------------------------------------------------------------------------------------------------

# import os
# path_to = os.path.join('.', 'dataset_3363_3.txt')
# dan = ''

# with open(path_to, 'r') as text:
#     for line in text:
#         dan += line.strip()

# # dan = 'abc a bCd bC AbC BC BCD bcd ABC'
# dan_spis = []
# dan_spis = dan.lower().split()
# slov = {}
# big_znach = 0
# spis = []
# stroc=''

# print(dan_spis)
# for i in range(len(dan_spis)):
#     znach = dan_spis[i]
#     if znach in slov:
#         slov[znach] += 1
#     else:
#         slov[znach] = 1
# print(slov)
# print(big_znach)

# for v in slov.values():
#     if v > big_znach:
#         big_znach = v
#     else:
#         continue
# print(big_znach)

# for index, volue in slov.items():
#     if volue == big_znach:
#         spis += [index]
# print(spis)

# if len(spis) > 1:
#     min_znach = min(spis)
#     stroc = min_znach + ' ' + str(big_znach)
# else:
#     stroc = spis[0] + ' ' + str(big_znach)

# print(stroc)

# with open('text_ret.txt', 'w') as text:
#     text.write(stroc)

# ---------------------------------------------------------------------------------------------------
# import os

# path_to_file = os.path.join('.', 'dataset_3363_4.txt')
# mas_oc = []
# spisoc_stud=[]
# # spisoc_oc=[]
# slov = {}
# otv, sum_v, s_math_oc, s_fisic_oc, s_rus_oc = 0, 0, 0, 0, 0

# with open(path_to_file, 'r') as text:
#     for line in text:
#         name, math_oc, fisic_oc, rus_oc = line.strip().split(';')
#         print(name, math_oc, fisic_oc, rus_oc)
#         spisoc_oc=[int(math_oc), int(fisic_oc), int(rus_oc)]
#         spisoc_stud.append(spisoc_oc)

#         slov[name] = [int(math_oc), int(fisic_oc), int(rus_oc)]
# # print(slov)
# # print(len(slov))

# print(spisoc_stud)


# for v in slov.values():
#     len_v = len(v)
#     for i in range(len_v):
#         sum_v += v[i]

#         if i == 0:
#             s_math_oc += v[i]
#         elif i == 1:
#             s_fisic_oc += v[i]
#         elif i == 2:
#             s_rus_oc += v[i]

#     average_oc = sum_v/len_v
#     mas_oc.append(average_oc)
#     sum_v = 0
# print(mas_oc)

# len_slov = len(slov)
# with open('text_4.txt', 'w') as text:
#     average_item = str(s_math_oc/len_slov)+' ' + \
#         str(s_fisic_oc/len_slov)+' '+str(s_rus_oc/len_slov)

#     for i in mas_oc:
#         text.write(str(i)+'\n')
#     text.write(average_item)
# ---------------------------------------------------------------------------------------------------

# import os

# path_to_file = os.path.join('.', 'dataset_3363_4.txt')
# mas_oc = []
# spisoc_stud = []
# otv, sum_v, s_math_oc, s_fisic_oc, s_rus_oc = 0, 0, 0, 0, 0

# with open(path_to_file, 'r') as text:
#     for line in text:
#         name, math_oc, fisic_oc, rus_oc = line.strip().split(';')
#         print(name, math_oc, fisic_oc, rus_oc)
#         spisoc_oc = [int(math_oc), int(fisic_oc), int(rus_oc)]
#         spisoc_stud.append(spisoc_oc)
# print(spisoc_stud)

# for i in range(len(spisoc_stud)):
#     for j in range(len(spisoc_stud[i])):
#         sum_v += spisoc_stud[i][j]
#         if j == 0:
#             s_math_oc += spisoc_stud[i][j]
#         elif j == 1:
#             s_fisic_oc += spisoc_stud[i][j]
#         elif j == 2:
#             s_rus_oc += spisoc_stud[i][j]

#     average_oc = sum_v/len(spisoc_stud[i])
#     mas_oc.append(average_oc)
#     sum_v = 0
# print(mas_oc)

# len_spisoc_stud = len(spisoc_stud)
# print(len_spisoc_stud)
# with open('text_4.txt', 'w') as text:
#     average_item = str(s_math_oc/len_spisoc_stud)+' ' + \
#         str(s_fisic_oc/len_spisoc_stud)+' '+str(s_rus_oc/len_spisoc_stud)

#     for i in mas_oc:
#         text.write(str(i)+'\n')
#     text.write(average_item)

# ---------------------------------------------------------------------------------------------------

# import math
# r=float(input())
# pi=math.pi
# per=2*pi*r
# print(per)
# ---------------------------------------------------------------------------------------------------

# from sys import argv


# for i in range(1, len(argv)):
#     print(argv[i], end=' ')
# ---------------------------------------------------------------------------------------------------
# import os
# import requests

# path_to_file=os.path.join('.','dataset_3378_2.txt')
# sil=''
# with open(path_to_file, 'r') as text:
#     for line in text:
#         sil+=line.strip()

# print(sil)
# r=requests.get(sil)

# stroc_otv=r.text.splitlines()
# len_stroc_otv=len(stroc_otv)
# print(stroc_otv)
# print(len_stroc_otv)

# with open('Otv_3_6.txt', 'w') as text:
#     text.write(str(len_stroc_otv))
# ---------------------------------------------------------------------------------------------------
# import os
# import requests

# def spis_file(name):
#     with open('text_3_6.txt', 'w') as text:
#         text.write(name +'\n')

# path_file_in = os.path.join('.', 'dataset_3378_3.txt')
# s = ''

# with open(path_file_in, 'r') as text:
#     for line in text:
#         s += line.strip()
# print(s)

# silk = ''
# name_file = ''
# c = 0
# for i in s:
#     if c < 52:
#         silk += i
#     elif c >= 52:
#         name_file += i
#     c += 1
# print('Ссылка', silk)
# print('Название файла', name_file)

# count_=0
# while True:
#     count_+=1
#     if 'We'not in name_file:
#         r = requests.get(silk+name_file)
#         print(name_file, count_)
#         name_file = r.text.strip()
#         spis_file(name_file)
#     else:
#         print('Конец:', name_file)
#         with open('Otv_3_6.txt', 'w') as text:
#             text.write(name_file)
#         break

# ---------------------------------------------------------------------------------------------------

# import os
# import requests


# def file_rw(name, action_to_file='r', name_file='', spisok_files=None):
#     with open(name, action_to_file) as text:
#         stroc = ''

#         if action_to_file == 'w':
#             text.writelines(name_file + '\n')
#         elif action_to_file == 'r':
#             for line in text:
#                 stroc += line.strip()
#                 return stroc
#         else:
#             print('Ошибка в записи и прочтении файла')


# spisok_file_name = []
# path_file_in = os.path.join('.', 'dataset_3378_3.txt')
# s = file_rw(path_file_in)

# silk = ''
# name_file = ''
# c = 0
# for i in s:
#     if c < 52:
#         silk += i
#     elif c >= 52:
#         name_file += i
#     c += 1
# print('Ссылка', silk)
# print('Название файла', name_file)

# count_ = 0
# while True:
#     count_ += 1
#     if 'We'not in name_file:
#         r = requests.get(silk+name_file)
#         print(name_file, count_)
#         name_file = r.text.strip()
#     else:
#         print('Конец:', name_file)
#         file_rw('Otv_3_6.txt', 'w', name_file)
#         break

# ---------------------------------------------------------------------------------------------------
# import os
# check_team = []
# name_team = []
# slov = {}
# path_file = os. path.join('.', 'game.txt')
# with open(path_file, 'r', encoding='utf-8') as text:
#     for line in text:
#         for j in line.strip().split(';'):
#             if j.isdigit() == True:
#                 j = int(j)
#                 check_team.append(j)
#             else:
#                 name_team.append(j)

# # stroc = []
# # n = int(input())
# # slov = {}
# # for i in range(n):
# #     stroc.append([str(j) for j in input().split(';')])

# print(name_team)
# print(check_team)


# def Wins(n):
#     slov[name_team[n]][1] += 1
#     slov[name_team[n]][4] += 3


# def Lost(n):
#     slov[name_team[n]][3] += 1


# def Draw(n1, n2):
#     slov[name_team[n1]][2] += 1
#     slov[name_team[n1]][4] += 1

#     slov[name_team[n2]][2] += 1
#     slov[name_team[n2]][4] += 1


# for i in range(len(name_team)):
#     if name_team[i] not in slov:
#         slov[name_team[i]] = [0, 0, 0, 0, 0]
#         slov[name_team[i]][0] = name_team.count(name_team[i])
#     if i % 2 == 0:
#         p = i
#     else:
#         if check_team[p] > check_team[i]:
#             print('>')
#             print('P', check_team[p], name_team[p])
#             print('I', check_team[i], name_team[i])
#             Wins(p)
#             Lost(i)

#             print(slov[name_team[p]][1], slov[name_team[p]]
#                   [4], slov[name_team[i]][3])

#         elif check_team[p] < check_team[i]:
#             print('<')
#             print('P', check_team[p], name_team[p])
#             print('I', check_team[i], name_team[i])
#             Wins(i)
#             Lost(p)

#             print(slov[name_team[i]][1], slov[name_team[i]]
#                   [4], slov[name_team[p]][3])

#         else:
#             print('=')
#             print('P', check_team[p], name_team[p])
#             print('I', check_team[i], name_team[i])
#             Draw(i, p)

#             print(slov[name_team[i]][2], slov[name_team[i]][4],
#                   slov[name_team[p]][2], slov[name_team[p]][4])


# print(slov)

# ---------------------------------------------------------------------------------------------------
# import os
# check_team = []
# name_team = []
# slov = {}
# path_file = os. path.join('.', 'game.txt')
# with open(path_file, 'r', encoding='utf-8') as text:
#     for line in text:
#         for j in line.strip().split(';'):
#             if j.isdigit() == True:
#                 j = int(j)
#                 check_team.append(j)
#             else:
#                 name_team.append(j)

# # Ввод с консоли
# # check_team = []
# # name_team = []
# # n = int(input())
# # slov = {}
# # for i in range(n):
# #     for j in str(input()).strip().split(';'):
# #         if j.isdigit() == True:
# #             j = int(j)
# #             check_team.append(j)
# #         else:
# #             name_team.append(j)


# def Wins(n):
#     slov[name_team[n]][1] += 1
#     slov[name_team[n]][4] += 3


# def Lost(n):
#     slov[name_team[n]][3] += 1


# def Draw(n1, n2):
#     list_dan = [n1, n2]
#     for ld in list_dan:
#         slov[name_team[ld]][2] += 1
#         slov[name_team[ld]][4] += 1


# for i in range(len(name_team)):
#     if name_team[i] not in slov:
#         slov[name_team[i]] = [0, 0, 0, 0, 0]
#         slov[name_team[i]][0] = name_team.count(name_team[i])

#     if i % 2 != 0:
#         if check_team[p] > check_team[i]:
#             Wins(p)
#             Lost(i)
#         elif check_team[p] < check_team[i]:
#             Wins(i)
#             Lost(p)
#         else:
#             Draw(i, p)
#     else:
#         p = i
# print(slov)

# for key, index in slov.items():
#     print(f'{key}:', end='')
#     for idx in index:
#         print(idx, end=' ')
#     print('\n', end='')
# ---------------------------------------------------------------------------------------------------
# import os
# sp = []
# slov = {}
# sp_encrypted = []
# sp_dencrypted = []
# path_f = os.path.join('.', '3.7_dop_zad.txt')

# with open(path_f, 'r') as text:
#     for line in text:
#         sp.append([str(i)for i in line.strip()])
# print(sp)

# # Ввод с консоли
# # sp=[]
# # slov={}
# # sp_encrypted = []
# # sp_dencrypted = []
# # while True:
# #     if len(sp)<=3:
# #         sp.append([str(i)for i in input().strip()])
# #     else:
# #         break
# # print(sp)

# for i in range(len(sp)):
#     for j in range(len(sp[i])):
#         if i == 0:
#             slov[sp[i][j]] = sp[i+1][j]
#         elif i == 2:
#             if sp[i][j] in slov:
#                 sp_encrypted.append(slov.get(sp[i][j]))
#         elif i == 3:
#             for key, volue in slov.items():
#                 if volue == sp[i][j]:
#                     sp_dencrypted.append(key)
#         else:
#             continue
# print(slov)
# # print(sp_encrypted)
# # print(sp_dencrypted)

# print(*sp_encrypted, '\n', *sp_dencrypted, sep='')
# ---------------------------------------------------------------------------------------------------
# mnoj=[]
# sp=[]
# war=[]
# n=int(input())
# for i in range(n):
#     mnoj.append(str(input()).lower().strip())
# print(mnoj)

# c=int(input())
# for i in range(c):
#     sp.append(str(input()).lower().split(' '))
# print(sp)

# for i in range(len(sp)):
#     for j in range(len(sp[i])):
#         if sp[i][j] not in mnoj and sp[i][j] not in war:
#             war.append(sp[i][j])

# for w in war:
#     print(w)
# ---------------------------------------------------------------------------------------------------
# mnoj=set()
# sp=[]
# war=set()
# n=int(input())
# for i in range(n):
#     mnoj.add(str(input()).lower().strip())
# print(mnoj)

# c=int(input())
# for i in range(c):
#     sp.append(str(input()).lower().split(' '))
# print(sp)

# for i in range(len(sp)):
#     for j in range(len(sp[i])):
#         if sp[i][j] not in mnoj:
#             war.add(sp[i][j])

# for w in war:
#     print(w)
# ---------------------------------------------------------------------------------------------------
# import os

# slov = {'запад': -1, 'юг': -1, 'север': 1, 'восток': 1}
# spis_to_dan = [['восток', 'запад'], ['север', 'юг']]
# danni = []
# otv = [0, 0]
# path_to_file = os.path.join('.', '3.7_zad4.txt')

# with open(path_to_file, 'r', encoding='utf8') as text:
#     for line in text:
#         danni.append(line.strip().split(' '))
# print(danni)

# # # Ввод с консоли
# # slov = {'запад': -1, 'юг': -1, 'север': 1, 'восток': 1}
# # spis_to_dan = [['восток', 'запад'], ['север', 'юг']]
# # danni = []
# # otv = [0, 0]

# # n = int(input())
# # for i in range(n):
# #     danni.append(str(input()).split(' '))

# for i in danni:
#     for j in i:
#         if j.isdigit() == True:
#             dob = side * int(j)
#             if j_pred in spis_to_dan[0]:
#                 print('1', j_pred, side, j)
#                 otv[0] += dob
#             else:
#                 print('2', j_pred, side, j)
#                 otv[1] += dob
#         else:
#             if j in slov:
#                 side = slov.get(j)
#                 j_pred = j
# print(*otv)
# ---------------------------------------------------------------------------------------------------
import os

slov = {}
spis = []
min_class = 1
max_claass = 11
otv_str = ''
path_to_read = os.path.join('.', 'dataset_3380_5.txt')
path_to_write = os.path.join('.', 'Otv_3380_5.txt')

with open(path_to_read, 'r') as text:
    for line in text:
        spis.append(line.strip().split('\t'))
print(spis)


def Write_file(cl):
    with open(path_to_write, 'w') as text:
        text.write(cl)


for i in range(len(spis)):
    for j in range(len(spis[i])):
        if j == 0:
            j_class = int(spis[i][j])
            if j_class not in slov:
                slov[j_class] = []
        elif j == 2:
            slov[j_class].append(int(spis[i][j]))
print(slov)

for key, volue in slov.items():
    s_v = 0
    for v in volue:
        s_v += v
    slov[key] = s_v/len(volue)
print(slov)

for i in range(min_class, max_claass+1):
    if i not in slov:
        # print(i, '-')
        otv_str += str(i)+' '+'-'+'\n'
        Write_file(otv_str)
    else:
        # print(i, slov.get(i))
        otv_str += str(i)+' '+str(slov.get(i))+'\n'
        Write_file(otv_str)
print(otv_str)