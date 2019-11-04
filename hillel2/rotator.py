x = int(input("Enter your value:"))

a = x - (x % 100)
b = x%10
c = x%100
a = a/100
c = (c-b)/10

print("Rotated ", x,"is:", str(int(b)) + str(int(c)) + str(int(a)))
