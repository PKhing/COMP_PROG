import math
sum_par = 0
sum_stroke = 0
sum_stroke_fix = 0
for i in range(9):
    par,stroke,choose = [int(i) for i in input().split()]
    if choose == 1:
        sum_stroke_fix += min(stroke,par+2)
    sum_par += par
    sum_stroke += stroke
handicap =  math.floor((1.5*sum_stroke_fix-sum_par)*0.8)
print(sum_stroke)
print(handicap)
print(sum_stroke-handicap)