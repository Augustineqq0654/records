import socket

tcp_server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
ADDR = (host, 1234)
tcp_server_sock.bind(ADDR)
tcp_server_sock.listen()
sock, addr = tcp_server_sock.accept()
print('Linked!')
data = sock.recv(1024).decode()

while data and data != 'exit':
    print('Receive message:', data)
    send_data = input('Input your message: ')
    sock.send(send_data.encode())
    if send_data == 'exit':
        break
    data = sock.recv(1024).decode()
    
sock.close()
tcp_server_sock.close()
print('End')
