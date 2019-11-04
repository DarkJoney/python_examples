"""Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего
параметра функции. Функция должна принимать три параметра: в первом параметре передаётся число для сдвига, второй
параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр задаёт
направление сдвига (по умолчанию влево (False))."""


def shift(input, snum = 1, dir = False):
    if dir == False:
        for i in range(0, snum):
            input = input*(2**1)
    elif dir == True:
        for i in range(0, snum):
            input = input//(2**1)
    else:
        print("system error")
    return input


a = int(input("Enter the value to shift: "))
b = int(input("How much times do you want to shift?"))
dir = input("in what direction? left/right:" )
if dir == "left":
    dir = False
elif dir == "right":
    dir = True
else:
    print("Wrong direction!")
out = shift(a, b, dir)
print(out)