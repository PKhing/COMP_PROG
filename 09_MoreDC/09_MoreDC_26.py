from collections import OrderedDict
n = int(input())
mp = OrderedDict()
for i in range(n):
    a,b = input().split(':')
    tmp = [j.strip() for j in b.split(',')]
    mp[a]=tmp
s = input()
ch = False
for i in mp:
    if i==s:
        continue
    for j in mp[s]:
        if j in mp[i]:
            ch = True
            print(i)
            break
if not ch:
    print("Not Found")
