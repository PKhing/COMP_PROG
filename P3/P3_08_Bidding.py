n = int(input())
tab = {}
ans = {}
pay = {}
for t in range(n):
    s = input().split()
    name = s[1]
    id = s[2]
    if s[0]=='W':
        if id in tab:
            if name in tab[id]:
                tab[id][name] = [-1,-t]
    else:
        price = int(s[3])
        if id not in tab:
            tab[id] = {}
        tab[id][name] = [price,-t]
        if name not in ans:
            ans[name] = []
            pay[name] = 0
for i in tab:
    mx = [0,-1]
    name = ""
    for j in tab[i]:
        if tab[i][j]>mx:
            mx = tab[i][j]
            name = j
    if name =='':
        continue
    ans[name].append(i)
    pay[name]+=mx[0]
l = []
for i in ans:
    ans[i].sort()
    l.append([i,pay[i],ans[i]])
l.sort()
for i in l:
    s = i[0]+': $'+str(i[1])+(" -> " if i[1]!=0 else"")
    for k in i[2]:
        s+=' '+k
    print(s)


    
