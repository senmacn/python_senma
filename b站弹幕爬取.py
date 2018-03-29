'''
项目：b站弹幕爬取
encoding = 'utf-8'
by python 3
方式：访问bilibili api 获取弹幕cid re正则爬取
api：https://api.bilibili.com/x/player/pagelist?aid=(_)&jsonp=jsonp
弹幕地址：https://comment.bilibili.com/(__cid__).xml
注：出现 OSError: [Errno 22] Invalid argument: '",.txt' 为api未标注弹幕名称，正则匹配出现问题
'''

import requests,re
from requests.exceptions import RequestException

def get_one_page(url,params,headers):
    try:
        response = requests.get(url,params=params,headers=headers)
        if response.status_code == 200:
            return response.text
        else:
            return None
    except RequestException:
        return None

def get_chat_id(html):
    cids = re.findall("\"cid\":(.+?),",html)
    partName = re.findall("\"part\":\"(.+?)\"",html)
    return zip(partName,cids)

def get_chat(part,headers):
    chatUrl = 'https://comment.bilibili.com/' + part[1] + '.xml'
    html = requests.get(chatUrl,headers=headers).text
    with open(part[0]+'.txt','w',encoding='utf-8') as f:
        chats = re.findall("<d p=.+?>(.+?)</d>",html)
        for chat in chats:
            f.write(chat+'\n')
        f.close()

def main():
    startUrl = 'https://api.bilibili.com/x/player/pagelist?'
    params = {'aid': 0, 'jsonp': 'jsonp'}
    headers  = {'Cookie':'fts=1479480115; pgv_pvi=8739522560; rpdid=owiwislxildopqkpwsopw; HTML5PlayerCRC32=3055924696; _qddaz=QD.xhrk1j.5t5kiy.'
                         +'j4117gag; LIVE_BUVID=f9d74ea77afe6592e07ba2a8fa1e8eee; LIVE_BUVID__ckMd5=f415a6dc76240b60; UM_distinctid=15e4fce33611-0'
                          +'9b12be5f9020e-74147e73-100200-15e4fce336299; buvid3=08E4AE1E-FCFB-4A02-B2C5-4E03720C583C28558infoc; biliMzIsnew=1; '
                           +'biliMzTs=0; LIVE_PLAYER_TYPE=2; tma=136533283.76818350.1502545833770.1502545833770.1502545833770.1; tmd=2.136533283.'
                            +'76818350.1502545833770.; user_face=https%3A%2F%2Fi0.hdslb.com%2Fbfs%2Fface%2F790e29b7060ae27c7ba11a0ec9c1f3552ff681ea'
                             +'.jpg; _cnt_dyn=0; _cnt_pm=0; _cnt_notify=0; uTZ=-480; im_local_unread_9193162=0; im_seqno_9193162=8; im_notify_type_'
                              +'9193162=2; DedeUserID=9193162; DedeUserID__ckMd5=3d29b63c463d19fa; SESSDATA=24c539fc%2C1520171204%2C43217b85; bili'
                               +'_jct=0f3cbcc3020c97b1b7b4f6e6abf31b41; sid=8uc5gwg6; finger=7360d3c2; BANGUMI_SS_21464_REC=192290; BANGUMI_SS_5843_REC=193240;'
                                +' BANGUMI_SS_21554_REC=173187; BANGUMI_SS_21469_REC=173267; BANGUMI_SS_21466_REC=173254; BANGUMI_SS_21603_REC=183842; BANGUMI_'
                                 +'SS_21542_REC=173292; purl_token=bilibili_1519441244; pgv_si=s2795274240; CNZZDATA2724999=cnzz_eid%3D130604683-1479480113-nul'
                                  +'l%26ntime%3D1519449136; _dfcaptcha=9de8c5f3ab2e641f721b858286ccef65',
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             +'Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4549.400 QQBrowser/9.7.12900.400'}
    params['aid'] = input('请输入您想要提取弹幕的视频的aid号码：')
    html = get_one_page(startUrl,params,headers)
    for part in get_chat_id(html):
        get_chat(part,headers)

if __name__ == '__main__':
    main()