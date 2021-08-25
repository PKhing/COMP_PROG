import math
a,b,c,d = [int(i) for i in input().split()]
if a==1:
    c,d=d,c
    if b==1:
        c=c+d
    elif b==2:
        c=c-d
    elif b!=3:
        c=c+pow(c,d)
    else:
        c=c/d
    a = (d+math.sqrt(pow(c/b,3)+d))/(2+b*d)
else:
    if a==2:
        if b>1:
            c=c+d
        if b>2:
            c=c/d
        if b>3:
            c=c+pow(c,d)
        else:
            a=math.log(c,10)
    else:
        while a>d:
            a = a-2
            if a<b:
                break
            c = c+a
print(a,b,c,d)