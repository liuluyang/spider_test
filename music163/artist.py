import requests
import json
import time
import redis
import random
from scrapy.selector import Selector


headers_weixin = {
    'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'cookie':'JSESSIONID-WYYY=edl%2FxXZrX2mltkjS8kRcvUiGN7Z91aKs72A1Q%5CTKzm5%5C8zu%2FMRBQp%5CN%2FKsEVmyciZ6r4mCZrffd5iMqgENDp4MH%2B%2BnpyS6%5C4aC7QHbdXK%2BlH%5C7B4e1JeFoMmEOlFT66mMgqzV6CqUJshes4HOCCZYt%2FGQwSqKv8FQ3g1kuaqCTvPCTU6%3A1559708934317; _iuqxldmzr_=32; _ntes_nnid=277d63b62719025bdd916a6194206a61,1559707134406; _ntes_nuid=277d63b62719025bdd916a6194206a61; WM_NI=86SW6cromyVtK%2FTSnLJCo0B52KCl5N0Mtz5ZsUlimfkcNywks6EsoP%2BDnhUXc348yIpR3eofsr1kKi9cXOOYBDcBEaI5Qn0T%2FJG%2FkzwwP1PHF4D4GneObN4sCHBe1LjyY1k%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed1ca3395aa8587fb448b868fb6c45e829f9abbf262f3a9fd94dc68a8ebf7a2e62af0fea7c3b92afcea9db8b569b2b1a39ad58089f19cb4ed488a9da1d1c13ff2958d8db846f493bc9bb852b18ba48af06ea9bd829af661b1ea8b94ee5ce99ca289d854a1edfcd9fc43b48efd86ee6eb1aeff8cca63fbbd98b0ce53829cada3c86b8beb9f8fb360ed9689d0ea72b5a9a0d2d34486ec8cd5c666a791aeafb77981988e86b448aaa797d2ea37e2a3; WM_TID=7QE6t%2BivV95AERABFBcsnl1n4cwc49Qw; MUSIC_U=9de0b492647e46615f3abe7801cdbbe8aae296c499f9dcfc467fcb290f7461305bbfdc603a15d2d6f75141c171b8e054f71bf6af47ac8a4fe22a3b9787ab8578f2f513a9c38b5dc7; __remember_me=true; __csrf=f97bda7712c09a400e7d428020a749aa'
}

headers_qq = {
    'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'cookie':'JSESSIONID-WYYY=K%2Ba0Qv3DKUQErllkaowdkvj1JIh%2BsKEqfTd90hqfOalm1cDveMHTClsZa15wjrGtNk5Xo7dDgX4yJ8q%2FUuRzq5RAW%5CV9yqYfmkq%5CVdj0zVJ%2FXQtX2ucaA90xmjNFb0Iahxj%5CFMrVBpejn3II%5COPtu1FFDdvjm%5CADtuT1E6fSMdw3NqkW%3A1559709683989; _iuqxldmzr_=32; _ntes_nnid=777d2283057206a7cd0df4022cbf7c15,1559707884050; _ntes_nuid=777d2283057206a7cd0df4022cbf7c15; WM_NI=I1QOOHkciV%2F9b1Y%2FtmCRTEfZnxYgrTSbmNch9Nn2xusvYGLZHsDKQY9duEkoKw3E4bUfc%2Ft2IPQTd6CHu7Pij6kWgWLOcsPznpaDVYKMT0B2nvIYIvs0H3uxZxbO55R8cjU%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6b3418ce8ab89eb7b9a9e8ba6d15b979e9eaebb63a9b5fedaec6f8b91fbb0c92af0fea7c3b92a8bef9fb0ce44a9bda7b7ae33a2ef97d0f767818e9ca6e552aea89788f16091bea3afe264fb92a2d3fb7fb1aa97a8cf528cad8cacd453fbbcbba6ea6589a9fda6b76a97baadd0f73a8b909fb5e73e8198bbd8d363aaeaa5b8e65d9091ad94d372aeb0afa5d55389939cd1c13aaeaa87bacc7eb1f088d4f8749aa8aeb0b83f92e8ad8bd837e2a3; WM_TID=MHv7ffkEeltBAAEURBYsnxgj42eIK8OJ; MUSIC_U=f000ce7feb116c25685a526ef26df5a71d709536f57060643cd405df8c945538dfa4cad550a94393d87a7010ca3577102362b3a10153d56ce1443e85d9146c43ab95d95de4103765f2f513a9c38b5dc7; __remember_me=true; __csrf=8f36c5c16e76137d66825cb9ff9b4191'
}

