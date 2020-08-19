x = ["01","02","51","53","55","58"]
y = input()
ch = 0
for i in range(20,41):
    if str(i)==y:
        ch=1
for i in x:
    if i == y:
        ch=1
if ch == 1:
    print("OK")
else:
    print("Error")