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

buffer = []

def doConnect(host,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
        sock.connect((host,port))
    except :
        pass
    return sock

while True:

	hello = 'Hello'+ "\r\n"
	s.send(hello.encode('utf-8'))
	
	while True:

		try:
			#读取接收到的数据并写入文件
			msg = s.recv(1024)#接收小于1024字节的数据
			if msg:
				buffer.append(msg.decode('utf-8'))
			else:
				break
			data = ''.join(buffer)
			with open('Client.txt', 'a') as f:
    				f.write(data)
			print (msg.decode('utf-8'))

		except socket.error:
			print ('\r\nsocket error,do reconnect')
			#推迟执行
			time.sleep(3)
			#自动重连
			s = doConnect(host,port)

		except IOError:
			print('\r\nwrite error')
			time.sleep(3)

		except:
			print ('\r\nother error occur ')
		time.sleep(1)