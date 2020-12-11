s = input()
n = int(input())
dict = []
s = s.lower()
for i in range(n):
    dict.append(input())
def cut(s,st):
    ans = -1
    for x in dict:
        ch = 0
        for j in range(len(x)):
            if st+j>=len(s):
                ch=1
                break
            if s[st+j]!=x[j]:
                ch=1
                break
        if ch==0:
            ans = max(ans,st+len(x))
    return ans
tmp = ""
i=0
while i<len(s):
    x = cut(s,i)
    if x!=-1:
        if tmp!= '':
            print(tmp,end=' ')
            tmp=''
        print(s[i:x],end = ' ')
        i=x
    else:
        tmp+=s[i]
        i+=1
if tmp!= '':
    print(tmp,end=' ')