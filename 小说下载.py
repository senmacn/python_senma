import requests,os.path,re
from tkinter import *
from bs4 import BeautifulSoup
from tkinter.messagebox import *
from tkinter.simpledialog import askstring
from tkinter.filedialog import *

startUrl = 'http://zhannei.baidu.com/cse/search?'

class dingdian_novel(Frame):
    def __init__(self):
        self.params = {'s': '5592277830829141693', 'entry': 1, 'q': None}
        self.info = [None,None]
        Frame.__init__(self)
        self.pack()
        Label(self,text='小说搜索器').pack(side=TOP,fill=X)
        Button(self,text='查询',command=self.get_books_info).pack(side=TOP,fill=X)
        Button(self,text='保存',command=self.save_in_position).pack(side=TOP,fill=X)
        Button(self,text='退出',command=self.Quit).pack(side=TOP,fill=X)
        mainloop()
    def get_save_position(self):
        return askdirectory()

    def get_books_info(self):
        bookName = askstring('查询','请输入您想要查询的小说的名称:')
        self.params['q'] = str(bookName)
        try:
            response = requests.get(startUrl,params=self.params)
            soup = BeautifulSoup(response.text,'html.parser')
            attr = soup.find('a', {'cpos': 'title'})
            self.info[0] = bookName
            self.info[1] = attr.get('href')
            showinfo('info','查询成功')
        except:
            showinfo('info','查询失败')

    def save_in_position(self):
        if self.info[0]:
            urls = []
            filePosition = os.path.join(self.get_save_position(),self.info[0]) + '.txt'
            for index in re.findall('<td.+?<a href="(.+?.html)">',requests.get(self.info[1]).text):
                urls.append(self.info[1] +index)
            with open(filePosition,'w',encoding='utf-8') as f:
                for url in urls:
                    target = requests.get(url)
                    target.encoding = 'gbk'
                    text = BeautifulSoup(target.text,'html.parser').select('#contents')[0].get_text()
                    f.write(text)
                showinfo('成功','这波咋呼')

        else:showwarning('捞的嘛','请您先查询!!!')

    def Quit(self):
        ans = askyesno('退出','真的要退出吗？')
        if ans:
            self.quit()
        else:
            showinfo('info','你再退一个试试？')

if __name__ == '__main__':
    dingdian_novel()