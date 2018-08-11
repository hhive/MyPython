#!/usr/bin/python3
# 文件名：client.py

# 导入 socket模块
import socket
import time
import threading
import logging


class Client:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    isOk = True

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.s = self.do_connect(self.host, self.port)

        # 心跳检测
        self.s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))

    # 自动重连
    def do_connect(self, host, port):
        self.isOk = False
        # 创建 socket 对象
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        while not self.isOk:
            try:
                # 连接服务，指定主机和端口
                sock.connect((host, port))
                self.isOk = True
            except socket.error:
                print('\n网络错误，开始重连')
                time.sleep(3)
        return sock

    def send_msg(self):
        while True:
            if self.isOk:
                print("请输入你想发送的数据，回车结束：")
                # hello = 'Hello' + "\r\n"
                hello = input('>>')
                hello = hello + "\r\n"
                self.s.send(hello.encode())
            time.sleep(1)

    def receiver_msg(self):
        End = r'\r\n'
        while True:
            try:
                # 接收小于 1024 字节的数据
                # 读取接收到的数据并写入文件
                total_data = []
                print("\nClient读入数据准备")
                while True:
                    data = self.s.recv(1024).decode()
                    if End in data:
                        total_data.append(data[:data.find(End)])
                        break
                    total_data.append(data)
                print("\nClient开始写入文件")
                # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
                data = ''.join(total_data)
                with open('Client.txt', 'a') as f:
                    f.write(data)
            except socket.error:
                # 自动重连
                print("socket.error")
                self.s = self.do_connect(self.host, self.port)

            except IOError:
                print('\n写入文件错误')

            # except:
            #     print('\n其他错误发生')
            time.sleep(1)

    def mythread(self, name):
        if name == 'send':
            self.send_msg()
        else:
            if name == 'recv':
                self.receiver_msg()
            else:
                print('error: The format is not recognized!')


list = ['recv', 'send']
sockets = Client(socket.gethostname(), 9998)
files = range(len(list))
threads = []

# 创建线程
for i in files:
    t = threading.Thread(target=sockets.mythread, args=(list[i],))
    threads.append(t)

if __name__ == '__main__':
    # 启动线程
    for i in files:
        threads[i].start()