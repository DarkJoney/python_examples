rows = 9
cols = 14
target = cols // 2
targetb = 0
targeta = 0
check = 0

for i in range(rows):
    check = i
    print(i, end='\t')
    targeta = target - i
    targetb = (target + i)-1
    for _ in range(cols):
        if i == 0:
            if _ == target:
                    print('* ', end='')
            else:
                print("  ", end='')
        if i != 0:
            if _ == targeta:
                print('* ', end='')
            else:
                print(" ", end='')
            if _ == targetb:
                print('* ', end='')
            else:
                print(" ", end='')
        if i == rows-1:
            print('*', end='')
    print()

