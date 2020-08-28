x = input()
filename,year = x.split()
f = open(filename)
l = []
for s in f.read().splitlines():
    if s[:2]==year[2:]:
        l.append(float(s.split()[1]))
if len(l)==0:
    print("No data")
else:
    print(min(l),max(l),sum(l)/len(l))
