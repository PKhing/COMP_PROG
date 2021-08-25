def isLeap(y):
    x = 0
    if y%4==0: 
        if y%100!=0:
            x=1
        elif y%400==0:
            x=1
    return x
month = [31,28,31,30,31,30,31,31,30,31,30,31]
d,m,y = [int(e) for e in input().split()]
if isLeap(y-543) == 1:
    month[1]=29
d+=15
if d>month[m-1]:
    d-=month[m-1]
    m+=1
if m>12:
    y+=1
    m-=12
print(str(d)+'/'+str(m)+'/'+str(y))

