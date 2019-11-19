import requests
import json
import time
import redis
import os
import pickle
from urllib.request import urlretrieve
from threading import Thread
from db import ConnectDB


def img_download(url, name='', dir_name=None):

    url = 'http' + url.split('http')[-1]
    name = name.replace('?', '')
    name = name.replace('\t', '')
    name = '{}-{}'.format(name,url.split('/')[-1])
    dir_path = os.path.abspath('.')
    dir_path = os.path.join(dir_path, 'images')
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    if dir_name:
        filename = os.path.join(dir_path, dir_name)
        if not os.path.exists(filename):
            os.makedirs(filename)
    else:
        filename = dir_path
    filename = os.path.join(filename, name)

    if not os.path.isfile(filename):
        print(filename, url)
        urlretrieve(url, filename)
        print('图片下载完成：', name)
    else:
        print('图片已存在：', name)


if __name__ == '__main__':
    c = ConnectDB()
    weibo_data = c.weibo_info_get(group_id=1)
    for d in weibo_data:
        author = d.get('author')
        img_urls = d.get('img_urls')
        if img_urls:
            img_urls = json.loads(img_urls)
            print(author, type(img_urls), img_urls)
            for url in img_urls.get('pic_ids', []):
                img_download(url, name='', dir_name=author)

