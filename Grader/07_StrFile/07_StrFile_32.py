s = input()
ch=1

if len(s)<8:
    print("Less than 8 characters")
    ch=0

c=0
for i in s:
    if i.islower():
        c=1
if c==0:
    print("No lowercase letters")
    ch=0

c=0
for i in s:
    if i.isupper():
        c=1
if c==0:
    print("No uppercase letters")
    ch=0


c=0
for i in s:
    if i.isnumeric():
        c=1
if c==0:
    print("No numbers")
    ch=0

c=0
for i in s:
    if not i.isnumeric() and not i.isalpha():
        c=1
if c==0:
    print("No symbols")
    ch=0

s = s.lower()
c=0
for i in range(3,len(s)):
    if s[i]==s[i-1] and s[i-1]==s[i-2] and s[i-2]==s[i-3]:
        c=1
if c==1:
    print("Character repetition")
    ch=0



key = "01234567890"
c=0
for i in range(3,len(s)):
    if key.find(s[i-3:i+1])!=-1 or key[::-1].find(s[i-3:i+1])!=-1:
        c=1
        
if c==1:
    print("Number sequence")
    ch=0


key = "abcdefghijklmnopqrstuvwxyz"
c=0
for i in range(3,len(s)):
    if key.find(s[i-3:i+1])!=-1 or key[::-1].find(s[i-3:i+1])!=-1:
        c=1
if c==1:
    print("Letter sequence")
    ch=0


c=0
key = "!@#$%^&*()_+"
for i in range(3,len(s)):
    if key.find(s[i-3:i+1])!=-1 or key[::-1].find(s[i-3:i+1])!=-1:
        c=1

key = "qwertyuiop"
for i in range(3,len(s)):
    if key.find(s[i-3:i+1])!=-1 or key[::-1].find(s[i-3:i+1])!=-1:
        c=1
key = "asdfghjkl"
for i in range(3,len(s)):
    if key.find(s[i-3:i+1])!=-1 or key[::-1].find(s[i-3:i+1])!=-1:
        c=1

key = "zxcvbnm"
for i in range(3,len(s)):
    if key.find(s[i-3:i+1])!=-1 or key[::-1].find(s[i-3:i+1])!=-1:
        c=1
if c==1:
    print("Keyboard pattern")
    ch=0
if ch==1:
    print("OK")