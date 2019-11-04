"""7. Петя перешёл в другую школу. На уроке физкультуры ему понадобилось определить своё место в строю. Помогите ему это
сделать.
    - Программа получает на вход невозрастающую последовательность натуральных чисел, означающих рост каждого человека в
    строю. После этого вводится число X – рост Пети. Все числа во входных данных натуральные и не превышают 200.
    - Выведите номер, под которым Петя должен встать в строй. Если в строю есть люди с одинаковым ростом, таким же, как
    у Пети, то он должен встать после них.
"""

a = []
cls = int(input("Enter the number of children in class:"))
petya = int(input("Enter Petya's length: "))

for i in range(0,cls):
    z = int(input("Enter the children's length:"))
    if z <= 200:
        a.append(z)
    elif z > 200:
        print("Hey, let's don't feed this children anymore, he gets too big!")
        cls +=1
print(a)
num = 0
for i in range(len(a)):
    if a[i] >= petya:
        num = i + 1

print("Petya's place in order is:", num)