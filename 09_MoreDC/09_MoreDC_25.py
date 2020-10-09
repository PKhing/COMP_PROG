def row_number(t, e): # return row number of t containing e (top row is row #0)
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j]==e:
                return i
def flatten(t): # return a list of ints converted from list of lists of ints t
    ans = []
    for i in range(len(t)):
        for j in range(len(t[0])):
            if t[i][j]!=0:
                ans.append(t[i][j])
    return ans
def inversions(x): # return the number of inversions of list x
    cnt = 0
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]>x[j]:
                cnt+=1
    return cnt

def solvable(t): # return True if tiling t (list of lists of ints) is solvable
# otherwise return False
    n = len(t)
    a = inversions(flatten(t))
    b = row_number(t,0)
    if n%2==1:
        if a%2==1:
            return False
    else:
        if a%2==b%2:
            return False
    return True
exec(input().strip()) # do not remove this line
