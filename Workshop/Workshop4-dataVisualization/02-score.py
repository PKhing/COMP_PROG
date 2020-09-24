import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('Workshop/Workshop4-dataVisualization/exams_100.csv')


# Create index of 100 students and save it in a list 
index_student = [idx+1 for idx in range(len(csv_data['gender']))]
#print(index_student) #นักเรียน 100 คน

#ดึงค่าคะแนนของนักเรียนทั้ง 3 วิชามาจากDataFrameของPandas
math_score = csv_data['math score']
reading_score = csv_data['reading score']
writing_score = csv_data['writing score']

#เรียงค่าคะแนนวิชาคณิตศาตร์ และวิชาการอ่านจากน้อยไปหามาก
#วิชาคณิตศาสตร์ 
#Write code below please.
math_score = list(math_score)
math_score.sort()
#วิชาการอ่าน
#Write code below please.
reading_score = list(reading_score)
reading_score.sort()

writing_score = list(writing_score)
writing_score.sort()

plt.figure(figsize=(10,6))
# Write code below please. #
x = [i for i in range(10)]
plt.plot(x,math_score[:10],color = "red",label = 'Math')
plt.plot(x,reading_score[:10],color = "lightBlue",label = 'Reading')
plt.legend(loc='best')
############################
plt.title('Line chart comparison on Math and Reading score of 10 students')
plt.ylabel('Score')
plt.xlabel('Individual student')
plt.show()