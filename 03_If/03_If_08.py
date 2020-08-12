d = int(input())
m = int(input())
y = int(input())
y-=543
x = 0
if y%4==0: 
    if y%100!=0:
        x=1
    elif y%400==0:
        x=1
if m > 1:
    d+=31
if m > 2:
    if x==0:
        d+=28
    else:
        d+=29
if m > 3:
    d+=31
if m > 4:
    d+=30
if m > 5:
    d+=31
if m > 6:
    d+=30
if m > 7:
    d+=31
if m > 8:
    d+=31
if m > 9:
    d+=30
if m > 10:
    d+=31
if m > 11:
    d+=30
print(d)