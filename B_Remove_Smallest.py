t = int(input())    
for _ in range(t):
    n = int(input())
    lst = list(map(int,input().split()))
    lst.sort()
    p = True
    if n == 1: 
        print("YES")
        continue
    for i in range(n-1):
        if abs(lst[i] - lst[i+1]) > 1:
            p = False
            break

    if p:
        print("YES")

    else:
        print("NO")