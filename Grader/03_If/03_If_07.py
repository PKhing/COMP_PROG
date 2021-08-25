s = input()
if len(s)<=3:
    print(s)
elif len(s)==4:
    print(str(round(int(s)/1000,1))+"K")
elif len(s)<=6:
    print(str(int(int(s)/1000+0.5))+"K")
elif len(s)==7:
    print(str(round(int(s)/1000000,1))+"M")
elif len(s)<=9:
    print(str(int(int(s)/1000000+0.5))+"M")
elif len(s)==10:
    print(str(round(int(s)/1000000000,1))+"B")
else:
    print(str(int(int(s)/1000000000+0.5))+"B")