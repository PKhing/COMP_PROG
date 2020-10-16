def base2(i,n):
    s = ''
    while i!=0:
        s=str(i%2)+s
        i>>=1
    while len(s)<n:
        s = '0'+s
    return s
n = int(input())
k = int(input())
if n<=0 and k<=0:
    print("Invalid n and k")
elif n<=0:
    print("Invalid n")
elif k<=0:
    print("Invalid k")
else:
    s = ""
    for i in range(1,k+1):
        s+=str(i)
        s+='-'*(n-(0 if i<10 else (1 if i<100 else 2)))
    print(s[:-1])
    s = ''
    for i in range(1<<n):
        if i!=0 and i%k==0:
            print(s[:-1])
            s=''
        s+=base2(i^(i>>1),n)+','
    print(s[:-1])
