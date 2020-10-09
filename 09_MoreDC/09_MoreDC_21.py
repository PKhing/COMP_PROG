def factor(n):
    i = 2
    ans = []
    while i<=n and n>1:
        cnt = 0
        while n%i==0:
            n/=i
            cnt+=1
        if cnt>0:
            ans.append([i,cnt])
        i+=1
    return ans
exec(input().strip())