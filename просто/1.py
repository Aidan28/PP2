c, d, a, b = int(input()), int(input()), int(input()), int(input())
print(' ', '\t', end='')
for i in range(a, b + 1):
    print(i, end='\t')
print()
for i in range(c, d + 1):
    print(i, end='\t')
    for j in range(a, b + 1):
        print(i * j, end='\t')
    print()