x = input().split()
a = []
for i in x:
    a.append(float(i))
    
mn = a[0]
mni = 0
mx = a[0]
mxi = 0
for i in range(len(a)):
    if a[i] < mn:
        mn = a[i]
        mni = i
    if a[i] > mx:
        mx = a[i]
        mxi = i
ans = 0
for i in range(len(a)):
    if i!=mni and i!=mxi:
        ans+=a[i]
print(round(ans/2,2))