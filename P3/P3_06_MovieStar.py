n = int(input())
mp = {}
for i in range(n):
    a,b,c = [i.strip() for i in input().split(',')]
    if b not in mp:
        mp[b] = []
    if c not in mp:
        mp[c] = []
    mp[b].append(a)
    mp[c].append(a)
l = [i.strip() for i in input().split(',')]
for i in l:
    s = i+' -> '
    if i not in mp:
        s+="Not found"
        print(s)
    else:
        for j in mp[i]:
            s+=j+', '
        print(s[:-2])