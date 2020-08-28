a = [0]*36
b = [0]*36
sa = input()
sb = input()
for i in sa:
    if i.isalpha():
        a[ord(i.lower())-ord('a')]+=1
    elif i.isnumeric():
        a[int(i)+26]+=1

for i in sb:
    if i.isalpha():
        b[ord(i.lower())-ord('a')]+=1
    elif i.isnumeric():
        b[int(i)+26]+=1
for i in range(36):
    if a[i] != b[i]:
        print("NO")
        exit()
print("YES")
