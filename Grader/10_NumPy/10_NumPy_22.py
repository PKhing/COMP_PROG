import numpy as np
def mult_table(nrows, ncols):
 # คืนอาเรย์ที่มี shape เป็น (nrow, ncols) ภายในเก็บตารางสูตรคูณ (ดูตัวอย่างข ้างล่าง)
    a = np.arange(1,nrows+1,1)
    b = np.arange(1,ncols+1,1)
    a = a.reshape(nrows,1)
    return a*b
exec(input().strip()) 