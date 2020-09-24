import urllib.parse
import urllib.request
from bs4 import BeautifulSoup

#run
# เปลี่ยนหน้าเว็บที่เราจะ scrape

page2 = 'นาดาวบางกอก'
url2 = 'http://th.wikipedia.org/wiki/' + urllib.parse.quote(page2)
html2 = urllib.request.urlopen(url2).read()
soup2 = BeautifulSoup(html2, 'html.parser')

#run
# ----- TO DO 2 -----
# ดึงรายชื่อนักแสดงนาดาวบางกอกมาแสดงผล

artists_list = []
print()

for i in soup2.find('span',id='นักแสดงในสังกัด').parent.find_next_sibling().find('ul').find_all('li'):
  print(i.a.text)


######################################