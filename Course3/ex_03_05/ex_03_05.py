import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL - ')
print('Retrieving', url)
time.sleep(1)
try:
    uh = urllib.request.urlopen(url, context=ctx)
except:
    print('Invalid URL')
    quit()

data = uh.read()
print('Retrieved', len(data), 'characters')
tree = ET.fromstring(data)

lst = tree.findall('comments/comment')
print('User count:', len(lst))
sum = 0
for item in lst:
    sum = sum + int(item.find('count').text)
print('Sum:', sum)
