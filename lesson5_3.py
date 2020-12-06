# Example №1

# from collections import Counter
# with open('text_lesson5.txt') as f:
# 	text_string = f.read().lower().replace(',', '').replace('.', '').strip().split(' ')
# print(dict(Counter(text_string)))


#Example №2

# with open('text_lesson5.txt') as f:
# 	text_string = f.read().lower().replace(',', '').replace('.', '').strip().split(' ')
# def frequency(string):
#     frequency_dict = {}
#     for i in string:
#         if i in frequency_dict:
#             frequency_dict[i] += 1
#         else:
#             frequency_dict[i]=1
#     return frequency_dict
# print(frequency(text_string))

# Evample 3

with open('text_lesson5.txt') as f:
	text_string = f.read().lower().replace(',', '').replace('.', '').strip().split(' ')

frequency_dict = {}
def frequency(string):
	count = frequency_dict.get(string,0)
	frequency_dict[string] = count + 1
	return frequency_dict

kol = list(map(frequency,text_string))
print(kol[1])


