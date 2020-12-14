# Задача fizz-buzz:
# У вас есть три числа, они вводятся из консоли. Первое число называется fizz, второе называется buzz. 
# До третьего необходимо досчитать от единицы. 
# Считая, надо выводить число. Если число кратно fizz - надо выводить F вместо числа. 
# Если число кратно buzz - надо выводить B вместо числа. 
# Если число кратно и fizz и buzz, надо выводить FB. И так - пока не будет достигнуто третье введенное число.


print ("Enter first number :") 
number1 = int(input())
print ("Enter second number :") 
number2 = int(input())
print ("Enter third number :") 
number3 = int(input())
#num = []
for num in range(1, number3 + 1):
	if num % 2 == 0:
		print("F",end='')
	if num % 5 == 0:
		print ("B", end='')
	if num % 2  != 0 and num % 5 != 0:
		print (num, end='')
	print (" ", end ='')
print("\n")