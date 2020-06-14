import requests, random, json

import urllib.parse


class Music(object):
    def run(self, music_name, type_num, num):
        music_name_decode = urllib.parse.quote(music_name)
        types = {1: 'netease', 2: 'qq', 3: 'kugou', 4: 'kuwo', 5: 'ximalaya', 6: 'kg'}
        type_web = types.get(int(type_num))
        url = 'http://www.youtap.xin'
        headers = {
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'Connection': 'keep-alive',
            'Host': 'www.youtap.xin',
            'Origin': 'http://www.youtap.xin',
            'Sec-Fetch-Mode': 'cors ',
            'Referer': 'http://www.youtap.xin/?name={}&type={}'.format(music_name_decode, type_web),
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
            'X-Requested-With': 'XMLHttpRequest'
        }

        post_data = {
            'input': music_name,
            'filter': 'name',
            'type': type_web,
            'page': str(num)
        }

        res = requests.post(url, headers=headers, data=post_data)
        res_json = json.loads(res.text)
        datas = res_json['data']
        return datas


if __name__ == '__main__':
    music = Music()
    datas = music.run(music_name='不要说话', type_num=2, num=1)
    for data in datas:
        print(data)
        music_url = data['url']
        if music_url == None or music_url == 'http://None':
            pass
        else:
            author = data['author']
            title = data['title']
            music_title = author + '-' + title
            print(music_title)
            res = requests.get(music_url)
            music = res.content
            with open('./mp3/{}.mp3'.format(music_title), 'ab') as fd:
                fd.write(music)
