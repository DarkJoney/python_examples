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
