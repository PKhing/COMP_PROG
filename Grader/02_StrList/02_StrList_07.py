s = input()
x = s[3::7]
y = s[7::5]
a = str(int(x)+int(y)+10000)
b = a[-4:-1]
su = str(int(b[0])+int(b[1])+int(b[2]))[-1]
ans = b+chr(ord('A') + int(su))
print(ans)
