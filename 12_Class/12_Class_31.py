class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "("+str(self.x)+","+str(self.y)+")"
class Rect:
    def __init__(self, p1, p2):
        self.ld = p1
        self.ru = p2
    def area(self):
        return (self.ld.x-self.ru.x)*(self.ld.y-self.ru.y)
    def contains(self, p):
        return (self.ld.x<=p.x and p.x<=self.ru.x)and(self.ld.y<=p.y and p.y<=self.ru.y)
x1,y1,x2,y2 = [int(e) for e in input().split()]
lowerleft = Point(x1,y1)
upperright = Point(x2,y2)
rect = Rect(lowerleft, upperright)
print(rect.area())
m = int(input())
for i in range(m):
    x,y = [int(e) for e in input().split()]
    p = Point(x,y)
    print(rect.contains(p)) 