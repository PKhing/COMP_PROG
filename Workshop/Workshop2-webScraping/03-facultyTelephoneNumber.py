import urllib
import urllib.request as urq
import os
dir_path = os.path.dirname(os.path.realpath("__file__"))
url = 'https://www.chula.ac.th/en/academics/faculties-and-schools'
html = str(urq.urlopen(url).read().decode('utf-8'))
bf = 0
while(html.find("post-entry",bf+1)!=-1):
  bf = html.find("post-entry",bf+1)
  st = html.find("<a href=\"",bf+1)
  ed = html.find("\"",st+9)
  #print(html[st+9:ed])
  url_fac = html[st+9:ed-1]
  faculty_name = url_fac[-url_fac[::-1].find("/"):]
  print(faculty_name)
  html_fac = str(urq.urlopen(url_fac).read().decode('utf-8'))
  st = html_fac.find("Tel:")
  st = html_fac.find(">",st)
  ed = html_fac.find("<br />",st)
  tel = html_fac[st+1:ed]
  tel = tel.replace("+66","0")
  tel = tel.replace("&#8211;","-")
  tel = tel.replace("</span>","")
  tel = tel.strip()
  print(tel+'\n')
