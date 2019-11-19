import requests
import json
from scrapy.selector import Selector
import  time

BASE_URL = 'https://www.jianshu.com/'
headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }

data_set = set()


def text_parse(resp):
    global data_set
    response = Selector(resp)
    li = response.css('.note-list li')

    data = []
    for per in li:
        try:
            d = {}
            # data_id = per.css('li::attr(data-note-id)').extract_first()
            href = per.css('.title::attr(href)').extract_first()
            if href in data_set:
                continue
            title = per.css('.title::text').extract_first()
            desc = per.css('.abstract::text').extract_first()
            desc = desc.strip() if desc else None
            created_at = per.css('.time::attr(data-shared-at)').extract_first()
            created_at = created_at.replace('T', ' ')
            created_at = created_at.replace('+08:00', '')
            img = None
            try:
                img = per.css('.img-blur::attr(src)').extract_first()
            except:
                pass
            # print(href, title, desc, img)
            d = {
                'href':href, 'title':title, 'desc':desc, 'img':img, 'created_at':created_at
            }
            data.append(d)
            data_set.add(href)
        except Exception as e:
            print('内容解析错误:', e)

    return data


def article_list_get():
    base_url = 'https://www.jianshu.com/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }
    s = requests.session()
    resp = s.get(base_url, headers=headers)

    print(resp.status_code)
    print(resp.text)

    response = Selector(resp)

    li = response.css('.note-list li')
    print(li)
    id_list = []
    params = ''
    for per in li:
        print(per)
        data_id = per.css('li::attr(data-note-id)').extract_first()
        id_list.append(data_id)
        params += 'seen_snote_ids[]={}&'.format(data_id)
        href = per.css('a::attr(href)').extract_first()
        title = per.css('.title::text').extract_first()
        desc = per.css('.abstract::text').extract_first()
        print(data_id, href, title, desc)
    params += 'page=2'
    params = base_url + '?' + params
    print(params)
    # url = 'https://www.jianshu.com/trending_notes'
    # form_data = {
    #     'page':4,
    #     'seen_snote_ids[]':id_list
    # }
    # resp = s.post(url, data=form_data, headers=headers)
    # print(resp.status_code)
    # print(resp.json)
    headers = {
        'X-CSRF-Token':'V8ToZnnIex4bVWHq7JQD9FVfYIXrSUi4uvMiBoSVtwMOvNlCkosRSEqVuWMHw176qjvIdNQB/j4ayOekznFU4Q==',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    }

    resp = s.get(params, headers=headers)
    print(resp.status_code)
    # print(resp.text)
    text_parse(resp)


    pass


def user_article_get(u):
    """

    :param u:
    :return:
    """
    get_url = BASE_URL + 'u/{}?page={}'
    page = 1
    num = 0
    while True:
        # time.sleep(0.5)
        r = requests.get(get_url.format(u, page), headers=headers)
        page += 1
        print(r.status_code)
        #print(r.text)
        data = text_parse(r)
        if not data:
            break

        num += len(data)
        for d in data:
            print(d)
        print(num)


if __name__ == '__main__':
    # article_list_get()
    user_article_get('b3b2c03354f3')
    pass