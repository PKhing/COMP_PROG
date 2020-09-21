import urllib
import urllib.request as urq
import os
dir_path = os.path.dirname(os.path.realpath("__file__"))
url = 'https://www.chula.ac.th/en/academics/faculties-and-schools'
html = str(urq.urlopen(url).read().decode('utf-8'))
faculty = []
for i in html.splitlines():
  if i.find("/\">Faculty of")!= -1:
    st = i.find("/\">Faculty of")
    ed = i.find("<",st)
    faculty.append(i[st+3:ed])
for i in faculty :
  print(i)
print("Number of Faculties : "+str(len(faculty)))
