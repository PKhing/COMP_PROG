def add_poly(p1, p2):
    mp = {}
    for a,x in p1:
        if not x in mp:
            mp[x]=0
        mp[x]+=a
    for a,x in p2:
        if not x in mp:
            mp[x]=0
        mp[x]+=a
    ans = []
    for i in mp:
        if mp[i]!=0:
            ans.append([i,mp[i]])
    ans.sort(reverse = True)
    rans = []
    for i in ans:
        rans.append(tuple([i[1],i[0]]))
    return rans
def mult_poly(p1, p2):
    mp = {}
    for a1,x1 in p1:
        for a2,x2 in p2:
            if not x1+x2 in mp:
                mp[x1+x2]=0
            mp[x1+x2]+=a1*a2
    ans = []
    for i in mp:
        if mp[i]!=0:
            ans.append([i,mp[i]])
    ans.sort(reverse = True)
    rans = []
    for i in ans:
        rans.append(tuple([i[1],i[0]]))
    return rans
# ต้องมีสองค ำสงั่ ข ้ำงล่ำงนี้ ตอนสง่ ให้Grader ตรวจ
for i in range(3):
    exec(input().strip())