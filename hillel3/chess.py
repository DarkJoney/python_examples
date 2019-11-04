"""Шахматный конь ходит буквой “Г” — на две клетки по вертикали в любом направлении и на одну клетку по горизонтали,
или наоборот. Даны две различные клетки шахматной доски, определите, может ли конь попасть с первой клетки на вторую
одним ходом."""
print("  12345678")
print("1 _X_X_X_X\n2 X_X_X_X_\n3 _X_X_X_X\n4 X_X_X_X_\n5 _X_X_X_X\n6 X_X_X_X_\n7 _X_X_X_X\n8 X_X_X_X_")

print("\nInput the horse's move coordinates:")
x1 = int(input("x1:"))
y1 = int(input("y1:"))
x2 = int(input("x2:"))
y2 = int(input("y2:"))


if (x1 - 2 == x2 or x1 + 2 == x2) and (y1 - 1 == y2 or y1 + 1 == y2):
    print('YES')
elif (x1 - 1 == x2 or x1 + 1 == x2) and (y1 - 2 == y2 or y1 + 2 == y2):
    print('YES')
else:
    print('NO')
