# Написать программу, которая выводит сама себя

import sys
filename = sys.argv[0]
with open(filename) as f:
	for line in f:
		print(line, end="")
