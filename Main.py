#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2017-11-6 23:21:21
# @Author  : poplar. (BYH5566#gmail.com)
# @Link    : http://white-poplar.github.io
# @Version : $Id$

import traceback
import lib.Tool
from Action import Action
import time
import threading


def main():
    print("当前时间", time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))

    # 主功能
    action = Action()

    # 线程组
    threads = []

    # 摇红包
    t1 = threading.Thread(target=action.get_packet)
    threads.append(t1)

    # 拍小票
    t2 = threading.Thread(target=action.up_receipt)
    threads.append(t2)

    # 遍历启动线程
    for t in threads:
        # t.setDaemon(True)
        t.start()
    t.join()


if __name__ == "__main__":
    try:
        main()
        # pass
    except Exception as e:
        print("主程序出错(；′⌒`)")
        lib.Tool.write_error_log("主程序出错(；′⌒`)")
        lib.Tool.write_error_log(traceback.format_exc())
