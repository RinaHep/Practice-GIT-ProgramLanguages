def f():
    s=(int(input("Введите последовательность слов: ")))
    return ' '.join(s.split(" ")[::-1])
n=f()
print(n)