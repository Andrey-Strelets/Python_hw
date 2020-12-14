# Банкомат выдает сумму максимально возможными купюрами

nominal = [10, 20, 50, 100, 200, 500, 1000]
print("Enter summa: ")
sum = int(input())

def returnsum(sum, nominal):
    repay = [0] * len(nominal)

    for ind, bill in reversed(list(enumerate(nominal))):
    	while bill <= sum:
            sum = sum - bill
            repay[ind] += 1
    return(repay)
print(returnsum(sum, nominal))
