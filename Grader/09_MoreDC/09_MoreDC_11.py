n = int(input())
for i in range(n):
    s = input()
    cnt = 0
    for j in s:
        if j!='.':
            break
        else:
            cnt +=1
    ans = '.'*(cnt//2)+s[cnt:]
    print(ans)