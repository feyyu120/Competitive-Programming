t = int(input())    
for _ in range(t):
    sqr = list(map(int,input().split()))
    if all(x == sqr[0] for x in sqr):
        print('YES')

    else:
        print("NO")
        