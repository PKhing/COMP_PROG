import sys
# f= "input.txt"
f = input()
op = input()
sys.stdin = open(f,'r')
tab = []
dot = []
pri = []
while 1:
    try:
        s = input()
        tab.append(s)
    except:
        break
for j in range(len(tab[0])):
    ch = 1
    for i in range(len(tab)):
        if tab[i][j]!='.':
            ch=0
    dot.append(ch)
if op=='LSTRIP':
    ch = 1
    for i in dot:
        if i!=1:
            ch = 0
        pri.append(ch)
    for i in tab:
        ans = ""
        for j in range(len(i)):
            if pri[j]==0:
                ans+=i[j]
        print(ans)
elif op=='RSTRIP':
    ch = 1
    for i in dot[::-1]:
        if i!=1:
            ch = 0
        pri.append(ch)
    pri = pri[::-1]
    for i in tab:
        ans = ""
        for j in range(len(i)):
            if pri[j]==0:
                ans+=i[j]
        print(ans)
elif op=='STRIP':
    ch = 1
    for i in dot:
        if i!=1:
            ch = 0
        pri.append(ch)
    ch = 1
    for i in range(len(dot)-1,-1,-1):
        if dot[i]!=1:
            ch = 0
            break
        pri[i]=ch
    for i in tab:
        ans = ""
        for j in range(len(i)):
            if pri[j]==0:
                ans+=i[j]
        print(ans)
elif op=="STRIP_ALL":
      for i in tab:
        ans = ""
        for j in range(len(i)):
            if dot[j]==0:
                ans+=i[j]
        print(ans)
else:
    print("Invalid command")