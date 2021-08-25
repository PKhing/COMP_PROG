a = list(input())
x = 0
y = ""
for i in range(len(a)):
    x += (13-i)*int(a[i])
    y+=a[i]
    if i==0 or i==4 or i==9:
       y+=' '
x = (11-x%11)%10
y+= ' '+str(x)
print(y)

