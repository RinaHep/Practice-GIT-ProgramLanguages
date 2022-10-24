def f():
    l=[a,b,c]
    count=0
    for i in l:
        for j in l:
            for k in l:
                x=i*100+j*10+k
                if 100<=x<=N:
                    count+=1
    return count
a = int(input("Введите цифру a: "))
b = int(input("Введите цифру b: "))
c = int(input("Введите цифру c: "))
if a>10 or b>10 or c>10:
    print ("Произошла ошибка! Пожалуйста, попробуйте заново.")
N = int(input("Введите число n: "))
if N>210 and N<231:
    count = f()
else:
    print("Значение N не входит в промежуток (210;231).")
print (count)