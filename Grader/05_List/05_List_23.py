def cmp(x):
    return x[0]**2+x[1]**2
n = int(input())
x = []
for i in range(n):
    x.append([float(i) for i in input().split()]+[i])
x.sort(key=cmp)
ans ='#'+str(x[2][2]+1)+': ('+str(x[2][0])+', '+str(x[2][1])+')'
print(ans)