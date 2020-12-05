# n = int(input("n = :"))
# def prime_number(n):
# 	if n==1:
# 		return False
# 	for i in range(2, n):
# 		if n % i == 0:
# 			return False
# 		else:
# 			return True 

n = int(input("n="))
prime_number=[]
for i in range(2, n):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime_number.append(i)
        
def number_square(num):
	return num ** 2

numbers_square_map = list(map(number_square, prime_number))
print(numbers_square_map)