with open("text.py", "r") as ins:
    array = []
    for line in ins:
        array.append(line)
    i = len(array) - 1
    while i >= 0:
    	print (array[i], end='')
    	i -= 1

    # count = len(array)
    # while count > 0:
	   #  count -= 1
	   #  print(array[count], end='')
	    


