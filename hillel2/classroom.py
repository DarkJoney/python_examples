print("Let's buy some tables...\n")
guys1 = int(input("Enter the number of children for 1st class:"))
guys2 = int(input("Enter the number of children for 2nd class:"))
guys3 = int(input("Enter the number of children for 3rd  class:"))

class1 = guys1 % 2
class1 += guys1
class1 /= 2

class2 = guys2 % 2
class2 += guys2
class2 /= 2

class3 = guys3 % 2
class3 += guys3
class3 /= 2

print(" Classroom 1 needs ",int(class1),"tables\n","Classroom 2 needs ",int(class2),"tables\n","Classroom 3 needs ",int(class3),"tables\n")