headers_weibo = {
    'user_agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'cookie':'__guid=94650624.3066118144778431500.1559708075718.662; JSESSIONID-WYYY=dAFmb7H9VMbHaWznha66Un9YKDnnfsXi2JI1jl3RJc5AD7S7kDrvM1CWTKKf5UFA0gOBjvM8O8%5Cg2WHJIV%5CWtOkO4jUcBPlGylzcS2PqJXUQhxOij3CjUybD%5CBaZCqKTB0aMqC3dQ5hb5%2F0el6cJvD03Q92TG0HE9sEPDXmK7inn%2F2nX%3A1559709917076; _iuqxldmzr_=32; _ntes_nnid=ff223dfa4d92720be4824f89228a7d37,1559708117536; _ntes_nuid=ff223dfa4d92720be4824f89228a7d37; WM_NI=%2BHv5xdC%2BQVCZsDPaq5jlF5YxoWT8zYg0gS6kgtYBFe1tRtf%2BNI7aQApjm37ZGICb%2Bs9ScwSl4lYsIz45lJ6ZQ0RN3iRhHiR9IzrbD8RhfalcW55BE4OYiI9PyZ6kcf52Slk%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee83c9408894fa90f65283868aa2d15e969f9e85f263f3b9a3daf246f6b3a6d6c72af0fea7c3b92ae998bad6fb7081f59fb7c252b19ca082f43faab48ad6dc74ad899cd9f953a5f0a9b4b561a5ac97a3c56ff3ac9e95e5218e97f982d44bb4b6a3d4b65285978d83aa79fb8dad98d268f8b49794cc72f8eba4abb55293f09eafb26392b8888ad1338ba6be83c73492b8aa82ef6995ebfba3c8408d87a7aabc5cbb86fa8ce26ef7ee9d8dea37e2a3; WM_TID=DXih43lfJTREAFFRUENpnggnstYrnnpD; MUSIC_U=c3a472f2d095d7a2862ba4a26f16556089bd5619243090c7ccdaa0082080395946faee766b0bf2884920635ea3d3c9668bafcdfe5ad2b092; __remember_me=true; __csrf=5efbdcb4a17e887f339d326096707c2b'
}

headers_phone = {
    'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36 Edge/15.15063',
    'cookie':'JSESSIONID-WYYY=Ka6esfub83AVodeh39mi3BaQSoTWAexA%2FzcESBoMjGv%2Fusfh3eTK11mCNDRJJfi8fEWVkiKbso7xDbFVbDkw7%5CJ3T685iDNAprWeZd0loAhu0ltqD%2BTjXwcCI%2B%2FHYX2QAYI31tq%5CRaES7qR0JP6EWyxD1f6zCJSaxjg8%5CzCkhl4Pg5p1%3A1559710209309; _iuqxldmzr_=32; WM_NI=LeM44yNwACxDYclQsYdqBU5PQ4vt6VEZdYzT5u1UOB%2BjYIHVuSH92Ka5KS0MAHe5QJrnPkEOglPf5FbNlvDZNKQTDGWBLsEckg1YG5r2mbltfuXMMWyXsCnaCWRSFYfxcmc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee82cb4ff4e8aab4c946b79a8fa2c15e929e9faef362f4efa3d9f46ffcac829ac92af0fea7c3b92a90bb83d5b7738ea98fa4fb509bbda4b2f253a8af8eb6b85c93ecba95b55e8786acbaf960f7abffb6ce4ae9b697aacb5eb78d88dab141a3eb85b4b3478398abd6d442b2b2a08cc845a5b4a087b84ea292a497c7528e959fb5c74d959e8494c869a9b9ffbac63fb2eea383ef80a6ab98aed05dbb88bda4ed6b81899eb4c553a6a8ad8ee237e2a3; WM_TID=EEp2I6KzpGxEUUBVBEZ9yk03t%2Fb5pY2Y; MUSIC_U=8a9b68cbf3070e1e157aedba9ff1c41e0f67642b7e3500b31f66509434d40129fce9a13cab322f5e3385098816c634897955a739ab43dce1; __csrf=413f4c997605ac950546f21398306bdd; _ntes_nnid=d3044b8cf49e5dd6ed430b68c137658b,1559708409419; _ntes_nuid=d3044b8cf49e5dd6ed430b68c137658b'
}

headers = {
    'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36',
    'cookie':'JSESSIONID-WYYY=edl%2FxXZrX2mltkjS8kRcvUiGN7Z91aKs72A1Q%5CTKzm5%5C8zu%2FMRBQp%5CN%2FKsEVmyciZ6r4mCZrffd5iMqgENDp4MH%2B%2BnpyS6%5C4aC7QHbdXK%2BlH%5C7B4e1JeFoMmEOlFT66mMgqzV6CqUJshes4HOCCZYt%2FGQwSqKv8FQ3g1kuaqCTvPCTU6%3A1559708934317; _iuqxldmzr_=32; _ntes_nnid=277d63b62719025bdd916a6194206a61,1559707134406; _ntes_nuid=277d63b62719025bdd916a6194206a61; WM_NI=86SW6cromyVtK%2FTSnLJCo0B52KCl5N0Mtz5ZsUlimfkcNywks6EsoP%2BDnhUXc348yIpR3eofsr1kKi9cXOOYBDcBEaI5Qn0T%2FJG%2FkzwwP1PHF4D4GneObN4sCHBe1LjyY1k%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed1ca3395aa8587fb448b868fb6c45e829f9abbf262f3a9fd94dc68a8ebf7a2e62af0fea7c3b92afcea9db8b569b2b1a39ad58089f19cb4ed488a9da1d1c13ff2958d8db846f493bc9bb852b18ba48af06ea9bd829af661b1ea8b94ee5ce99ca289d854a1edfcd9fc43b48efd86ee6eb1aeff8cca63fbbd98b0ce53829cada3c86b8beb9f8fb360ed9689d0ea72b5a9a0d2d34486ec8cd5c666a791aeafb77981988e86b448aaa797d2ea37e2a3; WM_TID=7QE6t%2BivV95AERABFBcsnl1n4cwc49Qw'
}

