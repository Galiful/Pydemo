import requests
from pyquery import PyQuery as pq

url = 'http://www3.uptorrentfilespacedownhostabc.info/updowm/file.php/P22OGZq.html'
post_url = 'http://www3.uptorrentfilespacedownhostabc.info/updowm/down.php'

session = requests.Session()
session.headers['Referer'] = url

r = session.get(url)
inputs = pq(r.text).find('input[type="hidden"]')
data = {pq(_).attr('name'): pq(_).attr('value') for _ in inputs}
r = session.post(post_url, data=data)

file_name = '{0}.torrent'.format(data['name'])
with open(file_name, 'wb') as f:
    f.write(r.content)