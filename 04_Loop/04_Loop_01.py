size = 0
sum = 0.0
x = input()
while  x!= 'q':
    size+=1
    sum+=float(x)
    x = input()
if size==0:
    print("No Data")
else :
    print(round(sum/size,2))