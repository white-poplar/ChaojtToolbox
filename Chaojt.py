#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-6 23:43:32
# @Author  : poplar. (BYH5566#gmail.com)
# @Link    : http://white-poplar.github.io
# @Version : $Id$

import sys
import requests
import re
import json
import random
import time
import lib.Tool
import Global


# 超级淘
class Chaojt():
    def __init__(self):
        # 删除
        print("init")
        # 加载用户账号信息
        data_my = lib.Tool.load_setting_path('conf', 'my.ini')
        if data_my is None:
            print("程序退出中-_-|||")
            time.sleep(5)
            sys.exit()

        self.m = data_my['m']
        self.p = data_my['p']

        # 加载通用配置信息
        data_setting = lib.Tool.load_setting_path('conf', 'setting.ini')
        if data_setting is None:
            print("程序退出中-_-|||")
            time.sleep(5)
            sys.exit()

        self.ClientID = data_setting['X-CID']

        # 用户基础信息
        self.cid = ""
        self.uid = ""
        self.nickname = ""
        self.balance = ""
        self.mobile = ""
        self.avatar = ""
        self.cashAccount = ""
        self.cashRealName = ""

        self.base_url = "http://tao.lexiangquan.com/?"
        self.session = requests.session()
        self.session.headers.update(data_setting)

        self.session.cookies.update(
            {"PHPSESSID": "7u11c5fgb625he1u3c3mobst10", "path": "/"})

        self.username = self.get_username()
        # self.username = self.get_username() or self.get_username()

        if self.username is None:
            # return
            print("程序退出中-_-|||")
            time.sleep(5)
            sys.exit()

        print("登录用户：", self.username, self.mobile, self.balance)

    def check_login(self):
        '''
        是否登录
        '''
        res = self.session.get(self.base_url + 'act=m_home&op=info')
        if re.search("\"code\":0", res.text):
            return True
        return False

    def get_username(self):
        '''
        获取登录信息
        未登录执行登录操作
        '''
        res = self.session.get(self.base_url + 'act=m_home&op=info')
        data = json.loads(res.text)
        # 删除
        print(data)
        if data['code'] == 0:

            # 读取基础信息
            self.cid = str(data['data']['cid'])
            self.uid = str(data['data']['uid'])
            self.nickname = str(data['data']['nickname'])
            self.balance = str(data['data']['balance'])
            self.mobile = str(data['data']['mobile'])
            self.avatar = str(data['data']['avatar'])
            self.cashAccount = str(data['data']['cashAccount'])
            self.cashRealName = str(data['data']['cashRealName'])

            return str(data['data']['nickname'])
        else:
            # print("用户尚未登录！")
            # sys.exit()
            return self.user_login()

    def user_login(self):
        ''' 用户登录 '''

        print("用户登录中(*/ω＼*)")
        lib.Tool.write_log('用户登录中(*/ω＼*)' + '' + self.m)

        # 随机基础设置参数
        data_setting = lib.Tool.load_setting_path('conf', 'setting.ini')
        data_setting['User-Agent'] = random.choice(Global.USERAGENT)
        data_setting['X-CHANNEL'] = random.choice(Global.CHANNEL)

        # 统一设置为 1510298341778
        # _timestamp = str(time.time())
        # data_setting['X-TIMESTAMP'] = _timestamp[0:10] + _timestamp[11:14]

        self.ClientID = lib.Tool.cre_uuid('-')
        data_setting['X-CID'] = self.ClientID

        self.session = requests.session()
        self.session.headers.update(data_setting)

        res = self.session.post(
            self.base_url + 'act=login',
            data={
                'm': self.m,
                'p': self.p,
                'ClientID': self.ClientID
            })
        data = json.loads(res.text)
        # 删除
        print(data)
        if data['code'] == 0:
            print("登录成功(￢_￢)")
            lib.Tool.write_log('登录成功(￢_￢)' + ' ' + str(data['data']['uid']))

            # 更新 setting.ini
            data_setting['X-CID'] = self.ClientID
            data_setting['X-TOKEN'] = ''
            data_setting['X-M'] = str(data['data']['uid'])

            if not lib.Tool.modify_file('conf', 'setting.ini', json.dumps(data_setting)):
                print('咦，好像出错了，请火速联系白楊\(≧▽≦)/')
                sys.exit()

            self.session = requests.session()
            self.session.headers.update(data_setting)

            # 读取基本信息
            self.cid = str(data['data']['cid'])
            self.uid = str(data['data']['uid'])
            self.nickname = str(data['data']['nickname'])
            self.balance = str(data['data']['balance'])
            self.mobile = str(data['data']['mobile'])
            self.avatar = str(data['data']['avatar'])
            self.cashAccount = str(data['data']['cashAccount'])
            self.cashRealName = str(data['data']['cashRealName'])

            return str(data['data']['nickname'])
        else:
            print("登录失败●﹏●")
            lib.Tool.write_log(str(data))
            return None
