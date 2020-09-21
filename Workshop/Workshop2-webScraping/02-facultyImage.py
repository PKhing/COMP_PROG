import urllib
import urllib.request as urq
import os
dir_path = os.path.dirname(os.path.realpath("__file__"))
url = 'https://www.chula.ac.th/en/academics/faculties-and-schools'
html = str(urq.urlopen(url).read().decode('utf-8'))
bf = 0
while html.find("post-media",bf+1)!=-1:
  bf = html.find("post-media",bf+1)
  st = html.find("data-src=\"",bf+1)
  ed = html.find("\"",st+10)
  image_url = html[st+10:ed]
  faculty_name = image_url[-image_url[::-1].find("/"):]
  d = urq.urlopen(image_url)
  l = open("Workshop/Workshop2/faculty_image/"+faculty_name,"wb+")
  l.write(d.read())
  l.close()