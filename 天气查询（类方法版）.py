'''
天气查询 url:http://tianqi.sogou.com/
2018/3/3
by python 3.6
'''
import requests,re

class the_weather(object):
    startUrl = 'http://tianqi.sogou.com/' #目标站点

    def __init__(self,city,time=15):
        '''
        :param city: 输入希望查询天气的城市的拼音
        :param time: 输入查询的时间段，int类型，<=15，默认为15天
        weather：网站返回的信息，保存为list
        '''
        self.city = city
        self.url = the_weather.startUrl + str(city) + '/15'
        self.time = time
        self.weather = []

    def request_weather(self):
        try:
            acception = requests.get(self.url,timeout=10)
            acception.raise_for_status()
            acception.encoding = 'utf-8'
            html = acception.text
        except:
            return "请求失败"
        days = re.findall("td2[\s\S]+?<p class=\"p1\">(.+?)</p>",html)
        weeks = re.findall("td2[\s\S]+?<p class=\"p2\">(.+?)</p>",html)
        weathers = re.findall("td3[\s\S]+?<div title=\"(.+?)\" class=",html)
        tempretures = re.findall("td5[\s\S]+?<p class=\"p1\">(.+?)</p>",html)
        self.weather = [i for i in zip(days,weeks,weathers,tempretures)]

    def get_weather(self):
        return self.weather[0:self.time]

def main():
    city = input('请输入需要查询天气的城市的拼音：\n')
    time = int(input('请输入需要查询的时间段：\n'))
    myWeather = the_weather(city=city,time=time)
    myWeather.request_weather()
    print(myWeather.get_weather())

if __name__=='__main__':
    main()