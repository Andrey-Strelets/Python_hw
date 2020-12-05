


what = input ("What are we doing (+, -) : " )
a = float( input ("Enter first number : " ) ) 
b = float( input(" Enter secont number : " ) ) 
 
if what == '+':
	c = a+b
	print ( "Result : " + str(c) )
elif what == '-':
	c = a-b
	print ( "Result : " + str(c) )
else:
	print ("Wrong operation selected ")