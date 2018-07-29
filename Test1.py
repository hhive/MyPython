#!/usr/bin/python3
# 文件名：client.py

# 导入 socket、sys 模块
import socket
import sys
import time


# 自动重连
def do_connect(host, port):
    # 创建 socket 对象
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # 连接服务，指定主机和端口
        sock.connect((host, port))
    except:
        pass
    return sock


def main():
    # s.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1) #在客户端开启心跳维护
    # s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
    buffer = []
    End = '\r\n'
    # 获取本地主机名
    host = socket.gethostname()
    # host = 'www.sina.com.cn'
    # 设置端口
    port = 9998
    s = do_connect(host, port)
    s.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 10000, 3000))
    while True:
        try:
            # 接收小于 1024 字节的数据

            hello = 'Hello' + "\r\n"
            s.send(hello.encode('utf-8'))
            # 读取接收到的数据并写入文件
            print("Client开始读入数据")
            total_data = []
            data = ''
            while True:
                print("Client开始读入数据1")
                data = s.recv(1024).decode()
                print("Client开始读入数据2")
                if End in data:
                    print("Client开始读入数据2")
                    total_data.append(data[:data.find(End)])
                    break
                print("Client开始读入数据3")
                total_data.append(data)
            print("Client开始写入文件")
            data = ''.join(total_data)
            with open('Client.txt', 'a') as f:
                f.write(data)
            #print(msg.decode('utf-8'))

        except socket.error:
            print('\r\nsocket error,do reconnect')
            # 推迟执行
            time.sleep(3)
            # 自动重连
            s = do_connect(host, port)

        except IOError:
            print('\r\nwrite error')
            time.sleep(3)

        # except:
        #     print('\r\nother error occur ')
        time.sleep(1)


if __name__ == "__main__":
    main()
