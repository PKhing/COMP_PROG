import numpy as np
def convex_polygon_area(p):
    p.append(p[0])
    ans = 0
    for i in range(len(p)-1):
        ans += p[i][0]*p[i+1][1]
        ans -= p[i][1]*p[i+1][0]
    return abs(ans/2)
def is_heterogram(s):
    s = s.lower()
    a = set()
    for i in s:
        if i.isalpha():
            if i in a:
                return False
            a.add(i)
    return True
def replace_ignorecase(s, a, b):
    lows = s.lower()
    lowa = a.lower()
    bf = -len(a)
    ptr = -len(a)
    ans = ""
    while lows.find(lowa,ptr+len(a))!=-1:
        bf = ptr
        ptr = lows.find(lowa,ptr+len(a))
        ans += s[bf+len(a):ptr]
        ans += b
    if ptr+len(a)<len(s):
        ans += s[ptr+len(a):]
    return ans
def top3(votes):
    l = []
    for i in votes:
        l.append((-votes[i],i))
    l.sort()
    ans = []
    cnt = 0
    for i in l:
        if cnt==3:
            break
        ans.append(i[1])
        cnt+=1
    return ans
# print(replace_ignorecase("AaAaA", "AA", "X"))
for k in range(2):
    exec(input().strip())


