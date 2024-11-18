import socket


print('server socket!')

# Exiting context manager is equivalent to calling close().
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.bind(('localhost', 8500))  # '' addr for any.
    soc.listen(5)
    # TODO: Add logic to actually handle 5 connections.
    c_soc, addr = soc.accept()
    print(f'Have client socket {c_soc} at {addr}.')
    c_soc.send('Hello from server!'.encode())
    while True:
        print(c_soc.recv(1028).decode())

