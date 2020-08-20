n = int(input())
cnt = 0
queue = []
recent = [0,0]
sum = 0
cus = 0
for i in range(n):
    s = input()
    if s.split()[0] == "reset":
        cnt = int(s.split()[1])
    if s.split()[0] == "new":
        queue.append([cnt,s.split()[1]])
        print("ticket "+str(cnt))
        cnt+=1
    if s.split()[0] == "next":
        recent = queue[0]
        queue=queue[1:]
        print("call "+str(recent[0]))
    if s.split()[0] == "order":
        print("qtime "+str(recent[0])+" "+str(int(s.split()[1])-int(recent[1])))
        sum+=int(s.split()[1])-int(recent[1])
        cus+=1
    if s.split()[0] == "avg_qtime":
        print("avg_qtime "+str(round(sum/cus,4)))  
