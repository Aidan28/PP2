a = [int(i) for i in input().split()]
res = []
if len(a) == 1:
    print(a[0])
else:
    for i in range(len(a)):
        if i == len(a) - 1:
            res.append(a[i - 1] + a[0])
        else:
            res.append(a[i - 1] + a[i + 1])
print(*res)