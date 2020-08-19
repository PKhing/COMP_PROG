s = '0'+input()
cnt=0
ans = ""
for i in range(1,len(s)):
    if s[i]!=s[i-1]:
        if i!=1:
            ans+=str(cnt)+' '
        ans+=s[i]+' '
        cnt=1
    else :
        cnt+=1
ans+=str(cnt)
print(ans)