n = input()
mn1,mn2= input().split()
mn1=int(mn1)
mn2=int(mn2)
mx1 = mn1
mx2 = mn1
cnt = 0
while True:
    a = input()
    if a=="Zig-Zag":
        print(mn1,mx2)
        break
    elif a=="Zag-Zig":
        print(mn2,mx1)
        break
    x,y=a.split()
    x=int(x)
    y=int(y)
    if cnt%2==0:
        x,y = y,x
    mx1 = max(mx1,x)
    mn2 = min(mn2,y)
    mx2 = max(mx2,y)
    cnt+=1
    mn1 = min(mn1,x)

