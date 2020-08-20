n=int(input())
y=[n]
while n!=1:
    if n%2==0:
        n//=2
    else:
        n=3*n+1
    y.append(n)
if len(y)>15:
    y = y[-15:]
ans = str(y[0])
for i in y[1:]:
    ans+="->"+str(i)
print(ans)