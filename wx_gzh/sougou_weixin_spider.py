import requests
from scrapy.selector import Selector
from urllib.parse import urljoin
from lxml import etree
import re
import random
import json
import time


agents = [
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Chrome/4.0.249.0 Safari/532.5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US) AppleWebKit/532.9 (KHTML, like Gecko) Chrome/5.0.310.0 Safari/532.9",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/7.0.514.0 Safari/534.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/9.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/10.0.601.0 Safari/534.14",
    "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/11.0.672.2 Safari/534.20",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/12.0.712.0 Safari/534.27",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.24 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.120 Safari/535.2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/16.0.912.36 Safari/535.7",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US; rv:1.9pre) Gecko/2008072421 Minefield/3.0.2pre",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.10) Gecko/2009042316 Firefox/3.0.10",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-GB; rv:1.9.0.11) Gecko/2009060215 Firefox/3.0.11 (.NET CLR 3.5.30729)",
    "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6 GTB5",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; tr; rv:1.9.2.8) Gecko/20100722 Firefox/3.6.8 ( .NET CLR 3.5.30729; .NET4.0E)",
    "Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0a2) Gecko/20110622 Firefox/6.0a2",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:7.0.1) Gecko/20100101 Firefox/7.0.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:2.0b4pre) Gecko/20100815 Minefield/4.0b4pre",
    ]
BASE_URL = 'https://weixin.sogou.com'


def gzh_url_get(key_word='python'):
    """
    公众号链接获取
    :param key_word:
    :return:
    """

    headers = {
            #'Referer': 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=PC_-_PC&ie=utf8&_sug_=n&_sug_type_=',  #必填
            'User-Agent':random.choice(agents),
            #'Cookie':'SNUID=6304031C7673FDE789E3E11E76BE7E3A'
            }

    # 搜索结果获取
    search_url = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query={}&ie=utf8&_sug_=n&_sug_type_='.format(key_word)
    search_resp = requests.get(search_url, headers=headers)
    cookie = search_resp.headers['set-cookie']
    headers['Referer'] = search_url
    headers['Cookie'] = cookie

    #
    # html = Selector(search_resp)
    # href = html.xpath('//a[@uigs="account_name_0"]/@href').extract_first()

    html = etree.HTML(search_resp.content.decode('utf8'))
    href = html.xpath('//a[@uigs="account_name_0"]/@href')[0]
    k = int(random.random()*100)
    h = href[6+4+26+k]
    other_params = '&k={}&h={}'.format(k, h)
    href = BASE_URL + href + other_params        # 加密链接

    # 公众号链接获取
    gzh_html = requests.get(href, headers=headers)
    gzh_html = gzh_html.text

    pattern = re.compile(r"'(.*)'")
    result = pattern.findall(gzh_html)
    result = ''.join(result)  #公众号链接
    print(result)

    return result, headers


def gzh_article_list_get(url, headers):
    """
    公众号文章列表获取
    :param url:
    :return:
    """
    r = requests.get(url, headers=headers)
    print(r)
    content = r.content.decode('utf8')
    print(content)
    # with open('gzh_list.html', 'w', encoding='utf8') as f:
    #     f.write(content)

    # html = etree.HTML(content)
    # article_list = html.xpath('//div[@class="weui_msg_card"]')
    # print(article_list)
    # for article in article_list:
    #     print(article)
    content = content.split('var msgList =')[-1].\
        split('seajs.use("sougou/profile.js");')[0].strip()[:-1]
    content = json.loads(content)

    data = {}
    data_list = content['list']
    for d in data_list:
        app_msg = d.get('app_msg_ext_info')
        if not app_msg:
            continue
        # print(app_msg['title'], app_msg['content_url'], app_msg['cover'])
        data[app_msg['fileid']] = {
            'title': app_msg['title'], 'content_url': app_msg['content_url'],
            'cover': app_msg['cover']
        }
        for m in app_msg.get('multi_app_msg_item_list', []):
            # print(m['title'], m['content_url'], m['cover'])
            data[m['fileid']] = {
                'title': m['title'], 'content_url': m['content_url'],
                'cover': m['cover']
            }
    for article in data.items():
        content_url = article[-1]['content_url']
        url = urljoin(url, content_url).replace('amp;', '')
        # print(url)
        data[article[0]]['url'] = url
        print(article)


if __name__ == '__main__':
    url, headers = gzh_url_get()
    gzh_article_list_get(url, headers)
    pass
