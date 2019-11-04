"""5. Пользователь делает вклад в размере `a` гривнен сроком на `years` лет под 10% годовых (каждый год размер его вклада
увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на них в следующем году тоже будут проценты).
Написать функцию `bank`, принимающая аргументы `a` и `years`, и возвращающую сумму, которая будет на счету пользователя."""


def bank(a, money):
    deposit = money * 10 / 100
    z = money + (deposit * a)
    return z

print("Welcome to MMM!")
money = int(input("How much money do you have?"))
a = int(input("How long will you trust to us?"))
out = bank(a, money)
print(out)