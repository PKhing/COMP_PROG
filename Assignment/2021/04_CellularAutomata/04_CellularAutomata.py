# Homework 4: 1D cellular automata
# apply runrule 19 times
def run20(p):
  print(p)
  for i in range(19):
    pin = list(p) # copy input list
    p = runrule(pin) # produce output list
    print(p)
# cell index 0..19
# neibourhood 5
# apply rule to cell index 2..17
def runrule(p):
  pp = 20*[0] # initialise output
  for i in range(2,18):
    pp[i] = rule1(p,i)
  return pp

def rule1(p,i):
  return int(p[i-2:i+3] == [0,0,0,0,0] or p[i-2:i+3] == [1,1,1,1,1])
# print a list without space
def prettyprint(p):
  s = "".join([str(e) for e in p])
  print(s)
# get input as string of length 20 characters
# input 10101010101010101010
# output a list of integer 0/1
def getinput():
  p = input().strip()
  p3 = [int(x) for x in p]
  return p3
# p0 = [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
def main():
  p0 = getinput()
  run20(p0)
  # mycellular() # your own initial pattern and rules, use prettyprint()
# def mycellular():
#   . . .
main()
# -----------------