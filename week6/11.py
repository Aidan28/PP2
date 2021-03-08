def sover_4isla(n):
    cnt = 0
    for i in range(1, n):
        if n % i == 0: cnt += i
    return cnt == n
print(sover_4isla(6))