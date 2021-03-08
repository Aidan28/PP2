s = input().split()
max = len(s[0])
for i in s:
    if len(i) > max:
        max = len(i)
for i in s:
    if len(i) == max:
        print(i)
        print(len(i))
        exit(0)