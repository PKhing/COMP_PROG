edge = {}
visited = set()
while True:
    s = input()
    if not ' ' in s:
        break
    a,b = s.split()
    if not a in edge:
        edge[a] = set()
    if not b in edge:
        edge[b] = set()
    edge[a].add(b)
    edge[b].add(a)
ans = set()
ans.add(s)
if not s in edge:
    edge[s]=set()
for i in edge[s]:
    ans.add(i)
    visited.add(i)
for i in visited:
    for j in edge[i]:
        ans.add(j)
lans = []
for i in ans:
    lans.append(i)
lans.sort()
for i in lans:
    print(i)
