""" Написать функцию для перевода десятичного числа в другую систему исчисления"""


def decToAny(input, val):
    table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    hex = []
    if val != 10:
        while input != 0:
            hex.append(table[int(input % val)])
            input /= val
            input = int(input)
    else:
        i = 0
        decimal = 0
        while input != 0:
            dec = input % 10
            decimal = decimal + dec * pow(2, i)
            input = input // 10
            i += 1
        else:
            hex.append(decimal)
    hex.reverse()
    hex = ''.join(map(str, hex))
    return hex

x = int(input("Enter the value:"))
z = int(input("Enter the system:"))
out = decToAny(x, z)
print("0x" + str(out))