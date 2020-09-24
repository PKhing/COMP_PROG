import pandas as pd
import matplotlib.pyplot as plt

csv_data = pd.read_csv('Workshop/Workshop4-dataVisualization/exams_100.csv')

gender = csv_data['gender']
male = 0
female = 0
for i in gender:
  if i=="male":
    male+=1
  else:
    female+=1
print("Amount of student: "+str(len(gender)))
print("Amount of male student: "+str(male))
print("Amount of female student: "+str(female))

x = ['Male','Female']
cnt = [male,female]
pos = [i for i,val in enumerate(x)]
plt.bar(pos,cnt,color = ['lightGreen','lightBlue'])
plt.xlabel("Sex")
plt.ylabel("Amount")
plt.title("Comparison of student genders")
plt.xticks(pos,x)
plt.show()