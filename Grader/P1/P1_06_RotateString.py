t = input()
n = int(input())
m = -1
x = []
for i in range(n):
    s = input()
    if m==-1:
        m=len(s)
    if len(s)!=m:
        print("Invalid size")
        exit(0)
    x.append(s)
if t == "90":
    for i in range(m):
        ans = ""
        for j in range(n-1,-1,-1):
            ans+=x[j][i]
        print(ans)
if t == "flip":
    for i in range(n):
        ans = ""
        for j in range(m-1,-1,-1):
            ans+=x[i][j]
        print(ans)
if t == "180":
    for i in range(n-1,-1,-1):
        ans = ""
        for j in range(m-1,-1,-1):
            ans+=x[i][j]
        print(ans)
