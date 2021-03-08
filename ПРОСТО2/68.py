n = int(input())
cnt = 0
arr = list(map(int, input().split()))
for i in range(1, n-1, 2):
    if arr[i-1] == arr[i+1]:
        cnt += 1
print(cnt)