key = [0,3,6,9,12,15,19,22,26]
def text2keys(s):
    ans = ""
    for i in s:
        if i==' ':
            ans+='0 '
        elif i.isalpha():
            x = 0
            while ord(i.lower())-ord('a')>=key[x+1]:
                x+=1
            for j in range(ord(i.lower())-ord('a')-key[x]+1):
                ans+= str(x+2)
            ans+=' '
    return ans
def keys2text(s):
    ans = ""
    for i in s.split():
        if i=='0':
            ans+=' '
        else:
            ans+= chr(key[int(i[0])-2]+len(i)-1+ord('a'))
    return ans
# print(text2keys("I am busy.")) 
# print(keys2text("444 0 2 6 0 22 88 7777 999"))
exec(input().strip())
