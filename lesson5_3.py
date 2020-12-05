frequency = {}
with open('text_lesson5.txt') as f:
	text_string = f.read().lower()
	print(text_string)

def count_words(word):
	
# for word in frequency:
# 	count = frequency.get(word,0)
# 	frequency[word] = count + 1

# frequency_list = frequency.keys()

# for words in frequency_list:
# 	print(words,frequency(words))
