m = int(input())
s1 = 0
s2 = 0
for k in range(3*m):
    a,b = input().split()
    if a=='R' and b=='P':
        s2+=1
    if a=='P' and b=='R':
        s1+=1
    if a=='P' and b=='S':
        s2+=1
    if a=='S' and b=='P':
        s1+=1
    if(a=='S' and b=='R'):
        s2+=1
    if(a=='R' and b=='S'):
        s1+=1
    if s1==m:
        print(s1,s2)
        print("Player 1 wins")
        exit(0)
    if s2==m:
        print(s1,s2)
        print("Player 2 wins")
        exit(0)
print(s1,s2)
print("Tie")