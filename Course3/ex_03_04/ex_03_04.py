import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
count = input('Enter Count - ')
pos = input('Enter Position - ')
lst = list()

while int(count) > 0:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
            lst.append(tag.get('href', None))
    print(lst[int(pos)-1])
    url = lst[int(pos)-1]
    lst.clear()
    tags.clear()
    count = int(count)-1
