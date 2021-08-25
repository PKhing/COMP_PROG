def cmp(a):
    return a[1]
n = int(input())
mp = {}
for i in range(n):
    a,b = input().split()
    b = int(b)
    mp[a]=b
m = int(input())
tab = []
for i in range(m):
    s = input().split()
    s[1]=float(s[1])
    tab.append(s)
tab.sort(reverse=True,key=cmp)
ans = []
for i in tab:
    for j in i[2:]:
        if mp[j]!=0:
            mp[j]-=1
            ans.append([i[0],j])
            break
ans.sort()
for i in ans:
    print(i[0]+' '+str(i[1]))