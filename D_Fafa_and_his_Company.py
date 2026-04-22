n = int(input())   
way = 0 
for i in range(1,n//2 + 1):
    if n %i == 0 and (n-i) % i == 0:
        way += 1
print(way)