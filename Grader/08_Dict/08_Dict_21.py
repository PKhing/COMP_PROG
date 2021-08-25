cnt = [[0,i] for i in range(26)]
for i in input():
    if i.isalpha():
        cnt[ord(i.lower())-ord('a')][0] -=1
cnt.sort()

for i in cnt:
    if i[0]!=0:
        print(chr(ord('a')+i[1])+' -> '+str(-i[0]))