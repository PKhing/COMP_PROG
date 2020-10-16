key1 = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
key2 = ['C','D','H','S']
val = []
s = input()
for i in range(len(s)//2):
    a = s[2*i]
    b = s[2*i+1]
    val.append([a,b])
ans = ""
for i in range(1,len(val)):
    if val[i-1][0]!=val[i][0]:
        tmp = key1.index(val[i-1][0])-key1.index(val[i][0])
    else:
        tmp = key2.index(val[i-1][1])-key2.index(val[i][1])
    if tmp>0:
        ans+='+'
    ans+= str(tmp)
print(ans)
