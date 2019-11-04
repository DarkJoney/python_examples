"""## operators

11. Дано трехзначное число. Найдите сумму его цифр.
"""
x = int(input("Enter your value:"))

a = x - (x % 100)
b = x%10
c = x%100
a = a/100
c = (c-b)/10

out= a+b+c
print("The digits sum of", x, "is",int(out))