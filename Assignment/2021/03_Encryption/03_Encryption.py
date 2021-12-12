# encryption inspired by AES (Advanced Encryption Standard)
# Prabhas Chongstitvatana
key = "ABCDEFGHIJKLMNOP"
plaintext = "I LOVE PYTHON101"
def encrypt(key,text):
  t1 = oneround(key,text)
  t2 = oneround(key,t1)
  return t2
def oneround(key,text):
  t1 = addkey(key,text)
  t2 = subbyte(t1)
  t3 = shiftrow(t2)
  t4 = mixcolumn(t3)
  return t4


# ================ addkey =====================
# xor key with text, keep it in printable range
def addkey(k,t):
  s = ""
  for i in range(len(t)):
    s+= doxor(k[i],t[i])
  return s
# doxor xor ascii code of two characters c1, c2
def doxor(c1,c2):
  c3 = ord(c1)^ord(c2)
  c4 = makeprintable(c3)
  return c4
def makeprintable(c):
  c1 = ((c % 90) + 32 % 90)
  return chr(c1)


# =================== subbyte =====================
# substitute characters in t with pattern in subinput and suboutput
def subbyte(t):
  s = ""
  for i in range(len(t)):
    s += findreplace(t[i])
  return s
# findreplace use subinput and suboutput
def findreplace(c):
  index = subinput.find(c)
  c2 = suboutput[index]
  return c2
# these two functions use "for", which we will learn later, just use
# it now
def createsubinput():
  s = ""
  for i in range(32,91):
    s += chr(i)
  return s
def createsuboutput():
  s = ""
  for i in range(33,91):
    s += chr(i)
  s += chr(32)
  return s
subinput = createsubinput()
suboutput = createsuboutput()




# =================== shift row =====================
# rotate string one character to the right
def shiftonce(t):
  t1 = t[-1]+t[:-1]
  return t1
def shiftrow(t):
  t1 = shiftonce(t)
  t2 = shiftonce(t1)
  return t2



# =================== mixcolumn =====================
# coefficients use in multiply with fix polynomial in mixcolumn
# fixpoly = "2311123111233112"
# we just hardcode it into the function
def mixcolumn(t):
  fixpoly = "2311123111233112"
  s = ""
  for i in range(len(t)):
    s+= mulc(t[i],fixpoly[i])
  return s
def mulc(c1,c2):
  c3 = ord(c1)*ord(c2)
  c4 = makeprintable(c3)
  return c4



  


# =================== main =====================
def test():
  s = ""
  s += "1"
  s += "2"
  print(s)
  txt = "WHATEVER01234567"
  txt2 = subbyte(txt)
  print(plaintext)
  txt4 = oneround(key,plaintext)
  print(txt4)
  txt5 = encrypt(key,plaintext)
  print(txt5)

def main():
  # key = input()
  # plaintext = input()
  ciphertext = encrypt(key, plaintext)
  print(ciphertext)
  test()
main()
#### End ######