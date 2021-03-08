a, d = map(int, input().split())
cnt = 0
while 1:
    if a > d:
        print(cnt)
        break
    a *= 3 
    d *= 2
    cnt += 1