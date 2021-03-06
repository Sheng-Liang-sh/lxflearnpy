#!/usr/bin/env python3
# -*- coding:utf-8 -*-
###
# File: /mnt/d/pycodes/lxflearnpy/socketServer.py
# Project: /mnt/d/pycodes/lxflearnpy
# Created Date: Sunday, May 17th 2020, 4:29:02 pm
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

import socket, threading, time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 监听端口
s.bind(('127.0.0.1', 9999))
s.listen(5)  # 最大连接数量
print('Waiting for connection......')

def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)

while True:
    # 接受一个新连接:
    sock, addr = s.accept()
    # 创建新线程来处理TCP连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()