import requests
from bs4 import BeautifulSoup
import os

current_path = 'C:/Users/Administrator/Desktop/file/'


def down_torrent(link):
    headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Host": "www3.uptorrentfilespacedownhostabc.info",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.360",
    }

    torrent_html = requests.get(link)
    torrent_html.encoding == 'utf-8'

    soup = BeautifulSoup(torrent_html.text, 'lxml')

    input_list = soup.find_all('input')

    down_parms = {}  #POST提交的参数
    for i in input_list:
        if i.get('name'):
            down_parms[i.get('name')] = i.get('value')
    
    print (down_parms)
    #POST地址        
    post_link = link.split('file.php')[0] + 'down.php'
    
    #下载文件保存位置
    down_dir = os.path.join(current_path, down_parms['name'])
    
    if not os.path.exists(down_dir):
        os.mkdir(down_dir)
    down_path = os.path.join(down_dir, down_parms['name'])
    down_path = down_path + '.torrent'
    s = requests.Session()
    torrent_html = s.post(post_link, headers=headers, data=down_parms)
    with open(down_path, 'wb') as f:
        for chunk in torrent_html.iter_content(10):
            f.write(chunk)



if __name__ == '__main__':
    down_torrent('http://www3.uptorrentfilespacedownhostabc.info/updowm/file.php/P22OGZq.html')