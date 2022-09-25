f=int (input())
k=int (input())
if f<k:
    R=f+k**2-1
elif k<2 and f==3:
    R=k**2
else:
    R=f-1
print (R)            