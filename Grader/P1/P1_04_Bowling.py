s = input()
def get(i):
    if i<len(s):
        return score(i)
    return 0
def score(i):
    if s[i]=='X':
        return 10
    if s[i]=='/':
        return 10-ord(s[i-1])+ord('0')
    return ord(s[i])-ord('0')
sum = 0
sum_frame = 0
frame = []
for i in range(len(s)):
    if s[i] =='X':
        if len(frame)!=9:
            sum_frame += 10+get(i+1)+get(i+2)
            frame.append(sum_frame)
            sum_frame = 0
        else:
            sum_frame +=10
    elif s[i] == '/':
        if len(frame)!=9:
            sum_frame += get(i)+get(i+1)
            frame.append(sum_frame)
            sum_frame = 0
        else: 
            sum_frame += get(i)
    else:
        if i>0 and s[i-1]!= 'X' and s[i-1]!= '/' and sum_frame == get(i-1 )and len(frame)!= 9:
            sum_frame+=score(i)
            frame.append(sum_frame)
            sum_frame = 0
        else:
            sum_frame += score(i)
frame.append(sum_frame)
for i in frame:
   # print(i)
    sum += i
x = int(input())
if 1<= x and x<=10:
    print(frame[x-1])
else: 
    print(sum)