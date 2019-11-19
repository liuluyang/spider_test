
import requests
import json

# url = 'https://music.163.com/artist?id=5346'
# r = requests.get(url)
#
# print(r.text)


def comments_get(song_id):
    url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_{}?csrf_token='.format(song_id)
    form_data = {
        'params':'Hu40UopWTDSaPSFYAjwxV7K1UKRBaclOR6ULAZzvmoGSctqBB6aq3xWWHo6YjIYA2i/5KFuV2lG8jNNS/z7X5WN4etCC8242CVFWy9fD8ufxuLzrV8Bv16LOxoYhoyFItodd/u18sY/dABWTcQHh/A0pf7Q+T8X/enLGnCz2NxmSA7zOk/JQPxHcoZRgs7SS',
        'encSecKey':'d114a39f4e1fd59c92ec1b762f58a83409920f71529e39f25c334f9ac62a0470d7a36f28b2ce38dcd56db126363e16bf5659134ef863483866f70ca8bb685ca530ec8f6c0ddaa85d9298bba2ff6f6b69c6914e18403554b46eca4acd8aa5bb46ecf7a383aa3bbf85054f6a25a1ff6255073113b27d4e105eeda34cba518f0684'
    }
    r = requests.post(url, data=form_data).json()
    print(r)
    if r['code'] == 200:
        for c in r['hotComments']:
            print(c['content'])
            print('  '*len(c['content']), '--', c['user']['nickname'])


# form_data = {
#     'params':'jEgKis1hwN7BD8r+Kh70bTr7wzDyRT82uRHLNtzhZA4zoreDfm8uDSPcrJoq1KTajEfJnqCJPgukKXKhrDpPBsZtd4n5cjS3d55ZxQXDPlbDlLBjNdlEHC3UrbN9QUjI',
#     'encSecKey':'97493cee5b26f8eb10d382e15ce88349065ee0b7a7c6af7389e82736734fd3c52dfadca68326d3c3638de4162e68346ec8e5680a51c188c89f878776883157763ac28eace35a17105fee33b3b5888406e3f18fd5ffe2214b19fa435c97111d25965deef9d4e57389b605c565b34ea0261a9626d337d3b97597d02d75fd8dc354'
# }
# url = 'https://music.163.com/weapi/song/lyric?csrf_token='
# r = requests.post(url, data=form_data)
# print(r)
# print(r.json())


if __name__ == '__main__':
    comments_get('32408674')