rans = input()
ans = input()
if len(rans)!=len(ans):
    print("Incomplete answer")
else:
    cnt = 0
    for i in range(len(ans)):
        if(rans[i]==ans[i]):
            cnt+=1
    print(cnt)