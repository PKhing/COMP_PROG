h1 = int(input())
m1 = int(input())
s1 = int(input())
h2 = int(input())
m2 = int(input())
s2 = int(input())
t1 = h1*60*60 + m1*60 + s1
t2 = h2*60*60 + m2*60 + s2
dt = t2 - t1
dh = dt // (60*60)
dt -= dh * 60*60
dm = dt // 60
dt -= dm*60
ds = dt
if ds < 0:
    ds += 60
    dm -= 1
if dm < 0:
    dm += 60
    dh -= 1
if dh < 0:
    dh += 24
print(str(dh)+":"+str(dm)+":"+str(ds))