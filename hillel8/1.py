"""1. Написать функцию `arithmetic`, принимающую 3 аргумента: первые 2 - числа, третий - операция, которая должна быть
произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить; / — разделить (первое на
второе). В остальных случаях вернуть строку `"Неизвестная операция"`.
"""


def arithmetic(a, b, action):
    if action == '/':
        return a/b
    elif action == '*':
        return a*b
    elif action == '+':
        return a+b
    elif action == '-':
        return a-b
    else:
        return "unknown OPERATION"


v1 = int(input("Enter the first value: "))
v2 = int(input("Enter the second value: "))
action = input("Enter + or - or / or *")
result = arithmetic(v1, v2, action)
print(result)

