def sum(a):
    sum = 0
    for i in a:
        sum+=i
    return sum
def first_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี first fit
    for i in L:
        if sum(i)+e<=100:
            i.append(e)
            return L
    L.append([e])
    return L
def best_fit(L, e): # น ำ e ใสรำยกำรย่อยใ ่ น L ด ้วยวิธี best fit
    mx = -1
    ans = -1
    for i in range(len(L)):
        if sum(L[i])+e<=100 and sum(L[i])+e>mx:
            mx=sum(L[i])+e
            ans = i
    if ans==-1:
        L.append([e])
        return L
    L[ans].append(e)
    return L
def partition_FF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย first fit
    L = []
    for i in D:
        first_fit(L,i)
    return L
def partition_BF(D): # คืนลิสต์ของลิสต์ที่ได ้จำกกำรแบ่งข ้อมูลใน D ด ้วย best fit
    L = []
    for i in D:
        best_fit(L,i)
    return L
exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
