n=int(input())
name = []
words = []
sum = []
for i in range(n):
    name.append(input())
    s = input()
    mp = {}
    sum.append(len(s.split()))
    for i in s.split():
        if i not in mp:
            mp[i]=0
        mp[i]+=1
    words.append(mp)
while 1:
    s = input()
    if s=='-1':
        break
    mx = 0
    ans = "NOT FOUND"
    for i in range(len(name)):
        if s in words[i]:
            val = words[i][s]/sum[i]/len(words[i])
        else:
            val = -1
        if val>mx:
            mx = val
            ans = name[i]
    print(ans)
