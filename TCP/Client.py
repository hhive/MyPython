#!/usr/bin/python3
# 文件名：client.py
 
# 导入 socket、sys 模块
import socket
import sys
import time
 
 #自动重连
def doConnect(host,port):
	# 创建 socket 对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try :
    	# 连接服务，指定主机和端口
        sock.connect((host,port))
    except :
        pass
    return sock

def main():
	#s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护
	#s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
	buffer = []
	# 获取本地主机名
	host = socket.gethostname()
	#host = 'www.sina.com.cn'
	# 设置端口
	port = 9996
	s = doConnect(host,port)
	s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
	while True:
		try:
			# 接收小于 1024 字节的数据
			hello = 'Hello'+ "\r\n"
			s.send(hello.encode('utf-8'))
			#读取接收到的数据并写入文件
			print("Client开始读入数据")
			msg = s.recv(1024)   #接收小于1024字节的数据
			print(msg)
			if msg:
				buffer.append(msg.decode('utf-8'))
			else:
				print("Client数据读取完成")#？
				break
			print("Client开始写入文件")
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

if __name__ == "__main__":
	main()