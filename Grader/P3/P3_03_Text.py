import sys
f = input()
n = int(input())
s = ""
for i in range(1,n+1):
    if i%10==0:
        s+=(str(i//10))
    else:
        s+=('-')
print(s)
sys.stdin = open(f,'r')
s = ""
while 1:
    try:
        a = input()
        s+='.'+a
    except:
        break
s = s[1:]
l = []
ptr = 0
for i in range(1,len(s)):
    if (s[i-1]=='.' and s[i]!='.') or (s[i-1]!='.' and s[i]=='.'):
        l.append(s[ptr:i])
        ptr = i
l.append(s[ptr:])
# print(l)
ans = ""
for i in l:
    if ans == "" and i[0]=='.':
        continue
    elif i[0]=='.':
        ans+=i
    elif len(ans)+len(i)<=n:
        ans+=i
    else:
        print(ans.strip('.'))
        ans = i
print(ans)