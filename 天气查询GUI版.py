'''
天气查询 url:http://tianqi.sogou.com/
2018/3/3
by python 3.6
'''
import requests,re,sys
from tkinter import *
from tkinter.simpledialog import askinteger,askstring
from tkinter.messagebox import *

class myGui(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.city = ''
        self.time = 0
        self.pack()
        Label(self,text='天气查询').pack(side=TOP)
        Button(self,text='城市',command=self.Get_the_city).pack(side=TOP)
        Button(self, text='时间', command=self.Get_the_time).pack(side=TOP)
        Button(self,text='查询',command=self.search_weather).pack(side=TOP)
        Button(self,text='退出',command=self.to_quit).pack(side=TOP)

    def Get_the_city(self):
        self.city = askstring('city','please input the city which you want to know')
    def Get_the_time(self):
        self.time = askinteger('time','please input the time which you want to know')
    def to_quit(self):
        if askyesno('退出','你真的想要退出吗？'):
            sys.exit()
        else:
            showinfo('退出','太好了')
    def search_weather(self):
        if self.city and self.time:
            myWeather = the_weather(city=self.city, time=self.time)
            myWeather.request_weather()
            print(myWeather.get_weather())
        else:
            showerror('error','请输入正确的城市和时间')

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
    myGui().mainloop()

if __name__=='__main__':
    main()