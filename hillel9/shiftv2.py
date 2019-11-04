"""10. Написать функцию, циклически сдвигающую целое число на N разрядов вправо или влево, в зависимости от третьего
параметра функции.
Функция должна принимать три параметра: в первом параметре передаётся число для сдвига,
 второй параметр задаёт количество разрядов для сдвига (по умолчанию сдвиг на 1 разряд), 3-й булевский параметр з
 адаёт направление сдвига (по умолчанию влево (False))."""


def shiftfun(value, times, shift):
    data = list(map(int, str(value)))
    for i in range(times):
        if shift == True:
            data.insert(0, data.pop())
        elif shift == False:
            data.insert(len(data), data.pop(0))

    shiftout = ''.join(map(str, data))
    return shiftout

a = int(input("Enter the value to shift: "))
b = int(input("How much times do you want to shift?"))
direction = input("in what direction? left/right:" )
if direction == "left":
    direction = False
elif direction == "right":
    direction = True
else:
    print("Wrong direction!")
out = shiftfun(a, b, direction)
print(out)