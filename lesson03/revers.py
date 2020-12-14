# Написать программу, которая выводит саму себя задом наперед

with open("revers.py", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
    i = len(array) - 1
    while i >= 0:
    	print(array[i], end='')
    	i -= 1

# Example 2

# import sys
# filename = sys.argv[0]
# with open(filename) as f:
#   for line in reversed(list(f)):
        
#       print(line, end="")
	    


