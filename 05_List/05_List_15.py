x = [int(e) for e in input().split()]
x.sort()
y = [x[0]]
for i in range(1,len(x)):
    if x[i]!=x[i-1]:
        y.append(x[i])
print(len(y))
print(y[:10])
