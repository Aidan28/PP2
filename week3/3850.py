"""
lst = input().split()
for i in reversed(range(len(lst))):
    if lst[i] == '0':
        lst.append(lst.pop(i))
print(*lst)
"""
arr=list(input().split())
zeros=arr.count('0')
for i in arr:
    if i!='0':print(i,end=" ")
for i in range(zeros):
    print('0',end=" ")