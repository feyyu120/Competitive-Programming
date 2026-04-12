n = int(input())
database = {}
for i in range(n):
    name = input()
    if name not in database:
        print("OK")
        database[name] = 0
    else:
        database[name] += 1
        new_name = name + str(database[name])
        print(new_name)
        database[new_name] = 0