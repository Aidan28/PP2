a, u, l = input(), 0, 0
for i in a:
    if i.isupper(): u+=1
    elif i.islower(): l+=1
print(str(u), '\n' + str(l))