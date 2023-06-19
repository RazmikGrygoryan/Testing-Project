# def say_name(name):
#     print(f'Hello, {name}, youre fucking pathetic looser wagey')
# say_name(input('Plese tell me your name bruv: '))


# def say_name(name='Sasha'):
#     print(f'Hello, {name}, youre fucking pathetic looser wagey')
# say_name()
# say_name(input('Plese tell me your name bruv: '))


# def print_mess(name, *, age, company):
#     print(f'name: {name}, age: {age}, company: {company}')
# print_mess('bob',age= 7, company='Tates')


# def sum(a, b):
#     return a + b
# geeks = sum
# print(geeks(1, 6))

# def do_operation(a, b, operation):
#     result = operation(a, b)
#     return f'result: {result}'
# def sum(a,b):
#     return a + b
# def mult(a,b):
#     return a * b
# print(do_operation(6,1,sum))
# print(do_operation(7,1,mult))


# def sum(a, b):
#     return a + b
# def mult(a,b):
#     return a * b
#
# def select_operation(choice):
#     if choice == 1:
#         return sum
#     elif choice == 2:
#         return mult
# operation = select_operation(1)
# print(operation(1, 6))
#
# operation = select_operation(2)
# print(operation(1, 7))


#
# def func(*args):
#     print(args[0])
#     print(args)
# func('Alesk', 'Razmik', 'Danya')


# def func(**kwargs):
#     for key in kwargs:
#         print(f'{key}: = {kwargs[key]}')
# func(name= 'Pedkic', age= 7)



# letter = input('Введите букву латинского бро: ')
# if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
#     print('Буква гласная бро')
# elif letter == 'y':
#     print('Буква гласная или согласная бро')
# else:
#     print('Согласная буква бро')



# number = int(input('Введи число бро: '))
# if number % 2 == 0:
#     print('Четное число бро')
# else:
#     print('Нечетное бро')


# my_dict = {'a': 1, 'b': 2}
#
# for key in my_dict:
#     print(key)
#
# for value in my_dict.values():
#     print(value)



# def outer_func(x):
#     def inner_func(y):
#         return x + y
#     return inner_func
#
# add_10 = outer_func(10)
# print(add_10(5))



# hours = 1
# minutes = 1
# seconds = 1
# print("%02d:%02d:%02d"%(hours, minutes, seconds))



# string = input("Введите числа через пробел:")
#
# list_of_strings = string.split() # список строковых представлений чисел
# list_of_numbers = list(map(int, list_of_strings)) # список чисел
#
# list_of_numbers.append(sum(list_of_numbers[0:]))
# print(list_of_numbers[::-1])

# book = {}
# title = input("Введите название книги: ")
# author = input("Введите фамилию автора: ")
# year = int(input('Введите год выпуска: '))
#
# book['title'] = title
# book['author'] = author
# book['year'] = year
#
# print(book)




# text = input("Введите текст:")
# unique = set(text)
# print("Количество уникальных символов: ", len(unique))
# print(unique)



# text = list(map(int, input().split()))
# text1 = list(map(int, input().split()))
# text_set, text1_set = set(text), set(text1)
#
# list_list = text_set.symmetric_difference(text1_set)
# print(list_list)



# РЕШЕНИЕ №1
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# money = int(input('Введите сумму вклада: '))
# deposit = []
# deposit.append(money / 100 * per_cent['ТКБ'])
# deposit.append(money / 100 * per_cent['СКБ'])
# deposit.append(money / 100 * per_cent['ВТБ'])
# deposit.append(money / 100 * per_cent['СБЕР'])
# deposit = list(map(int, deposit))
# print(f'Максимальная сумма, которую вы можете заработать — {int(max(deposit))}')


# РЕШЕНИЕ №2
# per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# money = int(input('Введите сумму вклада: '))
# deposit = []
# for i in per_cent.values():
#     deposit.append(money / 100 * i)
# deposit = list(map(int, deposit))
# print(f'Максимальная сумма, которую вы можете заработать — {int(max(deposit))}')




# n = input()
# s = len(n) // 2
# s_new = f'{n[s:]} {n[:s]}'
# print(s_new)


# s = input()
# a, b = s.split()
# print(b, a)



# s = input() # ввод строки
# if 'f' in s: # если буква f встречается в строке
#     first_index = s.index('f') # находим индекс первого появления буквы f
#     if first_index == s.rindex('f'): # если буква f встречается только один раз
#         print(first_index) # выводим её индекс
#     else: # если буква f встречается два и более раз
#         last_index = s.rindex('f') # находим индекс последнего появления буквы f
#         print(first_index, last_index) # выводим индексы первого и последнего появления буквы f
