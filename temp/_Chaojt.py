# -*- coding: utf-8 -*-
import requests
import re
import json

default_timeout = 10

class Chaojt():
    def __init__(self):
        self.header = { 
                    'Accept-Encoding': 'gzip',
                    'Connection': 'Keep-Alive',
                    'Host': 'tao.lexiangquan.com',
                    'User-Agent': 'com.lexiangquan.supertao/1.9.0 (Linux; U; Android 4.4.2; zh-cn)',
                    'Accept': 'application/json; q=0.5',
                    'X-CHANNEL': 'huawei',
                    'X-TIMESTAMP': '1509949382391',
                    'UA-INFO': 'kOjui4bT3xsG373erP2Sl7FgLCFAbvp5SEWJDzF81tDXyiAOkUSimbNkgz6G0RO5PKx59IrbfJDiGS4q8G/9Wp2D7fUcrFhlBEMkvXphIfpcS60GXqsvE99U/SWQ3bIuYBO0Jy5j2WvOdzEei3E4IO2b4YXjhAnLOM68iWdF2py81zd48uQ/q1colbUZT+b+VPUSj/SUj9fJNQMCjiRExw32bwJlGBs0a/pUxboeQFHT0t0knoxgVSGSz3p1I5tCGB4Bp6nf3ZXDH0yFM15/wA6M8jsY9o0KqxWnIOogpCnCzZQ8NNLEfJ99+spdcpVZc28UTnSRR8/tFSp81Rmc6vVa3h2D6Ay8gw9LF+Bb4MYFP0gU5ojN3zni/R8cmQKMpIbyqALDXzapGmc1xEfG3v2aHfDHKoDoo9alEfOOycmSB2x/FOrfS4K72Qq2IPcVo/q19u16FxWiQ33HrKK9dGN2iqxarloYgGSBP/gAeTnSzpZ/frgMvYBa3lijsquz/+Qy+yy+DgIbspOLjEdI5XgOKpdJ5Aue7wUFoFfg8lK6fH26hkonATaGR671tr/xO99bmiGn4Nc/UXFQRkplN0DVD1JPK+aN1XL+DnLVQ+ku6ospCSDnimWWArmYwENk+CY6vBjgn4qg6wMcSfDYTWSVpLyBFKgRKkTReoyUAqk=',
                    'X-CID': 'a251f10b37552d311adf5c425a23e5ab',
                    'X-TOKEN': '66dac11b0a9b39c108c0b95c507fa72e',
                    'X-M': 'm_37ba4060168cdc98fa3de07fc2566b94'
                    }
                 
    # 模拟 http 请求
    def httpRequest(self, method, action, query=None, urlencoded=None, callback=None, timeout=None):
        if (method == 'GET'):
            ## url = action if (query == None) else (action + '?' + query)
            connection = requests.get(action, headers=self.header, timeout=default_timeout, params=query)

        elif (method == 'POST'):
            connection = requests.post(
                action,
                data=query,
                headers=self.header,
                timeout=default_timeout
            )

        connection.encoding = "UTF-8"
        connection = json.loads(connection.text)
        return connection
                 
    # 登录
    def login(self, username, password):
        action = 'http://tao.lexiangquan.com/?act=login'
        data = {
            'm': username,
            'p': password,
            'ClientID': 'a151f10b37552d311adf5c425a23e5ab'
        }
        return self.httpRequest('POST', action, data)
        # try:
        #     return self.httpRequest('POST', action, data)
        # except Exception as e:
        #     print('except:', e)
        #     return {'code': 501}
            

CJT = Chaojt()

data = CJT.httpRequest('GET', 'http://tao.lexiangquan.com/?act=shake&op=index', '')
print(str(data))
print('=' * 50)

prizeId = str(data['data']['prizeInfo']['prizeId'])

print('prizeId=%s' % prizeId)
data = CJT.httpRequest('GET', 'http://tao.lexiangquan.com/?act=shake&op=receive&prize_id=' + prizeId, '')
print(str(data))
print('=' * 50)

# data = CJT.login('13656178592','chaojitao')
# if data['code']==0:
#     print('登录成功， Id：'+str(data['data']['uid']))
#     print(str(data))
#     print('=' * 50)

#     data = CJT.httpRequest('POST', 'http://tao.lexiangquan.com/?act=shake&op=index', '')
#     print(str(data))
#     print('=' * 50)
    

# else:
#     print('登录错误，错误Code：'+str(data['code']))
