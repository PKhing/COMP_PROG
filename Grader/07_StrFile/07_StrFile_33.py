def cmp(a,b):
    if a.split()[0][-2:] == b.split()[0][-2:]:
        return a.split()[0]<b.split()[0]
    return a.split()[0][-2:] < b.split()[0][-2:]
        
x = input()
filename1,filename2 = x.split()
file1 = open(filename1)
file2 = open(filename2)
a = file1.read().splitlines()
b = file2.read().splitlines()
i = 0
j = 0
while i<len(a) and j<len(b):
    if cmp(a[i],b[j]):
        print(a[i])
        i+=1
    else:
        print(b[j])
        j+=1
while i<len(a):
    print(a[i])
    i+=1
while j<len(b):
    print(b[j])
    j+=1