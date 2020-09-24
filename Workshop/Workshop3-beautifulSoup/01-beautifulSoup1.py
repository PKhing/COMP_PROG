import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

# ----- TO DO 1.1 ----- 
# แปลงข้อมูลในตัวแปร page โดยใช้ urllib.parse.quote() ให้อยู่ในรูปแบบ percent-encoded string 
# แล้วนำไปต่อท้าย 'http://th.wikipedia.org/wiki/' แล้วเก็บไว้ในตัวแปร url ตามเดิม

url = 'http://th.wikipedia.org/wiki/' + urllib.parse.quote('จีดีเอช')
html = urllib.request.urlopen(url).read() 
soup = BeautifulSoup(html, 'html.parser')

# ----- TO DO 1.2 -----
# ลองดึงบริษัทในเครือ (อดีต) มาแสดงผลให้หน่อย
# ง่ายจะตาย :)
print(">> Affiliated corporations (Past)")
new_comp = soup('dt')[1].find_next('ul').find_all('li')

for t in new_comp:
    print(t.a.text)

#run
# ----- TO DO 1.3 -----
# จงหา link ของ social media [facebook, twitter, instagram, tv.line] มาแสดงผล
# มี code มาให้แล้ว ช่วยเติมสิ่งที่ขาดหายไปหน่อย
# Hint : หาจากคำว่า "แหล่งข้อมูลอื่น"

social_media = soup.find_all('span',string = "แหล่งข้อมูลอื่น")

# เนื่องจากเรา find_all (เพราะว่าแหล่งข้อมูลอื่นปรากฏอยู่หลายที่ในเว็บไซต์ ทำให้เราต้องเลือกว่าจะใช้อันไหน)
# เติม index ให้หน่อยว่า 0 หรือ 1 หรือ 2 หรือ 3

sm_ul = social_media[1]

# หาก inspect ดูจะพบว่าหากเราค้นหาด้วย <span> เราจะอยู่ภายใต้ <h2> 
# ดังนั้นหากต้องการไปยัง <ul> เราควรที่จะต้องถอยกลับมาที่ <h2> ก่อนแล้วถึงค่อยไปหา <ul>
# เราสามารถถอยกลับมาได้โดยใช้คำสั่ง .parent เพื่อหลับไปยัง <h2> จากนั้นใช้ find_next_sibling() เพื่อไปยัง tab ถัดไป
print(">> Social media")
for li in sm_ul.parent.find_next_sibling():
    try:
        print(li.a['href'])
    except:
        continue
