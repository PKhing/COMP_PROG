import math
def days_in_feb(y): # คืนจ านวนวันของเดือนกุมภาพันธ์ในปี y
    y1=y-543
    days_in_feb1 = 28
    if y1 % 400 == 0 or y1 % 100 != 0 and y1%4 == 0 :
        days_in_feb1 = 29
    return days_in_feb1
def days_in_month(m1,y): # คืนจ านวนวันของเดือน m ในปี y
    days_in_m1 = 31
    if m1==4 or m1==6 or m1==9 or m1==11 :
        days_in_m1 = 30
    elif m1==2 :
        days_in_m1 = days_in_feb(y)
    return days_in_m1
def days_in_between(d1,m1,y1,d2,m2,y2):
    days = 0
    if m1 < 12 : days += 31
    if m1 < 11 : days += 30
    if m1 < 10 : days += 31
    if m1 < 9 : days += 30
    if m1 < 8 : days += 31
    if m1 < 7 : days += 31
    if m1 < 6 : days += 30
    if m1 < 5 : days += 31
    if m1 < 4 : days += 30
    if m1 < 3 : days += 31
    if m1 < 2 : days += days_in_feb(y1)
    if m2 > 1 : days += 31
    if m2 > 2 : days += days_in_feb(y2)
    if m2 > 3 : days += 31
    if m2 > 4 : days += 30
    if m2 > 5 : days += 31
    if m2 > 6 : days += 30
    if m2 > 7 : days += 31
    if m2 > 8 : days += 31
    if m2 > 9 : days += 30
    if m2 > 10 : days += 31
    if m2 > 11 : days += 30
    days += (days_in_month(m1,y1) - d1 + 1) + int((y2 - y1 - 1)*365) + (d2 - 1)
    return days
 # คืนจ านวนวันตั้งแต่วันเดือนปีd1,m1,y1 ถึง d2,m2,y2
d1,m1,y1,d2,m2,y2 = input().split()
x = days_in_between(int(d1),int(m1),int(y1),int(d2),int(m2),int(y2))
print(x,"{:.2f}".format(math.sin(2*math.pi*x/23)),"{:.2f}".format(math.sin(2*math.pi*x/28)),"{:.2f}".format(math.sin(2*math.pi*x/33)))