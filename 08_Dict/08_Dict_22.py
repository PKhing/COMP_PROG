n = int(input())
price = {}
for i in range(n):
    a,b = input().split()
    price[a]=float(b)
q = int(input())
sales = {}
sum = 0.0
for i in range(q):
    a,b = input().split()
    b = float(b)
    if price.get(a)!=None:
        if sales.get(a)!=None:
            sales[a]+=b*price[a]
            sum+=b*price[a]
        else:
            sales[a]=b*price[a]
            sum+=b*price[a]
mx = 0.0
ans = []
for i in sales:
    if sales[i]>mx:
        ans.clear()
        mx = sales[i]
        ans.append(i)
    elif sales[i]==mx:
        ans.append(i)
ans.sort()
if mx==0.0:
    print("No ice cream sales")
else:
    print("Total ice cream sales: "+str(sum))
    s = "Top sales: "
    for i in ans:
        s+=str(i)+", "
    s = s[:-2]
    print(s)
