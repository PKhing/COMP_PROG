import urllib
import urllib.request as urq
import os
mem_html = str(urq.urlopen("https://www.cp.eng.chula.ac.th/en/about/faculty/").read().decode('utf-8'))
bf = 0
blank_photo = urq.urlopen("http://mis.cp.eng.chula.ac.th/view.php?q=instructor/picture&v=badge&key=10019319").read()
print("Current Faculty Members\n")
retired = mem_html.find("Retired Faculty Members")
deceased = mem_html.find("Deceased aculty Members")
while mem_html.find("instructorRow",bf+1)!=-1:
  bf = mem_html.find("instructorRow",bf+1)
  if bf>retired:
    print("\nRetired Faculty Members\n")
    retired = 1e9
  if bf>deceased:
    break
  st = mem_html.find("<img src=\"",bf)
  ed = mem_html.find("\"",st+11)
  image_url = mem_html[st+10:ed]
  image_url = image_url.replace("amp;","")
  if blank_photo  != urq.urlopen(image_url).read():
    st = mem_html.find("<p>",ed)
    ed = mem_html.find("<",st+3)
    print(mem_html[st+3:ed].strip())
