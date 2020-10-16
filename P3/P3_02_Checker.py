s = input().strip()
if len(s)<=3:
    a = s[0] 
    b = s[1:]
    ch1 = 0
    ch2 = 0
    if not a.isalpha():
        ch1=1
    try:
        b = int(b)
        if b<=0 or b>52:
            ch2=1
    except:
        ch2 = 1
    if ch1 and ch2:
        print("Invalid row and column")
        exit(0)
    elif ch1:
        print("Invalid row")
        exit(0)
    elif ch2:
        print("Invalid column")
        exit(0)
else:
    a,b = s.split(',')
    if a.find('row')==-1:
        a,b=b,a
    a=a.strip()
    b=b.strip()
    a = a[3:]
    b = b[3:]
    a=a.strip()
    b=b.strip()
    a = a[1:]
    b = b[1:]
    a=a.strip()
    b=b.strip()
    ch1 = 0
    ch2 = 0
    if not a.isalpha() or len(a)!=1:
        ch1=1
    try:
        b = int(b)
        if b<=0 or b>52:
            ch2=1
    except:
        ch2 = 1
    if ch1 and ch2:
        print("Invalid row and column")
        exit(0)
    elif ch1:
        print("Invalid row")
        exit(0)
    elif ch2:
        print("Invalid column")
        exit(0)
row = a
col = b
r = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(row)
if r%2 == int(col)%2 :
 print('Black')
else:
 print('White')