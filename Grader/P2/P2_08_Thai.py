def to_Thai(x):
    key = ["soon",'neung','song','sam','si','ha','hok','chet','paet','kao']
    ans = ""
    s = str(x)
    while len(s)<4:
        s = '0'+s
    if x<10:
        return key[x]

    if s[0]!='0':
        ans += ' '+key[int(s[0])]
        ans += ' pun'

    if s[1]!='0':
        ans += ' '+key[int(s[1])]
        ans += ' roi'


    if s[2]!='1' and s[2]!='0' and s[2]!='2':
        ans += ' '+key[int(s[2])]
    elif s[2]=='2':
        ans += ' yi'
    if s[2]!='0':
        ans += ' sip'


    if s[3]!= '1' and s[3]!= '0':
        ans += ' '+ key[int(s[3])]
    elif s[3] == '1':
        ans += ' et'
    return ans.strip()
exec(input().strip())

