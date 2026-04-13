t = int(input())

for _ in range(t):
    n = int(input())
    
    best_x = 2
    max_sum = 0

    for x in range(2, n + 1):
        s = 0
        multiple = x
        
        while multiple <= n:
            s += multiple
            multiple += x
        
        if s > max_sum:
            max_sum = s
            best_x = x

    print(best_x)
