s = input()
ch = 0
if len(s) == 10 and (s[0:2]=="06" or s[0:2]=="08" or s[0:2]=="09"):
    print("Mobile number")
else:
    print("Not a mobile number")