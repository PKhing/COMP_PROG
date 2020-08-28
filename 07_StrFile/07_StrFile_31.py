s = input()
dna =""
for i in s:
    if i.upper()!='A' and i.upper()!='G' and i.upper()!='T' and i.upper()!='C':
        print("Invalid DNA")
        exit()
    else:
        dna += i.upper()
cmd = input()
if cmd=='R':
    ans = ""
    for i in dna[::-1]:
        if i=='A':
            ans+='T'
        elif i=='T':
            ans+='A'
        elif i=='G':
            ans+='C'
        else:
            ans+='G'
    print(ans)
elif cmd=='F':
    a=0
    t=0
    c=0
    g=0
    for i in dna:
        if i=='A':
            a+=1
        elif i=='T':
            t+=1
        elif i=='G':
            g+=1
        else:
            c+=1
    ans = "A="+str(a)+", T="+str(t)+", G="+str(g)+", C="+str(c)
    print(ans)
else:
    x=input()
    x=x.upper()
    cnt=0
    for i in range(len(dna)-1):
        if dna[i:i+2]==x:
            cnt+=1
    print(cnt)


