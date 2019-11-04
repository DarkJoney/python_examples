guyscount = int(input("Let's meet your students...:"))
applecount = int(input("Give the apples to the children...:"))
v1 = applecount%guyscount
v2 = applecount//guyscount
print("Apples left:",v1)
print("Apples got:",int((applecount-v1)/guyscount))