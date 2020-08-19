x = int(input())
for i in range(x-1):
    s = ""
    for j in range(x-i-1):
        s+=" "
    s+="*"
    for j in range(2*i-1):
        s+=" "
    if i!=0: s+="*"
    print(s)
s = ""
for i in range(2*x-1):
    s+="*"
print(s)