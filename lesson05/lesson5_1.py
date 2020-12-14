# Задание 1
# Написать 2 функции. Первая функция будет принимать строку и приводить ее к нижнему регистру.
# Вторая функция будет принимать строку и проводить ее к верхнему регистру.
# После чего с помощью map применить ваши функции к списку строк. Отдельно каждую функцию к отдельному списку строк!

string_input = 'YOur StRinG'
string_list = list(string_input)
string_list2 = list(string_input)

def str_upper (string_input):
	return string_input.upper()
print(str_upper(string_input))

def str_lower (string_input):
	return string_input.lower()
print(str_lower(string_input))

new_list = list(map(str_upper, string_list))
new_list2 = list(map(str_lower, string_list2))

print(new_list)
print(new_list2)