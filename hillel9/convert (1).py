""" Написать функцию для перевода десятичного числа в другую систему исчисления"""
from string import ascii_uppercase
from string import digits


def dectoany(valin, val):
    dictsym = digits + ascii_uppercase

    sampltab = []
    for i in range(len(dictsym)):
        sampltab.append(dictsym[i])

    condataout = []
    if val != 10:
        while valin != 0:
            condataout.append(sampltab[int(valin % val)])
            valin /= val
            valin = int(valin)
    else:
        i = 0
        calcval = 0
        while valin != 0:
            dec = valin % 10
            calcval = calcval + dec * pow(2, i)
            valin = valin // 10
            i += 1
        else:
            condataout.append(calcval)
    condataout.reverse()
    condataout = ''.join(map(str, condataout))
    return condataout

x = int(input("Enter the value:"))
z = int(input("Enter the system:"))
out = dectoany(x, z)
print(str(out))
