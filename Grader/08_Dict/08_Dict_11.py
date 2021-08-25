def reverse(d):
    r = {}
    for i in d:
        r[d[i]]=i
    return r
def keys(d,v):
    l = []
    for i in d:
        if d[i] == v:
            l.append(i)
    return l
exec(input().strip()) 