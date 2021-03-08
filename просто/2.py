a, b = int(input()), int(input()) 
sum, cnt = 0, 0
for i in range(a, b + 1):
    if i % 3 ==0:
        sum += i
        cnt += 1
print(sum / cnt)
