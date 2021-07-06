import socket

tcp_client_sock = socket.socket()
ADDR = (socket.gethostname(), 1234)
tcp_client_sock.connect(ADDR)
print('Linked')

while True:
    data = input('Input your message: ')
    if data and data != 'exit':
        tcp_client_sock.send(data.encode())
        recv_data = tcp_client_sock.recv(1024)
        if not recv_data or recv_data == 'exit':
            break
        print('Receive message:', recv_data.decode())
        continue
    break
    
