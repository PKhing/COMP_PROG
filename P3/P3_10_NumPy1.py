import numpy as np
def eq(A, B, p):
    cnt = np.equal(A,B).sum()
    sum = 1
    for i in A.shape:
        sum*=i
    return cnt/sum*100>=p
    # A และ B เป็นอาเรย์ที่มีขนาดเท่ากัน (กี่มิติก็ได ้), p เป็นจ านวนระหว่าง 0 ถึง 100
    # คืน True ถ้าข ้อมูลใน A กับใน B ที่ต าแหน่งเดียวกันมีค่าเท่ากันอย่างน้อยร้อยละ p ของจ านวนชอ่ งทัง้หมด
    # ถ้ามีไม่ถึงก็คืน False
def closest_point_indexes(points, p):
    x = points[:,0]
    y = points[:,1]
    dist = ((x-p[0])**2+(y-p[1])**2)
    mn = dist.min()
    idx = np.arange(0,len(points),1)
    return idx[dist==mn]
    # points คืออาเรย์สองมิติที่มี 2 คอลัมน์ คอลัมน์ 0 เก็บพิกัด x คอลัมน์ 1 เก็บพิกัด y
    # p คืออาเรย์มิติเดียว 2 ชอ่ ง เก็บพกิ ัด x และ y
    # คืน อาเรย์ที่เก็บ index ของจุดต่าง ๆ ใน points ที่อยู่ใกล ้กับจุด p มากสุด
    # ถ้ามีหลายจุดที่ใกล ้สุดเท่ากัน ให ้เก็บ index ทั้งหลายเรียงจากน้อยไปมาก
def number_of_inversions(A):
    cnt = 0
    for i in range(len(A)):
        #print(np.append(np.zeros(len(A)-i),A[:i]))
        #print(np.less(A,np.append(A[i:],np.zeros(i))))
        cnt+= np.less(A,np.append(np.zeros(len(A)-i),A[:i])).sum()
    return cnt
    # A เป็นอาเรย์หนึ่งมิติเก็บจ านวนเต็ม
    # คืน จ านวนคู่ข ้อมูลใน A ที่ตัวทางซา้ยมากกวา่ ตัวขวา
    # (คือมีข ้อมูล A[i] กับ A[j] ที่ i < j แต่ A[i] > A[j] อยู่กี่คู่)
    # เชน่ [1 2 9 4 8 7] มี4 คู่คือ 9 กับ 4, 9 กับ 8, 9 กับ 7 และ 8 กับ 7
    # [9 7 5 3 2] มี 10 คู่ เพราะทกุ คมู่ ตี ัวซา้ยมากกวาตัวขว ่ า ในขณะที่ [2 4 6 8] มี 0 คู่

exec(input().strip()) # ตอ้ งมคี าสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