n = int(input())
arr = list(map(int, input().strip().split()))
for i in range(0, n-1):
    if i % 2 == 0:
        print(arr[i], end = ' ')