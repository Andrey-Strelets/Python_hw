banknots = {10:10, 20:10, 50:10, 100:10, 200:100, 500:1000}
# print("Enter summa: ")
# sum = int(input())
def niminal_and_kol(banknots):
	nominal = [banknots[i][0] for i in banknots]
	kol = [banknots[i][1] for i in banknots]
	return(nominal, kol)
	print(banknots)