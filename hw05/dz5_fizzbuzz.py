# Продолжаем идеализировать fizzbuzz, теперь применяем функции и map везде, где можно и нельзя!


rint ("Enter first number :") 
number1 = int(input())
print ("Enter second number :") 
number2 = int(input())
print ("Enter third number :") 
# number3 = int(input())
number3 = [5, 18, 9]
def fizzbuzz(num):
	for num in range(1, num + 1):
		if num % 2 == 0:
			print("F",end='')
		if num % 5 == 0:
			print ("B", end='')
		if num % 2  != 0 and num % 5 != 0:
			print (num, end='')
		print (" ", end ='')
	print("\n")
fizz_buzz_number = list(map(fizzbuzz, number3))
print(fizz_buzz_number)

