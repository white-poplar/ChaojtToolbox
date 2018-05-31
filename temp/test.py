#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-6 23:21:21
# @Author  : poplar. (BYH5566#gmail.com)
# @Link    : http://white-poplar.github.io
# @Version : $Id$

import os
import random


if __name__ == '__main__':
    # print(os.listdir('../receipts'))
    file_names = []
    for (root, dirs, files) in os.walk('../receipts', False):
        file_names = files

    print(file_names)

    for (root, dirs, files) in os.walk('../receipts', False):
        print(root)  # 当前目录路径
        print(dirs)  # 当前路径下所有子目录
        print(files)  # 当前路径下所有非目录子文件
        print(files[random.randint(0, len(files) - 1)])
        filename = files[random.randint(0, len(files) - 1)]

    print('*' * 30)
    print(filename)
