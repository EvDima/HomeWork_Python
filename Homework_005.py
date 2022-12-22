# 1. Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. 
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. 
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
from random import randint as rd 

# user1 = input('Введите имя первого игрока: ')
# user2 = input('Введите имя второго игрока: ')
# igrok = rd(1, 3)
# conf = 2021
# if igrok == 1:
#     print(f"Первым ходит {user1}")
# else:
#     print(f"Первым ходит {user2}")
# lowDigit = 1
# highDigit = 28
# maxConf = conf
# win = False
# print(f'Всего конффет: {maxConf}')

# while not win:
#     if conf > highDigit:
#         igrok1 = int(input(f"Ты можещь взять от {lowDigit} до {highDigit} конфет, сколько ты взял?: "))
#         conf -= igrok1 
#         print(f'Осталось конфет: {conf}')

#         if conf > highDigit:
#             igrok2 = int(input(f'Ты можещь взять от {lowDigit} до {highDigit} конфет, сколько ты взял?: '))
#             conf -= igrok2
#             print(f'Осталось конфет: {conf}')

#             if conf <= highDigit:
#                 win = True
#                 if igrok == 1:
#                     print(f"Осталось {conf} шт, их забирает {user1}. Значит ПОБЕДИЛ {user1}")
#                 else:
#                     print(f"Осталось {conf} шт, их забирает {user2}. Значит ПОБЕДИЛ {user2}")
#     else:
#         win = True
#         if igrok == 1:
#             print(f"Осталось {conf} шт, их забирает {user2}. Значит ПОБЕДИЛ {user2}")
#         else:
#             print(f"Осталось {conf} шт, их забирает {user1}. Значит ПОБЕДИЛ {user1}")


# user1 = input('Введите имя игрока: ')
# botName = 'Бот'

# conf = 100
# bot = 1
# print(f"Первым ходит {botName}")
# igrok2 = 1
# lowDigit = 1
# highDigit = 28
# maxConf = conf
# win = False
# print(f'Всего конффет: {maxConf}')

# while not win:
#     if conf > highDigit:
#         if igrok2 == 1:
#             print(1)
#             conf -= igrok2
#         else:
#             bot1 = 29 - igrok2
#             print(bot1)
#             conf = conf - bot1 

#         print(f'Осталось конфет: {conf}')

#         if conf > highDigit:
#             igrok2 = int(input(f'Ты можещь взять от {lowDigit} до {highDigit} конфет, сколько ты взял?: '))
#             conf -= igrok2
#             print(f'Осталось конфет: {conf}')

#             if conf <= highDigit:
#                 win = True
#                 if bot == 1:
#                     print(f"Осталось {conf} шт, их забирает {botName}. Значит ПОБЕДИЛ {botName}")
#                 else:
#                     print(f"Осталось {conf} шт, их забирает {user1}. Значит ПОБЕДИЛ {user1}")
#     else:
#         win = True
#         if bot == 1:
#             print(f"Осталось {conf} шт, их забирает {user1}. Значит ПОБЕДИЛ {user1}")
#         else:
#             print(f"Осталось {conf} шт, их забирает {botName}. Значит ПОБЕДИЛ {botName}")



   
    
# 2. Создайте программу для игры в ""Крестики-нолики"".

# broad = list(range(1,10))

# def darw_broad(broad):
#     print("_"* 13)
#     for i in range(3):
#         print("|", broad[0+i*3], "|", broad[1+i*3], "|", broad[2+i*3], "|")
#         print("_"* 13)

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_index = input("Куда ставим" + player_token + "--> ")
#         try:
#             player_index = int(player_index)
#         except:
#             print("Что то не так нажали")
#             continue
#         if player_index >= 1 and player_index <= 9:
#             if (str(broad[player_index - 1]) not in "XO"):
#                 broad[player_index - 1]  = player_token
#                 valid = True
#             else:
#                 print("Занято")
#         else:
#             print("Еще раз попробуй")

# def check_win(broad):
#     victory = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for i  in victory:
#         if broad[i[0]] == broad[i[1]] == broad[i[2]]:
#             return broad[i[0]]
#     return False
    
# def game(broad):
#     counter = 0
#     win = False
#     while not win:
#         darw_broad(broad)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(broad)
#             if tmp:
#                 print(tmp,"Выйграл!")
#                 win = True
#                 break
#         if counter == 9:
#             print("Ничья")
#             break
#     darw_broad(broad)

# game(broad)



# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

# with open('file.txt', 'w', encoding='UTF-8') as file:
#     file.write(input('Напишите текст необходимый для сжатия: '))
# with open('text_words.txt', 'r') as file:
#     my_txt = file.readline()
#     txt_compr = my_txt.split()

# print(my_txt)

# def file_encod(txt):
#     encond = ''
#     prev_char = ''
#     count = 1
#     if not txt:
#         return ''

#     for char in txt:
#         if char != prev_char:
#             if prev_char:
#                 encond += str(count) + prev_char
#             count = 1
#             prev_char = char
#         else:
#             count += 1
#     else:
#         encond += str(count) + prev_char
#         return encond


# txt_compr = file_encod(my_txt)

# with open('text_code_words.txt', 'w', encoding='UTF-8') as file:
#     file.write(f'{txt_compr}')
# print(txt_compr)
