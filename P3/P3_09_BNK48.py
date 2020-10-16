cnt = {}
score = {}
kami = {}
cntkami = {}
while 1:
    s = input()
    if len(s)==1:
        break
    name,idol,pt = s.split()
    pt = int(pt)
    if not idol in cnt:
        cnt[idol]=set()
        score[idol]=0
    if not name in kami:
        kami[name]={}
    cnt[idol].add(name)
    score[idol]+=pt
    if not idol in kami[name]:
        kami[name][idol]=0
    kami[name][idol]+=pt
    if idol not in cntkami:
            cntkami[idol]=0
if s=='1':
    l = []
    for i in score:
        l.append([-score[i],i])
    l.sort()
    print(l[0][1]+', '+l[1][1]+', '+l[2][1])
if s=='2':
    l = []
    for i in cnt:
        l.append([-len(cnt[i]),i])
    l.sort()
    print(l[0][1]+', '+l[1][1]+', '+l[2][1])
if s=='3':
    for i in kami:
        mn = [0,""]
        for j in kami[i]:
            mn = min(mn,[-kami[i][j],j])
        cntkami[mn[1]]+=1
    l = []
    for i in cntkami:
        l.append([-cntkami[i],i])
    l.sort()
    print(l[0][1]+', '+l[1][1]+', '+l[2][1])
