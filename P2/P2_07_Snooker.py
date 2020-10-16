key = ['X','R','Y','G','W','B','P','K']
def score(s):
    ans = 0
    for i in s:
        ans += key.index(i)
    return ans
s2 = 0
s1 = 0
while 1:
    try:
        s = input()
    except:
        break
    if len(s)==0:
        break
    if s[0]=='1':
        s1 += score(s[1:])
    else:
        s2 += score(s[1:])
print(s1,s2)
if s1==s2:
    print("Tie")
elif s1>s2:
    print("Player 1 wins")
else:
    print("Player 2 wins")
