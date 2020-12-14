# Каждый пишет сумму списка при помощи for и while

a = [10, 10, 10, 10, 60, 50, 50]
def sum_list(list):
	sum_list = 0
	for i in list:
		sum_list = sum_list + i
	return sum_list
print(sum_list(a))


# example2
# print(sum(a))

# example3

# a = [10, 10, 10, 10, 60, 50, 50]
# _sum_ = 0
# for i in a:
# 	_sum_ = _sum_ + i
# print(_sum_) 