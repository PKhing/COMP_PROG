def knows(R,x,y):
 # return True if x knows y
    return y in R[x]
def is_celeb(R,x): # return True if a is celeb, otherwise return False
 # return False if x knows someone who is not him/herself
 # return False if there exists someone in R who don't know x
 # otherwise return True
    for i in R:
        if not(x==i or x in R[i]):
            return False
    return True
def find_celeb(R):
    ans = []
    for i in R:
        if is_celeb(R,i):
            return i
    return None
 # for each person x in the party
 # if x is celeb --> return x
 # if no celeb in the party --> return None
def read_relations() :
 # build a dictionary R from inputs
 # whose structure is shown in the example
    R = dict()
    while True:
        d = input().split()
        if len(d) == 1 : break
        a,b = d
        if not a in R:
            R[a]=set()
        if not b in R:
            R[b]=set()
        R[a].add(b)
    return R
def main():
    R = read_relations()
    c = find_celeb(R)
    if c == None :
        print('Not Found')
    else:
        print(c)
exec(input().strip()) # do not remove this line