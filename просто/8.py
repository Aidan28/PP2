a = int(input())
list = []
i = 1 
while 1:
    for j in range(i):
        list.append(i)
        if len(list) == a:
            print(*list)
            exit(0)
    i += 1