import socket


print('client socket!')

# c_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conns = dict()
for i in range(10):
    print(f'connectin #{i}')
    conns[f'c_soc_{i}'] = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    conns[f'c_soc_{i}'].connect(('localhost', 9999))
    print(conns[f'c_soc_{i}'])

