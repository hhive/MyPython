#!/usr/bin/python3
# 文件名：client.py
 
# 导入 socket、sys 模块
import socket
import sys
import time
 
# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 
# 获取本地主机名
host = socket.gethostname()
 
# 设置端口好
port = 9998
 
# 连接服务，指定主机和端口
s.connect((host, port))
 
s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护

while True:
	hello = 'Hello'+ "\r\n"
	s.send(hello.encode('utf-8'))
	# 接收小于 1024 字节的数据
	while True:
		try:
			msg = s.recv(1024)
			#s.close()
			print (msg.decode('utf-8'))
		except socket.error:
			print ('\r\nsocket error,do reconnect')
			#推迟执行
			time.sleep(3)
			#自动重连
			s = doConnect(host,port)
		except:
			print ('\r\nother error occur ')
		time.sleep(1)