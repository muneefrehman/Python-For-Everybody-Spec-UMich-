import urllib.request, urllib.parse, urllib.error
import ssl
import json
import time

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


url = input('Enter URL - ')
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
time.sleep(1)
print('Retrieved', len(data), 'characters')


info = json.loads(data)
print('User count:', len(info))
comments = info['comments']

sum = 0
for item in comments:
    count = item['count']
    sum = sum + count

print(sum)
