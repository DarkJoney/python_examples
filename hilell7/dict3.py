"""Дан текст состоящий из нескольких строки. Выведите слово, которое в этом тексте встречается чаще всего. Если таких
слов несколько, выведите последнее.
Задачу необходимо решить с использованием словаря.
"""
import pprint

datastring = "Mercedes has won the most of the races until now. Mercedes holds 12 wins, over 3 for Ferrari and 2 for Red Bull. Red Bull has the best engine, but Mercedes has more skilled drivers."
counter = {}
for word in datastring.split():
        if counter.get(word, None) is None:
            counter[word] = 1
        else:
            counter[word] = counter[word]+1

maxkey = ""
maxval = 0

for x, y in counter.items():
    if maxval <= y:
        maxval = y
        maxkey = x

print("Word", maxkey, "has occured", maxval,"times")