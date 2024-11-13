import socket


print('server socket!')

s_soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_soc.bind(('localhost', 9999))
s_soc.listen(1)

while True:
    client_soc, ret_address = s_soc.accept()
    print(client_soc, ret_address)
    print(type(client_soc), type(ret_address))

