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

#Write code below please.
mean_math = math_score.mean()
mean_writing = writing_score.mean()
mean_reading = reading_score.mean()

median_math = math_score.median()
median_reading = reading_score.median()
median_writting = writing_score.median()

#Plot multiple bar graph
#Write code below please.
mean = [mean_math,mean_reading,mean_writing]
med = [median_math,median_reading,median_writting]
index_mean = [i for i in range(3)]
index_med = [i+0.40 for i in range(3)]
index_number = [i+0.20 for i in range(3)]

plt.bar(index_mean,mean,0.4,label = "Mean score",color = "orchid")
plt.bar(index_med,med,0.4,label = "Median score",color = "lightGreen")
plt.ylim(0,100)
plt.ylabel('Scores')
plt.xticks(index_number,('Math','Reading','Writing'))
plt.title('Scores by mean and median')
plt.legend(loc = 'best')
plt.show()