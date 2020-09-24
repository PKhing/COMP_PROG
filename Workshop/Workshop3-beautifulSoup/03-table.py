import urllib.parse
import urllib.request
import copy
from time import sleep
from bs4 import BeautifulSoup

url = 'http://th.wikipedia.org/wiki/' + urllib.parse.quote('จีดีเอช')
html = urllib.request.urlopen(url).read() 
soup = BeautifulSoup(html, 'html.parser')

#ค้นหาตารางที่เก็บข้อมูลภาพยนตร์

table2 = soup.find_all('span', string='ภาพยนตร์')[1].find_next('table')

# 4.1.4 ดึงข้อมูลภาพยนตร์ของ GDH จากหน้าวิกิพีเดีย ว่าหนังแต่ละเรื่องเข้าฉายเมื่อไหร่ ทำรายได้ไปมากน้อยแค่ไหน และใครเป็นผู้กำกับ
rows = table2('tr')
head = ['year','name','director','company','release','url']
movies = []
rows = rows[1:]
for i in range(len(rows)):
  movies.append({})
for i in range(len(rows)):
  j = 0
  for cell in rows[i]('td'):
    while j<5 and movies[i].get(head[j],-1)!=-1:
      j+=1
    if j>=5:
      break
    for k in range(int(cell.get('rowspan',1))):
      movies[i+k][head[j]] = cell.text.strip()
    if head[j]=='name':
      if cell.a == None:
        movies[i]['url'] = '-'
      else:
        movies[i]['url'] = cell.a['href']
for movie in movies:
  s = ""
  for j in head:
    s+="\'"+j+"\': \'"+movie[j]+'\', '
  s = s[:-2]
  print("{"+s+"}\n")

# 4.1.5 : แสดงผลรายได้ของหนังแต่ละเรื่อง

for movie in movies:
    print('Processing ' + movie['name'] + '...')
    
    try:
        movie_html = urllib.request.urlopen('http://th.wikipedia.com' + movie['url'])
        movie_soup = BeautifulSoup(movie_html, 'html.parser')
        
        # ค้นหารายได้ของภาพยนตร์
        income_td = movie_soup.find('th', text='รายได้').find_next()
        movie['gross'] = income_td.text.split(" ")[0]
    except Exception as e:
        movie['gross'] = 'unknown'
    
    # มารยาทในการดึงข้อมูลเราควรที่จะต้องใส่ sleep เพื่อไม่ให้ server ทำงานหนักเกินไป
    sleep(1) 

for m in movies:
    print('"%s", "%s", "%s", "%s ล้านบาท"' % 
          (m['name'], m['release'], m['director'], m['gross']))