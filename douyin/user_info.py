import requests
import json


"""
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Encoding: gzip, deflate, br
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0

Cookie: odin_tt=3e5ff79d99ffa7b92f59588b9023c30fefea6baeab13f78f22131b00384e812f867286e27baf2c4df7264108e5e6351bbe67a47b4cb5ff5bc28916259fbbbcc4; sid_guard=89eef67ab0b9432d9d789931f866b5a9%7C1559221518%7C5184000%7CMon%2C+29-Jul-2019+13%3A05%3A18+GMT; uid_tt=a438cf97f9c98d1d796dccf30b6ee7f3; sid_tt=89eef67ab0b9432d9d789931f866b5a9; sessionid=89eef67ab0b9432d9d789931f866b5a9; install_id=76156745162; ttreq=1$eb3980021e241651e931c0fc9aca0abe1c47d0e2; qh[360]=1
"""

url = 'https://api.amemv.com/aweme/v1/aweme/post/?max_cursor=1558168577000&user_id=55083947526&count=10&retry_type=no_retry&iid=76156745162&device_id=67855074473&ac=wifi&channel=smartisan&aid=1128&app_name=aweme&version_code=680&version_name=6.8.0&device_platform=android&ssmix=a&device_type=OE106&device_brand=SMARTISAN&language=zh&os_api=27&os_version=8.1.0&uuid=869096036932026&openudid=05ffdf917b567084&manifest_version_code=680&resolution=1080*2070&dpi=400&update_version_code=6802&_rticket=1561126165196&app_type=normal&js_sdk_version=1.16.3.0&mcc_mnc=46000&ts=1561126175&sec_user_id=MS4wLjABAAAAj82BIytr87RleLz0mL2hVSIjRQYF96O_rLosNnqG7bA'

headers = {
    'cookie':'odin_tt=3e5ff79d99ffa7b92f59588b9023c30fefea6baeab13f78f22131b00384e812f867286e27baf2c4df7264108e5e6351bbe67a47b4cb5ff5bc28916259fbbbcc4; sid_guard=89eef67ab0b9432d9d789931f866b5a9%7C1559221518%7C5184000%7CMon%2C+29-Jul-2019+13%3A05%3A18+GMT; uid_tt=a438cf97f9c98d1d796dccf30b6ee7f3; sid_tt=89eef67ab0b9432d9d789931f866b5a9; sessionid=89eef67ab0b9432d9d789931f866b5a9; install_id=76156745162; ttreq=1$eb3980021e241651e931c0fc9aca0abe1c47d0e2; qh[360]=1',
    'user_agent':'com.ss.android.ugc.aweme/680 (Linux; U; Android 8.1.0; zh_CN; OE106; Build/OPM1.171019.026; Cronet/58.0.2991.0)'
}

r = requests.get(url, headers=headers)
print(r.status_code)
print(r.json())
