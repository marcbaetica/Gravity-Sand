import socket


print('client socket!')

# c_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conns = dict()
for i in range(1):
    print(f'connectin #{i}')
    conns[f'c_soc_{i}'] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conns[f'c_soc_{i}'].connect(('localhost', 9999))
    print(conns[f'c_soc_{i}'])
    print(conns[f'c_soc_{i}'].send('hi from client'.encode()))
    print(conns[f'c_soc_{i}'].recv(12).decode())
    print(conns[f'c_soc_{i}'].recv(12).decode())

