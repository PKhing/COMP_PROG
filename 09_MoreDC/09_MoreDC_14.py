f1 = open(input())
f2 = open(input())
f3 = open(input())
mp1 = {}
mp2 = {}
for i in f1.read().splitlines():
    a,b = i.split(',')
    mp1[a]=b
for i in f2.read().splitlines():
    a,b = i.split(',')
    mp2[a]=b
for i in f3.read().splitlines():
    a,b = i.split(',')
    if a in mp1 and b in mp2:
        print(mp1[a]+','+mp2[b])
    else:
        print("record error")
    