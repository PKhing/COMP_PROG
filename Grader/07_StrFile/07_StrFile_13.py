s = input()
for i in range(len(s)):
    if not s[i].isnumeric() and not s[i].isalpha():
        s = s[:i]+' '+s[i+1:]
ch = 0
ans = ""
if s[0]==' ': s=s[1:]
for i in s:
    if i==' ':
        ch=1
    if i.isalpha():
        if ch==1:
            ch=0
            ans+=i.upper()
        else:
            ans+=i.lower()
    if i.isnumeric():
        ch=0
        ans+=i
print(ans)
