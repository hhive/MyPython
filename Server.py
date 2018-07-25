#!/usr/bin/python3
# 文件名：server.py
 
# 导入 socket、sys 模块
import socket
import sys
import time
 
# 创建 socket 对象
serversocket = socket.socket(
            socket.AF_INET, socket.SOCK_STREAM)
 
# 获取本地主机名
host = socket.gethostname()
 
port = 9998
 
# 绑定端口
serversocket.bind((host, port))
serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在服务器端开启心跳维护value设置为1，表示将SO_REUSEADDR标记为TRUE，操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口。
# 设置最大连接数，超过后排队
serversocket.listen(5)
 
while True:
    # 建立客户端连接
    clientsocket,addr = serversocket.accept()     
    print("连接地址: %s" % str(addr))
    msg='欢迎访问！'+ "\r\n"
    clientsocket.send(msg.encode('utf-8'))
    get = clientsocket.recv(1024)
    print(get.decode('utf-8'))
    time.sleep(3)

    #clientsocket.close()