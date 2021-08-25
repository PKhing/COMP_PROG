s = input()
x = ['0','1','2','3','4','5','6','7','8','9']
for i in s:
    if i in x:
        x.remove(i)
ans = ""
for i in range(len(x)):
    if i!=0:
        ans+=','
    ans+=x[i]
if len(x) == 0:
    print("None")
else:
    print(ans)
