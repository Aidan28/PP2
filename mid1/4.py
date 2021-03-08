way = input()
a, b = map(int, input().split())
x, y = 0, 0
for i in way:
    if i == "L":
        x -= 1
    elif i == "R":
        x += 1
    elif i == "U":
        y += 1
    elif i == "D":
        y -= 1
    if x == a and y == b:
        print('Passed')
        exit(0)
print('Missed')