from random import *
l = [randint(1,10) for i in range(10)]
print(l)
repeated=[i for i in set(l) if l.count(i)>1]
if len(repeated) == 0:
    print("Повторяющихся элементов нет")
else:
    print(repeated)