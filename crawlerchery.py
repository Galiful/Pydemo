import requests
from requests.exceptions import RequestException
import json
import time

# ajax 请求获取|网页认证|文件下载

def get_page(url):
    #获取pdf文件json
    try:
        headers = {
            'Cookie': 'DigestTracker=AAABb4Lzmkc; JSESSIONID=0000BATfwSfFt-lqb5vaX8060Nz:1a1vdtiv5; LtpaToken2=ZijBosJo7qik5wPGRWQcafg1oGq+/6Fs9pOvbm3N1cnSZFWbfBw+26c2dSi+7+guw4Aab6li/RYvtcrNM4mCzYUBwY1HIvf6Q5E4u61cAde9EzVzVZIkPKdXx7fOd8StYDj5Si8fX4oIJAuV1Oe2NeaSnVcmE+sbX4nZ48MihI/DjJd1VD3PLUXafJd5rk0Z5zLTnrnDwsfki1V/la4wCs/gAXiRyzOyJkXmIyYxz6aAQIryqDszA30A12fgZ8ZwaNdvyh9iDETFkmOLheSMhn+76DSQrCn47hdwsXfcjFOF3Ntt2gTLmY89Tju5rxXq5sLccyx7uDGPEgRMVPu5Vz6orDwy2aX+YF/dOP+qwqbHTEP5KBgdiJ2V8E9dLrvDuDPn34PCGXjRbRTu923wnM7GIafScZLNAyEz337IKpgjFWX5S29oNBXjUcdSafKtsUg/aVFMaJ2awq0E1N9+Bi9mfNCk/6V/ccvSn/qbmvzEn20qkzh2pl29iBJNH0oWFkNvV4hXRDZagxKD6uEb4z0uYHQn3KdzRoDgtSDSNTzE9emka9P4bYIKGVq3cRGXjFokp9pnuS9m2lHmi0Vsh9eKanhycFXUG5ufZL3Oam+XShMLrvpvLXA9tH4NWsFuYni1zPl8o6Ucsy59TIGAaXYuicnt17muwP99RHPKlPhonGu7VSD8BMYI4wquQONUaBJIBy/QqaGZBAorVj0Q1D+RCFqQ9hDLlmHKKiWGVjLC7Kqf8hHfkJE5QUsjaTaluLy3E8JN/Lg55yTAUVlfKosBDyLZw5rEHN/0wlc7Os+TcTVqoPqDfdU6UQikBepK; LtpaToken=mUIxkjVm8J0oNUSgEpXC6mH3I+THwqAyNwnUasjlhn2YbdbHGw+KT+eJOal7I2f9CUiQzLPVo/0gsrbgx0ZVQ5CRTOEyq7na0U+UMJ+hrBgml8aCc9E2uUQBKwV960RuLS1AorOlKcYOZtEsow0fKP4kYtd+TXwjgnoVJDvTHf0ARa5qrLLJZdAPeiyGNvv1EiyQWe2YBu4xCDhH00m/B7RVLvNlrN+56Z0RqiKQT8r8VcxSpQ7kbBsg/iTjyMRwZBuINnU867mCjgJqP+BMYx9JwoiE9Mpd8Z+v9CEUpZLjKPeytsmAtzdLD2SR38hCRoi2UkPI1Jfdmg3QY4OwUgnj0uv8HG9COkyHEvDWd0n9m0bYs1aifZ/p8MQwjZOI/ypyVhbm6tSMi8Xg8R3KxNI9sUngfWGELu5gnyqfp0em4GcswNBfRNIQUD7pCJ3nejo0tkkjdPdtcIqiIVhhwU9R53vTwPBj; indi_locale=zh-cn',
            'Host': 'www.mychery.com',
            'Origin': 'http://www.mychery.com',
            'Referer': 'http://www.mychery.com/wps/myportal/!ut/p/a1/pZJLb4JAFIV_i4suydx5wMwsR6wCpZKgpMKG8FSsIjakqf31hYaFbSJt09ncuck5k--eOyhCGxTVyWu1TdrqVCeHvo-MmBGT4SkQ1zPWGJS1cBzbl5Qv9U4QdgK4cRR89QtvKUBhaZC552MwYfCPCHq_R6TAFLArAqaDCu5XhmkK-rDG6AlFKMrqtml3KMx2xcvlDq5LnBdNe32P3_fp9z6W_StNVuUozDlOy7KkGuZFprGECS3lhdSIYKTAUnAd84F6BOuH1D6pO4m5UBbjbpcUEwTs2dSacfkIYBuDYCzY0WgCQGEHyW9SzDFa_XFq5xefodqfz5HqVnKq2-KtRZt_7KQ5BsFR0Iv27Aug-mGrJpMP43y3ow!!/dl5/d5/L2dBISEvZ0FBIS9nQSEh/',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest',
        }
        data = {
            'siteAreaId': 'chery_dept_zjb_9',
            'isAll': 'ALL',
            'start': '0',
            'end': '10',
            'pageNo': '1',
            'pageSize': '10',

        }
        auth = ('ch225253', '225253.cn')
        response = requests.post(url, data=data, headers=headers, auth=auth)
        if response.status_code == 200:
            return response.json()
        print('Error:', 'not 200')
        return None
    except RequestException as e:
        print('Error:', e.args)
        return None


def parse_page(json):
    #解析json
    if (json):
        items = json.get('rows')
        for item in items:
            cherynote = {}
            cherynote['attachment'] = item.get('attachment')
            cherynote['createDate'] = item.get('createDate')
            cherynote['creator'] = item.get('creator')
            cherynote['title'] = item.get('tfileitle')
            cherynote['url'] = item.get('url')
            yield cherynote


