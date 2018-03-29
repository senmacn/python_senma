import requests,os
from bs4 import BeautifulSoup

startPath = "D:\\Python"    #初始保存位置
startUrl = "http://www.meimeizi.com/category/bo-luo-she"
param = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4033.400 QQBrowser/9.6.12624.400",'Cookie':'cna=Cwe2EFeDXC8CATzP7Qn2IM7Z'}

def download(url,dir_path):    #储存
    try:
        file = open(dir_path,"wb")
        print("url --- On downloading")
        cont = requests.get(url,params=param).content
        file.write(cont)
        file.close()
    except:
        print('None')
soup = BeautifulSoup(requests.get(startUrl,params=param).text,"html.parser")
tags = soup.find_all("a",{"class":"zoom"})
soup2 = BeautifulSoup(requests.get(startUrl+"/page/2",params=param).text,"html.parser")
tags2 = soup.find_all("a",{"class":"zoom"})
urls = []

#得到所有urls
if tags != []:
    for tag in tags:
        urls.append(tag.get("href"))
    for tag in tags2:
        urls.append(tag.get("href"))
else:
    print("not found")

#建立文件夹储存
for url in urls:
    soup = BeautifulSoup(requests.get(url,params=param).text,"html.parser")    #第一页
    title = str(soup.select("#content > div.article_container.row.box > h1")[0]).strip("<h1>").strip("</h1>")    #标题
    pagestag = soup.select("#content > div.article_container.row.box > div.context > div.pagelist > a")    #找到所有页码
    photos = []
    for photo in soup.select("#post_content img"):
        photo = photo.get("src")
        photos.append(photo)
        print(photo)
    for tag in pagestag:
        tag = tag.get("href")
        soup = BeautifulSoup(requests.get(tag,params=param).text, "html.parser")
        for photo in soup.select("#post_content img"):
            photo = photo.get("src")
            photos.append(photo)
            print(photo)
    try:
        os.makedirs(startPath + "\\" + title)
    except:
        pass
    for photo in photos:
        path = startPath + "\\" + title + "\\" + str(photo)[-10:]
        download(photo,path)