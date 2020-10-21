# TODO 2.1 สร้างฟังก์ชั่น recursive ของ Minimum Edit Distance
def edit_distance(real,fake,m,n):
  
  if m == 0:
    return 0 #เติมสิ่งที่ฟังก์ชั่นต้องคืนกลับมา เมื่อสตริงตัวที่ 1 ที่ให้เช็คเป็นสตริงเปล่า
  
  if n == 0: 
    return 0 #เติมสิ่งที่ฟังก์ชั่นต้องคืนกลับมา เมื่อสตริงตัวที่ 2 ที่ให้เช็คเป็นสตริงเปล่า
  
  #เติมสิ่งที่ฟังก์ชั่นต้องคืนกลับมา ในกรณีที่ตัวสุดท้ายของสตริงทั้ง 2 อันเหมือนกันให้ข้ามไปคำนวณตัวถัดไป
  if real[m-1] == fake[n-1]: 
    return edit_distance(real,fake,m-1,n-1)
  
  
  #เติมสิ่งที่ฟังก์ชั่นต้องคืนค่าให้สมบูรณ์ เพื่อที่ฟังก์ชั่นจะได้ทำงานถูกต้อง
  return 1+ min(edit_distance(real,fake,m-1,n),edit_distance(real,fake,m,n-1),edit_distance(real,fake,m-1,n-1))

#ในการทดสอบฟังก์ชั่น เราจะทดสอบบนสตริงเล็กๆ เช่น CAT กับ DOG
print(edit_distance("CAT","DOG",3,3))
print(edit_distance("COMP","CHAMP",4,5))
print(edit_distance("PRAYUT","PAYDAY",6,6))