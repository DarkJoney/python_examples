input = int(input("Num of rows:"))

for i in range(0, input):
    if i == 0:
        for z in range(0,input+1):
            if z < input-1:
                print("  ", end="")
            elif z == input-1:
                print(" ", end="")
            else:
                print("*", end="")
                print()

    for j in range(0, input-i-1):
        print("  ", end="")
    for j in range(0,i+1):
        print("* ", end="")
    for j in range(0,i+1):
        print("* ", end="")
    print()

for n in range(input-1, 0, -1):
    for m in range(0, input-n):
        print("  ", end="")
    for m in range(0, n):
        if m == 0 or m == n-1:
            print("* ", end="")
        else:
            print("  ", end="")
    for m in range(0, n):
        if m == n or m == n - 1 or m == 0:
            print("* ", end="")
        else:
            print("  ", end="")
    if n == 1:
        print()
        for h in range(0,input+1):
            if h < input-1:
                print("  ", end="")
            elif h == input-1:
                print(" ", end="")
            else:
                print("*", end="")
                print()
    print()