n = int(input())
a = input().split()
m = int(input())
b = input().split()
print('Missed students:')
for i in a:
    if i not in b:
        print('-', i)
print('Not in the group:')
for i in b:
    if i not in a:
        print('-', i)