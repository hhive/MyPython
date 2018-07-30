#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
import socket
import sys
import time
import threading


class Client:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    isOk = True

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = self.do_connect(self.host, self.port)
        self.s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))

    # 自动重连
    def do_connect(self, host, port):
        self.isOk = False
        # 创建 socket 对象
        sock = self.s
        while not self.isOk:
            try:
                # 连接服务，指定主机和端口
                sock.connect((host, port))
                self.isOk = True
            except socket.error:
                print('\n网络错误，开始重连')
        return sock

    def send_msg(self):
        while True:
            if self.isOk:
                print("请输入你想发送的数据，回车结束：")
                # hello = 'Hello' + "\r\n"
                hello = input('>>\n')
                hello = hello + "\r\n"
                self.s.send(hello.encode())
            time.sleep(1)

    def recever_msg(self):
        End = '\r\n'
        while True:
            try:
                # 接收小于 1024 字节的数据
                # 读取接收到的数据并写入文件
                total_data = []
                data = ''
                print("Client开始读入数据")
                while True:
                    data = self.s.recv(1024).decode()
                    if End in data:
                        total_data.append(data[:data.find(End)])
                        break
                    total_data.append(data)
                print("Client开始写入文件")
                data = ''.join(total_data)  # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
                with open('Client.txt', 'a') as f:
                    f.write(data)
            except socket.error:
                # 自动重连
                self.s = self.do_connect(self.host, self.port)

            except IOError:
                print('\n写入文件错误')

            except:
                print('\n其他错误发生')
            time.sleep(1)

    def player(self, name):
        if name == 'send':
            self.send_msg()
            print("\n")
        else:
            if name == 'recv':
                self.recever_msg()
            else:
                print('error: The format is not recognized!')


list = ['recv', 'send']
sockets = Client(socket.gethostname(), 9998)
# sockets.send_msg()
# sockets.recever_msg()
# t1 = threading.Thread(target=sockets.send_msg())
# t2 = threading.Thread(target=sockets.recever_msg())
# t2.start()
# t1.join()
files = range(len(list))
threads = []

# 创建线程
for i in files:
    t = threading.Thread(target=sockets.player, args=(list[i],))
    threads.append(t)

if __name__ == '__main__':
    # 启动线程
    for i in files:
        threads[i].start()
    for i in files:
        threads[i].join()