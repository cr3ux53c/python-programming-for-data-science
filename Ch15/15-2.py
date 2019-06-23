import urllib.request
from bs4 import BeautifulSoup

with open("researcher.xml", "r", encoding = "utf-8") as researcher_xml:
    xml = researcher_xml.read()

soup = BeautifulSoup(xml,"html.parser")

for i,element in enumerate(soup.findAll('researcher')):
    if i%2==1:
        print(element['researcherid'])
        print(element.na.get_text())
        print(element.salary)
    else:
        pass
