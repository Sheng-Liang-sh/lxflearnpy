#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /mnt/d/pycodes/lxflearnpy/updClient.py
# Project: /mnt/d/pycodes/lxflearnpy
# Created Date: Sunday, May 17th 2020, 5:00:41 pm
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
for data in [b'Michael', b'Tracy', b'Sarah']:
    # 发送数据:
    s.sendto(data, ('127.0.0.1', 9999))
    # 接收数据:
    print(s.recv(1024).decode('utf-8'))
s.close()
