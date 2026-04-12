n,k=map(int,input().split())
a=list(map(int,input().split()))
maxim=1
count=1
for i in range(1,n):
    if a[i]!=a[i-1]:
        count+=1
        if count>maxim:
            maxim=count
    else:
        count=1
print(maxim)