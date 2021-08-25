class piggybank:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
        self.d = 0
    # มีตัวแปร 4 ตัวเก็บจ านวนเหรียญของเหรียญแต่ละแบบ
    def add1(self, n):
        self.a+=n
    # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญบาท
    def add2(self, n):
        self.b+=n
    # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญสองบาท
    def add5(self, n):
        self.c+=n
    # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญห้าบาท

    def add10(self, n):
        self.d+=n
    # เพิ่ม n ในตัวแปรที่เก็บจ านวนเหรียญสิบบาท
    def __int__(self):
        return self.a+self.b*2+self.c*5+self.d*10
    # คืนมูลค่ารวม = ค่าของเหรียญคูณกับจ านวนเหรียญ
    def __lt__(self, rhs):
        return int(self)<int(rhs)
    # เปรียบเทียบจ านวนเงินใน self กับจ านวนเงินใน rhs
    def __str__(self):
        return "{1:"+str(self.a)+', 2:'+str(self.b)+', 5:'+str(self.c)+', 10:'+str(self.d)+'}'
    # คืนสตริงที่แสดงจ านวนเหรียญแต่ละแบบตามตัวอย่าง
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
