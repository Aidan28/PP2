'''
sin, n = {}, int(input())
for i in range(n):
    s1, s2 = input().split()
    sin[s1] = s2
    sin[s2] = s1
x = str(input())
print(sin[x])
'''
n= int(input())
sinonym=dict()
for i in range(n):
    x,y=input().split()
    sinonym[x]=y
    sinonym[y]=x
key=input()
print(sinonym[key])