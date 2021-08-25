import math
def spiral_square(n): # n is a positive odd number
    tab = [[0 for i in range(n)] for j in range(n)]
    key = [[0,1],[-1,0],[0,-1],[1,0]]
    cnt = 1
    k = 0
    ptr = 1
    i=j=n//2
    while cnt<=n:
        for x in range(math.floor(cnt)):
            tab[i][j]=ptr
            ptr+=1
            i+=key[k][0]
            j+=key[k][1]
        cnt+=0.5
        k+=1
        k%=4
    return tab



def print_square(S):
 # เรยีกใชฟ้ ังกช์ นั นเี้พอื่ แสดงคา่ ของ S ที่เป็นลิสต์ของลิสต์ของจ านวนเต็ม
    for i in range(len(S)):
        print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))
exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
