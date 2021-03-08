def multiply(list):
    cnt = 1
    for i in list:
        cnt *= i
    return cnt
print(multiply((8, 2, 3, -1, 7)))