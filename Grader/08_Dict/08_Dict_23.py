n = int(input())
mp = {}
mprev = {}
for i in range(n):
    a,b,c = input().split()
    a = a+' '+b
    b = c
    mp[a] = b
    mprev[b] = a
q = int(input())
for i in range(q):
    s = input()
    if mp.get(s)!=None:
        print(s+" --> "+mp[s])
    elif mprev.get(s)!=None:
        print(s+" --> "+mprev[s])
    else:
        print(s+" --> Not found")