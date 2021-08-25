# Prog-10: Steganography
# 6?3?????21 Name ?

import math
import copy
import numpy
from PIL import Image

# -----------------------------------------
def load_image(filename): 
    im = Image.open(filename).convert('RGB')
    return numpy.asarray(im).tolist()         
      
def save_image(img, filename):     
    im = Image.fromarray(numpy.uint8(img))   
    im.save(filename)
  
def show_image(filename):       
    im = Image.open(filename)
    im.show()     

def clone_image(img):
    return copy.deepcopy(img)

def char_to_bits(ch):
    return ('0000000' + bin(ord(ch))[2:])[-8:]

def bits_to_char( bits ):
    return chr( bits_to_int(bits) )

def int_to_bits(n):
    return ('0'*16 + bin(n)[2:])[-16:]

def bits_to_int( bits ):
    return int(bits,2)

def main():
    op = input('E(mbed text) or G(et text): ')
    if op == 'E' or op == 'G':
        file_in = input('Input image file (.png): ')
        if file_in[-4:] != '.png':
            file_in = file_in + '.png'
        if op == 'E':
            text = input('Text to be embedded: ')
            file_out = file_in[:-4] + '_x' + '.png'
            success = embed_text_to_image(text, file_in, file_out)
            if success:
                print('The output image file is', file_out)
            else:
                print('Need a bigger image.')
        else:
            txt = get_embedded_text_from_image(file_in)
            if txt == '':
                print('No hidden text.')
            else:
                print('The hidden text is', txt)
    else:
        print('Try again, re-enter E or G')
# --------------------------------------------------
def get_embedded_bits(img):
    bits = ""
    for row in img:
        for col in row:
            for color in col:
                bits+=str(color%2)
    return bits

def embed_bits_to_image(bits,img):
    result = clone_image(img)
    cnt = 0
    for i in range(len(result)):
        for j in range(len(result[0])):
            for k in range(len(result[0][0])):
                result[i][j][k] = (result[i][j][k]&(~1))|int(bits[cnt])
                cnt+=1
                if cnt == len(bits):
                    return result

# --------------------------------------------------
def embed_text_to_image(text, file_in, file_out):
    img = load_image(file_in)
    if len(img)*len(img[0]) < math.ceil(16+(8*len(text))/3):
        return False
    bits = SPECIAL_BITS
    bits += int_to_bits(len(text))
    for i in text:
        bits+= char_to_bits(i)
    bits += SPECIAL_BITS
    result = embed_bits_to_image(bits,img)
    save_image(result,file_out)
    return True

# --------------------------------------------------
def get_embedded_text_from_image(file_in):
    img = load_image(file_in)
    bits = get_embedded_bits(img)
    if bits[:16] != SPECIAL_BITS : 
        return ""
    textlen = bits_to_int(bits[16:32])
    if bits[32+8*(textlen):32+8*(textlen)+16] != SPECIAL_BITS : 
        return ""
    text = ""
    for i in range(textlen):
        text+= bits_to_char(bits[32+8*i:32+8*(i+1)])
    return text

# --------------------------------------------------
SPECIAL_BITS = '0100111101001011'
main()