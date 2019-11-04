print("\n\'\'\'\n")
userinput = int(input("Please enter an integer number: "))
x = userinput
y = x
x += 1
y -= 1
print("The next number for the number",userinput,"is",str(x) + ".")
print("The previous number for the number",userinput,"is",str(y) + ".")
print("\n\'\'\'\n")

#я хотел сделать userinput += 1 в print(), но IDE сыпет syntax error. В C++ я делал тот же ++ в том же cout... Пробовал обрачивать в int(), результата нет.