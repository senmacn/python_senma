from selenium import webdriver
import time
import csv

#打开排行榜
startUrl = "https://www.bilibili.com/ranking?spm_id_from=333.334.banner_link.1#!/all/0/0/3/"
driver = webdriver.PhantomJS(executable_path="C:\\Users\\HDDEZB\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe")
driver.get(startUrl)
time.sleep(3)

#定位前100个视频url
elems = driver.find_elements_by_class_name("rank-item")
urls = []
dic = []

#定位url
for elem in elems:
    urls.append(elem.find_element_by_tag_name("a").get_attribute('href'))

#分别进入url获取信息
for i in range(2):
    info = []
    driver.get(urls[i])  # 进入视频
    time.sleep(3)
    title = driver.find_element_by_xpath("//*[@id='viewbox_report']/div[1]/div[1]/h1").get_attribute("title")
    kind = driver.find_element_by_css_selector("#viewbox_report > div.info > div.tminfo > span:nth-child(2) > a").text
    playNumber = driver.find_element_by_css_selector("#dianji").text
    info.append(title)
    info.append(kind)
    info.append(playNumber)
    dic.append(info)
driver.close()
#写入数据
csvfile = open("kan.csv",'w',newline="",encoding="UTF-16")
writer = csv.writer(csvfile)
for info in dic:
    writer.writerow(info)
csvfile.close()