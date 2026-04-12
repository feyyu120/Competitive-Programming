n = int(input())
s = input()
if n % 4 != 0:
    print("===")
    exit()
count = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
for c in s:
    if c in count:
        count[c] += 1
for c in count:
    if count[c] > n // 4:
        print("===")
        exit()
result = list(s)
for i in range(n):
    if result[i] == '?':
        for c in count:
            if count[c] < n // 4:
                result[i] = c
                count[c] += 1
                break
print("".join(result))