import urllib.request, urllib.parse, urllib.error
import json

url = input('Enter location: ')
print('Retrieving', url)
uh = urllib.request.urlopen(url)
data = uh.read()
print('Retrieved', len(data), 'characters')
info = json.loads(data)
info = info['comments']
print('Count:', len(info))

sum = 0

for i in info:
    x = i['count']
    x = int(x)
    sum = sum + x
    
print('Sum:', sum)
