n = int(input())
m = int(input())
tab = [[0 for i in range(n)] for i in range(n)]
ans = -1
def check1(i,j,m,ch):
    global ans
    if m==0:
        if ans==-1 or ans==ch:
            ans = ch
            return
        else:
            print("ERROR")
            exit(0)
    if tab[i][j]==ch:
        check1(i+1,j,m-1,ch)
def check2(i,j,m,ch):
    global ans
    if m==0:
        if ans==-1 or ans==ch:
            ans = ch
            return
        else:
            print("ERROR")
            exit(0)
    if tab[i][j]==ch:
        check2(i,j+1,m-1,ch)
def check3(i,j,m,ch):
    global ans
    if m==0:
        if ans==-1 or ans==ch:
            ans = ch
            return
        else:
            print("ERROR")
            exit(0)
    if tab[i][j]==ch:
        check3(i+1,j+1,m-1,ch)
def check4(i,j,m,ch):
    global ans
    if m==0:
        if ans==-1 or ans==ch:
            ans = ch
            return
        else:
            print("ERROR")
            exit(0)
    if tab[i][j]==ch:
        check4(i-1,j+1,m-1,ch)
notover = 0
for i in range(n):
    x = input().split()
    for j in range(n):
        tab[i][j]=x[j]
        if x[j]=='0':
            notover=1
        if x[j]!='0' and x[j]!='1' and x[j]!='2':
            print("ERROR")
            exit(0)
for i in range(n):
    for j in range(n):
        if tab[i][j]=='0':
            continue
        if i<=n-m:
            check1(i,j,m,tab[i][j])
        if j<=n-m:
            check2(i,j,m,tab[i][j])
        if i<=n-m and j<=n-m:
            check3(i,j,m,tab[i][j])
        if i>=m-1 and j<=n-m:
            check4(i,j,m,tab[i][j])
if ans=='1':
    print("1 WIN")
elif ans=='2':
    print("2 WIN")
else:
    if notover:
        print("NOT OVER")
    else:
        print("DRAW")