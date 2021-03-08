import re
s = input()
s1 = input()
s2= re.compile(s1)
ans = s2.search(s)
if ans != -1:
    print("First time {} occured in position: {}".format(s1,ans.start()))
else:
    print("Not found")