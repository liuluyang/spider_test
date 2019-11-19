


proxyHost = "http-dyn.abuyun.com"
proxyPort = "9020"
# 代理隧道验证信息
proxyUser = "H8P82770U1YHR33D"
proxyPass = "709100148FA6EF36"
proxyMeta = "http://%(user)s:%(pass)s@%(host)s:%(port)s" % {
    "host": proxyHost,
    "port": proxyPort,
    "user": proxyUser,
    "pass": proxyPass
}
proxies = {
    "http": '47.75.223.85:9001',
    "https": '47.75.223.85:9001'
}

import requests

headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
    #'cookie':'lastCity=101010100; _uab_collina=156355031870848334094638; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1563550319,1563551560; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1563551560; __c=1563551560; __g=-; __l=l=%2Fwww.zhipin.com%2F&r=https%3A%2F%2Fwww.so.com%2Fs%3Fie%3Dutf-8%26src%3Ddlm%26shb%3D1%26hsid%3D006c443fea89d257%26ls%3Dn08f4f9b899%26q%3Dboss; __a=50242003.1563550319.1563550319.1563551560.3.2.1.3'
    # 'cookie':'tgw_l7_route=a37704a413efa26cf3f23813004f1a3b; _xsrf=DvCX4Wma6P2pr85Q88BPEQQ2tJgNpkkF; _zap=ff6399be-519f-48c2-bb57-3de2a00db8cd; d_c0="AIDheR_Qwg-PTtIhzuePAbXa2skOUo9wp_c=|1563551715"; capsion_ticket="2|1:0|10:1563551715|14:capsion_ticket|44:MGJhMmUyZGYyOTdiNDEyYmExZTQ1ZjJiNjRmN2Q2Mzg=|93d792d4b87c228cb1356ff8c7a871969a1dfd314ab6b9eb766c334820735dbf"; l_n_c=1; q_c1=5c410fb18c734c07981db91d73a92e9c|1563551719000|1563551719000; r_cap_id="NzkwNWI3YmQ0ZGI3NDE1MDlkYWVmY2Y3Y2YwY2YxMWI=|1563551719|624fd9d47b01721d417ecb1f02295534c0d7e06a"; cap_id="ODBmZDE5Y2UxNDBjNDM3M2IyMTkzMDk5NGEyNjBhNjQ=|1563551719|4cb832b3ffe6dfb9d978772107bad045bbef21a5"; l_cap_id="NmQ2ZWQzNzA1N2ZmNDEyNjg4OGI4NWMyODk2OWY3Mzg=|1563551719|4ece993508d0a8ec65ab99a5f9a54af9fcf8b12b"; n_c=1; __utma=51854390.481263843.1563551716.1563551716.1563551716.1; __utmb=51854390.0.10.1563551716; __utmc=51854390; __utmz=51854390.1563551716.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmv=51854390.000--|3=entry_date=20190719=1'
}

r = requests.get('http://liuluyang.cn/polls/upload')
print(r, r.content.decode())
# with open('index_list.html', 'w', encoding='utf8') as f:
#     f.write(r.content.decode())
#
# print(r.headers)