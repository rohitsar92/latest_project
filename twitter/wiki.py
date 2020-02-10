
from urllib.request import urlopen

from bs4 import  BeautifulSoup

names = input(str("enter the name:"))
html = urlopen('https://en.wikipedia.org/wiki/' + 'names')
page = BeautifulSoup(html.read(),"lxml")

head = page.findAll({"h1","h2","h3","p"})
for allheading in head:
    print(allheading.text)
    
#savefile = open("withheader.text","w")
#savefile.write(str(html))
#savefile.close()
#print(head)

#print(page.h1)
#print(page.h2)
