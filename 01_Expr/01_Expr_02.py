import math
a = float(input())
b = float(input())
c = float(input())
x = math.sqrt(b*b-4*a*c)
print(round((-b-x)/(2*a),3),round((-b+x)/(2*a),3))