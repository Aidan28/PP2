n = int(input())
a = input().split()
k = int(input())
m =''.join(a)
print(int(m[:k]) * int(m[k:]))