import requests

proxy = {
    'http': 'http://112.85.171.44:9999/',
    #'https': '112.85.171.226:9999'
}
proxy_2 = {
    'http':'http://121.233.251.23:9999/'
}

url = 'http://47.75.223.85/polls/index'
url_2 = 'https://www.baidu.com'
r = requests.get(url, proxies = proxy_2)


print(r, r.text)