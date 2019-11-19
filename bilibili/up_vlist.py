import requests
import json
import time



def up_vlist_get(mid):
    """

    :param mid:
    :return:
    """
    url = 'https://api.bilibili.com/x/space/acc/info?mid={}&jsonp=jsonp'
    up_info = requests.get(url.format(mid)).json()
    if up_info['code'] == 0:
        data = up_info['data']
        print(data['mid'], data['name'], data['sex'], data['sign'], data['face'])
    else:
        print('up主信息获取失败')
        return False

    vlist_url = 'https://space.bilibili.com/ajax/member/getSubmitVideos?' \
                'mid={}&pagesize=100&tid=0&page={}&keyword=&order=pubdate'
    vlist_data = []
    page = 1
    while True:
        vlist = requests.get(vlist_url.format(mid, page)).json()['data']
        pages = vlist['pages']
        vlist_data.extend(vlist['vlist'])
        if page >= pages:
            break
        page += 1
    for index,d in enumerate(vlist_data):
        print(index, d)


if __name__ == "__main__":
    up_vlist_get('323401468')