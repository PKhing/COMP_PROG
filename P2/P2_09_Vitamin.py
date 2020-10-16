from collections import OrderedDict
n = int(input())
mp = OrderedDict()
for i in range(n):
    s = input().split()
    mp[s[0]]=[float(j) for j in s[1:]]
op = input()
if op == 'show':
    for i in mp:
        s = ''
        s+= i
        for j in mp[i]:
            s+=' '+str(j)
        print(s)
    exit(0)
op,x =op.split()
if op == 'get':
    i=x
    if i not in mp:
        print(i+" not found")
        exit(0)
    s = ''
    s+= i
    for j in mp[i]:
        s+=' '+str(j)
    print(s)
if op == 'avg':
    x = int(x)-1
    sum = 0
    for i in mp:
        sum += mp[i][x]
    print(round(sum/len(mp),4))
if op == 'max':
    x = int(x)-1
    p = ""
    mx = 0
    for i in mp:
        if mp[i][x]>mx:
            p = i
            mx = mp[i][x]
        if mp[i][x]==mx and i<p:
            p = i
            mx = mp[i][x]
    print(p,mx)
if op == 'sort':
    x = int(x)-1
    l = []
    for i in mp:
        l.append(([mp[i][x]],i))
    l.sort()
    s = ''
    for i in l:
        s+=i[1]+' '
    print(s)
