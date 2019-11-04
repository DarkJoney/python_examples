"""
5. Программа запрашивает ввод последовательности целых чисел, пока не будет введён 0. Как только
будет введён 0 (ноль), программа должна посчитать и вывести на экран:
- количество введённых чисел (завершающий 0 не считается)
- их сумму
- произведение
- среднее арифметическое (не считая завершающего числа 0)
- определить значение и порядковый номер наибольшего элемента последовательности. Если наибольших элементов несколько,
выведите порядковый номер первого из них. Нумерация элементов начинается с 1 (еденицы)
- определить количество чётных и не чётных элементов в последовательности
- количество положительных и отрицательных значений"""
count = 0
sum = 0
mult = 1
biggest = 0
biggestnum = 0
odd = 0
even = 0
pos = 0
neg = 0
while True:
    number = int(input("Enter value:"))
    if number != 0:
        count +=1
        sum = sum + number
        mult = mult*number
        if biggest < number:
            biggest = number
            biggestnum = count
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        if number > 0:
            pos += 1
        else:
            neg += 1
    elif number == 0:
            break
print("Number of entered values:",count)
print("Sum of entered values:", sum)
print("Multiplication of entered values:", mult)
print("The biggest value entered: ", biggest, "which is", biggestnum)
print("Number of odd values:", odd)
print("Number of even values:", even)
print("Number of positive values:", pos)
print("Number of negative values:", neg)
