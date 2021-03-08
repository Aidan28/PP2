s = input()
i = 0
while i < len(s):
    cnt = 0
    ch = s[i]
    while i < len(s):
        if s[i] == ch:
            cnt += 1
            i += 1
        else:
            break
    print(ch + str(cnt), end='')
    