x = ["January","February","March","April","May","June","July","August","September","October","November","Deccember"]
y = input().split('/')
s = x[int(y[1])-1]+" "+y[0]+", "+y[2]
print(s)