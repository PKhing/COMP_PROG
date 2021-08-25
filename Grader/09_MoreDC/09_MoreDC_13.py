n = int(input())
win = set()
lose = set()
for i in range(n):
    a,b = input().split()
    win.add(a)
    lose.add(b)
for i in lose:
    if i in win:
        win.remove(i)
print(sorted(win))