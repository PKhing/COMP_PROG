import sys
s = input()
sys.stdin = open(s, 'r')
t = input()
pattern = input().split('[')[1:-1]
mp = {}
mprv = {}
for i in pattern:
    a,b = i.split(']')
    mp[a]=b
    mprv[b]=a
if t == "T2M":
    while 1:
        ch = 1
        ans = ""
        try:
            s = input()
        except:
            break
        for i in s:
            try:
                ans+=mp[i]+' '
            except:
                print("Invalid : "+s)
                ch = 0
                break
        if ch:
            print(ans)
elif t == "M2T":
    while 1:
        ch = 1
        ans = ""
        try:
            s = input()
        except:
            break
        for i in s.split():
            try:
                ans+=mprv[i]
            except:
                print("Invalid : "+s)
                ch = 0
                break
        if ch:
            print(ans)
else:
    print("Invalid code")