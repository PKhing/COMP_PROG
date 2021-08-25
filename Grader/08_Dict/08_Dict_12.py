n = int(input())
mp = {}
mprev = {}
for i in range(n):
    a,b = input().split()
    mp[a] = b
    mprev[b] = a
q = int(input())
for i in range(q):
    s = input()
    if mp.get(s)!=None:
        print(mp[s])
    elif mprev.get(s)!=None:
        print(mprev[s])
    else:
        print("Not found")