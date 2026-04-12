n,m = map(int,input().split())
matrix = []
for _ in range(n):
    lst = list(map(str,input().split()))
    matrix.extend(lst)
if any( x in {'C','Y','M'} for x in matrix):
    print("#Color")

else:
    print("#Black&White")
        

