M=int(input("Введите количество строк: "))
N=int(input("Введите количество столбцов: "))
A=[]
P=[]
#ввод матрицы
for i in range(M):
    B=[]
    for j in range(N):
        B.append(int(input()))
    A.append(B)
#вывод матрицы
for i in range(M):
    for j in range(N):
        print(A[i][j], end=' ')
    print()

for i in range(M):
    P=sorted(A[i])
    if A[i]==P or A[i]==P[::-1]:
        print(max(A[i]))#максимальный элемент строк