x = input().split()
n = len(x)
s = input()
for c in s:
    if c=='C':
        x =x[n//2:]+x[:n//2]
    if c=='S':
        y=[]
        for i in range(n//2):
            y.append(x[i])
            y.append(x[i+n//2])
        x=y
ans = ""
for i in x:
    ans+=i+' '
print(ans)