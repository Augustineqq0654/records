import socket
import time

# 创建客户端套接字
tcp_client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 服务器套接字地址
addr = (socket.gethostname(), 1234)
# 使用客户端套接字的 connect 方法向服务器发送连接请求
tcp_client_sock.connect(addr)

# 向服务器发送四条数据，其中最后一个是断开连接的消息
for data in ['Michael', 'Tracy', 'Sarah', 'exit']:
    # 这里使用 time.sleep 方法挂起当前线程
    # 目的是为了让 for 循环发送的消息有一定的时间间隔，避免对方接收数据连在一起
    time.sleep(.1)
    # 注意数据格式为二进制，使用 encode 方法处理
    tcp_client_sock.send(data.encode())
    # 接收服务器发来的消息
    data = tcp_client_sock.recv(1024).decode()
    if data:
        print(data)
        continue
        
    tcp_client_sock.close()