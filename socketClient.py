#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /mnt/d/pycodes/lxflearnpy/socketClient.py
# Project: /mnt/d/pycodes/lxflearnpy
# Created Date: Sunday, May 17th 2020, 4:45:11 pm
# Author: Sheng Liang
# -----
# Last Modified: Sun May 17 2020
# Modified By: Sheng Liang
# -----
# Copyright (c) 2020 Wu & Sheng
# 
# It will be better.
# Keep happy!
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 建立连接:
s.connect(('127.0.0.1', 9999))
# 接收欢迎消息:
print(s.recv(1024).decode('utf-8'))
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()
