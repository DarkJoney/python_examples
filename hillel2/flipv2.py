a = int(input("Let's enter 3-digit number for flip:"))
x = a%10 #3
y = a%100 #23
z = (a-y)/100
outres = (x*100)+(y-x)+z
#print (a)
print(int(outres)) #вывод перевернуттого числа после расчета
print(str(int(a))[::-1]) #вывод числа якобы перевернутым при помощи slice