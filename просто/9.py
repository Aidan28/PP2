a = [int(i) for i in input().split()] 
n = int(input())
if n not in a:
    print('Отсутствует')
else:
    for i in range (len(a)):
        if a[i] == n:
            print(i, end = ' ')
