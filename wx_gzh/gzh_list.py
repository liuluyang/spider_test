import requests
from scrapy.selector import Selector


base_url = 'https://weixin.sogou.com'

headers_weixin = {
            #'accept-encoding': 'gzip, deflate, br',
            #'Host': 'weixin.sogou.com',
            #'Referer': 'https://www.zhihu.com/',
            'Referer': 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=python&ie=utf8&_sug_=n&_sug_type_=',
            'Cookie':'SNUID=6304031C7673FDE789E3E11E76BE7E3A',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE', #必填
        #'cookie':'ABTEST=7|1560511535|v1; SNUID=F3E7FBE58F8A04C8694C6F0A8F0D5E70; IPLOC=CN1301; SUID=7D68756A2028940A000000005D03842F; __guid=14337457.1653876378889126000.1560511535090.3198; SUID=7D68756A1508990A000000005D038430; JSESSIONID=aaaChkk5ugGIl5So1Q3Qw; SUV=008FECF46A75687D5D0384344A2C0873; monitor_count=4'
        }
headers = {
            #'accept-encoding': 'gzip, deflate, br',
            #'Host': 'weixin.sogou.com',
            'Referer': 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=PC_-_PC&ie=utf8&_sug_=n&_sug_type_=',  #必填
            #'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
            # 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',  #必填
        #'Cookie':'SNUID=E5FFE2F2979D138FFA8307DC98F3972B' #必填
        'Cookie':'SNUID=6304031C7673FDE789E3E11E76BE7E3A'
        }
url = 'https://weixin.sogou.com'

url_2 = 'https://weixin.sogou.com/weixin?type=1&s_from=input&query=python&ie=utf8&_sug_=n&_sug_type_='

r = requests.session()

index_html = r.get(url_2)
# print(index_html)
# print(index_html.text)
# print(index_html.cookies)

cookies = {
    'SUV':'008FECF46A75687D5D0384344A2C0873',
    'SNUID':'F3E7FBE58F8A04C8694C6F0A8F0D5E70'
}

search_html = r.get(url_2, headers=headers_weixin)
print(search_html)
print(search_html.text)
html = Selector(search_html)
print(search_html.cookies)
print(search_html.headers)
#print(search_html.headers['set-cookie'])

href = html.xpath('//a[@uigs="account_name_0"]/@href').extract_first()
k = 55
h = 6+4+26+k
h = href[h]
other = '&k={}&h={}'.format(k, h)
href = base_url + href + other
# href = 'https://weixin.sogou.com/link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6EzDJysI4ql5MPrOUp16838dGRMI7NnPqJEw9EIStUnHnBE8An7tcDwwvDqyjOWdzKhkrIQmebKHlYhHkd3mspLTPGUm0OolGErK4Sq5xclsY1-mWDU6MeZnIzd3W_c8G6aCmBFFglcaq9-TF6aY1m_3Dxh0nHZgPa9uAx7VyD9aOiLZVSxHN3G4OZCnxixtX&type=1&query=python&k=49&h=n' #k,h参数是必填的 但整个url跟头信息没有必然联系
"""
疑问：
href链接是否长期有效
头信息有效期有多长
解答：
href链接长期有效，但是对应生成的微信公众号链接有期限，所以需要更新href.
浏览器cookie长时间有效，也就是头信息长期有效
"""

print(href)
#print(k, h, other)


gzh_html = r.get(href, headers=headers_weixin)
print(gzh_html)
print(gzh_html.text)
gzh_html = gzh_html.text

import re

pattern = re.compile(r"'(.*)'")
result = pattern.findall(gzh_html)
result = ''.join(result)  #公众号链接
print(result)


