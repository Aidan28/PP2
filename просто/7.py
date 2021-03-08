cnt = 0
sq_cnt = 0
while True:
    a = int(input())
    cnt += a
    sq_cnt += a**2
    if cnt == 0:
        break
print(sq_cnt)
