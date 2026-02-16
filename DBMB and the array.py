t = int(input())

for _ in range(t):
    n,s,x = map(int,input().split())
    a = list(map(int,input().split()))

    totalSum = sum(a)
    if totalSum == s:
        print("YES")
        continue
    while totalSum < s:
        totalSum += x
        if totalSum == s:
            print("YES")
            break
    if totalSum > s:
        print("NO")
 
