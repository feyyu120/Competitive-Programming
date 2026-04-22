n = int(input())
people = list(map(int,input().split()))
if any(x == 1 for x in people):
    print("HARD")
else:
    print("EASY")
