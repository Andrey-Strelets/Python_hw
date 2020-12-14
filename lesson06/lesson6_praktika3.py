# Написать функцию перевода размеров женского белья из международного во все остальные. 
# Внтри функции нужно просто обращаться к правильно составленному словарю.
sizes = {
    'XXS': {'Russia': 42, 'Germany': 36, 'USA': 8, 'France': 38, 'UK': 24},
    'XS': {'Russia': 44, 'Germany': 38, 'USA': 10, 'France': 40, 'UK': 26},
    'S': {'Russia': 46, 'Germany': 40, 'USA': 12, 'France': 42, 'UK': 28},
    'M': {'Russia': 48, 'Germany': 42, 'USA': 14, 'France': 44, 'UK': 30},
    'L': {'Russia': 50, 'Germany': 44, 'USA': 16, 'France': 46, 'UK': 32},
    'XL': {'Russia': 52, 'Germany': 46, 'USA': 18, 'France': 48, 'UK': 34},
    'XXL': {'Russia': 54, 'Germany': 48, 'USA': 20, 'France': 50, 'UK': 36},
    'XXXL': {'Russia': 56, 'Germany': 50, 'USA': 22, 'France': 52, 'UK': 38}}

input_size = input("Input international size: ")
get_size = input("Convert to size: ")


def convert(size):
	key = get_size
	if key in sizes[input_size]:
		print(get_size, "size: ", sizes[input_size][get_size])
	else:
		print("size is not found")
			
convert(input_size)