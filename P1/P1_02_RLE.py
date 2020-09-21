t = input()
if t == "str2RLE":
    s = input()
    ans = ""
    cnt=1
    for i in range(1,len(s)):
        if s[i]!=s[i-1]:
            ans+=s[i-1]+' '+str(cnt)+' '
            cnt = 1
        else:
            cnt+=1
    ans+=s[-1]+' '+str(cnt)
    print(ans)
elif t=="RLE2str":
    s = input().split()
    ans = ""
    for i in range(len(s)//2):
        ans +=s[2*i]*int(s[2*i+1])
    print(ans)
else:
    print("Error")