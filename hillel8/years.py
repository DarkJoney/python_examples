"""2. Написать функцию `is_year_leap`, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False
иначе."""


def is_year_leap(year):
    check = True
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
           check = False
    return check


x = int(input("Please enter the year to check:"))
out = is_year_leap(x)
print(out)