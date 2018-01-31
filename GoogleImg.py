import bs4
import sys
import urllib.request

from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"

name = input('enter word for download 20 images: ')

my_url = 'https://www.google.co.in/search?q='+name+'&num=20&newwindow=1&source=lnms&tbm=isch&sa=X&ved=0ahUKEwju0oy8o_XYAhUC2WMKHU6UBAkQ_AUICigB&biw=1366&bih=670'

opener = AppURLopener()
response = opener.open(my_url)

page_html = response.read()

page_soup = soup(page_html,"html.parser")

i = 1

for img in page_soup.findAll('img'):
    temp = img.get('src')
    if temp[:1] == "/":
        image = my_url + temp
    else:
        image = temp

    #filename = img.get('alt')
    #if len(filename)==0:
    filename = str(i)
    i = i+1

    imagefile = open(filename+".jpeg",'wb')
    imagefile.write(urllib.request.urlopen(image).read())
    imagefile.close()
