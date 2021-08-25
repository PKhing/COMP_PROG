from collections import OrderedDict
s = input()
mp = OrderedDict()
while s!='q':
    b,a = s.split(',')
    if not a in mp:
        mp[a] = []
    mp[a].append(b)
    s = input()
for i in mp:
    s = i.strip()+": "
    for j in mp[i]:
        s+= j+', '
    print(s[:-2])
