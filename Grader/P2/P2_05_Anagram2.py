a = input()
b = input()
cnta = [0]*26
cntb = [0]*26
for i in a:
    if i.isalpha():
        cnta[ord(i.lower())-ord('a')]+=1
for i in b:
    if i.isalpha():
        cntb[ord(i.lower())-ord('a')]+=1
print(a)
ch = 1
for i in range(26):
    if cnta[i]>cntb[i]:
        print(" - remove "+str(cnta[i]-cntb[i])+' '+chr(i+ord('a'))+("'s" if cnta[i]-cntb[i]>1 else ""))
        ch=0
if ch:
    print(" - None")
print(b)
ch = 1
for i in range(26):
    if cntb[i]>cnta[i]:
        print(" - remove "+str(cntb[i]-cnta[i])+' '+chr(i+ord('a'))+("'s" if cntb[i]-cnta[i]>1 else ""))
        ch=0
if ch:
    print(" - None")

