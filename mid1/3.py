n = int(input())
a = set()
l = [int(i) for i in input().split()]
for i in l:
    a.add(i)
if len(a) == len(l):
    print('YES')
else:
    print('NO')