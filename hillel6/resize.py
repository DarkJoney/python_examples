"""12. Дан список целых чисел и два числа `k` и  `C`. Необходимо вставить в список на позицию с индексом `k` значение
`C`, сдвинув все элементы, имевшие индекс более `k`, вправо.
Поскольку при этом количество элементов в списке увеличивается, после считывания списка в его конец нужно будет
добавить новый элемент, используя метод `append()`.
    - Вставку необходимо осуществлять в уже введённый список, не создавая дополнительного списка.
    - Использовать метод `insert()` не разрешается."""

import random

length = int(input("Enter the list length: "))
a = random.sample(range(30), length)

print(a)
c = int(input("Enter the value to add:"))
k = int(input("Select the place to insert the value:"))
temp = a[k]
a.append("")


while length > k:
    a[length] = a[length - 1]
    length -= 1
a[k] = c
print(a)