# Prog-07: EAN-13 Barcode
# ??3?????21 Name ?

import math
import matplotlib.pyplot as plt
#-------------------------------------------------
def show_barcode(digits, ean13_code): 
    x = [[int(e) for e in ean13_code]]
    plt.axis('off')         
    plt.imshow(x, aspect='auto', cmap='binary')      
    plt.title(digits)     
    plt.show()   
#-------------------------------------------------
def test1():
    digits = input('Enter a 13-digit number: ')  
    codes = encode_EAN13(digits)       
    if codes == '':
        print(digits, 'is not an EAN-13 number.')     
    else:
        decoded_digits = decode_EAN13(codes)
        if decoded_digits == digits:
            show_barcode(digits, codes)
        else:
            print('Error in decoding.')
#-------------------------------------------------
L_codes = ['0001101', '0011001', '0010011', '0111101', '0100011', \
           '0110001', '0101111', '0111011', '0110111', '0001011']
G_codes = ['0100111', '0110011', '0011011', '0100001', '0011101', \
           '0111001', '0000101', '0010001', '0001001', '0010111']
R_codes = ['1110010', '1100110', '1101100', '1000010', '1011100', \
           '1001110', '1010000', '1000100', '1001000', '1110100']

#=================================================
group1Patterns = ['LLLLLL','LLGLGG','LLGGLG','LLGGGL','LGLLGG','LGGLLG','LGGGLL','LGLGLG','LGLGGL','LGGLGL']
    
def count1(code):
    cnt = 0
    for i in code:
        if i=='1':
            cnt+=1
    return cnt

def findCode(code,codeList):
    for i in range(10):
        if code == codeList[i]:
            return str(i)

def decode(codes):
    codeList = [codes[7*i:7*i+7] for i in range(len(codes)//7)]
    digits = ""
    patterns = ""
    try:
        for code in codeList:
            if code[0]=='1':
                patterns+='R'
                digits+=findCode(code,R_codes)
            elif count1(code)%2:
                patterns+='L'
                digits+=findCode(code,L_codes)
            else:
                patterns+='G'
                digits+=findCode(code,G_codes)
        return (digits,patterns)
    except:
        return ("","")
def decode_EAN13_oneside(codes):
    if len(codes) != 95:
        return ""
    if codes[:3]!="101" or codes[-3:]!="101" or codes[45:50]!="01010":
        return ""
    group1 = codes[3:45]
    group2 = codes[50:92]
    decode1 = digits_of(group1)
    pattern = patterns_of(group1)
    decode2 = digits_of(group2)
    
    if decode1=="" or decode2=="":
        return ""
    try:
        ans = findCode(pattern,group1Patterns)+decode1+decode2
        if check_digit(ans[:-1])!=ans[-1]:
            return ""
        return ans
    except:
        return ""

def codes_of(digits, patterns):
    ans = ""
    for i in range(len(digits)):
        digit = ord(digits[i])-ord('0')
        pattern = patterns[i]
        if pattern == "L":
            ans+=L_codes[digit]
        if pattern == "R":
            ans+=R_codes[digit]
        if pattern == "G":
            ans+=G_codes[digit]
    return ans



def digits_of(codes):
    return decode(codes)[0]


def patterns_of(codes):
    return decode(codes)[1]


def check_digit(digits):
    sum = 0
    for i in range(len(digits)):
        if i%2==0:
            sum+=int(digits[i])
        else:
            sum+=3*int(digits[i])
    return str(10-((sum-1)%10+1))


def encode_EAN13(digits):
    for i in digits:
        if ord(i)<ord('0')or ord(i)>ord('9'):
            return ""
    if len(digits)!=13:
        return ""
    if check_digit(digits[:-1])!=digits[-1]:
        return ""
    group1 = codes_of(digits[1:7],group1Patterns[ord(digits[0])-ord('0')])
    group2 = codes_of(digits[7:],"RRRRRR")
    return '101'+group1+'01010'+group2+'101'
    

def decode_EAN13(codes):
    ans = decode_EAN13_oneside(codes)
    if ans == "":
        ans = decode_EAN13_oneside(codes[::-1])
    return ans


#-------------------------------------------------
test1()
# print(decode_EAN13("10101101110111001000110101001110011101010111101010100001010000101000100100001011101001101100101"[::-1]))
# print(check_digit("8850046337392"))
# print(codes_of("210292","LLGGGL"))
# print(codes_of("045192","RRRRRR"))
# print(codes_of('45', 'LG') )
# print(digits_of('01000110111001'))
# print(digits_of('01000111111111'))
# print(patterns_of('01000110111001'))
# print(patterns_of('01000111111111'))
# print(check_digit('321029204519'))
# print(check_digit('123456789018'))
# print(encode_EAN13('1234'))
# print(encode_EAN13('one-two-33333'))
# print(encode_EAN13('1111111111111'))
# print(encode_EAN13('3210292045192'))
# print(decode_EAN13('10100100110011001010011100110110010111001001101010111001010111001001110110011011101001101100101'[::-1]))