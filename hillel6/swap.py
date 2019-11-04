"""10. В списке все элементы различны. Поменяйте местами минимальный и максимальный элемент этого списка. Создавать новый
список недопустимо.
"""
import random
a = random.sample(range(30), 10)
max = a[0]
min = a[0]
maxid = 0
minid = 0

for i in range(len(a)):
    if max > a[i]:
        max = a[i]
        maxid = i
    if min < a[i]:
        min = a[i]
        minid = i

print(a)
print(a[maxid], a[minid])
a[maxid] = min
a[minid] = max
print(a)