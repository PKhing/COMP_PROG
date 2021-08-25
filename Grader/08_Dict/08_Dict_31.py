def total(pocket):
    sum = 0
    for i in pocket:
        sum+=i*pocket[i]
    return sum
def take(pocket, money_in):
    for i in money_in:
        if pocket.get(i)==None:
            pocket[i] = money_in[i]
        else:
            pocket[i] +=money_in[i]
    return pocket

def pay(pocket, amt):
    if total(pocket)<amt:
        return {}
    l = []
    for i in pocket:
        l.append([i,pocket[i]])
    l.sort(reverse=True)
    i = 0
    mp = {}
    while amt>0 and i<len(l):
      #  print(amt)
        while l[i][0]<=amt and l[i][1]>0:
            l[i][1]-=1
            amt-=l[i][0]
            if mp.get(l[i][0])==None:
                mp[l[i][0]]=1
            else:
                mp[l[i][0]]+=1
        i+=1
    if amt>0:
        return {}
    for i in mp:
        pocket[i] -=mp[i]
    return mp
    

exec(input().strip()) 