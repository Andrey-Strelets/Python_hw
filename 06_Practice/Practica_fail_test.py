
# Задача 3. Файл-тест. Есть файл, в котором хранятся числа в следующем формате:

# 2 4 5;3 2
# 3 2 1;2 0
# 6 5 2 1 2;3 1
# .....
# Цифры до точки с запятой надо суммировать, потом делить на их количество. 
# В первой строке сумма будет 11, разделить на их количество, т.е. на 3, получается 3 целых и в остатке 2. Аналогичным образом во второй строке 6 делим на три, ровно два и в сотатке ноль, в третьей строке сумма 16, на 5 делим, получаем 3 и 1 в остатке. Вот так:

# 2 4 5;3 2                 2+4+5/3 = 3, в остатке 2
# 3 2 1;2 0                 3+2+1/3 = 2, в остатке 0
# 6 5 2 1 2;3 1         6+5+2+1+2/5 = 3, в остатке 1
# .....
# Задача: проверить каждую строку файла, если строка записана верно, вывести ее и после написать True, если строка не верна, вывести результат с пометкой False.


# f = open("C:/Python/git/homework/file_test.txt")
# for l in f.readlines():
# 	before = [int(i) for i in l.split(';')[0] if i.isdigit()]
# 	after = [int(i) for i in l.split(';')[1] if i.isdigit()]
# 	whole = sum(before) // len(before)
# 	percent = sum(before) % len(before)
# 	if whole == after[0] and percent == after[1]:
# 		print(l.strip(), True, sep=' ---> ')
# 	else:
# 		print(l.strip(), False, sep=' ---> ')



# Задача 2. Бриллиант

# Входным данным является целое число. Необходимо:

# написать проверку, чтобы в работу пускать только положительные нечетные числа
# для правильного числа нужно построить бриллиант из звездочек или любых других символов и вывести его в консоли. Для числа 1 он выглядит как одна взездочка, для числа три он выглядит как звезда, потом три звезды, потом опять одна, для пятерки - звезда, три, пять, три, одна...
#    *        *
#            ***
#    *      *****
#   ***      ***
#    *        *т

# num = int(input("Enter your number: "))
# while not (num % 2 and num > 0):
#     print("Try again ")
#     num = int(input("Enter your number: "))
# if num % 2 and num > 0:
#     for i in range(1, num + 1, 2):
#         print(i * "*")
#     for i in range(num - 2, 0, -2):
#         print(i * "*")


# Задача 1. Курьер

# Вам известен номер квартиры, этажность дома и количество квартир на этаже. 
# Задача: написать функцию, которая по заданным параметрам напишет вам, в какой подъезд и на какой этаж подняться, чтобы найти искомую квартиру.


# import math
# number_of_flat = int(input('Введите номер квартиры \n'))
# etazh = int(input('Введи количество этажей \n'))
# kol_vo_kvartir = int(input('Введи количество квартир на этаже \n'))
# kvartir_v_padike = etazh * kol_vo_kvartir
# nomer_padika = math.ceil(number_of_flat / kvartir_v_padike)
# if number_of_flat > kvartir_v_padike:
# 	ost_etazh = (number_of_flat % kvartir_v_padike)
# 	if ost_etazh > kol_vo_kvartir:
# 		nomer_etazha = math.ceil(ost_etazh / kol_vo_kvartir)
# 	elif ost_etazh <= kol_vo_kvartir:
# 		nomer_etazha = 1
# elif number_of_flat < kvartir_v_padike:
# 	nomer_etazha =  math.ceil(kvartir_v_padike / kol_vo_kvartir)

# # etazh = (number_of_flat - (nomer_padika - 1) * kvartir_v_padike + 1) // kol_vo_kvartir
# print('тебе нужен падик номер ', nomer_padika, 'и этаж номер ', nomer_etazha)

# while number_of_flat > kvartir_v_padike:
# 	nomer_padika += 1
# 	number_of_flat -= kvartir_v_padike
# if  number_of_flat < kvartir_v_padike:
# 	nomer_padika = 1

import math
number = int(input('Введите номер квартиры: '))
floors = int(input('Введи количество этажей: '))
flats = int(input('Введи количество квартир на этаже: '))
entrance = 1

while number > (flats * floors):
    entrance += 1
    number -= flats * floors

print("Here is your floor: ", math.ceil(number/flats))
print("Here is your entrance: ", entrance)


# working
# flat_number = int(input('Please enter number flat \n'))
# stages = int(input('Please enter number of stages \n'))
# flat_per_stage = int(input('Please enter of flats in stages\n'))
# def get_coordinates(flat_number, stages, flat_per_stage):
#     flats_per_block = stages * flat_per_stage
#     if flat_number % flats_per_block:
#         target_block = (flat_number // flats_per_block) + 1
#     else:
#         target_block = (flat_number // flats_per_block)
#     temp_flats = flat_number - int(flat_number // flats_per_block) * flats_per_block
#     if temp_flats == 0:
#         return ["Number entrance:", target_block, "Number stage", stages]
#     else:
#         if temp_flats % flat_per_stage:
#             target_stage = temp_flats // flat_per_stage + 1
#         else:
#             target_stage = temp_flats // flat_per_stage
#     return ["Number entrance:", target_block, "Number stage", target_stage]
# print(get_coordinates(flat_number, stages, flat_per_stage))