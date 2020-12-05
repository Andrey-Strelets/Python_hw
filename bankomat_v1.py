string = input("Введите слово: ")
newString = ""
ranged = len(string) - 1
while ranged != -1:
    newString += string[ranged]
    ranged -= 1
print(newString)