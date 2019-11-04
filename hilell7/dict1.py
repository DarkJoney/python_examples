"""1. В единственной строке записан текст. Для каждого слова из данного текста подсчитайте, сколько раз оно встречалось в
этом тексте ранее."""

datastring = "mercedes ferrari honda renault renault mercedes ferrari honda mercedes"
counter = {}
for word in datastring.split():
        if counter.get(word, None) is None:
            counter[word] = 1
        else:
            counter[word] = counter[word]+1
print(counter)