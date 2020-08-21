def make_int_list(x):
    return [int(i) for i in x.split()]
 # รับสตริง x มำแยกและแปลงเป็น int เก็บใน list แล้วคืนเป็นผลลัพธ์
 # เช่น x = '12 34 5' ได้ผลเป็น [12 34 5]
def is_odd(e):
    return e%2==1
 # คืนค่ำจริงเมื่อ e เป็นจ ำนวนคี่ ถ้ำไม่ใช่ คืนค่ำเท็จ
def odd_list(alist):
    x = []
    for i in alist:
        if i%2==1:
            x.append(i)
    return x
 # คืน list ที่มีค่ำเหมือน alist แต่มีเฉพำะตัวที่เป็นจ ำนวนคี่
 # เช่น alis = [10, 11, 13, 24, 25] จะได้ [11, 13, 25]
def sum_square(alist):
    sum = 0
    for i in alist:
        sum+=i*i
    return sum
 # คืนผลรวมของก ำลังสองของแต่ละค่ำใน alist
 # เช่น alist = [1,3,4] ได้ผลเป็น (1*1 + 3*3 + 4*4) = 26
exec(input().strip()) # ต้องมีบรรทัดนี้เมื่อส่งไป grader