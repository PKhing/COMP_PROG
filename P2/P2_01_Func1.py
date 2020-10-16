def is_odd(n):
 # คืน (True/False) ว่า n เป็นจ านวนคี่หรือไม่
    if n%2==1:
        return True
    return False
def has_odds(x):
 # คืน (True/False) ว่า x เป็นลิสต์ที่มีข ้อมูลบางตัวเป็นจ านวนคี่
    for i in x:
        if i%2==1:
            return True
    return False
def all_odds(x):
 # คืน (True/False) ว่า x เป็นลิสต์ที่มีข ้อมูลทุกตัวเป็นจ านวนคี่
    for i in x:
        if i%2==0:
            return False
    return True
def no_odds(x):
 # คืน (True/False) ว่า x เป็นลิสต์ที่มีไม่มีข ้อมูลที่เป็นจ านวนคี่เลย
    for i in x:
        if i%2==1:
            return False
    return True

def get_odds(x):
    ans = []
    for i in x:
        if i%2==1:
            ans.append(i)
    return ans
 # คืนลิสต์ที่มีจ านวนคี่ที่มีเก็บในลิสต์ x (ล าดับก่อนหลังให ้เป็นไปตามล าดับเดียวกับใน x)
 # เชน่ x = [1,2,3,5,0] จะได ้ผลคือ [1,3,5]

def zip_odds(a, b):
    oa = get_odds(a)
    ob = get_odds(b)
    ans = []
    i = 0
    j = 0
    while i < len(oa) or j < len(ob):
        if i < len(oa):
            ans.append(oa[i])
            i+=1
        if j < len(ob):
            ans.append(ob[j])
            j+=1
    return ans

 # คืนลิสต์ที่สร้างจากการน าจ านวนคี่ใน a และ b มาสลับกันเก็บในลิสต์ผลลัพธ์ (เริ่มจากใน a ก่อน)
 # เชน่ a = [0,8,1,2,4,6,5,7,9,2,3] กับ b = [4,19,11,12,10,17] จะได ้คือ
 # [1,19,5,11,7,17,9,3]

exec(input().strip())