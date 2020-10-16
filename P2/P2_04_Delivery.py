# import sys
# sys.stdin = open('input.txt', 'r')
# sys.stdout = open('output.txt', 'w+')
days = [31,28,31,30,31,30,31,31,30,31,30,31]
class Date:
    def __init__(self,d,m,y):
        self.d = d
        self.m = m
        self.y = y
    def isleap(self):
        return (self.y%4==0)&(self.y%100!=0)|(self.y%400==0)
    def updateleap(self):
        if self.isleap():
            days[1]=29
        else:
            days[1]=28
    def __add__(self,d):
        self.updateleap()
        self.d += d
        while self.d > days[self.m-1]:
            self.d -= days[self.m-1]
            self.m+=1
            if self.m == 13:
                self.m = 1
                self.y += 1    
                self.updateleap()
        return self
    def validate(self):
        if self.y < 2015 :
            return "Invalid year"
        if self.m <=0 or self.m >12:
            return "Invalid month"
        self.updateleap()
        if self.d <=0 or self.d>days[self.m-1]:
            return "Invalid date"
        return "Valid"
    def __lt__(self,rhs):
        if self.y == rhs.y:
            if self.m == rhs.m:
                return self.d<rhs.d
            return self.m<rhs.m
        return self.y<rhs.y
    def __str__(self):
        return str(self.d)+"/"+str(self.m)+"/"+str(self.y+543)
    def __eq__(self,rhs):
        return self.d==rhs.d and self.m == rhs.m and self.y ==rhs.y
s = input()
tab = []
mp = { 'E':1,'Q':3,'N':7 ,'F':14}
while s!= 'END':
    num,t,d,m,y = s.split()
    date = Date(int(d),int(m),int(y)-543)
    
    if date.validate()!="Valid":
        print("Error: "+s+" --> "+date.validate())
    elif t not in mp:
        print("Error: "+s+" --> Invalid delivery type")
    else:
        date+=mp[t]
        tab.append([date,num])
    s = input()
tab.sort()
for i in tab:
    print(i[1]+": delivered on "+str(i[0]))

        