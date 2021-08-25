s = input()
x = ""
for i in s:
    if i=='(':
        x+='['
    elif i=='[':
        x+='('
    elif i==')':
        x+=']'
    elif i==']':
        x+=')'
    else :
        x+=i
print(x)