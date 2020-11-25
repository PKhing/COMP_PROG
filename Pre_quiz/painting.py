import math
n = int(input())
s = input().split()
tab = [[s[n*i+j] for j in range(n)] for i in range(n)]
for i in range(n-1):
    for j in range(n-1):
        x = set()
        x.add(tab[i][j])
        x.add(tab[i+1][j])
        x.add(tab[i][j+1])
        x.add(tab[i+1][j+1])
        sum = 0
        for k in x:
            if k!= 'x':
                sum+=int(k)
        if tab[i][j] == 'x':
            tab[i][j]=str(math.floor(sum/(len(x)-1)))
        if tab[i+1][j] == 'x':
            tab[i+1][j]=str(math.floor(sum/(len(x)-1)))
        if tab[i][j+1] == 'x':
            tab[i][j+1]=str(math.floor(sum/(len(x)-1)))
        if tab[i+1][j+1] == 'x':
            tab[i+1][j+1]=str(math.floor(sum/(len(x)-1)))
for i in range(n):
    s = ''
    for j in range(n):
        s+=str(tab[i][j])+' '            
    print(s)
    
