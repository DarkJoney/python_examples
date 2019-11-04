"""4. Написать функцию `season`, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время года, которому
этот месяц принадлежит (зима, весна, лето или осень).
"""

def season(num):
    if num >= 1 and num <=2 or num == 12:
        return "winter"
    elif num <=5 and num > 2:
        return "spring"
    elif num <= 8 and num > 5:
        return "summer"
    elif num > 8 and num < 12:
        return "autumn"


a = int(input("Enter the month number: "))
b = season(a)
print("This month belongs to " + b)