import requests

'''https://cataas.com'''

r1 = requests.get('https://cataas.com/cat?json=true')

with open('text.txt', 'wb') as fd:
    for chunk in r1.iter_content(chunk_size=128):
        fd.write(chunk)


r2 = requests.get('https://cataas.com/cat/gif')
with open('text1.txt', 'wb') as fd:
    for chunk in r2.iter_content(chunk_size=128):
        fd.write(chunk)

r3 = requests.get('https://cataas.com/api/cats?tags=cute')
with open('text2.txt', 'wb') as fd:
    for chunk in r3.iter_content(chunk_size=10):
        fd.write(chunk)



