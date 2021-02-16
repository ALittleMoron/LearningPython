import socket
import sys


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 8000)
print('Подключено к {} порт {}'.format(*server_address))
sock.connect(server_address)

try:
    mess = 'Hello Wоrld!'
    print(f'Отправка: {mess}')
    message = mess.encode()
    sock.sendall(message)
    
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        mess = data.decode()
        print(f'Получено: {data.decode()}')

finally:
    print('Закрываем сокет')
    sock.close()