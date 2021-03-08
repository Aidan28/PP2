a = [int(i) for i in input().split()]
a.sort()
for i in range (len(a)-1):
    if a[i] != a[i + 1]:
        if a.count(a[i]) > 1:
            print(a[i], end = ' ')
if a.count(a[len(a) - 1]) > 1:
    print(a[(len(a) - 1)])
