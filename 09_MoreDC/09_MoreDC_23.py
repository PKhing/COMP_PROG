def plus(a,b):
    mn = a[0]+b[0]
    sc = a[1]+b[1]
    if sc>=60:
        mn+=1
        sc-=60
    return [mn,sc]
n = int(input())
mp = {}
for i in range(n):
    a,b,ty,t = input().split(',')
    mn,sc = [int(j) for j in t.split(':')]
    if ty in mp:
        mp[ty] = plus(mp[ty],[mn,sc])
    else:
        mp[ty] = [mn,sc]
ans = []
for i in mp:
    ans.append([mp[i],i])
ans.sort(reverse=True)
cnt = 0
for i in ans:
    cnt+=1
    s = i[1].strip()+' --> '+str(i[0][0])+':'
    if i[0][1]<10:
        s+='0'
    s+=str(i[0][1])
    print(s)
    if cnt==3:
        break