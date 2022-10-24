from random import *
mas=[randint(1,30) for i in range(15)]
modified=[]
for i in range(15):
    modified.append(mas[i])
    if mas[i]<10: 
        modified[i]=0 
    elif mas[i]>20:
        modified[i]=1
print("Первоначальный массив:\n",mas,"\n","Преобразованный массив:\n",modified)