# 1.Пользователь вводит число, нужно вывести чило pi с заданной точностью(БЕЗ БИБЛИОТЕК/МОДУЛЕЙ)
# import math

# n = int(input("Введите число: "))
# pi = sum(1/16**x*(4/(8*x + 1) - 2/(8*x + 4) - 1/(8*x + 5) - 1/(8*x + 6)) for x in range(n))

# print(pi)



# 2. Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# num = int(input("Введите натуральное число: "))
# i = 2
# list = []
# oldNum = num

# while num > 1:
#     if num % i == 0:
#         num //= i
#         list.append(i)
#     elif num % i != 0:
#         i += 1 

# res = str(list)[1: -1]  
# print(f"Список простых множителей числа {oldNum}: {res}", end=" ")


# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

# list = [1, 3, 3, 2, 4, 5, 6, 6, 1]
# print(list)
# newList = []

# for i in list:
#     if i not in newList:
#         newList.append(i)
# print(newList)



# 4. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# *Пример:* 
# - k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

# from random import randint as rd

# k = int(input("Введите K: "))
# for  i in range(k, 0, -1):
#     x = rd(-100, 100)
#     if x > 0:
#         print(f"+{x}x^{i}", end=" ")
#     else:  
#         print(f"{x}x^{i}", end=" ")
# print(rd(-100, 100), end="")