def download_file(json, headers, path):
    #对json中的pdf地址进行下载保存（注：下载地址get同样需要headers）
    for item in parse_page(json):
        downloadurl = 'http://www.mychery.com'+item['attachment']
        file = requests.get(downloadurl, headers=headers, stream=True)
        with open(path + item['title'] + '.pdf', "wb") as f:
            size = 0
            for chunk in file.iter_content(chunk_size=512):
                f.write(chunk)
                size += len(chunk)
            if(str(size) == file.headers['Content-Length']):
                print(item['title']+':Success,'+'size:' +
                      file.headers['Content-Length'])
            else:
                print(item['title']+':error,'+size +
                      '!='+file.headers['Content-Length'])


def main():
    headers = {
        'Cookie': 'DigestTracker=AAABb4Lzmkc; JSESSIONID=0000BATfwSfFt-lqb5vaX8060Nz:1a1vdtiv5; LtpaToken2=ZijBosJo7qik5wPGRWQcafg1oGq+/6Fs9pOvbm3N1cnSZFWbfBw+26c2dSi+7+guw4Aab6li/RYvtcrNM4mCzYUBwY1HIvf6Q5E4u61cAde9EzVzVZIkPKdXx7fOd8StYDj5Si8fX4oIJAuV1Oe2NeaSnVcmE+sbX4nZ48MihI/DjJd1VD3PLUXafJd5rk0Z5zLTnrnDwsfki1V/la4wCs/gAXiRyzOyJkXmIyYxz6aAQIryqDszA30A12fgZ8ZwaNdvyh9iDETFkmOLheSMhn+76DSQrCn47hdwsXfcjFOF3Ntt2gTLmY89Tju5rxXq5sLccyx7uDGPEgRMVPu5Vz6orDwy2aX+YF/dOP+qwqbHTEP5KBgdiJ2V8E9dLrvDuDPn34PCGXjRbRTu923wnM7GIafScZLNAyEz337IKpgjFWX5S29oNBXjUcdSafKtsUg/aVFMaJ2awq0E1N9+Bi9mfNCk/6V/ccvSn/qbmvzEn20qkzh2pl29iBJNH0oWFkNvV4hXRDZagxKD6uEb4z0uYHQn3KdzRoDgtSDSNTzE9emka9P4bYIKGVq3cRGXjFokp9pnuS9m2lHmi0Vsh9eKanhycFXUG5ufZL3Oam+XShMLrvpvLXA9tH4NWsFuYni1zPl8o6Ucsy59TIGAaXYuicnt17muwP99RHPKlPhonGu7VSD8BMYI4wquQONUaBJIBy/QqaGZBAorVj0Q1D+RCFqQ9hDLlmHKKiWGVjLC7Kqf8hHfkJE5QUsjaTaluLy3E8JN/Lg55yTAUVlfKosBDyLZw5rEHN/0wlc7Os+TcTVqoPqDfdU6UQikBepK; LtpaToken=mUIxkjVm8J0oNUSgEpXC6mH3I+THwqAyNwnUasjlhn2YbdbHGw+KT+eJOal7I2f9CUiQzLPVo/0gsrbgx0ZVQ5CRTOEyq7na0U+UMJ+hrBgml8aCc9E2uUQBKwV960RuLS1AorOlKcYOZtEsow0fKP4kYtd+TXwjgnoVJDvTHf0ARa5qrLLJZdAPeiyGNvv1EiyQWe2YBu4xCDhH00m/B7RVLvNlrN+56Z0RqiKQT8r8VcxSpQ7kbBsg/iTjyMRwZBuINnU867mCjgJqP+BMYx9JwoiE9Mpd8Z+v9CEUpZLjKPeytsmAtzdLD2SR38hCRoi2UkPI1Jfdmg3QY4OwUgnj0uv8HG9COkyHEvDWd0n9m0bYs1aifZ/p8MQwjZOI/ypyVhbm6tSMi8Xg8R3KxNI9sUngfWGELu5gnyqfp0em4GcswNBfRNIQUD7pCJ3nejo0tkkjdPdtcIqiIVhhwU9R53vTwPBj; indi_locale=zh-cn',
        'Host': 'www.mychery.com',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
    }
    url = 'http://www.mychery.com/wps/myportal/!ut/p/a1/pZFRb4IwFIV_yx72SHpbKm0fK06RMUkQovBCEGHiBuJClumvXzE8uCWgy_rS3uQ7zT3noAitUVQln8Vr0hSHKnlv58iIKTEpHgNxXMPHIK2Zbc89obPFSAGhAqDnSPip5-6Cg8TCIFPXw2BCpx8AWr1LBMc6YIcHdAQyeFoapsn1Zx-jFYpQlFZN3exQmO6yj9MjXF_xNqub63d83m9-z7Fof6nTYovCLcObPM91DbMs1WhCubZhmdAIpyTDgrMRZt3WA2vdlVqfPoBb-otrhZgzaVHmqKQpJzCfjK0JEy8Ac6MDhooZjDa4BSiToXLBetecYrT8Y6z2HbkV--MxkqrzQ9VkXw1a_6P0ugyCkuunQnvzrLOflyv58A1C-IKA/dl5/d5/L2dBISEvZ0FBIS9nQSEh/pw/Z7_42C41B02LO6T10AHGJJIR937F3/res/c=cacheLevelPage/=/?ACTION_NAME=searchContent'
    path = 'C:/Users/Administrator/Desktop/file/cherynote/'

    json = get_page(url)
    download_file(json, headers, path)


if __name__ == '__main__':
    main()
