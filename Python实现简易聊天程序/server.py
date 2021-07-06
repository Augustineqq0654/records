import threading
import socket

def main():
    # 创建 TCP 服务器套接字
    tcp_server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # socket 的 gethostname 方法获得系统的主机名
    # 元组为 地址-端口号 元组，作为套接字的 bind 方法的参数
    # 端口号选择大于 1024 小于 65536 且未被占用的任意数值
    ADDR = (socket.gethostname(), 1234)
    # 绑定地址和端口号
    tcp_server_sock.bind(ADDR)
    # 启动监听，监听来自客户端发送的连接请求
    tcp_server_sock.listen()
    print('Waiting for connection')
    
    # 无限循环使得服务器套接字接收多个客户端请求
    while True:
        