headers_list = [headers_weixin, headers_qq, headers_weibo, headers_phone, headers]

def time_now():

    t = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    return t

def redis_connection():
    """
    连接redis
    :return:
    """
    pool = redis.ConnectionPool(host='47.75.223.85', port=6379, db=5, password='lvjian')
    r = redis.Redis(connection_pool=pool)

    return r

def artist_get(type_num, initial, redis):
    """
    获取歌手名字及ID（存入）
    :param type_num:
    :param initial:
    :param redis:
    :return:
    """
    time.sleep(0.5)
    try:
        url = 'https://music.163.com/discover/artist/cat?id={}&initial={}'.\
                format(type_num, initial)
        r = requests.get(url, headers=headers)

        resp = Selector(r)
        artist_name = resp.css('.sml .nm::text').extract()
        artist_id = resp.css('.sml .nm::attr(href)').extract()
        artist_id = [id.split('id=')[-1] for id in artist_id]
        print(artist_name, len(artist_name))
        print(artist_id, len(artist_id))
        for z in list(zip(artist_name, artist_id)):
            print(z)
            if not redis.sismember('artist_set', z[-1]):
                redis.lpush('artist_list', json.dumps(list(z)))
                redis.sadd('artist_set', z[-1])
    except Exception as e:
        print(e)

def redis_data_get(redis):
    """
    获取歌手名字及ID（取出）
    :param redis:
    :return:
    """
    data = redis.lrange('artist_list', 0, -1)
    data = [json.loads(d.decode()) for d in data]
    print('全部华语歌手及乐队：',data)

    return data

def song_get(artist_info, redis):
    """
    获取歌手的top50歌曲（存入）
    :param artist_info:
    :param redis:
    :return:
    """
    global headers_list
    name, artist_id = artist_info
    status = 404
    try:
        if not redis.sismember('artist_has_get_set', artist_id):
            url = 'https://music.163.com/artist?id={}'.format(artist_id)
            headers = random.choice(headers_list)
            r = requests.get(url, headers=headers)
            status = r.status_code

            resp = Selector(r)
            if '你要查找的网页找不到' in r.text:
                print('账户被封')
                headers_list.remove(headers)
                return
            data = resp.css('#song-list-pre-data::text').extract_first()
            if not data:
                print('该歌手暂无歌曲->', artist_info)
            else:
                try:
                    data = json.loads(data)
                except:
                    data = r.text.split('<textarea id="song-list-pre-data" style="display:none;">')[-1]
                    data = data.split('</textarea>')[0]
                    data = json.loads(data)
                data = [[d['name'], d['id']] for d in data]
                print(artist_info, data)
                data_dict = {'song_list':data, 'name':name,
                             'artist_id':artist_id, 'time_now':time_now()}
                redis.hset('artist_song_dict', artist_id, json.dumps(data_dict))
            redis.sadd('artist_has_get_set', artist_id)
            time.sleep(random.choice([1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]))
        else:
            print('已经抓取->',artist_info)
    except Exception as e:
        print(status, e)
        error = {'error_fun':'song_get', 'error':str(e),
                 'artist_info':artist_info, 'status':status, 'time_now':time_now()}
        redis.lpush('error_list', json.dumps(error))
        time.sleep(2)

    if not headers_list:
        print('帐号全部被封')
        error = {'error_fun': 'song_get', 'error': '帐号全部被封',
                 'artist_info': artist_info, 'status': status,
                 'time_now': time_now()}
        redis.lpush('error_list', json.dumps(error))
        raise ValueError('帐号全部被封')


if __name__ == '__main__':
    redis = redis_connection()
    print(redis)

    # for type_num in ['1001', '1002', '1003']:
    #     for abc in range(65, 91):
    #         artist_get(type_num, str(abc), redis)

    artist_has_get_set = redis.smembers('artist_has_get_set')
    artist_has_get_set = {a.decode() for a in artist_has_get_set}
    print('已抓取：', len(artist_has_get_set), artist_has_get_set)
    data = redis_data_get(redis)
    for d in data[:]:
        if d[-1] not in artist_has_get_set:
            song_get(d, redis)

    # song_get(['黄韵玲', '7893'], redis)
    # print(time_now())