N=int (input())
K=int (input())
f1=0
f2=1
i=0
sum=0
for i in range(1,N+K-1,1):
    if (i>=K):
        sum=sum+f1
        print(f1,end="+")
    f3=f1+f2
    f1=f2
    f2=f3
print(f1)
sum=sum+f1
print(sum)