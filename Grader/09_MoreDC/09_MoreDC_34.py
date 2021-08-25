def pattern1(n, m):
    # nrows  0, ncols  0
    tab = [[0 for j in range(m)] for i in range(n)]
    cnt = 1
    for i in range(n):
        for j in range(m):
            tab[i][j]=cnt
            cnt+=1
    return tab
def pattern2(n, m):
    # nrows  0, ncols  0
    tab = [[0 for j in range(m)] for i in range(n)]
    cnt = 1
    for j in range(m):
        for i in range(n):
            tab[i][j]=cnt
            cnt+=1
    return tab
def pattern3(n): # N  0
    cnt = 1
    tab = [[0 for j in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(i,n):
            tab[i][j]=cnt
            cnt+=1
    return tab
def pattern4(n): # N  0
    cnt = 1
    tab = [[0 for j in range(n)]for i in range(n)]
    for j in range(n):
        for i in range(j,-1,-1):
            tab[i][j]=cnt
            cnt+=1
    return tab
def pattern5(n): # N  0
    cnt = 1
    tab = [[0 for j in range(n)]for i in range(n)]
    for i in range(n):
        for j in range(n-i):
            tab[j][j+i]=cnt
            cnt+=1
    return tab
def pattern6(n): # N  0
    cnt = 1
    tab = [[0 for j in range(n)]for i in range(n)]
    for i in range(n):
        if i%2==0:
            for j in range(n-i):
                tab[j][j+i]=cnt
                cnt+=1
        else:
            for j in range(n-i-1,-1,-1):
                tab[j][j+i]=cnt
                cnt+=1
    return tab

exec(input().strip())