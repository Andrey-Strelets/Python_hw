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



# задача брилиант

# num = int(input("Enter your number: "))
# while not (num % 2 and num > 0):
#     print("Try again ")
#     num = int(input("Enter your number: "))
# if num % 2 and num > 0:
#     for i in range(1, num + 1, 2):
#         print(i * "*")
#     for i in range(num - 2, 0, -2):
#         print(i * "*")


# Первая задача
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
flat_number = int(input('Please enter number flat \n'))
stages = int(input('Please enter number of stages \n'))
flat_per_stage = int(input('Please enter of flats in stages\n'))
def get_coordinates(flat_number, stages, flat_per_stage):
    flats_per_block = stages * flat_per_stage
    if flat_number % flats_per_block:
        target_block = (flat_number // flats_per_block) + 1
    else:
        target_block = (flat_number // flats_per_block)
    temp_flats = flat_number - int(flat_number // flats_per_block) * flats_per_block
    if temp_flats == 0:
        return ["Number entrance:", target_block, "Number stage", stages]
    else:
        if temp_flats % flat_per_stage:
            target_stage = temp_flats // flat_per_stage + 1
        else:
            target_stage = temp_flats // flat_per_stage
    return ["Number entrance:", target_block, "Number stage", target_stage]
print(get_coordinates(flat_number, stages, flat_per_stage))