"""
GET /weixin?type=1&s_from=input&query=PC_-_PC&ie=utf8&_sug_=n&_sug_type_= HTTP/1.1
Host: weixin.sogou.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: CXID=9A3C842AF36174D2866FE9BA5D678EC2; ad=bkllllllll2t@TRvlllllV8@t2wlllllzXqI1kllll9llllljCxlw@@@@@@@@@@@; SUID=D269756A3865860A5CFF70D20004A05F; IPLOC=CN1301; SUV=1560263629831348; ABTEST=2|1560263639|v1; weixinIndexVisited=1; pgv_pvi=1753839616; SNUID=E5FFE2F2979D138FFA8307DC98F3972B; cd=1560486263&116f144858c01eae2a0428d3081a1cc0; ld=VZllllllll2t@@tagyGPgO1RwzBNlhVTzXqoKyllllylllljRklll5@@@@@@@@@@; sct=25; JSESSIONID=aaagMyIyhcltH-01iR3Qw

"""

"""
GET /link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6EzDJysI4ql5MPrOUp16838dGRMI7NnPqBslXCD4oW_GcFvuY98cx-gwvDqyjOWdzUkg8qZ5ASrPSFhC9qqo6j5gqjqzMNd-iO86XWqP18upFR7PM2eqVBlGbrRX2WvADQrKlSD0oQJEuZUpVCaaau9qSvWrDPLpKp6vlJoQxq9TsqyE1gXwNd2RTpLLTNgHY&type=1&query=PC_-_PC&k=75&h=Z HTTP/1.1
Host: weixin.sogou.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Referer: https://weixin.sogou.com/weixin?type=1&s_from=input&query=PC_-_PC&ie=utf8&_sug_=n&_sug_type_=
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: CXID=9A3C842AF36174D2866FE9BA5D678EC2; ad=bkllllllll2t@TRvlllllV8@t2wlllllzXqI1kllll9llllljCxlw@@@@@@@@@@@; SUID=D269756A3865860A5CFF70D20004A05F; IPLOC=CN1301; SUV=1560263629831348; ABTEST=2|1560263639|v1; weixinIndexVisited=1; pgv_pvi=1753839616; SNUID=E5FFE2F2979D138FFA8307DC98F3972B; cd=1560486263&116f144858c01eae2a0428d3081a1cc0; ld=VZllllllll2t@@tagyGPgO1RwzBNlhVTzXqoKyllllylllljRklll5@@@@@@@@@@; sct=25; JSESSIONID=aaagMyIyhcltH-01iR3Qw

"""

"""
GET /link?url=dn9a_-gY295K0Rci_xozVXfdMkSQTLW6EzDJysI4ql5MPrOUp16838dGRMI7NnPqr2EDBvaDflL1fAQvy07E8AwvDqyjOWdzUkg8qZ5ASrPSFhC9qqo6j5gqjqzMNd-iO86XWqP18upFR7PM2eqVBlGbrRX2WvADQrKlSD0oQJEuZUpVCaaau727RfLH1_wIym2cNVykdj6zvkmcbrUB2uO00efWrWmm&type=1&query=PC_-_PC&k=69&h=z HTTP/1.1
Host: weixin.sogou.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3
Referer: https://weixin.sogou.com/weixin?type=1&s_from=input&query=PC_-_PC&ie=utf8&_sug_=n&_sug_type_=
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.9
Cookie: CXID=9A3C842AF36174D2866FE9BA5D678EC2; ad=bkllllllll2t@TRvlllllV8@t2wlllllzXqI1kllll9llllljCxlw@@@@@@@@@@@; SUID=D269756A3865860A5CFF70D20004A05F; IPLOC=CN1301; SUV=1560263629831348; ABTEST=2|1560263639|v1; weixinIndexVisited=1; pgv_pvi=1753839616; SNUID=E5FFE2F2979D138FFA8307DC98F3972B; cd=1560486263&116f144858c01eae2a0428d3081a1cc0; ld=VZllllllll2t@@tagyGPgO1RwzBNlhVTzXqoKyllllylllljRklll5@@@@@@@@@@; sct=25; JSESSIONID=aaagMyIyhcltH-01iR3Qw

"""