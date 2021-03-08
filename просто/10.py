a =[]
while True:
    b = [i for i in input().split()]
    if b == ['end']:
        break
    else:
        a.append(b)
for i in range(len(a)):
    for j in range(len(a[0])):
        pi, mi, pj, mj = i + 1, i - 1, j + 1, j - 1
        if pi == len(a): pi = 0
        if pj == len(a[0]): pj = 0
        if mi == -1: mi = len(a) - 1
        if mj == -1: mj = len(a[0]) - 1
        print(int(a[pi][j]) + int(a[mi][j]) + int(a[i][pj]) + int(a[i][mj]), end = ' ')
    print()