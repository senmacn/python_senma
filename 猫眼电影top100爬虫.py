'''
抓取猫眼电影top100
保存为txt
2018/2/16 21.46
'''

import requests,json,re
from requests.exceptions import RequestException

headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400'

}

def get_one_page(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None

def get_infomation(text):
    patten = re.compile("<dd>[\s\S]+?title=(.+?)\"[\s\S]+?src=\"http(.+?)\"[\s\S]+?\"star\">([\s\S]+?)</p>[\s\S]+?"
                        +"\"releasetime\">([\s\S]+?)</p>[\s\S]+?integer\">([\s\S]+?)</i>.+?fraction\">([\s\S]+?)</i>")
    info = re.findall(patten,text)
    for item in info:
        yield {
            'name':item[0],
            "image":"http"+item[1],
            "stars":item[2].lstrip().strip(" "),
            "time":item[3][5:],
            "score":item[4]+item[5]
        }

def main(offset):
    url = 'http://maoyan.com/board/4?offset='+str(offset)
    text = get_one_page(url)

    with open("猫眼电影top100.txt", "a", encoding='utf-8') as f:
        for item in get_infomation(text):
            f.write(json.dumps(item,ensure_ascii=False)+'\n')
        f.close()

if __name__ == '__main__':
    for i in range(10):
        main(i*10)