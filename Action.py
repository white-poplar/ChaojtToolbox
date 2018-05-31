#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-6 23:43:32
# @Author  : poplar. (BYH5566#gmail.com)
# @Link    : http://white-poplar.github.io
# @Version : $Id$

import os
import traceback
import Chaojt
import time
import json
import random
import lib.Tool


def Retry(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs) or func(*args, **kwargs) or func(*args, **kwargs)
    return wrapper


class Action(Chaojt.Chaojt):

    # 摇红包
    def _receive_code(self, prize_id):
        '''
        领取红包
        '''
        res = self.session.get(
            self.base_url + 'act=shake&op=receive&prize_id=' + prize_id)
        data = json.loads(res.text)
        # 删除
        print(data)
        if data['code'] != 0:
            print('红包', time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime()), data['message'])
            lib.Tool.write_log(data)
            return False
        else:
            print('红包', time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime()), '领取成功(￣▽￣)~*')
            lib.Tool.write_log(str(data))
            return True

    def _gain_code(self):
        '''
        接收红包
        '''
        res = self.session.get(self.base_url + 'act=shake&op=index')
        data = json.loads(res.text)
        # 删除
        print(data)
        if data['code'] != 0:
            print('红包', time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime()), data['message'])
            lib.Tool.write_log(str(data))
            return False
        else:
            # 红包Id
            time.sleep(8)
            return self._receive_code(str(data['data']['prizeInfo']['prizeId']))

    def get_packet(self):
        '''
        获取红包 20min/次
        '''
        try:
            while True:
                time.sleep(random.randint(5, 15))
                # 删除
                print('GO-HB')
                self._gain_code()
                time.sleep(60 * 20)    # 20min
        except Exception as e:
            print("摇红包出错(；′⌒`)")
            lib.Tool.write_error_log("摇红包出错(；′⌒`)")
            lib.Tool.write_error_log(traceback.format_exc())

    # 拍小票
    def _check_code(self, brandId):
        '''
        是否已上传
        '''
        res = self.session.post(self.base_url + 'act=receipt&op=check', data={
            'brandId': brandId
        })
        data = json.loads(res.text)
        # 删除
        print(data)
        if data['code'] != 0:
            print('小票', time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime()), data['message'])
            lib.Tool.write_log(str(data))
            return False
        else:
            return True

    def _up_receipt(self, dirpath, filename, brandId):
        '''
        上传小票
        '''
        file = os.path.join(dirpath, filename)
        # 删除
        print(file)
        res = self.session.post(self.base_url + 'act=receipt', data={'brandId': brandId},
                                files={'file': ('image.jpeg', open(file, 'rb'), "image/jpeg")})
        data = json.loads(res.text)
        # 删除
        print(data)
        if data['code'] != 0:
            print('小票', time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime()), data['message'])
            lib.Tool.write_log(str(data))
            return False
        else:
            print('小票', time.strftime('%Y-%m-%d %H:%M:%S',
                                      time.localtime()), '上传成功(:◎)≡')
            lib.Tool.write_log(str(data))
            return True

    def _get_receipt(self, dirpath, brandId):
        '''
        获取小票
        '''
        if not lib.Tool.is_path_empty(dirpath):
            print('小票文件夹（%s）不存在或为空∮' % dirpath)
            lib.Tool.write_log('小票文件夹（receipts）不存在或为空∮')
            return

        # 获取目录下文件名列表
        for (root, dirs, files) in os.walk(dirpath, False):
            filename = files[random.randint(0, len(files) - 1)]

        print('选择小票，%s 卍' % filename)
        lib.Tool.write_log('选择小票，%s 卍' % filename)

        # 上传
        self._up_receipt(dirpath, filename, brandId)

    def up_receipt(self):
        '''
        上传小票 程序启动1h后执行一次
        '''
        try:
            time.sleep(random.randint(5, 15))
            # time.sleep(60*60)   # 1h
            # 删除
            print('GO-XP')
            if self._check_code(0):
                self._get_receipt('receipts', 0)

        except Exception as e:
            print("拍小票出错(；′⌒`)")
            lib.Tool.write_error_log("拍小票出错(；′⌒`)")
            lib.Tool.write_error_log(traceback.format_exc())
