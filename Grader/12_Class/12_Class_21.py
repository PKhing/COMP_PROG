class Complex :
    def __init__(self,a,b):
        self.r = a
        self.i = b
    def __str__(self):
        s = ""
        if self.r==0 and self.i==0:
            return '0'
        if self.r!=0:
            s = str(self.r)
            if self.i>0:
                s+='+'
        if self.i!=0 and self.i!=1 and self.i!=-1:
            s+=str(self.i)
        if self.i==-1:
            s+='-'
        if self.i!=0:
            s+='i'
        return s
    def __add__(self, rhs):
        return Complex(self.r+rhs.r,self.i+rhs.i)
    def __mul__(self, rhs):
        a = self.r
        b = self.i
        c = rhs.r
        d = rhs.i
        return Complex(a*c-b*d,a*d+b*c)
    def __truediv__(self, rhs):
        a = self.r
        b = self.i
        c = rhs.r
        d = rhs.i
        return Complex((a*c+b*d)/(c**2+d**2),(b*c-a*d)/(c**2+d**2))
t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)