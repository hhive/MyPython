# coding=utf-8
# !/usr/bin/python3
# 文件名：server.py

# 导入 socket、sys 模块
import socket
import sys
import time

# 创建 socket 对象
server_socket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9998

# 绑定端口
server_socket.bind((host, port))
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE,
                         1)  # 在服务器端开启心跳维护value设置为1，表示将SO_REUSEADDR标记为TRUE，操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口。
# 设置最大连接数，超过后排队
server_socket.listen(5)

while True:
    # 建立客户端连接
    print("Server开始连接Client")
    client_socket, addr = server_socket.accept()  # 只连接一次所以只执行一次？
    # 发送数据
    print("连接地址: %s" % str(addr))
    print("Server开始发送数据")
    #msg = input() + "\r\n"
    msg = """运泰利自动化是致力于工业自动化产品的研制和开发、自动测试系统与各类五金模具、工装、测试治具的设计和制作，其自动化设备主要涵盖生产自动化、工厂自动化、过程控制、整体解决方案以及产品测试系统等领域。公司本着“满足客户需求，超越客户期望”的宗旨、“服务至上，质量第一”的原则，定位于为客户提供“高可靠、高品质的产品、最称心的服务”为目标，按客户的设备和工艺要求进行自动化系统的设计、安装和调试。提供自动化解决方案。
    运泰利自动化目前拥有各类进口和国产数控机床及专用设备30余台，汇集了一批国内优秀的产品研发专才、工程技术人员和服务队伍。其中中高级技术人员占百分之六十。并于2008年通过ISO9001：2000质量管理体系的认证。严格的管理制度保证了产品的高品质、高质量。以精湛的专业技术力量，为每一台出厂的设备提供最佳的品质保障。"""
    msg = msg + "\r\n"
    client_socket.send(msg.encode())
    # 接受数据
    print("Server开始接收数据")
    get = client_socket.recv(1024)
    print(get.decode('utf-8'))

    time.sleep(3)
