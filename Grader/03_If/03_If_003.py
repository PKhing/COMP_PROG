a,b,c,d = [int(e) for e in input().split()]
if a>b:
    a,b=b,a
    if d>=a:
        if c>d:
            c=c-a
    else:
        c=c+a
    b = a+c+d
else:
    if c>a and a>=b:
        d=d+a
    if d>c:
        b=b+2
    else:
        b=b*2
print(a,b,c,d)
