t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    answer = float('inf')
    for i in range(1, n):
        answer = min(answer, max(a[i-1], a[i]))
    print(answer - 1)  