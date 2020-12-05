# import sys
# filename = sys.argv[0]
# with open(filename) as f:
# 	for line in f:
# 		print(line)

# with open("lesson4_praktika_2.py") as ins:
#     array = []
#     for line in ins:
#         array.append(line)
#     i = len(array) - 1
#     while i >= 0:
#     	print(array[i], end='')
#     	i -= 1

import sys
filename = sys.argv[0]
with open(filename) as f:
	for line in reversed(list(f)):
		
		print(line, end="")