def add(s):
    if s=='A' or s=='B+':
        return 'A'
    if s=='B':
        return 'B+'
    if s=='C+':
        return 'B'
    if s=='C':
        return 'C+'
    if s=='D+':
        return 'C'
    if s=='D':
        return 'D+'
    if s=='F':
        return 'D'
no = []
grade = []
a = input()
while a!='q':
    no.append(a.split()[0])
    grade.append(a.split()[1])
    a=input()
plus = input().split()
for i in range(len(no)):
    if no[i] in plus:
        grade[i]=add(grade[i])
    print(no[i],grade[i])