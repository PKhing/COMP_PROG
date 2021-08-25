import math
x = input().split(',')
u = int(x[1]+x[2])
if x[1]!= "":
    u-=int(x[1])
d = int("9"*len(x[2])+"0"*len(x[1]))
u = u+int(x[0])*d
xx = math.gcd(u,d)
u = int(u//xx)
d = int(d//xx)
ans = str(u) +' / '+str(d)
print(ans)
