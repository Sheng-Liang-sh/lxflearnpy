#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /mnt/d/pycodes/lxflearnpy/udpServer.py
# Project: /mnt/d/pycodes/lxflearnpy
# Created Date: Sunday, May 17th 2020, 4:58:08 pm
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

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 9999))

print('Bind UDP on 9999...')
while True:
    # 接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello, %s!' % data, addr)

