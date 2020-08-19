l=0.0
a=float(input())
r=0
x=a
while x>0:
    x//=10
    r+=1
#print(l,r)  
r = float(r)
while l<=r:
    x = (l+r)/2
    if abs(a-10**x)<=10**-10*max(a,10**x):
        print(round(x,6))
        break
    if 10**x>a:
        r=x
    else:
        l=x
    #print(x)

    