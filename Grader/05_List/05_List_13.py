
x = []
y = []
cnt = 0
def add(a):
    global cnt
    if cnt%2==0:
        x.append(a)
    else:
        y.append(a)
    cnt+=1
n = int(input())

for i in range(n):
    add(input())
a = input().split()
for i in a:
    add(i)
while True:
    a = input()
    if a=="-1":
        break
    else:
        add(a)
y = y[-1::-1]
y+=x
y = [int(e) for e in y]

print(y)