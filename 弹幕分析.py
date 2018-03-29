'''
获取文章（弹幕）中的词组进行分析
python 3.6
'''
#! usr/bin/python
# #coding=utf-8
from matplotlib import pyplot as plt
def danmu_sort(danmux):
    danmuy = []
    for danmu in danmux:
        if len(danmu) >= 4:
            for i in range(len(danmu)-3):
                danmuy.append(danmu[i]+danmu[i+1]+danmu[i+2]+danmu[i+3])
    return danmuy

danmus = {}
danmux = []
with open("danmu.txt",'r',encoding="utf-8",newline="") as f:
    for line in f:
        danmux.append(line)

    danmux = danmu_sort(danmux)

    for danmu in danmux:
        if danmu not in danmus:
            danmus[danmu] = 1
        else:
            danmus[danmu] += 1
    f.close()


danmu_num = []
danmu_name = []
for key,value in danmus.items():
    if value>50:
        danmu_num.append(value)
        danmu_name.append(key)
        print(key,value)

plt.pie(danmu_num,labels=danmu_name,autopct='%1.1f%%')
plt.show()