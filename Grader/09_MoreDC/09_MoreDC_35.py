n = int(input())
tab = []
for i in range(n):
    a = input().split()
    tab.append(a)
s = input().split()
ans = []
for i in tab:
    ch = True
    for j in s:
        if not j in i[1:]:
            ch=False
    if ch:
        ans.append(i)
ans.sort()
if len(ans)==0:
    print("Not Found")
for i in ans:
    s = ""
    for j in i:
        s+=j+' '
    print(s)