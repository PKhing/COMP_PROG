s = input()
if s[-1]=='s' or s[-1]=='x' or s[-2:]=='ch':
    print(s+"es")
elif s[-1]=='y' and (s[-2]!='a' and s[-2]!='e' and s[-2]!='i' and s[-2]!='o' and s[-2]!='u' ):
    print(s[:-1]+"ies")
else:
    print(s+"s")