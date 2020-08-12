a = input()
b = input()
a = a[1:-1].split(',')
b = b[1:-1].split(',')
c = []
for i in range(3) :
    a[i] = float(a[i])
    b[i] = float(b[i])
    c.append(a[i]+b[i])
print(str(a) +' + '+str(b)+' = '+str(c))
