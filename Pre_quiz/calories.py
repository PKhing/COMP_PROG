from collections import OrderedDict 
import math
m = {'P01':265.3,
'P02':246.9,
'P03':256.9,
'P04':272.5,
'P05':309.3}
def printlist(a):
    s = "["
    for i in a:
        s+=("(\'"+i[1]+'\', '+str(i[0])+'), ')
    print(s[:-2]+']')
n = int(input())
ans = []
for i in range(n):
    s = input().split(',')
    cnt = 0.0
    j=1
    while j<len(s):
        cnt+=m[s[j]]*int(s[j+1])
        j+=2
    ans.append((math.ceil(cnt),s[0]))
print('Before ascending sort')
printlist(ans)
ans.sort()
print('After ascending sort')
printlist(ans)
