import math
n = int(input())
x = math.sqrt(2*math.pi)*n**(n+1/2)
print(x*math.e**(-n+(1/(12*n+1))))
print(x*math.e**(-n+(1/(12*n))))