n = int(input())
arr = list(map(int, input().strip().split()))[:n]
print(arr[n-1], end = ' ')
for i in range(n-1):
    print(arr[i], end = ' ')