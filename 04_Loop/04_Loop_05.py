#AAA
#AAAAAA
#ต้องตอบ 0
x = input()
y = input()
y = y.replace("\""," ",-1)
y = y.replace("("," ",-1)
y = y.replace(")"," ",-1)
y = y.replace(","," ",-1)
y = y.replace("."," ",-1)
y = y.replace("\'"," ",-1)
y = y.replace(" ","  ",-1)
x = " "+x+" "
y = " "+y+" "
print(len(y.split(x))-1)