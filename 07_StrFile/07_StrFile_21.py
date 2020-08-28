s = input()
while s!="end":
    ans = ""
    for i in s:
        if i.isalpha():
            if i.isupper():
                ans+=chr((ord(i)-ord('A') + 13)%26+ord('A'))
            else:
                ans+=chr((ord(i)-ord('a') + 13)%26+ord('a'))
        else:
            ans+=i
    print(ans)
    s=input()
