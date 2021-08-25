import numpy as np
import math
def p( X ):
 # X เป็นอาเรย์ขนาด n2 เก็บจ านวนโจทย์ที่ท า (คอลัมน์ 0) กับเกรดเฉลี่ย (คอลัมน์1) ของนักเรียน n คน
 # คืนอาเรย์ขนาด n ชอ่ ง เก็บความน่าจะเป็นที่นักเรียนแต่ละคนจะเรียนผ่านวิชา ค านวณจากสูตรข ้างบน
 # ใชค้ วามสามารถของ NumPy จะเขียนได ้โดยไมต่ อ้ งใชว้งวน (อย่างมาก 3 บรรทัด)
    logit = -3.98 +X[:,0]*0.1+X[:,1]*0.5
    ans = 1/(1+math.e**(-logit))
    return ans
exec(input().strip()) 