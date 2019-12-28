import requests
import re
from urllib.parse import urlencode
import time
url=input('请输入你想要的下载的基本url:')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36',
    'referer': 'https://www.zhihu.com/question/63727821',
    'cookie':'_zap=82db0d2d-d161-4ecd-b55e-b17bf86cfe90; d_c0="AMCi0vY_xQ-PTh98HfMCYbE8JkFGAx7V-P0=|1563715251"; _xsrf=i5BTsTolY1LdKrSrOlEyKV3HTKcmxfVU; z_c0=Mi4xaFFaVkVRQUFBQUFBd0tMUzlqX0ZEeGNBQUFCaEFsVk4yU0NtWGdEem8zeTFJdU94Smp3X0FGMktlcXRTZEUtU3Z3|1572393689|a5e9c1d3739682bd3a2bc443c419936e890c9902; q_c1=e62080fe706444faa3b2ce5e1bc9698f|1574840314000|1564904380000; tst=r; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1575035934,1575115419,1575270780,1575270793; tgw_l7_route=4860b599c6644634a0abcd4d10d37251; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1575271720'
    }
base_url=url
base_url=list(base_url.split('/'))
base_url.insert(3,'api')
base_url.insert(4,'v4')
base_url[5] ='questions'
base_url.append('answers?')
base_url[0] ='https:'
b =''
for i in range(len(base_url)):
    if i == 0:
        b = b + base_url[i] + '//'
    elif i > 1:
        b = b + base_url[i] + '/'
update_url = b.strip('/')
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36',
    'referer': 'https://www.zhihu.com/question/63727821'
}
n = 0
for offset in range(0,1000,5):
    params = {
        'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled,is_recognized,paid_info,paid_info_content;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics',
        'limit': '5',
        'offset': offset,
        'platform': 'desktop',
        'sort_by': 'default'
    }
    url = update_url + urlencode(params)  # 得到json数据的url
    response = requests.get(url, headers=headers)
    data = response.json()  # 将json模式的数据传给字典模式
    images = data.get('data')  ##得到data里的数据，列表模式
    for image in images:    #字典模式
        img = image.get('content')
        img_url = re.findall('data-actualsrc="(.*?)"', img, re.S)
        for i in img_url:
            response = requests.get(i, headers=headers).content
            # name=md5(response).hexdigest()
            file_path = 'G://知乎实践//{}.gif'.format(n)
            with open(file_path, 'wb') as f:
                f.write(response)
                print('第{}张图片下载完成'.format(n))
            time.sleep(1)
            n += 1
