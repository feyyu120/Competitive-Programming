t = int(input())
for _ in range(t):
    n = int(input())
    if n % 4 == 0:
        print(n // 4)
    else:
        print(1 + n // 4 )
 