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
        print("正在初始化")

    # 自动重连
    def do_connect(self, host, port):
        # 创建 socket 对象
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            # 连接服务，指定主机和端口
            sock.connect((host, port))
            self.isOk = True
        except:
            pass
        return sock

    def send_msg(self):
        #global s
        while True:
            try:

                if self.isOk:
                    print("请输入你想发送的数据，回车结束：")
                    # hello = 'Hello' + "\r\n"
                    hello = input()
                    hello = hello + "\r\n"
                self.s.send(hello.encode('utf-8'))

            except socket.error:
                self.isOk = False
                print('\r\n网络错误，开始重连')
                # 推迟执行
                time.sleep(3)
                # 自动重连
                self.s = self.do_connect(self.host, self.port)

    def recever_msg(self):
        #global s
        End = "\r\n"
        buffer = []
        while True:
            try:
                total_data = []
                data = ''
                while True:
                    data = socket.recv(8192)
                    if End in data:
                        total_data.append(data[:data.find(End)])
                        break
                    total_data.append(data)
                    if len(total_data) > 1:
                        # check if end_of_data was split
                        last_pair = total_data[-2] + total_data[-1]
                        if End in last_pair:
                            total_data[-2] = last_pair[:last_pair.find(End)]
                            total_data.pop()
                            break
                print("Client开始写入文件")
                data = ''.join(buffer)  # join() 方法用于将序列中的元素以指定的字符连接生成一个新的字符串。
                with open('Client.txt', 'a') as f:
                    f.write(data)
                #print(msg.decode('utf-8'))
            except socket.error:
                self.isOk = False
                print('\r\n网络错误，开始重连')
                # 推迟执行
                time.sleep(3)
                # 自动重连
                self.s = self.do_connect(self.host, self.port)

            except IOError:
                print('\r\n写入文件错误')
                time.sleep(3)

            except:
                print('\r\n其他错误发生')
            time.sleep(1)

    def player(self, name):
        if name == 'send':
            self.send_msg()
        else:
            if name == 'recv':
                self.recever_msg()
            else:
                print('error: The format is not recognized!')


list = ['send', 'recv']
sockets = Client(socket.gethostname(), 9996)
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