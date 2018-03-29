'''
天气查询(url = 'http://tianqi.sogou.com/beijing/')
python 3.6
'''
import requests,re

class the_weather(object):
    url = 'http://tianqi.sogou.com/beijing/15'
    day = []
    week = []
    weather = []
    tempreturn = []
    wind = []

    def get_html(self,url):
        headers = {'Cookie':'_umdata=65F7F3A2F63DF020566D87A7423AA047C8EF0E0D861BE25F798019594C0841DB3533DF5ECD50E747CD43AD3E795C914CBF0BB9577CCAE5A103915860F449100B; cna=Cwe2EFeDXC8CATzP7Qn2IM7Z; cnaui=2187674363; _uab_collina=151096810885002092177497; tcm=2wbxcSifOVItrMIBxiY/wKjXA7B1j6VwdDwmLR3v3/xpgpHMyF0nYIA5oEeI60wIsmk5VPti+hc=; _umdata=65F7F3A2F63DF020566D87A7423AA047C8EF0E0D861BE25F798019594C0841DB3533DF5ECD50E747CD43AD3E795C914CC1B866BD1C3C71E04E2445EA61FD4740; _lastvisited=Cwe2EFeDXC8CATzP7Qn2IM7Z%2C%2CCwe2EFeDXC8CATzP7Qn2IM7ZkYfdXluq%2Cjbrj1l61%2Cjbrj1l61%2C3%2Ce4949017%2CCwe2EFeDXC8CATzP7Qn2IM7Z',
                    'User-Agent':'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 53.0.2785.104Safari / 537.36Core / 1.53.4399.400QQBrowser / 9.7.12828.400'}
        try:
            acception = requests.get(url,headers=headers,timeout=10)
            acception.raise_for_status()
            acception.encoding = 'utf-8'
            return acception.text
        except:
            return "请求失败"

    def get_weather(self,html):
        myWeather.day = re.findall("td2[\s\S]+?<p class=\"p1\">(.+?)</p>",html)
        myWeather.week = re.findall("td2[\s\S]+?<p class=\"p2\">(.+?)</p>",html)
        myWeather.weather = re.findall("td3[\s\S]+?<div title=\"(.+?)\" class=",html)
        myWeather.tempreture = re.findall("td5[\s\S]+?<p class=\"p1\">(.+?)</p>",html)
        myWeather.wind = re.findall("td5[\s\S]+?<p class=\"p2\">(.+?)</p>",html)

if __name__=='__main__':
    myWeather = the_weather()
    html = myWeather.get_html(myWeather.url)
    myWeather.get_weather(html)
    print(myWeather.day, '\n', myWeather.week, '\n', myWeather.weather, '\n', myWeather.tempreture, '\n', myWeather.wind)
