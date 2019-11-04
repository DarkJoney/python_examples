"""
3. Пользователь вводит, отдельно, строку `s` и один символ `ch`. Необходимо выполнить поиск в строке `s` всех символов `ch`.
Для решения можно использовать только функцию `find`(rfind), операторы  `if` и `for`(while).
"""

s = input("Enter the string:")
ch = input("Enter the symbol to look for:")

print(s.find(ch))
x = 0
while x != -1:
    x = s.find(ch, x+1)
    if x != -1:
        print(s[x], " at " , x, sep='')
