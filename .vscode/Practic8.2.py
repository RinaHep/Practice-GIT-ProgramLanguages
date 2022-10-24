M=int(input("Введите количество строк: "))
N=int(input("Введите количество столбцов: "))
k=int(input("Введите k-строку: "))
A=[]
C=[]
for i in range(M):
    B=[]
    for j in range(N):
        B.append(int(input()))
    A.append(B)
print("Первоначальная матрица")
for i in range(M):
    for j in range(N):
        print(A[i][j], end=" ")
    print()
print("Преобразованная матрица")
for i in range(M):
    D=[]
    for j in range(N):
        D.append(A[j][i])
    C.append(D)
A.clear()
C.sort(key=lambda x:x[k-1])
for i in range(M):
    B=[]
    for j in range(N):
        B.append(C[j][i])
    A.append(B)
for i in range(M):
    for j in range(N):
        print(A[i][j], end=" ")
    print()